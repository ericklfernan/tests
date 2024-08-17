git clone https://github.com/ericklfernan/tests.git

mkdir -p /mnt/data/input
mkdir -p /mnt/data/output
sudo chmod -R 777 /mnt/data/output

docker compose -f ./tests/test5-kms/spark.yml up -d



---------------------------------------------------------------------------------------------------------------------------------------
For minIO
Create these directories on your docker swarm manager (this is for simulation only, in real life, minIO will nt be created in docker)
mkdir -p /mnt/data/minio1 /mnt/data/minio2 /mnt/data/minio3

Check the minio.yml and be sure to mount or map those locations to a common mount point i.e., /mnt/data/minio1:/data, /mnt/data/minio2:/data, /mnt/data/minio3:/data
---------------------------------------------------------------------------------------------------------------------------------------
Now run the docker compose -f ./tests/test5-kms/minio.yml up -d
Check the mount point if working.
    Go inside container
        docker exec -it minio1 /bin/bash
            cd /data
            touch erick.csv
            exit
    Go to your swarm manager
        cd /mnt/data/minio1
        ls
        you should see here the erick.csv
When you found the erick.csv then the mount point is working.
---------------------------------------------------------------------------------------------------------------------------------------
Spark
Create /mnt/data/spark-app on host machine
Put here the spark application script.


    

docker compose -f ./tests/test5-kms/minio.yml up -d
docker compose -f ./tests/test5-kms/spark.yml up -d
docker compose -f ./tests/test5-kms/kafka.yml up -d

docker exec -it --user root spark-master /bin/bash

sudo chmod -R 777 /mnt/data/ouput