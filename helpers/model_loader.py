import numpy as np
import tqdm
from docs.config import GLOVE_PATH

class GloveService():
    ''' The class is for Loading GloVe Embedding into memory and accessing it further'''
    def __init__(self):
        try:
            self.file = open(GLOVE_PATH,"r")
        except Exception as e:
            raise FileNotFoundError("Cannot find Glove model at %s"%GLOVE_PATH)
        self.__glove_model = self.__load_glove_embedding()


    def __load_glove_embedding(self):
        '''Loads text word embedding into a dictionary'''
        glove_embedding = dict()
        print ('This will take a while...')

        for line in tqdm.tqdm(self.file, desc= "Loading GloVe"):
            splitLine = line.split()
            word = splitLine[0]
            embedding = np.array([float(val) for val in splitLine[1:]])
            glove_embedding[word] = embedding
        return glove_embedding

    def if_exist(self,token):
        '''Checks if the provided vocab exists in the embedding dictionary'''
        if token in self.__glove_model.keys():
            return True
        else:
            return False


    def get_vector(self,token):
        '''Returns the vector of the word from the embedding dictionary'''
        try:
            vector = self.__glove_model[token]
            # vector_list = ast.literal_eval(vector)
            vector_nparray = np.array(vector).astype(float)
            return vector_nparray

        except:
            raise ValueError