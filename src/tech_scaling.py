import pandas as pd
import json



tech_indices = [  7,  10,  14,  22,  28]
def load_tables():

   
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
            "cpa" : cpa,
            "defect_den": defect_density,
            "beolVfeol" : beolVfeol,
            "dyn_pwr_ratio" : dyn_pwr_ratio
        }
    
    
    
