# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/maintainer-deprecated.md

---
title: The maintainer entry is deprecated
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > The maintainer entry is deprecated
---

# The maintainer entry is deprecated

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/maintainer-deprecated`

**Language:** Docker

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Use `LABEL` instead of `MAINTAINER` to report the maintainer of a Dockerfile.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
MAINTAINER Jean Bar <jean@bar.fr>
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
LABEL maintainer="Jean Bar <jean@bar.fr>"
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
