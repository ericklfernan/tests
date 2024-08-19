It is important grant permission to the volume prior.

mkdir -p /var/lib/docker/volumes/minio_data/_data

sudo chown -R root:root /var/lib/docker/volumes/minio_data/_data
or 
sudo chmod -R 777 /var/lib/docker/volumes/minio_data/_data


docker-compose build

docker-compose up -d minio

docker-compose up writer

docker-compose up reader

docker volume inspect minio-example_minio_data

docker logs minio-example-reader-1
docker logs minio-example-writer-1

docker-compose up -d --scale writer=3

ls -al /var/lib/docker/volumes/minio-example_minio_data/_data/example-bucket/example.csv/

cat /var/lib/docker/volumes/minio-example_minio_data/_data/example-bucket/example.csv/xl.meta
