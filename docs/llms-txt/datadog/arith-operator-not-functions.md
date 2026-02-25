# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-pandas/arith-operator-not-functions.md

---
title: Use arithmetic operator instead of a function
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use arithmetic operator instead of a function
---

# Use arithmetic operator instead of a function

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-pandas/arith-operator-not-functions`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

User should use arithmetic operators (`+`, `-`, etc) instead of function (`.add`) to make the code more clear.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
def myfunction():
    foo = pd.DataFrame({'angles': [0, 3, 4],
                        'degrees': [360, 180, 360]},
                        index=['circle', 'triangle', 'rectangle'])
    if something:
        baz = foo.add(1)
    elif other_thing:
        baz = foo.add(42)
    else:
        baz = foo.add(51)

    bar = whatever()
    baz = bar.add(4)
```

```python
def myfunction():
    foo = pd.DataFrame({'angles': [0, 3, 4],
                        'degrees': [360, 180, 360]},
                        index=['circle', 'triangle', 'rectangle'])
    baz = foo.add(1)

    bar = whatever()
    baz = bar.add(4)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
foo = pd.DataFrame({'angles': [0, 3, 4],
                   'degrees': [360, 180, 360]},
                  index=['circle', 'triangle', 'rectangle'])
baz = foo + 1
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
