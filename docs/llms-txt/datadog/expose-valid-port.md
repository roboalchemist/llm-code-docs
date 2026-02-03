# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/expose-valid-port.md

---
title: Expose a valid UNIX port number
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Expose a valid UNIX port number
---

# Expose a valid UNIX port number

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/expose-valid-port`

**Language:** Docker

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The `EXPOSE` instruction should take a valid UNIX port range.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
EXPOSE 1001232323
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
EXPOSE 8080
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 