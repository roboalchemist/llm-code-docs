# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/html-string-from-parameters.md

---
title: Avoid HTML built in strings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid HTML built in strings
---

# Avoid HTML built in strings

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/html-string-from-parameters`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [79](https://cwe.mitre.org/data/definitions/79.html)

## Description{% #description %}

Detect unsafe HTML content. User-input may be injected into HTML content without being sanitized.

User input should always be checked before being used in HTML data.

#### Learn More{% #learn-more %}

- [CWE-79: Improper Neutralization of Input During Web Page Generation](https://cwe.mitre.org/data/definitions/79.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
def my_function(arg1: str, arg2, arg3 = "blabla", arg4: str = "blibli"):
    html1 = f"<div>{arg1}</div>"
    html1 = "<div>{0}</div>".format(arg1)
    html2 = f"<div>{arg2['bli']}</div>"
    html2 = "<div>{0}</div>".format(arg2['bli'])
    html3 = "<div>" + arg1 + "</div>"
    render(f"<div>{arg1}</div>")
    return html


def my_function2(arg1: str, arg2, arg3 = "blabla", arg4: str = "blibli"):
    html1 = f"<div>{arg51}</div>"
    html1 = "<div>{0}</div>".format(arg42)
    html2 = f"<div>{arg26['bli']}</div>"
    html2 = "<div>{0}</div>".format(arg51['bli'])
    html3 = "<div>" + arg41 + "</div>"
    render(f"<div>{arg51}</div>")
    return html


def my_function3(arg1: str, arg2, arg3 = "blabla", arg4: str = "blibli"):
    html1 = f"<div>{arg1}</div>"
    html1 = "<div>{0}</div>".format(arg1)
    html2 = f"<div>{arg2['bli']}</div>"
    html2 = "<div>{0}</div>".format(arg2['bli'])
    html3 = "<div>" + arg1 + "</div>"
    render(f"<div>{arg1}</div>")
    return html
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
def my_function(arg1: str, arg2, arg3 = "blabla", arg4: str = "blibli"):
    html1 = f"<div>{sanitize_value(arg1)}</div>"
    html1 = "<div>{0}</div>".format(sanitize_value(arg1))
    html2 = f"<div>{sanitize_value(arg2['bli'])}</div>"
    html2 = "<div>{0}</div>".format(sanitize_value(arg2['bli']))
    html3 = "<div>" + sanitize_value(arg1) + "</div>"
    render(f"<div>{sanitize_value(arg1)}</div>")
    return html
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 