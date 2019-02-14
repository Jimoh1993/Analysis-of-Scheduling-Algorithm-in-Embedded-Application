# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 08:07:22 2019

@author: USER
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 05:30:15 2019

@author: USER
"""
import os

#import os.path
if os.path.isfile('../random-numbers.txt'):
    print('found')
else: 
    print('Not found')

#Function to count number of files in a folder
def directory(path,extension):
  list_dir = []
  list_dir = os.listdir(path)
  count = 0
  for file in list_dir:
    if file.endswith(extension): # eg: '.txt'
      count += 1
  return count

print (directory('../input', '.txt'))

with open("copy.txt", "w") as file:
    file.write("Your text goes here")

# Method 1
#f = open("Path/To/Your/File.txt", "w")   # 'r' for reading and 'w' for writing
#f.write("Hello World from " + f.name)    # Write inside file 
#f.close()                                # Close file 
#
## Method 2
#with open("Path/To/Your/File.txt", "w") as f:   # Opens file and casts as f 
#    f.write("Hello World form " + f.name)       # Writing
#    f.close()                                   # Close file
#
##Method3
#f = open('file.txt','w')
#a = input('is python good?')
#f.write('answer:'+str(a))
#f.close()
#
##Method3 modify
#with open('spam.txt', 'a') as f:
#    f.write(string_output)


#cur_path = os.path.dirname(__file__)
#new_path = os.path.relpath('..\\input\\input-1.txt', cur_path)
#if (new_path):    
    #print (new_path)
#else:
   # print('File Not Found')

#d = os.getcwd()         # Get the working directory
##os.chdir("..")          #Go up one directory from working directory
#o = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))] #Tupple List of all directory
#!Below code search the tuple for the directory i want and open the file in that directory
#print(o)
#for item in o:
    #if os.path.exists(item):
        #file = item + '\\inpt-1.tx'

        ##print(item)
        #print('found')
    #else:
        #print('file not find')