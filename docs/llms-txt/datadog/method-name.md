# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/method-name.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/method-name.md

---
title: Method name should use camelCase
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Method name should use camelCase
---

# Method name should use camelCase

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/method-name`

**Language:** JavaScript

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Ensure that method names use `camelCase` and not `snake_case` or `PascalCase`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
const a = { GetValue() {} }
class A { set_value() {} }
class A { *set_value() {} }
class A { #set_value() {} }
class A { #SetValue() {} }
class A { _SetValue() {} }
class A { __Set_Value() {} }
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
const a = { getValue() {} }
class A { setValue() {} }
class A { #fooBla() {} }
class A { _setValue() {} }
class A { __setValue() {} }
class A { set2() {} }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 