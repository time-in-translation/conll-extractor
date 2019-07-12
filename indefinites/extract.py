# -*- coding: utf-8 -*-

import csv
import os

import click
import pyconll

from core.utils import to_xml_id

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
                w.writerow([os.path.basename(in_file),
                            result.get('full'),
                            '-t {} {}'.format(result.get('start'), result.get('end'))])
                #w.writerow(['-t {} {}'.format(result.get('start'), result.get('end'))])


@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def process_files(files):
    for f in files:
        out_file = os.path.join(os.path.dirname(f), os.path.basename(f).replace('.conllu', '.csv'))
        process_single(f, out_file)


if __name__ == '__main__':
    process_files()
