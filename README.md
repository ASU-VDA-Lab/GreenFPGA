# GreenFPGA

Tool to evaluate the carbon footprint of FPGA-based computing across its lifetime. The tool can also perform comparisons with ASIC counterpart. 

 <img src="images/fpga-lifecycle.png" alt="drawing" width="600"/> 

 <img src="images/greenfga-arch.png" alt="drawing" width="600"/> 


## Abstract

## Table of Contents

## File Structure 
Add this with links 
```
├── images
│   ├── asic_fpga_app.png
│   ├── dnn.png
│   ├── fpga-lifecycle.png
│   └── greenfga-arch.png
├── LICENSE
├── README.md
├── src
│   ├── CO2_func.py
│   ├── ECO_chip.py
│   └── tech_scaling.py
├── tech_params
│   ├── beol_feol_scaling.json
│   ├── cpa_scaling.json
│   ├── defect_density.json
│   └── dyn_pwr_scaling.json
└── test_example
    ├── Agilex
    │   ├── fpga_spec.json
    │   ├── green_fpga_param.json
    │   └── node_list.txt
    ├── ASIC_analysis
    │   ├── fpga_spec.json
    │   ├── green_fpga_param.json
    │   └── node_list.txt
    ├── FPGA_analysis
    │   ├── fpga_spec.json
    │   ├── green_fpga_param.json
    │   └── node_list.txt
    ├── Moffett
    │   ├── fpga_spec.json
    │   ├── green_fpga_param.json
    │   └── node_list.txt
    ├── Stratix
    │   ├── fpga_spec.json
    │   ├── green_fpga_param.json
    │   └── node_list.txt
    └── TPU
        ├── fpga_spec.json
        ├── green_fpga_param.json
        └── node_list.txt
```

Explain about these parameters, that can be added along with the command for faster analysis 
```
--design_dir : Directory for desing analysis 
--num_app : Number of app 
--num_lifetime : Total evaluation lifetime 
--num_des : Number of designs, quite differnt from num_app as it depends on type of device used (FPGA or ASIC) and analysis done
--nfpga : Number of FPGAs, Appsize/fpga_capacity 
--power : Power of the device 
--chip_area : Area of the device 
--ope_vol : Opertaion Volume 
--emb_vol : Embodied Volume
```
 <img src="images/dnn.png" alt="drawing" width="600"/> 

Explain about each input parameter files and parameters used 
```
        ├── appdev.json
        ├── area.json
        ├── designC.json
        ├── eol.json
        ├── node_list.txt
        ├── operationalC.json
        └── packageC.json
```
 <img src="images/asic_fpga_app.png" alt="drawing" width="600"/> 

Add result runs 

Add Citation 

