# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/no-latest-tag.md

---
title: Do not use latest tag
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use latest tag
---

# Do not use latest tag

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/no-latest-tag`

**Language:** Docker

**Severity:** Warning

**Category:** Security

## Description{% #description %}

Using the `latest` tag can lead to unpredictable builds because the base image may be updated without notice, potentially introducing breaking changes or vulnerabilities. This unpredictability makes it difficult to reproduce builds reliably or troubleshoot issues that arise due to unexpected image updates.

To comply with this rule, specify an explicit version or tag for the base image, such as `debian:jessie` or `python:3.9-slim`. Pinning the base image to a specific version ensures consistent and repeatable builds, improving stability and security by preventing unintended updates.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
FROM debian:latest
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM debian:jessie
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
