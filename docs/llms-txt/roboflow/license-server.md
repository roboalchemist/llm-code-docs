# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/enterprise-deployment/license-server.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/enterprise-deployment/license-server.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/enterprise-deployment/license-server.md

# Source: https://docs.roboflow.com/deploy/enterprise-deployment/license-server.md

# License Server

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-9e91b0b1bd864d523e13bbabd615708b95712059%2Fdiagram.png?alt=media" alt=""><figcaption><p>Use the license server as a proxy for the Roboflow API.</p></figcaption></figure>

## Prerequisites

* Linux server running Ubuntu 20.04+ or Debian 11+
* Internet access to api.roboflow\.com and repo.roboflow\.com
* Static IP address or hostname
* Port 80 available (or custom port)
* Docker Engine 20.10+
* 200GB+ storage
* 4GB+ memory

## Using the License Server

If you wish to firewall the Roboflow Inference Server from the Internet, you will need to use the Roboflow License Server which acts as a proxy for the Roboflow API and your models' weights.

On a machine with access to `https://api.roboflow.com` and `https://repo.roboflow.com` (and port `80` open to the Inference Server running in your private network), pull the License Server Docker container:

```
docker pull repo.roboflow.com/roboflow/license-server
```

And run it:

```
docker run -d --name license-server -p 80:80 --restart unless-stopped \
    repo.roboflow.com/roboflow/license-server:latest
```

Configure your Inference Server to use this License Server by passing its IP in the `LICENSE_SERVER` environment variable:

```
sudo docker run --net=host --env LICENSE_SERVER=10.0.1.1 roboflow/inference-server:cpu
```
