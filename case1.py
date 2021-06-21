# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 12:52:57 2021

@author: lucky
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import data into python
url = 'https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/denco.csv'
df = pd.read_csv(url)
df
df.columns
df.shape # dim of the data set
df.head(3)
df.dtypes
df.describe
df['region'] = df['region'].astype('category')
df.region.value_counts()
df.region.value_counts().plot(kind='bar')

#%%case study
#Objective
#Expand Business by encouraging loyal customers to Improve repeated sales
#%%Information Required
#1.Who are the most loyal Customers - Improve repeated sales, Target customers with low sales Volumes
df.custname.value_counts() 
df1 = df[df['custname'].map(df['custname'].value_counts()) >= 100]
df1
df1.custname.value_counts() 
len(df1.custname.unique()) # no of loyal customers
df1.shape

#%%
# Prof's way i.e. top 5
df.groupby('custname').size().sort_values(ascending=False).head(5)

#%%

# low sales volume customers
df2 = df[df['custname'].map(df['custname'].value_counts()) < 100]
df2
df2.custname.value_counts() 
len(df2.custname.unique())
df1.shape

#%% prof's way
df.groupby('custname').size().sort_values(ascending=False).tail(5)
#%%

#2. Which customers contribute the most to their revenue - How do I retain these customers & target incentives

# The loyal costomer with max revenue
df1.groupby('custname').sum().revenue.sort_values(ascending = False)#Total revenue in dsescending order
# giving column names
df3 = df.groupby('custname').aggregate({'revenue':'sum'})
df4 = df1[df1['custname'].map(df3['revenue']) >= 2000000]
df4
df4.groupby('custname').sum().revenue.sort_values(ascending = False)
df4.custname.value_counts() 
len(df4.custname.unique()) # no of loyal customers
df4.shape

# In general the customer with max revenue (objective)
df3_new = df.groupby('custname').aggregate({'revenue':'sum'})
df4_new = df[df['custname'].map(df3_new['revenue']) >= 2000000]
df4_new
df4_new.groupby('custname').sum().revenue.sort_values(ascending = False) # printing total revenue in desc order
df4_new.custname.value_counts() 
len(df4_new.custname.unique()) # no of loyal customers
df4_new.shape

#%%
# By prof's method
df.groupby('custname').aggregate ({'revenue':np.sum}).sort_values( by='revenue', ascending=False).head(5)
# Alternative
df.groupby('custname')['revenue'].aggregate([np.sum,'size']).sort_values(by='sum', ascending=False).head(5)

#%%Objective
#Maximise revenue from high value parts
#%%Information Required
#What part numbers bring in to significant portion of revenue - Maximise revenue from high value parts

# parts with maximum revenue
df.groupby('partnum').sum().revenue.sort_values(ascending = False)

# giving column names
df5 = df.groupby('partnum').aggregate({'revenue':'sum'})
df6 = df[df['partnum'].map(df5['revenue']) >= 1000000]
df6
df6.groupby('partnum').sum().revenue.sort_values(ascending = False)
len(df6.partnum.unique())
df6.partnum.value_counts()

#%%
# Prof's way (max revenue) 
df[['partnum','revenue']].sort_values(by='revenue',ascending=False).head(5)

#%%

#What parts have the highest profit margin - What parts are driving profits & what parts need to build further
df.sort_values(['margin'],ascending = 0).margin.head(5)
df7 = df.loc[df['margin'] >= 500000]
df7
len(df7.partnum.unique())
df7.partnum.value_counts()

#%%
# prof's way
df[['partnum','margin']].sort_values( by='margin', ascending=False).head(5)
# for total margin
df[['partnum','margin']].groupby('partnum').sum().sort_values(by='margin',ascending=False).head(5)

#%%
# parts to focus for positive margin
df8 = df.loc[(df['margin'] < 500000) & (df['margin'] > 0) ]
df8.sort_values(['margin'],ascending = 0)
df8
len(df8.partnum.unique())
df8.partnum.value_counts()

# For zero and negative margin 
df9 = df.loc[df['margin'] <= 0 ]
df9.sort_values(['margin'],ascending = 0)
df9
len(df9.partnum.unique())
df9.partnum.value_counts()

#%%
# most sold items
df.partnum.value_counts().head()

#or 
df.groupby('partnum').size().sort_values(ascending=False).head(5)

#%%
#which regions gavemax revenue
df.groupby('region').sum().revenue.sort_values(ascending = False).head(5)
df[['revenue', 'region']].groupby('region').sum().sort_values(by='revenue',ascending=False).plot(kind='barh')


#%%
# Extra
df.groupby(['custname'])['margin'].nlargest(3)
df.sort_values(['revenue'], ascending= True).groupby( 'region' ).mean()
