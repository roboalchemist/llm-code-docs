# Source: https://docs.prefect.io/integrations/prefect-kubernetes/api-ref/prefect_kubernetes-observer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# observer

# `prefect_kubernetes.observer`

## Functions

### `configure` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-kubernetes/prefect_kubernetes/observer.py#L51" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
configure(settings: kopf.OperatorSettings, **_)
```

### `initialize_clients` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-kubernetes/prefect_kubernetes/observer.py#L56" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
initialize_clients(logger: kopf.Logger, **kwargs: Any)
```

### `cleanup_fn` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-kubernetes/prefect_kubernetes/observer.py#L70" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
cleanup_fn(logger: kopf.Logger, **kwargs: Any)
```

### `start_observer` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-kubernetes/prefect_kubernetes/observer.py#L451" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
start_observer()
```

Start the observer in a separate thread.

### `stop_observer` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-kubernetes/prefect_kubernetes/observer.py#L502" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
stop_observer()
```

Stop the observer thread.


Built with [Mintlify](https://mintlify.com).