#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 1 

Template File for fault_detection_time_series

@author:  
"""
import fault_detection_one_sample as one 

def fault_detection_time_series(irradiance_time_series_average,
                                power_time_series, model_para, margin):       
    real_fault_list = []
    if len(power_time_series) <= len(irradiance_time_series_average):
        for k in range(len(power_time_series)):
            fault = one.fault_detection_one_sample(irradiance_time_series_average[k],
                                    power_time_series[k], model_para, margin)
            if fault == True:
                real_fault_list.append(k)
    else:
        for k in range(len(irradiance_time_series_average)):
            fault = one.fault_detection_one_sample(irradiance_time_series_average[k],
                                    power_time_series[k], model_para, margin)
            if fault == True:
                real_fault_list.append(k)
    return real_fault_list