git clone https://github.com/ericklfernan/tests.git

mkdir -p /mnt/data/input
mkdir -p /mnt/data/output

sudo chown -R $(id -u):$(id -g) /mnt/data/output

sudo chmod -R 777 /mnt/data/output

cp ./tests/test5-kms/script/spark02.py /mnt/data/
cp ./tests/test5-kms/input/data.csv /mnt/data/input/

docker compose -f ./tests/test5-kms/docker/spark.yml up -d

docker exec -it spark-master /opt/bitnami/spark/bin/spark-submit /mnt/data/spark02.py

# 1 Stop and Remove All Running Containers
docker stop $(docker ps -q)

# 2 Next, remove all containers (both running and stopped)
docker rm $(docker ps -aq)

# 3 Once all containers are stopped and removed, you can remove all Docker images:
docker rmi $(docker images -q)

# 4 If you also want to clean up unused Docker volumes (not attached to any container)
docker volume prune -f

# 5 To clean up any unused Docker networks
docker network prune -f

---------------------------------------------------------------------------
# Here is how you can combine all the 5 commands into 1 command

docker stop $(docker ps -q) && docker rm $(docker ps -aq) && docker rmi $(docker images -q) && docker volume prune -f && docker network prune -f

or 

nano ~/.bashrc
# add this
alias clean='docker stop $(docker ps -q) && docker rm $(docker ps -aq) && docker rmi $(docker images -q) && docker volume prune -f && docker network prune -f'
# apply the changes
source ~/.bashrc
# now you can run by
clean



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

sudo chmod -R 777 /mnt/data/output