# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/function-naming.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-code-style/function-naming.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-best-practices/function-naming.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/function-naming.md

---
title: Function name should use camelCase or PascalCase
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Function name should use camelCase or PascalCase
---

# Function name should use camelCase or PascalCase

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/function-naming`

**Language:** JavaScript

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Ensure that the function uses `camelCase` or `PascalCase` in case it is an `Object`. Generator functions should always be `camelCase`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
function My_Class() {}
function get_value() {}
function* GetValue() {}
function *get_value() {}
function _get_value_() {}
function __get_value() {}
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
function MyClass() {}
function getValue() {}
function* getValue() {}
function *getValue() {}
function _getValue() {}
function $__getValue__() {}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 