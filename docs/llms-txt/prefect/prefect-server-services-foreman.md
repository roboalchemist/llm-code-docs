# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-services-foreman.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# foreman

# `prefect.server.services.foreman`

The Foreman service. Monitors workers and marks stale resources as offline/not ready.

## Functions

### `monitor_worker_health` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/foreman.py#L35" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
monitor_worker_health(perpetual: Perpetual = Perpetual(automatic=False, every=timedelta(seconds=get_current_settings().server.services.foreman.loop_seconds))) -> None
```

Monitor workers and mark stale resources as offline/not ready.

Iterates over workers currently marked as online. Marks workers as offline
if they have an old last\_heartbeat\_time. Marks work pools as not ready
if they do not have any online workers and are currently marked as ready.
Marks deployments as not ready if they have a last\_polled time that is
older than the configured deployment last polled timeout.


Built with [Mintlify](https://mintlify.com).