# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-services-pause_expirations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# pause_expirations

# `prefect.server.services.pause_expirations`

The FailExpiredPauses service. Responsible for putting Paused flow runs in a Failed state if they are not resumed on time.

## Functions

### `fail_expired_pause` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/pause_expirations.py#L20" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
fail_expired_pause(flow_run_id: Annotated[UUID, Logged], pause_timeout: Annotated[str, Logged]) -> None
```

Mark a single expired paused flow run as failed (docket task).

### `monitor_expired_pauses` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/pause_expirations.py#L54" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
monitor_expired_pauses(docket: Docket = CurrentDocket(), db: PrefectDBInterface = Depends(provide_database_interface), perpetual: Perpetual = Perpetual(automatic=False, every=timedelta(seconds=get_current_settings().server.services.pause_expirations.loop_seconds))) -> None
```

Monitor for expired paused flow runs and schedule failure tasks.


Built with [Mintlify](https://mintlify.com).