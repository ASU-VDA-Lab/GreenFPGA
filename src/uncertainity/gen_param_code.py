import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from matplotlib import font_manager
import pandas as pd
import joblib
import argparse
import time
from scipy.stats import mode

from params_prob import *
#from ECO_function import *

en_plot = False
debug = True
#sample_size = 10
sample_size = 50


##############
dd = defden_kde_gen(sample_size)
print(len(dd)) if debug else None
find_prob(dd) if debug else None
print("Mean dd:",np.mean(dd)) if debug else None
print("Mode dd:",mode(dd)) if debug else None

if en_plot:
    dd_x,dd_y = mean_calc_plot(dd)
    plot_trend(dd_x,dd_y,'main dd xaxis','main dd yaxis','Main file',f"defden_{sample_size}")
    plot_hist(dd,f"defden_hist_{sample_size}")
    find_prob(dd)
###############

epa_v = epa_kde_gen(sample_size)
print(len(epa_v)) if debug else None
find_prob(epa_v) if debug else None
print("Mean epa:",np.mean(epa_v)) if debug else None
print("Mode epa:",mode(epa_v)) if debug else None

if en_plot:
    epa_x,epa_y = mean_calc_plot(epa_v)
    #epa_x,epa_y = smooth_uncertainity(epa)
    plot_trend(epa_x,epa_y,'main epa xaxis','main epa yaxis','Main file',f"epa_{sample_size}")
    plot_hist(epa_v,f"epa_hist_{sample_size}")
    find_prob(epa_v)
################

ci = ci_taiwan_kde(sample_size)
print(len(ci)) if debug else None
find_prob(ci) if debug else None
print("Mean ci:",np.mean(ci)) if debug else None
print("Mode ci:",mode(ci)) if debug else None

if en_plot:
    ci_x,ci_y = mean_calc_plot(ci)
    plot_trend(ci_x,ci_y,'main ci xaxis','main ci y axis','Main file',f"ci_tw_{sample_size}")
    plot_hist(ci,f"ci_tw_hist_{sample_size}")
    find_prob(ci)
###############

gpa = gpa_func_gen(sample_size)
print(len(gpa))  if debug else None 
print(type(gpa))
find_prob(gpa) if debug else None
print("Mean gpa:",np.mean(gpa)) if debug else None
print("Mode gpa:",mode(gpa)) if debug else None

if en_plot:
    gpa_x,gpa_y = mean_calc_plot(gpa)
    plot_trend(gpa_x,gpa_y,'main_gpa xaxis','main_gpa y axis','Main file',f"gpa_{sample_size}")
    plot_hist(gpa,f"gpa_hist_{sample_size}")
    find_prob(gpa)
####################

#Creating a dict 
params_data = {
    'GPA' : gpa,
    'EPA' : epa_v,
    'CarbonInt' : ci,
    'defden' : dd
}

#Converting to DataFrame
params_df = pd.DataFrame(params_data)

#Explorting to xlsx
params_df.to_excel(f"example_final_params_data_{sample_size}.xlsx",index=False)