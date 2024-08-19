docker swarm init
docker node ls


create additional workers
docker run -d --privileged --name worker1 --hostname worker1 docker:19.03-dind
docker run -d --privileged --name worker2 --hostname worker2 docker:19.03-dind
docker run -d --privileged --name worker2 --hostname worker3 docker:19.03-dind

get the ip of the manager
docker node ls
docker inspect docker-desktop

get the token 
docker swarm join-token manager
manager: SWMTKN-1-4zqtdcts84z61nmwq77inihxyijevqsqwmhd8dgqc66cyct18u-2vmtr806n7vismpgppx6k9f3v
docker exec -it worker1 docker swarm join --token SWMTKN-1-4zqtdcts84z61nmwq77inihxyijevqsqwmhd8dgqc66cyct18u-2vmtr806n7vismpgppx6k9f3v 192.168.65.3:2377

get the token 
docker swarm join-token worker
worker: SWMTKN-1-4zqtdcts84z61nmwq77inihxyijevqsqwmhd8dgqc66cyct18u-182c0noj9ubnmv013563t10om
docker exec -it worker2 docker swarm join --token SWMTKN-1-4zqtdcts84z61nmwq77inihxyijevqsqwmhd8dgqc66cyct18u-182c0noj9ubnmv013563t10om 192.168.65.3:2377
docker exec -it worker3 docker swarm join --token SWMTKN-1-4zqtdcts84z61nmwq77inihxyijevqsqwmhd8dgqc66cyct18u-182c0noj9ubnmv013563t10om 192.168.65.3:2377
