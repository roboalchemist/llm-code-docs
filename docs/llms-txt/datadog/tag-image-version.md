# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/tag-image-version.md

---
title: Always tag the version of an image
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Always tag the version of an image
---

# Always tag the version of an image

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/tag-image-version`

**Language:** Docker

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule dictates that Docker images should always be tagged with a specific version number. In Docker, an image tag represents a particular version of an image. The use of tags allows developers to have better control over which versions of an image are being used in their projects.

This is crucial because it ensures the consistency and reliability of the Docker environment. If an image is not tagged, Docker defaults to using the 'latest' version of the image. However, the 'latest' tag does not guarantee that the same version of an image will be used every time, which can lead to unexpected behavior or compatibility issues.

To comply with this rule, always specify a version number when pulling a Docker image. Instead of `FROM debian`, write `FROM debian:unstable` or `FROM debian:10.3`. This ensures that you are using a specific version of the image, providing a more predictable and stable environment for your project.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
FROM debian
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM scratch
ADD hello /
CMD ["/hello"]
```

```docker
FROM ${IMAGE}
```

```docker
FROM debian:unstable as base

FROM base as final
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 