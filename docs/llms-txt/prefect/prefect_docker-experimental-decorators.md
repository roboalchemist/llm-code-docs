# Source: https://docs.prefect.io/integrations/prefect-docker/api-ref/prefect_docker-experimental-decorators.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# decorators

# `prefect_docker.experimental.decorators`

## Functions

### `docker` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-docker/prefect_docker/experimental/decorators.py#L13" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
docker(work_pool: str, **job_variables: Any) -> Callable[[Flow[P, R]], Flow[P, R]]
```

Decorator that binds execution of a flow to a Docker work pool

**Args:**

* `work_pool`: The name of the Docker work pool to use
* `**job_variables`: Additional job variables to use for infrastructure configuration


Built with [Mintlify](https://mintlify.com).