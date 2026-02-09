# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/ssl-context.md

---
title: Do not use weak SSL context
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use weak SSL context
---

# Do not use weak SSL context

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/ssl-context`

**Language:** Java

**Severity:** Notice

**Category:** Security

## Description{% #description %}

Do not use `"SSL"` as it uses an old protocol. Use `"TLS"` instead.

#### Learn More{% #learn-more %}

- [Difference between SSL and TLS](https://serverfault.com/questions/64484/functional-implications-of-differences-in-ssl-and-tls/368574#368574)
- [Weak SSL Context](https://find-sec-bugs.github.io/bugs.htm#SSL_CONTEXT)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Foo {
    
    public static foobar() {
        SSLContext.getInstance("SSL");
    }
}
    
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Foo {
    
    public static foobar() {
        SSLContext.getInstance("TLS");
    }
}
    
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 