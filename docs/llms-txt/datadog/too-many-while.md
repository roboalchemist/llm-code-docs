# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/too-many-while.md

---
title: 'do not use too many nested loops and conditions '
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not use too many nested loops and conditions
---

# do not use too many nested loops and conditions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/too-many-while`

**Language:** Python

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

A program should have a maximum level of nesting loops. If your program has too many nested loops (`if`/`for`/`while`), consider refactoring your program to avoid too many nesting levels.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
while bla:
    while foo:
        while bar:
            while baz:
                pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
while bla:
    while foo:
        while bar:
            pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
