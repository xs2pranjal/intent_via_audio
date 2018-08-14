# PYTHON Intent Identification with audio input

## Getting Started

This application can be run in using the following;

```bash
# clone this repo
git clone https://github.com/xs2pranjal/intent_via_audio.git
cd intent_via_audio

# install python dependencies
pip3 install -r requirements.txt

# dowload the pre-trained embeddings and some libraries. This might take a while...
./download_data.sh
```

## Audio Service

`audio_service.py` allows you identify intent addressed within a text/audio file, it returns the top n intents addressed in the input file.
```bash
python3 audio_service.py -t intent
```
By default, `audio_service.py` takes the num of intent as 4 and the data file present in `./data/sample.mp3`. You can specify your own values for each of these parameters if you would like:
```bash
python3 audio_service.py -t intent --top_n 3 --file_path ./data/sample.mp3
```
You can also test the intent for a text file, you can do this with the use of a text file instead of the audio file.
```bash
python3 audio_service.py -t intent --file_path ./data/news.txt
```

## TTS

`audio_service.py` also allows you to convert text to speech, it creates a .mp3 file in the data directory.
```bash
python3 audio_service.py -t tts
```
By default, `audio_service.py` for tts takes a data file present in `./data/sample.txt`. You can specify your own values for the file if you would like:
```bash
python3 audio_service.py -t tts --file_path ./data/news.txt
```