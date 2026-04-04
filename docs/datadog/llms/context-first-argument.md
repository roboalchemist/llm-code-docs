# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/context-first-argument.md

---
title: The Context should be the first argument in a function
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > The Context should be the first argument in a function
---

# The Context should be the first argument in a function

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/context-first-argument`

**Language:** Go

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

In Go, it is a best practice to use the `context` package and pass a `context.Context` as the first argument to functions that are expected to be long-running, have potential timeouts, or require cancellation.

Here are the reasons why using `context` as the first argument is recommended:

1. Cancellation and timeouts: The `context` package provides functionality to handle cancellation and timeouts in a clean and controlled way. By passing a `context.Context` as the first argument, you allow callers of the function to control the lifecycle of the function execution by canceling it or setting timeouts. This promotes better resource management and avoids situations where long-running operations are left unfinished or hang indefinitely.
1. Propagation of Context: By passing the `context.Context` as the first argument, you create a clear and consistent pattern for propagating the context throughout your codebase. This allows the context to flow seamlessly across different function calls, enabling features like cancellation and timeout to be propagated correctly to the lower levels of your program.
1. Testability: Using `context` as the first argument makes it easier to write unit tests for your functions. You can create a `context.Context` object with specific cancellation or timeouts in your tests and validate the behavior of your function under different scenarios. This enables better test coverage and ensures that your functions respond correctly to different context states.
1. Code readability: By making it explicit that your function requires a `context.Context`, you improve the readability of your code. Developers who read your code can immediately understand the intent and requirements of the function just by looking at the function signature. This makes it easier to reason about the behavior of the function in different context scenarios.

By following the convention of using `context` as the first argument, you adhere to Go's idiomatic practices, improve code readability, facilitate testability, and allow for better control and propagation of cancellation and timeouts. This helps in building robust, maintainable, and scalable Go codebases.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
package main

import (
    "context"
)

func main(){
    serve(0, context.TODO())
}

func serve(port int, ctx context.Context){
    fmt.Println(port)
    fmt.Printf("%+v\n", ctx)
}

func serve(port int, blah string, ctx context.Context){
    fmt.Println(port)
    fmt.Printf("%+v\n", ctx)
}

func anotherServe(ctx context.Context, myVar,anotherVar string){
    return
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
package main

import (
    "context"
)

func main(){
    serve(0, context.TODO())
}

func serve(ctx context.Context, port int){
    fmt.Println(port)
    fmt.Printf("%+v\n", ctx)
}

func serve(ctx context.Context, port int, blah string){
    fmt.Println(port)
    fmt.Printf("%+v\n", ctx)
}

func anotherServe(ctx context.Context, myVar,anotherVar string){
    return
}

func displayHelpMessage(ctx workflow.Context, args interface{}, action *something.Action, sb *strings.Builder, executionContext something.ExecutionContext) error {
}


func testAgainWithTesting(t *testing.T, ctx context.Context, stdin io.Reader, stdout io.Writer, stderr io.Writer, args []string) error {
}
```

```go
package main

import (
    "context"
)

func main(){
    serve(0, context.TODO())
}

func serve(ctx context.Context, port int){
    fmt.Println(port)
    fmt.Printf("%+v\n", ctx)
}

func serve(ctx context.Context, port int, blah string){
    fmt.Println(port)
    fmt.Printf("%+v\n", ctx)
}

func anotherServe(ctx context.Context, myVar,anotherVar string){
    return
}

func displayHelpMessage(ctx workflow.Context, args interface{}, action *something.Action, sb *strings.Builder, executionContext something.ExecutionContext) error {
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
