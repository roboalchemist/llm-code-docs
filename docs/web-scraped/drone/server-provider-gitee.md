# Source: https://docs.drone.io/server/provider/gitee/

Title: Gitee | Drone

URL Source: https://docs.drone.io/server/provider/gitee/

Markdown Content:
This article explains how to install the Drone server for Gitee. The server is packaged as a minimal Docker image distributed on [DockerHub](https://hub.docker.com/r/drone/drone).

Preparation
-----------

Create an OAuth Application
---------------------------

Create a `Gitee OAuth application`. The `Consumer Key` and `Consumer Secret` are used to authorize access to Gitee resources.

The authorization callback URL must match the below format and path, and must use your exact server scheme and host.

![Image 1: Application Create](https://docs.drone.io/screenshots/gitee_token_create.png)![Image 2: Application View](https://docs.drone.io/screenshots/gitee_token_created.png)

Create a shared secret to authenticate communication between runners and your central Drone server.

You can use openssl to generate a shared secret:

```
$ openssl rand -hex 16
bea26a2221fd8090ea38720fc445eca6
```

Download
--------

The Drone server is distributed as a lightweight Docker image. The image is self-contained and does not have any external dependencies.

```
$ docker pull drone/drone:2
```

Configuration
-------------

The Drone server is configured using environment variables. This article references a subset of configuration options, defined below. See [Configuration](https://docs.drone.io/server/reference/) for a complete list of configuration options.

*   **DRONE_GITEE_CLIENT_ID**Required string value provides your `Gitee OAuth Client ID`.
*   **DRONE_GITEE_CLIENT_SECRET**Required string value provides your `Gitee OAuth Client Secret`.
*   **DRONE_GITEE_SERVER**Optional url value provides Gitee server address. The default value is the gitee.com server address at `https://gitee.com`.
*   **DRONE_GITEE_API_SERVER**Optional string value provides Gitee api server address. The default value is `https://gitee.com/api/v5`.
*   **DRONE_RPC_SECRET**Required string value provides the shared secret generated in the previous step. This is used to authenticate the rpc connection between the server and runners. The server and runner must be provided the same secret value.
*   **DRONE_SERVER_HOST**Required string value provides your external hostname or IP address. If using an IP address you may include the port. For example, `drone.domain.com`
*   **DRONE_SERVER_PROTO**Required string value provides your external protocol scheme. This value should be set to `http` or `https`. This field defaults to https if you configure ssl or acme.

Start the Server
----------------

The server container can be started with the below command. The container is configured through environment variables. _Remember to replace the placeholder values below with the appropriate values._

```
1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
``````
docker run \
  --volume=/var/lib/drone:/data \
  --env=DRONE_GITEE_CLIENT_ID=f7018cdd7c2a2515eb0cc3eeea039a3aeda0991a520c9e6f7eca37b97761de20 \
  --env=DRONE_GITEE_CLIENT_SECRET=a29f1465460f620d1238b6ebf207ae6778a6bfd074b3c7befe72d5f9647ed02c \
  --env=DRONE_RPC_SECRET=super-duper-secret \
  --env=DRONE_SERVER_HOST=drone.domain.com \
  --env=DRONE_SERVER_PROTO=https \
  --publish=80:80 \
  --publish=443:443 \
  --restart=always \
  --detach=true \
  --name=drone \
  drone/drone:2
```

Install Runners
---------------

Once your server is up and running you will need to install runners to execute your build pipelines. See our runner installation documentation for detailed installation instructions.

[Install Runners](https://docs.drone.io/runner/overview/)
