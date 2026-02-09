# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-console.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-console.md

---
title: Avoid leaving console debug statements
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid leaving console debug statements
---

# Avoid leaving console debug statements

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-console`

**Language:** JavaScript

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Debugging with `console` (such as `console.log` or `console.info`) is not considered a bad practice, but these statements can be accidentally left in production code, leading to unnecessary log pollution. It is important to remove or replace these debugging statements to maintain clean and secure production builds.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
console.log(foo) // General-purpose logging which can expose internal information 
console.error(foo) // Error logging which can expose sensitive information
console.info(foo) // Informational logging which can clutter production logs
console.warn(foo) // Warning logging which can be excessive for production
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
Console.info(foo) // Example placeholder for a custom logging method or library
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 