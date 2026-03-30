# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/reference-documentation-comment.md

---
title: Document comments should reference existing parameters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Document comments should reference existing parameters
---

# Document comments should reference existing parameters

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/reference-documentation-comment`

**Language:** C#

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule emphasizes the importance of accurately documenting method parameters in C#. Inaccurate or missing documentation can lead to confusion and mistakes when other developers use your code. The XML comments above a method, specifically the `<param>` tags, should match the actual parameters of the method.

The violation occurs when there is a discrepancy between the parameters mentioned in the XML comments and the actual parameters of the method. This could be a misspelled parameter name or a parameter mentioned in the comments that does not exist in the method signature.

## How to Remediate{% #how-to-remediate %}

To fix this issue, always ensure that your XML comments accurately reflect your method signatures. Review your comments carefully whenever you add, remove, or rename method parameters. This not only prevents this rule violation but also improves the clarity and maintainability of your code. For example, in the method `public void foo(string foo, string bar)`, the XML comment should include `<param name="foo"></param>` and `<param name="bar"></param>` to accurately document the parameters.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp

/// a method doing something
/// <param name="fooo"></param>
public void foo(string foo) {

}
```

```csharp
public class MyClass()
{
    /// a method doing something
    /// <param name="fooo"></param>
    public void foo(string foo) {

    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
/// <summary>
/// Creates an instance of the specified .NET type from the <see cref="JToken"/> using the specified <see cref="JsonSerializer"/>.
/// </summary>
/// <typeparam name="T">The object type that the token will be deserialized to.</typeparam>
/// <param name="jsonSerializer">The <see cref="JsonSerializer"/> that will be used when creating the object.</param>
/// <returns>The new object created from the JSON value.</returns>
public T? ToObject<T>(JsonSerializer jsonSerializer)
{
    return (T?)ToObject(typeof(T), jsonSerializer);
}


/// <summary>
/// Returns the JSON for this token using the given formatting and converters.
/// </summary>
/// <param name="formatting">Indicates how the output should be formatted.</param>
/// <param name="converters">A collection of <see cref="JsonConverter"/>s which will be used when writing the token.</param>
/// <returns>The JSON for this token using the given formatting and converters.</returns>
[RequiresUnreferencedCode(MiscellaneousUtils.TrimWarning)]
[RequiresDynamicCode(MiscellaneousUtils.AotWarning)]
public string ToString(Formatting formatting, params JsonConverter[] converters)
{
}
```

```csharp





public class MyClass()
{
    /// a method doing something
    /// <param name="foo"></param>
    public void foo(string foo, string bar) {

    }
    /// <summary>
    /// When implemented, controls the binding of a serialized object to a type.
    /// </summary>
    /// <param name="wefwe">The type of the object the formatter creates a new instance of.</param>
    /// <param name="wef">Specifies the <see cref="Assembly"/> name of the serialized object.</param>
    /// <param name="wefwe">Specifies the <see cref="System.Type"/> name of the serialized object.</param>
    void foo(string wefwe, out string? wef, out string? wefwe);
}
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
