from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StringType, TimestampType

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Kafka to MinIO") \
    .master("spark://spark-master:7077") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1") \
    .getOrCreate()

# Read from Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka1:9092,kafka2:9093,kafka3:9094") \
    .option("subscribe", "events") \
    .option("startingOffsets", "earliest") \
    .load()

df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Process and write to MinIO
df = df.withColumn("value", from_json(col("value").cast("string"), schema))
df = df.withColumn("window", window(col("event_time"), "1 minute"))
df = df.groupBy("window").count()

query = df.writeStream \
    .outputMode("append") \
    .format("csv") \
    .option("path", "s3a://minio-bucket/spark-output/") \
    .option("checkpointLocation", "/tmp/checkpoint/") \
    .start()

query.awaitTermination()
