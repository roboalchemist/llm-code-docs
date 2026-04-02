Source: https://docs.slack.dev/tools/bolt-python/reference/context/assistant/thread_context

# Module slack_bolt.context.assistant.thread_context

## Classes

`class AssistantThreadContext (payload: dict)`

Expand source code

```python
class AssistantThreadContext(dict):
    enterprise_id: Optional[str]
    team_id: Optional[str]
    channel_id: str

    def __init__(self, payload: dict):
        dict.__init__(self, **payload)
        self.enterprise_id = payload.get("enterprise_id")
        self.team_id = payload.get("team_id")
        self.channel_id = payload["channel_id"]
```

dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d\[k\] = v dict(\*\*kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2)

### Ancestors

* builtins.dict

### Class variables

`var channel_id : str`

The type of the None singleton.

`var enterprise_id : str | None`

The type of the None singleton.

`var team_id : str | None`

The type of the None singleton.
