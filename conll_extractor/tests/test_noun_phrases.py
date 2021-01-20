# -*- coding: utf-8 -*-

import os
import unittest

from ..core.constants import DEFINITE, INDEFINITE
from ..noun_phrases.extract import process_single


class TestDefinites(unittest.TestCase):
    def test_extract(self):
        data_dir = 'conll_extractor/tests/data'
        in_file = os.path.join(os.getcwd(), data_dir, 'en_partut-ud-test.conllu')
        cmp_file = os.path.join(os.getcwd(), data_dir, 'definites.csv')
        tmp_file = os.path.join(os.getcwd(), data_dir, 'tmp.csv')

        process_single(in_file, tmp_file, definiteness=DEFINITE)

        with open(tmp_file, 'r') as tmp:
            with open(cmp_file, 'r') as cmp:
                self.assertListEqual(tmp.readlines(), cmp.readlines())

        os.remove(tmp_file)


class TestIndefinites(unittest.TestCase):
    def test_extract(self):
        data_dir = 'conll_extractor/tests/data'
        in_file = os.path.join(os.getcwd(), data_dir, 'en_partut-ud-test.conllu')
        cmp_file = os.path.join(os.getcwd(), data_dir, 'indefinites.csv')
        tmp_file = os.path.join(os.getcwd(), data_dir, 'tmp.csv')

        process_single(in_file, tmp_file, definiteness=INDEFINITE)

        with open(tmp_file, 'r') as tmp:
            with open(cmp_file, 'r') as cmp:
                self.assertListEqual(tmp.readlines(), cmp.readlines())

        os.remove(tmp_file)
