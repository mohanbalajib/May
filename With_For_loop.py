# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 19:47:55 2018

@author: Mohan
"""

import pandas as pd

# Read Input file
df=pd.read_csv('E:\Python\seven/input.csv',skiprows=range(1, 5))

# last n columns Delete
df.drop(df.columns[[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12]], axis=1, inplace=True)

# Drop 2nd row
df=df.drop(df.index[[1]])

# Write output after skiping first 5 rows
df.to_csv('E:\Python\seven/OP_out1.csv',mode='a', sep=',')

# Transpose the Data frame 1
df_T=pd.read_csv('E:\Python\seven/OP_out1.csv', index_col=0, header=None).T

# Write output to outfile
df_T.to_csv('E:\Python\seven/OP_out6.csv',mode='a', sep=',')

#to remove the first 2 rows
df_T=df_T.tail(-2)

# Add new column Year
df_T.insert(0, 'Year', '2018')

# Assign the Header
df_T.columns = ["Year","Dummy","Stations","Revenue","Rev5","Rev6","Rev7","Rev8","Rev9","Rev10","Rev11","Rev12","Rev13","Rev14","Rev15","Rev16","Rev17","Rev18","Rev19","Rev20", "Rev21"]

# Assign 0 to missing values
#df_T["Stations"].fillna(0, inplace = True) 
df_T["Revenue"].fillna(0, inplace = True) 
df_T["Rev5"].fillna(0, inplace = True) 
df_T["Rev6"].fillna(0, inplace = True) 
df_T["Rev7"].fillna(0, inplace = True) 
df_T["Rev8"].fillna(0, inplace = True) 
df_T["Rev9"].fillna(0, inplace = True) 
df_T["Rev10"].fillna(0, inplace = True) 
df_T["Rev11"].fillna(0, inplace = True) 
df_T["Rev12"].fillna(0, inplace = True) 
df_T["Rev13"].fillna(0, inplace = True) 
df_T["Rev14"].fillna(0, inplace = True)
df_T["Rev15"].fillna(0, inplace = True) 
df_T["Rev16"].fillna(0, inplace = True) 
df_T["Rev17"].fillna(0, inplace = True) 
df_T["Rev18"].fillna(0, inplace = True) 
df_T["Rev19"].fillna(0, inplace = True) 
df_T["Rev20"].fillna(0, inplace = True) 
df_T["Rev21"].fillna(0, inplace = True) 

#Write the output after replacing the zeros in place of nulls
df_T.to_csv('E:\Python\seven/OP_out7.csv',mode='a', sep=',')

# Get Category Names
df1=df[df.columns[0:2]]

# Assign the Header
df1.columns = ["Category","Subcategory" ]

#to remove the first 2 rows
df1=df1.tail(-1)

# Write output Categery and Subcategory Data freame
df1.to_csv('E:\Python\seven/OP_out2.csv',mode='a', sep=',')

# Write fist row to out put file (Stations row)
df[0:1].to_csv('E:\Python\seven/OP_out3.csv', mode='a', sep=',')

# Transpose the Statios row
df2=pd.read_csv('E:\Python\seven/OP_out3.csv', sep=',').T

# Write the data
df2.to_csv('E:\Python\seven/OP_out4.csv', sep=',')

# Assign Header as Stations
df2.columns = ["Stations" ]

# Write output Categery and Subcategory Data freame
df2.to_csv('E:\Python\seven/OP_out5.csv',mode='a', sep=',')

# Get all station names
df2.iloc[3]['Stations'] 
df2.iloc[15]['Stations']
df2.iloc[27]['Stations']
df2.iloc[39]['Stations'] 
df2.iloc[51]['Stations']
df2.iloc[63]['Stations']
df2.iloc[75]['Stations'] 
df2.iloc[87]['Stations']
df2.iloc[99]['Stations']
df2.iloc[111]['Stations'] 
df2.iloc[123]['Stations']
df2.iloc[135]['Stations']
df2.iloc[147]['Stations'] 
df2.iloc[159]['Stations']
df2.iloc[171]['Stations']
df2.iloc[183]['Stations']
df2.iloc[195]['Stations']
df2.iloc[207]['Stations'] 
df2.iloc[219]['Stations'] 
df2.iloc[231]['Stations']  
df2.iloc[243]['Stations'] 
df2.iloc[255]['Stations'] 
df2.iloc[267]['Stations']
df2.iloc[279]['Stations'] 
df2.iloc[291]['Stations']  
df2.iloc[303]['Stations'] 
df2.iloc[315]['Stations'] 
df2.iloc[327]['Stations'] 



# Create Multiple Data Frames based on Stations
s_df1=(df_T[0:12])
s_df2=(df_T[12:24])
s_df3=(df_T[24:36])
s_df4=(df_T[36:48])
s_df5=(df_T[48:60])
s_df6=(df_T[60:72])
s_df7=(df_T[72:84])
s_df8=(df_T[84:96])
s_df9=(df_T[96:108])
s_df10=(df_T[108:120])
s_df11=(df_T[120:132])
s_df12=(df_T[132:144])
s_df13=(df_T[144:156])
s_df14=(df_T[156:168])
s_df15=(df_T[168:180])
s_df16=(df_T[180:192])
s_df17=(df_T[192:204])
s_df18=(df_T[204:216])
s_df19=(df_T[216:228])
s_df20=(df_T[228:240])
s_df21=(df_T[240:252])
s_df22=(df_T[252:264])
s_df23=(df_T[264:276])
s_df24=(df_T[276:288])
s_df25=(df_T[288:300])
s_df26=(df_T[300:312])
s_df27=(df_T[312:324])
s_df28=(df_T[324:336])

#Fill Stations 
sf1=s_df1.fillna(df2.iloc[3]['Stations'])
sf2=s_df2.fillna(df2.iloc[15]['Stations'])
sf3=s_df3.fillna(df2.iloc[27]['Stations'])
sf4=s_df4.fillna(df2.iloc[39]['Stations'])
sf5=s_df5.fillna(df2.iloc[51]['Stations'])
sf6=s_df6.fillna(df2.iloc[63]['Stations'])
sf7=s_df7.fillna(df2.iloc[75]['Stations'])
sf8=s_df8.fillna(df2.iloc[87]['Stations'])
sf9=s_df9.fillna(df2.iloc[99]['Stations'])
sf10=s_df10.fillna(df2.iloc[111]['Stations'])
sf11=s_df11.fillna(df2.iloc[123]['Stations'])
sf12=s_df12.fillna(df2.iloc[135]['Stations'])
sf13=s_df13.fillna(df2.iloc[147]['Stations'])
sf14=s_df14.fillna(df2.iloc[159]['Stations'])
sf15=s_df15.fillna(df2.iloc[171]['Stations'])
sf16=s_df16.fillna(df2.iloc[183]['Stations'])
sf17=s_df17.fillna(df2.iloc[195]['Stations'])
sf18=s_df18.fillna(df2.iloc[207]['Stations'])
sf19=s_df19.fillna(df2.iloc[219]['Stations'])
sf20=s_df20.fillna(df2.iloc[231]['Stations'])
sf21=s_df21.fillna(df2.iloc[243]['Stations'])
sf22=s_df22.fillna(df2.iloc[255]['Stations'])
sf23=s_df23.fillna(df2.iloc[267]['Stations'])
sf24=s_df24.fillna(df2.iloc[279]['Stations'])
sf25=s_df25.fillna(df2.iloc[291]['Stations'])
sf26=s_df26.fillna(df2.iloc[303]['Stations'])
sf27=s_df27.fillna(df2.iloc[315]['Stations'])
sf28=s_df28.fillna(df2.iloc[327]['Stations'])



#Assign Month to data frames
sf1.insert(0, 'Month',range(1, 1 + len(sf1)))
sf2.insert(0, 'Month',range(1, 1 + len(sf2)))
sf3.insert(0, 'Month',range(1, 1 + len(sf3)))
sf4.insert(0, 'Month',range(1, 1 + len(sf4)))
sf5.insert(0, 'Month',range(1, 1 + len(sf5)))
sf6.insert(0, 'Month',range(1, 1 + len(sf6)))
sf7.insert(0, 'Month',range(1, 1 + len(sf7)))
sf8.insert(0, 'Month',range(1, 1 + len(sf8)))
sf9.insert(0, 'Month',range(1, 1 + len(sf9)))
sf10.insert(0, 'Month',range(1, 1 + len(sf10)))
sf11.insert(0, 'Month',range(1, 1 + len(sf11)))
sf12.insert(0, 'Month',range(1, 1 + len(sf12)))
sf13.insert(0, 'Month',range(1, 1 + len(sf13)))
sf14.insert(0, 'Month',range(1, 1 + len(sf14)))
sf15.insert(0, 'Month',range(1, 1 + len(sf15)))
sf16.insert(0, 'Month',range(1, 1 + len(sf16)))
sf17.insert(0, 'Month',range(1, 1 + len(sf17)))
sf18.insert(0, 'Month',range(1, 1 + len(sf18)))
sf19.insert(0, 'Month',range(1, 1 + len(sf19)))
sf20.insert(0, 'Month',range(1, 1 + len(sf20)))
sf21.insert(0, 'Month',range(1, 1 + len(sf21)))
sf22.insert(0, 'Month',range(1, 1 + len(sf22)))
sf23.insert(0, 'Month',range(1, 1 + len(sf23)))
sf24.insert(0, 'Month',range(1, 1 + len(sf24)))
sf25.insert(0, 'Month',range(1, 1 + len(sf25)))
sf26.insert(0, 'Month',range(1, 1 + len(sf26)))
sf27.insert(0, 'Month',range(1, 1 + len(sf27)))
sf28.insert(0, 'Month',range(1, 1 + len(sf28)))



#Get the cagegory Names
df1.iloc[0]['Category']
df1.iloc[1]['Category']
df1.iloc[2]['Category']
df1.iloc[3]['Category']
df1.iloc[4]['Category']
df1.iloc[5]['Category']
df1.iloc[6]['Category']
df1.iloc[7]['Category']
df1.iloc[8]['Category']
df1.iloc[9]['Category']
df1.iloc[10]['Category']
df1.iloc[11]['Category']
df1.iloc[12]['Category']
df1.iloc[13]['Category']
df1.iloc[14]['Category']
df1.iloc[15]['Category']
df1.iloc[16]['Category']
df1.iloc[17]['Category']

print df1.rsplit(':', 1)[0] 

# Now of rows count
t_rows=df1.shape[0]
t_columns = df1.shape[1]  # gives number of col count
i=0
for row in df1.iterrows():
  df1.iloc[i]['Category']
  i=i+1
# Category dispaly
row1 = next(df1.iterrows())[1][0]

#Subcategory Display
row2 = next(df1.iterrows())[1][1]

# Category dispaly
row2 = next(df1.iterrows())[1][2]

#Subcategory Display
row2 = next(df1.iterrows())[1][1]


# Get the Sub Category Names
df1.iloc[0]['Subcategory']
df1.iloc[1]['Subcategory']
df1.iloc[2]['Subcategory']
df1.iloc[3]['Subcategory']
df1.iloc[4]['Subcategory']
df1.iloc[5]['Subcategory']
df1.iloc[6]['Subcategory']
df1.iloc[7]['Subcategory']
df1.iloc[8]['Subcategory']
df1.iloc[9]['Subcategory']
df1.iloc[10]['Subcategory']
df1.iloc[11]['Subcategory']
df1.iloc[12]['Subcategory']
df1.iloc[13]['Subcategory']
df1.iloc[14]['Subcategory']
df1.iloc[15]['Subcategory']
df1.iloc[16]['Subcategory']
df1.iloc[17]['Subcategory']

#Insert into data frame
sf1.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf1.insert(0,'Category',df1.iloc[0]['Category'])
sf2.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf2.insert(0,'Category',df1.iloc[0]['Category'])
sf3.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf3.insert(0,'Category',df1.iloc[0]['Category'])
sf4.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf4.insert(0,'Category',df1.iloc[0]['Category'])
sf5.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf5.insert(0,'Category',df1.iloc[0]['Category'])
sf6.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf6.insert(0,'Category',df1.iloc[0]['Category'])
sf7.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf7.insert(0,'Category',df1.iloc[0]['Category'])
sf8.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf8.insert(0,'Category',df1.iloc[0]['Category'])
sf9.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf9.insert(0,'Category',df1.iloc[0]['Category'])
sf10.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf10.insert(0,'Category',df1.iloc[0]['Category'])
sf11.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf11.insert(0,'Category',df1.iloc[0]['Category'])
sf12.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf12.insert(0,'Category',df1.iloc[0]['Category'])
sf13.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf13.insert(0,'Category',df1.iloc[0]['Category'])
sf14.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf14.insert(0,'Category',df1.iloc[0]['Category'])
sf15.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf15.insert(0,'Category',df1.iloc[0]['Category'])
sf16.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf16.insert(0,'Category',df1.iloc[0]['Category'])
sf17.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf17.insert(0,'Category',df1.iloc[0]['Category'])
sf18.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf18.insert(0,'Category',df1.iloc[0]['Category'])
sf19.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf19.insert(0,'Category',df1.iloc[0]['Category'])
sf20.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf20.insert(0,'Category',df1.iloc[0]['Category'])
sf21.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf21.insert(0,'Category',df1.iloc[0]['Category'])
sf22.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf22.insert(0,'Category',df1.iloc[0]['Category'])
sf23.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf23.insert(0,'Category',df1.iloc[0]['Category'])
sf24.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf24.insert(0,'Category',df1.iloc[0]['Category'])
sf25.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf25.insert(0,'Category',df1.iloc[0]['Category'])
sf26.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf26.insert(0,'Category',df1.iloc[0]['Category'])
sf27.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf27.insert(0,'Category',df1.iloc[0]['Category'])
sf28.insert(0,'Subcategory',df1.iloc[0]['Subcategory'])
sf28.insert(0,'Category',df1.iloc[0]['Category'])


# Yet to write
sf1.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',')
sf2.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf3.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf4.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf5.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf6.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf7.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf8.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf9.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf10.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf11.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf12.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf13.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf14.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf15.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf16.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf17.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf18.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf19.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf20.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf21.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf22.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf23.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf24.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf25.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf26.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf27.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)
sf28.to_csv('E:\Python\seven/OP_out8.csv',mode='a', sep=',',header=None)


# Read final output
df_f_i=pd.read_csv('E:\Python\seven/OP_out8.csv')

# Drop Dummy column and into another output file
df_f_i.drop(columns=['Dummy']).to_csv('E:\Python\seven/OP_out9.csv',mode='a', sep=',')

#Read the file
df_i=pd.read_csv('E:\Python\seven/OP_out9.csv')

# Create Date freames based on Revenue 
df_f1=df_i.loc[:,['Category','Subcategory','Year','Month','Stations','Revenue']]
#df_f2=df_i.loc[:,['Category','Subcategory','Year','Month','Stations','Rev2']]

df_c2=df_i.loc[:,['Year','Month','Stations','Rev5']]
df_c3=df_i.loc[:,['Year','Month','Stations','Rev6']]
df_c4=df_i.loc[:,['Year','Month','Stations','Rev7']]
df_c5=df_i.loc[:,['Year','Month','Stations','Rev8']]
df_c6=df_i.loc[:,['Year','Month','Stations','Rev9']]
df_c7=df_i.loc[:,['Year','Month','Stations','Rev10']]
df_c8=df_i.loc[:,['Year','Month','Stations','Rev11']]
df_c9=df_i.loc[:,['Year','Month','Stations','Rev12']]
df_c10=df_i.loc[:,['Year','Month','Stations','Rev13']]
df_c11=df_i.loc[:,['Year','Month','Stations','Rev14']]
df_c12=df_i.loc[:,['Year','Month','Stations','Rev15']]
df_c13=df_i.loc[:,['Year','Month','Stations','Rev16']]
df_c14=df_i.loc[:,['Year','Month','Stations','Rev17']]
df_c15=df_i.loc[:,['Year','Month','Stations','Rev18']]
df_c16=df_i.loc[:,['Year','Month','Stations','Rev19']]
df_c17=df_i.loc[:,['Year','Month','Stations','Rev20']]
df_c18=df_i.loc[:,['Year','Month','Stations','Rev21']]



# Add category and SUb Category to Rev2
df_c2.insert(0, 'Subcategory',df1.iloc[1]['Subcategory'])
df_c2.insert(0, 'Category',df1.iloc[1]['Category'])
df_c3.insert(0, 'Subcategory',df1.iloc[2]['Subcategory'])
df_c3.insert(0, 'Category',df1.iloc[2]['Category'])
df_c4.insert(0, 'Subcategory',df1.iloc[3]['Subcategory'])
df_c4.insert(0, 'Category',df1.iloc[3]['Category'])
df_c5.insert(0, 'Subcategory',df1.iloc[4]['Subcategory'])
df_c5.insert(0, 'Category',df1.iloc[4]['Category'])
df_c6.insert(0, 'Subcategory',df1.iloc[5]['Subcategory'])
df_c6.insert(0, 'Category',df1.iloc[5]['Category'])
df_c7.insert(0, 'Subcategory',df1.iloc[6]['Subcategory'])
df_c7.insert(0, 'Category',df1.iloc[6]['Category'])
df_c8.insert(0, 'Subcategory',df1.iloc[7]['Subcategory'])
df_c8.insert(0, 'Category',df1.iloc[7]['Category'])
df_c9.insert(0, 'Subcategory',df1.iloc[8]['Subcategory'])
df_c9.insert(0, 'Category',df1.iloc[8]['Category'])
df_c10.insert(0, 'Subcategory',df1.iloc[9]['Subcategory'])
df_c10.insert(0, 'Category',df1.iloc[9]['Category'])
df_c11.insert(0, 'Subcategory',df1.iloc[10]['Subcategory'])
df_c11.insert(0, 'Category',df1.iloc[10]['Category'])
df_c12.insert(0, 'Subcategory',df1.iloc[11]['Subcategory'])
df_c12.insert(0, 'Category',df1.iloc[11]['Category'])
df_c13.insert(0, 'Subcategory',df1.iloc[12]['Subcategory'])
df_c13.insert(0, 'Category',df1.iloc[12]['Category'])
df_c14.insert(0, 'Subcategory',df1.iloc[13]['Subcategory'])
df_c14.insert(0, 'Category',df1.iloc[13]['Category'])
df_c15.insert(0, 'Subcategory',df1.iloc[14]['Subcategory'])
df_c15.insert(0, 'Category',df1.iloc[14]['Category'])
df_c16.insert(0, 'Subcategory',df1.iloc[15]['Subcategory'])
df_c16.insert(0, 'Category',df1.iloc[15]['Category'])
df_c17.insert(0, 'Subcategory',df1.iloc[16]['Subcategory'])
df_c17.insert(0, 'Category',df1.iloc[16]['Category'])
df_c18.insert(0, 'Subcategory',df1.iloc[17]['Subcategory'])
df_c18.insert(0, 'Category',df1.iloc[17]['Category'])


# Write teh data into final file.
df_f1.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',')
#df_f2.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',',header=None)
df_c2.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',',header=None)
df_c3.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',',header=None)
df_c4.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',',header=None)
df_c5.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',',header=None)
df_c6.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',',header=None)
df_c7.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',',header=None)
df_c8.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',',header=None)
df_c9.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',',header=None)
df_c10.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',',header=None)
df_c11.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',',header=None)
df_c12.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',',header=None)
df_c13.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',',header=None)
df_c14.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',',header=None)
df_c15.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',',header=None)
df_c16.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',',header=None)
df_c17.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',',header=None)
df_c18.to_csv('E:\Python\seven/OP_out_final.csv',mode='a', sep=',',header=None)





















