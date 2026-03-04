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