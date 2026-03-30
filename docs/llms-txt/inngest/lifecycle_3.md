# Source: https://www.inngest.com/docs-markdown/reference/python/middleware/lifecycle

# Python middleware lifecycle

The order of middleware lifecycle hooks is as follows:

1. [`transform_input`](#transform-input)
2. [`before_memoization`](#before-memoization)
3. [`after_memoization`](#after-memoization)
4. [`before_execution`](#before-execution)
5. [`after_execution`](#after-execution)
6. [`transform_output`](#transform-output)
7. [`before_response`](#before-response)

All of these functions may be called multiple times in a single function run. For example, if your function has 2 steps then all of the hooks will run 3 times (once for each step and once for the function).

Additionally, there are two hooks when sending events:

1. [`before_send_events`](#before-send-events)
2. [`after_send_events`](#after-send-events)

## Hook reference

### `transform_input`

Called when receiving a request from Inngest and before running any functions. Commonly used to mutate data sent by Inngest, like decryption.

- `ctx` (Context): ctx argument passed to Inngest functions.

* `function` (Function): Inngest function object.

- `steps` (StepMemos): Memoized step data.

### `before_memoization`

Called before checking memoized step data.

### `after_memoization`

Called after exhausting memoized step data.

### `before_execution`

Called before executing "new code". For example, `before_execution` is called after returning the last memoized step data, since function-level code after that step is "new".

### `after_execution`

Called after executing "new code".

### `transform_output`

Called after a step or function returns. Commonly used to mutate data before sending it back to Inngest, like encryption.

- `result` (TransformOutputResult): Only set if there's an error.Step or function output. Since None is a valid output, always call the has\_output method before accessing the output.Step or function output. Since None is a valid output, always call the has\_output method before accessing the output.Step ID.Step type enum. Useful in very rare cases.Step options. Useful in very rare cases.

### `before_response`

Called before sending a response back to Inngest.

### `before_send_events`

Called before sending events to Inngest.

- `events` (list\[Event]): Events to send.

### `after_send_events`

Called after sending events to Inngest.

- `result` (SendEventsResult): Error string if an error occurred.Event IDs.