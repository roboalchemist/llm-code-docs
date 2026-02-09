# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/pip-no-cache.md

---
title: Do not use cache when installing packages
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use cache when installing packages
---

# Do not use cache when installing packages

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/pip-no-cache`

**Language:** Docker

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule states that Dockerfiles should not use a cache when installing packages. When building Docker images, Docker has a built-in caching mechanism that reuses instructions from previous builds, which can speed up the build process. However, when installing packages, this can lead to outdated packages being used, which might have security vulnerabilities or bugs.

It is important to avoid using a cache when installing packages because it ensures that the latest version of a package is always used. This reduces the risk of security vulnerabilities and bugs, and ensures that your application has the most up-to-date and secure dependencies.

When installing packages with pip in a Dockerfile, use the `--no-cache-dir` option. This tells pip not to use a cache when installing packages, which ensures that the latest version of the package is always used. For example, instead of writing `RUN pip install django`, write `RUN pip install --no-cache-dir django`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
FROM busybox
RUN pip install django
RUN pip3 install django
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM busybox
RUN pip install --no-cache-dir django
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 