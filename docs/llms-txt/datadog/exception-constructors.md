# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/exception-constructors.md

---
title: When inheriting exception, implement all constructors
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > When inheriting exception, implement all constructors
---

# When inheriting exception, implement all constructors

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/exception-constructors`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule stipulates that when creating a custom exception by inheriting from the `Exception` class, all the constructors of the base `Exception` class should be implemented. This is important because it ensures that your custom exception behaves consistently with the built-in exceptions in C#. By doing so, you provide more flexibility for the code that throws your exception, allowing it to pass along a message, an inner exception, or both, which can be extremely helpful when debugging.

Non-compliance with this rule can lead to unexpected behavior and make debugging difficult, as some information might not be propagated correctly when the exception is thrown.

## How to remediate?{% #how-to-remediate %}

To fix this rule always implement the following three constructors when creating a custom exception: a parameterless constructor, a constructor that takes a string message, and a constructor that takes a string message and an inner exception. For example:

```
public class MyException : Exception
{
    public MyException() : base()
    {
    }

    public MyException(string message) : base(message)
    {
    }

    public MyException(string message, Exception innerException) : base(message, innerException)
    {
    }
}
```

By following this practice, you ensure that your custom exceptions can be used just like any other exceptions in C#.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
public class MyException : Exception
{
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
public class MyException : Exception
{
    public MyException() : base()
    {
    }

    public MyException(string message) : base(message)
    {
    }

    public MyException(string message, Exception innerException) : base(message, innerException)
    {
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 