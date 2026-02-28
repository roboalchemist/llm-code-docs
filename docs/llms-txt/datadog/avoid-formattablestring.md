# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/avoid-formattablestring.md

---
title: Avoid FormattableString
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid FormattableString
---

# Avoid FormattableString

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/avoid-formattablestring`

**Language:** C#

**Severity:** Info

**Category:** Performance

## Description{% #description %}

The function `string.Create` prevents unnecessary allocations. It should be preferred over `FormattableString` functions.

#### Learn More{% #learn-more %}

- [Creating Strings with no allocation overhead using String.Create](https://www.stevejgordon.co.uk/creating-strings-with-no-allocation-overhead-using-string-create-csharp)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public static void myFunction(string s)
    {
        Console.WriteLine(FormattableString.CurrentCulture("foobar"));
        Console.WriteLine(FormattableString.Invariant($"Counter: {(int)counter}"));
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    public static void myFunction(string s)
    {
        Console.WriteLine(string.Create(CultureInfo.CurrentCulture, "foobar"));
        Console.WriteLine(string.Create(CultureInfo.InvariantCulture, $"Counter: {(int)counter}"));
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
