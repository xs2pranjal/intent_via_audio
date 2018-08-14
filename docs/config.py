#File path of the glove embedding file.
#Download link: http://nlp.stanford.edu/data/glove.42B.300d.zip
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(ROOT_DIR, 'data/')
# GLOVE_FILE_PATH = os.path.join(ROOT_DIR, 'data/glove/glove.42B.300d.txt')
GLOVE_PATH = os.path.join(DATA_DIR, 'glove.42B.300d.txt')

GOOGLE_CRED = os.path.join(ROOT_DIR, 'docs/cred.json')

CATEGORIES = ["food","sports","health","business","travelling","finance","education","music","technology","fashion",
              "stocks","news","romance","comedy","adventure","animals","clothing","insurance","hardware","political",
              "religious", "photography","fitness","transportation"]