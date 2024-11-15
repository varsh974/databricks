# Databricks notebook source
df=spark.read.json("dbfs:/FileStore/tables/Michelin/1.json")

# COMMAND ----------

df.display()

# COMMAND ----------

df.write.saveAsTable("test.json")
