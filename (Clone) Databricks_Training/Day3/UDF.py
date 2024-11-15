# Databricks notebook source
# MAGIC %sql
# MAGIC create function function_name(para datatype)
# MAGIC returns datatype
# MAGIC return logic

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table michelin.emp2;
# MAGIC create table michelin.emp2 (id int ,name string, age int);
# MAGIC insert into table michelin.emp2 values(1,'varsha',25),(2,'geeta',29),(3,'ashu',17),(4,'tanu',16),(5,'laxmi',18)

# COMMAND ----------

# MAGIC %sql
# MAGIC create function michelin.voter_eligible(age int)
# MAGIC returns string
# MAGIC return case
# MAGIC when age>18 then 'eligible'
# MAGIC else 'you are not eligible for voting'
# MAGIC end
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * ,michelin.voter_eligible(age) as eligibility from michelin.emp2

# COMMAND ----------


