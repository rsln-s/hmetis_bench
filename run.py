import shlex
import os
import sys
import csv
import statistics
from subprocess import Popen, PIPE
from joblib import Parallel, delayed
import multiprocessing
import re
import operator
from itertools import product
import math

def get_first_word_after_substring(output, str_to_look_for):
	outsplit = output.split(str_to_look_for, 1)
	if len(outsplit) < 2:
		return None
	return str((re.match(b'\w+', outsplit[1])).group(0))

def get_first_int_after_substring(output, str_to_look_for):
	outsplit = output.split(str_to_look_for)
	if len(outsplit) < 2:
		return None
	outclean = []
	for s in outsplit:
		outclean.append(s.strip())

	return int(float((re.match(b'\d+', outclean[-1])).group(0)))

def get_first_num_after_substring(output, str_to_look_for):
	outsplit = output.split(str_to_look_for)
	if len(outsplit) < 2:
		return None
	outclean = []
	for s in outsplit:
		outclean.append(s.strip())

	return float((re.match(b'\d+.\d+', outclean[-1])).group(0))

def run_for_file(filename, num_parts, imbal):
	cmd = "./hmetis2.0pre1 -ptype=kway -ufactor=" + str(imbal) + " " + filename + " " + str(num_parts)
	# Run zdrive
	process = Popen(shlex.split(cmd), stdout=PIPE)
	(output, err) = process.communicate()
	exit_code = process.wait()

	#Process output
	cutn = get_first_num_after_substring(output, b'Hyperedge Cut:')
	cutl = get_first_num_after_substring(output, b'Sum of External Degrees:')
	if (cutn == None) or (cutl == None):
		print("Something went wrong")

	try:
		graphname = (filename.split("."))[-3]
	except IndexError:
		print("Index error: ", filename, "cannot be split into ", filename.split("."))
		graphname = filename
	result = [graphname, num_parts, imbal, cutn, cutl]

	tmp_out_filename = "output_for_inp_" + graphname + ".csv"
	with open(tmp_out_filename, 'w') as tmp_out:
	    tmp_w = csv.writer(tmp_out)
	    tmp_w.writerow(result)
	return result 


graph_files_all = os.listdir(".")
graph_files = list(filter(lambda x: ".part." not in x, graph_files_all))
graph_files = list(filter(lambda x: "core." not in x, graph_files))
graph_files = list(filter(lambda x: "hmetis2.0pre1" not in x, graph_files))
graph_files = list(filter(lambda x: "run.py" not in x, graph_files))

outfilename = 'output.csv'

parts = [2,4,8,16,32,64,128]
imbal = [3,5,10]	
num_cores = 16 
results = Parallel(n_jobs=num_cores)(delayed(run_for_file)(f, n, imb) for f, n, imb in product(graph_files, parts, imbal))

with open(outfilename, 'w') as csvfile:
	out = csv.writer(csvfile)
	out.writerow(['Graph name', 'Num parts', 'Imbal','CUTN min', 'CUTL min'])
	for r in results:
		out.writerow(r)

