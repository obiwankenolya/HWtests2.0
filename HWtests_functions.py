import unittest
from functions import *
from unittest.mock import patch


class TestFunctions(unittest.TestCase):

    def test_get_document_owner(self):
        with patch('functions.input', return_value="11-2") as test_user_input:
            func_result = get_document_owner(documents)
        for person in documents:
            if test_user_input in person:
                self.assertEqual(documents.index(func_result), documents.index(person))
        if test_user_input not in documents:
            self.assertEqual(func_result, None)

    def test_get_documents_info(self):
        func_result = get_documents_info(documents)
        self.assertEqual(len(documents), len(func_result))

    def test_get_shelf_number_by_document_number(self):
        with patch('functions.input', return_value="11-2") as test_user_input:
            func_result = get_shelf_number_by_document_number(directories)
        for shelf, document in directories.items():
            if test_user_input in document:
                self.assertEqual(func_result, directories.index(shelf) + 1)

    def test_add_document_and_shelf(self):
        a = len(documents)
        b = len(directories)
        len_shelf_1 = len(directories['1'])
        len_shelf_2 = len(directories['2'])
        len_shelf_3 = len(directories['3'])
        with patch('functions.input', return_value='1''2''3''4'):
            add_document_and_shelf()
        self.assertEqual(len(documents), a + 1)
        if len(directories) == b:
            if len_shelf_1 < len(directories['1']):
                self.assertEqual(len_shelf_1 + 1, len(directories['1']))
            elif len_shelf_2 < len(directories['2']):
                self.assertEqual(len_shelf_2 + 1, len(directories['2']))
            elif len_shelf_3 < len(directories['3']):
                self.assertEqual(len_shelf_3 + 1, len(directories['3']))
        else:
            self.assertEqual(b + 1, len(directories))

    def test_main(self):
        with patch('functions.input', return_value="p") as test_user_input:
            func_result = main()
        if test_user_input is 'p':
            with patch('functions.input', return_value="11-2"):
                func_result1 = get_document_owner(documents)
                self.assertEqual(func_result, func_result1)
        with patch('functions.input', return_value="l") as test_user_input:
            func_result = main()
        if test_user_input is 'l':
            self.assertEqual(func_result, get_documents_info(documents))
        with patch('functions.input', return_value="s") as test_user_input:
            func_result = main()
        if test_user_input is 's':
            with patch('functions.input', return_value="11-2"):
                func_result1 = get_shelf_number_by_document_number(directories)
                self.assertEqual(func_result, func_result1)
        with patch('functions.input', return_value="a") as test_user_input:
            func_result = main()
        if test_user_input is 'a':
            with patch('functions.input', return_value='1''2''3''4'):
                func_result1 = add_document_and_shelf()
                self.assertEqual(func_result, func_result1)
        else:
            self.assertEqual(func_result, None)


if __name__ == '__main__':
    unittest.main()
