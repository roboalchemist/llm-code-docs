# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/env-no-refer-envvar.md

---
title: Do not refer to an environment variable within the same ENV
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not refer to an environment variable within the same ENV
---

# Do not refer to an environment variable within the same ENV

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/env-no-refer-envvar`

**Language:** Docker

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

This rule advises against referencing an environment variable within the same `ENV` instruction in a Dockerfile. For example, writing `ENV FOO=bar \ BAZ=$FOO/bla` is problematic because the Docker build process does not expand environment variables declared in the same `ENV` command.

To avoid this issue, declare each environment variable in a separate `ENV` instruction if you need to reference a previously set variable. For instance, use `ENV FOO=bar` followed by `ENV BAZ=${FOO}/bla`. This ensures that `FOO` is properly set and expanded when `BAZ` is defined, leading to more reliable and predictable builds.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
ENV FOO=bar \
    BAZ=$FOO/baz
```

```docker
ENV FOO=bar \
    BAZ=${FOO}/baz
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
ENV FOO=bar
ENV BAZ=${FOO}/baz
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 