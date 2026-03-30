# Source: https://docs.wandb.ai/weave/guides/tracking/tracing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Understand Ops and Calls

> Learn how Ops and Calls create the foundation of W&B Weave's tracing system.

## Ops

An **Op** is a versioned, tracked function. When you decorate a function with `@weave.op()` (Python) or wrap it with `weave.op()` (TypeScript), Weave automatically captures its code, inputs, outputs, and execution metadata. Ops are the building blocks of tracing, evaluation scorers, and any tracked computation.

<CodeGroup>
  ```python Python theme={null}
      @weave.op
      async def my_function(){
        ...  }
  ```

  ```typescript Typescript theme={null}
  function myFunction() {
      ...
  }

  const myFunctionOp = weave.op(myFunction)
  ```
</CodeGroup>

## Calls

A **Call** is a logged execution of an Op. Every time an Op runs, Weave creates a Call that captures:

* Input arguments
* Output value
* Timing and latency
* Parent-child relationships (for nested calls)
* Any errors that occurred

Calls show up as **Traces** in the Weave UI and provide the data for debugging, analysis, and evaluation. For the full Call object structure and properties, see the [Call schema reference](/weave/guides/tracking/call-schema-reference).

Calls are similar to spans in the [OpenTelemetry](https://opentelemetry.io) data model. A Call can:

* Belong to a Trace (a collection of calls in the same execution context)
* Have parent and child Calls, forming a tree structure
