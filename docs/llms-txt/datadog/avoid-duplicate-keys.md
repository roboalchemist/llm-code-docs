# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/avoid-duplicate-keys.md

---
title: Avoid duplicate keys in dictionaries
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid duplicate keys in dictionaries
---

# Avoid duplicate keys in dictionaries

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/avoid-duplicate-keys`

**Language:** Python

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Keys in a dictionary must be unique.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
dict = {
  "key1": "key2",
  "key2": "key3",
  "key3": "key4",
  "key1": "bla"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
dict = {
  "key1": "key2",
  "key2": "key3",
  "key3": "key4",
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 