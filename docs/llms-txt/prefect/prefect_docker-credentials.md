# Source: https://docs.prefect.io/integrations/prefect-docker/api-ref/prefect_docker-credentials.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# credentials

# `prefect_docker.credentials`

Module containing docker credentials.

## Classes

### `DockerRegistryCredentials` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-docker/prefect_docker/credentials.py#L12" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Block used to manage credentials for interacting with a Docker Registry.

**Examples:**

Log into Docker Registry.

```python  theme={null}
from prefect_docker import DockerHost, DockerRegistryCredentials

docker_host = DockerHost()
docker_registry_credentials = DockerRegistryCredentials.load("BLOCK_NAME")
with docker_host.get_client() as client:
    docker_registry_credentials.login(client)
```

**Methods:**

#### `login` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-docker/prefect_docker/credentials.py#L50" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
login(self, client: docker.DockerClient)
```

Authenticates a given Docker client with the configured Docker registry.

**Args:**

* `client`: A Docker Client.


Built with [Mintlify](https://mintlify.com).