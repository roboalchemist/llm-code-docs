# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/avoid-goto-use.md

---
title: Avoid using goto statements
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using goto statements
---

# Avoid using goto statements

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/avoid-goto-use`

**Language:** C#

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The use of `goto` statements can make your code harder to maintain. A structured control flow statement such as an `if`, a loop, a `continue`, or a `break` can make the code much easier to read.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
string ID = "baz";
switch (ID)
{
    case "foo":
        Console.WriteLine("foo");
        break;
    case "bar":
        Console.WriteLine("bar");
        goto case "baz";
        break;
    case "baz":
        Console.WriteLine("baz");
    default:
        Console.WriteLine("n/a");
        break;
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
string ID = "baz";
switch (ID)
{
    case "foo":
        Console.WriteLine("foo");
        break;
    case "bar":
        Console.WriteLine("bar");
        break;
    case "baz":
        Console.WriteLine("baz");
    default:
        Console.WriteLine("n/a");
        break;
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
