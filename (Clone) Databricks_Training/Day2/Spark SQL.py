# Databricks notebook source
# MAGIC %sql
# MAGIC -- Querying Raw files
# MAGIC --select * from file_format.`path`

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table michelin.constructor_sql;
# MAGIC create table michelin.constructor_sql as 
# MAGIC select *, current_timestamp() as ingestion_date from json.`/Volumes/va_michelin/michelin/raw/constructors.json`

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from michelin.constructor_sql
