# Source: https://www.inngest.com/docs-markdown/reference/python/steps/invoke_by_id

# Invoke by ID&#x20;

Calls another Inngest function, waits for its completion, and returns its output.

This method behaves identically to the [invoke](/docs-markdown/reference/python/steps/invoke) step method, but accepts an ID instead of the function object. This can be useful for a few reasons:

- Trigger a function whose code is in a different codebase.
- Avoid circular dependencies.
- Avoid undesired transitive imports.

## Arguments

- `step_id` (str): Step ID. Should be unique within the function.

* `app_id` (str): App ID of the invoked function.

- `function_id` (str): ID of the invoked function.

* `data` (object): JSON-serializable data that will be passed to the invoked function as event.data.

- `user` (object): JSON-serializable data that will be passed to the invoked function as event.user.

## Examples

### Within the same app

```py
@inngest_client.create_function(
    fn_id="fn-1",
    trigger=inngest.TriggerEvent(event="app/fn-1"),
)
async def fn_1(ctx: inngest.Context) -> str:
    return "Hello!"

@inngest_client.create_function(
    fn_id="fn-2",
    trigger=inngest.TriggerEvent(event="app/fn-2"),
)
async def fn_2(ctx: inngest.Context) -> None:
    output = ctx.step.invoke_by_id(
        "invoke",
        function_id="fn-1",
    )

    # Prints "Hello!"
    print(output)
```

### Across apps

```py
inngest_client_1 = inngest.Inngest(app_id="app-1")
inngest_client_2 = inngest.Inngest(app_id="app-2")

@inngest_client_1.create_function(
    fn_id="fn-1",
    trigger=inngest.TriggerEvent(event="app/fn-1"),
)
async def fn_1(ctx: inngest.Context) -> str:
    return "Hello!"

@inngest_client_2.create_function(
    fn_id="fn-2",
    trigger=inngest.TriggerEvent(event="app/fn-2"),
)
async def fn_2(ctx: inngest.Context) -> None:
    output = ctx.step.invoke_by_id(
        "invoke",
        app_id="app-1",
        function_id="fn-1",
    )

    # Prints "Hello!"
    print(output)
```