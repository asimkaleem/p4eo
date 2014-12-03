#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'asim'
# fhand = open('mbox.txt')
# fhand = open('mbox-short.txt')
#
# count = 0
# for line in fhand:
#     count = count+1
# print "Line Count: ", count

#-----------------------------------------------------------------------------------------------------------------------
# Read relatively small files
#-----------------------------------------------------------------------------------------------------------------------
# fhand = open("mbox-short.txt")
# inp = fhand.read()
#prints length of a file.
# print len(inp)
#prints first 20 characters of file.
# print inp[:20]
# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     if line.startswith('From:'):
#         count = count+1
#         print str(count) + "-->" + line.rstrip()
# print "EOF"
# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     # Skip 'uninteresting lines'
#     if not line.startswith('From:') :
#         continue
#     # Process our 'interesting' line
#     print line
#-----------------------------------------------------------------------------------------------------------------------
# Exercise 7.3 Sometimes when programmers get bored or want to have a bit of fun,they add a harmless Easter Egg to their
# program (en.wikipedia.org/wiki/Easter_egg_(media)). Modify the program that prompts the user for the file name so that
#it prints a funny message when the user types in the exact file name ’na na boo boo’. The program should behave
# normally for all other files which exist and don’t exist. Here is a sample execution of the program:
#-----------------------------------------------------------------------------------------------------------------------
# fhand = raw_input("Enter File Name: ").lower()
# if fhand == 'na na boo boo':
#     print "NA NA BOO BOO TO YOU - You have been punk'd!"
# elif fhand != 'na na boo boo':
#     try:
#         fhand = open(fhand)
#         for line in fhand:
#             line = line.rstrip()
#             # Skip 'uninteresting lines'
#             if not line.startswith('From:'):
#                 continue
#             # Process our 'interesting' line
#             print line
#     except IOError:
#         print "file not found"
#-----------------------------------------------------------------------------------------------------------------------
#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of
# the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values
# and produce an output as shown below.
#-----------------------------------------------------------------------------------------------------------------------
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        pos = line.find(":")
        count = count+1
        getNumber = float(line[pos+1:])
        total = total+getNumber
average = total/count
print "Average spam confidence:" ,average

