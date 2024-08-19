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

# Ensure the bucket exists
if not minio_client.bucket_exists(bucket_name):
    minio_client.make_bucket(bucket_name)

# Create a simple DataFrame
df = pd.DataFrame({
    "column1": [1, 2, 3],
    "column2": ["a", "b", "c"]
})

# Convert DataFrame to CSV
csv_data = df.to_csv(index=False)

# Upload CSV file to MinIO
minio_client.put_object(
    bucket_name,
    csv_file_name,
    BytesIO(csv_data.encode('utf-8')),
    length=len(csv_data),
    content_type='application/csv'
)

print(f"CSV file '{csv_file_name}' has been created and saved to the bucket '{bucket_name}'")
