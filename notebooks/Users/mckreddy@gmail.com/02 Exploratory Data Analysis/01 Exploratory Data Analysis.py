# Databricks notebook source
# MAGIC %md
# MAGIC #Exploratory Data Analysis (EDA): Car prices
# MAGIC 
# MAGIC In this lab you will investigate a dataset with sale prices in $ for used (second-hand) cars.   
# MAGIC During the lab you will use a lot of the techniques we introduced in the presentation about EDA (Exploratory data analysis).
# MAGIC 
# MAGIC In the first part of this lab we stick to the most crucial elements in an EDA. If you are new to Python and/or Data Science this will be plenty of content to digest.   
# MAGIC But if you have more experience you might have time to explore the advanced section as well. This section contains many interesting things that we won't explain to the same level of detail as the main part.    

# COMMAND ----------

# MAGIC %md This lab is structured into three notebooks that cover the most important topics related to Exploratory Data Analysis (EDA). If your are new to Python and/or data science we highly recommend to go through the lab notebooks in the suggested order. 
# MAGIC 
# MAGIC The lab notebooks are:  
# MAGIC * <a href="$./02 Loading data with Azure Databricks">Loading data with Azure Databricks</a> - contains an introduction to data loading with Azure Data bricks. You will learn how to prepare your data environment to start performing EDA.
# MAGIC * <a href="$./03 Basic EDA with Azure Databricks">Basic EDA with Azure Databricks</a>  - contains a bit more advanced topics like data cleaning, handling missing values, and correlation analysis.
# MAGIC * <a href="$./04 Advanced EDA with Azure Databricks">Advanced EDA with Azure Databricks</a> - contains advanced topics like linear regression analysis, one hot encoding, feature scaling, dimensionality reduction, and feature importance estimation.