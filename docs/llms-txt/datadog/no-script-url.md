# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-script-url.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-script-url.md

---
title: Avoid using JavaScript in URLs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using JavaScript in URLs
---

# Avoid using JavaScript in URLs

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-script-url`

**Language:** JavaScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

JavaScript URLs are evaluated the same way `eval` is executed. This can lead to arbitrary code execution.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var a = 'javascript:void(0);';
var a = 'javascript:';
var a = `javascript:`;
var a = `JavaScript:`;
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var a = 'Hello World!';
var a = 10;
var url = 'xjavascript:'
var url = `xjavascript:`
var url = `${foo}javascript:`
var a = foo`javaScript:`;
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 