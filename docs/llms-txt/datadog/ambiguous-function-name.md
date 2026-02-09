# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/ambiguous-function-name.md

---
title: make sure function names are readable
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > make sure function names are readable
---

# make sure function names are readable

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/ambiguous-function-name`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In some fonts, these characters are indistinguishable from the numerals one and zero. Use characters that are not ambiguous.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
def I():  # use i instead
    pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
def i():
    pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 