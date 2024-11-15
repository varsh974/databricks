# Databricks notebook source
# MAGIC %md
# MAGIC Dataframe

# COMMAND ----------

df=spark.read.csv("dbfs:/FileStore/tables/Michelin/customers.csv")

# COMMAND ----------

df.show()


# COMMAND ----------

df.display()

# COMMAND ----------

df=spark.read.option("header",True).option("inferSchema",True).csv("dbfs:/FileStore/tables/Michelin/customers.csv")

# COMMAND ----------

df.display()

# COMMAND ----------

df=spark.read.csv("dbfs:/FileStore/tables/Michelin/customers.csv",header=True,inferSchema=True)

# COMMAND ----------

df.write.saveAsTable("test.customer")
