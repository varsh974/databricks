# Databricks notebook source
# MAGIC %md
# MAGIC ###  Create Table
# MAGIC ####   1.Pyspark (dataframe)
# MAGIC ####   2.Spark SQL
# MAGIC ####   3.UI

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

# DBTITLE 1,Reading/Extracting  file
df=spark.read.csv("/Volumes/va_michelin/michelin/raw/circuits.csv",header=True,inferSchema=True)

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table michelin.circuits

# COMMAND ----------

# DBTITLE 1,Transform
df1=df\
.withColumnsRenamed({"circuitId":"circuit_id","circuitRef":"circuit_ref","lat":"latitude","lng":"longitude","alt":"altitude"})\
.withColumn("ingestion_date",current_date())\
.drop("url")
#df1.write.saveAsTable("michelin.circuits")



# COMMAND ----------

# DBTITLE 1,Write
df1.write.mode("overwrite").saveAsTable("michelin.circuits")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from michelin.circuits
