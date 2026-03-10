# Source: https://www.inngest.com/docs-markdown/reference/python/steps/wait-for-event

# Wait for event

Wait until the Inngest server receives a specific event.

If an event is received before the timeout then the event is returned. If the timeout is reached then `None` is returned.

## Arguments

- `step_id` (str): Step ID. Should be unique within the function.

* `event` (str): Name of the event to wait for.

- `if_exp` (str | None): Only match events that match this CEL expression. For example, "event.data.height == async.data.height" will only match incoming events whose data.height matches the data.height value for the trigger event.

* `timeout` (int | datetime.timedelta): In milliseconds.

## Examples

```py
@inngest_client.create_function(
    fn_id="my_function",
    trigger=inngest.TriggerEvent(event="app/my_function"),
)
async def fn(ctx: inngest.Context) -> None:
    res = await ctx.step.wait_for_event(
        "wait",
        event="app/wait_for_event.fulfill",
        timeout=datetime.timedelta(seconds=2),
    )
```