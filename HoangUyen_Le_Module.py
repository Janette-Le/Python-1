#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import matplotlib as mp
import seaborn as sns
import math


# In[7]:


def dropping_column(dataset):
    columns = list(dataset)
    for i in columns:
        if len(dataset[i].unique()) == 1:
            dataset.drop(i,inplace=True,axis=1)


# In[8]:


def replacing_convert(dataset, column_list):
    for i in column_list:            
        dataset[i] = dataset[i].apply(lambda x: np.nan if x == '?' else x)
        dataset[i] = dataset[i].apply(lambda x: np.nan if x == '-' else x)
        data[i] = data[i].astype(str).astype(float)


# In[16]:


def filling_value(input_data, output_data, groupby_list, fill_list):
    for i in list(fill_list):
        average_values = pd.DataFrame(input_data.groupby(list(groupby_list))[i].mean()).reset_index()
        output_data = output_data.merge(average_values, on = groupby_list, how="left")

