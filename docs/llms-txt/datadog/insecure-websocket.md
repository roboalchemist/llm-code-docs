# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-browser-security/insecure-websocket.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-browser-security/insecure-websocket.md

---
title: Websockets must use SSL connections
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Websockets must use SSL connections
---

# Websockets must use SSL connections

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-browser-security/insecure-websocket`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [319](https://cwe.mitre.org/data/definitions/319.html)

## Description{% #description %}

Always use secure websocket communication. When using websocket, use addresses that are SSL-enabled.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
const client = new WebSocket('ws://app.domain.tld')
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
const client = new WebSocket('wss://app.domain.tld')
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
