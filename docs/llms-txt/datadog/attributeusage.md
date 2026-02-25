# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/attributeusage.md

---
title: Specify how attributes are used
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Specify how attributes are used
---

# Specify how attributes are used

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/attributeusage`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule is important because it helps control the usage of custom attributes in the C# code. Attributes in C# provide a powerful method of associating metadata, or declarative information, with code. However, without specifying how these attributes should be used, it can lead to misuse or confusion among developers.

The `AttributeUsage` attribute dictates where the custom attribute can be applied, helping to prevent improper usage. It can be set to apply to classes, structures, enums, delegates, interfaces, methods, fields, parameters, properties, and events. The `AllowMultiple` property determines whether the attribute can be applied multiple times to the same entity.

## How to remediate{% #how-to-remediate %}

To fix the issues related to this rule, add the `AttributeUsage` attribute when creating your custom attributes. Specify where your attribute should be used by setting appropriate `AttributeTargets` and control the number of times it can be applied to the same entity using the `AllowMultiple` property. For example, `[AttributeUsageAttribute(AttributeTargets.All, AllowMultiple = false)]` specifies that your custom attribute can be applied to any entity but not multiple times to the same entity.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
// should control how the attribute is used
public class MyNewAttribute : Attribute
{
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
[System.AttributeUsage(AttributeTargets.All, AllowMultiple = false)]
public class MyNewAttribute : Attribute
{
}
```

```csharp
[AttributeUsageAttribute(AttributeTargets.All, AllowMultiple = false)]
public class MyNewAttribute : Attribute
{
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
