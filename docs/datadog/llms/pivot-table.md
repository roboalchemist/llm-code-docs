# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-pandas/pivot-table.md

---
title: Use pivot_table instead of pivot or unstack
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use pivot_table instead of pivot or unstack
---

# Use pivot_table instead of pivot or unstack

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-pandas/pivot-table`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule encourages the use of `pivot_table` instead of `pivot` or `unstack` for reshaping data in pandas DataFrames. While `pivot` and `unstack` can be simpler for straightforward cases, they are limited because they do not handle duplicate values well and can raise errors if the data is not perfectly formatted.

Using `pivot_table` is important because it provides greater flexibility by allowing aggregation functions to handle duplicates and missing values gracefully. This makes your code more robust, especially when working with real-world data that often contains duplicates or incomplete entries.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
table = df.unstack(level=0)
```

```python
table = pd.pivot(
        df,
        index='foo',
        columns='bar',
        values='baz'
        )
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
table = df.pivot_table(
        df,
        values='D',
        index=['A', 'B'],
        columns=['C'],
        aggfunc=np.sum,
        fill_value=0
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
