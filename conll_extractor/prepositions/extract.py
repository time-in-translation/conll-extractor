# -*- coding: utf-8 -*-

import csv
import os

import pyconll

from .data import CONTRACTED, FILTER_CONTRACTED, PREPOSITIONS, DETERMINERS, FILTER_PP
from ..core.utils import to_xml_id, to_tokens

POS_ARTICLE = 'ART'
POS_NOUN = 'NN'


def process_single(in_file, out_file, contracted=False, filter_pps=False):
    with open(out_file, 'w') as f:
        w = csv.writer(f)
        w.writerow(['chapter', 'preposition', 'determiner', 'noun', 'extract'])

        sentences = pyconll.load_from_file(in_file)
        forms = CONTRACTED if contracted else PREPOSITIONS
        needs_determiner = not contracted

        for sentence in sentences:
            s = []
            results = []
            current_head = None
            current_det = None
            current_token = None
            current_token_id = None

            for token in sentence:
                s.append(token.form)

                if token.form in forms:
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

                if not filter_pps or check_filter(contracted, preposition, noun):
                    w.writerow([os.path.basename(in_file),
                                preposition,
                                determiner,
                                noun,
                                to_tokens(end, start)])


def check_filter(contracted, preposition, noun):
    f = FILTER_CONTRACTED if contracted else FILTER_PP
    return preposition in f and noun in f[preposition]
