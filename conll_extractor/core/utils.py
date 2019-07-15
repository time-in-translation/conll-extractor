# -*- coding: utf-8 -*-

import os


def to_xml_id(sentence_id, word_id):
    return 'w{}.{}'.format(sentence_id[1:], word_id)


def to_tokens(end, start):
    return '-t {} {}'.format(start, end)


def convert_filename(f):
    return os.path.join(os.path.dirname(f), os.path.basename(f).replace('.conllu', '.csv'))
