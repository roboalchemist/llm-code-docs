# Source: https://docs.prefect.io/v3/how-to-guides/workflows/retry-flow-runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# How to manually retry a flow run

Use `prefect flow-run retry` to re-execute a failed or cancelled flow run. The flow run keeps its original ID and parameters, but the `run_count` increments.

### Find flow runs to retry

List failed flow runs to find the name you need:

```bash  theme={null}
prefect flow-run ls --state FAILED
```

### Retry a deployment-based flow run

If the flow run was created from a deployment, retry schedules it for a worker to pick up:

```bash  theme={null}
prefect flow-run retry adventurous-crocodile
```

The flow run's state changes to `Scheduled` and a worker will pick it up for execution.

### Retry a local flow run

Flow runs created without a deployment require an `--entrypoint` to the flow code:

```bash  theme={null}
prefect flow-run retry adventurous-crocodile --entrypoint ./flows/my_flow.py:my_flow
```

The flow executes immediately in the current process.

### Retry by ID

If multiple flow runs share the same name, use the UUID instead:

```bash  theme={null}
prefect flow-run retry a1b2c3d4-e5f6-7890-abcd-ef1234567890
```


Built with [Mintlify](https://mintlify.com).