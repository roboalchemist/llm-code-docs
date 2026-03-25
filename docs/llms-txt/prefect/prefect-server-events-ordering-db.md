# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-events-ordering-db.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# db

# `prefect.server.events.ordering.db`

## Classes

### `CausalOrdering` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/db.py#L35" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `event_has_been_seen` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/db.py#L45" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
event_has_been_seen(self, event: Union[UUID, Event]) -> bool
```

#### `forget_follower` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/db.py#L71" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
forget_follower(self, db: PrefectDBInterface, follower: ReceivedEvent) -> None
```

Forget that this event is waiting on another event to arrive

#### `get_followers` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/db.py#L86" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_followers(self, db: PrefectDBInterface, leader: ReceivedEvent) -> List[ReceivedEvent]
```

Returns events that were waiting on this leader event to arrive

#### `get_lost_followers` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/db.py#L100" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_lost_followers(self, db: PrefectDBInterface) -> List[ReceivedEvent]
```

Returns events that were waiting on a leader event that never arrived

#### `preceding_event_confirmed` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/db.py#L124" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
preceding_event_confirmed(self, handler: event_handler, event: ReceivedEvent, depth: int = 0)
```

Events may optionally declare that they logically follow another event, so that
we can preserve important event orderings in the face of unreliable delivery and
ordering of messages from the queues.

This function keeps track of the ID of each event that this shard has successfully
processed going back to the PRECEDING\_EVENT\_LOOKBACK period.  If an event arrives
that must follow another one, confirm that we have recently seen and processed that
event before proceeding.

event (ReceivedEvent): The event to be processed. This object should include metadata indicating
if and what event it follows.
depth (int, optional): The current recursion depth, used to prevent infinite recursion due to
cyclic dependencies between events. Defaults to 0.

Raises EventArrivedEarly if the current event shouldn't be processed yet.

#### `record_event_as_seen` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/db.py#L49" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
record_event_as_seen(self, event: ReceivedEvent) -> None
```

#### `record_follower` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/events/ordering/db.py#L53" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
record_follower(self, db: PrefectDBInterface, event: ReceivedEvent) -> None
```

Remember that this event is waiting on another event to arrive


Built with [Mintlify](https://mintlify.com).