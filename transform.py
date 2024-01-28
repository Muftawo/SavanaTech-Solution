
from pyspark.sql import SparkSession
from pyspark.sql import functions as F




# Create a Spark session
spark = SparkSession.builder.appName("ScytaleTransform").getOrCreate()

# Read JSON files into a DataFrame
org_name = "your_org_name"  # Replace with your organization name
repo_data_path = f"/content/Scytale-exercise/scytale-repo3/data.json"
df = spark.read.json(repo_data_path, multiLine=True)


# Extract relevant information from the JSON structure
df_transformed = df.select(
    F.col("name").alias("Organization Name"),
    F.col("id").alias("repository_id"),
    F.col("name").alias("Organization Name"),
    F.col("login").alias("repository_owner"),
    F.size("pull_requests").alias("num_prs"),
    F.size(F.expr("filter(pull_requests, pr -> pr.state == 'merged')")).alias("num_prs_merged"),

)


df_transformed = df_transformed.withColumn(
    "is_compliant",
    (F.col("num_prs") == F.col("num_prs_merged")) & (F.col("repository_owner").contains("scytale")),
)


# Stop the Spark session
spark.stop()