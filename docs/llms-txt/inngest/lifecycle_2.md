# Source: https://www.inngest.com/docs-markdown/reference/typescript/v4/middleware/lifecycle

# Middleware lifecycle

Middleware lets you hook into function execution to add cross-cutting concerns like logging, error handling, and dependency injection. Middleware is class-based: you extend `Middleware.BaseMiddleware` and define hook methods.

## Creating middleware

Extend `Middleware.BaseMiddleware` and override the hooks you need:

```ts
import { Middleware } from "inngest";

class MyMiddleware extends Middleware.BaseMiddleware {
  // Override hook methods here
}
```

Register middleware at the client level (applies to all functions) or the function level (applies to one function):

```ts
// Client level
const inngest = new Inngest({
  id: "my-app",
  middleware: [MyMiddleware],
});

// Function level
inngest.createFunction({
  id: "my-fn",
  middleware: [MyMiddleware],
  triggers: { event: "app/user.created" },
}, async ({ event }) => {
  // ...
});
```

> **Callout:** A fresh middleware instance is created for every request, so you can safely use instance properties (this) to store per-request state without worrying about leaks between runs.

## Execution lifecycle

The following shows the order in which hooks are called during a request. This is the key mental model for understanding middleware:

1. **`wrapRequest()`** - Outermost wrapper around the entire HTTP request
2. **`transformFunctionInput()`** - Modify `ctx` before the function handler runs
3. **`wrapFunctionHandler()`** - Wrap function execution (e.g. for `AsyncLocalStorage`)
4. **`onMemoizationEnd()`** - After all memoized steps resolve
5. **`onRunStart()`** - First attempt only (attempt 0, no memoized steps)
6. Per step:
   - `transformStepInput()` → `wrapStep()` → `onStepStart()` → `wrapStepHandler()` → execute → `onStepComplete()` / `onStepError()`
7. **`onRunComplete()`** / **`onRunError()`** - When the function finishes

Event sending (`transformSendEvent()` → `wrapSendEvent()`) is not part of this fixed sequence. It runs whenever `inngest.send()` or `step.sendEvent()` is called.

> **Callout:** Hooks you don't define have zero overhead: the SDK skips them entirely. Only override the hooks you need.

## Observable hooks

Observable hooks (`on*`) are call-and-forget. They receive read-only arguments and do not return a value. Use them for logging, metrics, and side effects. Errors thrown in observable hooks are caught and logged, not propagated to the run or step.

***

### `onRunStart`

Called once on the very first attempt of a run (attempt 0, no memoized steps). Not called on subsequent retries or replays.

Will not call if the first attempt fails to reach the app (e.g. a network error).

- `ctx`: The function context.

* `functionInfo`: Metadata about the function being executed.

***

### `onRunComplete`

Called when a function completes successfully.

- `ctx`: The function context.

* `functionInfo`: Metadata about the function.

- `output`: The successful return value of the function.

***

### `onRunError`

Called each time a function throws an error.

- `ctx`: The function context.

* `error`: The error that was thrown.

- `functionInfo`: Metadata about the function.

* `isFinalAttempt`: Whether this is the last retry attempt before the run permanently fails.

***

### `onStepStart`

Called before a step handler runs. Only called for `step.run` and `step.sendEvent`.

- `ctx`: The function context.

* `functionInfo`: Metadata about the function.

- `stepInfo`: Metadata about the step being executed.

***

### `onStepComplete`

Called when a step succeeds. Only called for `step.run` and `step.sendEvent`. Never called for memoized steps.

- `ctx`: The function context.

* `functionInfo`: Metadata about the function.

- `output`: The successful return value of the step.

* `stepInfo`: Metadata about the step.

***

### `onStepError`

Called when a step throws an error. Only called for `step.run` and `step.sendEvent`. Never called for memoized steps.

- `ctx`: The function context.

* `error`: The error that was thrown.

- `functionInfo`: Metadata about the function.

* `isFinalAttempt`: Whether this is the last retry attempt for this step.

- `stepInfo`: Metadata about the step.

***

### `onMemoizationEnd`

Called once per request after all memoized steps have resolved. On the first request (no memoized steps), called immediately.

Use cases for this hook are limited. It's primarily useful for logging or metrics that should run after all memoized steps have resolved.

- `ctx`: The function context.

* `functionInfo`: Metadata about the function.

## Wrapping hooks

Wrapping hooks (`wrap*`) follow an onion model: you **must** call `next()` to continue processing. Code before `next()` runs on the way in, code after runs on the way out.

```ts
class MyMiddleware extends Middleware.BaseMiddleware {
  async wrapFunctionHandler({ next }: Middleware.WrapFunctionHandlerArgs) {
    console.log("before");
    const result = await next();
    console.log("after");
    return result;
  }
}
```

With multiple middleware, they nest: middleware 1 wraps middleware 2 wraps the inner handler.

***

### `wrapRequest`

Wraps the entire HTTP request

Example use cases: auth, top-level metrics, or error boundaries.

- `functionInfo`: Metadata about the function.

* `next`: Must call to continue processing. Returns the HTTP response.

- `requestInfo`: The incoming HTTP request metadata (headers, URL, method).

* `runId`: The ID of the current run.

***

### `wrapFunctionHandler`

Wraps function execution. `next()` resolves when the function completes.

Example use cases: `AsyncLocalStorage`, error transformation, timing, or [inserting steps](/docs-markdown/reference/typescript/v4/middleware/examples#inserting-steps).

> **Callout:** next() only resolves when the function fully completes or errors. When a new step is discovered, next() never resolves for that request. It intentionally hangs until garbage collection deletes it.

- `ctx`: The function context.

* `functionInfo`: Metadata about the function.

- `next`: Must call to execute the function handler.

***

### `wrapStep`

Wraps every step, including memoized steps and all step kinds (`step.run`, `step.sleep`, `step.invoke`, etc.).

Example use cases: deserialize memoized data, [insert steps](/docs-markdown/reference/typescript/v4/middleware/examples#inserting-steps).

> **Callout:** If the step is not memoized, next() never resolves for that request. The method intentionally hangs until garbage collection deletes it.

- `ctx`: The function context.

* `functionInfo`: Metadata about the function.

- `next`: Must call to continue processing the step.

* `stepInfo`: Metadata about the step. Check stepInfo.memoized to differentiate memoized vs fresh.

***

### `wrapStepHandler`

Wraps step handler execution. Only called for `step.run` and `step.sendEvent`.

Example use cases: serialize step output, [error handling](/docs-markdown/reference/typescript/v4/middleware/examples#error-handling), or timing.

- `ctx`: The function context.

* `functionInfo`: Metadata about the function.

- `next`: Must call to execute the step handler.

* `stepInfo`: Metadata about the step.

***

### `wrapSendEvent`

Wraps event sending via `inngest.send()` or `step.sendEvent()`.

Example use cases: backup on send failure, metrics.

- `events`: The events being sent.

* `functionInfo`: Metadata about the function, or null if called outside a function (e.g. inngest.send()).

- `next`: Must call to send the events.

## Transform hooks

Transform hooks (`transform*`) receive arguments and return a modified copy. Use them to inject dependencies, modify inputs, or enrich events.

***

### `transformFunctionInput`

Modify the function context before the handler runs.

Example use cases: dependency injection, deserialize event data.

- `ctx`: The function context. Add properties here to inject them into the function handler.

* `functionInfo`: Metadata about the function.

- `steps`: A record of memoized step data keyed by hashed step ID.

***

### `transformStepInput`

Modify step options or input before a step runs.

Example use cases: serialize `step.invoke` data, bust memoization cache (i.e. change step ID).

- `functionInfo`: Metadata about the function.

* `stepInfo`: Partial step metadata.

- `stepOptions`: The options passed to the step (first argument).

* `input`: Arguments passed to the step function (after ID and handler).

***

### `transformSendEvent`

Modify events before they are sent.

Example use cases: serialize event data, add metadata.

- `events`: The events being sent. Return a modified copy to change them.

* `functionInfo`: Metadata about the function, or null if called outside a function.

## Output type transforms

Output type transforms are `declare` properties that control how TypeScript types function and step return values. They have no runtime behavior — they only affect the type system.

By default, the SDK assumes all return values are serialized to JSON, so types like `Date` become `string`. If your middleware changes serialization behavior at runtime (e.g. via [`wrapStepHandler`](#wrapstephandler)), declare a corresponding type transform so TypeScript reflects the actual runtime types.

> **Callout:** Type transforms only affect types. You are responsible for ensuring the declared transform matches your runtime transformation.

Both transforms use the `Middleware.StaticTransform` pattern to imitate higher-kinded types. For example, a normal generic type that preserves `Date` instead of Jsonifying it:

```ts
// A normal generic type
type PreserveDate<In> = In extends Date ? Date : Jsonify<In>;
```

As a `StaticTransform`, this becomes an interface where `this["In"]` replaces the generic parameter and `Out` is the result:

```ts
import { Middleware } from "inngest";

// The same logic as a StaticTransform
interface PreserveDate extends Middleware.StaticTransform {
  Out: this["In"] extends Date ? Date : Jsonify<this["In"]>;
}
```

- `In`: The original return type. Set automatically by the SDK — do not set this yourself.

* `Out`: The transformed type. Define this to compute the output type based on In.

When multiple middleware declare transforms, they are chained in registration order: the `Out` of one becomes the `In` of the next.

***

### `functionOutputTransform`

Declares how function return types are transformed. By default, return types are Jsonified (e.g. `Date` becomes `string`).

```ts
import { Middleware } from "inngest";

interface PreserveDate extends Middleware.StaticTransform {
  Out: this["In"] extends Date ? Date : Jsonify<this["In"]>;
}

class MyMiddleware extends Middleware.BaseMiddleware {
  declare functionOutputTransform: PreserveDate;
}
```

***

### `stepOutputTransform`

Declares how step output types are transformed. By default, output types are Jsonified (e.g. `Date` becomes `string`).

```ts
import { Middleware } from "inngest";

interface PreserveDate extends Middleware.StaticTransform {
  Out: this["In"] extends Date ? Date : Jsonify<this["In"]>;
}

class MyMiddleware extends Middleware.BaseMiddleware {
  declare stepOutputTransform: PreserveDate;
}
```

***

## Static hooks

### `onRegister`

Called once when the middleware class is registered with a client or function.

Example use cases: one-time setup.

```ts
class MyMiddleware extends Middleware.BaseMiddleware {
  static onRegister({ client, functionInfo }: Middleware.OnRegisterArgs) {
    // One-time setup
  }
}
```

- `client`: The Inngest client instance.

* `functionInfo`: Metadata about the function, or null for client-level middleware.

## Important notes

- **Performance** - Undefined hooks have zero overhead. The SDK checks for hook presence and skips entirely if not defined.
- **Immutability** - Observable and wrapping hook arguments are deeply read-only. Do not mutate them.
- **`next()` is required** - Wrapping hooks must call `next()` or the request will hang.
- **Instance per request** - A new middleware instance is created for each request, so instance state is safe to use within a single request.