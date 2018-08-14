#!/bin/bash

sudo apt-get install sox
sudo apt-get install python3-gdbm
curl -L http://www-nlp.stanford.edu/data/glove.42B.300d.zip -o data/glove.42B.300d.zip
unzip data/glove.42B.300d.zip -d data/glove
rm data/glove.42B.300d.zip
sudo pip install -r requirements.txt