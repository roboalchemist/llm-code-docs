# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/comment-fixme-todo-ownership.md

---
title: TODO and FIXME comments must have ownership
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > TODO and FIXME comments must have ownership
---

# TODO and FIXME comments must have ownership

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/comment-fixme-todo-ownership`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

When using `TODO` or `FIXME`, specify who write the annotation. It's a best practice to remind you who created the annotation and have potential context and information about this issue.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
# TODO fix this function
def my_function():
    pass

# FIXME fix this function
def my_function():
    pass

# FIXME(): fix this function
def broken():
    pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
# TODO(bob) fix this function
def my_function():
    pass

# FIXME(julien) fix this function
def my_other_function():
    pass

# FIXME[julien] fix this function
def my_other_function():
    pass

# TODO[bob] fix this function
def my_function():
    pass

# TODO (amaan): fix this function
def broken():
    pass

# TODO (amaan.qureshi): fix this function too
def broken2():
    pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 