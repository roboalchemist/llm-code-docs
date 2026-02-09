# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-express/insecure-cookie.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-express/insecure-cookie.md

---
title: Avoid setting insecure cookie settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid setting insecure cookie settings
---

# Avoid setting insecure cookie settings

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-express/insecure-cookie`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [1004](https://cwe.mitre.org/data/definitions/1004.html)

## Description{% #description %}

When using cookies in your application, one should ensure appropriate security options are set to lessen the risk of exploits and unauthorized users.

This rule will detect when `secure` and `httpOnly` are set to `false` in a multitude of ways.

#### Learn More{% #learn-more %}

- [Express Security Best Practices](https://expressjs.com/en/advanced/best-practice-security.html#use-cookies-securely)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
const cookie = {
    secure: false,
    httpOnly: false,
}

const options = {
    cookie: {
        secure: false,
        httpOnly: false,
    }
}

cookieSession({ secure: false })
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
const cookie = {
    secure: true,
    httpOnly: true,
}

const options = {
    cookie: {
        secure: true,
        httpOnly: true,
    }
}

cookieSession({ secure: true })
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 