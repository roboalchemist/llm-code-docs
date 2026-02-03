# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/default-param-last.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/default-param-last.md

---
title: Avoid default parameters before normal parameters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid default parameters before normal parameters
---

# Avoid default parameters before normal parameters

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/default-param-last`

**Language:** JavaScript

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule encourages the practice of defining default parameters after the normal parameters in a function declaration. This is to ensure that the function behaves as expected when it is called with fewer arguments.

Default parameters are used to initialize formal parameters with default values. They are useful when an argument is not provided in the function or if it is undefined. If the function is called with fewer arguments than the declared parameters, the normal parameter receives `undefined`, while the default parameter is initialized with the provided value.

To avoid this, ensure that normal parameters are always defined before default parameters. This ensures that the function behaves as expected and doesn't cause any unexpected results.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
function foo(a = false, b) {}
foo(undefined, "b")
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
function foo(a, b = false) {}
foo("a")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 