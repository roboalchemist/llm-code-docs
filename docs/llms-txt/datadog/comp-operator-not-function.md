# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-pandas/comp-operator-not-function.md

---
title: Use operators to compare values, not functions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use operators to compare values, not functions
---

# Use operators to compare values, not functions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-pandas/comp-operator-not-function`

**Language:** Python

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

User should use comparison operators (`<`, `>`, etc) instead of function (`.ld`) to make the code more clear.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
foo.le(bar)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
foo < bar
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 