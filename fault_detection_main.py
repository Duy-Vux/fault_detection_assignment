#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 1 

Template File for fault_detection_main

@author: duy vu
"""
import calc_average as avg
import fault_detection_time_series as series


def fault_detection_main(irradiance_time_series,power_time_series,
                         irradiance_sampling_time,power_sampling_time,
                         model_para,margin):
    if type(irradiance_sampling_time) is int and irradiance_sampling_time > 0\
       and type(power_sampling_time) is int and power_sampling_time > 0\
       and (power_sampling_time%irradiance_sampling_time) == 0\
       and len(model_para) == 3 and (type(margin) is float or type(margin) is int)\
       and margin >0:
        if len(power_time_series) >= 1 and\
            irradiance_sampling_time*len(irradiance_time_series) >= power_sampling_time:
                segment_length = int(power_sampling_time/irradiance_sampling_time)
                irradiance_time_series_average = avg.calc_average(irradiance_time_series, segment_length)
                real_fault_list = series.fault_detection_time_series(irradiance_time_series_average,
                             power_time_series, model_para, margin)
                return real_fault_list
        else:
            return 'Not enough data'
    else:
        return 'Corrupted input'
    
               