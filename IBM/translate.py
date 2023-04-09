from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Замените значения YOUR_APIKEY и YOUR_URL на ваши учетные данные
api_key = '3HLPjtdJ6b7j-m6KMJ5ja9V1Vzye4EFheWzlBfAwygTQ'
url = 'https://api.us-east.language-translator.watson.cloud.ibm.com/instances/cfcfe476-a522-43cb-845b-797d57825676'

authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2021-09-30', authenticator=authenticator)
language_translator.set_service_url(url)
