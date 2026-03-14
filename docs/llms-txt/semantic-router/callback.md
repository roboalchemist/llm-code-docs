# Source: https://docs.aurelio.ai/graphai/client-reference/callback.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# graphai.callback

## GraphEvent Objects

```python  theme={null}
@dataclass
class GraphEvent()
```

A graph event emitted for specific graph events such as start node or end node,

and used by the callback to emit user-defined events.

**Arguments**:

* `type` (`GraphEventType | str`): The type of event, can be start\_node, end\_node, callback, or a custom str.
* `identifier` (`str`): The identifier of the event, this is set typically by a callback
  handler and can be used to distinguish between different events. For example, a
  conversation/session ID could be used.
* `token` (`str | None`): The token associated with the event, such as LLM streamed output.
* `params` (`dict[str, Any] | None`): The parameters associated with the event, such as tool call parameters
  or event metadata.

#### encode

```python  theme={null}
def encode(charset: str = "utf-8") -> bytes
```

Encodes the event as a JSON string, important for compatability with FastAPI

and starlette.

**Arguments**:

* `charset` (`str`): The character set to use for encoding the event.

## CallbackProtocol Objects

```python  theme={null}
@runtime_checkable
class CallbackProtocol(Protocol)
```

Protocol defining the interface for callback handlers.

## Callback Objects

```python  theme={null}
class Callback()
```

The original callback handler class. Outputs a stream of structured text
tokens. It is recommended to use the newer `EventCallback` handler instead.

#### aiter

```python  theme={null}
async def aiter() -> AsyncIterator[str]
```

Used by receiver to get the tokens from the stream queue. Creates
a generator that yields tokens from the queue until the END token is
received.

#### start\_node

```python  theme={null}
async def start_node(node_name: str, active: bool = True)
```

Starts a new node and emits the start token.

#### end\_node

```python  theme={null}
async def end_node(node_name: str)
```

Emits the end token for the current node.

#### close

```python  theme={null}
async def close()
```

Close the stream and prevent further tokens from being added.
This will send an END token and set the done flag to True.

## EventCallback Objects

```python  theme={null}
class EventCallback()
```

The event callback handler class. Outputs a stream of structured text
tokens. It is recommended to use the newer `EventCallback` handler instead.

#### \_\_call\_\_

```python  theme={null}
def __call__(token: str | None = None,
             type: GraphEventType | str = GraphEventType.CALLBACK,
             identifier: str | None = None,
             params: dict[str, Any] | None = None)
```

Builds a GraphEvent object and adds it to the queue.

#### acall

```python  theme={null}
async def acall(token: str | None = None,
                type: GraphEventType | str = GraphEventType.CALLBACK,
                identifier: str | None = None,
                params: dict[str, Any] | None = None)
```

Builds a GraphEvent object and adds it to the queue.

#### aiter

```python  theme={null}
async def aiter() -> AsyncIterator[GraphEvent]
```

Used by receiver to get the tokens from the stream queue. Creates
a generator that yields tokens from the queue until the END token is
received.

#### start\_node

```python  theme={null}
async def start_node(node_name: str, active: bool = True)
```

Starts a new node and emits the start token.

#### end\_node

```python  theme={null}
async def end_node(node_name: str)
```

Emits the end token for the current node.

#### close

```python  theme={null}
async def close()
```

Close the stream and prevent further tokens from being added.
This will send an END token and set the done flag to True.


Built with [Mintlify](https://mintlify.com).