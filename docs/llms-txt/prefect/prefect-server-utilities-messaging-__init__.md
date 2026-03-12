# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-utilities-messaging-__init__.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# __init__

# `prefect.server.utilities.messaging`

## Functions

### `create_cache` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L169" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_cache() -> Cache
```

Creates a new cache with the applications default settings.

**Returns:**

* a new Cache instance

### `create_publisher` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L195" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_publisher(topic: str, cache: Optional[Cache] = None, deduplicate_by: Optional[str] = None) -> Publisher
```

Creates a new publisher with the applications default settings.
Args:
topic: the topic to publish to
Returns:
a new Consumer instance

### `ephemeral_subscription` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L213" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
ephemeral_subscription(topic: str) -> AsyncGenerator[Mapping[str, Any], Any]
```

Creates an ephemeral subscription to the given source, removing it when the context
exits.

### `create_consumer` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L224" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_consumer(topic: str, **kwargs: Any) -> Consumer
```

Creates a new consumer with the applications default settings.
Args:
topic: the topic to consume from
Returns:
a new Consumer instance

## Classes

### `Message` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L32" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

A protocol representing a message sent to a message broker.

**Methods:**

#### `attributes` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L41" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
attributes(self) -> Mapping[str, Any]
```

#### `data` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L38" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
data(self) -> Union[str, bytes]
```

### `Cache` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L44" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `clear_recently_seen_messages` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L46" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
clear_recently_seen_messages(self) -> None
```

#### `forget_duplicates` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L54" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
forget_duplicates(self, attribute: str, messages: Iterable[Message]) -> None
```

#### `without_duplicates` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L49" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
without_duplicates(self, attribute: str, messages: Iterable[M]) -> list[M]
```

### `Publisher` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L59" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `publish_data` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L68" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
publish_data(self, data: bytes, attributes: Mapping[str, str]) -> None
```

### `CapturedMessage` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L85" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

### `CapturingPublisher` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L90" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

**Methods:**

#### `publish_data` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L115" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
publish_data(self, data: bytes, attributes: Mapping[str, str]) -> None
```

#### `publish_data` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L68" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
publish_data(self, data: bytes, attributes: Mapping[str, str]) -> None
```

### `StopConsumer` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L129" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Exception to raise to stop a consumer.

### `Consumer` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L138" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Abstract base class for consumers that receive messages from a message broker and
call a handler function for each message received.

**Methods:**

#### `cleanup` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L152" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
cleanup(self) -> None
```

Cleanup resources when the consumer is stopped.

Override this method in subclasses that need to perform cleanup,
such as unsubscribing from topics or closing connections.

The default implementation is a no-op, which is appropriate for
consumers that don't need explicit cleanup.

#### `run` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L148" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
run(self, handler: MessageHandler) -> None
```

Runs the consumer (indefinitely)

### `CacheModule` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L165" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

### `BrokerModule` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/messaging/__init__.py#L183" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>


Built with [Mintlify](https://mintlify.com).