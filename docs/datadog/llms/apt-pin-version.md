# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/apt-pin-version.md

---
title: Always pin versions in apt-get install
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Always pin versions in apt-get install
---

# Always pin versions in apt-get install

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/apt-pin-version`

**Language:** Docker

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

When using `apt-get install`, pin the version to avoid unwanted upgrades and undefined behavior.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
FROM debian:12

RUN set -eux; \
    apt-get update; \
    apt-get install -y curl git gcc g++ make cmake; \
    rm -rf /var/cache/apt/archives /var/lib/apt/lists/*
```

```docker
FROM debian:12
RUN apt-get install python

RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-19-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/ /var/cache/oracle*
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM debian:12
RUN apt-get install python=3.11
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
