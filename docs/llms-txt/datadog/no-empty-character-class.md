# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-empty-character-class.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-empty-character-class.md

---
title: Avoid empty character classes in regular expressions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid empty character classes in regular expressions
---

# Avoid empty character classes in regular expressions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-empty-character-class`

**Language:** JavaScript

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

In regular expressions, empty character classes do not match anything, and were likely used in error.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var foo = /^abc[]/;
var foo = /foo[]bar/;
if (foo.match(/^abc[]/)) {}
if (/^abc[]/.test(foo)) {}
var foo = /[]]/;
var foo = /\[[]/;
var foo = /\\[\\[\\]a-z[]/;
var foo = /[]]/d;
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var foo = /^abc[a-zA-Z]/;
var regExp = new RegExp("^abc[]");
var foo = /^abc/;
var foo = /[\\[]/;
var foo = /[\\]]/;
var foo = /[a-zA-Z\\[]/;
var foo = /[[]/;
var foo = /[\\[a-z[]]/;
var foo = /[\\-\\[\\]\\/\\{\\}\\(\\)\\*\\+\\?\\.\\\\^\\$\\|]/g;
var foo = /\\s*:\\s*/gim;
var foo = /[\\]]/uy;
var foo = /[\\]]/s;
var foo = /[\\]]/d;
var foo = /\[]/
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 