```python
#import the necessary packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
from scipy import stats 
import seaborn as sns; sns.set_theme(color_codes=True)
from scipy.stats.stats import pearsonr
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from statsmodels.stats.contingency_tables import mcnemar
```


```python
#have a quick glance at the data obtained from the users of the chatbot

df = pd.read_csv('fyp.csv')
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>objectId</th>
      <th>user_education</th>
      <th>pre_q1</th>
      <th>pre_q2</th>
      <th>pre_q3</th>
      <th>pre_q4</th>
      <th>pre_q5</th>
      <th>post_q1</th>
      <th>post_q2</th>
      <th>post_q3</th>
      <th>...</th>
      <th>survey_q3a</th>
      <th>survey_q3b</th>
      <th>survey_q4a</th>
      <th>survey_q4b</th>
      <th>survey_q5a</th>
      <th>survey_q5b</th>
      <th>survey_q6</th>
      <th>survey_q7a</th>
      <th>survey_q7b</th>
      <th>survey_q8</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>nR0eH4BXBxqQ7Askn6B7</td>
      <td>PECT (community rotation)</td>
      <td>a,b</td>
      <td>a,b,d</td>
      <td>a</td>
      <td>a,b</td>
      <td>a,d</td>
      <td>a,b,d</td>
      <td>a,c,d</td>
      <td>a</td>
      <td>...</td>
      <td>b</td>
      <td>b,c,e,d,a</td>
      <td>c</td>
      <td>c</td>
      <td>c</td>
      <td>c</td>
      <td>a,c,g,h,I,f,e,d,b</td>
      <td>d</td>
      <td>a,c,d,b</td>
      <td>d</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CUT0EUn0nhZAbFXeh0wP</td>
      <td>pre-registration training</td>
      <td>A, D</td>
      <td>A, D</td>
      <td>a</td>
      <td>C</td>
      <td>A, D</td>
      <td>A, B, D</td>
      <td>A, C, D</td>
      <td>a</td>
      <td>...</td>
      <td>b</td>
      <td>E, C, D, B, A</td>
      <td>d</td>
      <td>b</td>
      <td>d</td>
      <td>c</td>
      <td>C, I, F, A, H, G, E, D, B</td>
      <td>b</td>
      <td>C, A, D, B</td>
      <td>e</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NzwaGfA323uHOcrx36cT</td>
      <td>pre-registration training</td>
      <td>a, b, d</td>
      <td>a,c</td>
      <td>a</td>
      <td>a, b, d</td>
      <td>a, b, c, d</td>
      <td>a, b, c, d</td>
      <td>a, c, d</td>
      <td>a</td>
      <td>...</td>
      <td>a</td>
      <td>e, d, c, d, a</td>
      <td>a</td>
      <td>b</td>
      <td>a</td>
      <td>a</td>
      <td>f, a, i, c, h, e, g, b, d</td>
      <td>c</td>
      <td>a, d, c, b</td>
      <td>e</td>
    </tr>
    <tr>
      <th>3</th>
      <td>lUx7IcNBfmGYtJfAJY9F</td>
      <td>PECT (community rotation)</td>
      <td>a,d</td>
      <td>a,c</td>
      <td>a</td>
      <td>a,b,d</td>
      <td>a,c,d</td>
      <td>a,b,c,d</td>
      <td>a,b,d</td>
      <td>a</td>
      <td>...</td>
      <td>a</td>
      <td>a,b,e,c,d</td>
      <td>c</td>
      <td>b</td>
      <td>c</td>
      <td>c</td>
      <td>i,c,a,f,h,e,g,d,b</td>
      <td>d</td>
      <td>c,d,a,b</td>
      <td>e</td>
    </tr>
    <tr>
      <th>4</th>
      <td>mLxmeiMBSAs6RPbKpRge</td>
      <td>pre-registration training</td>
      <td>a, b, c, d</td>
      <td>a, c</td>
      <td>a</td>
      <td>a, b, d</td>
      <td>a, c, d</td>
      <td>a, b, d</td>
      <td>a, b, d</td>
      <td>a</td>
      <td>...</td>
      <td>a</td>
      <td>e, c, b, a, d</td>
      <td>e</td>
      <td>d</td>
      <td>e</td>
      <td>b</td>
      <td>g, i, h, a, c, f, b, e, d</td>
      <td>b</td>
      <td>a, c, d, b</td>
      <td>d</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 24 columns</p>
</div>




```python
#number of unique users

len(df)
```




    83




```python
#number of unique users grouped by education

df.groupby('user_education').size()
```




    user_education
    PECT (community rotation)    26
    PECT (industry rotation)     23
    pre-registration training    34
    dtype: int64




```python
#pre-learning q1 score for all 3 groups

df1 = df.filter(items=['objectId', 'pre_q1'])

df1['pre_q1'] = df1['pre_q1'].str.lower()

df1_split = df1['pre_q1'].str.split(',', expand=True)

df1_split.columns = ['alpha', 'beta', 'charlie', 'delta']
df1_split['alpha'] = df1_split['alpha'].str.replace(' ', '')
df1_split['beta'] = df1_split['beta'].str.replace(' ', '')
df1_split['charlie'] = df1_split['charlie'].str.replace(' ', '')
df1_split['delta'] = df1_split['delta'].str.replace(' ', '')

q1_mymap = {'a': 1, 'b': 1, 'c': 0, 'd': 1, 'None': 0}
df1_split = df1_split.applymap(lambda s: q1_mymap.get(s) if s in q1_mymap else s)
df1_split = df1_split.fillna(0)

df1_split['pre_q1_score'] = df1_split.sum(axis=1) / 3
df = pd.concat([df, df1_split['pre_q1_score']], axis=1)

df_q1 = df.filter(items=['user_education', 'pre_q1_score'])
df_q1.groupby('user_education').agg(["mean", "median", "var"]).reset_index()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>user_education</th>
      <th colspan="3" halign="left">pre_q1_score</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>mean</th>
      <th>median</th>
      <th>var</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PECT (community rotation)</td>
      <td>0.564103</td>
      <td>0.666667</td>
      <td>0.024615</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PECT (industry rotation)</td>
      <td>0.565217</td>
      <td>0.666667</td>
      <td>0.024594</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pre-registration training</td>
      <td>0.617647</td>
      <td>0.666667</td>
      <td>0.061497</td>
    </tr>
  </tbody>
</table>
</div>




```python
#pre-learning q2 score for all 3 groups

df1 = df.filter(items=['objectId', 'pre_q2'])

df1['pre_q2'] = df1['pre_q2'].str.lower()

df1_split = df1['pre_q2'].str.split(',', expand=True)

df1_split.columns = ['alpha', 'beta', 'charlie']
df1_split['alpha'] = df1_split['alpha'].str.replace(' ', '')
df1_split['beta'] = df1_split['beta'].str.replace(' ', '')
df1_split['charlie'] = df1_split['charlie'].str.replace(' ', '')

q2_mymap = {'a': 1, 'b': 0, 'c': 0, 'd': 1, 'None': 0, 'noneoftheabove': 0}
df1_split = df1_split.applymap(lambda s: q2_mymap.get(s) if s in q2_mymap else s)
df1_split = df1_split.fillna(0)

df1_split['pre_q2_score'] = df1_split.sum(axis=1) / 2
df = pd.concat([df, df1_split['pre_q2_score']], axis=1)

df_pre_q2 = df.filter(items=['user_education', 'pre_q2_score'])
df_pre_q2.groupby('user_education').agg(["mean", "median", "var"]).reset_index()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>user_education</th>
      <th colspan="3" halign="left">pre_q2_score</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>mean</th>
      <th>median</th>
      <th>var</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PECT (community rotation)</td>
      <td>0.615385</td>
      <td>0.5</td>
      <td>0.046154</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PECT (industry rotation)</td>
      <td>0.673913</td>
      <td>0.5</td>
      <td>0.059289</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pre-registration training</td>
      <td>0.750000</td>
      <td>1.0</td>
      <td>0.079545</td>
    </tr>
  </tbody>
</table>
</div>




```python
#pre-learning q3 score for all 3 groups

df1 = df.filter(items=['objectId', 'pre_q3'])

df1['pre_q3'] = df1['pre_q3'].str.lower()

df1_split = df1['pre_q3'].str.split(',', expand=True)

df1_split.columns = ['alpha']
df1_split['alpha'] = df1_split['alpha'].str.replace(' ', '')

q3_mymap = {'a': 1, 'b': 0, 'c': 0, 'None': 0}
df1_split = df1_split.applymap(lambda s: q3_mymap.get(s) if s in q3_mymap else s)
df1_split = df1_split.fillna(0)

df1_split['pre_q3_score'] = df1_split.sum(axis=1)
df = pd.concat([df, df1_split['pre_q3_score']], axis=1)

df_pre_q3 = df.filter(items=['user_education', 'pre_q3_score'])
df_pre_q3.groupby('user_education').agg(["mean", "median", "var"]).reset_index()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>user_education</th>
      <th colspan="3" halign="left">pre_q3_score</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>mean</th>
      <th>median</th>
      <th>var</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PECT (community rotation)</td>
      <td>0.653846</td>
      <td>1</td>
      <td>0.235385</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PECT (industry rotation)</td>
      <td>0.608696</td>
      <td>1</td>
      <td>0.249012</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pre-registration training</td>
      <td>0.911765</td>
      <td>1</td>
      <td>0.082888</td>
    </tr>
  </tbody>
</table>
</div>




```python
#pre-learning q4 score for all 3 groups

df1 = df.filter(items=['objectId', 'pre_q4'])

df1['pre_q4'] = df1['pre_q4'].str.lower()

df1_split = df1['pre_q4'].str.split(',', expand=True)

df1_split.columns = ['alpha', 'beta', 'charlie']
df1_split['alpha'] = df1_split['alpha'].str.replace(' ', '')
df1_split['beta'] = df1_split['beta'].str.replace(' ', '')
df1_split['charlie'] = df1_split['charlie'].str.replace(' ', '')

q4_mymap = {'a': 1, 'b': 1, 'c': 0, 'd': 1, 'None': 0}
df1_split = df1_split.applymap(lambda s: q4_mymap.get(s) if s in q4_mymap else s)
df1_split = df1_split.fillna(0)

df1_split['pre_q4_score'] = df1_split.sum(axis=1) / 3
df = pd.concat([df, df1_split['pre_q4_score']], axis=1)

df_pre_q4 = df.filter(items=['user_education', 'pre_q4_score'])
df_pre_q4.groupby('user_education').agg(["mean", "median", "var"]).reset_index()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>user_education</th>
      <th colspan="3" halign="left">pre_q4_score</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>mean</th>
      <th>median</th>
      <th>var</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PECT (community rotation)</td>
      <td>0.628205</td>
      <td>0.666667</td>
      <td>0.082906</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PECT (industry rotation)</td>
      <td>0.623188</td>
      <td>0.666667</td>
      <td>0.083882</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pre-registration training</td>
      <td>0.705882</td>
      <td>0.666667</td>
      <td>0.085958</td>
    </tr>
  </tbody>
</table>
</div>




```python
#pre-learning q5 score for all 3 groups

df1 = df.filter(items=['objectId', 'pre_q5'])

df1['pre_q5'] = df1['pre_q5'].str.lower()

df1_split = df1['pre_q5'].str.split(',', expand=True)

df1_split.columns = ['alpha', 'beta', 'charlie', 'delta']
df1_split['alpha'] = df1_split['alpha'].str.replace(' ', '')
df1_split['beta'] = df1_split['beta'].str.replace(' ', '')
df1_split['charlie'] = df1_split['charlie'].str.replace(' ', '')
df1_split['delta'] = df1_split['delta'].str.replace(' ', '')

q5_mymap = {'a': 1, 'b': 0, 'c': 1, 'd': 1, 'None': 0}
df1_split = df1_split.applymap(lambda s: q5_mymap.get(s) if s in q5_mymap else s)
df1_split = df1_split.fillna(0)

df1_split['pre_q5_score'] = df1_split.sum(axis=1) / 3
df = pd.concat([df, df1_split['pre_q5_score']], axis=1)

df_pre_q5 = df.filter(items=['user_education', 'pre_q5_score'])
df_pre_q5.groupby('user_education').agg(["mean", "median", "var"]).reset_index()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>user_education</th>
      <th colspan="3" halign="left">pre_q5_score</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>mean</th>
      <th>median</th>
      <th>var</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PECT (community rotation)</td>
      <td>0.717949</td>
      <td>0.666667</td>
      <td>0.050598</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PECT (industry rotation)</td>
      <td>0.666667</td>
      <td>0.666667</td>
      <td>0.050505</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pre-registration training</td>
      <td>0.803922</td>
      <td>0.666667</td>
      <td>0.041196</td>
    </tr>
  </tbody>
</table>
</div>




```python
#post-learning q1 score for all 3 groups

df1 = df.filter(items=['objectId', 'post_q1'])

df1['post_q1'] = df1['post_q1'].str.lower()

df1_split = df1['post_q1'].str.split(',', expand=True)

df1_split.columns = ['alpha', 'beta', 'charlie', 'delta']
df1_split['alpha'] = df1_split['alpha'].str.replace(' ', '')
df1_split['beta'] = df1_split['beta'].str.replace(' ', '')
df1_split['charlie'] = df1_split['charlie'].str.replace(' ', '')
df1_split['delta'] = df1_split['delta'].str.replace(' ', '')

post_q1_mymap = {'a': 1, 'b': 1, 'c': 0, 'd': 1, 'None': 0}
df1_split = df1_split.applymap(lambda s: post_q1_mymap.get(s) if s in post_q1_mymap else s)
df1_split = df1_split.fillna(0)

df1_split['post_q1_score'] = df1_split.sum(axis=1) / 3
df = pd.concat([df, df1_split['post_q1_score']], axis=1)

df_post_q1 = df.filter(items=['user_education', 'post_q1_score'])
df_post_q1.groupby('user_education').agg(["mean", "median", "var"]).reset_index()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>user_education</th>
      <th colspan="3" halign="left">post_q1_score</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>mean</th>
      <th>median</th>
      <th>var</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PECT (community rotation)</td>
      <td>0.794872</td>
      <td>0.666667</td>
      <td>0.045128</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PECT (industry rotation)</td>
      <td>0.782609</td>
      <td>0.666667</td>
      <td>0.046552</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pre-registration training</td>
      <td>0.823529</td>
      <td>1.000000</td>
      <td>0.041989</td>
    </tr>
  </tbody>
</table>
</div>




```python
#post-learning q1 score for all 3 groups

df1 = df.filter(items=['objectId', 'post_q2'])

df1['post_q2'] = df1['post_q2'].str.lower()

df1_split = df1['post_q2'].str.split(',', expand=True)

df1_split.columns = ['alpha', 'beta', 'charlie']
df1_split['alpha'] = df1_split['alpha'].str.replace(' ', '')
df1_split['beta'] = df1_split['beta'].str.replace(' ', '')
df1_split['charlie'] = df1_split['charlie'].str.replace(' ', '')

post_q2_mymap = {'a': 1, 'b': 0, 'c': 1, 'd': 1, 'None': 0}
df1_split = df1_split.applymap(lambda s: post_q2_mymap.get(s) if s in post_q2_mymap else s)
df1_split = df1_split.fillna(0)

df1_split['post_q2_score'] = df1_split.sum(axis=1) / 3
df = pd.concat([df, df1_split['post_q2_score']], axis=1)

df_post_q2 = df.filter(items=['user_education', 'post_q2_score'])
df_post_q2.groupby('user_education').agg(["mean", "median", "var"]).reset_index()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>user_education</th>
      <th colspan="3" halign="left">post_q2_score</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>mean</th>
      <th>median</th>
      <th>var</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PECT (community rotation)</td>
      <td>0.807692</td>
      <td>0.666667</td>
      <td>0.037094</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PECT (industry rotation)</td>
      <td>0.782609</td>
      <td>0.666667</td>
      <td>0.026350</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pre-registration training</td>
      <td>0.813725</td>
      <td>0.833333</td>
      <td>0.041691</td>
    </tr>
  </tbody>
</table>
</div>




```python
#post-learning q2 score for all 3 groups

df1 = df.filter(items=['objectId', 'post_q3'])

df1['post_q3'] = df1['post_q3'].str.lower()

df1_split = df1['post_q3'].str.split(',', expand=True)

df1_split.columns = ['alpha']
df1_split['alpha'] = df1_split['alpha'].str.replace(' ', '')

post_q3_mymap = {'a': 1, 'b': 0, 'c': 0, 'None': 0}
df1_split = df1_split.applymap(lambda s: post_q3_mymap.get(s) if s in post_q3_mymap else s)
df1_split = df1_split.fillna(0)

df1_split['post_q3_score'] = df1_split.sum(axis=1)
df = pd.concat([df, df1_split['post_q3_score']], axis=1)

df_post_q3 = df.filter(items=['user_education', 'post_q3_score'])
df_post_q3.groupby('user_education').agg(["mean", "median", "var"]).reset_index()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>user_education</th>
      <th colspan="3" halign="left">post_q3_score</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>mean</th>
      <th>median</th>
      <th>var</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PECT (community rotation)</td>
      <td>0.807692</td>
      <td>1</td>
      <td>0.161538</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PECT (industry rotation)</td>
      <td>0.826087</td>
      <td>1</td>
      <td>0.150198</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pre-registration training</td>
      <td>0.970588</td>
      <td>1</td>
      <td>0.029412</td>
    </tr>
  </tbody>
</table>
</div>




```python
#post-learning q4 score for all 3 groups
 
df1 = df.filter(items=['objectId', 'post_q4'])

df1['post_q4'] = df1['post_q4'].str.lower()

df1_split = df1['post_q4'].str.split(',', expand=True)

df1_split.columns = ['alpha', 'beta', 'charlie']
df1_split['alpha'] = df1_split['alpha'].str.replace(' ', '')
df1_split['beta'] = df1_split['beta'].str.replace(' ', '')
df1_split['charlie'] = df1_split['charlie'].str.replace(' ', '')

post_q4_mymap = {'a': 0, 'b': 0, 'c': 1, 'd': 1, 'None': 0}
df1_split = df1_split.applymap(lambda s: post_q4_mymap.get(s) if s in post_q4_mymap else s)
df1_split = df1_split.fillna(0)

df1_split['post_q4_score'] = df1_split.sum(axis=1) / 2
df = pd.concat([df, df1_split['post_q4_score']], axis=1)

df_post_q4 = df.filter(items=['user_education', 'post_q4_score'])
df_post_q4.groupby('user_education').agg(["mean", "median", "var"]).reset_index()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>user_education</th>
      <th colspan="3" halign="left">post_q4_score</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>mean</th>
      <th>median</th>
      <th>var</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PECT (community rotation)</td>
      <td>0.826923</td>
      <td>1.0</td>
      <td>0.078846</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PECT (industry rotation)</td>
      <td>0.826087</td>
      <td>1.0</td>
      <td>0.059289</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pre-registration training</td>
      <td>0.838235</td>
      <td>1.0</td>
      <td>0.056373</td>
    </tr>
  </tbody>
</table>
</div>




```python
#post-learning q5 score for all 3 groups

df1 = df.filter(items=['objectId', 'post_q5'])

df1['post_q5'] = df1['post_q5'].str.lower()

df1_split = df1['post_q5'].str.split(',', expand=True)

df1_split.columns = ['alpha', 'beta', 'charlie']
df1_split['alpha'] = df1_split['alpha'].str.replace(' ', '')
df1_split['beta'] = df1_split['beta'].str.replace(' ', '')
df1_split['charlie'] = df1_split['charlie'].str.replace(' ', '')

post_q5_mymap = {'a': 1, 'b': 0, 'c': 1, 'd': 0, 'e': 1, 'None': 0}
df1_split = df1_split.applymap(lambda s: post_q5_mymap.get(s) if s in post_q5_mymap else s)
df1_split = df1_split.fillna(0)

df1_split['post_q5_score'] = df1_split.sum(axis=1) / 3
df = pd.concat([df, df1_split['post_q5_score']], axis=1)

df_post_q5 = df.filter(items=['user_education', 'post_q5_score'])
df_post_q5.groupby('user_education').agg(["mean", "median", "var"]).reset_index()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>user_education</th>
      <th colspan="3" halign="left">post_q5_score</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>mean</th>
      <th>median</th>
      <th>var</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PECT (community rotation)</td>
      <td>0.820513</td>
      <td>0.666667</td>
      <td>0.028718</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PECT (industry rotation)</td>
      <td>0.840580</td>
      <td>1.000000</td>
      <td>0.028986</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pre-registration training</td>
      <td>0.901961</td>
      <td>1.000000</td>
      <td>0.023767</td>
    </tr>
  </tbody>
</table>
</div>




```python
#survey q1: How quickly were you able to learn to use this chatbot?

#in number of users

df2 = df.filter(items=['objectId', 'user_education', 'survey_q1'])
survey_q1_mymap = {'a': 'Almost instantly', 'b': 'After some time', 'c': 'Still learning how to use it'}
df2 = df2.applymap(lambda s: survey_q1_mymap.get(s) if s in survey_q1_mymap else s)
df2 = df2.groupby(['user_education','survey_q1']).size().unstack(level=1)
df2

#in percentage of users for each group

cols = list(df2)
df2[cols] = df2[cols].div(df2[cols].sum(axis=1), axis=0).multiply(100)
df2

#in percentage of users for each group (graph)

df2.plot(kind = 'bar')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q1</th>
      <th>After some time</th>
      <th>Almost instantly</th>
      <th>Still learning how to use it</th>
    </tr>
    <tr>
      <th>user_education</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PECT (community rotation)</th>
      <td>8</td>
      <td>16</td>
      <td>2</td>
    </tr>
    <tr>
      <th>PECT (industry rotation)</th>
      <td>8</td>
      <td>12</td>
      <td>3</td>
    </tr>
    <tr>
      <th>pre-registration training</th>
      <td>11</td>
      <td>22</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q1</th>
      <th>After some time</th>
      <th>Almost instantly</th>
      <th>Still learning how to use it</th>
    </tr>
    <tr>
      <th>user_education</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PECT (community rotation)</th>
      <td>30.769231</td>
      <td>61.538462</td>
      <td>7.692308</td>
    </tr>
    <tr>
      <th>PECT (industry rotation)</th>
      <td>34.782609</td>
      <td>52.173913</td>
      <td>13.043478</td>
    </tr>
    <tr>
      <th>pre-registration training</th>
      <td>32.352941</td>
      <td>64.705882</td>
      <td>2.941176</td>
    </tr>
  </tbody>
</table>
</div>






    <AxesSubplot:xlabel='user_education'>




    
![png](output_14_3.png)
    



```python
#survey q2: How easy was it to use the chatbot?

#in number of users

df3 = df.filter(items=['objectId', 'user_education', 'survey_q2'])
survey_q2_mymap = {'a': 'Very easy', 'b': 'Easy', 'c': 'Neutral', 'd': 'Difficult', 'e': 'Very difficult'}
df3 = df3.applymap(lambda s: survey_q2_mymap.get(s) if s in survey_q2_mymap else s)
df3 = df3.groupby(['user_education','survey_q2']).size().unstack(level=1)
df3 = df3.fillna(0)
df3

#in percentage of users for each group

cols = list(df3)
df3[cols] = df3[cols].div(df3[cols].sum(axis=1), axis=0).multiply(100)
df3

#in percentage of users for each group (graph)

df3.plot(kind = 'bar')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q2</th>
      <th>Difficult</th>
      <th>Easy</th>
      <th>Neutral</th>
      <th>Very easy</th>
    </tr>
    <tr>
      <th>user_education</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PECT (community rotation)</th>
      <td>2.0</td>
      <td>8.0</td>
      <td>3.0</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>PECT (industry rotation)</th>
      <td>2.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>pre-registration training</th>
      <td>0.0</td>
      <td>11.0</td>
      <td>0.0</td>
      <td>23.0</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q2</th>
      <th>Difficult</th>
      <th>Easy</th>
      <th>Neutral</th>
      <th>Very easy</th>
    </tr>
    <tr>
      <th>user_education</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PECT (community rotation)</th>
      <td>7.692308</td>
      <td>30.769231</td>
      <td>11.538462</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>PECT (industry rotation)</th>
      <td>8.695652</td>
      <td>39.130435</td>
      <td>4.347826</td>
      <td>47.826087</td>
    </tr>
    <tr>
      <th>pre-registration training</th>
      <td>0.000000</td>
      <td>32.352941</td>
      <td>0.000000</td>
      <td>67.647059</td>
    </tr>
  </tbody>
</table>
</div>






    <AxesSubplot:xlabel='user_education'>




    
![png](output_15_3.png)
    



```python
#survey q3a: The chatbot provides me with a personalized learning experience.

#in number of users

df4 = df.filter(items=['objectId', 'user_education', 'survey_q3a'])
survey_q3a_mymap = {'a': 'Strongly agree', 'b': 'Agree', 'c': 'Neutral', 'd': 'Disagree', 'e': 'Strongly disagree'}
df4 = df4.applymap(lambda s: survey_q3a_mymap.get(s) if s in survey_q3a_mymap else s)
df4 = df4.groupby(['user_education','survey_q3a']).size().unstack(level=1)
df4 = df4.fillna(0)
df4

#in percentage of users for each group

cols = list(df4)
df4[cols] = df4[cols].div(df4[cols].sum(axis=1), axis=0).multiply(100)
df4

#in percentage of users for each group (graph)

df4.plot(kind = 'bar')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q3a</th>
      <th>Agree</th>
      <th>Disagree</th>
      <th>Neutral</th>
      <th>Strongly agree</th>
    </tr>
    <tr>
      <th>user_education</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PECT (community rotation)</th>
      <td>17.0</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>PECT (industry rotation)</th>
      <td>11.0</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>pre-registration training</th>
      <td>22.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>6.0</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q3a</th>
      <th>Agree</th>
      <th>Disagree</th>
      <th>Neutral</th>
      <th>Strongly agree</th>
    </tr>
    <tr>
      <th>user_education</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PECT (community rotation)</th>
      <td>65.384615</td>
      <td>3.846154</td>
      <td>19.230769</td>
      <td>11.538462</td>
    </tr>
    <tr>
      <th>PECT (industry rotation)</th>
      <td>47.826087</td>
      <td>0.000000</td>
      <td>30.434783</td>
      <td>21.739130</td>
    </tr>
    <tr>
      <th>pre-registration training</th>
      <td>64.705882</td>
      <td>8.823529</td>
      <td>8.823529</td>
      <td>17.647059</td>
    </tr>
  </tbody>
</table>
</div>






    <AxesSubplot:xlabel='user_education'>




    
![png](output_16_3.png)
    



```python
#survey q3b: Rank the chatbot features from most relevant to least relevant in providing a personalized learning experience.

df5 = df.filter(items=['objectId', 'user_education', 'survey_q3b'])

df5['survey_q3b'] = df5['survey_q3b'].str.lower()

df5_split = df5['survey_q3b'].str.split(',', expand=True)

df5_split.columns = ['first', 'second', 'third', 'fourth', 'fifth']
df5_split['first'] = df5_split['first'].str.replace(' ', '')
df5_split['second'] = df5_split['second'].str.replace(' ', '')
df5_split['third'] = df5_split['third'].str.replace(' ', '')
df5_split['fourth'] = df5_split['fourth'].str.replace(' ', '')
df5_split['fifth'] = df5_split['fifth'].str.replace(' ', '')

df5 = pd.concat([df5['user_education'], df5_split], axis=1)

#for the PECT (community rotation) group

df5_pect_comm = df5[df5['user_education'] == "PECT (community rotation)"]

df5_pect_comm_first = pd.DataFrame(df5_pect_comm['first'].value_counts())
df5_pect_comm_first.reset_index(level=0, inplace=True)

df5_pect_comm_second = pd.DataFrame(df5_pect_comm['second'].value_counts())
df5_pect_comm_second.reset_index(level=0, inplace=True)

df5_pect_comm_third = pd.DataFrame(df5_pect_comm['third'].value_counts())
df5_pect_comm_third.reset_index(level=0, inplace=True)

df5_pect_comm_fourth = pd.DataFrame(df5_pect_comm['fourth'].value_counts())
df5_pect_comm_fourth.reset_index(level=0, inplace=True)

df5_pect_comm_fifth = pd.DataFrame(df5_pect_comm['fifth'].value_counts())
df5_pect_comm_fifth.reset_index(level=0, inplace=True)

data_frames = [df5_pect_comm_first, df5_pect_comm_second, df5_pect_comm_third, df5_pect_comm_fourth, df5_pect_comm_fifth]
df5_pect_comm = reduce(lambda left,right: pd.merge(left,right,on=['index'], how='outer'), data_frames).fillna(0)
df5_pect_comm['total_count'] = df5_pect_comm.iloc[:,1:6].sum(axis=1)
df5_pect_comm['weighted_avg_rank'] = ((df5_pect_comm['first'] * 1) +  (df5_pect_comm['second'] * 2) + (df5_pect_comm['third'] * 3) + (df5_pect_comm['fourth'] * 4) + (df5_pect_comm['fifth'] * 5)) / df5_pect_comm['total_count']
survey_q3b_mymap = {'a': 'Addressing you by name', 'b': 'Navigating through the educational modules at your own time', 'c': 'Tracking your progress in the educational modules', 'd': 'Choosing your preferred virtual patient to apply your knowledge', 'e': 'Providing feedback on your virtual patient assessment'}
df5_pect_comm = df5_pect_comm.applymap(lambda s: survey_q3b_mymap.get(s) if s in survey_q3b_mymap else s)
df5_pect_comm

#for the PECT (industry rotation) group

df5_pect_ind = df5[df5['user_education'] == "PECT (industry rotation)"]

df5_pect_ind_first = pd.DataFrame(df5_pect_ind['first'].value_counts())
df5_pect_ind_first.reset_index(level=0, inplace=True)

df5_pect_ind_second = pd.DataFrame(df5_pect_ind['second'].value_counts())
df5_pect_ind_second.reset_index(level=0, inplace=True)

df5_pect_ind_third = pd.DataFrame(df5_pect_ind['third'].value_counts())
df5_pect_ind_third.reset_index(level=0, inplace=True)

df5_pect_ind_fourth = pd.DataFrame(df5_pect_ind['fourth'].value_counts())
df5_pect_ind_fourth.reset_index(level=0, inplace=True)

df5_pect_ind_fifth = pd.DataFrame(df5_pect_ind['fifth'].value_counts())
df5_pect_ind_fifth.reset_index(level=0, inplace=True)

data_frames = [df5_pect_ind_first, df5_pect_ind_second, df5_pect_ind_third, df5_pect_ind_fourth, df5_pect_ind_fifth]
df5_pect_ind = reduce(lambda left,right: pd.merge(left,right,on=['index'], how='outer'), data_frames).fillna(0)
df5_pect_ind['total_count'] = df5_pect_ind.iloc[:,1:6].sum(axis=1)
df5_pect_ind['weighted_avg_rank'] = ((df5_pect_ind['first'] * 1) +  (df5_pect_ind['second'] * 2) + (df5_pect_ind['third'] * 3) + (df5_pect_ind['fourth'] * 4) + (df5_pect_ind['fifth'] * 5)) / df5_pect_ind['total_count']
survey_q3b_mymap = {'a': 'Addressing you by name', 'b': 'Navigating through the educational modules at your own time', 'c': 'Tracking your progress in the educational modules', 'd': 'Choosing your preferred virtual patient to apply your knowledge', 'e': 'Providing feedback on your virtual patient assessment'}
df5_pect_ind = df5_pect_ind.applymap(lambda s: survey_q3b_mymap.get(s) if s in survey_q3b_mymap else s)
df5_pect_ind

#for the pre-registration training group

df5_prereg = df5[df5['user_education'] == "pre-registration training"]

df5_prereg_first = pd.DataFrame(df5_prereg['first'].value_counts())
df5_prereg_first.reset_index(level=0, inplace=True)

df5_prereg_second = pd.DataFrame(df5_prereg['second'].value_counts())
df5_prereg_second.reset_index(level=0, inplace=True)

df5_prereg_third = pd.DataFrame(df5_prereg['third'].value_counts())
df5_prereg_third.reset_index(level=0, inplace=True)

df5_prereg_fourth = pd.DataFrame(df5_prereg['fourth'].value_counts())
df5_prereg_fourth.reset_index(level=0, inplace=True)

df5_prereg_fifth = pd.DataFrame(df5_prereg['fifth'].value_counts())
df5_prereg_fifth.reset_index(level=0, inplace=True)

data_frames = [df5_prereg_first, df5_prereg_second, df5_prereg_third, df5_prereg_fourth, df5_prereg_fifth]
df5_prereg = reduce(lambda left,right: pd.merge(left,right,on=['index'], how='outer'), data_frames).fillna(0)
df5_prereg['total_count'] = df5_prereg.iloc[:,1:6].sum(axis=1)
df5_prereg['weighted_avg_rank'] = ((df5_prereg['first'] * 1) +  (df5_prereg['second'] * 2) + (df5_prereg['third'] * 3) + (df5_prereg['fourth'] * 4) + (df5_prereg['fifth'] * 5)) / df5_prereg['total_count']
survey_q3b_mymap = {'a': 'Addressing you by name', 'b': 'Navigating through the educational modules at your own time', 'c': 'Tracking your progress in the educational modules', 'd': 'Choosing your preferred virtual patient to apply your knowledge', 'e': 'Providing feedback on your virtual patient assessment'}
df5_prereg = df5_prereg.applymap(lambda s: survey_q3b_mymap.get(s) if s in survey_q3b_mymap else s)
df5_prereg
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>first</th>
      <th>second</th>
      <th>third</th>
      <th>fourth</th>
      <th>fifth</th>
      <th>total_count</th>
      <th>weighted_avg_rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Navigating through the educational modules at ...</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>7</td>
      <td>4</td>
      <td>0.0</td>
      <td>26.0</td>
      <td>2.192308</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Providing feedback on your virtual patient ass...</td>
      <td>10.0</td>
      <td>4.0</td>
      <td>7</td>
      <td>5</td>
      <td>0.0</td>
      <td>26.0</td>
      <td>2.269231</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tracking your progress in the educational modules</td>
      <td>5.0</td>
      <td>16.0</td>
      <td>4</td>
      <td>1</td>
      <td>0.0</td>
      <td>26.0</td>
      <td>2.038462</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Addressing you by name</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>2</td>
      <td>9</td>
      <td>14.0</td>
      <td>26.0</td>
      <td>4.346154</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Choosing your preferred virtual patient to app...</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>6</td>
      <td>7</td>
      <td>12.0</td>
      <td>26.0</td>
      <td>4.153846</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>first</th>
      <th>second</th>
      <th>third</th>
      <th>fourth</th>
      <th>fifth</th>
      <th>total_count</th>
      <th>weighted_avg_rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Navigating through the educational modules at ...</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>4</td>
      <td>3</td>
      <td>0.0</td>
      <td>23.0</td>
      <td>2.086957</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Providing feedback on your virtual patient ass...</td>
      <td>6.0</td>
      <td>7.0</td>
      <td>8</td>
      <td>1</td>
      <td>1.0</td>
      <td>23.0</td>
      <td>2.304348</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tracking your progress in the educational modules</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>4</td>
      <td>7</td>
      <td>0.0</td>
      <td>23.0</td>
      <td>2.565217</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Addressing you by name</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>2</td>
      <td>3</td>
      <td>13.0</td>
      <td>23.0</td>
      <td>3.869565</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Choosing your preferred virtual patient to app...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5</td>
      <td>9</td>
      <td>9.0</td>
      <td>23.0</td>
      <td>4.173913</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>first</th>
      <th>second</th>
      <th>third</th>
      <th>fourth</th>
      <th>fifth</th>
      <th>total_count</th>
      <th>weighted_avg_rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Providing feedback on your virtual patient ass...</td>
      <td>13.0</td>
      <td>4.0</td>
      <td>10</td>
      <td>5</td>
      <td>2.0</td>
      <td>34.0</td>
      <td>2.382353</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Navigating through the educational modules at ...</td>
      <td>11.0</td>
      <td>10.0</td>
      <td>6</td>
      <td>6</td>
      <td>0.0</td>
      <td>33.0</td>
      <td>2.212121</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tracking your progress in the educational modules</td>
      <td>8.0</td>
      <td>18.0</td>
      <td>6</td>
      <td>2</td>
      <td>0.0</td>
      <td>34.0</td>
      <td>2.058824</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Addressing you by name</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>4</td>
      <td>13</td>
      <td>15.0</td>
      <td>34.0</td>
      <td>4.147059</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Choosing your preferred virtual patient to app...</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>8</td>
      <td>8</td>
      <td>17.0</td>
      <td>35.0</td>
      <td>4.142857</td>
    </tr>
  </tbody>
</table>
</div>




```python
#survey q4a: What best describes your level of knowledge on identifying the factors affecting long-term BPV
#BEFORE using the chatbot?

#in number of users

df6 = df.filter(items=['objectId', 'user_education', 'survey_q4a'])
survey_q4a_mymap = {'a': 'Excellent', 'b': 'Very good', 'c': 'Good', 'd': 'Fair', 'e': 'Poor'}
df6 = df6.applymap(lambda s: survey_q4a_mymap.get(s) if s in survey_q4a_mymap else s)
df6 = df6.groupby(['user_education','survey_q4a']).size().unstack(level=1)
df6 = df6.fillna(0)
df6

#in percentage of users for each group

cols = list(df6)
df6[cols] = df6[cols].div(df6[cols].sum(axis=1), axis=0).multiply(100)
df6

#in percentage of users for each group (graph)

df6.plot(kind = 'bar')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q4a</th>
      <th>Excellent</th>
      <th>Fair</th>
      <th>Good</th>
      <th>Poor</th>
      <th>Very good</th>
    </tr>
    <tr>
      <th>user_education</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PECT (community rotation)</th>
      <td>3.0</td>
      <td>4.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>PECT (industry rotation)</th>
      <td>0.0</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>pre-registration training</th>
      <td>3.0</td>
      <td>11.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>12.0</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q4a</th>
      <th>Excellent</th>
      <th>Fair</th>
      <th>Good</th>
      <th>Poor</th>
      <th>Very good</th>
    </tr>
    <tr>
      <th>user_education</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PECT (community rotation)</th>
      <td>11.538462</td>
      <td>15.384615</td>
      <td>30.769231</td>
      <td>15.384615</td>
      <td>26.923077</td>
    </tr>
    <tr>
      <th>PECT (industry rotation)</th>
      <td>0.000000</td>
      <td>34.782609</td>
      <td>34.782609</td>
      <td>17.391304</td>
      <td>13.043478</td>
    </tr>
    <tr>
      <th>pre-registration training</th>
      <td>8.823529</td>
      <td>32.352941</td>
      <td>11.764706</td>
      <td>11.764706</td>
      <td>35.294118</td>
    </tr>
  </tbody>
</table>
</div>






    <AxesSubplot:xlabel='user_education'>




    
![png](output_18_3.png)
    



```python
#survey q4b: What best describes your level of knowledge on identifying the factors affecting long-term BPV,
#AFTER using the chatbot?

#in number of users

df7 = df.filter(items=['objectId', 'user_education', 'survey_q4b'])
survey_q4b_mymap = {'a': 'Excellent', 'b': 'Very good', 'c': 'Good', 'd': 'Fair', 'e': 'Poor'}
df7 = df7.applymap(lambda s: survey_q4b_mymap.get(s) if s in survey_q4b_mymap else s)
df7 = df7.groupby(['user_education','survey_q4b']).size().unstack(level=1)
df7 = df7.fillna(0)
df7

#in percentage of users for each group

cols = list(df7)
df7[cols] = df7[cols].div(df7[cols].sum(axis=1), axis=0).multiply(100)
df7

#in percentage of users for each group (graph)

df7.plot(kind = 'bar')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q4b</th>
      <th>Excellent</th>
      <th>Fair</th>
      <th>Good</th>
      <th>Very good</th>
    </tr>
    <tr>
      <th>user_education</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PECT (community rotation)</th>
      <td>8.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>PECT (industry rotation)</th>
      <td>9.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>pre-registration training</th>
      <td>8.0</td>
      <td>2.0</td>
      <td>5.0</td>
      <td>19.0</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q4b</th>
      <th>Excellent</th>
      <th>Fair</th>
      <th>Good</th>
      <th>Very good</th>
    </tr>
    <tr>
      <th>user_education</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PECT (community rotation)</th>
      <td>30.769231</td>
      <td>0.000000</td>
      <td>19.230769</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>PECT (industry rotation)</th>
      <td>39.130435</td>
      <td>0.000000</td>
      <td>13.043478</td>
      <td>47.826087</td>
    </tr>
    <tr>
      <th>pre-registration training</th>
      <td>23.529412</td>
      <td>5.882353</td>
      <td>14.705882</td>
      <td>55.882353</td>
    </tr>
  </tbody>
</table>
</div>






    <AxesSubplot:xlabel='user_education'>




    
![png](output_19_3.png)
    



```python
#survey q5a: What best describes your level of knowledge on managing the factors affecting long-term BPV, 
#BEFORE using the chatbot?

#in number of users

df8 = df.filter(items=['objectId', 'user_education', 'survey_q5a'])
survey_q5a_mymap = {'a': 'Excellent', 'b': 'Very good', 'c': 'Good', 'd': 'Fair', 'e': 'Poor'}
df8 = df8.applymap(lambda s: survey_q5a_mymap.get(s) if s in survey_q5a_mymap else s)
df8 = df8.groupby(['user_education','survey_q5a']).size().unstack(level=1)
df8 = df8.fillna(0)
df8

#in percentage of users for each group

cols = list(df8)
df8[cols] = df8[cols].div(df8[cols].sum(axis=1), axis=0).multiply(100)
df8

#in percentage of users for each group (graph)

df8.plot(kind = 'bar')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q5a</th>
      <th>Excellent</th>
      <th>Fair</th>
      <th>Good</th>
      <th>Poor</th>
      <th>Very good</th>
    </tr>
    <tr>
      <th>user_education</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PECT (community rotation)</th>
      <td>2.0</td>
      <td>3.0</td>
      <td>10.0</td>
      <td>4.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>PECT (industry rotation)</th>
      <td>0.0</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>6.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>pre-registration training</th>
      <td>3.0</td>
      <td>7.0</td>
      <td>10.0</td>
      <td>6.0</td>
      <td>8.0</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q5a</th>
      <th>Excellent</th>
      <th>Fair</th>
      <th>Good</th>
      <th>Poor</th>
      <th>Very good</th>
    </tr>
    <tr>
      <th>user_education</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PECT (community rotation)</th>
      <td>7.692308</td>
      <td>11.538462</td>
      <td>38.461538</td>
      <td>15.384615</td>
      <td>26.923077</td>
    </tr>
    <tr>
      <th>PECT (industry rotation)</th>
      <td>0.000000</td>
      <td>21.739130</td>
      <td>43.478261</td>
      <td>26.086957</td>
      <td>8.695652</td>
    </tr>
    <tr>
      <th>pre-registration training</th>
      <td>8.823529</td>
      <td>20.588235</td>
      <td>29.411765</td>
      <td>17.647059</td>
      <td>23.529412</td>
    </tr>
  </tbody>
</table>
</div>






    <AxesSubplot:xlabel='user_education'>




    
![png](output_20_3.png)
    



```python
#survey q5b: What best describes your level of knowledge on managing the factors affecting long-term BPV, 
#AFTER using the chatbot?

#in number of users

df9 = df.filter(items=['objectId', 'user_education', 'survey_q5b'])
survey_q5b_mymap = {'a': 'Excellent', 'b': 'Very good', 'c': 'Good', 'd': 'Fair', 'e': 'Poor'}
df9 = df9.applymap(lambda s: survey_q5b_mymap.get(s) if s in survey_q5b_mymap else s)
df9 = df9.groupby(['user_education','survey_q5b']).size().unstack(level=1)
df9 = df9.fillna(0)
df9

#in percentage of users for each group

cols = list(df9)
df9[cols] = df9[cols].div(df9[cols].sum(axis=1), axis=0).multiply(100)
df9

#in percentage of users for each group (graph)

df9.plot(kind = 'bar')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q5b</th>
      <th>Excellent</th>
      <th>Good</th>
      <th>Very good</th>
    </tr>
    <tr>
      <th>user_education</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PECT (community rotation)</th>
      <td>7</td>
      <td>4</td>
      <td>15</td>
    </tr>
    <tr>
      <th>PECT (industry rotation)</th>
      <td>11</td>
      <td>2</td>
      <td>10</td>
    </tr>
    <tr>
      <th>pre-registration training</th>
      <td>10</td>
      <td>6</td>
      <td>18</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q5b</th>
      <th>Excellent</th>
      <th>Good</th>
      <th>Very good</th>
    </tr>
    <tr>
      <th>user_education</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PECT (community rotation)</th>
      <td>26.923077</td>
      <td>15.384615</td>
      <td>57.692308</td>
    </tr>
    <tr>
      <th>PECT (industry rotation)</th>
      <td>47.826087</td>
      <td>8.695652</td>
      <td>43.478261</td>
    </tr>
    <tr>
      <th>pre-registration training</th>
      <td>29.411765</td>
      <td>17.647059</td>
      <td>52.941176</td>
    </tr>
  </tbody>
</table>
</div>






    <AxesSubplot:xlabel='user_education'>




    
![png](output_21_3.png)
    



```python
#survey q6: Rank the chatbot features from most liked to most disliked.

df10 = df.filter(items=['objectId', 'user_education', 'survey_q6'])

df10['survey_q6'] = df10['survey_q6'].str.lower()

df10_split = df10['survey_q6'].str.split(',', expand=True)

df10_split.columns = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth']
df10_split['first'] = df10_split['first'].str.replace(' ', '')
df10_split['second'] = df10_split['second'].str.replace(' ', '')
df10_split['third'] = df10_split['third'].str.replace(' ', '')
df10_split['fourth'] = df10_split['fourth'].str.replace(' ', '')
df10_split['fifth'] = df10_split['fifth'].str.replace(' ', '')
df10_split['sixth'] = df10_split['sixth'].str.replace(' ', '')
df10_split['seventh'] = df10_split['seventh'].str.replace(' ', '')
df10_split['eighth'] = df10_split['eighth'].str.replace(' ', '')
df10_split['ninth'] = df10_split['ninth'].str.replace(' ', '')

df10 = pd.concat([df10['user_education'], df10_split], axis=1)

#for the PECT (community rotation) group

df10_pect_comm = df10[df10['user_education'] == "PECT (community rotation)"]

df10_pect_comm_first = pd.DataFrame(df10_pect_comm['first'].value_counts())
df10_pect_comm_first.reset_index(level=0, inplace=True)

df10_pect_comm_second = pd.DataFrame(df10_pect_comm['second'].value_counts())
df10_pect_comm_second.reset_index(level=0, inplace=True)

df10_pect_comm_third = pd.DataFrame(df10_pect_comm['third'].value_counts())
df10_pect_comm_third.reset_index(level=0, inplace=True)

df10_pect_comm_fourth = pd.DataFrame(df10_pect_comm['fourth'].value_counts())
df10_pect_comm_fourth.reset_index(level=0, inplace=True)

df10_pect_comm_fifth = pd.DataFrame(df10_pect_comm['fifth'].value_counts())
df10_pect_comm_fifth.reset_index(level=0, inplace=True)

df10_pect_comm_sixth = pd.DataFrame(df10_pect_comm['sixth'].value_counts())
df10_pect_comm_sixth.reset_index(level=0, inplace=True)

df10_pect_comm_seventh = pd.DataFrame(df10_pect_comm['seventh'].value_counts())
df10_pect_comm_seventh.reset_index(level=0, inplace=True)

df10_pect_comm_eighth = pd.DataFrame(df10_pect_comm['eighth'].value_counts())
df10_pect_comm_eighth.reset_index(level=0, inplace=True)

df10_pect_comm_ninth = pd.DataFrame(df10_pect_comm['ninth'].value_counts())
df10_pect_comm_ninth.reset_index(level=0, inplace=True)

data_frames = [df10_pect_comm_first, df10_pect_comm_second, df10_pect_comm_third, df10_pect_comm_fourth, df10_pect_comm_fifth, df10_pect_comm_sixth, df10_pect_comm_seventh, df10_pect_comm_eighth, df10_pect_comm_ninth]
df10_pect_comm = reduce(lambda left,right: pd.merge(left,right,on=['index'], how='outer'), data_frames).fillna(0)
df10_pect_comm['total_count'] = df10_pect_comm.iloc[:,1:10].sum(axis=1)
df10_pect_comm['weighted_avg_rank'] = ((df10_pect_comm['first'] * 1) +  (df10_pect_comm['second'] * 2) + (df10_pect_comm['third'] * 3) + (df10_pect_comm['fourth'] * 4) + (df10_pect_comm['fifth'] * 5) + (df10_pect_comm['sixth'] * 6) + (df10_pect_comm['seventh'] * 7) + (df10_pect_comm['eighth'] * 8) + (df10_pect_comm['ninth'] * 9)) / df10_pect_comm['total_count']
survey_q6_mymap = {'a': 'Accessing via messaging app', 'b': 'Having a persona for the chatbot', 'c': 'Navigating by buttons only', 'd': 'Having a “Help” section', 'e': 'Having a “Fact of the day” section', 'f': 'Having well-segregated educational modules', 'g': 'Providing links to content resources', 'h': 'Having virtual patient assessment', 'i': 'Providing feedback on your virtual patient assessment'}
df10_pect_comm = df10_pect_comm.applymap(lambda s: survey_q6_mymap.get(s) if s in survey_q6_mymap else s)
df10_pect_comm

#for the PECT (industry rotation) group

df10_pect_ind = df10[df10['user_education'] == "PECT (industry rotation)"]

df10_pect_ind_first = pd.DataFrame(df10_pect_ind['first'].value_counts())
df10_pect_ind_first.reset_index(level=0, inplace=True)

df10_pect_ind_second = pd.DataFrame(df10_pect_ind['second'].value_counts())
df10_pect_ind_second.reset_index(level=0, inplace=True)

df10_pect_ind_third = pd.DataFrame(df10_pect_ind['third'].value_counts())
df10_pect_ind_third.reset_index(level=0, inplace=True)

df10_pect_ind_fourth = pd.DataFrame(df10_pect_ind['fourth'].value_counts())
df10_pect_ind_fourth.reset_index(level=0, inplace=True)

df10_pect_ind_fifth = pd.DataFrame(df10_pect_ind['fifth'].value_counts())
df10_pect_ind_fifth.reset_index(level=0, inplace=True)

df10_pect_ind_sixth = pd.DataFrame(df10_pect_ind['sixth'].value_counts())
df10_pect_ind_sixth.reset_index(level=0, inplace=True)

df10_pect_ind_seventh = pd.DataFrame(df10_pect_ind['seventh'].value_counts())
df10_pect_ind_seventh.reset_index(level=0, inplace=True)

df10_pect_ind_eighth = pd.DataFrame(df10_pect_ind['eighth'].value_counts())
df10_pect_ind_eighth.reset_index(level=0, inplace=True)

df10_pect_ind_ninth = pd.DataFrame(df10_pect_ind['ninth'].value_counts())
df10_pect_ind_ninth.reset_index(level=0, inplace=True)

data_frames = [df10_pect_ind_first, df10_pect_ind_second, df10_pect_ind_third, df10_pect_ind_fourth, df10_pect_ind_fifth, df10_pect_ind_sixth, df10_pect_ind_seventh, df10_pect_ind_eighth, df10_pect_ind_ninth]
df10_pect_ind = reduce(lambda left,right: pd.merge(left,right,on=['index'], how='outer'), data_frames).fillna(0)
df10_pect_ind['total_count'] = df10_pect_ind.iloc[:,1:10].sum(axis=1)
df10_pect_ind['weighted_avg_rank'] = ((df10_pect_ind['first'] * 1) +  (df10_pect_ind['second'] * 2) + (df10_pect_ind['third'] * 3) + (df10_pect_ind['fourth'] * 4) + (df10_pect_ind['fifth'] * 5) + (df10_pect_ind['sixth'] * 6) + (df10_pect_ind['seventh'] * 7) + (df10_pect_ind['eighth'] * 8) + (df10_pect_ind['ninth'] * 9)) / df10_pect_ind['total_count']
survey_q6_mymap = {'a': 'Accessing via messaging app', 'b': 'Having a persona for the chatbot', 'c': 'Navigating by buttons only', 'd': 'Having a “Help” section', 'e': 'Having a “Fact of the day” section', 'f': 'Having well-segregated educational modules', 'g': 'Providing links to content resources', 'h': 'Having virtual patient assessment', 'i': 'Providing feedback on your virtual patient assessment'}
df10_pect_ind = df10_pect_ind.applymap(lambda s: survey_q6_mymap.get(s) if s in survey_q6_mymap else s)
df10_pect_ind

#for the pre-registration training group

df10_prereg = df10[df10['user_education'] == "pre-registration training"]

df10_prereg_first = pd.DataFrame(df10_prereg['first'].value_counts())
df10_prereg_first.reset_index(level=0, inplace=True)

df10_prereg_second = pd.DataFrame(df10_prereg['second'].value_counts())
df10_prereg_second.reset_index(level=0, inplace=True)

df10_prereg_third = pd.DataFrame(df10_prereg['third'].value_counts())
df10_prereg_third.reset_index(level=0, inplace=True)

df10_prereg_fourth = pd.DataFrame(df10_prereg['fourth'].value_counts())
df10_prereg_fourth.reset_index(level=0, inplace=True)

df10_prereg_fifth = pd.DataFrame(df10_prereg['fifth'].value_counts())
df10_prereg_fifth.reset_index(level=0, inplace=True)

df10_prereg_sixth = pd.DataFrame(df10_prereg['sixth'].value_counts())
df10_prereg_sixth.reset_index(level=0, inplace=True)

df10_prereg_seventh = pd.DataFrame(df10_prereg['seventh'].value_counts())
df10_prereg_seventh.reset_index(level=0, inplace=True)

df10_prereg_eighth = pd.DataFrame(df10_prereg['eighth'].value_counts())
df10_prereg_eighth.reset_index(level=0, inplace=True)

df10_prereg_ninth = pd.DataFrame(df10_prereg['ninth'].value_counts())
df10_prereg_ninth.reset_index(level=0, inplace=True)

data_frames = [df10_prereg_first, df10_prereg_second, df10_prereg_third, df10_prereg_fourth, df10_prereg_fifth, df10_prereg_sixth, df10_prereg_seventh, df10_prereg_eighth, df10_prereg_ninth]
df10_prereg = reduce(lambda left,right: pd.merge(left,right,on=['index'], how='outer'), data_frames).fillna(0)
df10_prereg['total_count'] = df10_prereg.iloc[:,1:10].sum(axis=1)
df10_prereg['weighted_avg_rank'] = ((df10_prereg['first'] * 1) +  (df10_prereg['second'] * 2) + (df10_prereg['third'] * 3) + (df10_prereg['fourth'] * 4) + (df10_prereg['fifth'] * 5) + (df10_prereg['sixth'] * 6) + (df10_prereg['seventh'] * 7) + (df10_prereg['eighth'] * 8) + (df10_prereg['ninth'] * 9)) / df10_prereg['total_count']
survey_q6_mymap = {'a': 'Accessing via messaging app', 'b': 'Having a persona for the chatbot', 'c': 'Navigating by buttons only', 'd': 'Having a “Help” section', 'e': 'Having a “Fact of the day” section', 'f': 'Having well-segregated educational modules', 'g': 'Providing links to content resources', 'h': 'Having virtual patient assessment', 'i': 'Providing feedback on your virtual patient assessment'}
df10_prereg = df10_prereg.applymap(lambda s: survey_q6_mymap.get(s) if s in survey_q6_mymap else s)
df10_prereg
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>first</th>
      <th>second</th>
      <th>third</th>
      <th>fourth</th>
      <th>fifth</th>
      <th>sixth</th>
      <th>seventh</th>
      <th>eighth</th>
      <th>ninth</th>
      <th>total_count</th>
      <th>weighted_avg_rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Having virtual patient assessment</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>6.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>26.0</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Navigating by buttons only</td>
      <td>6.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>26.0</td>
      <td>3.153846</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Providing links to content resources</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>26.0</td>
      <td>3.769231</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Accessing via messaging app</td>
      <td>4.0</td>
      <td>8.0</td>
      <td>6.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>26.0</td>
      <td>2.846154</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Having well-segregated educational modules</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>12.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>26.0</td>
      <td>4.615385</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Providing feedback on your virtual patient ass...</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>6.0</td>
      <td>1.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>26.0</td>
      <td>4.653846</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Having a “Fact of the day” section</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>11.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>26.0</td>
      <td>6.500000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Having a persona for the chatbot</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>14.0</td>
      <td>9.0</td>
      <td>26.0</td>
      <td>8.192308</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Having a “Help” section</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>7.0</td>
      <td>13.0</td>
      <td>26.0</td>
      <td>8.269231</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>first</th>
      <th>second</th>
      <th>third</th>
      <th>fourth</th>
      <th>fifth</th>
      <th>sixth</th>
      <th>seventh</th>
      <th>eighth</th>
      <th>ninth</th>
      <th>total_count</th>
      <th>weighted_avg_rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Accessing via messaging app</td>
      <td>9.0</td>
      <td>2.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>23.0</td>
      <td>2.391304</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Providing links to content resources</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>23.0</td>
      <td>3.782609</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Navigating by buttons only</td>
      <td>4.0</td>
      <td>8.0</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>23.0</td>
      <td>3.173913</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Providing feedback on your virtual patient ass...</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>23.0</td>
      <td>4.304348</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Having well-segregated educational modules</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>10.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>23.0</td>
      <td>4.434783</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Having virtual patient assessment</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>23.0</td>
      <td>4.173913</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Having a “Fact of the day” section</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>23.0</td>
      <td>6.217391</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Having a persona for the chatbot</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>15.0</td>
      <td>23.0</td>
      <td>8.304348</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Having a “Help” section</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>14.0</td>
      <td>7.0</td>
      <td>23.0</td>
      <td>8.217391</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>first</th>
      <th>second</th>
      <th>third</th>
      <th>fourth</th>
      <th>fifth</th>
      <th>sixth</th>
      <th>seventh</th>
      <th>eighth</th>
      <th>ninth</th>
      <th>total_count</th>
      <th>weighted_avg_rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Navigating by buttons only</td>
      <td>10.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>8.0</td>
      <td>7.0</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>34.0</td>
      <td>3.764706</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Providing links to content resources</td>
      <td>9.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>10.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>34.0</td>
      <td>3.441176</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Accessing via messaging app</td>
      <td>8.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>12.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>34.0</td>
      <td>2.735294</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Having well-segregated educational modules</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>34.0</td>
      <td>4.205882</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Having virtual patient assessment</td>
      <td>2.0</td>
      <td>11.0</td>
      <td>8.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>34.0</td>
      <td>3.441176</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Providing feedback on your virtual patient ass...</td>
      <td>0.0</td>
      <td>8.0</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>34.0</td>
      <td>3.882353</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Having a persona for the chatbot</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>6.0</td>
      <td>4.0</td>
      <td>19.0</td>
      <td>34.0</td>
      <td>8.029412</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Having a “Fact of the day” section</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>15.0</td>
      <td>12.0</td>
      <td>2.0</td>
      <td>34.0</td>
      <td>7.323529</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Having a “Help” section</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>16.0</td>
      <td>12.0</td>
      <td>34.0</td>
      <td>8.176471</td>
    </tr>
  </tbody>
</table>
</div>




```python
#survey q7a: How relevant is the chatbot content during your <<stage of education>>?

#in number of users

df11 = df.filter(items=['objectId', 'user_education', 'survey_q7a'])
survey_q7a_mymap = {'a': 'Extremely relevant', 'b': 'Very relevant', 'c': 'Moderately relevant', 'd': 'Slightly relevant', 'e': 'Not relevant at all'}
df11 = df11.applymap(lambda s: survey_q7a_mymap.get(s) if s in survey_q7a_mymap else s)
df11 = df11.groupby(['user_education','survey_q7a']).size().unstack(level=1)
df11 = df11.fillna(0)
df11

#in percentage of users for each group

cols = list(df11)
df11[cols] = df11[cols].div(df11[cols].sum(axis=1), axis=0).multiply(100)
df11

#in percentage of users for each group (graph)

df11.plot(kind = 'bar')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q7a</th>
      <th>Extremely relevant</th>
      <th>Moderately relevant</th>
      <th>Not relevant at all</th>
      <th>Slightly relevant</th>
      <th>Very relevant</th>
    </tr>
    <tr>
      <th>user_education</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PECT (community rotation)</th>
      <td>2.0</td>
      <td>11.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>PECT (industry rotation)</th>
      <td>0.0</td>
      <td>7.0</td>
      <td>10.0</td>
      <td>3.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>pre-registration training</th>
      <td>0.0</td>
      <td>9.0</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>15.0</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q7a</th>
      <th>Extremely relevant</th>
      <th>Moderately relevant</th>
      <th>Not relevant at all</th>
      <th>Slightly relevant</th>
      <th>Very relevant</th>
    </tr>
    <tr>
      <th>user_education</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PECT (community rotation)</th>
      <td>7.692308</td>
      <td>42.307692</td>
      <td>0.000000</td>
      <td>19.230769</td>
      <td>30.769231</td>
    </tr>
    <tr>
      <th>PECT (industry rotation)</th>
      <td>0.000000</td>
      <td>30.434783</td>
      <td>43.478261</td>
      <td>13.043478</td>
      <td>13.043478</td>
    </tr>
    <tr>
      <th>pre-registration training</th>
      <td>0.000000</td>
      <td>26.470588</td>
      <td>0.000000</td>
      <td>29.411765</td>
      <td>44.117647</td>
    </tr>
  </tbody>
</table>
</div>






    <AxesSubplot:xlabel='user_education'>




    
![png](output_23_3.png)
    



```python
#survey q7b: Rank the educational content from most relevant to least relevant to your <<stage of education>>.

df12 = df.filter(items=['objectId', 'user_education', 'survey_q7b'])

df12['survey_q7b'] = df12['survey_q7b'].str.lower()

df12_split = df12['survey_q7b'].str.split(',', expand=True)

df12_split.columns = ['first', 'second', 'third', 'fourth']
df12_split['first'] = df12_split['first'].str.replace(' ', '')
df12_split['second'] = df12_split['second'].str.replace(' ', '')
df12_split['third'] = df12_split['third'].str.replace(' ', '')
df12_split['fourth'] = df12_split['fourth'].str.replace(' ', '')

df12 = pd.concat([df12['user_education'], df12_split], axis=1)

#for the PECT (community rotation) group

df12_pect_comm = df12[df12['user_education'] == "PECT (community rotation)"]

df12_pect_comm_first = pd.DataFrame(df12_pect_comm['first'].value_counts())
df12_pect_comm_first.reset_index(level=0, inplace=True)

df12_pect_comm_second = pd.DataFrame(df12_pect_comm['second'].value_counts())
df12_pect_comm_second.reset_index(level=0, inplace=True)

df12_pect_comm_third = pd.DataFrame(df12_pect_comm['third'].value_counts())
df12_pect_comm_third.reset_index(level=0, inplace=True)

df12_pect_comm_fourth = pd.DataFrame(df12_pect_comm['fourth'].value_counts())
df12_pect_comm_fourth.reset_index(level=0, inplace=True)

data_frames = [df12_pect_comm_first, df12_pect_comm_second, df12_pect_comm_third, df12_pect_comm_fourth]
df12_pect_comm = reduce(lambda left,right: pd.merge(left,right,on=['index'], how='outer'), data_frames).fillna(0)
df12_pect_comm['total_count'] = df12_pect_comm.iloc[:,1:5].sum(axis=1)
df12_pect_comm['weighted_avg_rank'] = ((df12_pect_comm['first'] * 1) +  (df12_pect_comm['second'] * 2) + (df12_pect_comm['third'] * 3) + (df12_pect_comm['fourth'] * 4)) / df12_pect_comm['total_count']
survey_q7b_mymap = {'a': 'Common factors that affect long-term BPV', 'b': 'How the factors affect long-term BPV', 'c': 'Appropriate questions to probe the patients to identify the factors affecting their long-term BPV', 'd': 'Management plan(s) for the factors affecting long-term BPV'}
df12_pect_comm = df12_pect_comm.applymap(lambda s: survey_q7b_mymap.get(s) if s in survey_q7b_mymap else s)
df12_pect_comm

#for the PECT (industry rotation) group

df12_pect_ind = df12[df12['user_education'] == "PECT (industry rotation)"]

df12_pect_ind_first = pd.DataFrame(df12_pect_ind['first'].value_counts())
df12_pect_ind_first.reset_index(level=0, inplace=True)

df12_pect_ind_second = pd.DataFrame(df12_pect_ind['second'].value_counts())
df12_pect_ind_second.reset_index(level=0, inplace=True)

df12_pect_ind_third = pd.DataFrame(df12_pect_ind['third'].value_counts())
df12_pect_ind_third.reset_index(level=0, inplace=True)

df12_pect_ind_fourth = pd.DataFrame(df12_pect_ind['fourth'].value_counts())
df12_pect_ind_fourth.reset_index(level=0, inplace=True)

data_frames = [df12_pect_ind_first, df12_pect_ind_second, df12_pect_ind_third, df12_pect_ind_fourth]
df12_pect_ind = reduce(lambda left,right: pd.merge(left,right,on=['index'], how='outer'), data_frames).fillna(0)
df12_pect_ind['total_count'] = df12_pect_ind.iloc[:,1:5].sum(axis=1)
df12_pect_ind['weighted_avg_rank'] = ((df12_pect_ind['first'] * 1) +  (df12_pect_ind['second'] * 2) + (df12_pect_ind['third'] * 3) + (df12_pect_ind['fourth'] * 4)) / df12_pect_ind['total_count']
survey_q7b_mymap = {'a': 'Common factors that affect long-term BPV', 'b': 'How the factors affect long-term BPV', 'c': 'Appropriate questions to probe the patients to identify the factors affecting their long-term BPV', 'd': 'Management plan(s) for the factors affecting long-term BPV'}
df12_pect_ind = df12_pect_ind.applymap(lambda s: survey_q7b_mymap.get(s) if s in survey_q7b_mymap else s)
df12_pect_ind

#for the pre-registration training group

df12_prereg = df12[df12['user_education'] == "pre-registration training"]

df12_prereg_first = pd.DataFrame(df12_prereg['first'].value_counts())
df12_prereg_first.reset_index(level=0, inplace=True)

df12_prereg_second = pd.DataFrame(df12_prereg['second'].value_counts())
df12_prereg_second.reset_index(level=0, inplace=True)

df12_prereg_third = pd.DataFrame(df12_prereg['third'].value_counts())
df12_prereg_third.reset_index(level=0, inplace=True)

df12_prereg_fourth = pd.DataFrame(df12_prereg['fourth'].value_counts())
df12_prereg_fourth.reset_index(level=0, inplace=True)

data_frames = [df12_prereg_first, df12_prereg_second, df12_prereg_third, df12_prereg_fourth]
df12_prereg = reduce(lambda left,right: pd.merge(left,right,on=['index'], how='outer'), data_frames).fillna(0)
df12_prereg['total_count'] = df12_prereg.iloc[:,1:5].sum(axis=1)
df12_prereg['weighted_avg_rank'] = ((df12_prereg['first'] * 1) +  (df12_prereg['second'] * 2) + (df12_prereg['third'] * 3) + (df12_prereg['fourth'] * 4)) / df12_prereg['total_count']
survey_q7b_mymap = {'a': 'Common factors that affect long-term BPV', 'b': 'How the factors affect long-term BPV', 'c': 'Appropriate questions to probe the patients to identify the factors affecting their long-term BPV', 'd': 'Management plan(s) for the factors affecting long-term BPV'}
df12_prereg = df12_prereg.applymap(lambda s: survey_q7b_mymap.get(s) if s in survey_q7b_mymap else s)
df12_prereg
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>first</th>
      <th>second</th>
      <th>third</th>
      <th>fourth</th>
      <th>total_count</th>
      <th>weighted_avg_rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Common factors that affect long-term BPV</td>
      <td>14.0</td>
      <td>4.0</td>
      <td>7</td>
      <td>1.0</td>
      <td>26.0</td>
      <td>1.807692</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Appropriate questions to probe the patients to...</td>
      <td>11.0</td>
      <td>7.0</td>
      <td>8</td>
      <td>0.0</td>
      <td>26.0</td>
      <td>1.884615</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Management plan(s) for the factors affecting l...</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>7</td>
      <td>3.0</td>
      <td>26.0</td>
      <td>2.461538</td>
    </tr>
    <tr>
      <th>3</th>
      <td>How the factors affect long-term BPV</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>4</td>
      <td>22.0</td>
      <td>26.0</td>
      <td>3.846154</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>first</th>
      <th>second</th>
      <th>third</th>
      <th>fourth</th>
      <th>total_count</th>
      <th>weighted_avg_rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Common factors that affect long-term BPV</td>
      <td>12.0</td>
      <td>8.0</td>
      <td>3</td>
      <td>0.0</td>
      <td>23.0</td>
      <td>1.608696</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Appropriate questions to probe the patients to...</td>
      <td>8.0</td>
      <td>10.0</td>
      <td>5</td>
      <td>0.0</td>
      <td>23.0</td>
      <td>1.869565</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Management plan(s) for the factors affecting l...</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>14</td>
      <td>1.0</td>
      <td>23.0</td>
      <td>2.565217</td>
    </tr>
    <tr>
      <th>3</th>
      <td>How the factors affect long-term BPV</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>22.0</td>
      <td>23.0</td>
      <td>3.956522</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>first</th>
      <th>second</th>
      <th>third</th>
      <th>fourth</th>
      <th>total_count</th>
      <th>weighted_avg_rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Common factors that affect long-term BPV</td>
      <td>19.0</td>
      <td>8.0</td>
      <td>6</td>
      <td>1.0</td>
      <td>34.0</td>
      <td>1.676471</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Appropriate questions to probe the patients to...</td>
      <td>13.0</td>
      <td>11.0</td>
      <td>10</td>
      <td>0.0</td>
      <td>34.0</td>
      <td>1.911765</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Management plan(s) for the factors affecting l...</td>
      <td>2.0</td>
      <td>15.0</td>
      <td>16</td>
      <td>1.0</td>
      <td>34.0</td>
      <td>2.470588</td>
    </tr>
    <tr>
      <th>3</th>
      <td>How the factors affect long-term BPV</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2</td>
      <td>32.0</td>
      <td>34.0</td>
      <td>3.941176</td>
    </tr>
  </tbody>
</table>
</div>




```python
#survey q8: How frequent would you be using this chatbot during your stage of education?

#in number of users

df13 = df.filter(items=['objectId', 'user_education', 'survey_q8'])
survey_q8_mymap = {'a': 'More than once a day', 'b': 'Once a day', 'c': 'Once a week', 'd': 'Once a month', 'e': 'Less than once a month'}
df13 = df13.applymap(lambda s: survey_q8_mymap.get(s) if s in survey_q8_mymap else s)
df13 = df13.groupby(['user_education','survey_q8']).size().unstack(level=1)
df13 = df13.fillna(0)
df13

#in percentage of users for each group

cols = list(df13)
df13[cols] = df13[cols].div(df13[cols].sum(axis=1), axis=0).multiply(100)
df13

#in percentage of users for each group (graph)

df13.plot(kind = 'bar')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q8</th>
      <th>Less than once a month</th>
      <th>Once a month</th>
      <th>Once a week</th>
    </tr>
    <tr>
      <th>user_education</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PECT (community rotation)</th>
      <td>15.0</td>
      <td>7.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>PECT (industry rotation)</th>
      <td>17.0</td>
      <td>6.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>pre-registration training</th>
      <td>18.0</td>
      <td>13.0</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q8</th>
      <th>Less than once a month</th>
      <th>Once a month</th>
      <th>Once a week</th>
    </tr>
    <tr>
      <th>user_education</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PECT (community rotation)</th>
      <td>57.692308</td>
      <td>26.923077</td>
      <td>15.384615</td>
    </tr>
    <tr>
      <th>PECT (industry rotation)</th>
      <td>73.913043</td>
      <td>26.086957</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>pre-registration training</th>
      <td>52.941176</td>
      <td>38.235294</td>
      <td>8.823529</td>
    </tr>
  </tbody>
</table>
</div>






    <AxesSubplot:xlabel='user_education'>




    
![png](output_25_3.png)
    



```python
#have a glance at the updated data

df['pre_total_score'] = df['pre_q1_score'] + df['pre_q2_score'] + df['pre_q3_score'] + df['pre_q4_score'] + df['pre_q5_score']
df['post_total_score'] = df['post_q1_score'] + df['post_q2_score'] + df['post_q3_score'] + df['post_q4_score'] + df['post_q5_score']
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>objectId</th>
      <th>user_education</th>
      <th>pre_q1</th>
      <th>pre_q2</th>
      <th>pre_q3</th>
      <th>pre_q4</th>
      <th>pre_q5</th>
      <th>post_q1</th>
      <th>post_q2</th>
      <th>post_q3</th>
      <th>...</th>
      <th>pre_q3_score</th>
      <th>pre_q4_score</th>
      <th>pre_q5_score</th>
      <th>post_q1_score</th>
      <th>post_q2_score</th>
      <th>post_q3_score</th>
      <th>post_q4_score</th>
      <th>post_q5_score</th>
      <th>pre_total_score</th>
      <th>post_total_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>nR0eH4BXBxqQ7Askn6B7</td>
      <td>PECT (community rotation)</td>
      <td>a,b</td>
      <td>a,b,d</td>
      <td>a</td>
      <td>a,b</td>
      <td>a,d</td>
      <td>a,b,d</td>
      <td>a,c,d</td>
      <td>a</td>
      <td>...</td>
      <td>1</td>
      <td>0.666667</td>
      <td>0.666667</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>4.000000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CUT0EUn0nhZAbFXeh0wP</td>
      <td>pre-registration training</td>
      <td>A, D</td>
      <td>A, D</td>
      <td>a</td>
      <td>C</td>
      <td>A, D</td>
      <td>A, B, D</td>
      <td>A, C, D</td>
      <td>a</td>
      <td>...</td>
      <td>1</td>
      <td>0.000000</td>
      <td>0.666667</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>1</td>
      <td>0.5</td>
      <td>1.0</td>
      <td>3.333333</td>
      <td>4.500000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NzwaGfA323uHOcrx36cT</td>
      <td>pre-registration training</td>
      <td>a, b, d</td>
      <td>a,c</td>
      <td>a</td>
      <td>a, b, d</td>
      <td>a, b, c, d</td>
      <td>a, b, c, d</td>
      <td>a, c, d</td>
      <td>a</td>
      <td>...</td>
      <td>1</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>4.166667</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>lUx7IcNBfmGYtJfAJY9F</td>
      <td>PECT (community rotation)</td>
      <td>a,d</td>
      <td>a,c</td>
      <td>a</td>
      <td>a,b,d</td>
      <td>a,c,d</td>
      <td>a,b,c,d</td>
      <td>a,b,d</td>
      <td>a</td>
      <td>...</td>
      <td>1</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>0.666667</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>4.166667</td>
      <td>4.666667</td>
    </tr>
    <tr>
      <th>4</th>
      <td>mLxmeiMBSAs6RPbKpRge</td>
      <td>pre-registration training</td>
      <td>a, b, c, d</td>
      <td>a, c</td>
      <td>a</td>
      <td>a, b, d</td>
      <td>a, c, d</td>
      <td>a, b, d</td>
      <td>a, b, d</td>
      <td>a</td>
      <td>...</td>
      <td>1</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>0.666667</td>
      <td>1</td>
      <td>0.5</td>
      <td>1.0</td>
      <td>4.500000</td>
      <td>4.166667</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 36 columns</p>
</div>




```python
df_pre_reg = df[df['user_education'] == 'pre-registration training'][['pre_total_score', 'post_total_score']]
df_pre_reg_pre = df_pre_reg[['pre_total_score']]
df_pre_reg_post = df_pre_reg[['post_total_score']]
df_pre_reg_diff = df_pre_reg['post_total_score'] - df_pre_reg['pre_total_score']

df_comm = df[df['user_education'] == 'PECT (community rotation)'][['pre_total_score', 'post_total_score']]
df_comm_pre = df_comm[['pre_total_score']]
df_comm_post = df_comm[['post_total_score']]
df_comm_diff = df_comm['post_total_score'] - df_comm['pre_total_score']

df_ind = df[df['user_education'] == 'PECT (industry rotation)'][['pre_total_score', 'post_total_score']]
df_ind_pre = df_ind[['pre_total_score']]
df_ind_post = df_ind[['post_total_score']]
df_ind_diff = df_ind['post_total_score'] - df_ind['pre_total_score']
```


```python
#Shapiro-Wilk test for normality 

#on the overall pre-learning test scores for the pre-registration training group
shapiro_test_pre_reg_pre = stats.shapiro(df_pre_reg_pre)
shapiro_test_pre_reg_pre

#on the overall post-learning test scores for the pre-registration training group
shapiro_test_pre_reg_post = stats.shapiro(df_pre_reg_post)
shapiro_test_pre_reg_post

#on the difference between pre- and post-learning test scores for the pre-registration training group
shapiro_test_pre_reg_diff = stats.shapiro(df_pre_reg_diff)
shapiro_test_pre_reg_diff

#on the overall pre-learning test scores for the PECT (community) group
shapiro_test_pect_comm_pre = stats.shapiro(df_comm_pre)
shapiro_test_pect_comm_pre

#on the overall post-learning test scores for the PECT (community) group
shapiro_test_pect_comm_post = stats.shapiro(df_comm_post)
shapiro_test_pect_comm_post

#on the difference between pre- and post-learning test scores for the PECT (community) group
shapiro_test_df_comm_diff = stats.shapiro(df_comm_diff)
shapiro_test_df_comm_diff

#on the overall pre-learning test scores for the PECT (industry) group
shapiro_test_pect_ind_pre = stats.shapiro(df_ind_pre)
shapiro_test_pect_ind_pre

#on the overall post-learning test scores for the PECT (industry) group
shapiro_test_pect_ind_post = stats.shapiro(df_ind_post)
shapiro_test_pect_ind_post

#on the difference between pre- and post-learning test scores for the PECT (industry) group
shapiro_test_ind_diff = stats.shapiro(df_ind_diff)
shapiro_test_ind_diff
```




    ShapiroResult(statistic=0.9544362425804138, pvalue=0.16663327813148499)






    ShapiroResult(statistic=0.9361758828163147, pvalue=0.047477979212999344)






    ShapiroResult(statistic=0.9705243706703186, pvalue=0.47608324885368347)






    ShapiroResult(statistic=0.9284019470214844, pvalue=0.07099725306034088)






    ShapiroResult(statistic=0.8851564526557922, pvalue=0.007410846184939146)






    ShapiroResult(statistic=0.9663644433021545, pvalue=0.5318065881729126)






    ShapiroResult(statistic=0.969998300075531, pvalue=0.6889638900756836)






    ShapiroResult(statistic=0.9564438462257385, pvalue=0.39544710516929626)






    ShapiroResult(statistic=0.9754382967948914, pvalue=0.8158712983131409)




```python
#pre-, post-learning test scores and their difference for the pre-registration training group

df_pre_reg['prereg_score_diff'] = df_pre_reg['post_total_score'] - df_pre_reg['pre_total_score']
df_pre_reg.describe()

#Wilcoxon signed-rank test between the pre- and post-learning test scores

stats.wilcoxon(df_pre_reg['post_total_score'], df_pre_reg['pre_total_score'], alternative='greater')

#conclusion: statistically significant score improvement for pre-registration training group
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pre_total_score</th>
      <th>post_total_score</th>
      <th>prereg_score_diff</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>34.000000</td>
      <td>34.000000</td>
      <td>34.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3.789216</td>
      <td>4.348039</td>
      <td>0.558824</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.691834</td>
      <td>0.444509</td>
      <td>0.675301</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2.500000</td>
      <td>3.500000</td>
      <td>-0.833333</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>3.333333</td>
      <td>4.000000</td>
      <td>0.166667</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>3.750000</td>
      <td>4.333333</td>
      <td>0.666667</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>4.166667</td>
      <td>4.666667</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>1.666667</td>
    </tr>
  </tbody>
</table>
</div>






    WilcoxonResult(statistic=489.0, pvalue=9.648474408967074e-05)




```python
#pre-, post-learning test scores and their difference for the PECT (community) group

df_comm['comm_score_diff'] = df_comm['post_total_score'] - df_comm['pre_total_score']
df_comm.describe()

#Wilcoxon signed-rank test between the pre- and post-learning test scores

stats.wilcoxon(df_comm['post_total_score'], df_comm['pre_total_score'], alternative='greater')

#conclusion: statistically significant score improvement for PECT (community) training group
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pre_total_score</th>
      <th>post_total_score</th>
      <th>comm_score_diff</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>26.000000</td>
      <td>26.000000</td>
      <td>26.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3.179487</td>
      <td>4.057692</td>
      <td>0.878205</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.852347</td>
      <td>0.821844</td>
      <td>0.917191</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.500000</td>
      <td>2.333333</td>
      <td>-0.666667</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2.541667</td>
      <td>3.708333</td>
      <td>0.208333</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>3.500000</td>
      <td>4.083333</td>
      <td>0.833333</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>3.833333</td>
      <td>4.666667</td>
      <td>1.500000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>4.333333</td>
      <td>5.000000</td>
      <td>3.166667</td>
    </tr>
  </tbody>
</table>
</div>






    WilcoxonResult(statistic=298.0, pvalue=0.00013102656344575925)




```python
#pre-, post-learning test scores and their difference for the PECT (industry) group

df_ind['ind_score_diff'] = df_ind['post_total_score'] - df_ind['pre_total_score']
df_ind.describe()

#Wilcoxon signed-rank test between the pre- and post-learning test scores

stats.wilcoxon(df_ind['post_total_score'], df_ind['pre_total_score'], alternative='greater')

#conclusion: statistically significant score improvement for PECT (industry) training group
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pre_total_score</th>
      <th>post_total_score</th>
      <th>ind_score_diff</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>23.000000</td>
      <td>23.000000</td>
      <td>23.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3.137681</td>
      <td>4.057971</td>
      <td>0.920290</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.634950</td>
      <td>0.608460</td>
      <td>0.893113</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.833333</td>
      <td>2.833333</td>
      <td>-0.666667</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2.750000</td>
      <td>3.583333</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>3.166667</td>
      <td>4.000000</td>
      <td>0.833333</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>3.500000</td>
      <td>4.583333</td>
      <td>1.583333</td>
    </tr>
    <tr>
      <th>max</th>
      <td>4.166667</td>
      <td>5.000000</td>
      <td>2.833333</td>
    </tr>
  </tbody>
</table>
</div>



    /home/jianyang/my_project_dir/my_env/lib/python3.8/site-packages/scipy/stats/morestats.py:2967: UserWarning: Exact p-value calculation does not work if there are ties. Switching to normal approximation.
      warnings.warn("Exact p-value calculation does not work if there are "





    WilcoxonResult(statistic=237.0, pvalue=0.00016455319733510624)




```python
#boxplot of score differential for the 3 groups

boxplot_df = pd.concat([df_pre_reg['prereg_score_diff'], df_comm['comm_score_diff'], df_ind['ind_score_diff']], axis=1)
boxplot = boxplot_df.boxplot(patch_artist=True)

#Kruskal-Wallis test between the score differentials

stats.kruskal(df_comm_diff, df_ind_diff, df_pre_reg_diff)

#conclusion: no statistically signficant difference in score differential between the 3 groups
```




    KruskalResult(statistic=3.0028977518442037, pvalue=0.2228071063208662)




    
![png](output_32_1.png)
    



```python
#updated data

df14 = df.filter(items=['objectId', 'survey_q4a'])
survey_q4a_mymap = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}
df14 = df14.applymap(lambda s: survey_q4a_mymap.get(s) if s in survey_q4a_mymap else s)
df14.rename(columns={'survey_q4a':'survey_q4a_score'}, inplace=True)
df = pd.concat([df, df14['survey_q4a_score']], axis=1)

df15 = df.filter(items=['objectId', 'survey_q4b'])
survey_q4b_mymap = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}
df15 = df15.applymap(lambda s: survey_q4b_mymap.get(s) if s in survey_q4b_mymap else s)
df15.rename(columns={'survey_q4b':'survey_q4b_score'}, inplace=True)
df = pd.concat([df, df15['survey_q4b_score']], axis=1)

df16 = df.filter(items=['objectId', 'survey_q5a'])
survey_q5a_mymap = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}
df16 = df16.applymap(lambda s: survey_q5a_mymap.get(s) if s in survey_q5a_mymap else s)
df16.rename(columns={'survey_q5a':'survey_q5a_score'}, inplace=True)
df = pd.concat([df, df16['survey_q5a_score']], axis=1)

df17 = df.filter(items=['objectId', 'survey_q5b'])
survey_q5b_mymap = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}
df17 = df17.applymap(lambda s: survey_q5b_mymap.get(s) if s in survey_q5b_mymap else s)
df17.rename(columns={'survey_q5b':'survey_q5b_score'}, inplace=True)
df = pd.concat([df, df17['survey_q5b_score']], axis=1)

df['identification_diff_perception'] = df['survey_q4b_score'] - df['survey_q4a_score']
df['management_diff_perception'] = df['survey_q5b_score'] - df['survey_q5a_score']

df['identification_diff_test'] = df['post_q1_score'] + df['post_q4_score'] - (df['pre_q1_score'] + df['pre_q4_score'])
df['management_diff_test'] = df['post_q2_score'] + df['post_q5_score'] - (df['pre_q2_score'] + df['pre_q5_score'])

df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>objectId</th>
      <th>user_education</th>
      <th>pre_q1</th>
      <th>pre_q2</th>
      <th>pre_q3</th>
      <th>pre_q4</th>
      <th>pre_q5</th>
      <th>post_q1</th>
      <th>post_q2</th>
      <th>post_q3</th>
      <th>...</th>
      <th>pre_total_score</th>
      <th>post_total_score</th>
      <th>survey_q4a_score</th>
      <th>survey_q4b_score</th>
      <th>survey_q5a_score</th>
      <th>survey_q5b_score</th>
      <th>identification_diff_perception</th>
      <th>management_diff_perception</th>
      <th>identification_diff_test</th>
      <th>management_diff_test</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>nR0eH4BXBxqQ7Askn6B7</td>
      <td>PECT (community rotation)</td>
      <td>a,b</td>
      <td>a,b,d</td>
      <td>a</td>
      <td>a,b</td>
      <td>a,d</td>
      <td>a,b,d</td>
      <td>a,c,d</td>
      <td>a</td>
      <td>...</td>
      <td>4.000000</td>
      <td>5.000000</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0.666667</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CUT0EUn0nhZAbFXeh0wP</td>
      <td>pre-registration training</td>
      <td>A, D</td>
      <td>A, D</td>
      <td>a</td>
      <td>C</td>
      <td>A, D</td>
      <td>A, B, D</td>
      <td>A, C, D</td>
      <td>a</td>
      <td>...</td>
      <td>3.333333</td>
      <td>4.500000</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>0.833333</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NzwaGfA323uHOcrx36cT</td>
      <td>pre-registration training</td>
      <td>a, b, d</td>
      <td>a,c</td>
      <td>a</td>
      <td>a, b, d</td>
      <td>a, b, c, d</td>
      <td>a, b, c, d</td>
      <td>a, c, d</td>
      <td>a</td>
      <td>...</td>
      <td>4.166667</td>
      <td>5.000000</td>
      <td>5</td>
      <td>4</td>
      <td>5</td>
      <td>5</td>
      <td>-1</td>
      <td>0</td>
      <td>0.333333</td>
      <td>0.500000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>lUx7IcNBfmGYtJfAJY9F</td>
      <td>PECT (community rotation)</td>
      <td>a,d</td>
      <td>a,c</td>
      <td>a</td>
      <td>a,b,d</td>
      <td>a,c,d</td>
      <td>a,b,c,d</td>
      <td>a,b,d</td>
      <td>a</td>
      <td>...</td>
      <td>4.166667</td>
      <td>4.666667</td>
      <td>3</td>
      <td>4</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>0.333333</td>
      <td>0.166667</td>
    </tr>
    <tr>
      <th>4</th>
      <td>mLxmeiMBSAs6RPbKpRge</td>
      <td>pre-registration training</td>
      <td>a, b, c, d</td>
      <td>a, c</td>
      <td>a</td>
      <td>a, b, d</td>
      <td>a, c, d</td>
      <td>a, b, d</td>
      <td>a, b, d</td>
      <td>a</td>
      <td>...</td>
      <td>4.500000</td>
      <td>4.166667</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>3</td>
      <td>-0.500000</td>
      <td>0.166667</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>78</th>
      <td>s5iqNr1xkWHFvh8hlmGB</td>
      <td>PECT (community rotation)</td>
      <td>A, b, d</td>
      <td>D</td>
      <td>a</td>
      <td>A, b</td>
      <td>A, b, c</td>
      <td>B, d</td>
      <td>A, c, d</td>
      <td>a</td>
      <td>...</td>
      <td>3.500000</td>
      <td>4.666667</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0.333333</td>
      <td>0.833333</td>
    </tr>
    <tr>
      <th>79</th>
      <td>PosA3ijlNO2R366ou7Yw</td>
      <td>PECT (industry rotation)</td>
      <td>A, B</td>
      <td>A, C</td>
      <td>a</td>
      <td>B</td>
      <td>A</td>
      <td>A, B, D</td>
      <td>A, D</td>
      <td>a</td>
      <td>...</td>
      <td>2.833333</td>
      <td>4.666667</td>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>4</td>
      <td>4</td>
      <td>1.000000</td>
      <td>0.833333</td>
    </tr>
    <tr>
      <th>80</th>
      <td>WNWxCfTGRXmCTtbQkoXl</td>
      <td>PECT (industry rotation)</td>
      <td>a</td>
      <td>a</td>
      <td>b</td>
      <td>d</td>
      <td>c,d</td>
      <td>a,b,c,d</td>
      <td>a,d</td>
      <td>a</td>
      <td>...</td>
      <td>1.833333</td>
      <td>4.666667</td>
      <td>2</td>
      <td>5</td>
      <td>2</td>
      <td>5</td>
      <td>3</td>
      <td>3</td>
      <td>1.333333</td>
      <td>0.500000</td>
    </tr>
    <tr>
      <th>81</th>
      <td>vyMupERq1OJen1an4P5A</td>
      <td>PECT (industry rotation)</td>
      <td>a, b</td>
      <td>a, d</td>
      <td>b</td>
      <td>a, b</td>
      <td>a, d</td>
      <td>b, c, d</td>
      <td>a, c</td>
      <td>a</td>
      <td>...</td>
      <td>3.000000</td>
      <td>4.000000</td>
      <td>1</td>
      <td>4</td>
      <td>1</td>
      <td>5</td>
      <td>3</td>
      <td>4</td>
      <td>0.333333</td>
      <td>-0.333333</td>
    </tr>
    <tr>
      <th>82</th>
      <td>sBEqTYXgMeR3VVTuG46H</td>
      <td>PECT (industry rotation)</td>
      <td>b, c</td>
      <td>a, b</td>
      <td>a</td>
      <td>a, b</td>
      <td>a, d</td>
      <td>a, b, d</td>
      <td>a, c, d</td>
      <td>a</td>
      <td>...</td>
      <td>3.166667</td>
      <td>5.000000</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>2</td>
      <td>1.000000</td>
      <td>0.833333</td>
    </tr>
  </tbody>
</table>
<p>83 rows × 44 columns</p>
</div>




```python
df_prereg_corr = df[df['user_education'] == 'pre-registration training'][['identification_diff_test', 'management_diff_test', 'identification_diff_perception', 'management_diff_perception']]
df_comm_corr = df[df['user_education'] == 'PECT (community rotation)'][['identification_diff_test', 'management_diff_test', 'identification_diff_perception', 'management_diff_perception']]
df_ind_corr = df[df['user_education'] == 'PECT (industry rotation)'][['identification_diff_test', 'management_diff_test', 'identification_diff_perception', 'management_diff_perception']]
```


```python
#for the pre-registration training group

#Kendall rank correlation coefficient between actual test scores and perceived level of knowledge [on identification of factors affecting long-term BPV]

df_prereg_corr_identification = df_prereg_corr[['identification_diff_test', 'identification_diff_perception']]
stats.kendalltau(df_prereg_corr['identification_diff_test'], df_prereg_corr['identification_diff_perception'])

#conclusion: negligable correlation, not statistically significant

#Kendall rank correlation coefficient between actual test scores and perceived level of knowledge [on management of factors affecting long-term BPV]

df_prereg_corr_management = df_prereg_corr[['management_diff_test', 'management_diff_perception']]
stats.kendalltau(df_prereg_corr['management_diff_test'], df_prereg_corr['management_diff_perception'])

#conclusion: negligable correlation, not statistically significant
```




    KendalltauResult(correlation=0.15736998685076214, pvalue=0.25189253225271324)






    KendalltauResult(correlation=-0.017103155836767758, pvalue=0.9005876217059309)




```python
#for the PECT (community) group

#Kendall rank correlation coefficient between actual test scores and perceived level of knowledge [on identification of factors affecting long-term BPV]

df_comm_corr_identification = df_comm_corr[['identification_diff_test', 'identification_diff_perception']]
stats.kendalltau(df_comm_corr['identification_diff_test'], df_comm_corr['identification_diff_perception'])

#conclusion: negligable correlation, not statistically significant

#Kendall rank correlation coefficient between actual test scores and perceived level of knowledge [on management of factors affecting long-term BPV]

df_comm_corr_management = df_comm_corr[['management_diff_test', 'management_diff_perception']]
stats.kendalltau(df_comm_corr['management_diff_test'], df_comm_corr['management_diff_perception'])

#conclusion: negligable correlation, not statistically significant
```




    KendalltauResult(correlation=-0.10505549709297515, pvalue=0.5091562995340383)






    KendalltauResult(correlation=-0.048838370567834424, pvalue=0.7604387705355786)




```python
#for the PECT (industry) group

#Kendall rank correlation coefficient between actual test scores and perceived level of knowledge [on identification of factors affecting long-term BPV]

df_ind_corr_identification = df_ind_corr[['identification_diff_test', 'identification_diff_perception']]
stats.kendalltau(df_ind_corr['identification_diff_test'], df_ind_corr['identification_diff_perception'])

#conclusion: moderate positive correlation, statistically significant

#Kendall rank correlation coefficient between actual test scores and perceived level of knowledge [on management of factors affecting long-term BPV]

df_ind_corr_management = df_ind_corr[['management_diff_test', 'management_diff_perception']]
stats.kendalltau(df_ind_corr['management_diff_test'], df_ind_corr['management_diff_perception'])

#conclusion: negligable correlation, not statistically significant
```




    KendalltauResult(correlation=0.4213233131809254, pvalue=0.013050629786313833)






    KendalltauResult(correlation=0.21309769595029335, pvalue=0.19788820278106312)




```python
#graphical representation of the correlation coefficient between actual test scores and perceived level of knowledge for the 3 groups

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
sns.regplot(x="management_diff_test", y="management_diff_perception", data=df_prereg_corr_management, ax=axes[1, 0], color='#8f9805')
sns.regplot(x="management_diff_test", y="management_diff_perception", data=df_comm_corr_management, ax=axes[1, 1], color='c')
sns.regplot(x="management_diff_test", y="management_diff_perception", data=df_ind_corr_management, ax=axes[1, 2], color='mediumvioletred')
sns.regplot(x="identification_diff_test", y="identification_diff_perception", data=df_prereg_corr_identification, ax=axes[0, 0], color='#8f9805')
sns.regplot(x="identification_diff_test", y="identification_diff_perception", data=df_comm_corr_identification, ax=axes[0, 1], color='c')
sns.regplot(x="identification_diff_test", y="identification_diff_perception", data=df_ind_corr_identification, ax=axes[0, 2], color='mediumvioletred')
axes[1,0].set(xlim=(-1.5, 1.5), ylim=(-1.5, 4.5), xlabel= None, ylabel= 'Perception differential (knowledge on management)', )
axes[1,1].set(xlim=(-1.5, 1.5), ylim=(-1.5, 4.5), xlabel= 'Assessment score differential (knowledge on management)', ylabel= None)
axes[1,2].set(xlim=(-1.5, 1.5), ylim=(-1.5, 4.5), xlabel= None, ylabel= None)
axes[0,0].set(xlim=(-1.5, 1.5), ylim=(-1.5, 4.5), xlabel= None, ylabel= 'Perception differential (knowledge on identification)')
axes[0,0].set(title='Pre-registration')
axes[0,1].set(xlim=(-1.5, 1.5), ylim=(-1.5, 4.5), xlabel= 'Assessment score differential (knowledge on identification)', ylabel= None)
axes[0,1].set(title='PECT (community)')
axes[0,2].set(xlim=(-1.5, 1.5), ylim=(-1.5, 4.5), xlabel= None, ylabel= None)
axes[0,2].set(title='PECT (industry)')
plt.show()
```




    <AxesSubplot:xlabel='management_diff_test', ylabel='management_diff_perception'>






    <AxesSubplot:xlabel='management_diff_test', ylabel='management_diff_perception'>






    <AxesSubplot:xlabel='management_diff_test', ylabel='management_diff_perception'>






    <AxesSubplot:xlabel='identification_diff_test', ylabel='identification_diff_perception'>






    <AxesSubplot:xlabel='identification_diff_test', ylabel='identification_diff_perception'>






    <AxesSubplot:xlabel='identification_diff_test', ylabel='identification_diff_perception'>






    [(-1.5, 1.5),
     (-1.5, 4.5),
     Text(0.5, 0, ''),
     Text(0, 0.5, 'Perception differential (knowledge on management)')]






    [(-1.5, 1.5),
     (-1.5, 4.5),
     Text(0.5, 0, 'Assessment score differential (knowledge on management)'),
     Text(0, 0.5, '')]






    [(-1.5, 1.5), (-1.5, 4.5), Text(0.5, 0, ''), Text(0, 0.5, '')]






    [(-1.5, 1.5),
     (-1.5, 4.5),
     Text(0.5, 0, ''),
     Text(0, 0.5, 'Perception differential (knowledge on identification)')]






    [Text(0.5, 1.0, 'Pre-registration')]






    [(-1.5, 1.5),
     (-1.5, 4.5),
     Text(0.5, 0, 'Assessment score differential (knowledge on identification)'),
     Text(0, 0.5, '')]






    [Text(0.5, 1.0, 'PECT (community)')]






    [(-1.5, 1.5), (-1.5, 4.5), Text(0.5, 0, ''), Text(0, 0.5, '')]






    [Text(0.5, 1.0, 'PECT (industry)')]




    
![png](output_38_15.png)
    



```python
#updated data

df['identification_post_test'] = df['post_q1_score'] + df['post_q4_score']
df['identification_pre_test'] = df['pre_q1_score'] + df['pre_q4_score']
df['management_post_test'] = df['post_q2_score'] + df['post_q5_score']
df['management_pre_test'] = df['pre_q2_score'] + df['pre_q5_score']

df_prereg_corr_2 = df[df['user_education'] == 'pre-registration training'][['survey_q4a_score', 'survey_q4b_score', 'survey_q5a_score', 'survey_q5b_score', 'management_pre_test', 'management_post_test', 'identification_pre_test', 'identification_post_test']]
df_comm_corr_2 = df[df['user_education'] == 'PECT (community rotation)'][['survey_q4a_score', 'survey_q4b_score', 'survey_q5a_score', 'survey_q5b_score', 'management_pre_test', 'management_post_test', 'identification_pre_test', 'identification_post_test']]
df_ind_corr_2 = df[df['user_education'] == 'PECT (industry rotation)'][['survey_q4a_score', 'survey_q4b_score', 'survey_q5a_score', 'survey_q5b_score', 'management_pre_test', 'management_post_test', 'identification_pre_test', 'identification_post_test']]
```


```python
#for the pre-registration training group

#Kendall rank correlation coefficient between actual test scores and perceived level of knowledge, for both pre- and post-learning

stats.kendalltau(df_prereg_corr_2['survey_q4a_score'], df_prereg_corr_2['identification_pre_test'])
stats.kendalltau(df_prereg_corr_2['survey_q4b_score'], df_prereg_corr_2['identification_post_test'])
stats.kendalltau(df_prereg_corr_2['survey_q5a_score'], df_prereg_corr_2['management_pre_test'])
stats.kendalltau(df_prereg_corr_2['survey_q5b_score'], df_prereg_corr_2['management_post_test'])

#conclusion: all negligable correlation, not statistically significant
```




    KendalltauResult(correlation=0.2271554252121273, pvalue=0.11161464228738378)






    KendalltauResult(correlation=0.06442550097815462, pvalue=0.6671481939692023)






    KendalltauResult(correlation=0.14972151149925939, pvalue=0.29070738669372653)






    KendalltauResult(correlation=-0.15612981557711997, pvalue=0.3163494829310012)




```python
#for the PECT (community) group

#Kendall rank correlation coefficient between actual test scores and perceived level of knowledge, for both pre- and post-learning

stats.kendalltau(df_comm_corr_2['survey_q4a_score'], df_comm_corr_2['identification_pre_test'])
stats.kendalltau(df_comm_corr_2['survey_q4b_score'], df_comm_corr_2['identification_post_test'])
stats.kendalltau(df_comm_corr_2['survey_q5a_score'], df_comm_corr_2['management_pre_test'])
stats.kendalltau(df_comm_corr_2['survey_q5b_score'], df_comm_corr_2['management_post_test'])

#conclusion: all negligable correlation, not statistically significant; except for between post-learning identification score and perception (moderate negative correlation)
```




    KendalltauResult(correlation=-0.245181892901518, pvalue=0.13953962742990672)






    KendalltauResult(correlation=-0.42633618882242774, pvalue=0.013125360411551096)






    KendalltauResult(correlation=-0.22937672185417132, pvalue=0.1667924490382371)






    KendalltauResult(correlation=-0.16102535770970636, pvalue=0.36813333324013775)




```python
#for the PECT (industry) group

#Kendall rank correlation coefficient between actual test scores and perceived level of knowledge, for both pre- and post-learning

stats.kendalltau(df_ind_corr_2['survey_q4a_score'], df_ind_corr_2['identification_pre_test'])
stats.kendalltau(df_ind_corr_2['survey_q4b_score'], df_ind_corr_2['identification_post_test'])
stats.kendalltau(df_ind_corr_2['survey_q5a_score'], df_ind_corr_2['management_pre_test'])
stats.kendalltau(df_ind_corr_2['survey_q5b_score'], df_ind_corr_2['management_post_test'])

#conclusion: all negligable correlation, not statistically significant; except for between post-learning identification score and perception (moderate positive correlation)
```




    KendalltauResult(correlation=0.1350447409819031, pvalue=0.4646816412035434)






    KendalltauResult(correlation=0.35800029384704146, pvalue=0.05298938603131427)






    KendalltauResult(correlation=0.2913428162916919, pvalue=0.10399159980765983)






    KendalltauResult(correlation=-0.08336074110691877, pvalue=0.6718703645852881)




```python
#graphical representation of the correlation coefficient between actual test scores and perceived level of knowledge, for both pre- and post-learning, for the 3 groups
#on the IDENTIFICATION of the factors affecting long-term BPV

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
sns.regplot(x="identification_post_test", y="survey_q4b_score", data=df_prereg_corr_2, ax=axes[1, 0], color='#8f9805')
sns.regplot(x="identification_post_test", y="survey_q4b_score", data=df_comm_corr_2, ax=axes[1, 1], color='c')
sns.regplot(x="identification_post_test", y="survey_q4b_score", data=df_ind_corr_2, ax=axes[1, 2], color='mediumvioletred')
sns.regplot(x="identification_pre_test", y="survey_q4a_score", data=df_prereg_corr_2, ax=axes[0, 0], color='#8f9805')
sns.regplot(x="identification_pre_test", y="survey_q4a_score", data=df_comm_corr_2, ax=axes[0, 1], color='c')
sns.regplot(x="identification_pre_test", y="survey_q4a_score", data=df_ind_corr_2, ax=axes[0, 2], color='mediumvioletred')
axes[1,0].set(xlim=(0.5, 2.5), ylim=(0, 6), xlabel= None, ylabel= 'Perception (knowledge on identification after using chatbot)', )
axes[1,1].set(xlim=(0.5, 2.5), ylim=(0, 6), xlabel= 'Assessment score (knowledge on identification after using chatbot)', ylabel= None)
axes[1,2].set(xlim=(0.5, 2.5), ylim=(0, 6), xlabel= None, ylabel= None)
axes[0,0].set(xlim=(0.5, 2.5), ylim=(0, 6), xlabel= None, ylabel= 'Perception (knowledge on identification before using chatbot)')
axes[0,0].set(title='Pre-registration')
axes[0,1].set(xlim=(0.5, 2.5), ylim=(0, 6), xlabel= 'Assessment score (knowledge on identification before using chatbot)', ylabel= None)
axes[0,1].set(title='PECT (community)')
axes[0,2].set(xlim=(0.5, 2.5), ylim=(0, 6), xlabel= None, ylabel= None)
axes[0,2].set(title='PECT (industry)')
plt.show()
```




    <AxesSubplot:xlabel='identification_post_test', ylabel='survey_q4b_score'>






    <AxesSubplot:xlabel='identification_post_test', ylabel='survey_q4b_score'>






    <AxesSubplot:xlabel='identification_post_test', ylabel='survey_q4b_score'>






    <AxesSubplot:xlabel='identification_pre_test', ylabel='survey_q4a_score'>






    <AxesSubplot:xlabel='identification_pre_test', ylabel='survey_q4a_score'>






    <AxesSubplot:xlabel='identification_pre_test', ylabel='survey_q4a_score'>






    [(0.5, 2.5),
     (0.0, 6.0),
     Text(0.5, 0, ''),
     Text(0, 0.5, 'Perception (knowledge on identification after using chatbot)')]






    [(0.5, 2.5),
     (0.0, 6.0),
     Text(0.5, 0, 'Assessment score (knowledge on identification after using chatbot)'),
     Text(0, 0.5, '')]






    [(0.5, 2.5), (0.0, 6.0), Text(0.5, 0, ''), Text(0, 0.5, '')]






    [(0.5, 2.5),
     (0.0, 6.0),
     Text(0.5, 0, ''),
     Text(0, 0.5, 'Perception (knowledge on identification before using chatbot)')]






    [Text(0.5, 1.0, 'Pre-registration')]






    [(0.5, 2.5),
     (0.0, 6.0),
     Text(0.5, 0, 'Assessment score (knowledge on identification before using chatbot)'),
     Text(0, 0.5, '')]






    [Text(0.5, 1.0, 'PECT (community)')]






    [(0.5, 2.5), (0.0, 6.0), Text(0.5, 0, ''), Text(0, 0.5, '')]






    [Text(0.5, 1.0, 'PECT (industry)')]




    
![png](output_43_15.png)
    



```python
#graphical representation of the correlation coefficient between actual test scores and perceived level of knowledge, for both pre- and post-learning, for the 3 groups
#on the MANAGEMENT of the factors affecting long-term BPV

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
sns.regplot(x="management_post_test", y="survey_q5b_score", data=df_prereg_corr_2, ax=axes[1, 0], color='#8f9805')
sns.regplot(x="management_post_test", y="survey_q5b_score", data=df_comm_corr_2, ax=axes[1, 1], color='c')
sns.regplot(x="management_post_test", y="survey_q5b_score", data=df_ind_corr_2, ax=axes[1, 2], color='mediumvioletred')
sns.regplot(x="management_pre_test", y="survey_q5a_score", data=df_prereg_corr_2, ax=axes[0, 0], color='#8f9805')
sns.regplot(x="management_pre_test", y="survey_q5a_score", data=df_comm_corr_2, ax=axes[0, 1], color='c')
sns.regplot(x="management_pre_test", y="survey_q5a_score", data=df_ind_corr_2, ax=axes[0, 2], color='mediumvioletred')
axes[1,0].set(xlim=(0.5, 2.5), ylim=(0, 6), xlabel= None, ylabel= 'Perception (knowledge on management after using chatbot)', )
axes[1,1].set(xlim=(0.5, 2.5), ylim=(0, 6), xlabel= 'Assessment score (knowledge on management after using chatbot)', ylabel= None)
axes[1,2].set(xlim=(0.5, 2.5), ylim=(0, 6), xlabel= None, ylabel= None)
axes[0,0].set(xlim=(0.5, 2.5), ylim=(0, 6), xlabel= None, ylabel= 'Perception (knowledge on management before using chatbot)')
axes[0,0].set(title='Pre-registration')
axes[0,1].set(xlim=(0.5, 2.5), ylim=(0, 6), xlabel= 'Assessment score (knowledge on management before using chatbot)', ylabel= None)
axes[0,1].set(title='PECT (community)')
axes[0,2].set(xlim=(0.5, 2.5), ylim=(0, 6), xlabel= None, ylabel= None)
axes[0,2].set(title='PECT (industry)')
plt.show()
```




    <AxesSubplot:xlabel='management_post_test', ylabel='survey_q5b_score'>






    <AxesSubplot:xlabel='management_post_test', ylabel='survey_q5b_score'>






    <AxesSubplot:xlabel='management_post_test', ylabel='survey_q5b_score'>






    <AxesSubplot:xlabel='management_pre_test', ylabel='survey_q5a_score'>






    <AxesSubplot:xlabel='management_pre_test', ylabel='survey_q5a_score'>






    <AxesSubplot:xlabel='management_pre_test', ylabel='survey_q5a_score'>






    [(0.5, 2.5),
     (0.0, 6.0),
     Text(0.5, 0, ''),
     Text(0, 0.5, 'Perception (knowledge on management after using chatbot)')]






    [(0.5, 2.5),
     (0.0, 6.0),
     Text(0.5, 0, 'Assessment score (knowledge on management after using chatbot)'),
     Text(0, 0.5, '')]






    [(0.5, 2.5), (0.0, 6.0), Text(0.5, 0, ''), Text(0, 0.5, '')]






    [(0.5, 2.5),
     (0.0, 6.0),
     Text(0.5, 0, ''),
     Text(0, 0.5, 'Perception (knowledge on management before using chatbot)')]






    [Text(0.5, 1.0, 'Pre-registration')]






    [(0.5, 2.5),
     (0.0, 6.0),
     Text(0.5, 0, 'Assessment score (knowledge on management before using chatbot)'),
     Text(0, 0.5, '')]






    [Text(0.5, 1.0, 'PECT (community)')]






    [(0.5, 2.5), (0.0, 6.0), Text(0.5, 0, ''), Text(0, 0.5, '')]






    [Text(0.5, 1.0, 'PECT (industry)')]




    
![png](output_44_15.png)
    



```python
#boxplot of knowledge perception differential on the IDENTIFICATION of the factors affecting long-term BPV for the 3 groups

df_prereg_corr['prereg_iden_diff'] = df_prereg_corr['identification_diff_perception']
df_comm_corr['comm_iden_diff'] = df_comm_corr['identification_diff_perception']
df_ind_corr['ind_iden_diff'] = df_ind_corr['identification_diff_perception']

boxplot_df = pd.concat([df_prereg_corr['prereg_iden_diff'], df_comm_corr['comm_iden_diff'], df_ind_corr['ind_iden_diff']], axis=1)
boxplot = boxplot_df.boxplot(patch_artist=True)

boxplot_df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prereg_iden_diff</th>
      <th>comm_iden_diff</th>
      <th>ind_iden_diff</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>34.000000</td>
      <td>26.000000</td>
      <td>23.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.000000</td>
      <td>1.076923</td>
      <td>1.826087</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.015038</td>
      <td>1.163549</td>
      <td>1.192864</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>4.000000</td>
      <td>3.000000</td>
      <td>4.000000</td>
    </tr>
  </tbody>
</table>
</div>




    
![png](output_45_1.png)
    



```python
#Wilcoxon signed-rank test between the pre- and post-learning knowledge perception on the IDENTIFICATION of the factors affecting long-term BPV for the 3 groups

stats.wilcoxon(df_prereg_corr_2['survey_q4b_score'], df_prereg_corr_2['survey_q4a_score'], alternative='greater')
stats.wilcoxon(df_comm_corr_2['survey_q4b_score'], df_comm_corr_2['survey_q4a_score'], alternative='greater')
stats.wilcoxon(df_ind_corr_2['survey_q4b_score'], df_ind_corr_2['survey_q4a_score'], alternative='greater')

#conclusion: statistically significant knowledge perception improvement for all 3 groups
```




    WilcoxonResult(statistic=269.5, pvalue=1.994451352201845e-05)






    WilcoxonResult(statistic=120.0, pvalue=0.0002660027525696246)



    /home/jianyang/my_project_dir/my_env/lib/python3.8/site-packages/scipy/stats/morestats.py:2967: UserWarning: Exact p-value calculation does not work if there are ties. Switching to normal approximation.
      warnings.warn("Exact p-value calculation does not work if there are "





    WilcoxonResult(statistic=190.0, pvalue=5.5159969420047564e-05)




```python
#Kruskal-Wallis test between the knowledge perception differentials on the IDENTIFICATION of the factors affecting long-term BPV

stats.kruskal(df_comm_corr['identification_diff_perception'], df_ind_corr['identification_diff_perception'], df_prereg_corr['identification_diff_perception'])

#conclusion: statistically significant difference in knowledge perception differentials between the 3 groups
```




    KruskalResult(statistic=7.39686983627456, pvalue=0.024762251108910727)




```python
#pairwise analysis (Mann-Whitney U test) between the knowledge perception differentials on the IDENTIFICATION of the factors affecting long-term BPV

#between the PECT (industry) and PECT (community) groups
stats.mannwhitneyu(df_comm_corr['identification_diff_perception'], df_ind_corr['identification_diff_perception'], use_continuity=True, alternative='two-sided')

#between the pre-registration training and PECT (industry) groups
stats.mannwhitneyu(df_prereg_corr['identification_diff_perception'], df_ind_corr['identification_diff_perception'], use_continuity=True, alternative='two-sided')

#between the pre-registration training and PECT (community) groups
stats.mannwhitneyu(df_prereg_corr['identification_diff_perception'], df_comm_corr['identification_diff_perception'], use_continuity=True, alternative='two-sided')

#conclusion: statistically significant difference in knowledge perception differentials between the PECT (industry) and PECT (community) groups, and between the pre-registration training and PECT (industry) groups
```




    MannwhitneyuResult(statistic=196.0, pvalue=0.03381017897166371)






    MannwhitneyuResult(statistic=236.0, pvalue=0.009386438190276528)






    MannwhitneyuResult(statistic=441.0, pvalue=0.9937723710760119)




```python
#boxplot of knowledge perception differential on the MANAGEMENT of the factors affecting long-term BPV for the 3 groups

df_prereg_corr['prereg_manage_diff'] = df_prereg_corr['management_diff_perception']
df_comm_corr['comm_manage_diff'] = df_comm_corr['management_diff_perception']
df_ind_corr['ind_manage_diff'] = df_ind_corr['management_diff_perception']

boxplot_df = pd.concat([df_prereg_corr['prereg_manage_diff'], df_comm_corr['comm_manage_diff'], df_ind_corr['ind_manage_diff']], axis=1)
boxplot = boxplot_df.boxplot(patch_artist=True)

boxplot_df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prereg_manage_diff</th>
      <th>comm_manage_diff</th>
      <th>ind_manage_diff</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>34.000000</td>
      <td>26.000000</td>
      <td>23.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.264706</td>
      <td>1.115385</td>
      <td>2.043478</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.213780</td>
      <td>1.070586</td>
      <td>1.397344</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>4.000000</td>
      <td>3.000000</td>
      <td>4.000000</td>
    </tr>
  </tbody>
</table>
</div>




    
![png](output_49_1.png)
    



```python
#Wilcoxon signed-rank test between the pre- and post-learning knowledge perception on the MANAGEMENT of the factors affecting long-term BPV for the 3 groups

stats.wilcoxon(df_prereg_corr_2['survey_q5b_score'], df_prereg_corr_2['survey_q5a_score'], alternative='greater')
stats.wilcoxon(df_comm_corr_2['survey_q5b_score'], df_comm_corr_2['survey_q5a_score'], alternative='greater')
stats.wilcoxon(df_ind_corr_2['survey_q5b_score'], df_ind_corr_2['survey_q5a_score'], alternative='greater')

#conclusion: statistically significant knowledge perception improvement for all 3 groups
```




    WilcoxonResult(statistic=276.0, pvalue=1.0069560937955258e-05)






    WilcoxonResult(statistic=153.0, pvalue=0.00011014631109049817)



    /home/jianyang/my_project_dir/my_env/lib/python3.8/site-packages/scipy/stats/morestats.py:2967: UserWarning: Exact p-value calculation does not work if there are ties. Switching to normal approximation.
      warnings.warn("Exact p-value calculation does not work if there are "





    WilcoxonResult(statistic=210.0, pvalue=3.8568200545620204e-05)




```python
#Kruskal-Wallis test between the knowledge perception differentials on the MANAGEMENT of the factors affecting long-term BPV

stats.kruskal(df_comm_corr['management_diff_perception'], df_ind_corr['management_diff_perception'], df_prereg_corr['management_diff_perception'])

#conclusion: statistically significant difference in knowledge perception differentials between the 3 groups
```




    KruskalResult(statistic=6.572681059858701, pvalue=0.037390428494239424)




```python
#pairwise analysis (Mann-Whitney U test) between the knowledge perception differentials on the MANAGEMENT of the factors affecting long-term BPV

#between the PECT (industry) and PECT (community) groups
stats.mannwhitneyu(df_comm_corr['management_diff_perception'], df_ind_corr['management_diff_perception'], use_continuity=True, alternative='two-sided')

#between the pre-registration training and PECT (industry) groups
stats.mannwhitneyu(df_prereg_corr['management_diff_perception'], df_ind_corr['management_diff_perception'], use_continuity=True, alternative='two-sided')

#between the pre-registration training and PECT (community) groups
stats.mannwhitneyu(df_prereg_corr['management_diff_perception'], df_comm_corr['management_diff_perception'], use_continuity=True, alternative='two-sided')

#conclusion: statistically significant difference in knowledge perception differentials between the PECT (industry) and PECT (community) groups, and between the pre-registration training and PECT (industry) groups
```




    MannwhitneyuResult(statistic=184.0, pvalue=0.018054923413318227)






    MannwhitneyuResult(statistic=265.0, pvalue=0.035635506072066135)






    MannwhitneyuResult(statistic=466.0, pvalue=0.7146199577906074)




```python
#boxplot of relevance rating of the chatbot for the 3 groups

df_rel = df.filter(items=['objectId', 'user_education', 'survey_q7a'])
survey_q7a_mymap = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}
df_rel = df_rel.applymap(lambda s: survey_q7a_mymap.get(s) if s in survey_q7a_mymap else s)
df_prereg_corr['prereg_relevance'] = df_rel[df_rel['user_education'] == 'pre-registration training'][['survey_q7a']]
df_comm_corr['comm_relevance'] = df_rel[df_rel['user_education'] == 'PECT (community rotation)'][['survey_q7a']]
df_ind_corr['ind_relevance'] = df_rel[df_rel['user_education'] == 'PECT (industry rotation)'][['survey_q7a']]

boxplot_df = pd.concat([df_prereg_corr['prereg_relevance'], df_comm_corr['comm_relevance'], df_ind_corr['ind_relevance']], axis=1)
boxplot = boxplot_df.boxplot(patch_artist=True)
boxplot

boxplot_df.describe()
```




    <AxesSubplot:>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prereg_relevance</th>
      <th>comm_relevance</th>
      <th>ind_relevance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>34.000000</td>
      <td>26.000000</td>
      <td>23.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3.147059</td>
      <td>3.269231</td>
      <td>2.130435</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.857493</td>
      <td>0.874423</td>
      <td>1.140349</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2.000000</td>
      <td>3.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>4.000000</td>
      <td>5.000000</td>
      <td>4.000000</td>
    </tr>
  </tbody>
</table>
</div>




    
![png](output_53_2.png)
    



```python
#Kruskal-Wallis test between the relevance ratings of the chatbot of the 3 groups

stats.kruskal(df_prereg_corr['prereg_relevance'], df_comm_corr['comm_relevance'], df_ind_corr['ind_relevance'])

#conclusion: statistically significant difference in relevance rating of the chatbot between the 3 groups
```




    KruskalResult(statistic=14.071413644342162, pvalue=0.0008798960150665867)




```python
#pairwise analysis (Mann-Whitney U test) between the relevance ratings of the chatbot

#between the PECT (industry) and PECT (community) groups
stats.mannwhitneyu(df_ind_corr['ind_relevance'], df_comm_corr['comm_relevance'], use_continuity=True, alternative='two-sided')

#between the pre-registration training and PECT (industry) groups
stats.mannwhitneyu(df_prereg_corr['prereg_relevance'], df_ind_corr['ind_relevance'], use_continuity=True, alternative='two-sided')

#between the pre-registration training and PECT (community) groups
stats.mannwhitneyu(df_prereg_corr['prereg_relevance'], df_comm_corr['comm_relevance'], use_continuity=True, alternative='two-sided')

#conclusion: statistically significant difference in relevance ratings of the chatbot between the PECT (industry) and PECT (community) groups, and between the pre-registration training and PECT (industry) groups
```




    MannwhitneyuResult(statistic=141.0, pvalue=0.0010458791028786407)






    MannwhitneyuResult(statistic=586.0, pvalue=0.001032127396160797)






    MannwhitneyuResult(statistic=419.5, pvalue=0.7281104999622284)




```python
#create a seperate dataframe for analysis of pre- and post-learning test scores in the respective aspects (IDENTIFICATION and MANAGEMENT) of the factors affecting long-term BPV

df_prereg_corr_3 = df[df['user_education'] == 'pre-registration training'][['identification_diff_test', 'management_diff_test', 'identification_post_test', 'identification_pre_test', 'management_post_test', 'management_pre_test']]
df_comm_corr_3 = df[df['user_education'] == 'PECT (community rotation)'][['identification_diff_test', 'management_diff_test', 'identification_post_test', 'identification_pre_test', 'management_post_test', 'management_pre_test']]
df_ind_corr_3 = df[df['user_education'] == 'PECT (industry rotation)'][['identification_diff_test', 'management_diff_test', 'identification_post_test', 'identification_pre_test', 'management_post_test', 'management_pre_test']]

df_prereg_corr_3.describe()
df_comm_corr_3.describe()
df_ind_corr_3.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>identification_diff_test</th>
      <th>management_diff_test</th>
      <th>identification_post_test</th>
      <th>identification_pre_test</th>
      <th>management_post_test</th>
      <th>management_pre_test</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>34.000000</td>
      <td>34.000000</td>
      <td>34.000000</td>
      <td>34.000000</td>
      <td>34.000000</td>
      <td>34.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.338235</td>
      <td>0.161765</td>
      <td>1.661765</td>
      <td>1.323529</td>
      <td>1.715686</td>
      <td>1.553922</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.455947</td>
      <td>0.417394</td>
      <td>0.264274</td>
      <td>0.430216</td>
      <td>0.297377</td>
      <td>0.332627</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.833333</td>
      <td>-0.666667</td>
      <td>1.166667</td>
      <td>0.666667</td>
      <td>1.000000</td>
      <td>0.833333</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.041667</td>
      <td>0.000000</td>
      <td>1.500000</td>
      <td>1.000000</td>
      <td>1.416667</td>
      <td>1.500000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.333333</td>
      <td>0.166667</td>
      <td>1.666667</td>
      <td>1.333333</td>
      <td>1.666667</td>
      <td>1.666667</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.666667</td>
      <td>0.458333</td>
      <td>2.000000</td>
      <td>1.666667</td>
      <td>2.000000</td>
      <td>1.666667</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>identification_diff_test</th>
      <th>management_diff_test</th>
      <th>identification_post_test</th>
      <th>identification_pre_test</th>
      <th>management_post_test</th>
      <th>management_pre_test</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>26.000000</td>
      <td>26.000000</td>
      <td>26.000000</td>
      <td>26.000000</td>
      <td>26.000000</td>
      <td>26.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.429487</td>
      <td>0.294872</td>
      <td>1.621795</td>
      <td>1.192308</td>
      <td>1.628205</td>
      <td>1.333333</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.429918</td>
      <td>0.445490</td>
      <td>0.360733</td>
      <td>0.342190</td>
      <td>0.287934</td>
      <td>0.312694</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.500000</td>
      <td>-1.000000</td>
      <td>0.666667</td>
      <td>0.666667</td>
      <td>1.000000</td>
      <td>0.833333</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.333333</td>
      <td>0.041667</td>
      <td>1.375000</td>
      <td>1.000000</td>
      <td>1.333333</td>
      <td>1.166667</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.416667</td>
      <td>0.333333</td>
      <td>1.666667</td>
      <td>1.333333</td>
      <td>1.666667</td>
      <td>1.166667</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.666667</td>
      <td>0.500000</td>
      <td>2.000000</td>
      <td>1.333333</td>
      <td>1.916667</td>
      <td>1.500000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.333333</td>
      <td>0.833333</td>
      <td>2.000000</td>
      <td>1.666667</td>
      <td>2.000000</td>
      <td>2.000000</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>identification_diff_test</th>
      <th>management_diff_test</th>
      <th>identification_post_test</th>
      <th>identification_pre_test</th>
      <th>management_post_test</th>
      <th>management_pre_test</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>23.000000</td>
      <td>23.000000</td>
      <td>23.000000</td>
      <td>23.000000</td>
      <td>23.000000</td>
      <td>23.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.420290</td>
      <td>0.282609</td>
      <td>1.608696</td>
      <td>1.188406</td>
      <td>1.623188</td>
      <td>1.340580</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.514609</td>
      <td>0.370758</td>
      <td>0.320230</td>
      <td>0.281161</td>
      <td>0.231472</td>
      <td>0.281941</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.833333</td>
      <td>-0.333333</td>
      <td>0.833333</td>
      <td>0.666667</td>
      <td>1.333333</td>
      <td>0.833333</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.166667</td>
      <td>0.000000</td>
      <td>1.500000</td>
      <td>1.000000</td>
      <td>1.333333</td>
      <td>1.166667</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.333333</td>
      <td>0.166667</td>
      <td>1.666667</td>
      <td>1.333333</td>
      <td>1.666667</td>
      <td>1.333333</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.833333</td>
      <td>0.500000</td>
      <td>1.833333</td>
      <td>1.333333</td>
      <td>1.666667</td>
      <td>1.583333</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.333333</td>
      <td>1.166667</td>
      <td>2.000000</td>
      <td>1.666667</td>
      <td>2.000000</td>
      <td>1.666667</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Wilcoxon signed-rank test between the pre- and post-learning test scores on the IDENTIFICATION of the factors affecting long-term BPV for the 3 groups

stats.wilcoxon(df_prereg_corr_3['identification_post_test'], df_prereg_corr_3['identification_pre_test'], alternative='greater')
stats.wilcoxon(df_comm_corr_3['identification_post_test'], df_comm_corr_3['identification_pre_test'], alternative='greater')
stats.wilcoxon(df_ind_corr_3['identification_post_test'], df_ind_corr_3['identification_pre_test'], alternative='greater')

#conclusion: statistically significant test score improvement for all 3 groups
```




    WilcoxonResult(statistic=448.5, pvalue=0.0002732790568179283)






    WilcoxonResult(statistic=275.0, pvalue=0.00017129942829387183)



    /home/jianyang/my_project_dir/my_env/lib/python3.8/site-packages/scipy/stats/morestats.py:2967: UserWarning: Exact p-value calculation does not work if there are ties. Switching to normal approximation.
      warnings.warn("Exact p-value calculation does not work if there are "





    WilcoxonResult(statistic=228.0, pvalue=0.00046517311518495694)




```python
#Kruskal-Wallis test between the score differentials (in IDENTIFICATION of the factors affecting long-term BPV) of the 3 groups

stats.kruskal(df_prereg_corr_3['identification_diff_test'], df_comm_corr_3['identification_diff_test'], df_ind_corr_3['identification_diff_test'])

#conclusion: no statistically signficant difference in score differential between the 3 groups
```




    KruskalResult(statistic=0.4425441630279985, pvalue=0.801498577674214)




```python
#Wilcoxon signed-rank test between the pre- and post-learning test scores on the MANAGEMENT of the factors affecting long-term BPV for the 3 groups

stats.wilcoxon(df_prereg_corr_3['management_post_test'], df_prereg_corr_3['management_pre_test'], alternative='greater')
stats.wilcoxon(df_comm_corr_3['management_post_test'], df_comm_corr_3['management_pre_test'], alternative='greater')
stats.wilcoxon(df_ind_corr_3['management_post_test'], df_ind_corr_3['management_pre_test'], alternative='greater')

#conclusion: statistically significant test score improvement for all 3 groups
```




    WilcoxonResult(statistic=258.0, pvalue=0.01780482996649086)






    WilcoxonResult(statistic=249.5, pvalue=0.002149040734569897)






    WilcoxonResult(statistic=168.0, pvalue=0.00160156242704644)




```python
#Kruskal-Wallis test between the score differentials (in MANAGEMENT of the factors affecting long-term BPV) of the 3 groups

stats.kruskal(df_prereg_corr_3['management_diff_test'], df_comm_corr_3['management_diff_test'], df_ind_corr_3['management_diff_test'])

#conclusion: no statistically signficant difference in score differential between the 3 groups
```




    KruskalResult(statistic=2.3875830340637294, pvalue=0.30306998788335887)




```python
#convert 5-point likert scale in specific survey questions into binary scale (i.e. Good, Not Good)

df_crosstab = df.filter(items=['objectId', 'user_education', 'survey_q4a', 'survey_q4b', 'survey_q5a', 'survey_q5b'])
survey_mymap = {'a': 'Good', 'b': 'Good', 'c': 'Good', 'd': 'Not Good', 'e': 'Not Good'}
df_crosstab = df_crosstab.applymap(lambda s: survey_mymap.get(s) if s in survey_mymap else s)
df_prereg_crosstab = df_crosstab[df_crosstab['user_education'] == 'pre-registration training']
df_comm_crosstab = df_crosstab[df_crosstab['user_education'] == 'PECT (community rotation)']
df_ind_crosstab = df_crosstab[df_crosstab['user_education'] == 'PECT (industry rotation)']
```


```python
#survey q4a/b: What best describes your level of knowledge on identifying the factors affecting long-term BPV
#BEFORE/AFTER using the chatbot?

#in number of users

prereg_crosstab_IDE = pd.crosstab(df_prereg_crosstab['survey_q4a'], df_prereg_crosstab['survey_q4b'], margins = False) 
prereg_crosstab_IDE
comm_crosstab_IDE = pd.crosstab(df_comm_crosstab['survey_q4a'], df_comm_crosstab['survey_q4b'], margins = False) 
comm_crosstab_IDE
ind_crosstab_IDE = pd.crosstab(df_ind_crosstab['survey_q4a'], df_ind_crosstab['survey_q4b'], margins = False) 
ind_crosstab_IDE
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q4b</th>
      <th>Good</th>
      <th>Not Good</th>
    </tr>
    <tr>
      <th>survey_q4a</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Good</th>
      <td>19</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Not Good</th>
      <td>13</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q4b</th>
      <th>Good</th>
    </tr>
    <tr>
      <th>survey_q4a</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Good</th>
      <td>18</td>
    </tr>
    <tr>
      <th>Not Good</th>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q4b</th>
      <th>Good</th>
    </tr>
    <tr>
      <th>survey_q4a</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Good</th>
      <td>11</td>
    </tr>
    <tr>
      <th>Not Good</th>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python
#survey q5a/b: What best describes your level of knowledge on managing the factors affecting long-term BPV, 
#BEFORE/AFTER using the chatbot?

#in number of users

prereg_crosstab_MAN = pd.crosstab(df_prereg_crosstab['survey_q5a'], df_prereg_crosstab['survey_q5b'], margins = False) 
prereg_crosstab_MAN
comm_crosstab_MAN = pd.crosstab(df_comm_crosstab['survey_q5a'], df_comm_crosstab['survey_q5b'], margins = False) 
comm_crosstab_MAN
ind_crosstab_MAN = pd.crosstab(df_ind_crosstab['survey_q5a'], df_ind_crosstab['survey_q5b'], margins = False) 
ind_crosstab_MAN
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q5b</th>
      <th>Good</th>
    </tr>
    <tr>
      <th>survey_q5a</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Good</th>
      <td>21</td>
    </tr>
    <tr>
      <th>Not Good</th>
      <td>13</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q5b</th>
      <th>Good</th>
    </tr>
    <tr>
      <th>survey_q5a</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Good</th>
      <td>19</td>
    </tr>
    <tr>
      <th>Not Good</th>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>survey_q5b</th>
      <th>Good</th>
    </tr>
    <tr>
      <th>survey_q5a</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Good</th>
      <td>12</td>
    </tr>
    <tr>
      <th>Not Good</th>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
#McNemar's test on the change in perceived knowledge on the IDENTIFICATION of the factors affecting long-term BPV after using the chatbot

print(mcnemar(prereg_crosstab_IDE, exact=True, correction=True))
print(mcnemar(comm_crosstab_IDE, exact=True, correction=True))
print(mcnemar(ind_crosstab_IDE, exact=True, correction=True))

#conclusion: statistically significant change in perceived knowledge for all 3 groups
```

    pvalue      0.000244140625
    statistic   0.0
    pvalue      0.0078125
    statistic   0.0
    pvalue      0.00048828125
    statistic   0.0



```python
#McNemar's test on the change in perceived knowledge on the MANAGEMENT of the factors affecting long-term BPV after using the chatbot

print(mcnemar(prereg_crosstab_MAN, exact=True, correction=True))
print(mcnemar(comm_crosstab_MAN, exact=True, correction=True))
print(mcnemar(ind_crosstab_MAN, exact=True, correction=True))

#conclusion: statistically significant change in perceived knowledge for all 3 groups
```

    pvalue      0.000244140625
    statistic   0.0
    pvalue      0.015625
    statistic   0.0
    pvalue      0.0009765625
    statistic   0.0



```python
#in-depth analysis into users from the pre-registration training group whose test scores deteriorated after using the chatbot

prereg_list = df_pre_reg.index[df_pre_reg['prereg_score_diff'] < 0].tolist()
filter_df  = df[df.index.isin(prereg_list)]
prereg_diff = filter_df[['identification_diff_test', 'management_diff_test', 'identification_post_test', 'identification_pre_test', 'management_post_test', 'management_pre_test']]
prereg_diff
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>identification_diff_test</th>
      <th>management_diff_test</th>
      <th>identification_post_test</th>
      <th>identification_pre_test</th>
      <th>management_post_test</th>
      <th>management_pre_test</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>-0.500000</td>
      <td>0.166667</td>
      <td>1.500000</td>
      <td>2.000000</td>
      <td>1.666667</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>17</th>
      <td>-0.333333</td>
      <td>-0.333333</td>
      <td>1.666667</td>
      <td>2.000000</td>
      <td>1.666667</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>35</th>
      <td>0.333333</td>
      <td>-0.500000</td>
      <td>2.000000</td>
      <td>1.666667</td>
      <td>1.000000</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>36</th>
      <td>0.333333</td>
      <td>-0.666667</td>
      <td>1.666667</td>
      <td>1.333333</td>
      <td>1.333333</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>57</th>
      <td>-0.333333</td>
      <td>-0.333333</td>
      <td>1.666667</td>
      <td>2.000000</td>
      <td>1.666667</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>70</th>
      <td>-0.833333</td>
      <td>0.000000</td>
      <td>1.166667</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#in-depth analysis into users from the PECT (community) group whose test scores deteriorated after using the chatbot

comm_list = df_comm.index[df_comm['comm_score_diff'] < 0].tolist()
comm_filter_df  = df[df.index.isin(comm_list)]
comm_diff = comm_filter_df[['identification_diff_test', 'management_diff_test', 'identification_post_test', 'identification_pre_test', 'management_post_test', 'management_pre_test']]
comm_diff
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>identification_diff_test</th>
      <th>management_diff_test</th>
      <th>identification_post_test</th>
      <th>identification_pre_test</th>
      <th>management_post_test</th>
      <th>management_pre_test</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>16</th>
      <td>-0.500000</td>
      <td>-0.166667</td>
      <td>1.166667</td>
      <td>1.666667</td>
      <td>1.333333</td>
      <td>1.500000</td>
    </tr>
    <tr>
      <th>23</th>
      <td>0.000000</td>
      <td>0.500000</td>
      <td>0.666667</td>
      <td>0.666667</td>
      <td>1.666667</td>
      <td>1.166667</td>
    </tr>
    <tr>
      <th>46</th>
      <td>0.333333</td>
      <td>-1.000000</td>
      <td>1.666667</td>
      <td>1.333333</td>
      <td>1.000000</td>
      <td>2.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#in-depth analysis into users from the PECT (industry) group whose test scores deteriorated after using the chatbot

ind_list = df_ind.index[df_ind['ind_score_diff'] < 0].tolist()
ind_filter_df  = df[df.index.isin(ind_list)]
ind_diff = ind_filter_df[['identification_diff_test', 'management_diff_test', 'identification_post_test', 'identification_pre_test', 'management_post_test', 'management_pre_test']]
ind_diff
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>identification_diff_test</th>
      <th>management_diff_test</th>
      <th>identification_post_test</th>
      <th>identification_pre_test</th>
      <th>management_post_test</th>
      <th>management_pre_test</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>21</th>
      <td>-0.166667</td>
      <td>0.000000</td>
      <td>1.166667</td>
      <td>1.333333</td>
      <td>1.666667</td>
      <td>1.666667</td>
    </tr>
    <tr>
      <th>39</th>
      <td>-0.166667</td>
      <td>-0.166667</td>
      <td>1.166667</td>
      <td>1.333333</td>
      <td>1.333333</td>
      <td>1.500000</td>
    </tr>
    <tr>
      <th>42</th>
      <td>-0.833333</td>
      <td>0.166667</td>
      <td>0.833333</td>
      <td>1.666667</td>
      <td>1.666667</td>
      <td>1.500000</td>
    </tr>
    <tr>
      <th>71</th>
      <td>-0.166667</td>
      <td>-0.166667</td>
      <td>1.166667</td>
      <td>1.333333</td>
      <td>1.333333</td>
      <td>1.500000</td>
    </tr>
  </tbody>
</table>
</div>


