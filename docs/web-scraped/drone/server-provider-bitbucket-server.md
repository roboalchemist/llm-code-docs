# Source: https://docs.drone.io/server/provider/bitbucket-server/

Title: Bitbucket Server | Drone

URL Source: https://docs.drone.io/server/provider/bitbucket-server/

Markdown Content:
This article explains how to install the Drone server for Bitbucket Server, formerly known as Atlassian Stash. The server is packaged as a minimal Docker image distributed on [DockerHub](https://hub.docker.com/r/drone/drone).

Preparation
-----------

Create a Personal Access Token
------------------------------

Create a personal access token that is capable of cloning all repositories in the system. The token and associated username are used for all clone operations. We recommend creating a machine account for this purpose.

Navigate to the _Personal Access Tokens_ page in the account settings, and click the _Create Token_ button.

![Image 1: Token List](https://docs.drone.io/screenshots/stash_token_list.png)

Create the personal access token. The creation form should indicate pull and clone access as pictured below. Click the _Create_ button and copy the generated token.

![Image 2: Token Create](https://docs.drone.io/screenshots/stash_token_create.png)

Create a Key Pair
-----------------

Create a key pair on your server. The key pair is used to setup an authentication provide with Bitbucket and authorize API access.

Generate the private key:

```
$ openssl genrsa -out /etc/bitbucket/key.pem 1024
Generating RSA private key, 1024 bit long modulus
....................................++++++
..........++++++
e is 65537 (0x10001)
```

Generate a public key:

```
$ openssl rsa \
  -in /etc/bitbucket/key.pem \
  -pubout >> /etc/bitbucket/key.pub
```

Create an Application Link
--------------------------

Create a Bitbucket Application Link. The link will provide a Consumer ID and Private Key used to authorize access to Bitbucket resources. The Bitbucket application creation process is convoluted and error prone. Please bear with us.

Navigate the administrator panel and click the _Application Links_ settings page. Enter your Drone server URL and click _Create New Link_.

![Image 3: stash_application_link](https://docs.drone.io/screenshots/stash_application_link.png)

Please fill out the form using the values specified below. Once complete click _Continue_ to create your application.

*   Set the application name to _Drone_
*   Set the application type to _Generic Application_
*   Set the provider name to _Drone_
*   Set the consumer key to _OauthKey_
*   Set the shared secret to any random alphanumeric value
*   Set the request token url to your Drone server URL
*   Set the access token url to your Drone server URL
*   Set the authorize token url to your Drone server URL

![Image 4: stash_application_link_create](https://docs.drone.io/screenshots/stash_application_link_create.png)

Once the application is created it needs to be edited so that we can configure the _Incoming Authentication_. Please fill out the form using the values specified below and save your changes.

*   Set the consumer key to _OauthKey_
*   Set the consumer name to _Drone_
*   Paste the contents of `/etc/bitbucket/key.pub` in the public key textarea
*   Leave _Consumer Callback_ empty
*   Leave _Allow 2-Legged Oauth_ unchecked

![Image 5: stash_application_link_edit](https://docs.drone.io/screenshots/stash_application_link_edit.png)

Congratulations, you have made it through the most painful part of the installation. With luck, everything will work as expected and you will never have to do this again.

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

*   **DRONE_GIT_USERNAME**Required string value set to username associated with the Personal Account token. This username is used to authenticate and clone all private repositories.
*   **DRONE_GIT_PASSWORD**Required string value set to your Personal Account Token. The token is used to authenticate and clone all private repositories.
*   **DRONE_GIT_ALWAYS_AUTH**Optional boolean value configures Drone to authenticate when cloning public repositories. This should only be enabled when using GitHub Enterprise with private mode enable.
*   **DRONE_STASH_CONSUMER_KEY**Required string value configures your Bitbucket Server consumer key.
*   **DRONE_STASH_PRIVATE_KEY**Required string value configures the path to your Bitbucket Server private key file. Note that this file needs to also be mounted into the Drone server container as a volume.
*   **DRONE_STASH_SERVER**Required string value provides the Bitbucket Server address. For example `https://bitbucket.company.com`
*   **DRONE_RPC_SECRET**Required string value provides the shared secret generated in the previous step. This is used to authenticate the rpc connection between the server and runners. The server and runner must be provided the same secret value.
*   **DRONE_SERVER_HOST**Required string value provides your external hostname or IP address. If using an IP address you may include the port.
*   **DRONE_SERVER_PROTO**Required string value provides your external protocol scheme. This value should be set to http or https. This field defaults to https if you configure ssl or acme.

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
14
15
16
17
18
``````
docker run \
  --volume=/var/lib/drone:/data \
  --volume=/etc/bitbucket/key.pem:/etc/bitbucket/key.pem \
  --env=DRONE_GIT_PASSWORD=7c229228a77d2cbddaa61ddc78d45e \
  --env=DRONE_GIT_USERNAME=x-oauth-token \
  --env=DRONE_GIT_ALWAYS_AUTH=false \
  --env=DRONE_STASH_SERVER=https://bitbucket.company.com \
  --env=DRONE_STASH_CONSUMER_KEY=OauthKey \
  --env=DRONE_STASH_PRIVATE_KEY=/etc/bitbucket/key.pem \
  --env=DRONE_SERVER_HOST=drone.company.com \
  --env=DRONE_SERVER_PROTO=https \
  --env=DRONE_RPC_SECRET=super-duper-secret \
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
