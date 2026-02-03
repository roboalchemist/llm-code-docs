# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/ignore-saml-comment.md

---
title: Ignore SAML comments
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ignore SAML comments
---

# Ignore SAML comments

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/ignore-saml-comment`

**Language:** Java

**Severity:** Error

**Category:** Security

## Description{% #description %}

Ignoring comments in SAML may lead to vulnerabilities.

#### Learn More{% #learn-more %}

- [Duo Finds SAML Vulnerabilities Affecting Multiple Implementations](https://duo.com/blog/duo-finds-saml-vulnerabilities-affecting-multiple-implementations)
- [Spring SAML Vulnerability](https://spring.io/blog/2018/03/01/spring-security-saml-and-this-week-s-saml-vulnerability)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class MyClass {
 
    @Bean
    ParserPool myParserPool() {
        BasicParserPool pool = new BasicParserPool();
        pool.setIgnoreComments(false);
        return pool;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class MyClass {
 
    @Bean
    ParserPool myParserPool() {
        BasicParserPool pool = new BasicParserPool();
        return pool;
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 