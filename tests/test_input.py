import pandas.errors

import app.io.input as inp
import unittest

class TestReadFile(unittest.TestCase):
    def test_file(self):
        result = inp.read_file('tests/file_tests/file.txt')
        self.assertEqual(result, 'This test should be easy')

    def test_empty_file(self):
        result = inp.read_file('tests/file_tests/empty.txt')
        self.assertEqual(result, '')

    def test_multi_string_file(self):
        result = inp.read_file('tests/file_tests/multi_line.txt')
        self.assertEqual(result, 'This\ntest\nalso\nshould\nbe\nok')

class TestReadFilePandas(unittest.TestCase):
    def test_file(self):
        result = inp.read_file_with_pandas('tests/pandas_file_tests/file.txt', ' ')
        self.assertEqual(result, '101   Petrenko 25   Kyiv\n102  Sydorenko 25   Kyiv\n103 Shevchenko 15 Dnipro')

    def test_csv_file(self):
        result = inp.read_file_with_pandas('tests/pandas_file_tests/csv_formatted.txt')
        self.assertEqual(result, '201 Ivanchuk     Kyiv\n202  Fedoriv     Lviv\n203   Kuchma Uzhhorod')

    def test_table_format(self):
        result = inp.read_file_with_pandas('tests/pandas_file_tests/wrong_format.txt', ' ')
        self.assertRaises(pandas.errors.ParserError)