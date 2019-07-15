# -*- coding: utf-8 -*-

import csv
import os

import click
import pyconll

from core.utils import to_xml_id, to_tokens, convert_filename

POS_NOUN = 'NOUN'
POS_DETERMINER = 'DET'
FORMS_DETERMINER = ['a', 'an']


def process_single(in_file, out_file):
    with open(out_file, 'w') as f:
        w = csv.writer(f)
        w.writerow(['chapter', 'found', 'from-to'])

        sentences = pyconll.load_from_file(in_file)

        for sentence in sentences:
            results = []
            current_head = None
            current_token_id = None
            current_s = []

            for token in sentence:
                if token.form in FORMS_DETERMINER and token.upos == POS_DETERMINER:
                    current_token_id = token.id
                    current_head = token.head
                    current_s = []

                if current_head:
                    current_s.append(token.form)

                current_head_filled = current_head and token.id == current_head and token.upos == POS_NOUN

                if current_head_filled:
                    results.append({'full': ' '.join(current_s),
                                    'start': to_xml_id(sentence.id, current_token_id),
                                    'end': to_xml_id(sentence.id, token.id)})
                    current_head = None
                    current_token_id = None
                    current_s = []

            for result in results:
                full = result.get('full')
                start = result.get('start')
                end = result.get('end')
                w.writerow([os.path.basename(in_file), full, to_tokens(end, start)])


@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def process_files(files):
    for in_file in files:
        out_file = convert_filename(in_file)
        process_single(in_file, out_file)


if __name__ == '__main__':
    process_files()
