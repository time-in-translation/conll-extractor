# -*- coding: utf-8 -*-

import os
import unittest

from ..nouns.extract import process_single


class TestDefinites(unittest.TestCase):
    def test_extract(self):
        data_dir = 'conll_extractor/tests/data'
        in_file = os.path.join(os.getcwd(), data_dir, 'en_partut-ud-test.conllu')
        cmp_file = os.path.join(os.getcwd(), data_dir, 'plural-nouns-object.csv')
        tmp_file = os.path.join(os.getcwd(), data_dir, 'tmp.csv')

        process_single(in_file, tmp_file, deprel='obj', number='Plur')

        with open(tmp_file, 'r') as tmp:
            with open(cmp_file, 'r') as cmp:
                self.assertListEqual(tmp.readlines(), cmp.readlines())

        os.remove(tmp_file)
