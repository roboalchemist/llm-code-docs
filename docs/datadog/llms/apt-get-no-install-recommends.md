# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/apt-get-no-install-recommends.md

---
title: Do not use no-install-recommends
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use no-install-recommends
---

# Do not use no-install-recommends

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/apt-get-no-install-recommends`

**Language:** Docker

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule enforces the use of the `--no-install-recommends` option when installing packages with `apt-get` in Dockerfiles. The `--no-install-recommends` flag ensures that only essential packages are installed, avoiding unnecessary recommended packages that can bloat the image size.

To comply with this rule, always include `--no-install-recommends` in your `apt-get install` commands, for example: `apt-get install -y --no-install-recommends gcc`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
RUN apt-get install -y gcc
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install git
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install git
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
RUN apt-get install -y --no-install-recommends gcc
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install --no-install-recommends git
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install --no-install-recommends git
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
