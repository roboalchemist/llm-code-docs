# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-orchestration-instrumentation_policies.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# instrumentation_policies

# `prefect.server.orchestration.instrumentation_policies`

Orchestration rules related to instrumenting the orchestration engine for Prefect
Observability

## Classes

### `InstrumentFlowRunStateTransitions` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/orchestration/instrumentation_policies.py#L25" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

When a Flow Run changes states, fire a Prefect Event for the state change

**Methods:**

#### `after_transition` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/orchestration/instrumentation_policies.py#L28" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
after_transition(self, context: OrchestrationContext[orm_models.FlowRun, core.FlowRunPolicy]) -> None
```


Built with [Mintlify](https://mintlify.com).