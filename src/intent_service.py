import traceback
import numpy as np
from heapq import nlargest
from sklearn.metrics.pairwise import cosine_similarity
from helpers.noun_chunking import NounPhraseExtraction
from docs.config import CATEGORIES
from helpers.model_loader import GloveService

class IntentService():
    ''' The class is for Extracting the top n intents from the input text.'''
    def __init__(self, top_n):
        self.top_n = top_n
        self.__noun_phrase_tokens=[]
        self.__default_categories = CATEGORIES
        self.__glove_model = GloveService()

    def __generate_text_vector(self):
        '''Generates the text vector for the present noun phrases vocab'''
        token_vector_dict={}

        for token in self.__noun_phrase_tokens:
            # print(token)
            try:
                # print(type(self.__glove_model.get_vector(token)))
                token_vector_dict[token] = self.__glove_model.get_vector(token)

            except Exception as e:
                pass

        vector_mean = np.mean(list(token_vector_dict.values()),axis=0)

        return vector_mean

    def __get_text_category_affinity(self, text):
        '''Computes the affinity between the text and the category'''
        try:
            self.__noun_phrase_tokens = NounPhraseExtraction().get_noun_phrases(text)
        except Exception as e:
            traceback.print_exc()

        affinity_dict={}
        affinity_dict["aspects"]=self.__noun_phrase_tokens

        text_vector=self.__generate_text_vector()

        #calculate text affinity from each category
        category_affinity_dict={}

        for category in self.__default_categories:
            try:
                category_vector = self.__glove_model.get_vector(category)
                category_affinity_dict[category] = cosine_similarity(text_vector.reshape(1,-1),category_vector.reshape(1,-1)).item(0)
            except Exception as e:
                category_affinity_dict[category] = None

        affinity_dict["affinity"] = category_affinity_dict
        return affinity_dict

    def get_default_category(self,text):
        '''Returns the top-n intents closest to the text'''
        category_affinity_dict=self.__get_text_category_affinity(text)
        affinity_dict=category_affinity_dict.get('affinity')
        five_largest=nlargest(self.top_n,affinity_dict,key=affinity_dict.get)

        return five_largest