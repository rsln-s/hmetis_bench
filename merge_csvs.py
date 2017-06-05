# merges hmetis and zoltan csvs. Zoltan csv has to have unique ID!
import csv
import sys

def imbal_hmetis_2_zoltan(hmetis_imbal):
	return 1.0 + float(int(hmetis_imbal))/100.0

#print(str(imbal_hmetis_2_zoltan("10")))
#sys.exit(0)

with open('big_bench_f40a3f_merged.csv') as f:
	r = csv.reader(f, delimiter=';')
	z_dict = {row[0]: row[1:] for row in r}

with open('big_bench_hmetis.csv') as f:
	r = csv.reader(f)
	h_dict = {str(row[0])+str(b'rs_alg_dist')+str(row[1])+str(imbal_hmetis_2_zoltan(row[2])): row[1:] for row in r}

#print(str(z_dict["adder_dcop_19b'rs_alg_dist'21.05"]))
#print(str(h_dict["adder_dcop_19b'rs_alg_dist'21.05"]))
#sys.exit(0)

for k, v in h_dict.items():
	if k in z_dict:
		z_dict[k].extend(v)
		z_dict[k].extend([float(z_dict[k][4]) / float(h_dict[k][2])])
	else:
		print("Can't find the key", k)

with open('merged.csv', 'w') as f:
	w = csv.writer(f, delimiter=';')
	w.writerows([k] + z_dict[k] for k in z_dict.keys())
