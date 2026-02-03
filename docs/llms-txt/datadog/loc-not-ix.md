# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-pandas/loc-not-ix.md

---
title: prefer iloc or loc rather than ix
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > prefer iloc or loc rather than ix
---

# prefer iloc or loc rather than ix

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-pandas/loc-not-ix`

**Language:** Python

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The functions `notna` and `notnull` are similar. However, this is a best practice to use `notna` since other methods use the same naming patterns.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
index = df.iat[:, 1:3]
```

```python
index = df.at[:, ['B', 'A']]
```

```python
s = df.ix[[0, 2], 'A']
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
new_df = df.iloc[]
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 