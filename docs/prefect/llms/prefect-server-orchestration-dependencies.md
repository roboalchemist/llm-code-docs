# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-orchestration-dependencies.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# dependencies

# `prefect.server.orchestration.dependencies`

Injected orchestration dependencies

## Functions

### `provide_task_policy` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/orchestration/dependencies.py#L47" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
provide_task_policy() -> type[TaskRunOrchestrationPolicy]
```

### `provide_flow_policy` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/orchestration/dependencies.py#L58" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
provide_flow_policy() -> type[FlowRunOrchestrationPolicy]
```

### `provide_task_orchestration_parameters` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/orchestration/dependencies.py#L71" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
provide_task_orchestration_parameters() -> dict[str, Any]
```

### `provide_flow_orchestration_parameters` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/orchestration/dependencies.py#L82" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
provide_flow_orchestration_parameters() -> dict[str, Any]
```

### `temporary_task_policy` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/orchestration/dependencies.py#L94" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
temporary_task_policy(tmp_task_policy: type[TaskRunOrchestrationPolicy])
```

### `temporary_flow_policy` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/orchestration/dependencies.py#L108" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
temporary_flow_policy(tmp_flow_policy: type[FlowRunOrchestrationPolicy])
```

### `temporary_task_orchestration_parameters` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/orchestration/dependencies.py#L122" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
temporary_task_orchestration_parameters(tmp_orchestration_parameters: dict[str, Any])
```

### `temporary_flow_orchestration_parameters` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/orchestration/dependencies.py#L144" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
temporary_flow_orchestration_parameters(tmp_orchestration_parameters: dict[str, Any])
```

## Classes

### `OrchestrationDependencies` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/orchestration/dependencies.py#L22" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>


Built with [Mintlify](https://mintlify.com).