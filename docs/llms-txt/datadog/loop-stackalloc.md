# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/loop-stackalloc.md

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

**ID:** `csharp-best-practices/loop-stackalloc`

**Language:** C#

**Severity:** Warning

**Category:** Performance

## Description{% #description %}

This rule warns against using `stackalloc` inside loops. Allocating memory on the stack in each iteration can lead to excessive stack usage, which may cause stack overflow exceptions and degrade application performance. To avoid this issue, allocate the stack memory once outside the loop and reuse it within the loop body.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
for (int i = 0; i < 10; i++)
{
    Span<byte> buffer = stackalloc byte[256];
    buffer.Clear();
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
Span<byte> buffer = stackalloc byte[256];
for (int i = 0; i < 10; i++)
{
    buffer.Clear();
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 