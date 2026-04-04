# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/no-range-loop-with-len.md

---
title: Do not use for i in range(len())
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use for i in range(len(<array>))
---

# Do not use for i in range(len(<array>))

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/no-range-loop-with-len`

**Language:** Python

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

Do not iterate over an array using `for in range(len(array))`. Use instead `for i in array`.

#### Learn More{% #learn-more %}

- [Python Loop Through an Array](https://www.w3schools.com/python/gloss_python_array_loop.asp)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import random
import string

DEFAULT_CHAR_STRING = string.ascii_lowercase + string.digits


def generate_random_string(chars=DEFAULT_CHAR_STRING, size=20):
    return "".join(random.choice(chars) for _ in range(size))


NORMALIZED_SIZE = 8


def normalize(s):
    builder = []
    for i in range(NORMALIZED_SIZE):
        builder.append(s[i].capitalize())
    return "".join(builder)


FORBIDDEN_WORDS = set(["bad1", "bad2"])


def filter_forbidden_tags(tags):
    for i in range(len(tags)):
        if tags[i].tag in FORBIDDEN_WORDS:
            del tags[i]
    return tags
```

```python
for i in range(len(tab)):  # iterate directly over the array
  bla(tab[i])
```

```python
for i in range(len(tab)):  # iterate directly over the array
  bla(tab[i])
```

```python
for i in range(len(tab)):  # iterate directly over the array
  tab[i] = bla
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
for i, _ in enumerate(lst):
   print(i)

for i in range(len(lst)):
   print(i)
   plop = tab[i]
```

```python
for i in tab:
  bla(i)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
