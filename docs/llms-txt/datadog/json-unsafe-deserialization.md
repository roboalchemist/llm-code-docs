# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/json-unsafe-deserialization.md

---
title: Avoid unsafe deserialization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid unsafe deserialization
---

# Avoid unsafe deserialization

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/json-unsafe-deserialization`

**Language:** Java

**Severity:** Error

**Category:** Security

**CWE**: [502](https://cwe.mitre.org/data/definitions/502.html)

## Description{% #description %}

Deserialization of untrusted data can lead to undesired code execution. Use `activateDefaultTyping` to prevent deserialization into random classes.

#### Learn More{% #learn-more %}

- [ObjectMapper JavaDoc](https://javadoc.io/doc/com.fasterxml.jackson.core/jackson-databind/2.9.8/com/fasterxml/jackson/databind/ObjectMapper.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Main {
    public static void main(String[] args) {
        ObjectMapper mapper = new ObjectMapper();
        oneFunction();
        oneFunction();
        mapper.readValue(json, ABean.class);
        foo.var();
        anotherFunction();
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Main {
    public static void main(String[] args) {
        ObjectMapper mapper = new ObjectMapper();
        oneFunction();
        mapper.enableDefaultTyping();
        anotherFunction();
        mapper.readValue(json, ABean.class);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
