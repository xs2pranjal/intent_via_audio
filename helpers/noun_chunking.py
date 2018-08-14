from nltk import WordNetLemmatizer, RegexpParser
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class NounPhraseExtraction():

    '''
    The class is for Noun Phrases extraction from Textual Data.
    The grammar is taken from Su Nam Kim Paper.
    '''

    __grammar = r"""
                    NBAR:
                        {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns
                
                    NP:
                        {<NBAR>}
                        {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
                 """
    __lemmatizer = WordNetLemmatizer()
    __stop_words = set(stopwords.words("english"))

    def __init__(self):
        self.__noun_phrase_list=[]


    def __leaves(self,tree):
        """Finds NP (nounphrase) leaf nodes of a chunk tree."""

        for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
            yield subtree.leaves()


    def __normalise(self,word):
        """Normalises words to lowercase and stems and lemmatizes it."""

        word = word.lower()
        word =self.__lemmatizer.lemmatize(word)

        return word


    def __acceptable_word(self,word):
        """Checks conditions for acceptable word: length, stopword. We can increase the length if we want to consider large phrase"""
        accepted = bool(2 <= len(word) <= 40 and word.lower() not in self.__stop_words)

        return accepted


    def __get_terms(self,tree):
        """"""
        for leaf in self.__leaves(tree):
            term = [self.__normalise(w) for w, t in leaf if self.__acceptable_word(w)]
            yield term


    def get_noun_phrases(self,text):
        """Returns the noun phrases present in a text"""
        chunker = RegexpParser(self.__grammar)
        toks = word_tokenize(text)
        pos_tokens = pos_tag(toks)
        tree = chunker.parse(pos_tokens)

        for token in self.__get_terms(tree):
            if len(token)!=0:
                self.__noun_phrase_list.append(token[0])

        return self.__noun_phrase_list