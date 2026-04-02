Source: https://docs.slack.dev/tools/bolt-python/reference/context/get_thread_context

# Module slack_bolt.context.get_thread_context

## Sub-modules

`[slack_bolt.context.get_thread_context.async_get_thread_context](async_get_thread_context.html "slack_bolt.context.get_thread_context.async_get_thread_context")`

`[slack_bolt.context.get_thread_context.get_thread_context](get_thread_context.html "slack_bolt.context.get_thread_context.get_thread_context")`

## Classes

`class GetThreadContext (thread_context_store: [AssistantThreadContextStore](../assistant/thread_context_store/store.html#slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore "slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore"),   channel_id: str,   thread_ts: str,   payload: dict)`

Expand source code

```python
class GetThreadContext:
    thread_context_store: AssistantThreadContextStore
    payload: dict
    channel_id: str
    thread_ts: str

    _thread_context: Optional[AssistantThreadContext]
    thread_context_loaded: bool

    def __init__(
        self,
        thread_context_store: AssistantThreadContextStore,
        channel_id: str,
        thread_ts: str,
        payload: dict,
    ):
        self.thread_context_store = thread_context_store
        self.payload = payload
        self.channel_id = channel_id
        self.thread_ts = thread_ts
        self._thread_context: Optional[AssistantThreadContext] = None
        self.thread_context_loaded = False

    def __call__(self) -> Optional[AssistantThreadContext]:
        if self.thread_context_loaded is True:
            return self._thread_context

        if self.payload.get("assistant_thread") is not None:
            # assistant_thread_started
            thread = self.payload["assistant_thread"]
            self._thread_context = (
                AssistantThreadContext(thread["context"])
                if thread.get("context", {}).get("channel_id") is not None
                else None
            )
            # for this event, the context will never be changed
            self.thread_context_loaded = True
        elif self.payload.get("channel") is not None and self.payload.get("thread_ts") is not None:
            # message event
            self._thread_context = self.thread_context_store.find(channel_id=self.channel_id, thread_ts=self.thread_ts)

        return self._thread_context
```

### Class variables

`var channel_id : str`

The type of the None singleton.

`var payload : dict`

The type of the None singleton.

`var thread_context_loaded : bool`

The type of the None singleton.

`var thread_context_store : [AssistantThreadContextStore](../assistant/thread_context_store/store.html#slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore "slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore")`

The type of the None singleton.

`var thread_ts : str`

The type of the None singleton.
