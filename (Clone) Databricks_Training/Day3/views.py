# Databricks notebook source
# MAGIC %sql
# MAGIC create view michelin_circuits_country
# MAGIC as (select country, count(country) as count from michelin.circuits group by country order by count desc)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from michelin_circuits_country

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace temp view  country_temp as
# MAGIC (select country,location, count(country) as count from michelin.circuits group by country,location order by count desc)
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace global temp view country_global_temp as
# MAGIC (select country,location, count(country) as count from michelin.circuits group by country,location order by count desc)

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW VIEWS IN global_temp
