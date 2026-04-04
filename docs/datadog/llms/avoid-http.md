# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/avoid-http.md

---
title: Avoid fetching data from HTTP endpoint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid fetching data from HTTP endpoint
---

# Avoid fetching data from HTTP endpoint

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/avoid-http`

**Language:** Docker

**Severity:** Warning

**Category:** Security

**CWE**: [319](https://cwe.mitre.org/data/definitions/319.html)

## Description{% #description %}

Always use `https` links instead of `http`. Do not use clear-text protocols as they lack encryption and authentication.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
RUN cd /tmp && wget http://www.scalastyle.org/scalastyle_config.xml && mv scalastyle_config.xml /scalastyle_config.xml
RUN cd /tmp && curl -O http://www.scalastyle.org/scalastyle_config.xml && mv scalastyle_config.xml /scalastyle_config.xml
RUN foobar http://domain.tld
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
RUN cd /tmp && wget https://www.scalastyle.org/scalastyle_config.xml && mv scalastyle_config.xml /scalastyle_config.xml
RUN cd /tmp && curl -O https://www.scalastyle.org/scalastyle_config.xml && mv scalastyle_config.xml /scalastyle_config.xml
RUN cd /tmp && curl -O http://localhost:8080/path
RUN cd /tmp && curl -O http://127.0.0.1:8080/path
RUN cd /tmp && curl -O http://[::1]:8080/path
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
