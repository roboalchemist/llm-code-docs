# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/invalid-strip-call.md

---
title: strip() argument should not have duplicate characters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > strip() argument should not have duplicate characters
---

# strip() argument should not have duplicate characters

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/invalid-strip-call`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

When using `.strip()`, you only need to pass the letters you want to split on. There is no need to specify the same letter twice.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
"Hello World".strip("Hello")  # letter l is present twice in the string
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
"Hello World".strip("Helo")  # letter l is present twice in the string
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 