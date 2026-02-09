# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-flask/ssrf-requests.md

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

**ID:** `python-flask/ssrf-requests`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [918](https://cwe.mitre.org/data/definitions/918.html)

## Description{% #description %}

Use of unsanitized data from incoming request for handling SQL request may lead to SQL injection. Incoming request data must always be sanitized before used.

#### Learn More{% #learn-more %}

- [CWE-89: Improper Neutralization of Special Elements used in an SQL Command](https://cwe.mitre.org/data/definitions/89.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import flask
import requests

app = flask.Flask(__name__)

@app.route("/route/to/resource/<resource_id>")
def resource(resource_id):
    foo = requests.get(f"https://api.service.ext/get/by/id/{resource_id}")
    return None


@app.route("/route/to/resource/<resource_id>")
def resource2(resource_id):
    bar = requests.get("https://api.service.ext/get/by/id/" + resource_id})
    return None

@app.route("/route/to/resource/<resource_id>")
def resource3(resource_id):
    baz = requests.get("https://api.service.ext/get/by/id/{0}".format(resource_id}))
    return None


@app.get("/route/to/another/resource/<resource_id>")
def resource4(resource_id):
    foo = requests.get(f"https://api.service.ext/get/by/id/{resource_id}")
    return None

@app.get("/route/to/another/resource/<resource_id>")
def resource5(resource_id):
    bar = requests.get("https://api.service.ext/get/by/id/" + resource_id})
    return None

@app.get("/route/to/another/resource/<resource_id>")
def resource6(resource_id):
    baz = requests.get("https://api.service.ext/get/by/id/{0}".format(resource_id}))
    return None

@app.route("/route/to/resource/the/return/<resource_id>", methods=["GET"])
def get_param():
    rid = flask.request.args.get("resource_id")
    # unsanitized data
    requests.post(f"https://api.service.ext/get/by/id/{rid}", timeout=10)
    requests.patch(rid, timeout=10)
    requests.get("https://api.service.ext/get/by/id/{0}".format(rid))
    requests.get("https://api.service.ext/get/by/id/" + rid)
    requests.patch(rid, timeout=10)
    return None

@app.route("/this/is/fine/<sure>")
def fine(sure):
    print("foobar")
    return requests.get("https://api.service.ext/nothing")
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import flask
import requests

app = flask.Flask(__name__)

@app.route("/route/to/resource/<resource_id>")
def resource(resource_id):
    sanitized_resource_id = sanitize(resource_id)
    foo = requests.get(f"https://api.service.ext/get/by/id/{sanitized_resource_id}")
    return foo
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 