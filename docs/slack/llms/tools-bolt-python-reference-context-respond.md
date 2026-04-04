Source: https://docs.slack.dev/tools/bolt-python/reference/context/respond

# Module slack_bolt.context.respond

## Sub-modules

`[slack_bolt.context.respond.async_respond](async_respond.html "slack_bolt.context.respond.async_respond")`

`[slack_bolt.context.respond.internals](internals.html "slack_bolt.context.respond.internals")`

`[slack_bolt.context.respond.respond](respond.html "slack_bolt.context.respond.respond")`

## Classes

`class Respond (*,   response_url: str | None,   proxy: str | None = None,   ssl: ssl.SSLContext | None = None)`

Expand source code

```python
class Respond:
    response_url: Optional[str]
    proxy: Optional[str]
    ssl: Optional[SSLContext]

    def __init__(
        self,
        *,
        response_url: Optional[str],
        proxy: Optional[str] = None,
        ssl: Optional[SSLContext] = None,
    ):
        self.response_url = response_url
        self.proxy = proxy
        self.ssl = ssl

    def __call__(
        self,
        text: Union[str, dict] = "",
        blocks: Optional[Sequence[Union[dict, Block]]] = None,
        attachments: Optional[Sequence[Union[dict, Attachment]]] = None,
        response_type: Optional[str] = None,
        replace_original: Optional[bool] = None,
        delete_original: Optional[bool] = None,
        unfurl_links: Optional[bool] = None,
        unfurl_media: Optional[bool] = None,
        thread_ts: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> WebhookResponse:
        if self.response_url is not None:
            client = WebhookClient(
                url=self.response_url,
                proxy=self.proxy,
                ssl=self.ssl,
            )
            text_or_whole_response: Union[str, dict] = text
            if isinstance(text_or_whole_response, str):
                text = text_or_whole_response
                message = _build_message(
                    text=text,
                    blocks=blocks,
                    attachments=attachments,
                    response_type=response_type,
                    replace_original=replace_original,
                    delete_original=delete_original,
                    unfurl_links=unfurl_links,
                    unfurl_media=unfurl_media,
                    thread_ts=thread_ts,
                    metadata=metadata,
                )
                return client.send_dict(message)
            elif isinstance(text_or_whole_response, dict):
                message = _build_message(**text_or_whole_response)
                return client.send_dict(message)
            else:
                raise ValueError(f"The arg is unexpected type ({type(text_or_whole_response)})")
        else:
            raise ValueError("respond is unsupported here as there is no response_url")
```

### Class variables

`var proxy : str | None`

The type of the None singleton.

`var response_url : str | None`

The type of the None singleton.

`var ssl : ssl.SSLContext | None`

The type of the None singleton.
