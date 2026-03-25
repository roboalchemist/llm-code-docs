# Source: https://docs.prefect.io/v3/api-ref/python/prefect-docker-docker_image.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# docker_image

# `prefect.docker.docker_image`

## Classes

### `DockerImage` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/docker/docker_image.py#L19" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Configuration used to build and push a Docker image for a deployment.

**Attributes:**

* `name`: The name of the Docker image to build, including the registry and
  repository.
* `tag`: The tag to apply to the built image.
* `dockerfile`: The path to the Dockerfile to use for building the image. If
  not provided, a default Dockerfile will be generated.
* `**build_kwargs`: Additional keyword arguments to pass to the Docker build request.
  See the [`docker-py` documentation](https://docker-py.readthedocs.io/en/stable/images.html#docker.models.images.ImageCollection.build)
  for more information.

**Methods:**

#### `build` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/docker/docker_image.py#L64" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
build(self) -> None
```

#### `push` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/docker/docker_image.py#L79" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
push(self) -> None
```

#### `reference` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/docker/docker_image.py#L61" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
reference(self) -> str
```


Built with [Mintlify](https://mintlify.com).