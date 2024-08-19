import os
import pandas as pd
from minio import Minio
from io import BytesIO

# Initialize MinIO client
minio_client = Minio(
    "minio:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

bucket_name = "example-bucket"
csv_file_name = "example.csv"

# Read CSV file from MinIO
response = minio_client.get_object(bucket_name, csv_file_name)
csv_data = pd.read_csv(BytesIO(response.data))

print(f"Read the following data from '{csv_file_name}' in the bucket '{bucket_name}':")
print(csv_data)
