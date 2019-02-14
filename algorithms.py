#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: algorithms.py
import glb
from util import Timekeeper, Random

class SchedulingAlgorithm():
	"""superclass of all scheduling algorithms"""
	def __init__(self, algoName):
		self.tk = glb.tk = Timekeeper() # Reset time
		self.algoName = algoName
		glb.r = Random(glb.rf) # Reset Random numbers
	def main(self, ps, sortFunctionStr):
		while not ps.finished():
			if glb.v:
				print('Before cycle{}: {}.'.format((' '*5+str(self.tk.getNow()))[-5:],ps))
			ps.tickAll() # advance/deduct all time variables
			ps.updateStateAll() # update state accordingly
			if not len(ps.getByState('running')): # if there is no running process
				readyps = ps.getByState('ready').sortByInput().sortByArrival()
				readyps = getattr(readyps, sortFunctionStr)()  # sort function will differ by algo
				if len(readyps) > 0:
					readyps.pop(0).run()
			self.tk.tick() # advance 1 cycle
		print('\nThe scheduling algorithm used was {}\n'.format(self.algoName))
		ps.printSummaryAll()

class FCFS(SchedulingAlgorithm):
	"""First Come First Serve"""
	def __init__(self):
		super().__init__('First Come First Serve')
	def main(self, ps):
		super().main(ps, 'sortByReady')

class RR(SchedulingAlgorithm):
	"""Round Robin"""
	def __init__(self):
		super().__init__('Round Robin')
	def main(self, ps, quantum):
		glb.q = quantum
		super().main(ps, 'sortByReady')
		glb.q = False

class SJF(SchedulingAlgorithm):
	"""Shortest Job First: total time remaining (i.e., the
	input value C minus the number of cycles this process has run)"""
	def __init__(self):
		super().__init__('Shortest Job First')
	def main(self, ps):
		super().main(ps, 'sortByJob')

class PQ(SchedulingAlgorithm):
	"""Priority Queue"""
	def __init__(self):
		super().__init__('Priority Queue')
	def main(self, ps):
		super().main(ps, 'sortByPriority')

class MLQ(SchedulingAlgorithm):
	"""Multi-Level Queue"""
	def __init__(self):
		super().__init__('Multiple-Level Queues')
	def main(self, ps):
		super().main(ps, 'sortByQueue')