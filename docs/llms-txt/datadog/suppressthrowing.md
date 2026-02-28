# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/suppressthrowing.md

---
title: Do not use ConfigureAwaitOptions.SuppressThrowing with Task
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use ConfigureAwaitOptions.SuppressThrowing with Task
---

# Do not use ConfigureAwaitOptions.SuppressThrowing with Task

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/suppressthrowing`

**Language:** C#

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The `SuppressThrowing` option in `ConfigureAwaitOptions` can't be used with `Task<TResult>`, as it may cause an invalid `TResult` to be returned. This rule detects such cases to ensure the issue is caught during compilation rather than during execution.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
Task<int> t = new Task<int>(() => 1);
t.ConfigureAwait(ConfigureAwaitOptions.SuppressThrowing);
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
Task<int> t = new Task<int>(() => 1);
((Task)t).ConfigureAwait(ConfigureAwaitOptions.SuppressThrowing);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
