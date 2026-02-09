# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/use-absolute-paths.md

---
title: Use absolute paths or. use WORKDIR to switch directories
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use absolute paths or. use WORKDIR to switch directories
---

# Use absolute paths or. use WORKDIR to switch directories

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/use-absolute-paths`

**Language:** Docker

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule encourages the use of absolute paths or the `WORKDIR` instruction to change directories within Dockerfiles instead of chaining commands with `cd`. Using relative paths combined with `cd` in a single `RUN` instruction can lead to less readable and more error-prone code. It also makes it harder to track the current working directory during image builds.

To comply, either set the working directory explicitly using `WORKDIR /path/to/directory` before running commands or use absolute paths in instructions like `RUN cp /source/file /destination/path`. Avoid combining `cd` with other commands in a single `RUN` line, as this can cause unexpected behavior and complicate debugging.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
FROM busybox
RUN cd /usr/src/app && cp somedir/somefile ./someDirInUsrSrcApp/
```

```docker
FROM busybox
RUN cd /usr/src/app && git clone git@github.com:lukasmartinelli/hadolint.git 
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM busybox
RUN cp somedir/somefile /usr/src/app/someDirInUsrSrcApp/
```

```docker
FROM busybox
WORKDIR /usr/src/app
RUN git clone git@github.com:lukasmartinelli/hadolint.git
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 