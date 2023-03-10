"""Unittests for Translator.py"""

import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):

    """Tests English to French translation"""

    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french(' '), ' ')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

class TestFrenchToEnglish(unittest.TestCase):

    """Tests French to English translation"""

    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english(' '), ' ')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

unittest.main()
