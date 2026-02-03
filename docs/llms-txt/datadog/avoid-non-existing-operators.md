# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/avoid-non-existing-operators.md

---
title: Do not use operators that do not exists
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use operators that do not exists
---

# Do not use operators that do not exists

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/avoid-non-existing-operators`

**Language:** C#

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

Operator `+=` and `-=` do not exist and will lead to inconsistent or undefined behavior.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public void myMethod()
    {
        int myInt1 = 1;
        int myInt2 = 1;
        myInt2 =+ myInt1;
        myInt2 =- myInt1;

    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    public void myMethod()
    {
        int myInt1 = 1;
        int myInt2 = 1;
        myInt2 += myInt1;
        myInt2 -= myInt1;

    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 