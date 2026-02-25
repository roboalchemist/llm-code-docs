# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/redundant-modifiers.md

---
title: Avoid redundant modifiers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid redundant modifiers
---

# Avoid redundant modifiers

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/redundant-modifiers`

**Language:** C#

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

When `sealed` is used in the class definition, methods and attributes do not need to define or use the `sealed` modifier.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
public sealed class MyClass {

    public sealed void myMethod() {

    }
    sealed void myMethod() {

    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    public sealed myMethod()
    {
        if (foo) {
            throw new MyException();
        }

    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
