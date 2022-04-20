#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 17:27:12 2022

@author: james
"""

from nltk.corpus import words
import fnmatch
word_list = words.words()
# prints 236736
print(len(word_list))
for i in range(len(word_list)):
    word_list[i] = word_list[i].lower()
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letters = list(input('Input Available Letters, Place Yellow Letter First: '))
remainders = list(set(alphabet)-set(letters))
#print(len(remainders))
refined_list = fnmatch.filter(word_list, '*'+letters[0].lower()+'*')
print(len(refined_list))

new_list = [x for x in refined_list if (letters[1].lower() in x or letters[2].lower() in x or letters[3].lower() in x or letters[4].lower() in x or letters[5].lower() in x or letters[6].lower() in x )and len(x) > 3]
print(len(new_list))
bad_list = [x for x in new_list if remainders[0].lower() in x or remainders[1].lower() in x or remainders[2].lower() in x or remainders[3].lower() in x or remainders[4].lower() in x or remainders[5].lower() in x or remainders[6].lower() in x or remainders[7].lower() in x or remainders[8].lower() in x or remainders[9].lower() in x or remainders[10].lower() in x or remainders[11].lower() in x or remainders[12].lower() in x or remainders[13].lower() in x or remainders[14].lower() in x or remainders[15].lower() in x or remainders[16].lower() in x or remainders[17].lower() in x or remainders[18].lower() in x]
    
final_list = list(set(new_list)-set(bad_list))
print(len(final_list))
print(final_list)
