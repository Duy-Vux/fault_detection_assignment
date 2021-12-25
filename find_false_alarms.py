#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 1 

Template File for find_false_alarms

@author: 
"""


def find_false_alarms(your_fault_list,true_fault_list):
    false_alarm_list = []
    # if len(true_fault_list) == 0:
    #     false_alarm_list = your_fault_list
    # else:
    #     x = 1
    #     for k in range(len(your_fault_list)):
    #         while your_fault_list[k] != true_fault_list[x-1]:
    #             if x == len(true_fault_list):
    #                 false_alarm_list.append(your_fault_list[k])
    #                 break
    #             else:
    #                 x += 1
    
    for k in range(len(your_fault_list)):
        if not your_fault_list[k] in true_fault_list:
            false_alarm_list.append(your_fault_list[k])
    return false_alarm_list
        
            
            
