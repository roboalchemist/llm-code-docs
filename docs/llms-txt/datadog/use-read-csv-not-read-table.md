# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-pandas/use-read-csv-not-read-table.md

---
title: prefer read_csv to read_table
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > prefer read_csv to read_table
---

# prefer read_csv to read_table

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-pandas/use-read-csv-not-read-table`

**Language:** Python

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The functions `notna` and `notnull` are similar. However, this is a best practice to use `notna` since other methods use the same naming patterns.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
employees = pd.read_table(input_file)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
employees = pd.read_csv(input_file)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 