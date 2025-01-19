'''
@File    :   prams_prob.py
@Time    :   2024/11/28 23:51:22
@Author  :   Chetan Sudarshan 
@Version :   1.0
@Contact :   cchoppal@asu.edu
@Desc    :   #All functions needed for probabilistic model
'''


import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from matplotlib import font_manager
import pandas as pd

plot_en = True
dump_en = False

def smooth_uncertainity(data):
    # Create a histogram (frequencies and bin edges)
    frequencies, bin_edges = np.histogram(data, bins=10)

    # Compute bin centers
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    # Create a smooth curve using spline interpolation
    x_smooth = np.linspace(bin_centers.min(), bin_centers.max(), 200)  # Generate more points for smoothness
    spline = make_interp_spline(bin_centers, frequencies, k=3)  # Cubic spline
    y_smooth = spline(x_smooth)

    ## Plot the smooth curve
    #plt.plot(x_smooth, y_smooth, color='blue', label='Smooth Trend', linewidth=2)

    ## Add labels, title, and legend
    #plt.xlabel('Data Values')
    #plt.ylabel('Frequency')
    #plt.title('Histogram Trend Line (Smoothed)')
    #plt.legend()

    ## Show the plot
    #plt.show() 
    return x_smooth,y_smooth

def mean_calc_plot(data):
 
    # Compute a trend line
    mean = np.mean(data)
    std_dev = np.std(data)
    x = np.linspace(min(data), max(data), 100)
    y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)  # Gaussian fit
    #y = y * len(data) * (bins[1] - bins[0])  # Scale y to match the histogram
    y = y * len(data) * 500
    return x,y

def plot_trend(x,y,xlab,ylab,title,name):
    # Plot the trend line
    plt.plot(x, y, color='red', label='Trend Line')

    # Add labels and legend
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    plt.legend()

    # Show the plot
    #plt.show()
    #plt.savefig(f"src/new_src/gen_plots/{name}.pdf")
    #plt.clf()
    return

def plot_hist(data,name):
    plt.hist(data, bins=50, density=True, color='skyblue', edgecolor='black', alpha=0.7)
    #plt.show()
    #plt.savefig(f"src/new_src/gen_plots/{name}_hist.pdf")
    #plt.clf()
    return 

def plot_detailed_histogram(df,name,detailed):
    if detailed:
        df['Emb_Carbon'] = pd.to_numeric(df['Emb_Carbon'])
        df['Operational_Carbon'] = pd.to_numeric(df['Operational_Carbon'])
        df['Total_Carbon'] = pd.to_numeric(df['Total_Carbon'])
        df['Total_0.1_Ope'] = pd.to_numeric(df['Total_0.1_Ope'])
        df['Total_0.2_Ope'] = pd.to_numeric(df['Total_0.2_Ope'])
        df['Total_0.3_Ope'] = pd.to_numeric(df['Total_0.3_Ope'])
        df['Total_0.4_Ope'] = pd.to_numeric(df['Total_0.4_Ope'])
        df['Total_0.5_Ope'] = pd.to_numeric(df['Total_0.5_Ope'])
        df['Total_0.6_Ope'] = pd.to_numeric(df['Total_0.6_Ope'])
        df['Total_0.7_Ope'] = pd.to_numeric(df['Total_0.7_Ope'])
        df['Total_0.8_Ope'] = pd.to_numeric(df['Total_0.8_Ope'])
        df['Total_0.9_Ope'] = pd.to_numeric(df['Total_0.9_Ope'])
        df['Total_1.0_Ope'] = pd.to_numeric(df['Total_1.0_Ope'])
        

        # Plot histogram for Mfg_Carbon
        plt.figure(figsize=(25, 10))

        plt.subplot(4, 3, 1)
        df['Emb_Carbon'].plot(kind='hist', bins=50, density=True, alpha=0.6, color='b')
        plt.xlabel('Emb_Carbon kgCO2e')
        plt.ylabel('Probability')
        plt.title(f'Emb_Carbon Histogram of {name}')
    
        plt.subplot(4, 3, 2)
        df['Operational_Carbon'].plot(kind='hist', bins=50, density=True, alpha=0.6, color='b')
        plt.xlabel('Ope_carbon kgCO2e')
        plt.ylabel('Probability')
        plt.title(f'OpeCarbon Histogram of {name}')

        # Plot histogram for Tot_Carbon
        plt.subplot(4, 3, 3)
        df['Total_Carbon'].plot(kind='hist', bins=50, density=True, alpha=0.6, color='g')
        plt.xlabel('Tot_Carbon kgCO2e')
        plt.ylabel('Probability')
        plt.title(f'Tot_Carbon Histogram of {name}')
        
        # Plot histogram for Tot_Carbon
        plt.subplot(4, 3, 4)
        df['Total_0.1_Ope'].plot(kind='hist', bins=50, density=True, alpha=0.6, color='g')
        plt.xlabel('Tot_Carbon kgCO2e')
        plt.ylabel('Probability')
        plt.title(f'Tot_Carbon 0.1 Ope Histogram of {name}')
        
        # Plot histogram for Tot_Carbon
        plt.subplot(4, 3, 5)
        df['Total_0.2_Ope'].plot(kind='hist', bins=50, density=True, alpha=0.6, color='g')
        plt.xlabel('Tot_Carbon kgCO2e')
        plt.ylabel('Probability')
        plt.title(f'Tot_Carbon 0.2 Ope Histogram of {name}')
        
        # Plot histogram for Tot_Carbon
        plt.subplot(4, 3, 6)
        df['Total_0.3_Ope'].plot(kind='hist', bins=50, density=True, alpha=0.6, color='g')
        plt.xlabel('Tot_Carbon kgCO2e')
        plt.ylabel('Probability')
        plt.title(f'Tot_Carbon 0.3 Ope Histogram of {name}')

        # Plot histogram for Tot_Carbon
        plt.subplot(4, 3, 7)
        df['Total_0.4_Ope'].plot(kind='hist', bins=50, density=True, alpha=0.6, color='g')
        plt.xlabel('Tot_Carbon kgCO2e')
        plt.ylabel('Probability')
        plt.title(f'Tot_Carbon 0.4 Ope Histogram of {name}')
        
        # Plot histogram for Tot_Carbon
        plt.subplot(4, 3, 8)
        df['Total_0.5_Ope'].plot(kind='hist', bins=50, density=True, alpha=0.6, color='g')
        plt.xlabel('Tot_Carbon kgCO2e')
        plt.ylabel('Probability')
        plt.title(f'Tot_Carbon 0.5 Ope Histogram of {name}')
        
        # Plot histogram for Tot_Carbon
        plt.subplot(4, 3, 9)
        df['Total_0.6_Ope'].plot(kind='hist', bins=50, density=True, alpha=0.6, color='g')
        plt.xlabel('Tot_Carbon kgCO2e')
        plt.ylabel('Probability')
        plt.title(f'Tot_Carbon 0.6 Ope Histogram of {name}')

        # Plot histogram for Tot_Carbon
        plt.subplot(4, 3, 10)
        df['Total_0.7_Ope'].plot(kind='hist', bins=50, density=True, alpha=0.6, color='g')
        plt.xlabel('Tot_Carbon kgCO2e')
        plt.ylabel('Probability')
        plt.title(f'Tot_Carbon 0.7 Ope Histogram of {name}')
        
        # Plot histogram for Tot_Carbon
        plt.subplot(4, 3, 11)
        df['Total_0.8_Ope'].plot(kind='hist', bins=50, density=True, alpha=0.6, color='g')
        plt.xlabel('Tot_Carbon kgCO2e')
        plt.ylabel('Probability')
        plt.title(f'Tot_Carbon 0.8 Ope Histogram of {name}')
        
        # Plot histogram for Tot_Carbon
        plt.subplot(4, 3, 12)
        df['Total_0.9_Ope'].plot(kind='hist', bins=50, density=True, alpha=0.6, color='g')
        plt.xlabel('Tot_Carbon kgCO2e')
        plt.ylabel('Probability')
        plt.title(f'Tot_Carbon 0.9 Ope Histogram of {name}')

        plt.tight_layout()
        #plt.savefig(f"src/new_src/gen_plots/final_trend/{name}-CFP-histogram_detailed.pdf")
   
    
    else: 
        df['Emb_Carbon'] = pd.to_numeric(df['Emb_Carbon'])
        df['Operational_Carbon'] = pd.to_numeric(df['Operational_Carbon'])
        df['Total_Carbon'] = pd.to_numeric(df['Total_Carbon'])

        # Plot histogram for Mfg_Carbon
        plt.figure(figsize=(15, 5))

        plt.subplot(1, 3, 1)
        df['Emb_Carbon'].plot(kind='hist', bins=50, density=True, alpha=0.6, color='b')
        plt.xlabel('Emb_Carbon kgCO2e')
        plt.ylabel('Probability')
        plt.title(f'Emb_Carbon Histogram of {name}')
    
        plt.subplot(1, 3, 2)
        df['Operational_Carbon'].plot(kind='hist', bins=50, density=True, alpha=0.6, color='b')
        plt.xlabel('Ope_carbon kgCO2e')
        plt.ylabel('Probability')
        plt.title(f'OpeCarbon Histogram of {name}')

        # Plot histogram for Tot_Carbon
        plt.subplot(1, 3, 3)
        df['Total_Carbon'].plot(kind='hist', bins=50, density=True, alpha=0.6, color='g')
        plt.xlabel('Tot_Carbon kgCO2e')
        plt.ylabel('Probability')
        plt.title(f'Tot_Carbon Histogram of {name}')

        plt.tight_layout()
        #plt.savefig(f"src/new_src/gen_plots/final_trend/{name}-CFP-histogram.pdf")
        #df.to_csv(f"../dataset/{model}-CFP-histogram.csv")
    return 

def plot_merged_df(df1,df2,name):
    plt.figure(figsize=(15,5))
    
    df1['Total_0.2_Ope'] = pd.to_numeric(df1['Total_0.2_Ope'])
    df1['Total_0.2_Ope'].plot(kind='hist', bins=50, density=True, alpha=0.6, label='DataFrame 1')

    # Plot histogram for Total_Carbon for df2
    df2['Total_0.2_Ope'] = pd.to_numeric(df2['Total_0.2_Ope'])
    df2['Total_0.2_Ope'].plot(kind='hist', bins=50, density=True, alpha=0.6, label='DataFrame 2')

    plt.xlabel('Total_Carbon kgCO2e')
    plt.ylabel('Probability')
    plt.title('Total_Carbon Histogram')
    plt.legend()
    #plt.show()
    plt.tight_layout()
    #plt.savefig(f"src/new_src/gen_plots/final_trend/{name}-CFP-Total-Compare.pdf")
    return 

def find_prob(data):
    # Find the value with the highest probability
    unique_values, counts = np.unique(data, return_counts=True)
    probabilities = counts / len(data)  # Convert frequencies to probabilities

    # Find the maximum probability and its corresponding value
    max_prob_index = np.argmax(probabilities)
    max_prob_value = unique_values[max_prob_index]
    max_prob = probabilities[max_prob_index]

    print(f"Value with highest probability: {max_prob_value}")
    print(f"Highest probability: {max_prob:.2f}")
    return

def dump_xy_values_csv(x,y,file_name):
    csv_df = pd.DataFrame({'X': x,'Y':y}) #Create data frame 
    #csv_df.to_excel(f"src/uncertainity/kde_values/{file_name}",index=False)
    #csv_df.to_excel(f"{file_name}",index=False)
    return 

def yield_calc(area, defect_density):
    yield_val = (1+(defect_density*1e4)*(area*1e-6)/10)**-10
    return yield_val

#sample_size = 10000000

def defden_kde_gen(sample_size):
    defden = np.random.choice(np.arange(0.095,0.42,0.0065), size=sample_size, replace=True, p=[
    0.05625,
    0.05625,
    0.05625,
    0.05625,
    0.05625,
    0.05625,
    0.05625,
    0.05625,
    0.05625,
    0.05625,
    0.025,
    0.025,
    0.025,
    0.025,
    0.025,
    0.025,
    0.025,
    0.025,
    0.025,
    0.025,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,
    0.00625,])
    return defden



############
#EPA

def epa_kde_gen(sample_size):
    #10nm
    start=0.9
    end=1.5

    step_size=(end-start)/13

    epa = np.random.choice(np.arange(start,end,step_size), size=sample_size, replace=True, p=[
    0.092478422,
    0.09864365,
    0.101726264,
    0.103575832,
    0.101726264,
    0.097410604,
    0.091245376,
    0.08323058,
    0.073982737,
    0.061652281,
    0.048088779,
    0.033908755,
    0.012330456,]) 
    return epa


#######################

def ci_taiwan_kde(sample_size):
 
    #Carbon Intensity Taiwan
    start = 636.5161
    end = 684.674
    intervals = 50
    step = (end-start)/intervals

    ci_trend = np.random.choice(np.arange(start,end,step), size=sample_size, replace=True, p = [
    0.016,
    0.016,
    0.016,
    0.016,
    0.016,
    0.024,
    0.024,
    0.024,
    0.024,
    0.024,
    0.032,
    0.032,
    0.032,
    0.032,
    0.032,
    0.04,
    0.04,
    0.04,
    0.04,
    0.04,
    0.024,
    0.024,
    0.024,
    0.024,
    0.024,
    0.016,
    0.016,
    0.016,
    0.016,
    0.016,
    0.024,
    0.024,
    0.024,
    0.024,
    0.024,
    0.008,
    0.008,
    0.008,
    0.008,
    0.008,
    0.008,
    0.008,
    0.008,
    0.008,
    0.008,
    0.008,
    0.008,
    0.008,
    0.008,
    0.008,])
    return ci_trend



#########################

def gpa_func_gen(sample_size):
    #GPA
    mu = 150  # mean
    sigma = 30  # standard deviation

    gpa = np.random.normal(mu,sigma,sample_size)
    gpa = np.clip(gpa,50,300)
    return gpa


#######################

def ci_us_kde(sample_size):
    #Carbon Intensity US
    start_us = 369.4732
    end_us = 573.3789
    intervals_us = 40
    step_us = (end_us-start_us)/intervals_us


    ci_trend_us = np.random.choice(np.arange(start_us,end_us,step_us), size=sample_size, replace=True, p = [
    0.024590164,
    0.024590164,
    0.024590164,
    0.024590164,
    0.024590164,
    0.016393443,
    0.016393443,
    0.016393443,
    0.016393443,
    0.016393443,
    0.016393443,
    0.016393443,
    0.016393443,
    0.016393443,
    0.016393443,
    0.008196721,
    0.008196721,
    0.008196721,
    0.008196721,
    0.008196721,
    0.008196721,
    0.008196721,
    0.008196721,
    0.008196721,
    0.008196721,
    0.032786885,
    0.032786885,
    0.032786885,
    0.032786885,
    0.032786885,
    0.016393443,
    0.016393443,
    0.016393443,
    0.073770492,
    0.073770492,
    0.073770492,
    0.073770492,
    0.073770492,
    0.024590164,
    0.024590164,])
    return ci-ci_trend_us

