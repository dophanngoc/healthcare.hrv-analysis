#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" This script provides output rr intervals data from mmWave data file """


import argparse
from hrvanalysis import (
        remove_outliers,
        remove_ectopic_beats,
        interpolate_nan_values,
)


parser = argparse.ArgumentParser()
parser.add_argument("data_file")
args = parser.parse_args()

rr_intervals = []
with open(args.data_file, encoding="utf-8") as data_file:
    for line in data_file:
        line = line.split("HER: ")[1]
        rr_intervals.append(60000//int(line.rstrip("\n")))

rr_intervals_without_outliers = remove_outliers(rr_intervals=rr_intervals,
                                                low_rri=300, high_rri=2000)
interpolated_rr_intervals = interpolate_nan_values(
    rr_intervals=rr_intervals_without_outliers,
    interpolation_method="linear")

nn_intervals_list = remove_ectopic_beats(
    rr_intervals=interpolated_rr_intervals,
    method="malik")

interpolated_nn_intervals = interpolate_nan_values(
    rr_intervals=nn_intervals_list)

print(interpolated_nn_intervals)

data_file.close()
