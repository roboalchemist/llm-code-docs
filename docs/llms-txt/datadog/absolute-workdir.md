# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/absolute-workdir.md

---
title: Use absolute workdir
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use absolute workdir
---

# Use absolute workdir

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/absolute-workdir`

**Language:** Docker

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

When using a relative `WORKDIR`, you may run into problems since you are dependent on previous `WORKDIR` instructions. Using an absolute `WORKDIR` ensures you have the right path no matter where the instruction is positioned.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
FROM busybox
WORKDIR usr/src/app
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM busybox
WORKDIR /usr/src/app

WORKDIR $MYWORKDIR
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
