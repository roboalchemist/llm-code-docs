# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-services-repossessor.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# repossessor

# `prefect.server.services.repossessor`

The Repossessor service. Handles reconciliation of expired concurrency leases.

## Functions

### `revoke_expired_lease` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/repossessor.py#L27" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
revoke_expired_lease(lease_id: Annotated[UUID, Logged]) -> None
```

Revoke a single expired lease (docket task).

### `monitor_expired_leases` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/services/repossessor.py#L63" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
monitor_expired_leases(docket: Docket = CurrentDocket(), lease_storage: ConcurrencyLeaseStorage = Depends(get_concurrency_lease_storage), perpetual: Perpetual = Perpetual(automatic=False, every=timedelta(seconds=get_current_settings().server.services.repossessor.loop_seconds))) -> None
```

Monitor for expired leases and schedule revocation tasks.


Built with [Mintlify](https://mintlify.com).