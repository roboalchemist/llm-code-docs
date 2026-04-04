# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/multiple-healthcheck.md

---
title: Do not use multiple HEALTHCHECK
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use multiple HEALTHCHECK
---

# Do not use multiple HEALTHCHECK

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/multiple-healthcheck`

**Language:** Docker

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

A Dockerfile with multiple `HEALTHCHECK` instructions is confusing. A container should only have one `HEALTHCHECK` instruction.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
HEALTHCHECK CMD foo
HEALTHCHECK CMD bar
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
HEALTHCHECK CMD foo
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
