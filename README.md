# GreenFPGA

Tool to evaluate the carbon footprint of FPGA-based computing across its lifetime. The tool can also perform comparisons with ASIC counterpart. 

![LifeCycle](images/fpga-lifecycle.png)

<!--- <img src="images/greenfga-arch.png" alt="drawing" width="600"/> --->
![GreenFPGA](images/greenfga-arch.png)


## Abstract

## Table of Contents

## File Structure 
Add this with links 
```
├── LICENSE
├── README.md
├── src
│   ├── CO2_func.py
│   ├── ECO_chip.py
│   └── tech_scaling.py
├── tech_params
│   ├── analog_scaling.json
│   ├── beol_feol_scaling.json
│   ├── cpa_scaling.json
│   ├── defect_density.json
│   ├── dyn_pwr_scaling.json
│   ├── gates_perhr_scaling.json
│   ├── logic_scaling.json
│   ├── sram_scaling.json
│   └── transistors_scaling.json
└── test_example
    ├── Agilex
    │   ├── appdev.json
    │   ├── area.json
    │   ├── designC.json
    │   ├── eol.json
    │   ├── node_list.txt
    │   ├── operationalC.json
    │   └── packageC.json
    ├── ASIC_analysis
    │   ├── appdev.json
    │   ├── area.json
    │   ├── designC.json
    │   ├── eol.json
    │   ├── node_list.txt
    │   ├── operationalC.json
    │   └── packageC.json
    ├── FPGA_analysis
    │   ├── appdev.json
    │   ├── area.json
    │   ├── designC.json
    │   ├── eol.json
    │   ├── node_list.txt
    │   ├── operationalC.json
    │   └── packageC.json
    ├── Moffett
    │   ├── appdev.json
    │   ├── area.json
    │   ├── designC.json
    │   ├── eol.json
    │   ├── node_list.txt
    │   ├── operationalC.json
    │   └── packageC.json
    ├── Stratix
    │   ├── appdev.json
    │   ├── area.json
    │   ├── designC.json
    │   ├── eol.json
    │   ├── node_list.txt
    │   ├── operationalC.json
    │   └── packageC.json
    └── TPU
        ├── appdev.json
        ├── area.json
        ├── designC.json
        ├── eol.json
        ├── node_list.txt
        ├── operationalC.json
        └── packageC.json
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

![DNN-Sweep](images/dnn.png)

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
![ASIC-FPGA](images/asic_fpga_app.png)

Add result runs 

Add Citation 

