# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 08:23:08 2018

@author: Mohan
"""

import pandas as pd

df=pd.read_csv('E:\Python/OP.csv')

   # last n columns Delete
df.drop(df.columns[[0]], axis=1, inplace=True)

   # last n columns Delete
df.drop(df.columns[[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12]], axis=1, inplace=True)

df.to_csv('E:\Python/OP_out1.csv',mode='a', sep=',')

#Delete last n rows from  frame
df.drop(df.head(5).index,inplace=True) 

df=df.drop(df.index[[1]])


df.to_csv('E:\Python/OP_out2.csv',mode='a', sep=',')

# Get Category Names
df2=df[df.columns[0:2]]
df1=df[df.columns[0:2]]

df1.columns = ["Category","Subcategory" ]

df1=df1.drop(df1.index[0])

df1.iloc[0]['Category']
df1.iloc[1]['Category']

df1.iloc[0]['Subcategory']
df1.iloc[1]['Subcategory']

print(df1.iloc[1]['Subcategory'])

how1= df2.fillna(df1.iloc[0]['Subcategory'])



df1.insert(0, 'Year', df1.iloc[0]['Subcategory'])







----------------------

df1.loc([6], ['Category'])

df1.loc([0],  ['Category'])
'Belgium'
 df1.at([0],  ['Category'])

df1.iloc[[0],[0]]

print (df1.loc[[0],['Category'])



df1=pd.read_csv('E:\Python/OP_out2.csv')

df1.columns = ["Dummy","TEST"]

df_c1=df.iloc[1:,2].head(1)
df_c1.drop(df_c1.index[[-1]],inplace=True) 

df.ix[7,'Unnamed: 1']

print (df_c1)