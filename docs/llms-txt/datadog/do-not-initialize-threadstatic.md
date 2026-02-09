# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/do-not-initialize-threadstatic.md

---
title: Ensures that a ThreadStatic field is not initialized
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensures that a ThreadStatic field is not initialized
---

# Ensures that a ThreadStatic field is not initialized

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/do-not-initialize-threadstatic`

**Language:** C#

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

When a field has the [ThreadStatic attribute](https://learn.microsoft.com/en-us/dotnet/api/system.threadstaticattribute), it is unique for each thread. In order to have the expected value, the field should either be evaluated lazily, or set to the default.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class NonCompliant {
    [ThreadStatic]
    public static string Foo = "foo";
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class Compliant {
    [ThreadStatic]
    private static string _foo;
    
    public static string Foo {
        get {
            if (_foo == null) {
                _foo = "foo"
            }
            return _foo;
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 