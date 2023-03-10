"""This module translates from French to English
   or English to French
   using IBM Watson LanguageTranslatorV3"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(
    'kQg2x7HU93nHKQ37bf9Nkid-IToC6CnplRlpDZdwHgNz')
language_translator = LanguageTranslatorV3(
    version ='2018-05-01',
    authenticator = authenticator
)

language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/df6b9a3c-bd91-4fe8-b687-f60f8754a79c')

def english_to_french(english_text):

    """Translates English text to French text"""

    translation = language_translator.translate(
        text = english_text, model_id = 'en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):

    """Translates French text to English text"""

    translation = language_translator.translate(
        text = french_text, model_id ='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
