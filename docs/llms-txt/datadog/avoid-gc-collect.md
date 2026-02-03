# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/avoid-gc-collect.md

---
title: Avoid using GC.Collect
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using GC.Collect
---

# Avoid using GC.Collect

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/avoid-gc-collect`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

The `GC.Collect` method forces a garbage collector to run to free their memory. Using this method is usually not necessary and can impact your applications performance greatly as it may need to block all threads while it examines every object in memory to potential cleanup.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
static void Main(string[] args)
{
  GC.Collect();
  GC.Collect(42, GCCollectionMode.Optimized);
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 