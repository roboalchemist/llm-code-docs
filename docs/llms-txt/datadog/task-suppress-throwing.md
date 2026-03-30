# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/task-suppress-throwing.md

---
title: No ConfigureAwaitOptions.SuppressThrowing with Task
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > No ConfigureAwaitOptions.SuppressThrowing with Task<T>
---

# No ConfigureAwaitOptions.SuppressThrowing with Task<T>

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/task-suppress-throwing`

**Language:** C#

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule prohibits using `ConfigureAwaitOptions.SuppressThrowing` directly on instances of `Task<T>`. The `SuppressThrowing` option is intended to be applied only on non-generic `Task` objects. Applying it on `Task<T>` can lead to unexpected behavior or runtime issues because `Task<T>` handles exceptions differently.

To comply with this rule, explicitly cast `Task<T>` instances to `Task` before calling `ConfigureAwait(ConfigureAwaitOptions.SuppressThrowing)`. For example: `((Task)t).ConfigureAwait(ConfigureAwaitOptions.SuppressThrowing);`. This approach ensures the suppress throwing option is applied correctly without affecting the generic task's exception handling.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
Task<int> t = new Task<int>(() => 1);
(Task)t.ConfigureAwait(ConfigureAwaitOptions.SuppressThrowing);
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
Task<int> t = new Task<int>(() => 1);
((Task)t).ConfigureAwait(ConfigureAwaitOptions.SuppressThrowing);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
