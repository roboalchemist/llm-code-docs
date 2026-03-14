# Source: https://docs.drone.io/server/provider/github/

Title: GitHub | Drone

URL Source: https://docs.drone.io/server/provider/github/

Markdown Content:
This article explains how to install the Drone server for GitHub. The server is packaged as a minimal Docker image distributed on [DockerHub](https://hub.docker.com/r/drone/drone).

Preparation
-----------

Provision an Instance
---------------------

The Drone server should be installed on a server or virtual machine (using your cloud provider of choice) with standard http and https ports open. The instance must be publicly accessible by domain name or IP address to receive webhooks from GitHub.

_When installing the Drone server on your laptop for testing purposes, we recommend using a service like [ngrok](https://ngrok.com/) to provide your Drone server with a publicly accessible domain name._

Create an OAuth Application
---------------------------

[Create a GitHub OAuth application](https://docs.github.com/en/developers/apps/creating-an-oauth-app). The Consumer Key and Consumer Secret are used to authorize access to GitHub resources.

The authorization callback URL must match the below format and path, and must use your exact server scheme and host.

![Image 1: Application Create](https://docs.drone.io/screenshots/github_application_create.png)![Image 2: Application View](https://docs.drone.io/screenshots/github_application_created.png)

Create a shared secret to authenticate communication between runners and your central Drone server.

You can use openssl to generate a shared secret:

```
$ openssl rand -hex 16
bea26a2221fd8090ea38720fc445eca6
```

Download
--------

The Drone server is distributed as a lightweight Docker image. The image is self-contained and does not have any external dependencies. The latest tag will ensure the latest version of Drone.

```
$ docker pull drone/drone:2
```

Configuration
-------------

The Drone server is configured using environment variables. This article references a subset of configuration options, defined below. See [Configuration](https://docs.drone.io/server/reference/) for a complete list of configuration options.

*   **DRONE_GITHUB_CLIENT_ID**Required string value provides your GitHub oauth Client ID generated in the previous step.
*   **DRONE_GITHUB_CLIENT_SECRET**Required string value provides your GitHub oauth Client Secret generated in the previous step.
*   **DRONE_RPC_SECRET**Required string value provides the shared secret generated in the previous step. This is used to authenticate the rpc connection between the server and runners. The server and runner must be provided the same secret value.
*   **DRONE_SERVER_HOST**Required string value provides your external hostname or IP address. If using an IP address you may include the port. For example `drone.company.com`.
*   **DRONE_SERVER_PROTO**Required string value provides your external protocol scheme. This value should be set to http or https. This field defaults to https if you configure ssl or acme. _This value should be set to `https` if you deploy Drone behind a load balancer or reverse proxy with SSL termination._
*   **DRONE_USER_FILTER**Optional comma-separated list of GitHub users or organizations. Registration is limited to users in this list, or users that are members of organizations in this list. _Registration is open to the public if this value is unset._

Start the Server
----------------

The server container can be started with the below command. The container is configured through environment variables. For a full list of configuration parameters, please see the configuration reference.

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
  --env=DRONE_GITHUB_CLIENT_ID=your-id \
  --env=DRONE_GITHUB_CLIENT_SECRET=super-duper-secret \
  --env=DRONE_RPC_SECRET=super-duper-secret \
  --env=DRONE_SERVER_HOST=drone.company.com \
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
