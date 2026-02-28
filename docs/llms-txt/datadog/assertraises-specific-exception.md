# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/assertraises-specific-exception.md

---
title: assertRaises must check for a specific exception
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > assertRaises must check for a specific exception
---

# assertRaises must check for a specific exception

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/assertraises-specific-exception`

**Language:** Python

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

When checking an exception, check for a specific exception. Checking for `Exception` may bypass the verification of the correct behavior of the program.

Using a generic exception is error-prone and give a false sense of correctness. Instead, use the correct exception to check against.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
self.assertRaises(Exception, foo)  # check a specific Exception, not a generic one
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
self.assertRaises(ValueError, foo)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
