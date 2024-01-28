import os
from pyspark.sql import SparkSession
from pyspark.sql import functions as F


# start Spark session
spark = SparkSession.builder.appName("ScytaleTransform").getOrCreate()

# Read  all JSON files into a  pyspark DataFrame
org_name = 'Scytale-exercise'
json_files_path = [os.path.join(org_name, repo_name, 'data.json') for repo_name in os.listdir(org_name)]
df = spark.read.option("multiline","true").json(json_files_path)

# start data transformation
df_transformed = df.select(
    F.col("name").alias("Organization Name"),
    F.col("id").alias("repository_id"),
    F.col("name").alias("Organization Name"),
    F.col("login").alias("repository_owner"),
    F.size("pull_requests").alias("num_prs"),
    F.size(F.expr("filter(pull_requests, pr -> pr.state == 'merged')")).alias("num_prs_merged"),

)

#add is_complaint field
df_transformed = df_transformed.withColumn(
    "is_compliant",
    (F.col("num_prs") == F.col("num_prs_merged")) & (F.col("repository_owner").contains("scytale")),
)

#save resulting data as a parquet
parquet_output_path = f"{org_name}/solution"
df_transformed.write.parquet(parquet_output_path)

spark.stop()