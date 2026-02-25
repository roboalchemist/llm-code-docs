# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/yarn-clean.md

---
title: Run yarn clean after yarn install
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Run yarn clean after yarn install
---

# Run yarn clean after yarn install

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/yarn-clean`

**Language:** Docker

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule ensures that after running `yarn install` in a Dockerfile, a `yarn cache clean` command is executed to remove unnecessary cache files. This practice helps to minimize the image size by cleaning up temporary files and caches that are not needed for the runtime environment. mes.

To comply with this rule, always chain `yarn install` with `yarn cache clean` in the same RUN instruction like `RUN yarn install && yarn cache clean`. This approach ensures that the cache cleanup happens immediately after installation, reducing the number of layers and keeping the image optimized.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
RUN yarn install
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
RUN yarn install \
 && yarn cache clean
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
