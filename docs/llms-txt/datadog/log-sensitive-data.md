# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-node-security/log-sensitive-data.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-node-security/log-sensitive-data.md

---
title: Avoid logging sensitive data
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid logging sensitive data
---

# Avoid logging sensitive data

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-node-security/log-sensitive-data`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [532](https://cwe.mitre.org/data/definitions/532.html)

## Description{% #description %}

Do not log sensitive data such as user id, email or other personal data (first name, last name, etc).

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
console.log("email from user" + user.email);
console.log(`email from user ${user.email}`);
logger.info(`email from user ${user.email}`);
logger.info(`email from user ${username}: ${user.email}`);
logger.warn(email);
logger.error(`email from user ${email}`);

foobar.error(`email from user ${email}`);

logger.foobar(`email from user ${email}`);
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
console.log("email from user" + user.id);
console.log(`email from user ${user.uuid}`);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 