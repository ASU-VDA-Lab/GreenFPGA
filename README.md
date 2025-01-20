# GreenFPGA

GreenFPGA is a comprehensive framework for estimating the CFP of FPGAs over their lifecycle, considering uncertainties inherent in CFP modeling. The framework evaluates lifecycle CFP by accounting for the impacts of design, manufacturing, reconfigurability (reuse), operation, testing, disposal, and recycling. Using GreenFPGA, we evaluate scenarios in which the reconfigurability of FPGAs offsets embodied and operational CFP costs compared to application-specific integrated circuits (ASICs), graphics processing units (GPUs), and central processing units (CPUs). Additionally, we emphasize the importance of analyzing CFP across four platforms—FPGA, ASIC, GPU, and CPU while incorporating variables such as lifetime, usage time, volume, and number of applications. 

 <img src="images/greenfpga-lca.png" alt="drawing" width="600"/> 

## Table of Contents

-   [Abstract](#abstract)
-   [Getting started](#getting-started)
-   [Key parameters](#key-parameters)
-   [Running GreenFPGA](#running-greenfpga)
-   [Citation/Bibliography](#citation)

## Abstract
Modeling the carbon footprint (CFP) of computing includes both the operational CFP from the use of semiconductor devices and the embodied CFP from their manufacture and design has become essential for sustainability.  Field Programmable Gate Arrays (FPGAs) emerge as promising sustainable platforms due to their reconfigurability, allowing the embodied CFP to be amortized across multiple applications. This work introduces GreenFPGA, a framework for estimating the FPGA’s CFP across the lifespan, considering the uncertainties in CFP modeling. The framework evaluates the lifecycle CFP by accounting for the impacts of design, manufacturing, reconfigurability (reuse), operation, testing, disposal, and recycling. Using the GreenFPGA framework, the work evaluates scenarios where the reconfigurability of FPGAs helps outweigh the embodied and operational CFP costs compared to application-specific integrated circuits (ASICs), graphics processing units (GPUs), and central processing units (CPUs). The work emphasizes the importance of analyzing the CFP across four platforms—FPGA, ASIC, GPU, and CPU—by considering multiple parameters, including lifetime, usage time, volume, and the number of applications.



## Getting started

### Setup guide

GreenFPGA requires the following: 

```
- python 3.8 
- pip 20.0.2
- python3.8-venv
```

Additionally, please refer steps below that provide instructions to install the packages inside requirements.txt in a virtual environment. 

### Steps to install with bash

```
git clone https://github.com/ASU-VDA-Lab/GreenFPGA.git
cd GreenFPGA
python3 -m venv greenfpga
source greenfpga/bin/activate
pip3 install -r requirements.txt
```

## Key parameters
GreenFPGA uses input parameters from the JSON files under the test_examples and computes the CFP for multiple scenarios and multiple device platforms (FPGA, ASIC, GPU, and CPU).  

 <img src="images/greenfpga-arch.png" alt="drawing" width="600"/> 

### Specification Parameters 
All the important specification parameters of the FPGA, ASIC, GPU, and CPU are added to the [fpga_spec.json](./test_example/Agilex/fpga_spec.json). The file contains important parameters such as area of the design (mm2), power of the design (W), number of manufactured parts (Volume), lifetime of the evaluation (hrs), and based on the type of experiment and device type that we are analyzing, number of applications and number of designs are provieded as inputs in the [fpga_spec.json](./test_example/Agilex/fpga_spec.json).


The [node_list.txt](./test_example/TPU/node_list.txt) comprises the technology node associated with the design that needs to be analyzed. We have added example for each of the platforms (ASIC, FPGA, GPU, and CPU) under [test_example](./test_example/) directory. 

The remaining parameters regarding the design CFP, application-development CFP, EOL CFP, memory CFP, and testing CFP are all provided in [green_fpga_param.json](./test_example/TPU/green_fpga_param.json) based on user preferences. 

```     
   ├── fpga_spec.json
   ├── node_list.txt
   └── green_fpga_param.json
```

GreenFPGA tool can also accept parameters from the command line. Below are some of the main parameters that could be used to help sweep and analyze the variations in embodied and operational CFP.  


```
--design_dir    : Directory for design analysis 
--num_app       : Number of application  
--num_lifetime  : Total evaluation lifetime 
--node          : Tech node of analysis 
--mem_cap       : Memory capacity 
--dc_val        : DC Value
--num_des       : Number of designs needed to run the experiment
--nfpga         : Number of FPGAs, Appsize/fpga_capacity 
--power         : Power of the device under analysis
--chip_area     : Area of the device 
--ope_vol       : Opertaion Volume 
--emb_vol       : Embodied Volume
--uncertain_off : Uncertianity analysis off 
```
Commands to run GreenFPGA with these parameters are provided in the next section below. 

## Running GreenFPGA
Modify the input parameters according to the design and experiment being analyzed. 
The command to run GreenFPGA to obtain the breakdown of CFP for the design : 
```
python3 src/ECO_chip.py --design_dir test_example/TPU/
```
To run the analysis using command line parameters : 
```
python3 src/ECO_chip.py --design_dir test_example/TPU/ --num_des 1 --num_app 5 --num_lifetime 8 --power 150 --chip_area 650
python3 src/ECO_chip.py --design_dir test_example/Agilex/ --num_des 3 --num_app 3 --num_lifetime 5 --power 80  --chip_area 450
```

To execute the probabilistic model, the source code can be found in the [probabilistic](./src/uncertainity/) directory. This directory contains all the necessary functions and resources for running the probabilistic analysis. The code generates the required KDEs and other distributions for key parameters, accounting for inherent uncertainties such as spatial, temporal, process-driven, and system-driven variations that influence both the embodied and operational carbon footprint (CFP). Below is an example of the KDE for Carbon Intensity variation:

<img src="images/kde-ci.png" alt="drawing" width="600"/> 

Unlike ASICs, the extra embodied CFP that occurred during the manufacturing and design of FPGAs, GPUs, and CPUs can be amortized across its multiple applications and lifespan for various uses. For Num App = 1, FPGAs have higher CFP than ASICs since they have larger areas and are less energy efficient compared to ASICs, however the same FPGAs when used for Num App = 7, it can be seen that FPGAs are sustainably efficient compared to ASICs and have amortized the embodied CFP. 

<img src="images/asic-fpga-napp.jpg" alt="drawing" width="600"/> 


Below is an example output for a test_example TPU showing the breakdown in Total CFP :
```
-------------------------
Using below files 
test_example/TPU/green_fpga_param.json
test_example/TPU/fpga_spec.json
test_example/TPU/node_list.txt
-------------------------
-------------------------
Design    CFP : 2.590000e+07
Mfg       CFP : 3.141413e+08
EOL       CFP : 3.900000e+03
Operation CFP : 1.098548e+09
App Dev   CFP : 5.040000e+01
-------------------------
Embodied  CFP : 3.400452e+08
Operation CFP : 1.098548e+09
-------------------------
Total     CFP : 1.438593e+09
-------------------------
```

GreenFPGA also has the capability to provide a breakdown of embodied and operational CFP, as demonstrated below in a DNN test case comparing ASICs and FPGAs.

<img src="images/dnn.png" alt="drawing" width="600"/> 

GreenFPGA incorporates a probabilistic model that accounts for parameter variations arising from uncertainties, providing a range of values for each device under analysis. Below is a box plot comparing ASIC and FPGA, illustrating the variations in CFP values as the number of applications is swept.

<img src="images/BoxPlot.jpg" alt="drawing" width="600"/> 

In the paper, we perform a detailed analysis of the probabilistic model variations compared with the deterministic model. GreenFPGA can also perform sweeps in multiple parameters to observe the heatmap trends; shown below is a heat map analysis for ASIC vs FPGA.

<img src="images/asic-v-fpga-HM.png" alt="drawing" width="600"/> 



## Citation
If you find GreenFPGA useful or relevant to your research, please kindly cite our paper:
```
@inproceedings{sudarshan2023greenfpga,
      author = {Choppali Sudarshan, Chetan and Arora, Aman and Chhabria, Vidya A.},
      title = {GreenFPGA: Evaluating FPGAs as Environmentally Sustainable Computing Solutions},
      year = {2024},
      isbn = {9798400706011},
      publisher = {Association for Computing Machinery},
      address = {New York, NY, USA},
      url = {https://doi.org/10.1145/3649329.3657343},
      doi = {10.1145/3649329.3657343},
      articleno = {320},
      numpages = {6},
      location = {San Francisco, CA, USA},
      series = {DAC '24}
}
```
