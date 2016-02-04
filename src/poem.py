__author__ = 'Mac'

from collections import Counter
import string
import nltk

class Poem:
    """
    This class represents a poem.
    """

    def __init__(self, filename, iteration_mode = "line"):

        self.filename = filename
        self.iteration_mode = iteration_mode

        #read poem name & author name from the text file
        self.name, self.author = self.read_names()

        #initialize word counter - better & faster than an ordinary dictionary
        #its methods can be used to generate much useful stuff, like
        #frequency dictionary or just mere bag of words representation
        self.poem_counter = self.setup_word_counter


    def read_names(self):
        with open(self.filename, "r") as fr:
            name = fr.readline()
            author = fr.readline()
        return([name,author])


    @property
    def setup_word_counter(self):
        all_txt = u""
        for line in self:
            all_txt += line.decode("utf-8").lower()
        list_of_words = nltk.word_tokenize(all_txt.encode("utf-8").translate(None, string.punctuation))
        counter = Counter(list_of_words)
        return counter


    def __iter__(self):
        """
        A method that initializes iteration over a poem.
        :return:      self
        """
        fr = open(self.filename)
        if self.iteration_mode == 'line':
            self.iter_index = 2
        if self.iteration_mode == 'strophe':
            self.iter_index = 2
        fr.close()
        return self

    def next(self):
        """
        A standard method that iterates over a poem, yielding one line or strophe at a time.
        :return:
        """
        with open(self.filename, "r") as fr:
            if self.iteration_mode == 'line':
                for i, line in enumerate(fr):
                    if i == self.iter_index:
                        self.iter_index += 1
                        return line
                raise StopIteration
            elif self.iteration_mode == 'strophe':
                strophe = []
                for i,line in enumerate(fr):
                    if i == self.iter_index:
                        self.iter_index+=1
                        if line == '\n':
                            return strophe
                        else:
                            strophe.append(line)
                raise StopIteration

    def get_bow_representation(self):
        return self.poem_counter.keys()

    def get_frequency_dictionary(self):
        return dict(self.poem_counter)

    def get_most_frequent_words(self,number):
        return self.poem_counter.most_common(number)





