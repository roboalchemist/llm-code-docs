Source: https://docs.slack.dev/tools/bolt-python/reference/context/ack

# Module slack_bolt.context.ack

## Sub-modules

`[slack_bolt.context.ack.ack](ack.html "slack_bolt.context.ack.ack")`

`[slack_bolt.context.ack.async_ack](async_ack.html "slack_bolt.context.ack.async_ack")`

`[slack_bolt.context.ack.internals](internals.html "slack_bolt.context.ack.internals")`

## Classes

`class Ack`

Expand source code

```python
class Ack:
    response: Optional[BoltResponse]

    def __init__(self):
        self.response: Optional[BoltResponse] = None

    def __call__(
        self,
        text: Union[str, dict] = "",  # text: str or whole_response: dict
        blocks: Optional[Sequence[Union[dict, Block]]] = None,
        attachments: Optional[Sequence[Union[dict, Attachment]]] = None,
        unfurl_links: Optional[bool] = None,
        unfurl_media: Optional[bool] = None,
        response_type: Optional[str] = None,  # in_channel / ephemeral
        # block_suggestion / dialog_suggestion
        options: Optional[Sequence[Union[dict, Option]]] = None,
        option_groups: Optional[Sequence[Union[dict, OptionGroup]]] = None,
        # view_submission
        response_action: Optional[str] = None,  # errors / update / push / clear
        errors: Optional[Dict[str, str]] = None,
        view: Optional[Union[dict, View]] = None,
    ) -> BoltResponse:
        return _set_response(
            self,
            text_or_whole_response=text,
            blocks=blocks,
            attachments=attachments,
            unfurl_links=unfurl_links,
            unfurl_media=unfurl_media,
            response_type=response_type,
            options=options,
            option_groups=option_groups,
            response_action=response_action,
            errors=errors,
            view=view,
        )
```

### Class variables

`var response : [BoltResponse](../../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None`

The type of the None singleton.
