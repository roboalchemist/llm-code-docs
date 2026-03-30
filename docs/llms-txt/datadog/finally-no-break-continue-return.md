# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/finally-no-break-continue-return.md

---
title: do not use break or continue in finally block
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not use break or continue in finally block
---

# do not use break or continue in finally block

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/finally-no-break-continue-return`

**Language:** Python

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

When using `return`, `break` or `continue` in a `finally` block, it will stop the spread of any exceptions that were thrown in the `try`, `else`, or `except` blocks and will disregard any return statements.

#### Learn More{% #learn-more %}

- [Official Python documentation](https://docs.python.org/3/reference/compound_stmts.html#except)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
try:
    client_obj.get_url(url)
except (URLError, ValueError):
    client_obj.remove_url(url)
except SocketTimeout:
    client_obj.handle_url_timeout(url)
finally:
    break  # avoid break in the finally block
```

```python
try:
    client_obj.get_url(url)
except (URLError, ValueError):
    client_obj.remove_url(url)
except SocketTimeout:
    client_obj.handle_url_timeout(url)
finally:
    return 0  # avoid return in the finally block
```

```python
try:
    client_obj.get_url(url)
except (URLError, ValueError):
    client_obj.remove_url(url)
except SocketTimeout:
    client_obj.handle_url_timeout(url)
finally:
    continue  # avoid continue in the finally block
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
try:
  client_obj.get_url(url)
except (URLError, ValueError):
  client_obj.remove_url(url)
except SocketTimeout:
  client_obj.handle_url_timeout(url)
finally:
  print("cleanup the mess")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
