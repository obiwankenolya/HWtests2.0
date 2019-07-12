import unittest
import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

text = 'hi'


def translate_it(from_lang, to_lang):

    params = {
        'key': API_KEY,
        'text': f'{text}',
        'lang': f'{from_lang}-{to_lang}'
        }
    resp = requests.get(URL, params=params)
    translation = resp.json()['text'][0]

    return translation


class TestTranslator(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_translation(self):
        self.assertEqual(translate_it('en', 'ru'), 'привет')

    def test_code(self):
        params = {
            'key': API_KEY,
            'text': f'{text}',
            'lang': 'en-ru'
        }
        resp = requests.get(URL, params=params)
        resp_json = resp.json()
        self.assertEqual(resp_json['code'], 200)

    @unittest.expectedFailure
    def test_wrong_arg(self):
        self.assertRaises(KeyError, translate_it('lalala', 'ru'))

    @unittest.expectedFailure
    def test_too_many_args(self):
        self.assertRaises(TypeError, translate_it('en', 'ru', 'es'))


if __name__ == '__main__':
    unittest.main()
