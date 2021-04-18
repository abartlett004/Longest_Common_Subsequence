#############################################################################
# I/O functions for Lab 3
# Alex Bartlett
# 
# includes functions for reading input file, passing each set of sequences
# to be analyzed, and printing the resultant LCSs in a human-readable format
# with relevant statistics
#
#############################################################################

# import standard libraries
import re
from Lab3_LCS import *

# ensure input file is valid, containing only white space and lines that 
# follow the format: S<number> = <DNA sequence>
def validate_input(contents):

	# remote white space, consider each sequence separately
	contents = contents.strip()
	lines = contents.split('\n')

	# need at least 2 sequences to calculate LCS
	assert(len(lines) > 1), \
	"Invalid input: need at least two sequences to compare"

	# validate format of each line
	for line in lines:
		line = line.strip()
		assert(re.fullmatch(r"S[0-9]+[\s]*=[\s]*[ACTGactg]+$", line)), \
			"Invalid input: the following line in your input is invalid: \n {}".format(line)

	# if you reach this point, input file is valid
	return

# parse input file, pass pairs of sequences to be LCS-ed, print
# results in human-readable format
def find_LCSes(contents):
	contents = contents.strip()

	# begin creating output string, including headers
	output = "================================\n"
	output += "INPUT\n"
	output += "================================\n\n"
	
	# echo input in output string
	output += contents
	output += "\n\n"

	# begin creating and storing output
	output += "================================\n"
	output += "OUTPUT\n"
	output += "================================\n\n"


	# remote white space, consider each sequence separately
	lines = contents.split('\n')
	num_seqs = len(lines)

	# in turn, parse the lines and form every possible 
	# non-redundant pair of sequences
	for i in range(0, num_seqs-1):

		partsX = lines[i].split('=')
		seqX = partsX[1].strip().upper()

		for j in range(i + 1, num_seqs):
			partsY = lines[j].split('=')
			seqY = partsY[1].strip().upper()

			# calculate the LCS and stats for current pair of seqs
			lcs, comps, elapsed = find_LCS(seqX, seqY)
			
			# store which pair of seqs was being compared, the LCS,
			# and relevant statistics in the output
			output += lines[i] + '\n'
			output += lines[j] + '\n'
			output += 'LCS: ' + lcs + '\n'
			output += 'Comparisons: ' + str(comps) + '\n'
			output += 'Time Elapsed (sec): ' + str(float('%.3g' % elapsed)) + '\n\n'

	# when the LCS has been calculated for all possible sequence pairs, return output
	return output