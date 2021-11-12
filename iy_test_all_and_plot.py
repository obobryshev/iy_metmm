#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import iy_MPM2020m
#import iy_TRE05m


def build_results_path(model="TRE05", tt_model="2021-08-29_0126"):
    """
    model = "O2-TRE05"
    model = "O2-MPM2020"
    model = "O2-AER"
    """
    from os.path import join    
    
    main_path = "/home/sasha/progs/oxygen_study/iy_metmm/Output"
    
    results = join(
        main_path, 
        "iy_" + model + "_midlat-s_" + tt_model + ".xml"
    )
    
    fgrid = join(
        main_path,
        "fgrid_" + model + "_" + tt_model + ".xml"
        
    )
    
    res_path = list()
    res_path.append(results)
    res_path.append(fgrid)    
    
    return res_path


def read_arts_output_models():
    """


    Returns
    -------
    iy : list
        DESCRIPTION.
    fgrid : np.array 1-D
        DESCRIPTION.

    """    
    import numpy as np
    from pyarts import xml
    
   
    #tt_tre = iy_TRE05m.main(verbosity=1)
    
    tt_tre = "2021-08-29_0126"
    tt_aer = '2021-08-29_1241'
    tt_mpm = "2021-08-29_0205"
    
    l_tre = build_results_path(model="O2-TRE05",  tt_model=tt_tre)
    l_aer = build_results_path(model="O2-AER",    tt_model=tt_aer)
    l_mpm = build_results_path(model="O2-MPM2020", tt_model=tt_mpm)
    
    
    iy = list()
    iy.append(np.squeeze(xml.load(l_tre[0])))
    iy.append(np.squeeze(xml.load(l_aer[0])))
    iy.append(np.squeeze(xml.load(l_mpm[0])))
    fgrid = xml.load(l_tre[1])/1e9
    
    return iy, fgrid
        

def plot_5_500GHz(iy, fgrid):
    import matplotlib.pyplot as plt
    #import numpy as np
    
    fig, ax = plt.subplots()
    ax.plot(fgrid,  iy[0],  label = 'TRE05' )
    ax.plot(fgrid,  iy[1],  label = 'AER' )
    ax.plot(fgrid,  iy[2],  label = 'MPM2020' )
    ax.set_xlabel('Frequency, GHz') #,  fontsize = 12)
    ax.legend()
    plt.show()
    
    fig2, ax2 = plt.subplots()
    ax2.plot(fgrid,  iy[2]-iy[0],  label = 'MPM-TRE05' )
    ax2.plot(fgrid,  iy[1]-iy[0],  label = 'AER-TRE05' )
    ax2.set_xlabel('Frequency, GHz') #,  fontsize = 12)
    ax2.legend()
    plt.show()    
    
    return
    

def plot_any_range(iy, fgrid, start=50, end=60):
    import matplotlib.pyplot as plt
    #import numpy as np

    # Apply mask to subselect fgrid 50-60 GHz    
    mmask = (fgrid>start) & (fgrid<end)
    fgrid = fgrid[mmask]
    b = list()
    for f in iy:
        b.append(f[mmask])
    iy = b.copy()
    
    fig, ax = plt.subplots()
    ax.plot(fgrid,  iy[0],  label = 'TRE05' )
    ax.plot(fgrid,  iy[1],  label = 'AER' )
    ax.plot(fgrid,  iy[2],  label = 'MPM2020' )
    ax.set_xlabel('Frequency, GHz') #,  fontsize = 12)
    ax.legend()
    plt.show()
    
    fig2, ax2 = plt.subplots()
    ax2.plot(fgrid,  iy[2]-iy[0],  label = 'MPM-TRE05' )
    ax2.plot(fgrid,  iy[1]-iy[0],  label = 'AER-TRE05' )
    ax2.set_xlabel('Frequency, GHz') #,  fontsize = 12)
    ax2.legend()
    plt.show()   


def main():
    # TRE, AER, MPM
    iy, fgrid = read_arts_output_models()
    #plot_5_500GHz(iy, fgrid)
    plot_any_range(iy, fgrid, start=160, end=200)
    pass
    


if __name__ == "__main__":
    main()
    #pass
    