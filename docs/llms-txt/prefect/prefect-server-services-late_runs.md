# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-services-late_runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# late_runs

# `prefect.server.services.late_runs`

The MarkLateRuns service. Responsible for putting flow runs in a Late state if they are not started on time.
The threshold for a late run can be configured by changing `PREFECT_API_SERVICES_LATE_RUNS_AFTER_SECONDS`.

## Functions

### `mark_flow_run_late` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/late_runs.py#L25" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
mark_flow_run_late(flow_run_id: Annotated[UUID, Logged]) -> None
```

Mark a single flow run as late (docket task).

### `monitor_late_runs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/late_runs.py#L56" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
monitor_late_runs(docket: Docket = CurrentDocket(), db: PrefectDBInterface = Depends(provide_database_interface), perpetual: Perpetual = Perpetual(automatic=False, every=timedelta(seconds=get_current_settings().server.services.late_runs.loop_seconds))) -> None
```

Monitor for late flow runs and schedule marking tasks.


Built with [Mintlify](https://mintlify.com).