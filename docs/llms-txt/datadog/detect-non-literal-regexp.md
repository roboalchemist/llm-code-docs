# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-node-security/detect-non-literal-regexp.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-node-security/detect-non-literal-regexp.md

---
title: Detects non-literal values in regular expressions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Detects non-literal values in regular expressions
---

# Detects non-literal values in regular expressions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-node-security/detect-non-literal-regexp`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

## Description{% #description %}

Creating a regular expression with user input can lead to a Regular Expression Denial of Service (ReDoS) attack. In this type of attack, a user can submit a very complex regular expression that takes too long to execute.

If you have an advanced use case that requires regex evaluation with user input, always make sure to sanitize the data and provide a safe timeout environment.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var a = new RegExp(c, 'i');
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var a = new RegExp('ab+c', 'i');
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
