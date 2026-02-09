# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-best-practices/no-nested-ternary.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/no-nested-ternary.md

---
title: Avoid nested operators
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid nested operators
---

# Avoid nested operators

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/no-nested-ternary`

**Language:** C#

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Do not use nested ternary operators, as it makes the code harder to understand and maintain.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public static void routine(bool a, bool b, bool c)
    {
        var foo = a ? b ? "b": "a" : "c";
    }
}
```

```csharp
class MyClass {
    public static void routine(bool a, bool b, bool c)
    {
        var foo = a ? "a" : b ? "b" : "c";
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    public static void routine(bool a, bool b, bool c)
    {
        if (a) {
            if (b) {
                return "ab";
            }
            if(c) {
                return "ac";
            }
        } else {
            if (b) {
                return "b";
            }
            if (c) {
                return "c";
            }
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 