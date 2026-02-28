# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/permissive-cors.md

---
title: Avoid overly permissive CORS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid overly permissive CORS
---

# Avoid overly permissive CORS

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/permissive-cors`

**Language:** Java

**Severity:** Warning

**Category:** Security

## Description{% #description %}

Do not set overly permissive CORS requests. Restrict the host allowed to communicate with to prevent potential malicious requests in your application.

#### Learn More{% #learn-more %}

- [Fetch Living Standard](https://fetch.spec.whatwg.org/)
- [Enable Cross-Origin Resource Sharing](https://enable-cors.org/)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class NotCompliant {
    @GET
    @Path("/some/path")
    public Response getRoute() {
        response.addHeader("Access-Control-Allow-Origin: *");
    }
}
```

```java
class NotCompliant {
    @GET
    @Path("/some/path")
    public Response getRoute() {
        response.addHeader("Access-Control-Allow-Origin", "*");
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class NotCompliant {
    @GET
    @Path("/some/path")
    public Response getRoute() {
        response.addHeader("Access-Control-Allow-Origin", "https://developer.mozilla.org");
    }
}
```

```java
class NotCompliant {
    @GET
    @Path("/some/path")
    public Response getRoute() {
        response.addHeader("Access-Control-Allow-Origin: https://developer.mozilla.org");
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
