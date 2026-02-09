# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/contains-not-any.md

---
title: Use Contains for simple equality
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use Contains for simple equality
---

# Use Contains for simple equality

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/contains-not-any`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

When using only a simple comparison, use `Contains` instead of `Any` as it is more efficient in terms of resources allocation.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.Xml;

class MyClass {
    public static bool filter(IEnumerable<int> values, int target)
    {
        return values.Any(x => target == x);
    }
}
```

```csharp
using System.Xml;

class MyClass {
    public static bool filter(IEnumerable<int> values, int target)
    {
        return values.Any(x => x == target);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System.Xml;

class MyClass {
    public static bool filter1(IEnumerable<int> values, int target)
    {
        return values.Contains(target);
    }
    public static bool filter2(IEnumerable<int> values, int target)
    {
        return values.Any(c => c > target);
    }
    public static bool filter3(IEnumerable<SomeType> values, int target)
    {
        return values.Any(c => c.Id == target);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 