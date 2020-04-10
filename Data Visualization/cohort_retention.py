
# coding: utf-8

# In[1]:

# Import libraries
import pandas as pd
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:

dataset = pd.read_csv('C://Kuliah/nani/Prelimanary-Test/Data Visualization/dataset.csv', encoding = "ISO-8859-1")


# In[3]:

dataset


# In[4]:

dataset['order_date'] = pd.to_datetime(dataset['order_date'])


# In[15]:

# Group customers in acquisition cohorts based on the month they made their first purchase--
# Create function to truncate given date in column to a first day of the month
def get_month(x): return dt.datetime(x.year, x.month, 1)
# Apply function to invoice date to invoice month column
dataset['month'] = dataset['order_date'].apply(get_month)
grouping1 = dataset.groupby('user_id')['month']
dataset['CohortMonth'] = grouping1.transform('min')
print(dataset.describe())


# In[16]:

#
def get_date_int(df, column):
    year = df[column].dt.year
    month = df[column].dt.month
    day = df[column].dt.day
    return year, month, day
order_year, order_month, _ = get_date_int(dataset, 'month')
cohort_year, cohort_month, _ = get_date_int(dataset, 'CohortMonth')


# In[17]:

years_diff = order_year - cohort_year
months_diff = order_month - cohort_month


# In[18]:

dataset['CohortIndex'] = years_diff * 12 + months_diff + 1
dataset.head()


# In[20]:

# Count monthly active customers from each cohort
grouping_count = dataset.groupby(['CohortMonth', 'CohortIndex'])
cohort_data = grouping_count['user_id'].apply(pd.Series.nunique)
cohort_data = cohort_data.reset_index()
cohort_counts = cohort_data.pivot(index='CohortMonth',
                                  columns='CohortIndex',
                                  values='user_id')
print(cohort_counts.head())


# In[21]:

# --Calculate Retention Rate--
cohort_sizes = cohort_counts.iloc[:,0]
retention = cohort_counts.divide(cohort_sizes, axis=0)
retention.round(3) * 100
retention.index = retention.index.strftime('%m-%Y')


# In[ ]:




# In[ ]:



