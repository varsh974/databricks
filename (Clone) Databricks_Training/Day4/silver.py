# Databricks notebook source
# MAGIC %run /Workspace/Users/varshasalunke9741@gmail.com/Databricks_Training/Day4/include

# COMMAND ----------

df=spark.table("michelin.bronze.sales")
df1=df.dropDuplicates().dropna()
df1.write.mode("overwrite").saveAsTable("michelin.silver.sales")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from michelin.silver.sales

# COMMAND ----------

# MAGIC %sql
# MAGIC create table michelin.silver.products(
# MAGIC   product_id int,
# MAGIC   product_name string
# MAGIC
# MAGIC
# MAGIC
# MAGIC )
# MAGIC

# COMMAND ----------


