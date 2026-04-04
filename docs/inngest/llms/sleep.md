# Source: https://www.inngest.com/docs-markdown/reference/python/steps/sleep

# Sleep

Sleep for a period of time. Accepts either a `datetime.timedelta` object or a number of milliseconds.

## Arguments

- `step_id` (str): Step ID. Should be unique within the function.

* `duration` (int | datetime.timedelta): How long to sleep. Can be either a number of milliseconds or a datetime.timedelta object.

## Examples

```py
@inngest_client.create_function(
    fn_id="my_function",
    trigger=inngest.TriggerEvent(event="app/my_function"),
)
async def fn(ctx: inngest.Context) -> None:
    await ctx.step.sleep("zzz", datetime.timedelta(seconds=2))
```