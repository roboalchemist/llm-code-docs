# Source: https://docs.api7.ai/enterprise/deployment/docker.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/deployment/docker.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/deployment/docker.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/deployment/docker.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/deployment/docker.md

# Source: https://docs.api7.ai/enterprise/3.8.x/deployment/docker.md

# Source: https://docs.api7.ai/enterprise/3.7.x/deployment/docker.md

# Source: https://docs.api7.ai/enterprise/3.6.x/deployment/docker.md

# Source: https://docs.api7.ai/enterprise/3.5.x/deployment/docker.md

# Source: https://docs.api7.ai/enterprise/3.4.x/deployment/docker.md

# Source: https://docs.api7.ai/enterprise/3.3.x/deployment/docker.md

# Source: https://docs.api7.ai/apisix/install/docker.md

# Source: https://docs.api7.ai/enterprise/3.3.x/deployment/docker.md

# Source: https://docs.api7.ai/apisix/install/docker.md

# Install APISIX with Docker

APISIX offers Docker images that make it easy to deploy and manage APISIX in a containerized environment, providing the benefits of consistency, portability, and flexibility.

This document provides the installation steps for deploying APISIX with Docker in standalone and decoupled [deployment modes](https://docs.api7.ai/apisix/production/deployment-modes.md).

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Install [Docker](https://docs.docker.com/get-docker/).
* Install [cURL](https://curl.se/) to send requests to the services for validation.

You will need administrator privileges for some of the following steps.

## Standalone Mode[â](#standalone-mode "Direct link to Standalone Mode")

The following steps cover how to install APISIX in [file-driven standalone mode](https://docs.api7.ai/apisix/production/deployment-modes.md#file-driven) using Docker, while using the YAML config provider and `apisix.yaml` for gateway configuration.

The section provides one approach to achieve data persistence with [Docker volume](https://docs.docker.com/storage/volumes). Adjust the approach accordingly to integrate with your infrastructure.

### Create Configuration Files on Host[â](#create-configuration-files-on-host "Direct link to Create Configuration Files on Host")

To achieve data persistence, create a directory for configuration file and create [configuration files](https://docs.api7.ai/apisix/reference/configuration-files.md) `config.yaml` and `apisix.yaml` within:

```
mkdir ~/conf
touch ~/conf/config.yaml
echo '
routes:
  -
    id: example-route-to-httpbin
    uri: /anything/test
    upstream:
      nodes:
        httpbin.org: 1
      type: roundrobin
#END
' > ~/conf/apisix.yaml
```

â¶ `config.yaml`: this file will be initialized in container at startup. It is created on host as an empty file to mount to the container and synchronize with the file content in the container.

â· `apisix.yaml`: this file does not exist in container at startup. It is created on host with an example route to mount to the container and avoid any configuration error that may occur.

### Create `apisix` User on Host[â](#create-apisix-user-on-host "Direct link to create-apisix-user-on-host")

If you use a Debian or Ubuntu-based APISIX Docker image, to volume mount files created in the previous step with the appropriate permissions, you should create an `apisix` user with the same gid and uid as the `apisix` user in the container and change the owner of the configuration files to `apisix`.

Create a user `apisix` with uid and gid 636:

```
groupadd --system --gid 636 apisix
useradd --system --gid apisix --no-create-home --shell /usr/sbin/nologin --uid 636 apisix
```

Change the ownership of the directory with configuration files to `apisix`:

```
chown -R apisix:apisix ~/conf
```

### Install APISIX[â](#install-apisix "Direct link to Install APISIX")

Specify the [Docker image tag](https://hub.docker.com/r/apache/apisix/tags) in an environment variable:

```
TAG=3.15.0-ubuntu
```

Start APISIX in the standalone mode with configuration files mounted to the container:

```
docker run -d \
  --name apisix-standalone \
  -p9080:9080 -p9443:9443 -p9090:9092 \
  -e APISIX_STAND_ALONE=true \
  --mount type=bind,source="$(pwd)"/conf/apisix.yaml,target=/usr/local/apisix/conf/apisix.yaml \
  --mount type=bind,source="$(pwd)"/conf/config.yaml,target=/usr/local/apisix/conf/config.yaml \
  apache/apisix:${TAG}
```

### Verify Installation[â](#verify-installation "Direct link to Verify Installation")

Send a request to APISIX to see if it is running:

```
curl -Is "http://127.0.0.1:9080" | grep Server
```

If everything is ok, you should see the server version number, such as the following:

```
Server: APISIX/3.15.0
```

### Verify Data Persistence[â](#verify-data-persistence "Direct link to Verify Data Persistence")

In the previous steps, you have mounted `apisix.yaml` and `config.yaml` on the host to the corresponding files in the container.

Send a request to the pre-configured route in `apisix.yaml`:

```
curl -i "http://127.0.0.1:9080/anything/test"
```

You should see an `HTTP/1.1 200 OK` response similar to the following:

```
{
  ...
  "headers": {
    ...
  }, 
  "json": null, 
  "method": "GET", 
  "origin": "172.17.0.1, 34.xx.xx.xx", 
  "url": "http://127.0.0.1/anything/test"
}
```

You can modify configurations in `apisix.yaml` and `config.yaml` on host, which update the configurations in the container.

Changes to `apisix.yaml` will be loaded automatically to APISIX, whereas changes to `config.yaml` will require a reload of APISIX to take effect. See [configuration files](https://docs.api7.ai/apisix/reference/configuration-files.md) for more details.

## Decoupled Mode[â](#decoupled-mode "Direct link to Decoupled Mode")

The following steps cover how to install APISIX in decoupled mode using Docker and provide one approach to achieve data persistence with [Docker volume](https://docs.docker.com/storage/volumes). Adjust the approach accordingly to integrate with your infrastructure.

In decoupled mode, two APISIX instances should be deployed: one being the data plane (DP) and the other one being the control plane (CP).

### Create Configuration Files on Host[â](#create-configuration-files-on-host-1 "Direct link to Create Configuration Files on Host")

To achieve data persistence, create separate directories for DP and CP configuration files:

```
for instance in {cp,dp}; do
  mkdir -p ~/conf/"$instance"
  touch ~/conf/"$instance"/config.yaml
done
```

Create the [configuration files](https://docs.api7.ai/apisix/reference/configuration-files.md) `config.yaml` for DP instance:

```
echo '
deployment:
  role: data_plane
  role_data_plane:
    config_provider: etcd
#END
' > ~/conf/dp/config.yaml
```

Create the [configuration files](https://docs.api7.ai/apisix/reference/configuration-files.md) `config.yaml` for CP instance:

```
echo '
deployment:
  role: control_plane
  role_control_plane:
    config_provider: etcd
  admin:
    admin_key_required: true
    allow_admin:
      - 0.0.0.0/0
    admin_key:
      -
        name: admin
        key: Sup3rs3cretWr1teK3y   # replace with your write key
        role: admin
      -
        name: viewer
        key: Sup3rs3cretR3adK3y    # replace with your read key
        role: viewer
#END
' > ~/conf/cp/config.yaml
```

### Create `apisix` User on Host[â](#create-apisix-user-on-host-1 "Direct link to create-apisix-user-on-host-1")

If you use a Debian or Ubuntu-based APISIX Docker image, to volume mount files created in the previous step with the appropriate permissions, you should create an `apisix` user with the same gid and uid as the `apisix` user in the container and change the owner of the configuration files to `apisix`.

Create a user `apisix` with uid and gid 636:

```
groupadd --system --gid 636 apisix
useradd --system --gid apisix --no-create-home --shell /usr/sbin/nologin --uid 636 apisix
```

Change the ownership of the directory with configuration files to `apisix`:

```
chown -R apisix:apisix ~/conf
```

### Create a Docker Network[â](#create-a-docker-network "Direct link to Create a Docker Network")

Create a Docker bridge network for APISIX and etcd containers:

```
DOCKER_NETWORK_NAME="apisix-net"
docker network create -d bridge ${DOCKER_NETWORK_NAME}
```

### Install etcd[â](#install-etcd "Direct link to Install etcd")

Start the etcd container in the Docker network:

```
ETCD_IMAGE_TAG="3.5.7"   # >= 3.4.0
ETCD_CONTAINER_NAME="etcd-$ETCD_IMAGE_TAG"
ETCD_HOST=0.0.0.0
ETCD_PORT=2379

docker run -d \
  --name ${ETCD_CONTAINER_NAME} \
  --network=${DOCKER_NETWORK_NAME} \
  -e ALLOW_NONE_AUTHENTICATION=yes \
  -e ETCD_ADVERTISE_CLIENT_URLS=http://${ETCD_HOST}:${ETCD_PORT} \
  bitnami/etcd:${ETCD_IMAGE_TAG}
```

### Install APISIX[â](#install-apisix-1 "Direct link to Install APISIX")

Specify the APISIX [Docker image tag](https://hub.docker.com/r/apache/apisix/tags) in an environment variable:

```
TAG=3.15.0-ubuntu
```

Start an APISIX container as the **data plane** with configuration files mounted to the container. Map port `9080` for HTTP traffic and port `9443` for HTTPS traffic:

```
docker run -d \
  --name apisix-decoupled-dp \
  -p9080:9080 -p9443:9443 \
  --network=${DOCKER_NETWORK_NAME} \
  --mount type=bind,source="$(pwd)"/conf/dp/config.yaml,target=/usr/local/apisix/conf/config.yaml \
  -e APISIX_DEPLOYMENT_ETCD_HOST="[\"http://${ETCD_CONTAINER_NAME}:${ETCD_PORT}\"]" \
  apache/apisix:${TAG}
```

Start an APISIX container as the **control plane** with configuration files mounted to the container. Map port `9180` for Admin API and port `9090` for Control API:

```
docker run -d \
  --name apisix-decoupled-cp \
  -p9180:9180 -p9090:9092 \
  --network=${DOCKER_NETWORK_NAME} \
  --mount type=bind,source="$(pwd)"/conf/cp/config.yaml,target=/usr/local/apisix/conf/config.yaml \
  -e APISIX_DEPLOYMENT_ETCD_HOST="[\"http://${ETCD_CONTAINER_NAME}:${ETCD_PORT}\"]" \
  apache/apisix:${TAG}
```

### Verify Installation[â](#verify-installation-1 "Direct link to Verify Installation")

Send a request to APISIX to see if it is running:

```
curl -Is "http://127.0.0.1:9080" | grep Server
```

If everything is ok, you should see the server version number, such as the following:

```
Server: APISIX/3.15.0
```

### Verify Data Persistence[â](#verify-data-persistence-1 "Direct link to Verify Data Persistence")

In the previous steps, you have mounted `config.yaml` files on the host to the corresponding files in the containers.

Create a sample route by sending a request to the CP APISIX instance:

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes" -X PUT \
  -H "X-API-KEY: Sup3rs3cretWr1teK3y" \
  -d '{
    "id": "decoupled-test",
    "uri": "/anything/test",
    "upstream": {
      "type": "roundrobin",
      "nodes": {
        "httpbin.org:80": 1
      }
    }
  }'
```

Send a request to the route to verify:

```
curl -i "http://127.0.0.1:9080/anything/test"
```

You should see an `HTTP/1.1 200 OK` response.

You can modify configurations in `config.yaml` on host, which update the configurations in the container. Changes to `config.yaml` will require a reload of APISIX to take effect. See [configuration files](https://docs.api7.ai/apisix/reference/configuration-files.md) for more details.
