# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/avoid-chmod-777.md

---
title: Do not give wide permissions on files
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not give wide permissions on files
---

# Do not give wide permissions on files

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/avoid-chmod-777`

**Language:** Docker

**Severity:** Warning

**Category:** Security

## Description{% #description %}

Make sure you do not give too many permissions with copying or adding a file. Adding write permissions to all means that any other users may modify the files.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
ADD --chmod=777 src dst
COPY --chmod=777 src dst
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
ADD --chmod=755 src dst
COPY --chmod=755 src dst
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
