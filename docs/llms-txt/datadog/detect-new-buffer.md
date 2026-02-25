# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-node-security/detect-new-buffer.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-node-security/detect-new-buffer.md

---
title: Avoid Buffer(argument) with non-literal values
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid Buffer(argument) with non-literal values
---

# Avoid Buffer(argument) with non-literal values

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-node-security/detect-new-buffer`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

## Description{% #description %}

Dealing with binary data can be achieved with the Node.js Buffer class. However, if you use non-literal params, this could lead to malicious control over the value, resulting in an attack.

For example, a large number could allocate a significant amount of memory leading to a denial of service attack. It is recommended to use literal values that you can control to prevent these attacks.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var a = new Buffer(c)
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var a = new Buffer('test')
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
