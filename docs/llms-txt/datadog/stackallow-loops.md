# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/stackallow-loops.md

---
title: Do not use stackalloc in loops
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use stackalloc in loops
---

# Do not use stackalloc in loops

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/stackallow-loops`

**Language:** C#

**Severity:** Warning

**Category:** Performance

## Description{% #description %}

The rule "Do not use stackalloc in loops" is crucial to maintain efficient memory usage in your C# applications. `stackalloc` is a keyword in C# that allows you to allocate a block of memory on the stack, which is a limited resource. When used inside a loop, `stackalloc` may cause a rapid increase in memory usage that could lead to a StackOverflowException, especially if the loop iteration count is high or unpredictable.

It is important to remember that stack space is limited, and overuse can lead to stack overflow errors, which are generally hard to recover from. The memory allocated by stackalloc is automatically freed when the method that contains the `stackalloc` expression returns, but in a loop, the memory allocated in each iteration will not be freed until the method returns, which could be much later.

## How to Remediate{% #how-to-remediate %}

Use `stackalloc` outside loops, preferably in a method scope where the allocated memory size is clearly defined and limited. You can clear or reset the buffer after each iteration if needed. This practice ensures that the `stackalloc` memory is efficiently managed and prevents potential stack overflow issues.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System;

class Program
{
    static void Main()
    {
        for (int i = 0; i < 10; i++)
        {
            Span<int> buffer = stackalloc int[10];
            buffer[0] = i;
            Console.WriteLine(buffer[0]);
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System;

class Program
{
    static void Main()
    {
        Span<int> buffer = stackalloc int[10]; // stackalloc used only once, outside the loop

        for (int i = 0; i < 10; i++)
        {
            buffer.Clear(); // Optional: reset buffer contents
            buffer[0] = i;
            Console.WriteLine(buffer[0]);
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 