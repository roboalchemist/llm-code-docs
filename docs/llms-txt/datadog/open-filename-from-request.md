# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-django/open-filename-from-request.md

---
title: Filename coming from the request
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Filename coming from the request
---

# Filename coming from the request

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-django/open-filename-from-request`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [22](https://cwe.mitre.org/data/definitions/22.html)

## Description{% #description %}

Improper validation of input data, leading to potential data leaks. The path should be checked and validated before opening a file in order to prevent opening random files and leaking data.

#### Learn More{% #learn-more %}

- [CWE-22: Improper Limitation of a Pathname to a Restricted Directory](https://cwe.mitre.org/data/definitions/22.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
def download_file1(request):
    url = request.GET.get("filename")
    print(f"url of the file: {url}")
    file = open(url, "rb")

    with open(url) as f:
        pass
    pass


def download_file2(request):
    url = request.POST.get("filename")
    print(f"url of the file: {url}")
    file = open(url, "rb")

    with open(url) as f:
        pass
    pass

def download_file3(request):
    url = request.BLA.get("filename")
    print(f"url of the file: {url}")
    file = open(url, "rb")

    with open(url) as f:
        pass
    pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import os

def download_file(request):
    url = request.GET.get("filename")

    if ".." in url:
        return

    sanitized_path = os.path.realpath(url, strict=True)

    print(f"url of the file: {url}")
    file = open(sanitized_path, "rb")

    with open(sanitized_path) as f:
        pass
    pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 