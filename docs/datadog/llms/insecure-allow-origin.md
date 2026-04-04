# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-express/insecure-allow-origin.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-express/insecure-allow-origin.md

---
title: Avoid using an insecure Access-Control-Allow-Origin header
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using an insecure Access-Control-Allow-Origin header
---

# Avoid using an insecure Access-Control-Allow-Origin header

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-express/insecure-allow-origin`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [346](https://cwe.mitre.org/data/definitions/346.html)

## Description{% #description %}

Setting an Access-Control-Allow-Origin header with an unverified user-defined input can lead to sharing sensitive data with an unintended user.

If this is unavoidable, consider comparing the input against a safe-list.

#### Learn More{% #learn-more %}

- [OWASP Origin & Access-Control-Allow-Origin](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/07-Testing_Cross_Origin_Resource_Sharing)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
app.get('/', function (req, res) {
    res.set('Access-Control-Allow-Origin', req.headers.foo)
    res.set({ "foo": "bar", 'Access-Control-Allow-Origin': req.query.foo })
    res.header('Access-Control-Allow-Origin', req.params.foo)
    res.setHeader('Access-Control-Allow-Origin', req.body.foo);
    res.writeHead(200, { "foo": "bar", 'Access-Control-Allow-Origin': req.cookies.foo })
});
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
app.get('/', function (req, res) {
    res.set('Access-Control-Allow-Origin', "foo_url")
    res.set({ "foo": "bar", 'Access-Control-Allow-Origin': "foo_url" })
    res.header('Access-Control-Allow-Origin', "foo_url")
    res.setHeader('Access-Control-Allow-Origin', "foo_url");
    res.writeHead(200, { "foo": "bar", 'Access-Control-Allow-Origin': "foo_url" })
});
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
