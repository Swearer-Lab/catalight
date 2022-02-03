# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 09:25:10 2022

@author: brile
"""
import pandas as pd
import gc_analysis
import os
import sys

# getting the name of the directory where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to the sys.path.
sys.path.append(parent)

from experiment_control import Experiment

if __name__ == "__main__":

    # User inputs
    ###########################################################################
    # Calibration Location Info:
    # Format [ChemID, slope, intercept, start, end]
    calibration_path = ("G:\\Shared drives\\Photocatalysis Reactor\\"
                        "Reactor Baseline Experiments\\GC Calibration\\"
                        "calib_202012\\HayD_FID_Sophia_RawCounts.csv")

    # Sample Location Info:
    main_dir = r"C:\Users\brile\Documents\Temp Files\Calibration_dummy\20220203calibration_273K_0.0mW_50sccm"

    # Main Script
    ###########################################################################

    log_path = os.path.join(main_dir, 'expt_log.txt')
    expt_path = os.path.dirname(log_path)
    # import all calibration data
    calDF = pd.read_csv(
        calibration_path, delimiter=',', index_col='Chem ID')
    Expt1 = Experiment()  # Initialize experiment obj
    Expt1.read_expt_log(log_path)  # Read expt parameters from log
    Expt1.update_save_paths(expt_path)  # update file paths

    subplots1, subplots2 = gc_analysis.analyze_cal_data(Expt1, calDF)
# Standard figsize
# 1/2 slide = (6.5, 4.5);  1/6 slide = (4.35, 3.25);
# 1/4 slide =  (5, 3.65); Full slide =    (9, 6.65);
    print('Finished!')
