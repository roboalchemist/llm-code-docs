# Source: https://www.inngest.com/docs-markdown/reference/python/functions/create

# Create Function

Define your functions using the `create_function` decorator.

```py
import inngest

@inngest_client.create_function(
    fn_id="import-product-images",
    trigger=inngest.TriggerEvent(event="shop/product.imported"),
)
async def fn(ctx: inngest.Context):
    # Your function code
```

***

## `create_function`

The `create_function` decorator accepts a configuration and wraps a plain function.

### Configuration

- `batch_events` (Batch): Configure how the function should consume batches of events (reference)The maximum number of events a batch can have. Current limit is 100.How long to wait before invoking the function with the batch even if it's not full.
  Current permitted values are between 1 second and 1 minute. If you pass an int then it'll be interpreted in milliseconds.

* `cancel` (Cancel): Define an event that can be used to cancel a running or sleeping function (guide)The event name which will be used to cancelA match expression using arbitrary event data. For example, event.data.user\_id == async.data.user\_id will only match events whose data.user\_id matches the original trigger event's data.user\_id.The amount of time to wait to receive the cancelling event. If you pass an int then it'll be interpreted in milliseconds.

- `debounce` (Debounce): Options to configure function debounce (reference)A unique key expression to apply the debounce to. The expression is evaluated for each triggering event.Expressions are defined using the Common Expression Language (CEL) with the events accessible using dot-notation. Read our guide to writing expressions for more info. Examples:Debounce per customer id: 'event.data.customer\_id'Debounce per account and email address: 'event.data.account\_id + "-" + event.user.email'The time period of which to set the limit. The period begins when the first matching event is received.
  How long to wait before invoking the function with the batch even if it's not full.
  If you pass an int then it'll be interpreted in milliseconds.

* `fn_id` (str): A unique identifier for your function. This should not change between deploys.

- `name` (str): A name for your function. If defined, this will be shown in the UI as a friendly display name instead of the ID.

* `on_failure` (function): A function that will be called only when this Inngest function fails after all retries have been attempted (reference)

- `priority` (Priority): Configure function run prioritization.An expression which must return an integer between -600 and 600 (by default), with higher return values resulting in a higher priority.Examples:Return the priority within an event directly: event.data.priority (where
  event.data.priority is an int within your account's range)Rate limit by a string field: event.data.plan == 'enterprise' ? 180 : 0See reference for more information.

* `rate_limit` (RateLimit): Options to configure how to rate limit function execution (reference)A unique key expression to apply the limit to. The expression is evaluated for each triggering event.Expressions are defined using the Common Expression Language (CEL) with the events accessible using dot-notation. Read our guide to writing expressions for more info. Examples:Rate limit per customer id: 'event.data.customer\_id'Rate limit per account and email address: 'event.data.account\_id + "-" + event.user.email'The maximum number of functions to run in the given time period.The time period of which to set the limit. The period begins when the first matching event is received.
  How long to wait before invoking the function with the batch even if it's not full.
  Current permitted values are from 1 second to 1 minute. If you pass an int then it'll be interpreted in milliseconds.

- `retries` (int): Configure the number of times the function will be retried from 0 to 20. Default: 4

* `throttle` (Throttle): Options to configure how to throttle function executionThe maximum number of functions to run in the given time period.A unique key expression to apply the limit to. The expression is evaluated for each triggering event.Expressions are defined using the Common Expression Language (CEL) with the events accessible using dot-notation. Read our guide to writing expressions for more info. Examples:Rate limit per customer id: 'event.data.customer\_id'Rate limit per account and email address: 'event.data.account\_id + "-" + event.user.email'The time period of which to set the limit. The period begins when the first matching event is received.
  How long to wait before invoking the function with the batch even if it's not full.
  Current permitted values are from 1 second to 1 minute. If you pass an int then it'll be interpreted in milliseconds.

- `idempotency` (string): A key expression used to prevent duplicate events from triggering a function more than once in 24 hours. Read the idempotency guide here.Expressions are defined using the Common Expression Language (CEL) with the original event accessible using dot-notation. Read our guide to writing expressions for more information.

* `trigger` (TriggerEvent | TriggerCron | list\[TriggerEvent | TriggerCron]): What should trigger the function to run. Either an event or a cron schedule. Use a list to specify multiple triggers.

***

## Triggers

### `TriggerEvent`

- `event` (str): The name of the event.

* `expression` (str): A match expression using arbitrary event data. For example, event.data.user\_id == async.data.user\_id will only match events whose data.user\_id matches the original trigger event's data.user\_id.

### `TriggerCron`

- `cron` (str): A unix-cron compatible schedule string. Optional timezone prefix, e.g. TZ=Europe/Paris 0 12 \* \* 5.

### Multiple Triggers

Multiple triggers can be defined by setting the `trigger` option to a list of `TriggerEvent` or `TriggerCron` objects:

```py
import inngest

@inngest_client.create_function(
    fn_id="import-product-images",
    trigger=[
      inngest.TriggerEvent(event="shop/product.imported"),
      inngest.TriggerEvent(event="shop/product.updated"),
    ],
)
async def fn(ctx: inngest.Context):
    # Your function code
```

For more information, see the [Multiple
Triggers](/docs-markdown/guides/multiple-triggers) guide.

***

## Handler

The handler is your code that runs whenever the trigger occurs. Every function handler receives a single object argument which can be deconstructed. The key arguments are `event` and `step`. Note, that scheduled functions that use a `cron` trigger will not receive an `event` argument.

```py
@inngest_client.create_function(
    # Function options
)
async def fn(ctx: inngest.Context):
    # Function code
```

### `ctx`

- `attempt` (int): The current zero-indexed attempt number for this function execution. The first attempt will be 0, the second 1, and so on. The attempt number is incremented every time the function throws an error and is retried.

* `event` (Event): The event payload object that triggered the given function run. The event payload object will match what you send with inngest.send(). Below is an example event payload object:The event payload data.Time (Unix millis) the event was received by the Inngest server.

- `events` (list\[Event]): A list of event objects that's accessible when the batch\_events is set on the function configuration.If batching is not configured, the list contains a single event payload matching the event argument.

* `logger` (logging.Logger): A proxy object around either the logger you provided or the default logger.

- `run_id` (str): The unique ID for the given function run. This can be useful for logging and looking up specific function runs in the Inngest dashboard.

### `step`

The `step` object has a method for each kind of step in the Inngest platform.

If your function is `async` then its type is `Step` and you can use `await` to call its methods. If your function is not `async` then its type is `SyncStep`.

- `run` (Callable): Docs

* `send_event` (Callable): Docs

- `sleep` (Callable): Docs

* `sleep_until` (Callable): Docs

- `_experimental_parallel` (Callable): Docs