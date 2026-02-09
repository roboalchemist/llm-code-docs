# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/asspan-instead-of-range.md

---
title: Use AsSpan instead of range-based indexers for string
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use AsSpan instead of range-based indexers for string
---

# Use AsSpan instead of range-based indexers for string

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/asspan-instead-of-range`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule recommends using `AsSpan` over range-based indexers when manipulating strings in CSharp. By using `AsSpan`, you access a substring without creating a new string, which reduces memory allocation and avoids unnecessary garbage collection. Range-based indexers, on the other hand, can lead to unnecessary memory use by creating new strings.

This rule helps improve memory efficiency and performance, especially with large strings or many string changes. It also makes your code clearer and easier to maintain by showing you're working with part of a strong instead of making a new one.

## How to fix{% #how-to-fix %}

Use the `AsSpan` method to handle substrings efficiently. For example, instead of `str[1..3]`, use `str.AsSpan()[1..3]`. This prevents unnecessary string creation and improves efficiency.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
ReadOnlySpan<char> slice = str[1..3];
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
ReadOnlySpan<char> slice = str.AsSpan(1, 3);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 