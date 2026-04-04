# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/avoid-string-concat.md

---
title: avoid string concatenation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > avoid string concatenation
---

# avoid string concatenation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/avoid-string-concat`

**Language:** Python

**Severity:** Warning

**Category:** Performance

## Description{% #description %}

Concatenation of multiple strings is not efficient and make the code hard to read and understand.

Instead of concatenating multiple strings, use an f-string or a format string.

#### Learn More{% #learn-more %}

- [Python Documentation: `str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format)
- [Python Documentation - f-string](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
"my" + awesome + "string"
plop = "super" + "awesome" + "text"
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
"my {0} string".format(awesome)
f"my {awesome} string"
plop = "superawesometext"

function(
    tags = (
    user_tags
    + s.get("tags", [])
    + [
        f"schedule_id:{s['_id']}",
        f"schedule_name:{s['schedule_name']}",
        f"git_ref:{schedule_git_ref}",
    ]
)
)

ROOT = Path("/tmp")
my_path = ROOT / "mydir" / "subdir"
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
