# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/no-from-image.md

---
title: Dockerfiles should specify a base image
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Dockerfiles should specify a base image
---

# Dockerfiles should specify a base image

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/no-from-image`

**Language:** Docker

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

The rule stipulates that all Dockerfiles must specify a base image. This is important because without specifying a base image, you are building a container from scratch, and this is likely what is not intended.

To avoid violating this rule, always declare a base image at the start of your Dockerfile using the `FROM` keyword. For example, `FROM ubuntu:18.04` sets the base image to Ubuntu 18.04.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
RUN echo "hello"
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM image as base

# foo

FROM image2
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
