# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/parameter-name.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/parameter-name.md

---
title: Parameter name should use camelCase
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Parameter name should use camelCase
---

# Parameter name should use camelCase

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/parameter-name`

**Language:** JavaScript

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Ensure that parameter names use `camelCase` and not `snake_case` or `PascalCase`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
const a = { setValue(NewValue, event_info) {} }
class A { setValue(NewValue, event_info__) {} }
function setValue(NewValue, $_event_info_) {}
const a = function(NewValue, event_info) {}
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
const a = { getValue() {} }
class A { setValue(newValue_) {} }
class B { setValue(md5, valid5String) {} }
class B { setValue(_, valid5String) {} }

async.doSomething(nothing, (n, _cb) => {

}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 