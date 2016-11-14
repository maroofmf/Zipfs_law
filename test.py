'''
Author: Maroof

This code demonstrates
'''

import string
import sys
from scipy.stats import chisquare
import pylab as plt

# global variables needed for fast parsing
# translation table maps upper case to lower case and punctuation to spaces
translation_table = str.maketrans(string.punctuation+ 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                     " "*len(string.punctuation)+'abcdefghijklmnopqrstuvwxyz')

def get_words_from_text(text):
    """
    Parse the given text into words.
    Return list of all words found.
    """
    text = text.translate(translation_table)
    word_list = text.split()
    return word_list

def count_frequency(word_list):
    """
    Return a dictionary mapping words to frequency.
    """
    D = {}
    for new_word in word_list:
        if new_word in D:
            D[new_word] = D[new_word]+1
        else:
            D[new_word] = 1
    return D

def word_frequencies_for_file(text):
    """
    Return dictionary of (word,frequency) pairs for the given file.
    """
    word_list = get_words_from_text(text)
    freq_mapping = count_frequency(word_list)
    return freq_mapping

def displayFrequency(sorted_word_list,numberOfWords):
    plt.figure(1)
    xValue = [value for value,value2 in sorted_word_list]
    yValue = [value2 for value,value2 in sorted_word_list]
    yValueExpected = [numberOfWords/rank for rank in range(1,11)]
    x = range(10)
    plt.xticks(x,xValue)
    plt.bar(x,yValue, align = 'center')
    plt.plot(x,yValue,'r', linewidth = 2)
    plt.plot(x,yValueExpected, 'g', linewidth = 2)
    plt.title('Frequency distribution of words in data.txt')


def summary(sorted_word_list):
    print('-----------------Summary-----------------')
    print('WORD----COUNT')
    [print(word,'----',count) for word,count in sorted_word_list]



def main():

    argc = len(sys.argv)
    if argc!=2:
        print('Incorrect usage. Use: python3 test.py data.txt')
        sys.exit(-1)

    #Reading file content
    fileName = sys.argv[1]
    file = open(fileName,'rU')
    fileData = file.read().lower()
    file.close()

    # Parsing and counting words
    sorted_word_list = word_frequencies_for_file(fileData)
    sorted_word_list = list(sorted_word_list.items())
    sorted_word_list = sorted(sorted_word_list, key = lambda wordCount : wordCount[1], reverse = True)
    numberOfWords = len(sorted_word_list)

    # Hypothesis testing
    expectedFrequency = [numberOfWords/rank for rank in range(1,numberOfWords+1)]
    observedFrequency = [count for word,count in sorted_word_list]
    # print(expectedFrequency[0:3],"++++",observedFrequency[0:3])
    a,b=chisquare(observedFrequency,expectedFrequency)
    print(a,b)

    #Displaying words
    displayFrequency(sorted_word_list[0:10], numberOfWords)
    summary(sorted_word_list[0:10])
    # plt.show()

if __name__ == "__main__":
    main()

