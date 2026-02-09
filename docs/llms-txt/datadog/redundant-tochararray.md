# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/redundant-tochararray.md

---
title: Suggest using string's indexer property over toCharArray()
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Suggest using string's indexer property over toCharArray()
---

# Suggest using string's indexer property over toCharArray()

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/redundant-tochararray`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

When using a `for each` statement to iterate over a string's characters, using `ToCharArray()` is redundant and unnecessary, as the `string` type has [indexer](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/indexers/) that allows access to each `char`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class NonCompliant
{
    public static void Main()
    {
        string str1 = "foo";
        foreach (char ch in str1.toCharArray())
		{
		    Console.WriteLine($"{ch}");
		}
        foreach (char ch in "foo".toCharArray())
		{
		    Console.WriteLine($"{ch}");
		}
		var obj1 = new { str1 = "foo" };
        foreach (char ch in obj1.str1.toCharArray())
		{
		    Console.WriteLine($"{ch}");
		}
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class Compliant
{
    public static void Main()
    {
        string str1 = "foo";
        foreach (char ch in str1)
		{
		    Console.WriteLine($"{ch}");
		}
        foreach (char ch in "foo")
		{
		    Console.WriteLine($"{ch}");
		}
        var obj1 = new { str1 = "foo" };
        foreach (char ch in obj1.str1)
		{
		    Console.WriteLine($"{ch}");
		}
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 