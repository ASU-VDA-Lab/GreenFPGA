import pandas as pd
import json



tech_indices = [  7,  10,  14,  22,  28]
def load_tables():

   
    with open("tech_params/logic_scaling.json",'r') as logic_sc:
        LOGIC_scaling_table = json.load(logic_sc)
    logic_scaling = pd.DataFrame(data=LOGIC_scaling_table, index=tech_indices) 
    
    with open("tech_params/analog_scaling.json",'r') as analog_sc:
        analog_scaling_table = json.load(analog_sc)
    analog_scaling = pd.DataFrame(data=analog_scaling_table, index=tech_indices)
  
    with open("tech_params/sram_scaling.json",'r') as sram_sc:
        sram_scaling_table = json.load(sram_sc)
    sram_scaling = pd.DataFrame(data=sram_scaling_table, index=tech_indices)
    
    tech_indices_package = tech_indices + [65]
    with open("tech_params/defect_density.json",'r') as def_sc:
        def_scaling_table = json.load(def_sc)
    defect_density = pd.DataFrame(data=def_scaling_table,index=tech_indices_package)
    
    with open("tech_params/cpa_scaling.json",'r') as cpa_sc:
        cpa_scaling_table = json.load(cpa_sc)
    cpa = pd.DataFrame(data=cpa_scaling_table,index=tech_indices_package)
    
    
    with open("tech_params/beol_feol_scaling.json",'r') as beolfeol_sc:
        beolfeol_scaling_table = json.load(beolfeol_sc)
    beolVfeol = pd.DataFrame(data=beolfeol_scaling_table,index=tech_indices_package)

    with open("tech_params/dyn_pwr_scaling.json",'r') as dyn_sc:
        dyn_scaling_table = json.load(dyn_sc)
    dyn_pwr_ratio = pd.DataFrame(data=dyn_scaling_table,index=tech_indices_package)
    
    
    return {
            "logic": logic_scaling,
            "analog": analog_scaling,
            "sram": sram_scaling, 
            "cpa" : cpa,
            "defect_den": defect_density,
            "beolVfeol" : beolVfeol,
            "dyn_pwr_ratio" : dyn_pwr_ratio
        }
    
    
    
