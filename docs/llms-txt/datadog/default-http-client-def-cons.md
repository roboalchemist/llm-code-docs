# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/default-http-client-def-cons.md

---
title: DefaultHttpClient with default constructor is not secure
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > DefaultHttpClient with default constructor is not secure
---

# DefaultHttpClient with default constructor is not secure

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/default-http-client-def-cons`

**Language:** Java

**Severity:** Notice

**Category:** Security

**CWE**: [326](https://cwe.mitre.org/data/definitions/326.html)

## Description{% #description %}

DefaultHttpClient with default constructor is not compatible with TLS 1.2. Make sure your HTTP client support advanced encryption protocols.

#### Learn more{% #learn-more %}

- [DefaultHttpClient with default constructor is not compatible with TLS 1.2](https://find-sec-bugs.github.io/bugs.htm#SSL_CONTEXT)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public Class {

    public void foobar(){
        HttpClient client = new DefaultHttpClient();
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public Class {

    public void foobar() {
        HttpClient client1 = HttpClients.createSystem();
        HttpClient client = HttpClientBuilder.create().useSystemProperties().build();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
