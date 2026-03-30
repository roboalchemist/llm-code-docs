# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/logger-constant-template.md

---
title: Use constant template when logging data
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use constant template when logging data
---

# Use constant template when logging data

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/logger-constant-template`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

Using interpolated strings (`$"..."`) or string concatenation forces the CLR to build a new string **every time** the log statement executes â even if the current log level is disabled (e.g., when logging at Debug in production). Prefer using constant templates when logging data.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
_logger.LogInformation("User " + userId + " logged in");
```

```csharp
_logger.LogInformation($"User {userId} logged in at {timestamp}");
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
// check log enablement before
if (_logger.IsEnabled(LogLevel.Debug)) {
    _logger.LogInformation("User " + userId + " logged in");
}
```

```csharp
_logger.LogInformation("User {UserId} logged in at {Timestamp}", userId, timestamp);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
