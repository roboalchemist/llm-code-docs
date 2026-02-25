# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/incorrect-complete-options.md

---
title: Do not use TaskContinuationOptions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use TaskContinuationOptions
---

# Do not use TaskContinuationOptions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/incorrect-complete-options`

**Language:** C#

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

The `TaskContinuationOptions` enumeration is used to control the behavior of a task that is created to handle the completion of another task. However, using `TaskContinuationOptions` in a `TaskCompletionSource` is not recommended and can lead to unexpected behavior.

The importance of this rule is that it helps to avoid potential threading issues and ensures that your asynchronous code runs as expected. Misusing `TaskContinuationOptions` could lead to your continuation running on an unexpected thread, causing potential problems with thread-safety and synchronization.

To adhere to this rule and good coding practices, you should use `TaskCreationOptions` instead of `TaskContinuationOptions` when creating a new `TaskCompletionSource`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
var tcs = new TaskCompletionSource<int>(TaskContinuationOptions.RunContinuationsAsynchronously);
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
var tcs = new TaskCompletionSource<int>(TaskCreationOptions.RunContinuationsAsynchronously);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
