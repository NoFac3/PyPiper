'''
Source From...
Link: https://www.kaggle.com/code/cdabakoglu/word-vectors-cosine-similarity/notebook
Author: Caner Dabakoglu

uses glove.txt
'''

import numpy as np
import pandas as pd
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

class ws(object):

    def loadData():
        with open("glove.txt",'r', encoding='utf-8') as file:
            data = file.readlines()
        for i in range(len(data)):
            data[i] = data[i][:-1]
        data_dict = dict()
        for i in range(len(data)):
            split_data = data[i].split()
            data_dict[split_data[0]] = np.array(split_data[1:]).astype('float64')

        #data_dict["the"]
        return data_dict

    def cosine_similarity(a, b):
        nominator = np.dot(a, b)
        a_norm = np.sqrt(np.sum(a**2))
        b_norm = np.sqrt(np.sum(b**2))
        denominator = a_norm * b_norm
        cosine_similarity = nominator / denominator
        return cosine_similarity

    def find_word(a, b, c, data_dict):
        a, b, c = a.lower(), b.lower(), c.lower()
        a_vector, b_vector, c_vector = data_dict[a], data_dict[b], data_dict[c]
        all_words = data_dict.keys()
        max_cosine_similarity = -1000
        best_match_word = None
        for word in all_words:
            if word in [a, b, c]:
                continue
            c = ws()
            cos_sim = c.cosine_similarity(np.subtract(b_vector, a_vector), np.subtract(data_dict[word], c_vector))
            if cos_sim > max_cosine_similarity:
                max_cosine_similarity = cos_sim
                best_match_word = word
        return best_match_word, cos_sim

    def wordBag(words_bag, data_dict):
        for words in words_bag:
            f = ws()
            d, cos_sim = f.find_word(*words, data_dict)
            print("({}, {}) ----> ({}, {}) with {} difference".format(*words, d, cos_sim))

    def determinant(a):
        return np.sqrt(np.sum(a**2))

