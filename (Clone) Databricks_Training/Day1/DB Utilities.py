# Databricks notebook source
dbutils.fs.help()

# COMMAND ----------

# MAGIC %fs

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

# MAGIC %fs ls
# MAGIC

# COMMAND ----------

# MAGIC %fs ls /FileStore/tables/Michelin

# COMMAND ----------

dbutils.fs.mkdirs("/FileStore/tables/Michelin_Raw")

# COMMAND ----------

dbutils.fs.cp("/FileStore/tables/Michelin/customers.csv" ,"/FileStore/tables/Michelin_Raw")

# COMMAND ----------

dbutils.fs.rm("/FileStore/tables/Michelin/customers.xlsx")

# COMMAND ----------

dbutils.fs.cp("/FileStore/tables/Michelin_Raw/customers.csv","/FileStore/tables/Michelin")

# COMMAND ----------

dbutils.fs.ls("/FileStore/tables/Michelin")
