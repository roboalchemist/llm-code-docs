# Source: https://www.inngest.com/docs-markdown/reference/python/steps/sleep-until

# Sleep until

Sleep until a specific time. Accepts a `datetime.datetime` object.

## Arguments

- `step_id` (str): Step ID. Should be unique within the function.

* `until` (datetime.datetime): Time to sleep until.

## Examples

```py
@inngest_client.create_function(
    fn_id="my_function",
    trigger=inngest.TriggerEvent(event="app/my_function"),
)
async def fn(ctx: inngest.Context) -> None:
    await ctx.step.sleep_until(
        "zzz",
        datetime.datetime.now() + datetime.timedelta(seconds=2),
    )
```