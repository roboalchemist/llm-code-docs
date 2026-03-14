# Source: https://docs.drone.io/server/overview/

Title: Overview | Drone

URL Source: https://docs.drone.io/server/overview/

Markdown Content:
This section of the documentation will help you install and configure the Drone _Server_ and one or many _Runners_. A runner is a standalone daemon that polls the server for pending pipelines to execute.

Server Installation
-------------------

Drone integrates seamlessly with popular _Source Control Management_ providers. Please choose your provider to get started.

[GitHub](https://docs.drone.io/server/provider/github/)[Gitee](https://docs.drone.io/server/provider/gitee/)[GitLab](https://docs.drone.io/server/provider/gitlab/)[Gogs](https://docs.drone.io/server/provider/gogs/)[Gitea](https://docs.drone.io/server/provider/gitea/)[Bitbucket Cloud](https://docs.drone.io/server/provider/bitbucket-cloud/)[Bitbucket Server](https://docs.drone.io/server/provider/bitbucket-server/)

Server Upgrades
---------------

Drone server upgrades are meant to be simple and safe. Replace the old Docker image with the new Docker image and Drone will handle everything else (automatic database migrations, etc).

_If a release introduces breaking changes or requires manual upgrade it will be specified in the release notes. As a general rule we try to maintain strict backward compatibility and avoid breaking changes, even in major releases._

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
``````
# terminate the drone server
docker stop drone
docker rm drone

# pull the latest major release
docker pull drone/drone:2

# re-start the drone server using the
# newer docker image
docker run ...
```

Runner Installation
-------------------

Drone _Runners_ are standalone daemons that poll the server for pending pipelines to execute. There are different types of runners optimized for different use cases and runtime environments. Once the server is successfully installed you must install one or more runners.

[See the Runner Installation Guide](https://docs.drone.io/runner/overview/)
