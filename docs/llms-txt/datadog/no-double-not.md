# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/no-double-not.md

---
title: do not use double negation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not use double negation
---

# do not use double negation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/no-double-not`

**Language:** Python

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

Do not use two negation. It makes the code more complex to read and understand. Instead of using two negation, use the expression directly.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
if not not foo:  # just use if foo
    pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
if not foo:
    pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
