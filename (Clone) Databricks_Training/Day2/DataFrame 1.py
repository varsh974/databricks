# Databricks notebook source
# MAGIC %md
# MAGIC ###  Create Table
# MAGIC ####   1.Pyspark (dataframe)
# MAGIC ####   2.Spark SQL
# MAGIC ####   3.UI

# COMMAND ----------

# DBTITLE 1,Reading/Extracting  file
df=spark.read.csv("/Volumes/va_michelin/michelin/raw/circuits.csv",header=True,inferSchema=True)

# COMMAND ----------

df.display()

# COMMAND ----------

from pyspark.sql.functions import col
df.select(col("circuitId").alias("circuit_id"),"circuitRef").display()

# COMMAND ----------

df.withColumnRenamed("circuitId","circuit_id").display()

# COMMAND ----------

df.withColumnsRenamed({"circuitId":"circuit_id","circuitRef":"circuit_ref"}).display()

# COMMAND ----------

df.withColumn("ingestion_date",current_date()).display()

# COMMAND ----------

df.withColumn("country",upper("country")).display()
