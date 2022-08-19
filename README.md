# split-population-survival-exploits

This repository is a temprary holding area for the SPIE (Stochastic Process Information Extraction) library, once ready for release, this will be hosted by github.com.

In order to run the code, first install the library as is via `pip -e install .`

Then cd into `splitPopulationSurvivalExploits/src/point_processes` and edit `MVSPP_config.py` to choose the dataset and hyper-parameter configurations. Run the code by running `MultiVariateSurvivalSplitPopulation.py`. 

The dataset are locaation at`splitPopulationSurvivalExploits/src/data/KDD_data` and it contains .pkl files for the training,validation anad test datasets. Please follow the naming convention as shown. The pkl file is a dictionary with cascade index as key and the values are another dictionary of {'node_list':[node_1, node_2, ..., -1],  'timestamp_list':[0,0.1, ...., right_censoring_time]} 
