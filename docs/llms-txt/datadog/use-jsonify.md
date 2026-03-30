# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-flask/use-jsonify.md

---
title: use jsonify instead of json.dumps for JSON output
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > use jsonify instead of json.dumps for JSON output
---

# use jsonify instead of json.dumps for JSON output

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-flask/use-jsonify`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

With the flask framework, `jsonify` helps you write API endpoints that return JSON data.

#### Learn More{% #learn-more %}

- [Python Flask: `jsonify()`](https://flask.palletsprojects.com/en/2.3.x/api/#flask.json.jsonify)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
@app.route("/article")
def get_article():
    article = get_article_by_id(request.args.get("id"))
    return json.dumps(article) # use flask.jsonify instead of json.dumps
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
from flask import jsonify

@app.route("/article")
def get_article():
    article = get_article_by_id(request.args.get("id"))
    return jsonify(article)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
