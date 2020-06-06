# Databricks notebook source
# MAGIC %md
# MAGIC # Event Hub Demo Configuration
# MAGIC 
# MAGIC This Event Hub Demo requires three libraries.
# MAGIC 
# MAGIC ## Library Requirements
# MAGIC 
# MAGIC 1. the Maven library with coordinate `com.microsoft.azure:azure-eventhubs-spark_2.11:2.3.7`
# MAGIC    - this allows Databricks `spark` session to communicate with an Event Hub
# MAGIC 2. the Python library `azure-eventhub`
# MAGIC    - this is allows the Python kernel to stream content to an Event Hub
# MAGIC 3. the Python library `sseclient`
# MAGIC    - this is used to create a streaming client to an existing streaming server

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Links
# MAGIC 
# MAGIC More information on Azure Event Hubs is available here:
# MAGIC https://docs.databricks.com/spark/latest/structured-streaming/streaming-event-hubs.html
# MAGIC 
# MAGIC An example of sending content to an Azure Event Hub is shown here:
# MAGIC https://github.com/Azure/azure-event-hubs-python/blob/master/examples/send.py. This example was used to develop the streaming server used in this Demonstration.
# MAGIC 
# MAGIC The streaming server is reading a stream of changes made to Wikipedia. More on this data can be read here:
# MAGIC https://wikitech.wikimedia.org/wiki/EventStreams

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Azure Configuration
# MAGIC 
# MAGIC ### Create an Event Hub Namespace as a New Resource
# MAGIC 
# MAGIC <img src="https://files.training.databricks.com/images/adbcore/AAELV1l32QhCsJvKsehUJJ3EKq9G5uYnGKgB.png" width=600px>
# MAGIC 
# MAGIC <img src="https://files.training.databricks.com/images/adbcore/AAH4_gC7uxZAc4R2fHHdC9HldldhUOwwMU0B.png" width=600px>

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC <img src="https://files.training.databricks.com/images/adbcore/AAEEdFwJSWhPfZju3ePl_k98zo0yHwVKxyQB.png" width=400px>
# MAGIC 
# MAGIC <img src="https://files.training.databricks.com/images/adbcore/AAEGOxRtdKJIDJNxvf4oUI9whneQImQdPrAB.png" width=400px>

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### Retrieve Access Keys
# MAGIC 
# MAGIC Access the new Event Hub Namespace and make note of the primary `ConnectionString` available as part of the `RootManageSharedAccessKey`. This will be needed later for authentication.
# MAGIC 
# MAGIC <img src="https://files.training.databricks.com/images/adbcore/AAFbffwIdAtLsqRmJD_xMFMdWZ6RtvRSeo4B.png" width=600px>

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### Create a New Event Hub
# MAGIC 
# MAGIC Use and make note of a unique Event Hub name.
# MAGIC 
# MAGIC <img src="https://files.training.databricks.com/images/adbcore/AAGD4HAs-45OmoWeOOj_JpbweYM_mdZXil4B.png" width=500px>
# MAGIC 
# MAGIC <img src="https://files.training.databricks.com/images/adbcore/AAEoyeM119xOFbh8pk_S--ihBcLdacUifbUB.png" width=500px>

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2020 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>