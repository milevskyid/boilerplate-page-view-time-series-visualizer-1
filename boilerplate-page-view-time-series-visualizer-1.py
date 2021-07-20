#!/usr/bin/env python
# coding: utf-8

# In[38]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
get_ipython().run_line_magic('matplotlib', 'inline')


# In[39]:


df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')


# In[40]:


df = df[(df['value'] >= (df['value'].quantile(0.025))) & 
        (df['value'] <= (df['value'].quantile(0.975)))]


# In[41]:


fig = plt.figure(figsize=(12, 7))
plt.plot(df.index, df['value'],)
plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
plt.xlabel('Date')
plt.ylabel('Page Views')


# In[42]:


fig.savefig('line_plot.png')


# In[43]:


df_bar = df.copy()


# In[44]:


df_bar['year']=pd.DatetimeIndex(df_bar.index).year
df_bar['month']=pd.DatetimeIndex(df_bar.index).month


# In[45]:


df_bar_avg = df_bar.groupby(['year', 'month']).mean()
df_bar_avg = df_bar_avg.unstack()


# In[46]:


months = ['January', 'February', 'March', 'April' , 'May' , 'June', 'July', 'August', 'September', 'October', 'November', 'December']


# In[47]:


fig = df_bar_avg.plot(kind ="bar", figsize=(10,5)).figure
plt.xlabel("Years")
plt.ylabel("Average Page Views")
plt.legend(labels=months)


# In[48]:


df_box = df.copy()
df_box.reset_index(inplace=True)
df_box['year']=pd.DatetimeIndex(df_box['date']).year
df_box['month']=pd.DatetimeIndex(df_box['date']).month


# In[49]:


fig, axes = plt.subplots(figsize=(12, 7), ncols=2, sharex=False)
sns.despine(left=True)
ax1 = sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
ax1.set_xlabel('Year')
ax1.set_ylabel('Page Views')
ax1.set_title('Year-wise Box Plot(Trend)')

ax2 = sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
ax2.set_xlabel('Month')
ax2.set_ylabel('Page Views')
ax2.set_title('Month-wise Box Plot(Seasonality)')

