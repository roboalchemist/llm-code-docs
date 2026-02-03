# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/require-yield.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/require-yield.md

---
title: Require yield in generator functions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Require yield in generator functions
---

# Require yield in generator functions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/require-yield`

**Language:** JavaScript

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

Generator functions must yield at some point. Otherwise, use a normal function.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
function* foo() { return 0; }
(function* foo() { return 0; })();
var obj = { *foo() { return 0; } }
class A { *foo() { return 0; } }
function* foo() { function* bar() { yield 0; } }
function* foo() { function* bar() { return 0; } yield 0; }
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
function foo() { return 0; }
function* foo() { yield 0; }
function* foo() { }
(function* foo() { yield 0; })();
(function* foo() { })();
var obj = { *foo() { yield 0; } };
var obj = { *foo() { } };
class A { *foo() { yield 0; } };
class A { *foo() { } }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 