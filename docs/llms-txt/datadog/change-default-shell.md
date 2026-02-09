# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/change-default-shell.md

---
title: Use SHELL to change the default shell
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use SHELL to change the default shell
---

# Use SHELL to change the default shell

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/change-default-shell`

**Language:** Docker

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule encourages the use of the `SHELL` instruction to explicitly change the default shell in a Dockerfile rather than modifying it indirectly through commands like `RUN ln -sfv /bin/bash /bin/sh`. Using `SHELL` provides a clear and declarative way to specify which shell should be used for subsequent instructions, improving readability and maintainability.

To comply with this rule, replace any commands that attempt to change the default shell indirectly, such as `RUN ln -sfv /bin/bash /bin/sh`, with the `SHELL` instruction like `SHELL ["/bin/bash", "-c"]`. This approach keeps your Dockerfile clean and ensures consistent execution of shell commands.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
ADD something somethingelse

RUN ln -sfv /bin/bash /bin/sh
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
ADD something somethingelse

SHELL ["/bin/bash", "-c"]
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 