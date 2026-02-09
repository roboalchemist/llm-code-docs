# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-node-security/detect-eval-with-expression.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-node-security/detect-eval-with-expression.md

---
title: Avoid `eval` with expressions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid `eval` with expressions
---

# Avoid `eval` with expressions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-node-security/detect-eval-with-expression`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

## Description{% #description %}

The `eval` function could execute malicious code if used with non-literal values. The argument provided to the `eval` method could be used to execute malicious code. If an attacker manages to control the `eval` argument they can execute arbitrary code.

In JavaScript, the `eval()` function evaluates or executes an argument if it's a string of JavaScript code. If this argument is influenced by user input or other external sources, it can lead to security vulnerabilities. Specifically, if an attacker can control or manipulate the value of the `variable` in `eval(variable)`, they can execute arbitrary code.

You should avoid using `eval` at all costs, but if you face an advanced use case, use literal values that are under your control or sanitize the input. However, even then it is still recommended to avoid the use of `eval` as it has led to security breaches before.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
eval(a);
global.eval(a);
globalThis.eval(a);

const answer = eval(expression)
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
eval('alert()')
global.eval('a');
globalThis.eval('a');
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 