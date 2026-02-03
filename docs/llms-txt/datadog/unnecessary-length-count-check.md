# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/unnecessary-length-count-check.md

---
title: Checks for always-true expressions on collections and arrays
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Checks for always-true expressions on collections and arrays
---

# Checks for always-true expressions on collections and arrays

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/unnecessary-length-count-check`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Because the `Length` of an array or `Count` of a collection will never be negative, some expressions will always evaluate to true, and some will always evaluate to false.

```csharp
if (collection.Count >= 0) { /* ... */ }
// Equivalent to
if (true) { /* ... */ }

if (arr.Length < 0) { /* ... */ }
// Equivalent to
if (false) { /* ... */ }
```

This rule warns when always-true or always-false expressions are detected.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.Collections.Generic;
using static System.Linq.Enumerable;

class NonCompliant {
    public static void Main()
    {
        List<char> collection = ['a', 'b', 'c'];
        if (collection.Count >= 0) { /* ... */ }
        if (collection.Count >= 0b0) { /* ... */ }
        if (collection.Count >= 0x0) { /* ... */ }
        if (collection.Count >= -1) { /* ... */ }
        if (collection.Count > -1) { /* ... */ }
        if (collection.Count < 0) { /* ... */ }
        if (collection.Count < -1) { /* ... */ }
		
        char[] array = ['a', 'b', 'c'];
        if (array.Count() >= 0) { /* ... */ }
        if (array.Count() >= 0b0) { /* ... */ }
        if (array.Count() >= 0x0) { /* ... */ }
        if (array.Count() >= -1) { /* ... */ }
        if (array.Count() > -1) { /* ... */ }
        if (array.Count() < 0) { /* ... */ }
        if (array.Count() < -1) { /* ... */ }

        if (array.LongCount() >= 0b0) { /* ... */ }
        if (array.LongCount() >= 0x0) { /* ... */ }
        if (array.LongCount() >= -1) { /* ... */ }
        if (array.LongCount() > -1) { /* ... */ }
        if (array.LongCount() < 0) { /* ... */ }
        if (array.LongCount() < -1) { /* ... */ }

        if (array.Length >= 0) { /* ... */ }
        if (array.Length >= 0b0) { /* ... */ }
        if (array.Length >= 0x0) { /* ... */ }
        if (array.Length >= -1) { /* ... */ }
        if (array.Length > -1) { /* ... */ }
        if (array.Length < 0) { /* ... */ }
        if (array.Length < -1) { /* ... */ }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System.Collections.Generic;
using static System.Linq.Enumerable;

class Compliant {
    public static void Main()
    {
        List<char> collection = ['a', 'b', 'c'];
        if (collection.Count > 0) { /* ... */ }
        if (collection.Count > 0b0) { /* ... */ }
        if (collection.Count > 0x0) { /* ... */ }
        if (collection.Count > 1) { /* ... */ }
        if (collection.Count == 0) { /* ... */ }
		
        char[] array = ['a', 'b', 'c'];
        if (array.Count() > 0) { /* ... */ }
        if (array.Count() > 0b0) { /* ... */ }
        if (array.Count() > 0x0) { /* ... */ }
        if (array.Count() > 1) { /* ... */ }
        if (array.Count() == 0) { /* ... */ }

        if (array.LongCount() > 0) { /* ... */ }
        if (array.LongCount() > 0b0) { /* ... */ }
        if (array.LongCount() > 0x0) { /* ... */ }
        if (array.LongCount() > 1) { /* ... */ }
        if (array.LongCount() == 0) { /* ... */ }

        if (array.Length > 0) { /* ... */ }
        if (array.Length > 0b0) { /* ... */ }
        if (array.Length > 0x0) { /* ... */ }
        if (array.Length > 1) { /* ... */ }
        if (array.Length == 0) { /* ... */ }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 