# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/avoid-add-use-copy.md

---
title: Use COPY instead of ADD
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use COPY instead of ADD
---

# Use COPY instead of ADD

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/avoid-add-use-copy`

**Language:** Docker

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

This rule encourages the use of `COPY` instead of `ADD` in Dockerfiles when simply copying files or directories. While both instructions can copy files into the image, `ADD` has additional functionality such as extracting local tar archives and fetching remote URLs.

To make your Dockerfiles more uniform and predictable, you should use `COPY` unless you need `ADD`'s extra functionality.

See [official Docker documentation](https://docs.docker.com/build/building/best-practices/#add-or-copy)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
FROM python:3.4
ADD requirements.txt /usr/src/app/
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM python:3.4
COPY requirements.txt /usr/src/app/
ADD https://example.com/file.go /src
ADD archive.tar.gz /src/archive
ADD git@github.com:user/repo.git /src/foorepo
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
