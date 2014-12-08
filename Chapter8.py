#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'asim'

# numbers = [1,2,3,4,5,6]
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
# print numbers

# List operations (CONCATINATION) :
# a =[1,2,3]
# b = [4,5]
# c = a + b
# print c


#-----------------------------------------------------------------------------------------------------------------------
# List operations (Repeatitions):
#-----------------------------------------------------------------------------------------------------------------------
# a = [0]
# print a * 4

#-----------------------------------------------------------------------------------------------------------------------
# List operations (List Slicing):
#-----------------------------------------------------------------------------------------------------------------------
# t = ['a','b','c','d','e','f']
# print t[:3]

#-----------------------------------------------------------------------------------------------------------------------
#List operations (List Mutation):
#-----------------------------------------------------------------------------------------------------------------------
# t = ['a','b','c','d','e','f']
# t[0:1] = ['x','y','z',1]
# print t

#-----------------------------------------------------------------------------------------------------------------------
#List Methods (APPEND):
#-----------------------------------------------------------------------------------------------------------------------
#
# list = [ 1,2,3,4,5]
# list.append(6)
# print list


#-----------------------------------------------------------------------------------------------------------------------
#List Methods (Extends):
#-----------------------------------------------------------------------------------------------------------------------
# list = [ 1,2,3,4,5]
# list2 = [6,7,8,"Hello Wolrd"]
# list.extend(list2)
# print list

#-----------------------------------------------------------------------------------------------------------------------
#List Methods (Sort):
#-----------------------------------------------------------------------------------------------------------------------
# list1 = [9,8,6,4,1,"Hello World!",[3,2,1]]
# list1.sort()
# print list1

#-----------------------------------------------------------------------------------------------------------------------
#Deleting Elements:
#-----------------------------------------------------------------------------------------------------------------------
# old_list = [1,2,3,4,5,6,7,8,9]
# new_list = old_list.pop(0)
# print new_list
# print "old list after pop: ", old_list
# old_list = old_list.pop()
# print "old list after second pop: ", old_list

# numlist = list()
# while (True):
#     inp = raw_input("PLease enter a number: ")
#     if inp == 'done' :break
#     value= float(inp)
#     numlist.append(value)
#     average = sum(numlist) / len(numlist)
# print "Average", average

#-----------------------------------------------------------------------------------------------------------------------
#Lists and Strings
#-----------------------------------------------------------------------------------------------------------------------
s = 'pining for the fjords'
t = s.split()
print t
print t[2]


# s = 'spam-spam-spam'
# delimiter = '-'
# print s.split(delimiter)
# print s

# t = ['pining', 'for', 'the', 'fjords']
# delimiter = ' '
# print delimiter.join(t)

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From ') : continue
#     words = line.split()
# print words[2]





# print range(5)


# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print len(c)

#
# t = [9, 41, 12, 3, 74, 15]
# print t
# t.append(16)
# print t

#
# friends = [ 'Joseph', 'Glenn', 'Sally' ]
# friends.sort()
# print friends[0]

# fruit = 'Banana'
# fruit[0] = 'b'
# print fruit


#
#  8.4 Open the file romeo.txt
# read it line by line. For each line, split the line into a list of words using the
# split() function. The program should build a list of words. For each word on each line check to see if the word is
# already in the list and if not append it to the list. When the program completes, sort and print the resulting words
# in alphabetical order.
#
# You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

# fname = raw_input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     print line.rstrip()
