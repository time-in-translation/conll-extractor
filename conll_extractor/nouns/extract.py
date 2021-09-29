# -*- coding: utf-8 -*-

import csv
import os

import pyconll

from ..core.utils import to_xml_id, to_tokens

POS_NOUN = 'NOUN'
POS_DETERMINER = 'DET'
LEMMATA_DEFINITE = ['the']
LEMMATA_INDEFINITE = ['a', 'an']


def process_single(in_file, out_file, deprel=None, number=None):
    sentences = pyconll.load_from_file(in_file)
    results = []
    for sentence in sentences:
        for token in sentence.to_tree():
            result = check_token(sentence, token, deprel, number)
            if result:
                results.extend(result)

    with open(out_file, 'w') as f:
        w = csv.writer(f)
        w.writerow(['chapter', 'found', 'from-to'])
        for result in results:
            full = result.get('full')
            start = result.get('start')
            end = result.get('end')
            w.writerow([os.path.basename(in_file), full, to_tokens(end, start)])


def check_token(sentence, token, deprel, number):
    results = []
    if has_properties(token.data, deprel, number):
        result = get_children(token)
        result.append(token.data)
        result.sort(key=lambda x: int(x.id))
        results.append({'full': ' '.join([r.form for r in result]),
                        'start': to_xml_id(sentence.id, result[0].id),
                        'end': to_xml_id(sentence.id, result[-1].id)})
    else:
        for child in token:
            results.extend(check_token(sentence, child, deprel, number))
    return results


def has_properties(token, deprel, number):
    correct = token.upos == 'NOUN'
    if deprel:
        correct &= token.deprel == deprel
    if number:
        correct &= number in token.feats.get('Number', [])
    return correct


def get_children(token):
    result = []
    for child in token:
        result.append(child.data)
        result.extend(get_children(child))
    return result
