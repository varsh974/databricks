# Databricks notebook source
# MAGIC %sql
# MAGIC create table michelin.emp (id int ,name string)

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended michelin.emp

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into table michelin.emp values (1,'varsha')

# COMMAND ----------

# MAGIC %sql 
# MAGIC describe detail michelin.emp

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history michelin.emp

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into table michelin.emp values (2 ,'Rohini')

# COMMAND ----------

# MAGIC %sql
# MAGIC describe detail michelin.emp

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from michelin.emp version as of 2

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history michelin.emp

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into table michelin.emp values  (3,'Geet')

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into table michelin.emp values(4,'neha'),(5,'jay')

# COMMAND ----------

# MAGIC %sql
# MAGIC delete from michelin.emp where name='jay'

# COMMAND ----------

# MAGIC %sql
# MAGIC update michelin.emp 
# MAGIC set name ='neha' where name ='jay'

# COMMAND ----------

# MAGIC %sql
# MAGIC describe detail michelin.emp

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history michelin.emp

# COMMAND ----------

# MAGIC %sql
# MAGIC optimize  michelin.emp
# MAGIC zorder by (id)

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history michelin.emp

# COMMAND ----------

# MAGIC %sql
# MAGIC vacuum michelin.emp
# MAGIC  
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC vacuum michelin.emp retain 500 hours

# COMMAND ----------


