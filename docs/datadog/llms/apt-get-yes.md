# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/apt-get-yes.md

---
title: Always use -y with apt-get install
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Always use -y with apt-get install
---

# Always use -y with apt-get install

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/apt-get-yes`

**Language:** Docker

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

The rule "Always use -y with apt-get install" is a best practice in Dockerfile development to ensure that the Docker build process is non-interactive. Dockerfiles should be designed to build without requiring any user intervention. By using the `-y` flag with `apt-get install`, you can automatically answer yes to any prompts that the installation process might produce, making the process non-interactive.

This rule is crucial because a Docker build that requires user interaction can cause problems in automated build systems. It can lead to build failures or unexpected results due to lack of user response. This is especially important in CI/CD pipelines where the Docker build process should be fully automated.

To adhere to this rule, always include the `-y` flag when using `apt-get install` in your Dockerfiles. For example, instead of writing `RUN apt-get install gcc`, write `RUN apt-get install -y gcc`. Also, to avoid potential issues with locale settings, you can use `DEBIAN_FRONTEND=noninteractive` in conjunction with `apt-get install`. For instance, `RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y git`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
RUN echo "run apt-get install "
RUN echo "run apt-get install " && apt-get install wget
RUN echo "run apt-get install " || apt-get install wget
RUN echo "run apt-get install " ; apt-get install wget
```

```docker
RUN apt-get install gcc
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
RUN apt-get install -y gcc
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install git
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install git
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
