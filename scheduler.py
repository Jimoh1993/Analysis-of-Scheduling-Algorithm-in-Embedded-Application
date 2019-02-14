#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: scheduler.py
import sys
from copy import deepcopy as copy
import glb 
from process import Process, ProcessTable
from util import parseInput
from algorithms import FCFS, RR, SJF, PQ, MLQ 
    

def main():
    #print(glb.f) testing for input file from folder
    ps = ProcessTable()
    pspecs = parseInput(glb.f)
    for i in range(len(pspecs)):
        ps.append(Process(*pspecs[i],i))
        print('The original input was: {} '.format(ps.__repr__()))
        ps.sortByArrival()
        print('The (sorted) input is: {} \n'.format(ps.__repr__()))
    if glb.v:
        print('This detailed printout gives the state and remaining burst for each process\n')
        
        
    FCFS().main(copy(ps))
    RR().main(copy(ps), quantum = 2)
    SJF().main(copy(ps))
    PQ().main(copy(ps))
    MLQ().main(copy(ps))
    
        

#def main():
#    print(glb.f)
#    ps = ProcessTable()
#	pspecs = parseInput(glb.f)
#	for i in range(len(pspecs)):
#		ps.append(Process(*pspecs[i], i))
#    	print('The original input was: {} '.format(ps.__repr__()))
#    	ps.sortByArrival()
#    	print('The (sorted) input is:  {} \n'.format(ps.__repr__()))
#
#	if glb.v:
#		print('This detailed printout gives the state and remaining burst for each process\n')
#
#	FCFS().main(copy(ps))
#	RR().main(copy(ps), quantum=2)
#	SJF().main(copy(ps))
#	HPRN().main(copy(ps))


if __name__ == '__main__':
	if len(sys.argv) == 1:
		sys.argv.append('--verbose')
		sys.argv.append('--show-random')
		sys.argv.append('../input/input-3.txt')
	glb.init()
	glb.v = '--verbose' in sys.argv
	glb.sr = '--show-random' in sys.argv
	glb.f = sys.argv[-1]
	main()
