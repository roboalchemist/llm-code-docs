# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/ensure-self-type-parameter.md

---
title: Enforce correct TSelf parameter usage
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce correct TSelf parameter usage
---

# Enforce correct TSelf parameter usage

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/ensure-self-type-parameter`

**Language:** C#

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

This rule enforces the correct usage of the `TSelf` parameter in C#. When implementing an interface that requires a `TSelf` type parameter, such as `IParsable<TSelf>`, the `TSelf` parameter should be the same as the type that is implementing the interface. This is important because it ensures type safety and allows for correct usage of the interface's methods.

In the non-compliant code example, the class `MyDate` is implementing the `IParsable<TSelf>` interface but is using `DateOnly` for the `TSelf` parameter. This is incorrect because the `TSelf` parameter should be `MyDate`, the type that is implementing the interface.

To avoid violating this rule, always use the type that is implementing the interface for the `TSelf` parameter.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System;

// The 'IParsable<TSelf>' requires the 'TSelf' type parameter to be filled with the derived type 'MyDate'
public readonly struct MyDate : IParsable<DateOnly> {
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System;

public readonly class MyDate : IParsable<MyDate> { 
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 