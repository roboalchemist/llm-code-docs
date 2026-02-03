# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/avoid-unsafe.md

---
title: Avoid unsafe blocks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid unsafe blocks
---

# Avoid unsafe blocks

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/avoid-unsafe`

**Language:** C#

**Severity:** Notice

**Category:** Security

**CWE**: [823](https://cwe.mitre.org/data/definitions/823.html)

## Description{% #description %}

Avoid `unsafe` code blocks as much as possible. While `unsafe` blocks provide access to some important features of the C# language, you need to avoid using them as much as possible. For example, `unsafe` code allows developers to use pointers, but pointers and pointers arithmetic can lead to critical security issues. Unsafe code should be avoided or at least clearly identified in a small scope.

#### Learn More{% #learn-more %}

- [C# reference: unsafe code](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/unsafe-code)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.IO;
using System.Security.Cryptography;

class MyClass {
    public void myMethod
    {
        unsafe{
            // statements
        }
       
    }
}
```

```csharp
using System.IO;
using System.Security.Cryptography;

class MyClass {
    public unsafe void myMethod
    {
       // statements
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System.IO;
using System.Security.Cryptography;

class MyClass {
    public void myMethod
    {
       // statements
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 