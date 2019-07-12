# -*- coding: utf-8 -*-

import argparse
import csv
import os

import pyconll

from prepositions.data import PREPOSITIONS, DETERMINERS, FILTER_PREP
from core.utils import to_xml_id


def process_single(in_file, out_file, needs_determiner=True):
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
                            and token.xpos == 'ART' and token.form in DETERMINERS:
                        current_det = token.form

                current_det_filled = current_det is not None or not needs_determiner
                current_head_filled = current_head is not None and token.id == current_head and token.xpos == 'NN'

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
                if result.get('prep') in FILTER_PREP and result.get('noun') in FILTER_PREP[result.get('prep')]:
                    w.writerow([os.path.basename(in_file),
                                result.get('prep'),
                                result.get('det'),
                                result.get('noun'),
                                '-t {} {}'.format(result.get('start'), result.get('end'))])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_in', help='Input file')
    parser.add_argument('file_out', help='Output file')
    parser.add_argument('-d', '--needs_determiner', action='store_false', help='Do we need a determiner?')
    args = parser.parse_args()

    process_single(args.file_in, args.file_out, args.needs_determiner)
