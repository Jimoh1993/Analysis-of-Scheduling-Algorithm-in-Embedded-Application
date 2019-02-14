#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: glb.py
#import os
def init():
	global v, sr, f, r, rf, tk, q
	v = False    #option: verbose
	sr = False   #option: show random number used
	f = ''       #input file name
	rf = '../random-numbers.txt'  #random number file name
	r = None     #random number generator object
	tk = None    #timekeeper object
	q = False    #for round robin quantum: False or q

#Testing for file path
#if os.path.isfile('../input/input-1.txt'):
#    print('found')
#else: 
#    print('Not found')