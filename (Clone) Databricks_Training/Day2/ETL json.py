# Databricks notebook source
# MAGIC %run /Workspace/Users/varshasalunke9741@gmail.com/Databricks_Training/includes

# COMMAND ----------

df=spark.read.json("/Volumes/va_michelin/michelin/raw/constructors.json")

# COMMAND ----------

df1=add_ingestion_col(df)

# COMMAND ----------

df1.write.mode("overwrite").saveAsTable("constructor")
