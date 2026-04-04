# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-flask/urlopen-unsanitized-data.md

---
title: Use of unsanitized data to open API
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use of unsanitized data to open API
---

# Use of unsanitized data to open API

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-flask/urlopen-unsanitized-data`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [918](https://cwe.mitre.org/data/definitions/918.html)

## Description{% #description %}

Use of unsanitized from incoming request, leading to potential data leak and lack of control of the service. The code should check any incoming data and make sure it's safe to use it.

#### Learn More{% #learn-more %}

- [CWE-918: Server-Side Request Forgery (SSRF)](https://cwe.mitre.org/data/definitions/918.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import flask
from urllib.request import urlopen

app = flask.Flask(__name__)



@app.route("/route/to/resource/<resource_id>")
def resource2(resource_id):
    file1 = urlopen(resource_id)
    file2 = urlopen(f"/path/to/{resource_id}")


@app.route("/route/to/resource")
def resource2():
    resource_id = flask.request.args.get("resource_id")
    file1 = urlopen(resource_id)
    file2 = urlopen(f"/path/to/{resource_id}")
    file3 = urlopen("/path/to/{0}".format(resource_id))
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import flask
from urllib.request import urlopen

app = flask.Flask(__name__)

@app.route("/route/to/resource/<resource_id>")
def resource2(resource_id):
    sanitized_resource_id = sanitize(resource_id)
    file1 = urlopen(sanitized_resource_id)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
