# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-dupe-args.md

---
title: Function parameters redeclared
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Function parameters redeclared
---

# Function parameters redeclared

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-dupe-args`

**Language:** JavaScript

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

In JavaScript, it's syntactically valid to define multiple parameters with the same name in a function definition. However, doing so is considered bad practice as the last argument value will override the preceding argument value which can lead to issues that are hard to debug.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
function a(a, b, b) {}
function a(a, a, a) {}
function a(a, b, a) {}
function a(a, b, a, b) {}
var a = function(a, b, b) {}
var a = function(a, a, a) {}
var a = function(a, b, a) {}
var a = function(a, b, a, b) {}
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
function a(a, b, c){}
var a = function(a, b, c){}
function a({a, b}, {c, d}){}
function a([ , a]) {}
function foo([[a, b], [c, d]]) {}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
