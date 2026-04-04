# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/too-many-nested-if.md

---
title: do not use too many nested if conditions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not use too many nested if conditions
---

# do not use too many nested if conditions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/too-many-nested-if`

**Language:** Python

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Too many nested loops make the code hard to read and understand. Simplify your code by removing nesting levels and separate code in small units.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
if foo < 0:
    if bar:
        if baz:
            if bao:
                pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
if foo:
    if bar:
        if baz:
            pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
