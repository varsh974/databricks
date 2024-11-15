# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

input_path="dbfs:/mnt/vadatabricks1/michelin/project/"

# COMMAND ----------

def add_ingestion_col(df):
  df_final1=df.withColumn("ingestion_date",current_timestamp())
  df_final2 =df.withColumn("Source_path",input_file_name())
  return df_final2

# COMMAND ----------

# MAGIC %sql
# MAGIC use catalog michelin;

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists michelin.bronze;
# MAGIC create schema if not exists michelin.silver;
# MAGIC create schema if not exists michelin.gold;
