# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-express/default-session-config.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-express/default-session-config.md

---
title: Enforce overriding default config
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce overriding default config
---

# Enforce overriding default config

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-express/default-session-config`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [523](https://cwe.mitre.org/data/definitions/523.html)

## Description{% #description %}

Avoid leaving your session cookies open to exploits or unauthorized access, by overriding default values.

Setting the `name` value to something generic is better than using the default value.

#### Learn More{% #learn-more %}

- [Express Security Best Practices](https://expressjs.com/en/advanced/best-practice-security.html#use-cookies-securely)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
const session = require('express-session')

app.use(
    session({
        secret: "secret"
    })
)
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
const session = require('express-session')

app.use(
    session({
        secret: "secret",
        name: 'sessionId'
    })
)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
