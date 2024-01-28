import os
from pyspark.sql import SparkSession
from pyspark.sql import functions as F


# start Spark session
spark = SparkSession.builder.appName("ScytaleTransform").getOrCreate()

# Read  all JSON files into a  pyspark DataFrame
org_name = 'Scytale-exercise'
base_dir= f"{org_name}/repos/"

# get all data.json paths in a list and read into dataframe
json_files_path = [os.path.join(base_dir, repo_name, 'data.json') for repo_name in os.listdir(base_dir)]
df = spark.read.json(json_files_path,multiLine=True)


# start data transformation
df_transformed = df.select(
    F.col("org").alias("Organization Name"),
    F.col("id").alias("repository_id"),
    F.col("name").alias("repo Name"),
    F.col("login").alias("repository_owner"),
    #size of list is equal to nuber of prs
    F.size("pull_requests").alias("num_prs"),
    #count number of merges prs
    F.size(F.expr("filter(pull_requests, pr -> pr.state == 'merged')")).alias("num_prs_merged"),
)

#add is_complaint field
df_transformed = df_transformed.withColumn(
    "is_compliant",
    (F.col("num_prs") == F.col("num_prs_merged")) & (F.col("repository_owner").contains("scytale")),
)

#save resulting data as a parquet
parquet_output_path = f"{org_name}/solution.parquet"
df_transformed.write.mode("overwrite").parquet(parquet_output_path)

spark.stop()