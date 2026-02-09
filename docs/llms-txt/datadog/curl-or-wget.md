# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/curl-or-wget.md

---
title: Use either wget or curl but not both
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use either wget or curl but not both
---

# Use either wget or curl but not both

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/curl-or-wget`

**Language:** Docker

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule enforces the use of either `wget` or `curl` exclusively within a Dockerfile, but not both. Mixing these two tools in the same Dockerfile can lead to unnecessary complexity and larger image sizes due to installing multiple similar utilities. It also reduces consistency and maintainability of the Dockerfile.

To comply with this rule, choose either `wget` or `curl` based on your preference or the base image's default availability, and use it consistently throughout your Dockerfile. For example, if you decide to use `curl`, replace all occurrences of `wget` with equivalent `curl` commands like `curl -O <url>`. This approach ensures clarity and reduces the image footprint.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
FROM debian
RUN curl http://bing.com
ADD something somethingelse
RUN wget http://google.com
```

```docker
FROM debian
RUN wget http://google.com
ADD something somethingelse
RUN curl http://bing.com
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM debian
RUN curl http://google.com
RUN curl http://bing.com
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 