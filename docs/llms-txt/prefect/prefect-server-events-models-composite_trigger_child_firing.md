# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-events-models-composite_trigger_child_firing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# composite_trigger_child_firing

# `prefect.server.events.models.composite_trigger_child_firing`

## Functions

### `acquire_composite_trigger_lock` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/composite_trigger_child_firing.py#L17" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
acquire_composite_trigger_lock(session: AsyncSession, trigger: CompositeTrigger) -> None
```

Acquire a transaction-scoped advisory lock for the given composite trigger.

This serializes concurrent child trigger evaluations for the same compound
trigger, preventing a race condition where multiple transactions each see
only their own child firing and neither fires the parent.

The lock is automatically released when the transaction commits or rolls back.

### `upsert_child_firing` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/composite_trigger_child_firing.py#L51" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
upsert_child_firing(db: PrefectDBInterface, session: AsyncSession, firing: Firing)
```

### `get_child_firings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/composite_trigger_child_firing.py#L99" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_child_firings(db: PrefectDBInterface, session: AsyncSession, trigger: CompositeTrigger) -> Sequence['ORMCompositeTriggerChildFiring']
```

### `clear_old_child_firings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/composite_trigger_child_firing.py#L118" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
clear_old_child_firings(db: PrefectDBInterface, session: AsyncSession, trigger: CompositeTrigger, fired_before: DateTime) -> None
```

### `clear_child_firings` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/models/composite_trigger_child_firing.py#L134" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
clear_child_firings(db: PrefectDBInterface, session: AsyncSession, trigger: CompositeTrigger, firing_ids: Sequence[UUID]) -> set[UUID]
```

Delete the specified child firings and return the IDs that were actually deleted.

Returns the set of child\_firing\_ids that were successfully deleted. Callers can
compare this to the expected firing\_ids to detect races and avoid double-firing
composite triggers.


Built with [Mintlify](https://mintlify.com).