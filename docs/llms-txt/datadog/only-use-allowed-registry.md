# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/only-use-allowed-registry.md

---
title: Use only an allowed registry in the FROM image
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use only an allowed registry in the FROM image
---

# Use only an allowed registry in the FROM image

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/only-use-allowed-registry`

**Language:** Docker

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

This rule enforces the use of only allowed registries in the `FROM` instruction of a Dockerfile. It ensures that base images are pulled from trusted and verified sources, reducing the risk of introducing malicious or unverified software into your container environment.

To comply with this rule, always specify base images using registries that are explicitly permitted by your organization's policies. For example, use `FROM python:3.6` or `FROM docker.io/python:3.6` instead of `FROM randomrepo/python:3.6`. This practice helps ensure that the images you use are reliable and vetted.

You can specify the exact list of registries to check by defining the `registries` argument and separate them with a comma. There is an example of how to tweak your configuration file to add `registry1` and `registry2`.

```yaml
rulesets:
  - docker-best-practices:
    rules:
      only-use-allowed-registry:
        arguments:
          registries: registry1,registry2
```

## Arguments{% #arguments %}

- `registries`: comma-separated list of trusted registries

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
FROM registry.somedomain.com/images/mirror/dgraph/dgraph:v1.1.0
```

```docker
FROM x.com/debian
```

```docker
FROM randomrepo/python:3.6
FROM registry.something.io/images/base/ubuntu_2204:release
RUN acommand
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM ubuntu:18.04 AS builder1
FROM builder1 AS builder2
```

```docker
FROM python:3.6
RUN acommand
```

```docker
FROM docker.io/python:3.6
FROM scratch
RUN acommand
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 