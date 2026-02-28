# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-pandas/isna-instead-of-isnull.md

---
title: Use isna instead of isnull
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use isna instead of isnull
---

# Use isna instead of isnull

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-pandas/isna-instead-of-isnull`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The functions `isna` and `isnull` are similar. However, this is a best practice to use `isna` since other methods use the same naming patterns.

#### Learn More{% #learn-more %}

- [Pandas isna() and isnull(), what is the difference?](https://stackoverflow.com/questions/52086574/pandas-isna-and-isnull-what-is-the-difference)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
nulls = pd.isnull(val)  # prefer using isna
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
nas = pd.isna(val)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
