# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/avoid-call-gc-suppress-finalize.md

---
title: Avoid calling GC.SuppressFinalize()
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid calling GC.SuppressFinalize()
---

# Avoid calling GC.SuppressFinalize()

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/avoid-call-gc-suppress-finalize`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

As per [C# documentation](https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/implementing-dispose), the `GC.SuppressFinalize()` method should only be called inside the `Dispose()` method.

#### Learn More{% #learn-more %}

- [Documentation on the dispose pattern](https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/implementing-dispose#implement-the-dispose-pattern)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public static void myMethod()
    {
        GC.SuppressFinalize(this);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    public void Dispose()
    {
        Dispose(true);
        GC.SuppressFinalize(this);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 