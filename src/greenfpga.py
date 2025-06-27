import numpy as np
from   tqdm import tqdm, trange
import pandas as pd 
import itertools as it 
from   matplotlib import pyplot as plt

#Importing all functions from CO2_func files
from CO2_func import * 
from tech_scaling import *

import argparse
import json
import ast



scaling_factors = load_tables()



parser = argparse.ArgumentParser(description='Provide a Carbon Foot Print(CFP) estimate ')
parser = argparse.ArgumentParser()
parser.add_argument(
        '--design_dir',
        default=None,
        help='use existing template for design_dir "--design_dir test_example/TPU"'
        )

parser.add_argument(
        '--num_app',
        default=None,
        help='Number of applications'
)
parser.add_argument(
        '--num_lifetime',
        default=None, 
        help='Lifetime of the chip'
)
parser.add_argument(
        '--num_des',
        default=None, 
        help='Number of designs'
)
parser.add_argument(
        '--nfpga',
        default=None, 
        help='N_Fpga =  AppSize/Fpga_cap'
)
parser.add_argument(
        '--power',
        default=None, 
        help='Chip Power'
)
parser.add_argument(
        '--chip_area',
        default=None, 
        help='Chip area'
)
parser.add_argument(
        '--ope_vol',
        default=None, 
        help='Operation Volume'
)
parser.add_argument(
        '--emb_vol',
        default=None, 
        help='Embodied Volume'
)
################
   
args = parser.parse_args()
design_dir = args.design_dir

##########
if args.num_app is not None : 
    NUM_App = int(args.num_app)
if args.num_lifetime is not None :
    NUM_Life = float(args.num_lifetime)
    NUM_Life = NUM_Life*24*365 #in hours
if args.nfpga is not None:
    NUM_fpga = int(args.nfpga)
if args.power is not None:
    chip_power = float(args.power)
if args.chip_area is not None:
    chip_area = int(args.chip_area)
if args.num_des is not None :
    NUM_des = int(args.num_des)
if args.ope_vol is not None :
    ope_volume = float(args.ope_vol)
if args.emb_vol is not None :
    emb_volume = int(args.emb_vol)

##########    

param_json_file = design_dir+'green_fpga_param.json'
fpga_spec_file = design_dir+'spec.json'
node_list_file = design_dir+'node_list.txt'
print("-------------------------")
print("Using below files ")
print(param_json_file)
print(fpga_spec_file)
print(node_list_file)
print("-------------------------")


with open(node_list_file , 'r') as file:
    nodes=file.readlines()
nodes = [ast.literal_eval(node_item) for node_item in nodes]
nodes = [data for inside_node in nodes for data in inside_node]



with open(fpga_spec_file,'r') as file:
    fpga_spec_json = json.load(file)
with open(param_json_file,'r') as file:
    param_json = json.load(file)
    
area = fpga_spec_json['area']

inp_des=pd.DataFrame()
inp_des.at['Logic','type'] = 'logic'
inp_des.at['Logic','area'] = area*0.74
inp_des.at['Analog/IO','type'] = 'analog'
inp_des.at['Analog/IO','area'] = area*0.16
inp_des.at['Memory','type'] = 'sram'
inp_des.at['Memory','area'] = area*0.1
design=inp_des


if args.chip_area is not None :
    design.at['Logic','area'] = chip_area*0.74 
    design.at['Analog/IO','area'] = chip_area*0.16
    design.at['Memory','area'] = chip_area*0.1
else :
    design = design



if args.power is not None :
    power = chip_power
else:
    power = float(fpga_spec_json['power'])
powers = design.area.values * power / design.area.values.sum()
num_iter = param_json['num_iter']
if args.emb_vol is not None :
    num_prt_mfg = emb_volume
else :
    num_prt_mfg = fpga_spec_json['num_prt_mfg']
transistors_per_gate = param_json['Transistors_per_gate']
power_per_core = param_json['Power_per_core']
carbon_per_kWh = param_json['Carbon_per_kWh']
recycle_frac = param_json['recycle_frac']
recycle_cpa_frac = param_json['recycle_cpa_frac']
total_emp = param_json['tot_emp']
gate_scale = param_json['gate_scale']
energy_pp_yr = param_json['epp_yr']

if args.num_app is not None :
    num_app = NUM_App
else :
    num_app = fpga_spec_json['num_app']

if args.num_des is not None :
    num_des = NUM_des
else :
    num_des = fpga_spec_json['num_des']


app_size = param_json['App_size']
fpga_cap = param_json['Fpga_cap']
FE_dev_time = param_json['FE_dev_time']
BE_dev_time = param_json['BE_dev_time']
num_fpga_types = param_json['num_fpga_types']
config_time = param_json['config_time']
cpu_pow_p_core = param_json['CPU_power_per_core']
num_core = param_json['num_CPU_cores']
app_Carbon_per_kWh = param_json['app_dev_Carbon_per_kWh']
if args.nfpga is not None:
    N_fpga = NUM_fpga
else :
    N_fpga = app_size/fpga_cap

dis_frac =     param_json['discard_frac']
Cdis_p_ton =   param_json['Cdis_per_ton']
Crec_per_ton = param_json['Crec_per_ton']
chip_weight =  param_json['chip_weight']


design.insert(loc=2,column='power',value=powers)
    
if args.num_lifetime is not None :
    lifetime = NUM_Life
else :
    lifetime = fpga_spec_json['lifetime']
dc = param_json['dc']
    
    
package_type =    param_json['pkg_type']
interposer_node = param_json['interposer_node']
rdl_layer =       param_json['rdl_layers']
emib_layers =     param_json['emib_layers']
emib_pitch =      param_json['emib_pitch']
tsv_pitch =       param_json['tsv_pitch']
tsv_size =        param_json['tsv_size']
numBEOL =         param_json['num_beol']

tech_indices2 = [  7,  10,  14,  22,  28]
analog_scale = {"area": [ 1, 1, 1, 1.974743319, 2.278875162], "power": [ 1, 1, 1, 1.497716895, 1.749333333]}
analog_df = pd.DataFrame(data=analog_scale,index=tech_indices2)
scaling_factors['analog'] = analog_df
logic_scale = {"area":  [ 1, 1.949555068, 3.709574145, 7.325456759, 8.453656378 ],"power": [ 1, 1.237623762, 1.524390244, 2.283105023, 2.666666667 ] }
logic_df = pd.DataFrame(data=logic_scale,index=tech_indices2)
scaling_factors['logic'] = logic_df
sram_scale = {"area": [1, 1, 1.902779873, 3.757501843, 4.336197791], "power": [1, 1, 1.231707317, 1.844748858,  2.154666667] }
sram_df = pd.DataFrame(data=sram_scale,index=tech_indices2)
scaling_factors['sram'] = sram_df



result = calculate_CO2(design,scaling_factors, nodes, 'Test Name',
                       num_iter,package_type=package_type ,Ns=num_prt_mfg,lifetime=lifetime,
                       carbon_per_kWh=carbon_per_kWh,transistors_per_gate=transistors_per_gate,
                       power_per_core=power_per_core,interposer_node = interposer_node, rdl_layer=rdl_layer, emib_layers=emib_layers,
                       emib_pitch=emib_pitch, tsv_pitch=tsv_pitch, tsv_size=tsv_size, num_beol=numBEOL,
                       Na = num_app, t_app_fe = FE_dev_time, t_app_be = BE_dev_time, Nt = num_fpga_types,
                       t_app_config = config_time, app_Carbon_per_kWh = app_Carbon_per_kWh, Num_core = num_core,
                       Pc = cpu_pow_p_core, rcy_frac = recycle_frac, rcy_cpa_frac = recycle_cpa_frac,
                       energy_pp_yr=energy_pp_yr,tot_emp=total_emp,gate_sc=gate_scale)

cdes = result[1] #Using from CO2.py 
cmfg = result[0].sum(axis=1)
ceol = result[5]
cope = result[3].sum(axis=1)
capp = result[4]


#Converting to Kgs
cdes = cdes/1000
cmfg = cmfg.iloc[0]/1000
ceol = ceol/1000
cope = cope.iloc[0]/1000
capp = capp/1000

des_c,mfg_c,eol_c,ope_c,app_c = total_cfp_gen(num_des=num_des,des_c_pu=cdes,mfg_c_pu=cmfg,n_fpga=N_fpga,
                                              vol=num_prt_mfg,eol_c_pu=ceol,ope_c_pu=cope,app_c_tot=capp,dc=dc)

    
    
#print(" Total CFP des:"+str(num_des)+"_app:"+str(num_app)+"_life:"+str(lifetime)+"_power:"+str(power)+"_area"+str(design.area.values.sum())+" Des mfg eol ope app")
emb_c = des_c+mfg_c+eol_c+app_c
tot=emb_c+ope_c
    
print("-------------------------")
print(f"Design    CFP : {des_c:e}")
print(f"Mfg       CFP : {mfg_c:e}")
print(f"EOL       CFP : {eol_c:e}")
print(f"Operation CFP : {ope_c:e}")
print(f"App Dev   CFP : {app_c:e}")
print("-------------------------")
print(f"Embodied  CFP : {emb_c:e}")
print(f"Operation CFP : {ope_c:e}")
print("-------------------------")
print(f"Total     CFP : {tot:e}")
print("-------------------------")
print(" ")
  