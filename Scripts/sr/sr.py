import json
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('')
service = SpeechToTextV1(authenticator=authenticator)
service.set_service_url('')


with open("chunk0000.wav", 'rb') as audio_file:
    print(json.dumps(service.recognize(audio=audio_file, content_type='audio/wav').get_result()))





