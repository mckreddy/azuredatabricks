# Databricks notebook source
# MAGIC %md #Basic EDA with Azure Databricks

# COMMAND ----------

# MAGIC %md
# MAGIC This notebook contains slightly more advanced topics like data cleaning, handling missing values, and correlation analysis.
# MAGIC 
# MAGIC In order to run this notebook you should have previously run the <a href="$./02 Loading data with Azure Databricks">Loading data with Azure Databricks</a> notebook to get your data propery loaded.

# COMMAND ----------

# MAGIC %md ### Simple exploration

# COMMAND ----------

# MAGIC %md
# MAGIC To work with this data programmatically, we can access the data using a Spark DataFrame. Run the following code to create a DataFrame from our table.
# MAGIC 
# MAGIC Be sure to update the table name  "usedcars\_#####" with the unique name created while running the <a href="$./02 Loading data with Azure Databricks">Loading data with Azure Databricks</a> notebook.

# COMMAND ----------

df = spark.sql("SELECT * FROM usedcars_#####")
df

# COMMAND ----------

# MAGIC %md **`<IMPORTANT NOTE>`**

# COMMAND ----------

# MAGIC %md 
# MAGIC There are two major types of dataframes you will encounter in Python: Spark dataframes (sometimes referred as PySpark dataframes) and Pandas dataframes. Although they share several common features, they also differ quite a lot. Throughout the labs we will work mostly with Spark dataframes. Fortunatelly, it's very simple to convert a Spark dataframe to a Pandas dataframe. Run the next cell to get a Pandas dataframe from your Spark dataframe:

# COMMAND ----------

pdf = df.toPandas()
pdf

# COMMAND ----------

# MAGIC %md Read more about these differences [here](https://databricks.com/blog/2015/08/12/from-pandas-to-apache-sparks-dataframe.html).
# MAGIC 
# MAGIC 
# MAGIC **`</IMPORTANT NOTE>`**

# COMMAND ----------

# MAGIC %md Let's start by taking a look at our dataframe. Run the following cells to get the top 10 entries in the dataframe.

# COMMAND ----------

df.head(10)

# COMMAND ----------

# MAGIC %md The next one does the same but displays the data in more organized manner.

# COMMAND ----------

df.show(10)

# COMMAND ----------

# MAGIC %md We can get some information about the structure of the data. Note that all columns are currently of type string (as a byproduct of the import process). Well address this issue later in this notebook.

# COMMAND ----------

df.dtypes

# COMMAND ----------

# MAGIC %md
# MAGIC Now let's try getting a sense of our data set by collecting some summary statistics about every column. Run the following cell.

# COMMAND ----------

summary = df.describe()
display(summary)

# COMMAND ----------

# MAGIC %md We can do the same for one column.

# COMMAND ----------

display(df.describe('Price'))

# COMMAND ----------

# MAGIC %md 
# MAGIC **Challenge #1**
# MAGIC 
# MAGIC 
# MAGIC Looking at the count of values for the Price column, how many rows in our dataset our missing values for Price?

# COMMAND ----------

# MAGIC %md
# MAGIC **Challenge #2**
# MAGIC 
# MAGIC Which two other columns appear to be missing data? 

# COMMAND ----------

# MAGIC %md ### Data preparation

# COMMAND ----------

# MAGIC %md 
# MAGIC When examining the summary stats, one problem may have jumped out at you in the Price column. The Max price is $9,995.00 but the Mean price is $10,728.00. This does not make sense (e.g., the max price should be equal to or greater than the mean). Let's explore the data a little more to find out why.
# MAGIC 
# MAGIC Remember how all types are string. This is probably something we should fix. In fact, except for FuelType, all of the columns in this data should be numeric. 
# MAGIC 
# MAGIC Run the following cell to create a new DataFrame where all of the numeric cells are of the correct data type.
# MAGIC 
# MAGIC Be sure to update the table name  "usedcars\_#####" with the unique name created while running the <a href="$./02 Loading data with Azure Databricks">Loading data with Azure Databricks</a> notebook.

# COMMAND ----------

df_typed = spark.sql("SELECT cast(Price as int), cast(Age as int), cast(KM as int), FuelType, cast(HP as int), cast(MetColor as int), cast(Automatic as int), cast(CC as int), cast(Doors as int), cast(Weight as int) FROM usedcars_#####")
df_typed

# COMMAND ----------

# MAGIC %md
# MAGIC Now that we have fixed up the data types, let's revisit the statistical summary.

# COMMAND ----------

display(df_typed.describe())

# COMMAND ----------

# MAGIC %md
# MAGIC As can be seen in the above output, now the Price summary makes sense because the values are being properly handled as integers instead of strings. The min price is $4,350, the mean price is $10,728 and the max price is $32,500. 

# COMMAND ----------

# MAGIC %md
# MAGIC Now let's turn our attention to the FuelType and understand what values we have in that column:

# COMMAND ----------

display(df_typed.select("FuelType").distinct())

# COMMAND ----------

# MAGIC %md
# MAGIC As the above output shows, we have various issues with the FuelType values:
# MAGIC - The values have inconsistent casing (e.g., Diesel and diesel)
# MAGIC - We have three values that effectively mean the same thing (CNG, CompressedNaturalGas and methane).
# MAGIC 
# MAGIC Let's cleanup these values in our DataFrame. We want to perform these transformations:
# MAGIC - "Diesel" to "diesel"
# MAGIC - "Petrol" to "petrol"
# MAGIC - "CompressedNaturalGas" to "cng"
# MAGIC - "methane" to "cng"
# MAGIC - "CNG" to "cng"
# MAGIC 
# MAGIC We can use the replace() method of the na subpackage of the DataFrame to easily describe and apply our transformation in way that will work at scale.

# COMMAND ----------

df_cleaned_fueltype = df_typed.na.replace(["Diesel","Petrol","CompressedNaturalGas","methane","CNG"],["diesel","petrol","cng","cng","cng"],"FuelType")
display(df_cleaned_fueltype.select("FuelType").distinct())

# COMMAND ----------

# MAGIC %md
# MAGIC Now for the last bit of cleanup- let's address the rows that have missing (null) values. Recall from our previous exploration that the columns Price, Age and KM each had rows with missing values. 
# MAGIC 
# MAGIC You typically handle missing values either by deleting the rows that have them or filling them in with a suitable computed valued (sometimes called data imputation). While how you handle missing values depends on the situation, in our case we just want to delete the rows that having missing values. 

# COMMAND ----------

df_cleaned_of_nulls = df_cleaned_fueltype.na.drop("any",subset=["Price", "Age", "KM"])
display(df_cleaned_of_nulls.describe())

# COMMAND ----------

# MAGIC %md
# MAGIC **Challenge #3**
# MAGIC 
# MAGIC 
# MAGIC After cleaning your dataset of rows having any missing values, how many rows does your data set have?

# COMMAND ----------

# MAGIC %md 
# MAGIC Next, we want to save this prepared dataset as a global table so that we could use the cleansed data easily such as for further data understanding efforts or for modeling, irrespective of which Databrick cluster we end up using later on.
# MAGIC 
# MAGIC To do so, execute the following cell. 
# MAGIC 
# MAGIC Be sure to update the table name  "usedcars\_clean\_#####" (replace ##### to make the name unique within your environment - we recommend using the same ##### value you used while running the <a href="$./02 Loading data with Azure Databricks">Loading data with Azure Databricks</a> notebook).

# COMMAND ----------

df_cleaned_of_nulls.write.mode("overwrite").saveAsTable("usedcars_clean_#####")

# COMMAND ----------

# MAGIC %md ### Correlation analysis

# COMMAND ----------

# MAGIC %md
# MAGIC Finally, lets explore the relationship our data shows between the price of the car and the age of that car for cars that run on petrol only.
# MAGIC 
# MAGIC Run the following cell. Observe that a Scatter Plot chart type was selected. If you examine the Plot Options, notice that we have charted Age against Price. 
# MAGIC 
# MAGIC Be sure to update the table name  "usedcars\_clean\_#####" with the unique name created previously in this notebook.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT Price, Age FROM usedcars_clean_##### WHERE FuelType = 'petrol'

# COMMAND ----------

# MAGIC %md
# MAGIC ** Challenge #4**
# MAGIC 
# MAGIC Can you explain what the chart suggests about the data? 

# COMMAND ----------

# MAGIC %md Achieve the same using the matplotlib and pandas style:

# COMMAND ----------

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

fig, ax = plt.subplots()
pdf = df_cleaned_of_nulls.toPandas()
ax.scatter(pdf.Age, pdf.Price)

display(fig)

# COMMAND ----------

# MAGIC %md 
# MAGIC Run the following two cells to see the distribution of KM and the relationship between KM and Price. Note the use of np.arrange to create the array used for bins in the histogram.
# MAGIC 
# MAGIC Do you notice anything out of the ordinary?

# COMMAND ----------

fig, ax = plt.subplots()

bins= np.arange(0, 250000, 5000)
pdf['KM'].plot(kind='hist')

display(fig)

# COMMAND ----------

fig, ax = plt.subplots()
ax.scatter(pdf.KM, pdf.Price)
display(fig)


# COMMAND ----------

# MAGIC %md
# MAGIC Using Pandas it is very easy to calculate the correlations between all features:
# MAGIC 
# MAGIC ```python
# MAGIC dataframe.corr()
# MAGIC ```
# MAGIC 
# MAGIC We only want the correlation for features that are not categorical (remember that we consider binary features as categorical).   
# MAGIC In our dataset this corresponds to the features Age, KM, Weight, CC and HP.
# MAGIC 
# MAGIC __Exercise:__ Calculate the correlation matrix for all features that are not categorical. Remember to include `Price` since we also want the correlations between the features and the sales price.

# COMMAND ----------

# Run this cell and a very nice matrix will hopefully appear
fig, ax = plt.subplots()
sns.heatmap(pdf[['Price','Age', 'KM', 'Weight', 'CC', 'HP']].corr(),annot=True, center=0, cmap='BrBG', annot_kws={"size": 14})
display(fig)

# COMMAND ----------

# MAGIC %md
# MAGIC Even with our limited knowledge about cars we expected a stronger correlation between horsepower and weight, and also between horsepower and displacement.  
# MAGIC However, we also know that diesel-engines are very different from petrol-engines, and so mixing these two types can make the correlation very weak. 
# MAGIC 
# MAGIC __Exercise__: Plot the correlation matrix for all cars using petrol as fuel.

# COMMAND ----------

### Your code goes here

# COMMAND ----------

# MAGIC %md
# MAGIC __Exercise__: Plot the correlation matrix for all cars using diesel

# COMMAND ----------

### Your code goes here

# COMMAND ----------

# MAGIC %md
# MAGIC Look at that! We got a reasonable correlation between HP and CC and between HP and Weight.   
# MAGIC We can also see that the correlation between HP and Price,  Weight and Price and KM and Price increased when we split the data on the fueltypes petrol and diesel.  
# MAGIC 
# MAGIC __This is very interesting and worth a closer look! (left as an exercise)__
# MAGIC 
# MAGIC You are now ready to move to the next step: <a href="$./04 Advanced EDA with Azure Databricks">Advanced EDA with Azure Databricks</a>

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC # Answers to Challenges
# MAGIC 1. Seven rows are missing Price data. There are 1446 rows in the data set, but only 1439 of them have a value for Price.
# MAGIC 2. Age and KM also have fewer that 1446 values. 
# MAGIC 3. There should be 1436 rows after removing rows with missing values.
# MAGIC 4. The chart suggests that the Price of the car appears to go down with an increase in Age. So the older the car, the cheaper it is.