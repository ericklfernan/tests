# download the script from github
git clone https://github.com/ericklfernan/test1.git

# run the yml file to create the image, the container and then run the container
docker compose -f ./test1/app.yml up -d

# see the container logs
docker logs cont_x

# remove the container
docker container rm cont_x

# remove the image
docker image rm -f image_x

# remove the files
rm -r test1/
  
# shell command
docker exec -it cont_x sh

# re run a container
docker run -itd --name cont_x1 image_x
docker run -itd --mount type=bind,source=/root/erick,target=/root --name cont_x1 image_x

THIS ONE WORKS
1. mkdir erick
2. git clone https://github.com/ericklfernan/test1.git
3. docker compose -f ./test1/app.yml up -d 
-----------------------------------------------------
.. docker logs cont_x
.. docker container rm cont_x
.. docker image rm -f image_x
.. rm -r test1/
.. # re run a container
.. docker run -itd --name cont_x1 image_x
.. docker run -itd --mount type=bind,source=/root/erick,target=/root --name cont_x1 image_x
-----------------------------------------------------
4. docker exec -it cont_x sh
5. cd /root
6. ls
7. exit
8. cd /erick
9. ls
