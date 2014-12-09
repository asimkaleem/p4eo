#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'asim'
# myList = list()
# print myList
#
# myCollection = dict()
#
# print myCollection
# myCollection[1] = 'World'
# print myCollection
# print len(myCollection)
#
# myCollection1 = {1:"Hello World", 2 : "HOw are you"}
# print "My Second Colleciton", myCollection1
# for item in myCollection1:
#     print myCollection1[item]

# eng2sp = dict()
# eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# print "Lenght of dictionary: ", len(eng2sp)
# print "Content of dictionary: ", eng2sp
# print "Does translation of One exist? ", 'one' in eng2sp
# vals = eng2sp.values()
# print vals

#-----------------------------------------------------------------------------------------------------------------------
# Exercise 9.1 Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t
# matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the
# dictionary.
#-----------------------------------------------------------------------------------------------------------------------

# fhand = open("words.txt")
# lineCount = 0
# wordCount = 0
# myDict = {}
#
# for lines in fhand:
#     lineCount = lineCount + 1
#     words = lines.split()
#
#     for word in words:
#         myDict[word] = word
#         wordCount = wordCount+1
#
# print myDict
# print lineCount
# print wordCount

#-----------------------------------------------------------------------------------------------------------------------
# you are given a string and you want to count how many times each letter
# appears.
#-----------------------------------------------------------------------------------------------------------------------
word = 'nonteneous'
d = dict()
for c in word:
    if c not in d:
        d[c]= 1
    else:
        d[c] = d[c]+1
print d


