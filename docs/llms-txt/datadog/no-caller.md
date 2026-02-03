# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-caller.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-caller.md

---
title: Avoid the use of arguments.caller or arguments.callee
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid the use of arguments.caller or arguments.callee
---

# Avoid the use of arguments.caller or arguments.callee

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-caller`

**Language:** JavaScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

`arguments.caller` and `arguments.callee` has been deprecated and forbidden in ECMAScript 5 strict mode.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var x = arguments.callee;
var x = arguments.caller;
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var x = arguments.length
var x = arguments
var x = arguments[0]
var x = arguments[caller]
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 