Source: https://docs.slack.dev/tools/bolt-python/reference/context/assistant/thread_context_store/file

# Module slack_bolt.context.assistant.thread_context_store.file

## Classes

`class FileAssistantThreadContextStore (base_dir: str = '/Users/wbergamin/.bolt-app-assistant-thread-contexts')`

Expand source code

```python
class FileAssistantThreadContextStore(AssistantThreadContextStore):

    def __init__(
        self,
        base_dir: str = str(Path.home()) + "/.bolt-app-assistant-thread-contexts",
    ):
        self.base_dir = base_dir
        self._mkdir(self.base_dir)

    def save(self, *, channel_id: str, thread_ts: str, context: Dict[str, str]) -> None:
        path = f"{self.base_dir}/{channel_id}-{thread_ts}.json"
        with open(path, "w") as f:
            f.write(json.dumps(context))

    def find(self, *, channel_id: str, thread_ts: str) -> Optional[AssistantThreadContext]:
        path = f"{self.base_dir}/{channel_id}-{thread_ts}.json"
        try:
            with open(path) as f:
                data = json.loads(f.read())
                if data.get("channel_id") is not None:
                    return AssistantThreadContext(data)
        except FileNotFoundError:
            pass
        return None

    @staticmethod
    def _mkdir(path: Union[str, Path]):
        if isinstance(path, str):
            path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
```

### Ancestors

* [AssistantThreadContextStore](../store.html#slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore "slack_bolt.context.assistant.thread_context_store.store.AssistantThreadContextStore")

### Methods

`def find(self, *, channel_id: str, thread_ts: str) ‑> [AssistantThreadContext](../../thread_context/index.html#slack_bolt.context.assistant.thread_context.AssistantThreadContext "slack_bolt.context.assistant.thread_context.AssistantThreadContext") | None`

Expand source code

```python
def find(self, *, channel_id: str, thread_ts: str) -> Optional[AssistantThreadContext]:
    path = f"{self.base_dir}/{channel_id}-{thread_ts}.json"
    try:
        with open(path) as f:
            data = json.loads(f.read())
            if data.get("channel_id") is not None:
                return AssistantThreadContext(data)
    except FileNotFoundError:
        pass
    return None
```

`def save(self, *, channel_id: str, thread_ts: str, context: Dict[str, str]) ‑> None`

Expand source code

```python
def save(self, *, channel_id: str, thread_ts: str, context: Dict[str, str]) -> None:
    path = f"{self.base_dir}/{channel_id}-{thread_ts}.json"
    with open(path, "w") as f:
        f.write(json.dumps(context))
```
