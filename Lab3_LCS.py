#############################################################################
# Least common substring functions for Lab 3
# Alex Bartlett
# 
# includes functions for finding the length of and printing the longest
# common substring between two DNA sequences
#
#############################################################################

# import standard libraries
import numpy as np
import time

# function utilizing dynamic programming to compute the table c,
# and return the LCS as described in 15.4 
def find_LCS(X, Y):

	# begin timing
	start = time.time()

	# acquire lengths of seqs, ensure that X is longer than Y
	m = len(X)
	n = len(Y)
	if n > m:
		temp = X
		X = Y
		Y = temp
		temp2 = m
		m = n
		n = temp2

	# counter for storing number of comparisons made
	comps = 0
 	
 	# create the empty table c
	c = np.array([[None for i in range(n + 1)] for j in range(m + 1)])	

	# fill in the first row and column of c with zeroes, given that
	# a substring of length 0 can only have LCS of 0
	for i in range(1, m + 1):
		c[i,0] = 0

	for j in range(n + 1):
		c[0,j] = 0

	# use dynamic programming to continue comparing DNA bases and 
	# compute the rest of the table
	for i in range(1, m + 1):
		for j in range(1, n + 1):
 			
 			# add to LCS length if a matching base is foud
			if X[i - 1] == Y[j - 1]:
				c[i, j] = c[i - 1, j - 1] + 1
				comps += 1 # include comparison done in the "if" statment

			# determine which LCS (so far) is longer, use that length
			# for the current slot in the table
			elif c[i - 1, j] >= c[i, j - 1]:
				c[i, j] = c[i - 1, j]
				comps += 2 # one for the "if" and one for the "else if"
			else:
				c[i, j] = c[i, j - 1]
				comps += 2 # one for the "if" and one for the "else if"

	# use completely calculated table to assemble LCS
	lcs, new_comps = print_lcs(c, X, Y, m, n, '', comps)

	# incorporate number of comparisons made while traversing table
	final_comps = comps + new_comps

	# stop the clock
	end = time.time()

	# return the LCS, the total number of comparisons, and the amount of
	# time elapsed
	return lcs, final_comps, end - start

# function to traverse the table c starting with the ends of both sequences
# and assemble the LCS, as described in 15.4
def print_lcs(c, X, Y, i, j, lcs, comps):

	# this case is when we reach the beginning of the sequence(s)
	if c[i, j] == 0:
		return lcs, comps + 1 # "if" statement performs one comparison

	# if a matching base is found, find the LCS of the strings prior to that base
	# when done, add matching base to that LCS
	if X[i - 1] == Y[j - 1]:
		new_lcs, new_comps = print_lcs(c, X, Y, i - 1, j - 1, lcs, comps + 1)
		lcs =  lcs + new_lcs
		lcs = lcs + X[i - 1]
		comps += new_comps

	# determine which sub-LCS is longer and find the LCS for the substrings
	# of X and Y that produced that sub-LCS
	elif c[i - 1, j] > c[i, j - 1]:
		new_lcs, new_comps = print_lcs(c, X, Y, i - 1, j, lcs, comps + 2) 
		lcs =  lcs + new_lcs
		comps += new_comps # one for the "if" and one for the "else if"
	
	else:
		new_lcs, new_comps = print_lcs(c, X, Y, i, j - 1, lcs, comps + 2)
		lcs =  lcs + new_lcs
		comps += new_comps # one for the "if" and one for the "else if"

	# return the text of the LCS and the number of comparisons done while
	# assembling it
	return lcs, comps
