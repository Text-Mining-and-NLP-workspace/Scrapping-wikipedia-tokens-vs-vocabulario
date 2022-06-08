# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 12:21:13 2022

@author: amuralles
"""
import os
import re
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

sns.set_theme(style="darkgrid")
filename='token_VS_vocabulary.json'
with open(filename, 'r') as f:
    data=pd.DataFrame(json.load(f))

token_lst=[]
token=[]
vocabulary=[]
for text in data.iloc[0:250,0]:
    corpus=''.join(text)       
    token_lst+=re.split('\W+',corpus.lower())
    vocabulary_lst=Counter(token_lst).most_common()    
    token.append(len(token_lst))
    vocabulary.append(len(vocabulary_lst))


df=pd.DataFrame({'token':token,'vocabulary':vocabulary})
df['estimated']=np.sqrt(df.token)
coef=(df['vocabulary']/df['estimated']).mean()    
df['Ley de Heaps '+str(int(round(coef,0)))+'*N^1/2']=int(round(coef,0))*np.sqrt(df.token)

sns.relplot(x="token", y="value", kind="line", hue='variable',data=df.melt(id_vars =['token'], value_vars =['vocabulary', 'Ley de Heaps '+str(int(round(coef,0)))+'*N^1/2']))       
plt.savefig(os.getcwd()+'/token_VS_vocabulary_plot.png', dpi=300)
