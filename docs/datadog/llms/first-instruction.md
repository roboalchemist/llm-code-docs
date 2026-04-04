# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/first-instruction.md

---
title: First instruction should be ARG or FROM
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > First instruction should be ARG or FROM
---

# First instruction should be ARG or FROM

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/first-instruction`

**Language:** Docker

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule enforces that the very first instruction in a Dockerfile must be either `ARG` or `FROM`. These instructions are fundamental for defining the build-time variables and the base image, respectively, which are crucial for the Docker build process to function correctly. Starting with `ARG` or `FROM` ensures that the build context is properly initialized before any other commands are executed. This helps avoid unexpected behaviors or errors during the build, as Docker needs a base image or build argument context to interpret subsequent instructions.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
COPY foo bar
```

```docker
ADD foo bar
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
ARG foo
RUN something
```

```docker
# Something
FROM debian:jessie
RUN foobar
```

```docker
FROM debian:jessie
RUN foobar
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
