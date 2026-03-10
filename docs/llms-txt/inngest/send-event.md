# Source: https://www.inngest.com/docs-markdown/reference/python/steps/send-event

# Send event

> **Callout:** 💡️ This guide is for sending events from inside an Inngest function. To send events outside an Inngest function, refer to the client event sending guide.

Sends 1 or more events to the Inngest server. Returns a list of the event IDs.

## Arguments

- `step_id` (str): Step ID. Should be unique within the function.

* `events` (Event | list\[Event]): 1 or more events to send.Any data to associate with the event.A unique ID used to idempotently trigger function runs. If duplicate event IDs are seen, only the first event will trigger function runs.The event name. We recommend using lowercase dot notation for names (e.g. app/user.created)A timestamp integer representing the time (in milliseconds) at which the event occurred. Defaults to the time the Inngest receives the event.If the ts time is in the future, function runs will be scheduled to start at the given time. This has the same effect as sleeping at the start of the function.Note: This does not apply to functions waiting for events. Functions waiting for events will immediately resume, regardless of the timestamp.

## Examples

```py
@inngest_client.create_function(
    fn_id="my_function",
    trigger=inngest.TriggerEvent(event="app/my_function"),
)
async def fn(ctx: inngest.Context) -> list[str]:
    return await ctx.step.send_event("send", inngest.Event(name="foo"))
```