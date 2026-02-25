# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/http-parameter-pollution.md

---
title: Prevent HTTP parameter pollution
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent HTTP parameter pollution
---

# Prevent HTTP parameter pollution

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/http-parameter-pollution`

**Language:** Java

**Severity:** Warning

**Category:** Security

## Description{% #description %}

Do not concatenate HTTP parameters. Instead, use a proper API to set each parameter.

#### Learn More{% #learn-more %}

- [HTTP Parameter Pollution](https://capec.mitre.org/data/definitions/460.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Main {
    public void myMethod() {
        String input = request.getParameter("lang");
        GetMethod get = new GetMethod("https://api.endoint/path/to/api");
        get.setQueryString("param1=" + param1Value);

        if (true) {
            get.setQueryString("param1=" + param1Value);
        } else {
            get.setQueryString("param1=" + param1Value);
        }
        get.execute();
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Main {
    public void myMethod() {
        URIBuilder uriBuilder = new URIBuilder("https://api.endoint/path/to/api");
        uriBuilder.addParameter("param1", param1Value);

        HttpGet httpget = new HttpGet(uriBuilder.build().toString());
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
