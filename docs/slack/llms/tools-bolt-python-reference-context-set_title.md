Source: https://docs.slack.dev/tools/bolt-python/reference/context/set_title

# Module slack_bolt.context.set_title

## Sub-modules

`[slack_bolt.context.set_title.async_set_title](async_set_title.html "slack_bolt.context.set_title.async_set_title")`

`[slack_bolt.context.set_title.set_title](set_title.html "slack_bolt.context.set_title.set_title")`

## Classes

`class SetTitle (client: slack_sdk.web.client.WebClient, channel_id: str, thread_ts: str)`

Expand source code

```python
class SetTitle:
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

    def __call__(self, title: str) -> SlackResponse:
        return self.client.assistant_threads_setTitle(
            title=title,
            channel_id=self.channel_id,
            thread_ts=self.thread_ts,
        )
```

### Class variables

`var channel_id : str`

The type of the None singleton.

`var client : slack_sdk.web.client.WebClient`

The type of the None singleton.

`var thread_ts : str`

The type of the None singleton.
