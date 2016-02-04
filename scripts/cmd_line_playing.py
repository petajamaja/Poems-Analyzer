# -*- coding: utf-8 -*-
__author__ = 'Mac'

import os
import sys
# without this line it refused to import packages...
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.printing import smart_print

from src.poem import Poem

if __name__ == '__main__':

    poem = Poem("../data/Priblizhaetsa_zvuk.txt")
    print poem.author
    print poem.name

    #count = poem.poem_counter
    #var = count["и"]
    #print var

    bow = poem.get_bow_representation()
    freq = poem.get_frequency_dictionary()
    most_common_3 = poem.get_most_frequent_words(3)
    print(most_common_3)

    #smart_print(bow)
    #smart_print(count)

    #poem.iteration_mode='line'

    #for line in poem:
    #    print len(line)

    #poem.iteration_mode = 'strophe'

    #for strophe in poem:
    #    smart_print(strophe)
