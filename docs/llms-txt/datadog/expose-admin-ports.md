# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/expose-admin-ports.md

---
title: Do not expose sensitive ports
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not expose sensitive ports
---

# Do not expose sensitive ports

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/expose-admin-ports`

**Language:** Docker

**Severity:** Warning

**Category:** Security

## Description{% #description %}

Never expose admin ports such as the SSH port `22` in your container. It increases the surface of attack of your containers.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
FROM debian:jessie
EXPOSE 22
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM debian:jessie
EXPOSE 443
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
