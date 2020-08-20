#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:44:11 2020

@author: hwangsujeong
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


# =============================================================================
df3=pd.read_csv("C:/Users/김지은/Desktop/FBA_project/try_pca1.csv", encoding="UTF-8")
# =============================================================================

df3["Unnamed: 0"]=df3["Unnamed: 0"].map('{:06d}'.format)
df3["Unnamed: 0"]=df3["Unnamed: 0"].astype(str)

df3.isna().sum()

df3=df3.set_index(['index', 'Unnamed: 1']).sort_index()

#regularization
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df3[:] = scaler.fit_transform(df3[:])


df3_=pd.DataFrame(df3.index)

df3=df3.dropna()
#StandardScaler
pca = PCA(n_components=3)
principalComponents = pca.fit_transform(df3)
principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2','principal component 3'])
finalDataFrame = pd.concat([principalDf, df3_], axis=1)
pca.explained_variance_ratio_
sum(pca.explained_variance_ratio_)

#visualization
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 Component PCA', fontsize = 20)
y = df3_.loc[:,].values
labels = []
yList = y.tolist()
for label in 1:yList:
  if Index[0] not in labels:
    labels.append(Index[0])

targets = ['ROA', 'CFO', 'd_ROA', 'CFO-ROA', 'd_Debt', 'd_Liquid', 'd_Equiss', 'Margin']
finalDataFrame.rename(columns={0:'Index'}, inplace=True)
colors = ["#7fc97f","#beaed4","#fdc086","#ffff99","#386cb0","#f0027f","","#666666"]
for targets, color in zip(targets, colors):
    indicesToKeep = finalDataFrame['Index'] == Index
    ax.scatter(finalDataFrame.loc[indicesToKeep, 'principal component 1']
               , finalDataFrame.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 30)
    
ax.legend(Index)
ax.grid()

#select
plt.plot
plt.plot(np.cumsum(pca.explained_variance_ratio_))
         ,xlabel="number of components")
plt.xlabel("number of components")
plt.ylabel("cumulative explained variace")
#visualization2
import matplotlib.pyplot as plt
plt.scatter(principalComponents[:,0],principalComponents[:,1])
import seaborn as sns
sns.scatterplot(data=import seaborn as sns
sns.scatterplot(data=principalComponents,x='principal component 1',y='principal component 2',hue='diagnosis')
sns.scatterplot(data=principalComponents,x='PC1',y='PC2',hue='diagnosis')

#t-sne
import time
from sklearn.manifold import TSNE

n_sne = 100



time_start = time.time()
tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
tsne_results = tsne.fit_transform(df3.loc[rndperm[:n_sne],feat_cols].values)

df3.iloc[2].unique
출처: https://skyeong.net/186 [금융 데이터를 분석하는 뇌과학자]

fulls=pd.read_csv("C:/Users/김지은/Desktop/FBA_project/Full_Signal.csv")
fulls=fulls.drop(['index','Unnamed: 1'], axis=1)
x = fulls.loc[:,nameList[1:]].values
y = fulls.loc[:,['F-Score']].values
pca = PCA(n_components = 2)
principalComponents = pca.fit_transform(fulls)
principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])
finalDataFrame = pd.concat([principalDf, fulls[['F-Score']]], axis=1)
 labels = []
yList = y.tolist()
for label in yList:
  if label[0] not in labels:
    labels.append(label[0])
    
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 Component PCA', fontsize = 20)

colors = ["#7fc97f","#beaed4","#fdc086","#ffff99","#386cb0","#f0027f","#666666"]
for label, color in zip(labels, colors):
  indicesToKeep = finalDataFrame['F-Score'] == label
  ax.scatter(finalDataFrame.loc[indicesToKeep, 'principal component 1']
               , finalDataFrame.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 30)
  plt.show()

ax.legend(labels)
ax.grid()

plt.show()
ax.show()
기존에 있던 label 과 합쳐줍니다.
