# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-services-telemetry.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# telemetry

# `prefect.server.services.telemetry`

The Telemetry service. Sends anonymous data to Prefect to help us improve.

## Functions

### `send_telemetry_heartbeat` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/telemetry.py#L69" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
send_telemetry_heartbeat(perpetual: Perpetual = Perpetual(automatic=True, every=timedelta(seconds=600))) -> None
```

Sends anonymous telemetry data to Prefect to help us improve.

It can be toggled off with the PREFECT\_SERVER\_ANALYTICS\_ENABLED setting.


Built with [Mintlify](https://mintlify.com).