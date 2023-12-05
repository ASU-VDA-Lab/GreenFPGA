# GreenFPGA

Tool to evaluate the carbon footprint of FPGA-based computing across its lifetime. The tool can also perform comparisons with ASIC counterpart. 

 <img src="images/fpga-lifecycle.png" alt="drawing" width="600"/> 

 <img src="images/greenfga-arch.png" alt="drawing" width="600"/> 


## Abstract

## Table of Contents

-   [Directory structure](#directory-structure)
-   [Getting started](#getting-started)
-   [Key parameters](#key-parameters)
-   [Running GreenFPGA](#running-greenfpga)
-   [Outputs](#outputs)

## Directory Structure 
Add this with links 




- **src/**
  - [CO2_func.py](./src/CO2_func.py)
  - [ECO_chip.py](./src/ECO_chip.py)
  - [tech_scaling.py](./src/tech_scaling.py)
- **tech_params**
  - [beol_feol_scaling.json](./tech_params/beol_feol_scaling.json)
  - [cpa_scaling.json](./tech_params/cpa_scaling.json)
  - [defect_density.json](./tech_params/defect_density.json)
  - [dyn_pwr_scaling.json](./tech_params/dyn_pwr_scaling.json)
- [LICENSE](.LICENSE)
- [README.md](README.md)
- **test_example**
  - **Agilex**
    - [fpga_spec.json](./test_example/Agilex/fpga_spec.json)
    - [green_fpga_param.json](./test_example/Agilex/green_fpga_param.json)
    - [node_list.txt](./test_example/Agilex/node_list.txt)
  - **ASIC_analysis**
    - [fpga_spec.json](./test_example/ASIC_analysis/fpga_spec.json)
    - [green_fpga_param.json](./test_example/ASIC_analysis/green_fpga_param.json)
    - [node_list.txt](./test_example/ASIC_analysis/node_list.txt)
  - **FPGA_analysis**
    - [fpga_spec.json](./test_example/FPGA_analysis/fpga_spec.json)
    - [green_fpga_param.json](./test_example/FPGA_analysis/green_fpga_param.json)
    - [node_list.txt](./test_example/FPGA_analysis/node_list.txt)
  - **Moffett**
    - [fpga_spec.json](./test_example/Moffett/fpga_spec.json)
    - [green_fpga_param.json](./test_example/Moffett/green_fpga_param.json)
    - [node_list.txt](./test_example/Moffett/node_list.txt)
  - **Stratix**
    - [fpga_spec.json](./test_example/Stratix/fpga_spec.json)
    - [green_fpga_param.json](./test_example/Stratix/green_fpga_param.json)
    - [node_list.txt](./test_example/Stratix/node_list.txt)
  - **TPU**
    - [fpga_spec.json](./test_example/TPU/fpga_spec.json)
    - [green_fpga_param.json](./test_example/TPU/green_fpga_param.json)
    - [node_list.txt](./test_example/TPU/node_list.txt)
- **images**
  - [asic_fpga_app.png](./images/asic_fpga_app.png)
  - [dnn.png](./images/dnn.png)
  - [fpga-ligecycle.png](./images/fpga-lifecycle.png)
  - [greenfpga-arch.png](./images/greenfga-arch.png)




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

## Getting started

## Key parameters

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

## Running GreenFPGA
 
 <img src="images/asic_fpga_app.png" alt="drawing" width="600"/> 

## Outputs

Add result runs 

Add Citation 

