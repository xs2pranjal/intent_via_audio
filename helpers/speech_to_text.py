import io
import os
from docs.config import GOOGLE_CRED

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

class SpeechToText():

    os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', GOOGLE_CRED)

    def __init__(self):
        self.__client = speech.SpeechClient()

    def convert(self, file_path):

        # Loads the audio into memory
        with io.open(file_path, 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)

        config = types.RecognitionConfig(encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
                                         sample_rate_hertz=16000,
                                         language_code='en-US')

        # Detects speech in the audio file
        response = self.__client.recognize(config, audio)


        for result in response.results:
            return ('{}'.format(result.alternatives[0].transcript))


# if __name__ == "__main__":
#     file_name = os.path.join(os.path.dirname(__file__),
#                             'data',
#                             'result.raw')
#     SpeechToText().convert(file_name)