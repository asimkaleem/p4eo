#!/usr/bin/env python
# -*- coding: utf-8 -*-

# looping through the string.
# Example # 1
# myString = raw_input("Please enter a string: ")
# index = 0
# while index < len(myString):
#     letter = myString[index]
#     print letter
#     index = index+1
#-----------------------------------------------------------------------------------------------------------------------
# __author__ = 'asim'
# Exercise 6.1 Write a while loop that starts at the last character in the string and
# works its way backwards to the first character in the string, printing each letter on
# a separate line, except backwards.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise 6.1 Write a while loop that starts at the last character in the string and works its way backwards to the
# first character in the string, printing each letter on a separate line, except backwards
#
# myString = raw_input("Please enter a string: ")
# index = len(myString)
# while index > 0:
#     letter = myString[index-1]
#     print letter
#     index = index-1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# String Slices:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MySubString1 = "Please enter a string: "
# MySubString1 = myString1[0:8]
# MySubString1
# print MySubString1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Exercise 6.2 Given that fruit is a string, what does fruit[:] mean?
# fruit = 'orange'
# print fruit[:]
#-----------------------------------------------------------------------------------------------------------------------
# Exercise 6.3 Encapsulate this code in a function named count, and generalize it
# so that it accepts the string and the letter as arguments.
# def count(word):
#     x = 0
#     for letter in word:
#         if letter == 'a':
#             x = x + 1
#     return x

# myString = raw_input("Please enter a fruit name and it will give you back count of letter 'a' in it: ")
# print count(myString)

#-----------------------------------------------------------------------------------------------------------------------
# fruit = "Orange"
# print 'a' in fruit
#-----------------------------------------------------------------------------------------------------------------------
# Exercise 6.4 There is a string method called count that is similar to the function
# in the previous exercise. Read the documentation of this method at docs.python.
# org/library/string.html and write an invocation that counts the number of
# times the letter a occurs in 'banana'.
#-----------------------------------------------------------------------------------------------------------------------
# fruit = raw_input("Please enter some fruit name: ")
# print "No of A's in your given string are: ",fruit.lower().count('a')

#-----------------------------------------------------------------------------------------------------------------------
# Exercise 6.5 Take the following Python code that stores a string:‘
# str = 'X-DSPAM-Confidence: 0.8475'
# Use find and string slicing to extract the portion of the string after the colon character and then use the float
# function to convert the extracted string into a floating point number.
#-----------------------------------------------------------------------------------------------------------------------
# str = "X-DSPAM-Confidence: 0.8475"
# pos = str.find(":")
# getNumber = float(str[pos+1:])
# print getNumber

#-----------------------------------------------------------------------------------------------------------------------
# Exercise 6.6 Read the documentation of the string methods at docs.python.org/lib/string-methods.html. You might want
# to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.
#Done




















#-----------------------------------------------------------------------------------------------------------------------