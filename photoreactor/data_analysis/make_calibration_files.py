'''
This script was initially used to generate a "dummy" calibration experiment
using data collected before calibration expeirments were automated. Use this
script if you have calibration data that is not organized in the appropriate
data structure. This will create expt log file and data layout. then copy paste
calibration data into appropriate folders.
'''


from photoreactor.equipment.experiment_control import Experiment
import numpy as np
if __name__ == "__main__":
    main_fol = "/Users/ccarlin/Documents/calibration"

    expt = Experiment()
    expt.expt_type = 'calibration'
    expt.gas_type = ['CalGas', 'Ar', 'H2']
    expt.temp = [273]
    P_CalGas = np.array([100, 50, 10]) / 100   # pretend one 1000ppm gas
    P_H2 = P_CalGas * 0
    P_Ar = 1 - P_CalGas - P_H2
    expt.gas_comp = np.stack([P_CalGas, P_Ar, P_H2], axis=1).tolist()
    expt.tot_flow = [50]
    expt.sample_name = '20220418_caltest'
    expt.plot_sweep()
    expt.create_dirs(main_fol)
    print('finished expt5')
