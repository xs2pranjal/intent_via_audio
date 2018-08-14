from google.cloud import texttospeech
from docs.config import DATA_DIR, GOOGLE_CRED
import os

class TextToAudio():

    os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', GOOGLE_CRED)

    def __init__(self):
        self.__client = texttospeech.TextToSpeechClient()

    def synthesize_text(self,text):
        """Synthesizes speech from the input string of text."""

        input_text = texttospeech.types.SynthesisInput(text=text)

        # Note: the voice can also be specified by name.
        # Names of voices can be retrieved with client.list_voices().
        voice = texttospeech.types.VoiceSelectionParams(language_code='en-US',
                                                        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

        audio_config = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3)

        response = self.__client.synthesize_speech(input_text, voice, audio_config)

        # The response's audio_content is binary.
        save_path = os.path.join(DATA_DIR, 'output.mp3')
        with open(save_path, 'wb') as out:
            out.write(response.audio_content)
        print('Audio content written to file "%s"' %save_path)