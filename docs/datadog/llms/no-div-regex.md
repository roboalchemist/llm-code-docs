# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/no-div-regex.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/no-div-regex.md

---
title: Avoid equal signs at the beginning of regular expressions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid equal signs at the beginning of regular expressions
---

# Avoid equal signs at the beginning of regular expressions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/no-div-regex`

**Language:** JavaScript

**Severity:** Notice

**Category:** Error Prone

## Description{% #description %}

At the start of a regular expression literal, the characters `/=` can be mistaken for a division assignment operator.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var f = function() { return /=foo/; };
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var f = function() { return /foo/ig.test('bar'); };
var f = function() { return /\\=foo/; };
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
