#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 1 

Template File for power_prediction

@author:  
"""
def power_prediction(irradiance_average_one_sample, model_para):
    import math
    g = irradiance_average_one_sample
    power_generated_predict = float(g*(model_para[0] + model_para[1]*g +
                                    + model_para[2]*math.log(g)))
    return power_generated_predict
