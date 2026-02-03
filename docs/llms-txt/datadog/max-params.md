# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/max-params.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/max-params.md

---
title: Enforce a maximum number of parameters in a function
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce a maximum number of parameters in a function
---

# Enforce a maximum number of parameters in a function

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/max-params`

**Language:** JavaScript

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Having too many parameters can make your code hard to read. The parameters must be used in appropriate order. Forgetting the order of parameters can cause mistakes.

Too many parameters is a code smell. You should refactor your code in smaller reusable bits. While it may be valid to require more than four parameters, you should use object destructuring.

## Arguments{% #arguments %}

- `max-params`: Maximum number of parameters. Default: 4.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
function test(a, b, c, d, e) {}
var test = function(a, b, c, d, e, f) {};
var test = (a, b, c, d, e) => {};
(function(a, b, c, d, e) {});

// object property options
function test(a, b, c, d, e) {}
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
function test(d, e, f) {}
var test = function(a, b, c) {};
var test = (a, b, c) => {};
var test = function test(a, b, c) {};

// object property options
var test = function(a, b, c) {};
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 