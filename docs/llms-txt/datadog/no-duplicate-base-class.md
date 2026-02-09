# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/no-duplicate-base-class.md

---
title: use a base class only once
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > use a base class only once
---

# use a base class only once

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/no-duplicate-base-class`

**Language:** Python

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

Classes should not have the same superclass specified twice. Each superclass must be unique.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
class MyClass:
    pass


# The SuperClass parent is specified twice
class MyClassTwo(SuperClass, OtherClass, SuperClass):
    pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
class MyClass:
    pass


class MyClassTwo(SuperClass):
    pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 