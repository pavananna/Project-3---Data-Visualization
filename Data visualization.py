#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


d1=pd.read_csv("E:\\DIGI chrome\\Data sets\\housing_data (1).csv")


# In[3]:


d1


# In[4]:


d1.shape


# In[5]:


d1.columns


# In[6]:


d1.drop_duplicates(inplace=True)  #there is no duplicates


# In[7]:


d1.isnull().sum() #there is no null vaules


# In[8]:


sns.countplot(x='YrSold',data=d4)


# In[ ]:


# now we have to see the columns which are not much effect the sales price columns
# to see that we have to find the corelation and remove the vaules lie between -0.1 to +0.1


# In[ ]:


d1.corr() #by default it shows the correlation for the numeric columns.


# ### UNIVARIATE ANALYSIS

# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns


plt.figure(figsize = (20,20), dpi = 500)
sns.heatmap(d1.corr(), annot=True)


# In[ ]:


d2=d1.drop(['Unnamed: 0','OverallCond','BsmtFinSF2','LowQualFinSF','BsmtHalfBath','3SsnPorch','MiscVal','YrSold'],axis=1)
d2


# In[ ]:


d2.shape


# In[ ]:


#now we have to find the correlation for the categorical columns.
d2.info()


# In[ ]:


d2.select_dtypes(include="object").columns


# In[ ]:





# In[ ]:


categorical_columns=['MSSubClass','MSZoning', 'Street', 'Alley', 'LotShape', 'LandContour',
       'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1',
       'Condition2', 'BldgType', 'HouseStyle', 'RoofStyle', 'RoofMatl',
       'Exterior1st', 'Exterior2nd', 'MasVnrType', 'ExterQual', 'ExterCond',
       'Foundation', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1',
       'BsmtFinType2', 'Heating', 'HeatingQC', 'CentralAir', 'Electrical',
       'KitchenQual', 'Functional', 'FireplaceQu', 'GarageType',
       'GarageFinish', 'GarageQual', 'GarageCond', 'PavedDrive', 'PoolQC',
       'Fence', 'MiscFeature', 'MoSold', 'SaleType', 'SaleCondition']


# In[ ]:


categorical_columns


# In[ ]:


d2['MSSubClass'].unique()


# In[ ]:


from sklearn.preprocessing import LabelEncoder


# In[ ]:


lb=LabelEncoder()


# In[ ]:


# here we have taken categorical columns in a list and passed it into label encoder to transform all 
# the categorical columns into numerical columns.
for vaule in categorical_columns:
    d2[vaule]=lb.fit_transform(d2[vaule])
    


# In[ ]:


d2.info()


# In[ ]:


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns',None)
d2.corr()['SalePrice']


# In[ ]:


d3=d2.drop(['MSSubClass','Condition1','Condition2','Street','Alley','LandContour','Utilities','LotConfig','LandSlope','BldgType','BsmtCond','BsmtFinType2','FireplaceQu','MiscFeature','MoSold','SaleType'],axis=1)


# In[ ]:


d3.shape


# In[ ]:


d3.columns


# In[ ]:


#to get the original vaules of categorical columns take those columns and replace it those columns in original dataset
d4=d1[['MSZoning', 'LotFrontage', 'LotArea', 'LotShape', 'Neighborhood',
       'HouseStyle', 'OverallQual', 'YearBuilt', 'YearRemodAdd', 'RoofStyle',
       'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'MasVnrArea',
       'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual', 'BsmtExposure',
       'BsmtFinType1', 'BsmtFinSF1', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating',
       'HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF',
       'GrLivArea', 'BsmtFullBath', 'FullBath', 'HalfBath', 'BedroomAbvGr',
       'KitchenAbvGr', 'KitchenQual', 'TotRmsAbvGrd', 'Functional',
       'Fireplaces', 'GarageType', 'GarageYrBlt', 'GarageFinish', 'GarageCars',
       'GarageArea', 'GarageQual', 'GarageCond', 'PavedDrive', 'WoodDeckSF',
       'OpenPorchSF', 'EnclosedPorch', 'ScreenPorch', 'PoolArea', 'PoolQC',
       'Fence', 'SaleCondition', 'SalePrice']]


# In[ ]:


d4


# In[ ]:


d4.shape


# In[ ]:


d4.columns


# # univarate analysis

# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


sns.histplot(d4,x='SalePrice',)


# From this  we can say that most of the flates are ranges from 50,000 to 4,00,000

# In[ ]:


d4.columns


# In[ ]:


d4['PoolArea'].unique()


# In[ ]:


#Feature engineering
d4['Soiltype']=d4['MSZoning'].replace(['RL', 'RM', 'C (all)', 'FV', 'RH'],['Residential LD','Residential MD','Commercial','Floating VR','Residential HD'])


# In[ ]:


d4.drop('MSZoning',axis=1)


# In[ ]:


plt.scatter(x=d4['Soiltype'],y=d4['SalePrice'])


# ->From the above data we can say that most of the flates having Soiltype has Residential Low density ,
#  and also "the flat having soiltype as residential are having the high price value and the the average sale price.
#  
# ->And the soiltype as commericial  has less sale price.

# In[ ]:


d4['LotArea'].unique()


# In[ ]:


sns.lineplot(data=d4,x='SaleCondition',y='SalePrice')


# When the sale condition is partial we have high sale price and AdjLand has low saleprice

# In[ ]:


sns.barplot(data=d4,x='PoolArea',y='SalePrice',hue='PoolQC')


# In[ ]:


sns.countplot(x=d4['PoolArea'],data=d4)


# We can clearly see that when the when pool quality is excellent has high sales price and most of the flat doesnot have any pool area 

# In[ ]:


sns.barplot(data=d4,x='HouseStyle',y='SalePrice',hue='OverallQual')


# In[ ]:


sns.countplot(x=d4['HouseStyle'],data=d4)


# when the House Style is 2Story the sales price is high and also most of the flat are 1Story dwelling.

# In[ ]:


sns.countplot(x=d4['GarageFinish'],data=d4)


# Here we can observe that most of the garage are unfinished

# In[ ]:


sns.histplot(data=d4,x='GarageYrBlt',hue='GarageCond',kde=True)


# Here we can see that the garage thas has been bulit between 1920 to 2000 has the condition as typical and normal which we can say that the garage condition is not that much good but when the garage that has been built between 1920 to 1940 has the garage conditon has  excellent.

# In[ ]:


sns.scatterplot(x='GarageType',y='SalePrice',data=d4)


# Here we can see that the garage is attached to flat has high salesprice

# In[ ]:


sns.pairplot(d4[['GarageArea','GarageCars','SalePrice']])


# Here we can see that most of the flats has garage area between 500 to 1000 has high salesprice, and garage cars as 3 having high slaesprice.

# From the above deatails we can say that most of the flat doesnot have garage, but the garage that are attached to flat and having the garage area between 500 to 1000 which is specious to put 3 cars has high salesprice.  

# In[ ]:


'1stFlrSF', '2ndFlrSF'


# In[ ]:


sns.violinplot(data=d4,x='1stFlrSF',)


# From above diagram we can say that most of the flat have the first floor with the square feet between 1000 and 2000 

# In[ ]:


sns.violinplot(data=d4,x='2ndFlrSF')


# From above diagram we can say that most of the flat having square feet has 0 which means there is no second floor for most of the flats

# In[ ]:


sns.pairplot(d4[['1stFlrSF', '2ndFlrSF','SalePrice']])


# If we compare the 1stfloor and 2nd floor square feet diagram the most of the square feet between 500 to 2000 has 2nd floor and the area has squarefeet of 1900 have high sales price

# In[ ]:


d4["KitchenAbvGr"].unique()


# In[ ]:


sns.stripplot(x="KitchenAbvGr",hue="KitchenQual",y="SalePrice",data=d4)


# From this we can say that when the kicthen quality is excellent the sale price is high and when the kicthen quality is fair the sales price is low and also if we observe clearly most of the flates has the kitchen grade above 1.

# In[ ]:


d4['TotalBsmtSF'].unique()


# In[ ]:


sns.scatterplot(x="TotalBsmtSF",y="SalePrice",hue="BsmtQual",data=d4)


# From this we can say that when the basement condition is good and square feet is around 2000 the salesprice is high, there are some flates where there is no basement and when there is no basement the price is less than 2,00,000 and if we see only one flat have basement 6000sqft and condition is excellent but price is 2,00,000  which says that for that flat the remaning feauters are not good.

# In[ ]:


sns.scatterplot(x="BsmtUnfSF",y="SalePrice",data=d4)


# In[ ]:


sns.histplot(x=d4["BsmtUnfSF"],data=d4)


# From the above information we can clearly say most of the basement of the flats are not finished

# In[ ]:


sns.scatterplot(x="BsmtFinSF1",y="SalePrice",hue="BsmtFinType1",data=d4)


# From the above diagram we can say that when the basement finished area is good living quaters then the sales price is high and also when the basement finished area is average rec room then the sales price is low

# In[ ]:


sns.stripplot(x="BsmtExposure",y="SalePrice",data=d4,color="magenta")


# From the above diagram we can say that when we have walkout or garden-level walls are good exposure then the sales price is high.

# In[ ]:


d4['GrLivArea'].unique()


# In[ ]:


d4['BedroomAbvGr'].unique()


# In[ ]:


sns.scatterplot(x='GrLivArea',y="SalePrice",hue='BedroomAbvGr',data=d4)


# In[ ]:


sns.pairplot(d4[['BedroomAbvGr','FullBath', 'HalfBath','SalePrice']],)


# In[ ]:


d4['BedroomAbvGr'].unique()


# In[ ]:


sns.stripplot(x="BedroomAbvGr",y="SalePrice",data=d4,color="green")


# From the above two diagrams we can say that when we have the living area between 3000 to 4000 , which will have 4 bedrooms,if they have one half both room or 4 full bathrooms , In which the bedrooms should have grade level above 4 then the flat sales price is high.

# In[ ]:


d4['YearBuilt'].unique()


# In[ ]:


sns.scatterplot(x='YearBuilt',y="YearRemodAdd",data=d4)


# In[ ]:


sns.scatterplot(x='YearBuilt',y="YearRemodAdd",hue="SalePrice",data=d4)


# In[ ]:


sns.scatterplot(x='YearBuilt',y="SalePrice",data=d4)


# In[ ]:


sns.scatterplot(y='SalePrice',x="YearRemodAdd",data=d4)


# From the above diagram we can say that so many of the flates that are constructed after 1990 does not remodeled and the flates that are bulit in the year 2000 has high sales price.

# In[ ]:


sns.stripplot(x= 'RoofStyle',y="SalePrice",hue="RoofMatl",data=d4)


# From this we can say that when the roof style is Gable and roof material is wood Shingles the sales price is high not only that most of the flat are bulit by using gable type and with wood shingles only.

# In[ ]:


sns.stripplot(x="Exterior1st",y="SalePrice",data=d4,color="green")


# In[ ]:


d4['Exterior1st']=lb.fit_transform(d4['Exterior1st'])


# In[ ]:


sns.stripplot(x="Exterior1st",y="SalePrice",data=d4,color="green")


# In[ ]:


d4['Exterior2nd']=lb.fit_transform(d4['Exterior2nd'])


# In[ ]:


sns.stripplot(x="Exterior2nd",y="SalePrice",data=d4,color="magenta")


# From the above diagrams we can say that when the Exterior used more then one material and the condition of the material is average the sales price is high.

# In[ ]:


sns.scatterplot(y='SalePrice',x="MasVnrArea",hue="MasVnrType",data=d4)


# From this we can say that whwn there is no masnory veneer then the sales price is high and also when masnory veneer is brick face then also the sales price is high.

# In[ ]:


sns.violinplot(x="Heating",y="SalePrice",data=d4)


# In[ ]:


sns.stripplot(x="Heating",y="SalePrice",hue="HeatingQC",data=d4)


# From the above diagram we can say that when the heating is Gas forced warm air furnace and also the gas condition is excellent then the sales price is high and also most of the flats has the Gas forced warm air furnace as gas type.

# In[ ]:


d4['Fireplaces'].unique()


# In[ ]:


sns.violinplot(x="Fireplaces",y="SalePrice",data=d4)


# From this we can clearly say that when the fire places are 2 the sales price is high and also most of the flates doesnot have the fireplaces.

# In[ ]:


sns.stripplot(x='Functional',y="SalePrice",data=d4)


# Here the graph tells usin which the flates useful functionalities are warenteed for those the flates the sales price is high.

# In[ ]:


sns.countplot(x='Electrical',hue='CentralAir',data=d4)


# From this we can say that most of the flates have the centeral air condition with the circut type as Standard Circuit Breakers & Romex which is more useful.

# In[ ]:


sns.stripplot(x='Electrical',y='SalePrice',data=d4)


# the circut which has Standard Circuit Breakers & Romex has high sales price

# In[ ]:


sns.scatterplot(x='LotArea', y='SalePrice',hue="LotShape",data=d4)


# When the lot area isbetween 10000 to 50000 and when the shape is slighty irregular the sales price is high and most of the flates have lot area between 500 to 50000 square feet.

# In[ ]:


sns.stripplot(x='Foundation',y='SalePrice',data=d4)


# When the foundation of the flat is Poured Contrete the sale price is high and also most of the flates has the foundation as Poured Contrete.

# In[ ]:




