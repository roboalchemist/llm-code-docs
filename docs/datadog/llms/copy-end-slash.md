# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/copy-end-slash.md

---
title: COPY with more than 2 args must end with /
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > COPY with more than 2 args must end with /
---

# COPY with more than 2 args must end with /

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/copy-end-slash`

**Language:** Docker

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule enforces that when the COPY instruction in a Dockerfile has more than two arguments, the last argument must be a directory path ending with a slash (/). This ensures that multiple source files or directories are copied into the specified destination directory correctly. Always ensure that when copying multiple files or directories, the destination path ends with a slash, clearly indicating it is a directory. For example, use `COPY package.json yarn.lock my_app/` instead of `COPY package.json yarn.lock my_app`. This practice improves clarity and prevents ambiguous or incorrect Docker image builds.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
FROM node:carbon
COPY package.json yarn.lock my_app
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM node:carbon
COPY package.json yarn.lock my_app/
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
