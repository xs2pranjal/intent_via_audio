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
python3 audio_service.py --top_n 3 --file_path ./data/news.txt
```