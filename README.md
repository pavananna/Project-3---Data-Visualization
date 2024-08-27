# Project-3---Data-Visualization

1) To load the data set we have to import the pandas and then read the csv file.
2) Removing Duplicates & dealing missing values :
      a) For finding the missing values we have to use "isnull()" function to find the missing values, In the above dataset 
         there is no null vaules, now we have to any duplicaltes are there are not.
      b) For find the duplicates we have to use "drop_duplicates()" function for dropping the duplicates values, In the 
         above data set there is no duplicate values.
3) Removing the unnecesary Columns:
   3.1) Removing the numeric columns:
        a) For removing the unnecesary columns we have to find the correlation for the SalePrice Column with all Other 
           columns because we have to find the columns that are impacting the Price.
        b) After finding the correlation by using "corr()" function, we will get SalePrice columns to all other column 
           correlation.
        c) The values which are between -0.1 to +0.1 , remove those columns because these vaules are not showing that much 
           impact on the SalePrice column.
        d) For removing those columns we have to use "drop()" function.
    3.2) Removing the Categorical Column:
        a) For finding the columns which are categorical we can use "dtype()" (or) "info()" we will get the data types of 
           all the columns.
        b) Now we have to convert all the columns into numeric columns, For that we have take each categorical row and find 
           all the unique values for each column by using the "unique()" method.
        3.2.1) Feature Engineeering:
             a) There are some columns whose values with short abrevastion, so now we have create a new columns with the 
                values full abrevastion.
             b) For yhat we have use the "replace()" Method to replace the old values with the new values.
        c) After replacing the old values with the new vaules now we have to use" Label encoder from Sklearn" which is used             to give the unique numerical values for each unique value in the column.
        d) Now all the categorical columns are converted into numeric columns, so again find the correlation for SalePrice 
           to the all the columns , the columns which have the values between -0.1 to +0.1 remove those columns.
4) Univariate Analysis:
        a) when we have to do the univaraite analysis we have different types of plots like , countplot, histplot, vilion 
           plot,boxplot.
        b) For the above columns like 'GarageFinish',HouseStyle', '1stFlrSF' we have used the count plot as well as vilion 
           plot for funding how which unique has been used more times.
5) Bivariate Analysis:
        a) When we want to do a bivariate analysis we have different types of plots like Scatter plot, strip plot, bar plot, 
           line plot, vilion plot, box plot.
        b) For  the columns which have the multiple unique values like when we have the area of square feet we have multiple 
           unique values then we have to the scatter plot like YearBuilt, BsmtUnfSF.
        c) Bar plot when we have to find the trends or compare wther the slaes have been increased or not the we have to use 
           the bar plot like yearly sales.
6) Multivariate Analysis:
        a) For doing the Multivariate analysis we have different types of plot like Scatter plot with hue, Strip plot with 
           hue, heatmap, Pairplot wih hue.
        b) For the columns where we have multiple unique values and with some overall consition data then we have to use 
           scatter plot like lotshape, MasVnrArea,YearBuilt like that.
        c) when we have the data with countable unique values with some hue values then we can use the stripplot, the 
           columns like BedroomAbvGr, RoofStyle,Exterior2nd like that.
        d) when you want to compare multiple columns with each other then we have to use pair plot.
