# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/logging-exception.md

---
title: Avoid logging exception
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid logging exception
---

# Avoid logging exception

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/logging-exception`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

This rule discourages logging only the exception message without including the full exception object. Logging just the exception message can omit valuable context, such as the stack trace, which is essential for diagnosing and troubleshooting issues effectively.

To comply with this rule, always pass the exception object as a parameter to your logging method instead of concatenating or interpolating the exception message into the log string. For example, use `logger.error("Error processing file", e);` rather than `logger.error($"Error: {e.Message}");`. This practice ensures that the logging framework captures the full exception details, including stack traces and inner exceptions.

Note that you may still want to log the full exception of part of its attribute. In this case, you can disable this rule for your repository or organization.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
try {
    processFile();
} catch (IOException ex) {
    logger.error($"Error: {ex.Message}");
}
```

```csharp
try {
    processFile();
} catch (IOException e) {
    logger.error("Error processing file: " + e.getMessage());
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
try {
    processFile();
} catch (IOException e) {
    logger.error("Error processing file", e);
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 