

It is important grant permission to the volume prior.

mkdir -p /var/lib/docker/volumes/minio_data/_data

sudo chown -R root:root /var/lib/docker/volumes/minio_data/_data
or 
sudo chmod -R 777 /var/lib/docker/volumes/minio_data/_data


docker-compose build

docker-compose up -d

docker-compose logs -f kafka-producer
docker-compose logs -f spark-consumer

docker-compose up -d --scale kafka-producer=3
docker-compose up -d --scale spark-consumer=3

GIT CLONE
ASSUMPTION 
git is using main as branch

LOCAL
git add .
git commit -m "your comment"
git push -u origin main

REMOTE
git clone https://github.com/ericklfernan/tests.git

or to update existing local copy

git pull origin main