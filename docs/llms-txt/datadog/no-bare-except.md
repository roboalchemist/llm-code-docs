# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/no-bare-except.md

---
title: do not use bare except
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not use bare except
---

# do not use bare except

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/no-bare-except`

**Language:** Python

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Avoid bare `except`. Try to always use specialized exception names in `except` blocks.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
try:
  print("foo")
except:  # use a specialized exception name
  print("bar")
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
try:
    parsed = json.loads(response.body)
except json.JSONDecodeError:
    log.warning("Test skips request responded with invalid JSON '%s'", response.body)
    return
```

```python
try:
  pass
except (TypeError, ValueError):
    log.debug(
        (
            "received invalid x-datadog-* headers, "
            "trace-id: %r, parent-id: %r, priority: %r, origin: %r, tags:%r"
        ),
        trace_id,
        parent_span_id,
        sampling_priority,
        origin,
        tags_value,
    )
```

```python
try:
    foo()
except MyError as e:
    bar()
```

```python
try:
  print("foo")
except MyException:
  print("bar")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 