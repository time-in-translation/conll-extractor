import os
import unittest

from prepositions.extract import process_single

class TestPrepositions(unittest.TestCase):
    def test_extract(self):
        data_dir = 'tests/data'
        in_file = os.path.join(os.getcwd(), data_dir, 'de_gsd-ud-test.conllu')
        cmp_file = os.path.join(os.getcwd(), data_dir, 'prepositions.csv')
        tmp_file = os.path.join(os.getcwd(), data_dir, 'tmp.csv')

        process_single(in_file, tmp_file)

        with open(tmp_file, 'r') as tmp:
            with open(cmp_file, 'r') as cmp:
                self.assertListEqual(tmp.readlines(), cmp.readlines())

        os.remove(tmp_file)
