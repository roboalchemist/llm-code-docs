# Source: https://www.inngest.com/docs-markdown/reference/python/steps/invoke

# Invoke&#x20;

Calls another Inngest function, waits for its completion, and returns its output.

## Arguments

- `step_id` (str): Step ID. Should be unique within the function.

* `function` (Function): Invoked function.

- `data` (object): JSON-serializable data that will be passed to the invoked function as event.data.

* `user` (object): JSON-serializable data that will be passed to the invoked function as event.user.

## Examples

```py
@inngest_client.create_function(
    fn_id="fn-1",
    trigger=inngest.TriggerEvent(event="app/fn-1"),
)
async def fn_1(ctx: inngest.Context) -> None:
    return "Hello!"

@inngest_client.create_function(
    fn_id="fn-2",
    trigger=inngest.TriggerEvent(event="app/fn-2"),
)
async def fn_2(ctx: inngest.Context) -> None:
    output = await ctx.step.invoke(
        "invoke",
        function=fn_1,
    )

    # Prints "Hello!"
    print(output)
```

> **Callout:** 💡 step.invoke works within a single app or across apps, since the app ID is built into the function object.