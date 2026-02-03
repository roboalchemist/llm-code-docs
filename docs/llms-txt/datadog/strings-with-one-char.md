# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/strings-with-one-char.md

---
title: Avoid StartsWith or EndsWith with one character
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid StartsWith or EndsWith with one character
---

# Avoid StartsWith or EndsWith with one character

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/strings-with-one-char`

**Language:** C#

**Severity:** Warning

**Category:** Performance

## Description{% #description %}

This rule is designed to ensure that you use the most efficient methods for string comparison in C#. When using the `StartsWith` or `EndsWith` methods with a single character, the performance can be significantly reduced compared to using the indexer with the first or last index. This is because these methods are designed to work with substrings, not single characters, and therefore involve unnecessary overhead when used in this way.

The importance of this rule lies in writing efficient and performant code. In large-scale applications, using inefficient methods for string comparison can lead to noticeable performance issues. Therefore, it's crucial to use the appropriate methods for each specific use-case.

### Learn More{% #learn-more %}

- [StartsWith documentation](https://learn.microsoft.com/en-us/dotnet/api/system.string.startswith?view=net-8.0#system-string-startswith%28system-char%29)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.Xml;

class MyClass {
    public static void processString(string s)
    {
        bool r1 = s.StartsWith("/");
        bool r2 = s.EndsWith("/");
        data.Contains("\\n");
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System.Xml;

class MyClass {
    public static void processString(string s)
    {
        bool r1 = s.StartsWith('/');
        bool r2 = s.EndsWith('/');
        bool r3 = s.EndsWith("/", StringComparison.InvariantCulture);
        
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 