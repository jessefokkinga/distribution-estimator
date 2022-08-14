import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def generate_plot(nr_observations, data):
    
    # Generate random sample of observations to use in plot.
    sample = np.random.choice(data.index, size = nr_observations, replace = False)
    data_to_plot = data.loc[sample].reset_index()
    
    plt.figure(figsize=(15,8))
    
    # Set up the plot by using the point predictions, actual values and the computed upper and lower bounds.
    ax = sns.scatterplot(data=data_to_plot, x=data_to_plot.index, y='predictions', legend=False, color = 'blue')
    sns.scatterplot(data=data_to_plot, x=data_to_plot.index, y='actuals', legend=False, color = 'red')
    sns.scatterplot(data=data_to_plot, x=data_to_plot.index, y='upper_bounds', legend=False, color = 'blue', alpha = 0.5)
    sns.scatterplot(data=data_to_plot, x=data_to_plot.index, y='lower_bounds', legend=False, color = 'blue', alpha = 0.5)
    
    ax.fill_between(data_to_plot.index, data_to_plot['lower_bounds'], data_to_plot['upper_bounds'], alpha=0.2)
    
    ax.set(xlabel='Index', ylabel='Target variable')
    ax.legend(loc='upper right', labels=['Prediction', 'Actual'])

    return ax