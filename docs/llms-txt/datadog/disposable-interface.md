# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/disposable-interface.md

---
title: Classes with Dispose() should implement IDisposable
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Classes with Dispose() should implement IDisposable
---

# Classes with Dispose() should implement IDisposable

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/disposable-interface`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

`IDisposable` provides an interface for the cleanup of unmanaged resources through the function `void Dispose()`.

To avoid confusion, this rule ensures that any class that exposes a `public void Dispose()` function must implement `IDisposable`.

#### Learn More{% #learn-more %}

- [IDisposable documentation](https://learn.microsoft.com/en-us/dotnet/api/system.idisposable?view=net-8.0)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public void Dispose()
    {
        // contents of method
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass: IFoobar, IDisposable {
    public void Dispose()
    {
        // contents of method
    }
}
```

```csharp
class MyClass: IDisposable {
    public void Dispose()
    {
        // contents of method
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 