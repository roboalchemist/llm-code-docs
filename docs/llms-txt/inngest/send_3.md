# Source: https://www.inngest.com/docs-markdown/reference/python/client/send

# Send events

> **Callout:** 💡️ This guide is for sending events from outside an Inngest function. To send events within an Inngest function, refer to the step.send\_event guide.

Sends 1 or more events to the Inngest server. Returns a list of the event IDs.

```py
import inngest

inngest_client = inngest.Inngest(app_id="my_app")

# Call the `send` method if you're using async/await
ids = await inngest_client.send(
    inngest.Event(name="my_event", data={"msg": "Hello!"})
)

# Call the `send_sync` method if you aren't using async/await
ids = inngest_client.send_sync(
    inngest.Event(name="my_event", data={"msg": "Hello!"})
)

# Can pass a list of events
ids = await inngest_client.send(
    [
        inngest.Event(name="my_event", data={"msg": "Hello!"}),
        inngest.Event(name="my_other_event", data={"name": "Alice"}),
    ]
)
```

## `send`

Only for async/await code.

- `events` (Event | list\[Event]): 1 or more events to send.Any data to associate with the event.A unique ID used to idempotently trigger function runs. If duplicate event IDs are seen, only the first event will trigger function runs.The event name. We recommend using lowercase dot notation for names (e.g. app/user.created)A timestamp integer representing the time (in milliseconds) at which the event occurred. Defaults to the time the Inngest receives the event.If the ts time is in the future, function runs will be scheduled to start at the given time. This has the same effect as sleeping at the start of the function.Note: This does not apply to functions waiting for events. Functions waiting for events will immediately resume, regardless of the timestamp.

## `send_sync`

Blocks the thread. If you're using async/await then use `send` instead.

Arguments are the same as `send`.