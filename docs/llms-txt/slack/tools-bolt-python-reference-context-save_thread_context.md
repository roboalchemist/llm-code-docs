Source: https://docs.slack.dev/tools/bolt-python/reference/context/save_thread_context

# Module slack_bolt.context.save_thread_context

## Sub-modules

`[slack_bolt.context.save_thread_context.async_save_thread_context](async_save_thread_context.html "slack_bolt.context.save_thread_context.async_save_thread_context")`

`[slack_bolt.context.save_thread_context.save_thread_context](save_thread_context.html "slack_bolt.context.save_thread_context.save_thread_context")`

## Classes

`class SaveThreadContext (thread_context_store: [AssistantThreadContextStore](../assistant/thread_context_store/store.html#slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore "slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore"),   channel_id: str,   thread_ts: str)`

Expand source code

```python
class SaveThreadContext:
    thread_context_store: AssistantThreadContextStore
    channel_id: str
    thread_ts: str

    def __init__(
        self,
        thread_context_store: AssistantThreadContextStore,
        channel_id: str,
        thread_ts: str,
    ):
        self.thread_context_store = thread_context_store
        self.channel_id = channel_id
        self.thread_ts = thread_ts

    def __call__(self, new_context: Dict[str, str]) -> None:
        self.thread_context_store.save(
            channel_id=self.channel_id,
            thread_ts=self.thread_ts,
            context=new_context,
        )
```

### Class variables

`var channel_id : str`

The type of the None singleton.

`var thread_context_store : [AssistantThreadContextStore](../assistant/thread_context_store/store.html#slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore "slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore")`

The type of the None singleton.

`var thread_ts : str`

The type of the None singleton.
