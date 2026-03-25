# Source: https://docs.prefect.io/integrations/prefect-kubernetes/api-ref/prefect_kubernetes-experimental-decorators.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# decorators

# `prefect_kubernetes.experimental.decorators`

## Functions

### `kubernetes` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-kubernetes/prefect_kubernetes/experimental/decorators.py#L19" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
kubernetes(work_pool: str, **job_variables: Any) -> Callable[[Flow[P, R]], InfrastructureBoundFlow[P, R]]
```

Decorator that binds execution of a flow to a Kubernetes work pool

**Args:**

* `work_pool`: The name of the Kubernetes work pool to use
* `**job_variables`: Additional job variables to use for infrastructure configuration


Built with [Mintlify](https://mintlify.com).