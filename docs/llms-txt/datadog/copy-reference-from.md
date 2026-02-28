# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/copy-reference-from.md

---
title: COPY cannot reference the FROM alias
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > COPY cannot reference the FROM alias
---

# COPY cannot reference the FROM alias

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/copy-reference-from`

**Language:** Docker

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule enforces that the `COPY` instruction must reference a valid build stage alias defined by a preceding `FROM` statement using the `as` keyword. Specifically, the `--from` flag in `COPY` should only point to an existing build stage alias, ensuring that the source files are correctly retrieved from the intended build context.

To avoid violations, always declare build stages with `FROM <image> as <alias>` before using `COPY --from=<alias>`. Verify that the alias used in `COPY` matches exactly with the alias declared in the earlier `FROM` statement. For example, using `FROM debian:jesse as build` followed by `COPY --from=build ...` ensures compliance and reliable builds.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
FROM debian:jesse as build

COPY --from=build some stuff ./
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM debian:jesse as build

RUN stuff

FROM debian:jesse

COPY --from=build some stuff ./
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
