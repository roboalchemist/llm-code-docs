# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-express/access-restriction.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-express/access-restriction.md

---
title: Limit exposure to sensitive directories and files
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Limit exposure to sensitive directories and files
---

# Limit exposure to sensitive directories and files

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-express/access-restriction`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [548](https://cwe.mitre.org/data/definitions/548.html)

## Description{% #description %}

Exposing a directory listing could present an attacker an opportunity to access source code or other sensitive data through a file structure exploit. Restricting access to non-sensitive directories and files is strongly suggested.

#### Learn More{% #learn-more %}

- [Express Serve index middleware](https://expressjs.com/en/resources/middleware/serve-index.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
const express = require("express")
const serveIndex = require("serve-index")

const app = express()

app.use(serveIndex())
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
const express = require("express")
const serveIndex = require("serve-index")

const app = express()

app.use(serveIndex("/public"))
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
