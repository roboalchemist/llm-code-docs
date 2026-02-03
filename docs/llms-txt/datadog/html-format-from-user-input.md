# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-flask/html-format-from-user-input.md

---
title: Use of unsanitized data to make API calls
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use of unsanitized data to make API calls
---

# Use of unsanitized data to make API calls

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-flask/html-format-from-user-input`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [79](https://cwe.mitre.org/data/definitions/79.html)

## Description{% #description %}

Use of unsanitized from incoming request for SQL queries is unsafe and leads to SQL injections. Data from requests must be sanitized before being used to issues SQL queries, open file or deserialize data. Make sure the data is sanitized before use.

#### Learn More{% #learn-more %}

- [CWE-79: Improper Neutralization of Input During Web Page Generation](https://cwe.mitre.org/data/definitions/79.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import flask
import requests

app = flask.Flask(__name__)


@app.route("/route/to/resource/<resource_id>")
def resource1(resource_id):
    return f"<a href='/path/to/{resource_id}'>Click me!</a>"

@app.route("/route/to/resource/<resource_id>")
def resource2(resource_id):
    return "<a href='/path/to/{0}'>Click me!</a>".format(resource_id)


@app.route("/route/to/resource/<resource_id>")
def resource3():
    resource_id = flask.request.args.get("resource_id")
    return "<a href='/path/to/%s'>Click me!</a>" % resource_id


@app.route("/route/to/resource/<resource_id>")
def resource4(resource_id):
    ret = f"<a href='/path/to/{resource_id}'>Click me!</a>"
    return ret

@app.route("/route/to/resource/<resource_id>")
def resource2():
    resource_id = flask.request.args.get("resource_id")
    ret = "<a href='/path/to/{0}'>Click me!</a>".format(resource_id)
    return ret


@app.route("/route/to/resource/<resource_id>")
def resource3(resource_id):
    ret = "<a href='/path/to/%s'>Click me!</a>" % resource_id
    return ret
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import flask
import requests

app = flask.Flask(__name__)


@app.route("/route/to/resource/<resource_id>")
def resource2(resource_id):
    return "<a href='/path/to/{0}'>Click me!</a>".format(sanitize(resource_id))


@app.route("/route/to/resource/<resource_id>")
def resource2():
    resource_id = get.data()
    ret = requests.get(foo);
    ret = "<a href='/path/to/{0}'>Click me!</a>".format(resource_id)
    return ret
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 