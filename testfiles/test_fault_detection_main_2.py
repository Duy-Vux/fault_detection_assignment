#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (20T1) 

You can use this file to test your fault_detection_main().

All test cases in this file either do not valid data or do not have enough data. 
The function fault_detection_main() is expected to return a string. 

This file containing four test cases which you can choose by
adjusting the variable test_num in Line 21. 

You can use this file to come out with additional tests. 
"""

# %% import 
import fault_detection_main as fd

# %% Tests 
test_num = 4

if test_num == 0:
        # Irradiance measurements in W/m^2 
    irradiance_time_series = [240.2, 220.1, 260.2, 280.7, 
                              320.3, 300.7, 267.1, 321.2,  
                              421.7, 476.2, 321.6, 329.7, 
                              407.9, 456.7, 489.3, 521.5]
    
    # Generated power measured in kW 
    power_time_series = [31.2,27.5,46.9,62.2]
    
    # Data sampling times in minutes 
    irradiance_sampling_time = 13
    power_sampling_time = 52.5 # <-- Invalid 
    
    # Parameters of the model to predict the power generated for
    # a given level of irradiance    
    model_para = [0.086, 3.44e-5, 3e-3]    
    
    # Margin in power measurment to decide whether it is a fault or not 
    margin = 5.2 # in kW 
    
    # expected answer
    expected_answer = 'Corrupted input'    
elif test_num == 1: 
    # expected answer
    expected_answer = [2, 3]
    # Irradiance measurements in W/m^2 
    irradiance_time_series = [240.2, 220.1, 260.2, 280.7, 256.5,
                              320.3, 300.7, 267.1, 321.2, 234.5, 
                              421.7, 476.2, 321.6, 329.7, 323.4,
                              407.9, 456.7, 489.3, 521.5, 534.6,
                              543.7, 567.5]
    
    # Generated power measured in kW 
    power_time_series = [31.2,27.5,55.5,44.2,58.38,53.52]
    
    # Data sampling times in minutes <-- 59 is not an integral multiple of 12
    irradiance_sampling_time = 12
    power_sampling_time = 59  
    
    # Parameters of the model to predict the power generated for
    # a given level of irradiance    
    model_para = [0.086, 3.44e-5, 3e-3]    
    
    # Margin in power measurment to decide whether it is a fault or not 
    margin = 10.0 # in kW 
    
    # expected answer
    expected_answer = 'Corrupted input'
elif test_num == 2: 
    # This is an example with both invalid parameters and not enough data
    # Should return 'Corrupted input'
    
    # Irradiance measurements in W/m^2 
    irradiance_time_series = [340.2, 330.1, 360.2, 
                              280.7, 256.5, 220.5, 
                              301.2, 277.3, 321.2, 
                              467.5, 421.7, 476.2, 
                              421.6, 429.7, 423.4,
                              507.9, 556.7, 589.3, 
                              521.5, 534.6, 543.7, 
                              567.5, 523.4, 513.7, 
                              534.3, 583.6]
    
    # Generated power measured in kW 
    power_time_series = []
    
    # Data sampling times in minutes 
    irradiance_sampling_time = 20
    power_sampling_time = 60 
    
    # Parameters of the model to predict the power generated for
    # a given level of irradiance    
    model_para = [0.071, 1.44e-5] # <-- Should have 3 entries  
    
    # Margin in power measurment to decide whether it is a fault or not 
    margin = 4.7 # in kW 
    
    # expected answer    
    expected_answer = 'Corrupted input'
elif test_num == 3:
    # Irradiance measurements in W/m^2 
    irradiance_time_series = [240.2, 220.1, 260.2] # <-- Not enough data
    
    # Generated power measured in kW 
    power_time_series = [29.13, 36.11, 41.81, 53.36]
    
    # Data sampling times in minutes 
    irradiance_sampling_time = 13
    power_sampling_time = 52 
    
    # Parameters of the model to predict the power generated for
    # a given level of irradiance    
    model_para = [0.086, 3.44e-5, 3e-3]    
    
    # Margin in power measurment to decide whether it is a fault or not 
    margin = 5.2 # in kW 
    
    # expected answer
    expected_answer = 'Not enough data'
    
# %% Run the function and check the answers     
    
your_answer = fd.fault_detection_main(irradiance_time_series,power_time_series,
                                      irradiance_sampling_time,power_sampling_time,
                                      model_para, margin)

print('Your function returns',your_answer)
print('The expected answer is',expected_answer)

if your_answer == expected_answer:
    print('Your answer is correct')
else:
    print('Your answer is not correct')        
        
