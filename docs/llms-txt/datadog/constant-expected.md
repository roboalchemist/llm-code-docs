# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/constant-expected.md

---
title: Ensure correct usage of ConstantExpected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure correct usage of ConstantExpected
---

# Ensure correct usage of ConstantExpected

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/constant-expected`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The `ConstantExpected` rule in C# static analysis helps make sure constants are used correctly. Using constants incorrectly can lead to unexpected behavior, bugs, or security issues.

Apply the `ConstantExpected` attribute to parameters that should be constant within a range. This attribute has optional `Min` and `Max` parameters for the inclusive lower and upper bounds. The data type of `Min` and `Max` must match the parameter's data type.

## How to Remediate{% #how-to-remediate %}

To avoid violations, make sure the `ConstantExpected` attribute works with compatible parameter types and that `Min` and `Max` values are in the right order. The `Min` value must be less than or equal to `Max`. Also, `Min` and `Max` should fit within the parameter type's limits. For instance, if the parameter is an 'int', `Min` and `Max` should also be 'int' and within the 'int' range. Following these practices makes your code stronger, easier to maintain, and less error-prone.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
// check https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca1856

// Violation - value not compatible with parameter type.
static void M1([ConstantExpected(Min = "a")] char val) { }
static void M1([ConstantExpected(Min = "a", Max='b')] int val) { }
// Violation - unsupported type for attribute.
static void M2([ConstantExpected] decimal val) { }
// Violation - Min and Max values are inverted.
static void M3([ConstantExpected(Max = 0, Min = 1)] int val) { }
// Violation - value does not fit within the parameter value bounds.
static void M4([ConstantExpected(Min = long.MinValue)] int val) { }
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
static void M1([ConstantExpected(Min = 'a')] char val) { }
static void M2(decimal val) { }
static void M3([ConstantExpected(Min = 0, Max = 1)] int val) { }
static void M4([ConstantExpected(Min = int.MinValue)] int val) { }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
