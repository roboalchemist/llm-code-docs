# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/onbuild-allowed-actions.md

---
title: FROM or MAINTAINER cannot be triggered within ONBUILD
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > FROM or MAINTAINER cannot be triggered within ONBUILD
---

# FROM or MAINTAINER cannot be triggered within ONBUILD

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/onbuild-allowed-actions`

**Language:** Docker

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

No description found

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
ONBUILD FROM debian
```

```docker
ONBUILD MAINTAINER Ron Weasley
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM maven:3-jdk-8

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD ADD . /usr/src/app

ONBUILD RUN mvn install
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 