# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/condition-always-true.md

---
title: Avoid conditions that are always true
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid conditions that are always true
---

# Avoid conditions that are always true

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/condition-always-true`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In C#, having conditions that are **always true** (or always false) is generally a **bad practice** because it leads to **unreachable code, logic errors, and maintainability issues**.

## How to Remediate{% #how-to-remediate %}

- Replace true with a meaningful, dynamic condition.
- Use variables, method results, or flags to evaluate logic properly.
- Remove useless condition branches

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
// Count cannot be negative
if (myList.Count < 0) {
    // do something
}

// use double.IsNan instead
if (x == double.NaN) {
    // do something
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp

if (myList.Count >= 0) {
    // do something
}


if (double.isNaN(x)) {
    // do something
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 