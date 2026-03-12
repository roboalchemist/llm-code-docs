# Source: https://docs.prefect.io/integrations/prefect-gcp/api-ref/prefect_gcp-experimental-decorators.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# decorators

# `prefect_gcp.experimental.decorators`

## Functions

### `cloud_run` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-gcp/prefect_gcp/experimental/decorators.py#L20" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
cloud_run(work_pool: str, **job_variables: Any) -> Callable[[Flow[P, R]], InfrastructureBoundFlow[P, R]]
```

Decorator that binds execution of a flow to a Cloud Run V2 work pool

**Args:**

* `work_pool`: The name of the Cloud Run V2 work pool to use
* `**job_variables`: Additional job variables to use for infrastructure configuration

### `vertex_ai` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-gcp/prefect_gcp/experimental/decorators.py#L56" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
vertex_ai(work_pool: str, **job_variables: Any) -> Callable[[Flow[P, R]], InfrastructureBoundFlow[P, R]]
```

Decorator that binds execution of a flow to a Vertex AI work pool

**Args:**

* `work_pool`: The name of the Vertex AI work pool to use
* `**job_variables`: Additional job variables to use for infrastructure configuration


Built with [Mintlify](https://mintlify.com).