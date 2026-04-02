Source: https://docs.slack.dev/tools/bolt-python/reference/middleware/message_listener_matches

# Module slack_bolt.middleware.message_listener_matches

## Sub-modules

`[slack_bolt.middleware.message_listener_matches.async_message_listener_matches](async_message_listener_matches.html "slack_bolt.middleware.message_listener_matches.async_message_listener_matches")`

`[slack_bolt.middleware.message_listener_matches.message_listener_matches](message_listener_matches.html "slack_bolt.middleware.message_listener_matches.message_listener_matches")`

## Classes

`class MessageListenerMatches (keyword: str | Pattern)`

Expand source code

```python
class MessageListenerMatches(Middleware):
    def __init__(self, keyword: Union[str, Pattern]):
        """Captures matched keywords and saves the values in context."""
        self.keyword = keyword

    def process(
        self,
        *,
        req: BoltRequest,
        resp: BoltResponse,
        # As this method is not supposed to be invoked by bolt-python users,
        # the naming conflict with the built-in one affects
        # only the internals of this method
        next: Callable[[], BoltResponse],
    ) -> BoltResponse:
        text = req.body.get("event", {}).get("text", "")
        if text:
            m: Optional[Union[Sequence]] = re.findall(self.keyword, text)
            if m is not None and m != []:
                if type(m[0]) is not tuple:
                    m = tuple(m)
                else:
                    m = m[0]
                req.context["matches"] = m  # tuple or list
                return next()

        # As the text doesn't match, skip running the listener
        return resp
```

A middleware can process request data before other middleware and listener functions.

Captures matched keywords and saves the values in context.

### Ancestors

* [Middleware](../middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")

### Inherited members

* `**[Middleware](../middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")**`:
  * `[name](../middleware.html#slack_bolt.middleware.middleware.Middleware.name "slack_bolt.middleware.middleware.Middleware.name")`
  * `[process](../middleware.html#slack_bolt.middleware.middleware.Middleware.process "slack_bolt.middleware.middleware.Middleware.process")`
