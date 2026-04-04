# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/collection-while-iterating.md

---
title: do not modify a dictionary while iterating on it
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not modify a dictionary while iterating on it
---

# do not modify a dictionary while iterating on it

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/collection-while-iterating`

**Language:** Python

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

Never update a dictionary while iterating on it. If you wish to update the dictionary, create a new dictionary from the existing values.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
i = 0
for element in my_list:
    my_list["stuff"] = i  # modifying a dictionary while iterating
    i += 1
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
for i in myvalue:
    myvalue[i] = do_something()
```

```python
i = 0
new_list = {}
for element in my_list:
    new_list["stuff"] = i  # putting value to a new dictionary
    i += 1
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
