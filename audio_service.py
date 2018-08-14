import os
import argparse
from helpers.speech_to_text import SpeechToText
from helpers.text_to_audio import TextToAudio
from src.intent_service import IntentService
from docs.config import DATA_DIR

class TTS():
    def __init__(self):
        self.__client = TextToAudio()

    def text_to_mp3(self, text):
        return self.__client.synthesize_text(text)

class Intent():
    def __init__(self, top_n):
        self.__client = IntentService(top_n)

    def fetch_nearest_categ(self, text):
        return self.__client.get_default_category(text)

class STT():
    def __init__(self):
        self.__client = SpeechToText()

    def fetch_text(self, file_path):
        return self.__client.convert(file_path)


if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Parameters")

        parser.add_argument('-t',
                            '--type',
                            type=str,
                            help='Type of operation to perform, i.e. Finding intent from a audio file or converting text to audio',
                            choices=["intent", "tts"],
                            required=True)

        parser.add_argument('-f',
                            '--file_path',
                            type=str,
                            help='Path of the input file',
                            default= "",
                            required=False)

        parser.add_argument('-n',
                            '--top_n',
                            type=int,
                            help='The top n count of intents addressed in a file',
                            default=4,
                            required=False)

        args = parser.parse_args()

        type = args.type
        file_path = args.file_path
        top_n = args.top_n

        if type == "intent":
            if file_path == "":
                file_path = os.path.join(DATA_DIR, 'sample.mp3')

            text = ""
            ext = os.path.splitext(file_path)[1]

            if ext == ".mp3":
                raw_path = os.path.splitext(file_path)[0] + '.raw'
                os.system('sox %s -r 16000 %s'%(file_path,raw_path))

                if os.path.exists(raw_path):
                    text = STT().fetch_text(raw_path)
                else:
                    raise Exception("Audio input has not been converted to raw file, please install sox, and re-run")

            elif ext == ".txt":
                with open(file_path,'r') as text_file:
                    text = text_file.read()

            nearest_categ = Intent(top_n).fetch_nearest_categ(text)
            print("Nearest Categories: \n")
            print(nearest_categ)

        elif type == "tts":

            if file_path == "":
                file_path = os.path.join(DATA_DIR, 'sample.txt')

            text = ""

            try:
                with open(file_path) as text_file:
                    text = text_file.read()
                TTS().text_to_mp3(text)
            except:
                raise Exception("Unable to read txt file, please try with a valid text file")

        else:
            print ("Invalid type")