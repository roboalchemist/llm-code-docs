Source: https://docs.slack.dev/tools/bolt-python/reference/context/set_status

# Module slack_bolt.context.set_status

## Sub-modules

`[slack_bolt.context.set_status.async_set_status](async_set_status.html "slack_bolt.context.set_status.async_set_status")`

`[slack_bolt.context.set_status.set_status](set_status.html "slack_bolt.context.set_status.set_status")`

## Classes

`class SetStatus (client: slack_sdk.web.client.WebClient, channel_id: str, thread_ts: str)`

Expand source code

```python
class SetStatus:
    client: WebClient
    channel_id: str
    thread_ts: str

    def __init__(
        self,
        client: WebClient,
        channel_id: str,
        thread_ts: str,
    ):
        self.client = client
        self.channel_id = channel_id
        self.thread_ts = thread_ts

    def __call__(
        self,
        status: str,
        loading_messages: Optional[List[str]] = None,
        **kwargs,
    ) -> SlackResponse:
        return self.client.assistant_threads_setStatus(
            channel_id=self.channel_id,
            thread_ts=self.thread_ts,
            status=status,
            loading_messages=loading_messages,
            **kwargs,
        )
```

### Class variables

`var channel_id : str`

The type of the None singleton.

`var client : slack_sdk.web.client.WebClient`

The type of the None singleton.

`var thread_ts : str`

The type of the None singleton.
