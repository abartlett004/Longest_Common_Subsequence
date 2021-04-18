#############################################################################
# Main driver for Lab 3
# Alex Bartlett
#
# Parses input file, performs all LCs calculation for each pair of 
# seqs, and writes output to file along with efficiency statistics
#
##############################################################################

# import standard libraries
import argparse
from Lab3_utils import *


# main driver
if __name__ == "__main__":

	# parse command line argument to get name of desired input file 
	# and output file (if supplied)
	parser = argparse.ArgumentParser()
	parser.add_argument('--input_file', type = str,  \
		help = "path to file containing input sequences")
	parser.add_argument('--output_file', type = str, \
		help = "path to desired output file", default = "output.txt")
	args = parser.parse_args()

	# read input file
	with open(args.input_file) as file:
		contents = file.read()

	# validate input
	validate_input(contents)

	# parse input, calculate LCSes for each non-redundant pair of 
	# input sequences, and create output
	output = find_LCSes(contents)

	# write output to file
	outfile = open(args.output_file, 'w')
	outfile.writelines(output)
	outfile.close()