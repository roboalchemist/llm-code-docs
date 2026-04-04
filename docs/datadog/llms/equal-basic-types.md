# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/equal-basic-types.md

---
title: check equal is used on consistent basic types
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > check equal is used on consistent basic types
---

# check equal is used on consistent basic types

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/equal-basic-types`

**Language:** Python

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

When comparing basic types (string, integer, float), we should always values of the same types.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
1 == "1"  # Comparing an integer and a string
1.0 == "foo"  # Comparing a float and a string
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
1 == 1
"abc" == "def"
a == 1
a == b
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
