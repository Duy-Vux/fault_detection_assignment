#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 1 

Template File for calc_average

@author: 
"""

def calc_average(time_series, segment_length):
    irradiance_time_series_average = []
    for k in range(len(time_series)//segment_length):
        irradiance_time_series_average.append(sum(time_series[segment_length*k:segment_length*(k+1)])/segment_length)
    return irradiance_time_series_average