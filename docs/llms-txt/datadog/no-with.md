# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-with.md

---
title: The with statement can lead to ambiguous code
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > The with statement can lead to ambiguous code
---

# The with statement can lead to ambiguous code

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-with`

**Language:** JavaScript

**Severity:** Error

**Category:** Best Practices

**CWE**: [710](https://cwe.mitre.org/data/definitions/710.html)

## Description{% #description %}

The `with` statement in JavaScript is used to add a given object's properties as variables in a specific block of code. While it may seem convenient, the `with` statement has several pitfalls and can lead to hard-to-diagnose problems.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
with(foo) { bar() }
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
foo.bar()
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 