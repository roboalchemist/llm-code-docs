# Source: https://docs.safetycli.com/safety-docs/installation/docker-containers.md

# Docker Containers

Safety is available in a Docker container if you'd like to scan across Python versions or use Safety without having to install it, or Python, locally.

To get started, you can run the `ghcr.io/pyupio/safety` image. Any arguments provided will be transparently passed through to Safety:

```shell
docker run --rm -ti ghcr.io/pyupio/safety:latest --version
```

Scanning from a requirements file works as expected. You must, however, make sure to volume mount your project so that Safety can access it inside the container:

```shell
docker run --rm -ti -v /path/to/my/project:/target ghcr.io/pyupio/safety --key <YOUR-API-KEY> --stage cicd scan --target /target
```
