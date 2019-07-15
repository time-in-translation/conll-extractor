# -*- coding: utf-8 -*-

import csv
import os

import click
import pyconll

from .data import PREPOSITIONS, DETERMINERS, FILTER_PREP
from ..core.utils import to_xml_id, to_tokens, convert_filename

POS_ARTICLE = 'ART'
POS_NOUN = 'NN'


def process_single(in_file, out_file, needs_determiner=True, filter_prepositions=False):
    with open(out_file, 'w') as f:
        w = csv.writer(f)
        w.writerow(['chapter', 'preposition', 'determiner', 'noun', 'extract'])

        sentences = pyconll.load_from_file(in_file)

        for sentence in sentences:
            s = []
            results = []
            current_head = None
            current_det = None
            current_token = None
            current_token_id = None

            for token in sentence:
                s.append(token.form)

                if token.form in PREPOSITIONS:
                    # if token.form in CONTRACTED:
                    current_token = token.form
                    current_token_id = token.id
                    current_head = token.head

                if needs_determiner:
                    if current_head is not None and token.head == current_head \
                            and token.xpos == POS_ARTICLE and token.form in DETERMINERS:
                        current_det = token.form

                current_det_filled = current_det is not None or not needs_determiner
                current_head_filled = current_head is not None and token.id == current_head and token.xpos == POS_NOUN

                if current_head_filled and current_det_filled:
                    results.append({'prep': current_token,
                                    'det': current_det,
                                    'noun': token.lemma,
                                    'sentence': sentence.id,
                                    'start': to_xml_id(sentence.id, current_token_id),
                                    'end': to_xml_id(sentence.id, token.id)})
                    current_head = None
                    current_det = None
                    current_token = None

            for result in results:
                preposition = result.get('prep')
                determiner = result.get('det')
                noun = result.get('noun')
                start = result.get('start')
                end = result.get('end')

                if not filter_prepositions or check_filter(preposition, noun):
                    w.writerow([os.path.basename(in_file),
                                preposition,
                                determiner,
                                noun,
                                to_tokens(end, start)])


def check_filter(preposition, noun):
    return preposition in FILTER_PREP and noun in FILTER_PREP[preposition]
