# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/no-empty-list-as-parameter.md

---
title: Do not use an empty list as a default parameter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use an empty list as a default parameter
---

# Do not use an empty list as a default parameter

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/no-empty-list-as-parameter`

**Language:** Python

**Severity:** Warning

**Category:** Security

**CWE**: [230](https://cwe.mitre.org/data/definitions/230.html)

## Description{% #description %}

Developers should not be setting a default argument to an empty list. Instead, use `None` and check if the value is defined. Using a default list can cause unwanted behavior as the value of the argument is only evaluated once when the function is defined, not when it is run. Because of this, each function call will reference the same underlying memory when the default value is used, which can lead to unwanted behavior.

### Learn More{% #learn-more %}

- [Avoid using empty list as default argument](https://nikos7am.com/posts/mutable-default-arguments/)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
def newFunction(arg1, arg2: int, arg3 = [], arg4: MyType = []): # do not use an empty list as a default parameter
    arg3.append(arg2)
    arg4.append(arg1)
    print(arg3, arg4)

newFunction('a', 1)
newFunction('b', 2)
newFunction('c', 3)

# Will print:
# [1] ['a']
# [1, 2] ['a', 'b']
# [1, 2, 3] ['a', 'b', 'c']
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
def newFunction(arg1, arg2: int, arg3 = None, arg4 = None): # do not use an empty list as a default parameter
    if arg3 is None:
        arg3 = []
    if arg4 is None:
        arg4 = []
    arg3.append(arg2)
    arg4.append(arg1)
    print(arg3, arg4)

newFunction('a', 1)
newFunction('b', 2)
newFunction('c', 3)

# Will print:
# [1] ['a']
# [2] ['b']
# [3] ['c']
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
