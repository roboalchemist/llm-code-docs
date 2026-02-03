# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-express/https-protocol-missing.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-express/https-protocol-missing.md

---
title: Use `https` protocol over `http`
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use `https` protocol over `http`
---

# Use `https` protocol over `http`

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-express/https-protocol-missing`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [693](https://cwe.mitre.org/data/definitions/693.html)

## Description{% #description %}

Per [Express documentation](https://expressjs.com/en/advanced/best-practice-security.html#use-tls):

If your app deals with or transmits sensitive data, use [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS) to secure the connection and the data. This technology encrypts data before it is sent from the client to the server, thus preventing some common (and easy) hacks.

This rule will detect the usage of non `https.createServer()` usage.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var http = require('http');
var express = require('express');
var app = express();

var httpServer = http.createServer(app)
httpServer.listen(8080);
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var https = require('https');
var express = require('express');
var app = express();

var httpsServer = https.createServer(app)
httpsServer.listen(8080);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 