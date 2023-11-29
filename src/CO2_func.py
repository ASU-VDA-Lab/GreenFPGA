import numpy as np
import itertools as it
from   matplotlib import pyplot as plt
import math
from tech_scaling import *

##############################################
#Yeild Calculation 
def yield_calc(area, defect_density):
    yield_val = (1+(defect_density*1e4)*(area*1e-6)/10)**-10
    return yield_val

################################################


def recursive_split(areas, axis=0, emib_pitch=10):
    sorted_areas = np.sort(areas[::-1])
    if len(areas)<=1:
        v = (np.sum(areas)/2)**0.5
        size_2_1 = np.array((v + v*((axis+1)%2), v +axis*v))
#         print("single", axis, size_2_1)
        return size_2_1, 0
    else:
        sums = np.array((0.0,0.0))
        blocks= [[],[]]
        for i, area in enumerate(sorted_areas):
            blocks[np.argmin(sums)].append(area)
            sums[np.argmin(sums)] += area
#         print("blocks",axis, blocks)
        left, l_if = recursive_split(blocks[0], (axis+1)%2, emib_pitch)
#         print("left",axis, left)
        right, r_if = recursive_split(blocks[1], (axis+1)%2, emib_pitch)
#         print("right",axis, right)
        sizes = np.array((0.0,0.0))
        sizes[axis] = left[axis] + right[axis] + 0.5
        sizes[(axis+1)%2] = np.max((left[(axis+1)%2], right[(axis+1)%2]))
        t_if = l_if + r_if 
        t_if += np.ceil(np.min((left[(axis+1)%2], right[(axis+1)%2]))/emib_pitch) # for overlap 1 interface per 10mm
        return sizes, t_if


################################################
#TODO : Remove comments 
#wastage_add = will add extra si CFP wastage based on Formulae

def Si_chip(techs, types, areas,scaling_factors,Transistors_per_gate=8,Power_per_core=10,Carbon_per_kWh=700,packaging=False, always_chiplets=False,wastage_add = False,wafer_dia=450,
            rcy_mat_frac = 0,rcy_cpa_frac = 0.4):
    area = np.array(areas)
    cpa =  np.array([scaling_factors['cpa'].loc[c, 'cpa'] for c in techs])
#     delay =  np.array([scaling_factors[ty].loc[techs[i], 'delay'] for i, ty in enumerate(types)])
    if not packaging:
        area_scale = np.array([scaling_factors[ty].loc[techs[i], 'area'] for i, ty in enumerate(types)])
        #OLD design_carbon = design_costs(areas*area_scale, techs,scaling_factors,Transistors_per_gate,Power_per_core,Carbon_per_kWh)
        design_carbon = 0
        defect_den = scaling_factors['defect_den']
    else:
        design_carbon = 0
        defect_den = scaling_factors['defect_den']/4 # packaing has lower density 
        #Cost-effective design of scalable high-performance systems using active and passive interposers
        area_scale = np.ones_like(area)
    
    if (np.all(np.array(techs) == techs[0]) and  not always_chiplets):
        yields = yield_calc((area*area_scale).sum(), defect_den.loc[techs[0],'defect_density'])
        wastage_extra_cfp=0
        if wastage_add:
            wastage_extra_cfp = Si_wastage_accurate_t(wafer_dia=wafer_dia,chip_area=(area*area_scale).sum(),techs=techs,cpa_factors=scaling_factors['cpa'].loc[techs[0],'cpa'])
            wastage_extra_cfp = (wastage_extra_cfp * area) / area.sum()
    else:
        yields = np.zeros_like(techs,dtype=float)
        wastage_extra_cfp=np.zeros(len(techs))
        for i, c in enumerate(techs):   
            yields[i] = yield_calc(areas[i]*area_scale[i], scaling_factors['defect_den'].loc[c,'defect_density'])
#         print("yields:", yields)
            if wastage_add:
                wastage_extra_cfp[i] = Si_wastage_accurate_t(wafer_dia=wafer_dia,chip_area=areas[i]*area_scale[i],techs=techs[i],cpa_factors=scaling_factors['cpa'].loc[techs[i],'cpa'])
    
    mfg_carbon = area_scale*cpa*area / yields
    mfg_wst_carbon = mfg_carbon+wastage_extra_cfp
    if wastage_add:
        carbon = mfg_wst_carbon
    else:
        carbon = mfg_carbon
   
    carbon = ((1-rcy_mat_frac)*carbon) + (rcy_mat_frac*carbon*rcy_cpa_frac)
    return carbon, design_carbon, area_scale

###############################################
#TODO 

def power_chip(techs, types, scaling_factors,powers, lifetime, activity,Carbon_per_kWh):
    active = activity[0]
    on = activity[1]
    avg_pwr = activity[2]
    powers_in = np.array(powers)
    dyn_ratio =  np.array([scaling_factors['dyn_pwr_ratio'].loc[c, 'dyn_pwr_ratio'] for c in techs])
    pwr_scale = np.array([scaling_factors[ty].loc[techs[i], 'power'] for i, ty in enumerate(types)])
    powers_tech_scaled = powers_in * pwr_scale
    powers_scaled = powers_tech_scaled*on*avg_pwr*(dyn_ratio*active + (1-dyn_ratio))
    energy = lifetime*powers_scaled/1000
    op_carbon = Carbon_per_kWh * energy
    return op_carbon,powers_scaled 

###############################################

def end_cfp(cpa_dis_p_Ton, cpa_rcy_p_Ton, dis_frac, weight_p_die):
    cpa_dis_p_gm = cpa_dis_p_Ton/1000 
    cpa_rcy_p_gm = cpa_rcy_p_Ton/1000
    dis_cfp = cpa_dis_p_gm*weight_p_die
    rcy_cfp = cpa_rcy_p_gm*weight_p_die
    eol_cfp = (dis_frac*dis_cfp)-((1-dis_frac)*rcy_cfp)
    return eol_cfp

###############################################
#TODO : Remove comments 



def Interposer(areas, techs, types, scaling_factors, package_type="passive", always_chiplets=False,
               interposer_node=65, tsv_pitch=0.025, tsv_size=0.005, RDLLayers=6, EMIBLayers=5, 
               emib_pitch=10, numBEOL=8, transistors_per_gate=8, power_per_core=10,
               carbon_per_kWh=700, return_router_area=False
              ):
    #TBD 
    # passive interposer
    #1. Bonding yield  - 99% from "Cost-effective design of scalable high-performance systems using active and passive interposers"
    #2. Router overhead
    #3. Area overhead  -10% from "Cost-effective design of scalable high-performance systems using active and passive interposers"
    #4. 65 nm defect density, 
    #5. pacage defect density
    #6. 65nm carbon per area
    #7. packaging yield adjustments
    package_carbon = 0 
    router_carbon = 0 
    router_design = 0
    bonding_yield = 0.99
    router_area =0
    pkg_en = False
    if(pkg_en) :
        #################
        num_chiplets = len(areas)
        interposer_area, num_if = recursive_split(areas, emib_pitch=emib_pitch)
        num_if = int(np.ceil(num_if))
        interposer_area = np.prod(interposer_area) 
        interposer_carbon, _, _ = Si_chip([interposer_node], ["logic"], [interposer_area],scaling_factors,
                                  transistors_per_gate, power_per_core,carbon_per_kWh, True, always_chiplets)   
        package_carbon = interposer_carbon* scaling_factors['beolVfeol'].loc[interposer_node,'beolVfeol']
        ################

    package_carbon /= bonding_yield 
    router_carbon /= bonding_yield
    
    if return_router_area:
        return package_carbon, router_carbon, router_design, router_area
    else:
        return package_carbon, router_carbon, router_design


###############################################
#TODO : Remove comments 

def plot_packaging_carbon(carbon,labels):
    carbon.plot(kind='bar', stacked=False, figsize = (21,7),
        title='Packaging CO2 overhead manufacturing')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    
    plt.figure()
    ax = carbon[[x for x in labels if 'passive' in x]].plot.bar(
            stacked=True, figsize=(21,7), color=['tab:blue','tab:orange'], position=0, width=0.2)
    carbon[[x for x in labels if 'active' in x]].plot.bar(
            stacked=True, sharex=True, ax=ax, position=1, width=0.2, color=['tab:green','tab:red'])
    carbon[[x for x in labels if 'RDL' in x]].plot.bar(
            stacked=True, sharex=True, ax=ax, position=2, width=0.2, color=['tab:purple','tab:brown'])
    carbon[[x for x in labels if 'EMIB' in x]].plot.bar(
            stacked=True, sharex=True, ax=ax, position=3, width=0.2, color=['tab:pink','tab:cyan'])
    legend = ax.legend(labels, fontsize=12)#, loc='center left', bbox_to_anchor=(1.0, 0.93))
    plt.show()


    


###############################################
#Wastage calculation 

def Si_wastage_accurate_t(wafer_dia,chip_area,techs,cpa_factors):
    si_area = (math.pi * (wafer_dia ** 2))/4
    dpw = math.pi * wafer_dia * ((wafer_dia/(4*chip_area)) - (1/math.sqrt(2*chip_area)))
    area_wastage = si_area - (math.floor(dpw)*chip_area)
    unused_si_cfp = area_wastage*cpa_factors
    wastage_si_cfp_pdie = unused_si_cfp/dpw
    return wastage_si_cfp_pdie

###############################################

###############################################
#Programming CFP 

def app_cfp(power_per_core,num_core,Carbon_per_kWh,Na,Ns,fe_time,be_time,config_time):
    prog_time = ((Na*(fe_time+be_time)) + (Ns*config_time)) * 24*30 #Converting to hrs from months 
    program_energy = power_per_core*num_core*prog_time/1000 #in kWh
    prog_cfp = program_energy*Carbon_per_kWh
    return prog_cfp

###############################################

###############################################
#Design CFP 

def design_cfp_new(e_per_person_per_yr, total_employee, c_p_kWh, gate_scale):
    total_cfp_p_per = (e_per_person_per_yr*1000*700)
    total_co2 = total_cfp_p_per*total_employee*gate_scale #1000 to convert MWh to kWh
    new_des_cfp = total_co2
    #print("total_cfp_p_per",total_cfp_p_per)
    #print("total_co2",total_co2)
    return new_des_cfp


###############################################
#TODO : remove comments 

def calculate_CO2(design, scaling_factors, techs, design_name='', num_iter=90, package_type='RDL', always_chiplets=False,
                  lifetime = 2*365*24, activity=[0.2, 0.667, 0.1], Ns = 1e5, Nc=None, plot=False,package_factor=1,
                  return_ap=False, in_combinations=None, transistors_per_gate=8, power_per_core=10, carbon_per_kWh=700,
                  interposer_node=65, rdl_layer = 6, emib_layers = 5, emib_pitch=10, tsv_pitch = 0.025,
                  tsv_size = 0.005, num_beol = 8,  Na = 5, t_app_fe = 2.5, t_app_be = 1, Nt = 1,
                  t_app_config = 0, app_Carbon_per_kWh = 700, Num_core = 8, Pc = 10,
                  rcy_frac = 0, rcy_cpa_frac = 0.4 , cpa_dis_ton = 390, cpa_rcy_ton = 790, dis_frac = 1, die_weight = 2,
                  energy_pp_yr = 0.4625,tot_emp = 16000, gate_sc = 1
                 ):
    #num_iter = 90
    
    if in_combinations is None:
        combinations = list(it.product(techs, repeat=len(design.index)))
    else:
        combinations = in_combinations
    design_carbon = np.zeros((len(combinations), len(design.index)+1))
    op_carbon = np.zeros((len(combinations), len(design.index)+1))
    carbon = np.zeros((len(combinations), len(design.index)+1))
    
    areas=  np.zeros((len(combinations), len(design.index)))
    powers =  np.zeros((len(combinations), len(design.index)))
    for n, comb in enumerate(combinations):
        carbon[n,:-1], design_carbon[n,:-1], area_scale = Si_chip(techs=comb, types=design.type.values,
                                                                  areas=design.area.values,scaling_factors=scaling_factors, Transistors_per_gate=transistors_per_gate,
                                                                  Power_per_core=power_per_core,Carbon_per_kWh=carbon_per_kWh, always_chiplets=always_chiplets,wastage_add=True,
                                                                  rcy_mat_frac=rcy_frac , rcy_cpa_frac=rcy_cpa_frac)
        package_c, router_c, design_carbon[n,-1], router_a =Interposer(areas=design.area.values*area_scale, techs=comb, types=design.type.values,scaling_factors=scaling_factors,
                                          package_type=package_type, always_chiplets=always_chiplets, interposer_node=interposer_node,
                                          tsv_pitch=tsv_pitch, tsv_size=tsv_size, RDLLayers=rdl_layer, EMIBLayers=emib_layers, emib_pitch=emib_pitch, numBEOL=num_beol, 
                                          transistors_per_gate=transistors_per_gate,power_per_core=power_per_core,carbon_per_kWh=carbon_per_kWh,return_router_area=True)
        carbon[n, -1] = package_c*package_factor + router_c
         
        op_carbon[n,:-1], powers[n, :] = power_chip(comb, design.type.values,scaling_factors, design.power.values, lifetime, activity,Carbon_per_kWh=carbon_per_kWh)
        areas[n] =  design.area.values*area_scale +router_a
    if Nc is None:
        design_carbon *= num_iter/Ns
        total_carbon = carbon + design_carbon + op_carbon
    else:
        design_carbon *= num_iter/Nc[None,:]
        total_carbon = carbon + design_carbon + op_carbon
    carbon = pd.DataFrame(data=carbon, index=combinations, columns=(list(design.index) + ["Packaging"]))
    design_carbon = pd.DataFrame(data=design_carbon, index=combinations, columns=(list(design.index) + ["Packaging"]))
    op_carbon = pd.DataFrame(data=op_carbon, index=combinations, columns=(list(design.index) + ["Packaging"]))
    #     total_carbon =  carbon + (design_carbon*10/1e5)+ 0.8*(design_carbon*100/1e5)
    total_carbon = pd.DataFrame(data=total_carbon, index=combinations, columns=(list(design.index) + ["Packaging"]))
   
    #App-dev CFP
    app_dev_c = app_cfp(power_per_core=Pc, num_core=Num_core, Carbon_per_kWh=app_Carbon_per_kWh,
                        Na=Na,Ns=Ns,fe_time=t_app_fe,be_time=t_app_be,config_time=t_app_config)
 
    #Des
    design_carbon = design_cfp_new(energy_pp_yr,tot_emp,carbon_per_kWh,gate_sc)
    
    
    
    #Recycle CFP
    eol_c = end_cfp(cpa_dis_p_Ton=cpa_dis_ton, cpa_rcy_p_Ton=cpa_rcy_ton, dis_frac=dis_frac, weight_p_die=die_weight)
    
     

    
    if not return_ap:
        return carbon, design_carbon, total_carbon, op_carbon, app_dev_c, eol_c
    else:
        return carbon, design_carbon, total_carbon, op_carbon, app_dev_c, eol_c, areas, powers
    

###################

def total_cfp_gen(num_des,des_c_pu,mfg_c_pu,n_fpga,vol,eol_c_pu,ope_c_pu,app_c_tot,dc):
    design_cfp_total = num_des*des_c_pu
    mfg_cfp_total = n_fpga*(mfg_c_pu*num_des*vol)
    eol_cfp_total = n_fpga*(eol_c_pu*num_des*vol)
    ope_cfp_total = (n_fpga*(ope_c_pu*vol))*dc
    app_cfp_total = app_c_tot
    return design_cfp_total,mfg_cfp_total,eol_cfp_total,ope_cfp_total,app_cfp_total

###################