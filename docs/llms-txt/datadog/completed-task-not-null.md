# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/completed-task-not-null.md

---
title: Return a Task and not `null`
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Return a Task and not `null`
---

# Return a Task and not `null`

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/completed-task-not-null`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule emphasizes the importance of always returning a `Task` from asynchronous methods in C#, instead of `null`. Returning `null` from an async method can lead to `NullReferenceException` errors at runtime when the returned task is awaited. This can make debugging more difficult and can lead to unexpected behavior or bugs in your application.

The importance of this rule stems from the fact that it's a common best practice in asynchronous programming. It ensures that your asynchronous methods always return a valid task that can be awaited, regardless of the execution path of your method. This can make your asynchronous code easier to understand and maintain.

## How to Remediate{% #how-to-remediate %}

To fix this issue, always return a completed `Task` or `Task<T>` from your asynchronous methods instead of `null`. You can use `Task.CompletedTask` to return a completed task without a result, or `Task.FromResult(result)` to return a completed task with a result. For example: `return Task.FromResult<object>(null);` This will ensure that your asynchronous methods are always returning a valid task that can be awaited.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
public class {
    Task<object> GetAsync()
    {
        return null;
    }
}
```

```csharp
Task<object> GetAsync()
{
    return null;
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
Task<object> GetAsync()
{
    return Task.FromResult<object>(null);
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
