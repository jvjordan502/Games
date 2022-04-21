
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 15:27:12 2022

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

for i in range(len(remainders)):
    new_list = [x for x in new_list if remainders[i].lower() not in x ]
    
print(sorted(new_list))
print(len(new_list))
