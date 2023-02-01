"""
Created on Sat Mar 19 15:33:01 2022

@author: brile
"""
import os

import pandas as pd
from photoreactor.data_analysis import analysis_tools
from photoreactor.equipment.experiment_control import Experiment


def get_expt_list(file_path):
    """
    Get list of experiments.

    Parameters
    ----------
    file_path : str
        path to directory containing experiment logs

    Returns
    -------
    expt_list : list
        list of experiment log paths
    """
    expt_list = []
    for dirpath, dirnames, filenames in os.walk(file_path):
        for filename in filenames:
            if filename == 'expt_log.txt':
                log_path = os.path.join(dirpath, filename)
                expt_path = os.path.dirname(log_path)
                print('found')
                expt = Experiment()  # Initialize experiment obj
                expt.read_expt_log(log_path)  # Read expt parameters from log
                expt_list.append(expt)
    return expt_list


if __name__ == "__main__":
    # User inputs
    ###########################################################################

    # Calibration Location Info:
    # Format [ChemID, slope, intercept, start, end]

    # We need to put the calibration data somewhere thats accessible with a common path

    calibration_path = ("G:\\Shared drives\\Photocatalysis Reactor\\"
                        "Reactor Baseline Experiments\\GC Calibration\\"
                        "20210930_DummyCalibration\\HayN_FID_C2H2_DummyCal.csv")
    # import all calibration data
    calDF = pd.read_csv(calibration_path, delimiter=',', index_col='Chem ID')

    # Sample Location Info:
    main_dir = (r'G:\Shared drives\Photocatalysis Projects\AgPd Polyhedra'
                r'\Ensemble Reactor')

    expt1 = (r'20220602_Ag5Pd95_6wt%_3.45mg_sasol900_300C_3hr\postreduction'
             r'\20220618comp_sweep_340K_0.0mW_50sccm')

    # Main Script
    ###########################################################################
    for expt_path in [expt1]:
        file_path = os.path.join(main_dir, expt_path)
        # Here i'm only sending paths w/ 1 expt
        expt = get_expt_list(file_path)[0]

        (results, avg, std) = analysis_tools.load_results(expt)
        avg.index = [0.5, 1, 2, 5, 10, 15, 20, 30, 40]
        std.index = [0.5, 1, 2, 5, 10, 15, 20, 30, 40]
        expt.expt_list['Units'][2] = 'H2/C2H2'
        (ax1, ax2, ax3) = analysis_tools.plot_results(expt, calDF,
                                                      (results, avg, std),
                                                      s=['c2h4'], mass_bal='C',
                                                      reactant='c2h2',
                                                      figsize=(4.35, 3.25),
                                                      savedata='False')

        # Standard figsize
        # 1/2 slide = (6.5, 4.5);  1/6 slide = (4.35, 3.25);
        # 1/4 slide =  (5, 3.65); Full slide =    (9, 6.65);

        # avg.index= [0.5, 1, 2, 5, 10, 15, 20]
        # std.index= [0.5, 1, 2, 5, 10, 15, 20]
        # expt.expt_list['Units'][2]= 'H2/C2H2'
        # replot
    print('Finished!')
