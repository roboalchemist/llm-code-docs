# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/no-floating-decimal.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/no-floating-decimal.md

---
title: Avoid leading or trailing decimal points in numbers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid leading or trailing decimal points in numbers
---

# Avoid leading or trailing decimal points in numbers

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/no-floating-decimal`

**Language:** JavaScript

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

To prevent confusion between the dot operator and the decimal point, always use a leading number when writing floating point numbers.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var x = .5;
var x = -.5;
var x = 2.;
var x = -2.;
typeof.2
for(foo of.2);
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var x = 2.5;
var x = "2.5";
var t = {
    ecmaVersion: 2018,
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 