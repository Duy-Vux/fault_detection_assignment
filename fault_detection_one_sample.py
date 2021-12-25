#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 1 

Template File for fault_prediction_one_sample

@author:  
"""
import power_prediction as pred 

def fault_detection_one_sample(irradiance_average_one_sample,
                               power_one_sample,model_para,margin):
    if abs(power_one_sample - pred.power_prediction(irradiance_average_one_sample, model_para)) >= abs(margin):
        fault = True
    else:
        fault = False
    return fault

