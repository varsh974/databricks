# Databricks notebook source
# DBTITLE 1,python
print("Databricks day 1")

# COMMAND ----------

# MAGIC %sql
# MAGIC create database test;
# MAGIC create table test.mich_emp (id int ,name string);
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into table test.mich_emp values (1,'Varsha'),(2,'Sneha')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from test.mich_emp;
