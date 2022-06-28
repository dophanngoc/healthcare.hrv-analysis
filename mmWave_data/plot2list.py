#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("data_file")
args = parser.parse_args()
 
mmWave_data_file = open(args.data_file, 'r')
hrv_dataplots = []
initial_dataplots = ""
for line in mmWave_data_file:
    line = line.split("HER: ")[1]
    hrv_dataplots.append(60000//int(line.rstrip('\n')))

print(hrv_dataplots)

mmWave_data_file.close()
