# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/use-assembly-load.md

---
title: Use Assembly.Load
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use Assembly.Load
---

# Use Assembly.Load

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/use-assembly-load`

**Language:** C#

**Severity:** Notice

**Category:** Error Prone

## Description{% #description %}

This rule is intended to catch when `Assembly.LoadFrom`, `Assembly.LoadFile`, or `Assembly.LoadWithPartialName`  are used. DataDog recommends using `Assembly.Load` which will include the full specification of the DLL that needs to be loaded. The other methods might end up with another one that could lead to unexpected behavior.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
static void Main(string[] args)
{
    Assembly.LoadFrom("");
    Assembly.LoadFile("");
    Assembly.LoadWithPartialName("");
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
static void Main(string[] args)
{
    Assembly.Load("");
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
