# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-pandas/avoid-inplace.md

---
title: Avoid using inplace=True
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using inplace=True
---

# Avoid using inplace=True

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-pandas/avoid-inplace`

**Language:** Python

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Avoid using `inplace=True` as it does not have clear performance impact and is potentially dangerous and does not behave as it should.

#### Learn More{% #learn-more %}

- [Why You Should Probably Never Use pandas inplace=True](https://towardsdatascience.com/why-you-should-probably-never-use-pandas-inplace-true-9f9f211849e4?gi=ae387a166946)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
df.drop(['a'], axis=1, inplace=True)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
df.drop(['a'], axis=1, inplace=False)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
