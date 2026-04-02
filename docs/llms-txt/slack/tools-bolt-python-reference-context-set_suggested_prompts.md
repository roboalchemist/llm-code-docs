Source: https://docs.slack.dev/tools/bolt-python/reference/context/set_suggested_prompts

# Module slack_bolt.context.set_suggested_prompts

## Sub-modules

`[slack_bolt.context.set_suggested_prompts.async_set_suggested_prompts](async_set_suggested_prompts.html "slack_bolt.context.set_suggested_prompts.async_set_suggested_prompts")`

`[slack_bolt.context.set_suggested_prompts.set_suggested_prompts](set_suggested_prompts.html "slack_bolt.context.set_suggested_prompts.set_suggested_prompts")`

## Classes

`class SetSuggestedPrompts (client: slack_sdk.web.client.WebClient, channel_id: str, thread_ts: str)`

Expand source code

```python
class SetSuggestedPrompts:
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
        prompts: Sequence[Union[str, Dict[str, str]]],
        title: Optional[str] = None,
    ) -> SlackResponse:
        prompts_arg: List[Dict[str, str]] = []
        for prompt in prompts:
            if isinstance(prompt, str):
                prompts_arg.append({"title": prompt, "message": prompt})
            else:
                prompts_arg.append(prompt)

        return self.client.assistant_threads_setSuggestedPrompts(
            channel_id=self.channel_id,
            thread_ts=self.thread_ts,
            prompts=prompts_arg,
            title=title,
        )
```

### Class variables

`var channel_id : str`

The type of the None singleton.

`var client : slack_sdk.web.client.WebClient`

The type of the None singleton.

`var thread_ts : str`

The type of the None singleton.
