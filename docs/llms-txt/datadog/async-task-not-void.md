# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/async-task-not-void.md

---
title: Detects improper usage of void return in an async method
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Detects improper usage of void return in an async method
---

# Detects improper usage of void return in an async method

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/async-task-not-void`

**Language:** C#

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

According to the [task asynchronous programming](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model) (TAP) model, async methods should only return `void` if they are [event handlers](https://learn.microsoft.com/en-us/dotnet/api/system.eventhandler). Otherwise, they should return `Task` or `Task<TResult>`

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class NonCompliant {
    async void AsyncFetch() { /* ... */ }
    async void Click() { /* ... */ }
    async void HandleClick(object sender, EventArgs e, string notEventHandlerDelegateSignature) { /* ... */ }
}

using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Logging.Abstractions;

namespace Gemini.Build.CodeGeneration
{
    public class Logger : ILogger
    {
        public static ILogger Log { get; set; } = NullLogger.Instance;

        void ILogger.Log<TState>(LogLevel logLevel, EventId eventId, TState state, Exception? exception, Func<TState, Exception?, string> formatter)
        {
            Log.Log(logLevel, eventId, state, exception, formatter);
        }

        public bool IsEnabled(LogLevel logLevel)
        {
            return Log.IsEnabled(logLevel);
        }

        public IDisposable BeginScope<TState>(TState state)
        {
            return Log.BeginScope(state);
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class Compliant {
    async Task AsyncFetch() { /* ... */ }
    async void OnClick() { /* ... */ }
    async void HandleClick(object sender, EventArgs e) { /* ... */ }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
