# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/summary-documentation-comment.md

---
title: XML Documentation comments should have a summary
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > XML Documentation comments should have a summary
---

# XML Documentation comments should have a summary

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/summary-documentation-comment`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The rule requires that all classes and methods in C# have a summary XML documentation comment. The summary documentation comment is a special type of XML comment that starts with `/// <summary>` and ends with `/// </summary>`. This comment is used to provide a brief description of the class or method, which can be helpful for other developers, or for generating documentation.

The lack of summary documentation can make the code harder to understand and maintain, especially for large projects or when working in a team. It can be difficult to understand the purpose of a class or method just by its name, especially if it's complex or not self-explanatory. Providing a summary documentation comment can save time and effort for anyone who needs to understand or update the code in the future.

## How to remediate{% #how-to-remediate %}

Ensure that the XML documentation comments (starting with `///`) have the `<summary></summary>` field.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
/// A class doing something
/// A lot of things!
/// Note that XML documentation starts with "///"
public class MyClass()
{
    /// a method doing something
    /// Note that XML documentation starts with "///"
    public void foo() {

    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
// a class doing something
// a lot of things!
public class MyClass()
{
    // a method doing something
    public void foo() {

    }
}
```

```csharp
/// <summary>
/// 
/// </summary>
public class MyClass()
{
    /// <summary>
    /// 
    /// </summary>
    public void foo() {

    }

    /// <inheritdoc />
    public void bar() {

    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 