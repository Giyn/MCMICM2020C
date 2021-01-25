"""
-------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2021/1/25 16:13:42
# @Author  : Giyn
# @Email   : giyn.jy@gmail.com
# @File    : TF_IDF.py
# @Software: PyCharm
-------------------------------------
"""

import nltk
import math
import string

from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import *


def get_tokens(text: str):
    """

    participle

    Args:
        text: text

    Returns:
        tokens

    """
    lower = text.lower()
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    no_punctuation = lower.translate(remove_punctuation_map)
    tokens = nltk.word_tokenize(no_punctuation)

    return tokens


def stem_tokens(tokens, stemmer):
    """

    stemming

    Args:
        tokens: tokens
        stemmer: stemmer

    Returns:
        stemmed

    """
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))

    return stemmed


def tf(word, count):
    return count[word] / sum(count.values())


def n_containing(word, count_list):
    return sum(1 for count in count_list if word in count)


def idf(word, count_list):
    return math.log(len(count_list)) / (1 + n_containing(word, count_list))


def tfidf(word, count, count_list):
    return tf(word, count) * idf(word, count_list)


def count_term(text):
    tokens = get_tokens(text)
    filtered = [w for w in tokens if not w in stopwords.words('english')]
    stemmer = PorterStemmer()
    stemmed = stem_tokens(filtered, stemmer)
    count = Counter(stemmed)
    return count


def main(texts: list):
    countlist = []

    for text in texts:
        countlist.append(count_term(text))
    tf_idf_dict = {}
    for i, count in enumerate(countlist):
        # print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, count, countlist) for word in count}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:5]:
            tf_idf_dict[word] = round(score, 5)
            # print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))

        yield tf_idf_dict


if __name__ == "__main__":
    texts = ['Giyn likes guitar.',
             'Helen likes guitar too.',
             'Giyn also likes piano.']
    for i in main(texts):
        print(i)
