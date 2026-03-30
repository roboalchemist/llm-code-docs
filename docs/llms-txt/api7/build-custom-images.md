# Source: https://docs.api7.ai/apisix/install/docker/build-custom-images.md

# Build Your Own Docker Images

You can build your own Docker images and customize them for your needs.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [make](https://www.gnu.org/software/make) to build your Docker image from the makefile.

## Clone Repository[â](#clone-repository "Direct link to Clone Repository")

Clone the repository and navigate into the repository:

```
git clone https://github.com/apache/apisix-docker.git
cd apisix-docker
```

## Build a Docker Image[â](#build-a-docker-image "Direct link to Build a Docker Image")

Build a Docker image from a release:

```
APISIX_VERSION=3.15.0       # specify a release version
DISTRO=ubuntu              # ubuntu, debian, centos, or redhat
make build-on-$DISTRO
```

The make command builds a Docker image with this [Dockerfile](https://github.com/apache/apisix-docker/blob/master/ubuntu/Dockerfile). You can further customize the relevant files for your needs.

## Check Docker Image[â](#check-docker-image "Direct link to Check Docker Image")

List all Docker images:

```
docker images
```

You should see the list including the image built in the last step:

```
REPOSITORY     TAG            IMAGE ID       CREATED              SIZE
apache/apisix  3.15.0-ubuntu   422e111797f3   About a minute ago   337MB
```
