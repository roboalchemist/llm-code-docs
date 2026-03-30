# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/alias-must-be-unique.md

---
title: FROM aliases must be unique
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > FROM aliases must be unique
---

# FROM aliases must be unique

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/alias-must-be-unique`

**Language:** Docker

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

When using multiple images in a Dockerfile, aliases must be unique.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
FROM awesomeimage:version as build
RUN stuff
FROM otherawesomeimage:version1 as foobar
RUN plop
FROM otherawesomeimage:version2 as build
RUN more_stuff
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM awesomeimage:version as build
RUN stuff
FROM otherawesomeimage:version as another-alias
RUN more_stuff
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
