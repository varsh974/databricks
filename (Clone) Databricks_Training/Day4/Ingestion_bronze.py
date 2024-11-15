# Databricks notebook source
# MAGIC %run /Workspace/Users/varshasalunke9741@gmail.com/Databricks_Training/Day4/include

# COMMAND ----------

dbutils.widgets.text("source","")
source_file_name=dbutils.widgets.get("source")

dbutils.widgets.text("catalog","")
catalog_name=dbutils.widgets.get("catalog")

dbutils.widgets.text("schema","")
schema_name=dbutils.widgets.get("schema")




 

# COMMAND ----------

display(source_file_name)
display(catalog_name)
display(schema_name)

# COMMAND ----------

df_sales=spark.read.csv(f"{input_path}{source_file_name}",header=True,inferSchema=True)
df_sales_final=add_ingestion_col(df_sales)
df_sales_final.write.mode("overwrite").saveAsTable("bronze.sales")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from `${catalog}`.`${schema}`.`${source}`
