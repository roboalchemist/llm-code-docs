# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/use-stringbuilder.md

---
title: Prefer StringBuilder when building string in a loop
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer StringBuilder when building string in a loop
---

# Prefer StringBuilder when building string in a loop

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/use-stringbuilder`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

This rule encourages the use of `StringBuilder` when constructing strings inside loops instead of using string concatenation. Using `+` or `+=` to concatenate strings in a loop creates multiple intermediate string instances, which can lead to significant performance overhead due to repeated memory allocation and copying.

Avoiding this pattern is important because strings in C# are immutable, so each concatenation generates a new string object. This can increase memory usage and degrade performance, especially when building large strings or iterating over many elements.

To comply with this rule, use a `StringBuilder` instance to accumulate string content within loops. For example, instantiate a `StringBuilder` before the loop, call `Append` or `AppendLine` inside the loop to add content, and finally convert it to a string with `ToString()` after the loop completes.

By following this approach, you write more efficient, readable, and maintainable code that scales better when dealing with dynamic string construction in iterative contexts.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.Collections.Generic;

public class MyController
{
    public string DoSomething(List<Stuff> listOfStuff)
    {
        string html = "";

        for (int i = 0; i < listOfStuff.Count; i++)
        {
            var stuff = listOfStuff[i];
            html += "<div class='product'><h3>" + stuff.Name + "</h3><p>" + stuff.Description + "</p></div>";
            html = html + "<div class='product'><h3>" + stuff.Name + "</h3><p>" + stuff.Description + "</p></div>";
        }

        return html;
    }
}

public class Stuff
{
    public string Name { get; set; }
    public string Description { get; set; }
    public decimal Price { get; set; }
}
```

```csharp
public class MyController {
    
    public void DoSomething(Iterable listOfStuff) {
        foreach (var stuff in listOfStuff)
        {
            html += $@"
                <div class='product'>
                    <h3>{stuff.Name}</h3>
                    <p>{stuff.Description}</p>
                    <p>Price: ${stuff.Price}</p>
                </div>";
        }
    }
}
```

```csharp
using System.Collections.Generic;

public class MyController
{
    public string DoSomething(List<Stuff> listOfStuff)
    {
        string html = "";

        for (int i = 0; i < listOfStuff.Count; i++)
        {
            var stuff = listOfStuff[i];
            html += $@"
                <div class='product'>
                    <h3>{stuff.Name}</h3>
                    <p>{stuff.Description}</p>
                    <p>Price: ${stuff.Price}</p>
                </div>";
        }

        return html;
    }
}

public class Stuff
{
    public string Name { get; set; }
    public string Description { get; set; }
    public decimal Price { get; set; }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System.Text;
using System.Collections.Generic;

public class MyController
{
    public string DoSomething(IEnumerable<Stuff> listOfStuff)
    {
        var htmlBuilder = new StringBuilder();

        foreach (var stuff in listOfStuff)
        {
            htmlBuilder.AppendLine($@"
                <div class='product'>
                    <h3>{stuff.Name}</h3>
                    <p>{stuff.Description}</p>
                    <p>Price: ${stuff.Price}</p>
                </div>");
        }

        return htmlBuilder.ToString();
    }
}

public class Stuff
{
    public string Name { get; set; }
    public string Description { get; set; }
    public decimal Price { get; set; }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 