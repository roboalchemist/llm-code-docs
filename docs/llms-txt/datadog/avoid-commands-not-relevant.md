# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/avoid-commands-not-relevant.md

---
title: Avoid commands not made for containers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid commands not made for containers
---

# Avoid commands not made for containers

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/avoid-commands-not-relevant`

**Language:** Docker

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Some commands do not make sense to use when building a container. They require user inputs which cannot work when building a container. Avoid such commands in a Dockerfile.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
FROM busybox
RUN top
RUN vim
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM busybox
RUN mycommand foo bar
RUN apt-get install vim
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
