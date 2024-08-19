from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from minio import Minio
from io import BytesIO

# Initialize Spark session
spark = SparkSession.builder \
    .appName("KafkaSparkConsumer") \
    .getOrCreate()

# Read from Kafka topic
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "events") \
    .load()

# Convert Kafka value to string
df = df.selectExpr("CAST(value AS STRING)")

# Process JSON fields
df = df.withColumn("name", get_json_object(col("value"), "$.name")) \
       .withColumn("address", get_json_object(col("value"), "$.address")) \
       .withColumn("created_at", get_json_object(col("value"), "$.created_at"))

# Micro-batch the data every 5 seconds and write to MinIO
def write_to_minio(df, epoch_id):
    pandas_df = df.toPandas()
    minio_client = Minio(
        "minio:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )
    bucket_name = "spark-output"
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
    csv_data = pandas_df.to_csv(index=False)
    minio_client.put_object(
        bucket_name,
        f"batch_{epoch_id}.csv",
        data=BytesIO(csv_data.encode('utf-8')),
        length=len(csv_data),
        content_type='application/csv'
    )

# Write the micro-batched data to MinIO
query = df.writeStream \
    .foreachBatch(write_to_minio) \
    .trigger(processingTime="5 seconds") \
    .start()

query.awaitTermination()
