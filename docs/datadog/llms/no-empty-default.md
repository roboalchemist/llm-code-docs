# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/no-empty-default.md

---
title: Prevent empty default cases
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent empty default cases
---

# Prevent empty default cases

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/no-empty-default`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The default section of a switch should not be empty. If there is an error to raise, throw an exception, print a lock, and emit a metric.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public static bool filter(int target)
    {
        switch(target) {
            case 1:
                doSomething();
                break;
            default:
                break;
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    public static bool filter(int target)
    {
        switch(target) {
            case 1:
                doSomething();
                break;
            default:
                doSomethingElse();
                break;
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
