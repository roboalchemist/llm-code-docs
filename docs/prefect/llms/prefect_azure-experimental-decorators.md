# Source: https://docs.prefect.io/integrations/prefect-azure/api-ref/prefect_azure-experimental-decorators.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# decorators

# `prefect_azure.experimental.decorators`

## Functions

### `azure_container_instance` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-azure/prefect_azure/experimental/decorators.py#L19" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
azure_container_instance(work_pool: str, **job_variables: Any) -> Callable[[Flow[P, R]], InfrastructureBoundFlow[P, R]]
```

Decorator that binds execution of a flow to an Azure Container Instance work pool

**Args:**

* `work_pool`: The name of the Azure Container Instance work pool to use
* `**job_variables`: Additional job variables to use for infrastructure configuration


Built with [Mintlify](https://mintlify.com).