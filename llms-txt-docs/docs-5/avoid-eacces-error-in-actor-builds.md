# Source: https://docs.apify.com/academy/node-js/avoid-eacces-error-in-actor-builds.md

# Avoid EACCES error in Actor builds with a custom Dockerfile

Sometimes when building an Actor using a custom Dockerfile, you might receive errors like:


```
Missing write access to ...
```


or


```
EACCES: permission denied
```


This problem is usually caused by the fact that by default, the `COPY` Dockerfile instruction copies files as the root user (with UID and GID of 0), while your Dockerfile probably uses another user to copy files and run commands.

To fix this problem, make sure the `COPY`  instruction in Dockerfile uses the `--chown` flag. For example, instead of


```
COPY . ./
```


use


```
COPY --chown=myuser:myuser . ./
```


where `myuser` is the user and group defined by the `USER`  instruction in the base Docker image. To learn more, see https://docs.docker.com/reference/dockerfile/#copy.

Hope this helps!
