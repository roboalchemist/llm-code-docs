# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/nested-blocks.md

---
title: Do not have too many nested blocks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not have too many nested blocks
---

# Do not have too many nested blocks

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/nested-blocks`

**Language:** Python

**Severity:** Error

**Category:** Code Style

## Description{% #description %}

Avoid to nest too many loops together. Having too many loops make your code harder to understand. Prefer to organize your code in functions and unit of code you can clearly understand.

#### Learn More{% #learn-more %}

- [Computer Programming wikibooks - Minimize nesting](https://en.wikibooks.org/wiki/Computer_Programming/Coding_Style/Minimize_nesting)

## Arguments{% #arguments %}

- `max-levels`: Maximum number of nesting levels. Default: 4.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
def func():
    while foo:
        while bar:
            while baz:
                while wiz:  # too many nested elements
                    pass
```

```python
def func():
    for v in bla:
        for w in bar:
            for x in baz:
                for y in wiz:  # too many nested elements
                    pass
```

```python
def func():
    if foo:
        pass
    else:
        if bar:
            if baz:
                if wiz:  # too many nested elements
                    pass
```

```python
def func():
    if foo:
        if bar:
            if baz:
                if wiz:  # too many nested elements
                    pass
```

```python
def func():
    if foo:
        pass
    elif bar:
        if bar:
            if baz:
                if wiz:  # too many nested elements
                    pass
    else:
        pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
while Foo:
    while Bar:
        print("foobar")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
