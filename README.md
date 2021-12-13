# fastapi-filestore
This repository is FastAPI Filestore APP
    
# Requirement for FastAPI
* Python >= 3
* FastAPI >= 0.70.0 

# Container Information
* DockerHub : [https://hub.docker.com/r/han0495/fastapi-filestore](https://hub.docker.com/r/han0495/fastapi-filestore)   
* Quay.io : [https://quay.io/repository/chhanz/fastapi-filestore](https://quay.io/repository/chhanz/fastapi-filestore)   
   
# Tags
+ `latest` : This image is latest.
   
# Default ID/PASSWD
```
ENV FILESTORE_ID="root" \
    FILESTORE_PASS="testtest"
```
if you want change id/passwd,    
  * run `docker/podman`      
     ```bash
     $ podman run -e FILESTORE_ID="changeid" -e FILESTORE_PASS="changeme" ....
     or
     $ docker run -e FILESTORE_ID="changeid" -e FILESTORE_PASS="changeme" ....
     ```
   
# Run
```bash
$ podman run -d --name filestore quay.io/chhanz/fastapi-filestore
or
$ docker run -d --name filestore docker.io/han0495/fastapi-filestore
```
   
# Mount Volume
if you want mount volume,   
  * run `docker/podman`     
     ```bash
     $ podman -v /root/upload:/usr/src/app/upload ....
     or
     $ docker -v /root/upload:/usr/src/app/upload ....
     ```
   
# Expose Port
if you want expose port,
  * run `docker/podman`
    ```bash
    $ podman -p 30020:9090 ....
    or
    $ docker -p 30020:9090 ....
    ```
    
# Dockerfile
```docker
FROM python:3.10.1-alpine3.15
MAINTAINER han0495@gmail.com

ENV FILESTORE_ID="root" \
    FILESTORE_PASS="testtest"

WORKDIR /usr/src/app

COPY . .
RUN mkdir /usr/src/app/upload \
    && pip install --no-cache-dir -r requirements.txt

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9090" ]
```

# Build
```bash
$ git clone https://github.com/chhanz/fastapi-filestore.git
$ cd fastapi-filestore
$ docker build -t fastapi-filestore .
```
   
# How to use 'filecmd'
* [Follow to the page](filecmd.md)   

# Preview 'index'
![](/docs/img/index.png)
