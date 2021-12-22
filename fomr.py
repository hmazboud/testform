from azure.core.exceptions import ResourceNotFoundError
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient
import time

def extract_id_field_value(id_card, field_name):
    try:
        print(field_name)
        print('-'*25)
        print('Field Value: {0}'.format(id_card.fields.get(field_name).value))
        print('__________________________________________________')
    except AttributeError:
        print('Nothing returned')

API_KEY = '1ed171c29c074898b17b43b84ce5b874'
ENDPOINT = 'https://boo.cognitiveservices.azure.com/'
form_recognizer_client = FormRecognizerClient(ENDPOINT, AzureKeyCredential(API_KEY))

driver_license_url = 'https://gray-kolo-prod.cdn.arcpublishing.com/resizer/5Gp4BHAD5XTGGPRAAvXetQAu3YY=/1200x675/smart/filters:quality(85)/cloudfront-us-east-1.images.arcpublishing.com/gray/KUKKLVRFP5BKJLNLGH2NWSEPRA.jpg'
poller = form_recognizer_client.begin_recognize_identity_documents_from_url(driver_license_url)

time.sleep(10)

if poller.status() == 'succeeded':
    result = poller.result()
    field_names = result[0].fields.keys()
    for form in result:
        for field_name in field_names:
            extract_id_field_value(form, field_name)
