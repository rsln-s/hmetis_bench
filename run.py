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

def run_for_file(num_parts):
	filename = 'lp_ship12l'
	cmd = "./hmetis2.0pre1 big_bench/lp_ship12l.mat.hmetis " + str(num_parts)

	# Run zdrive
	process = Popen(shlex.split(cmd), stdout=PIPE)
	(output, err) = process.communicate()
	exit_code = process.wait()

	#Process output
	cutn = get_first_num_after_substring(output, b'Hyperedge Cut:')
	cutl = get_first_num_after_substring(output, b'Sum of External Degrees:')
	if (cutn == None) or (cutl == None):
		print("Something went wrong")
	
	result = [filename, num_parts, cutn, cutl]

	tmp_out_filename = "output_for_inp_" + filename + ".csv"
	with open(tmp_out_filename, 'w') as tmp_out:
	    tmp_w = csv.writer(tmp_out)
	    tmp_w.writerow(result)
	return result 

outfilename = 'output_'
if len(sys.argv) == 2:
        outfilename += sys.argv[1]

outfilename += '.csv'

parts = [2,4,8,16,32,64,128]	
num_cores = 8 
results = Parallel(n_jobs=num_cores)(delayed(run_for_file)(n) for n in parts)

with open(outfilename, 'w') as csvfile:
	out = csv.writer(csvfile)
	out.writerow(['Graph name', 'Num parts','CUTN min', 'CUTL min'])
	for r in results:
		out.writerow(r)

