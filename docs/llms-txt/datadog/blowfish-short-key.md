# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/blowfish-short-key.md

---
title: Blowfish should use a large key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Blowfish should use a large key
---

# Blowfish should use a large key

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/blowfish-short-key`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [326](https://cwe.mitre.org/data/definitions/326.html)

## Description{% #description %}

When using Blowfish, use at least 128 bits of entropy to prevent potential vulnerabilities.

#### Learn More{% #learn-more %}

- [Wikipedia - Blowfish weaknesses](https://en.wikipedia.org/wiki/Blowfish_%28cipher%29#Weakness_and_successors)
- [CWE-326: Inadequate Encryption Strength](https://cwe.mitre.org/data/definitions/326.html)

## Arguments{% #arguments %}

- `min-length`: Minimum length for a Blowfish key. Default: 128.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class MyClass {

    public void test () {
        KeyGenerator keyGen = KeyGenerator.getInstance("Blowfish");
        keyGen.init(64);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class MyClass {

    public void test () {
        KeyGenerator keyGen = KeyGenerator.getInstance("Blowfish");
        keyGen.init(128);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
