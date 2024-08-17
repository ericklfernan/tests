from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# Initialize Spark session
spark = SparkSession.builder.appName("AggregateCSV").getOrCreate()

# Define file paths
input_path  = "/mnt/data/input/data.csv"
output_path = "/mnt/data/output/result"

# Read the CSV file
df = spark.read.csv(input_path, header=True, inferSchema=True)

# print schema
df.printSchema()

# Perform some aggregation (e.g., calculate the average of a column)
# aggregated_df = df.groupBy("name").agg(avg("age").alias("AverageValue"))

# Write the aggregated data back to CSV
# aggregated_df.write.csv(output_path, header=True, mode="overwrite")
df.write.csv(output_path, header=True, mode="overwrite")

# Stop the Spark session
spark.stop()