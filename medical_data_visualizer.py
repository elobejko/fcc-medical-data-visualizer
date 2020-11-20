import pandas as pd
import seaborn as sns
#import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = np.multiply(df['weight'] / (df['height']/100) ** 2 > 25, 1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.multiply(df['cholesterol'] > 1, 1)
df['gluc'] = np.multiply(df['gluc'] > 1, 1)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['active', 'alco', 'cholesterol', 'gluc','overweight', 'smoke'])
    print(df_cat.head())
    

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    #df_cat = df_cat['variable'].value_counts()
   # print(df_cat.head())

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x = 'variable', hue = 'value', data = df_cat, height = 5, kind = "count", col = "cardio" )



    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'
    return 0



    # Do not modify the next two lines
  #  fig.savefig('heatmap.png')
  #  return fig
