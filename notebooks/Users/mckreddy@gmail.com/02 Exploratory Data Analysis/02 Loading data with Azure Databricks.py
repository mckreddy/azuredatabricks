# Databricks notebook source
# MAGIC %md #Loading data with Azure Databricks

# COMMAND ----------

# MAGIC %md ### Import data from a file

# COMMAND ----------

# MAGIC %md
# MAGIC In this section you will import a small dataset describing used cars and their price according to various factors. 

# COMMAND ----------

# MAGIC %md
# MAGIC There are multiple ways to make your data available for processing using Azure Databricks, either by connecting to the data source directly or by making a copy of the data into storage managed by Azure Databricks.
# MAGIC 
# MAGIC At a high level you can:
# MAGIC * [Upload small files through the Workspace user interface](https://docs.azuredatabricks.net/user-guide/tables.html#create-table-ui) that are then made available as global tables available across clusters. 
# MAGIC * Connect to remote data sources like Azure Storage blobs, SQL Data Warehouse and Cosmos DB. Once connected, you can copy the data into storage managed by Azure Databricks, if desired.
# MAGIC 
# MAGIC When using Azure Storage blobs, you can:
# MAGIC * [Access Azure Blob storage directly using the HDFS API](https://docs.azuredatabricks.net/spark/latest/data-sources/azure/azure-storage.html#access-azure-blob-storage-using-the-hdfs-api) and access the data using the WASBS protocol. This approach enables access to all users of the cluster in which access is configured.
# MAGIC * [Mount Azure Storage blob contains to the Databricks File System (DBFS)](https://docs.azuredatabricks.net/spark/latest/data-sources/azure/azure-storage.html#mount-azure-blob-storage-containers-with-dbfs) and access the data using DBFS file paths (e.g., underneath /mnt). This approach enables access to all users across all clusters in a workspace.
# MAGIC 
# MAGIC In this notebook, we will work with a small dataset stored in a CSV file that is available from Azure Storage blobs. 

# COMMAND ----------

# MAGIC %md
# MAGIC First, you will download a copy of the used cars data set. 
# MAGIC 
# MAGIC You can download this from here:
# MAGIC [UsedCars.csv](https://databricksdemostore.blob.core.windows.net/data/02.02/UsedCars.csv)

# COMMAND ----------

# MAGIC %md 
# MAGIC Second, you will upload this CSV file to your Azure Databricks Workspace by following these steps.
# MAGIC 
# MAGIC Open a new browser tab and navigate to your workspace.
# MAGIC 
# MAGIC Navigate to the Data tab and then select + to the right of Tables to create a new table. 
# MAGIC 
# MAGIC ![img](https://databricksdemostore.blob.core.windows.net/images/02/data-tab.png)
# MAGIC 
# MAGIC Leave the Data source set to Upload File. 
# MAGIC 
# MAGIC ![img](https://databricksdemostore.blob.core.windows.net/images/02/create-new-table-ui-data-source.png)
# MAGIC 
# MAGIC Select browse and then choose your copy of UsedCars.csv
# MAGIC 
# MAGIC ![img](https://databricksdemostore.blob.core.windows.net/images/02/create-new-table-ui-file.png)
# MAGIC 
# MAGIC Your file will be uploaded. Select Create Table with UI.
# MAGIC 
# MAGIC ![img](https://databricksdemostore.blob.core.windows.net/images/02/create-new-table-ui-file-ready.png)
# MAGIC 
# MAGIC In cluster drop-down, select an available cluster, and choose Preview Table. 
# MAGIC 
# MAGIC Then in the Specify Table Attributes, change the table name to **"usedcars_#####"** (replace ##### to make the name unique within your environment) and check the box for "First row is header". Your preview should look as follows. Observe that the table has the correct header names and that we are defaulting all columns to type STRING.
# MAGIC 
# MAGIC ![img](https://databricksdemostore.blob.core.windows.net/images/02/create-new-table-ui-table-attributes.png)
# MAGIC 
# MAGIC Select Create Table. When the Table:usedcars screen appears showing your new table, your data is loaded into a Table and you continue with the next steps in this notebook.

# COMMAND ----------

# MAGIC %md ### Access imported data

# COMMAND ----------

# MAGIC %md
# MAGIC Your data is now available for access using the name "usedcars". Run the following SQL query (be sure to update the table name "usedcars_#####" with the unique name created during the previous step) to examine the contents:

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM usedcars_#####

# COMMAND ----------

# MAGIC %md
# MAGIC Here is a summary of what each of the above columns mean
# MAGIC 
# MAGIC * Price: Sales price in $
# MAGIC * Age: Age of car in month
# MAGIC * KM: Mileage in kilometer
# MAGIC * Fueltype: Type of fuel used by the car
# MAGIC * HP: Engine power in Horsepower
# MAGIC * MetColor: Does the car have metallic paint or not. Binary (0 or 1)
# MAGIC * Automatic: Is the transmission automatic or not (not meaning manual transmission). Binary (0 or 1)
# MAGIC * CC: Displacement of the engine in cubic centimeters. (Number of cylinders multiplied by cylinder volume)
# MAGIC * Doors: Number of doors
# MAGIC * Weight: Weight in pounds

# COMMAND ----------

df = spark.sql("SELECT * FROM usedcars_#####")
df

# COMMAND ----------

# MAGIC %md 
# MAGIC Run the following cell to understand how many rows of data we have in this dataset. 

# COMMAND ----------

df.count()

# COMMAND ----------

# MAGIC %md You are now ready to move to the next step: <a href="$./03 Basic EDA with Azure Databricks">Basic EDA with Azure Databricks</a>