# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/hardcoded-crypto-key.md

---
title: Secret should not be hardcoded in code
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Secret should not be hardcoded in code
---

# Secret should not be hardcoded in code

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/hardcoded-crypto-key`

**Language:** Java

**Severity:** Error

**Category:** Security

**CWE**: [312](https://cwe.mitre.org/data/definitions/312.html)

## Description{% #description %}

Sensitive information should not be written in cleartext in code. This would leak secrets to unauthorized entities. Instead of writing secrets directly into the code, store the secrets in a secure vault or in environment variables. Make sure you also rotate secrets periodically.

#### Learn More{% #learn-more %}

- [CWE-312: Cleartext Storage of Sensitive Information](https://cwe.mitre.org/data/definitions/312.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Foo {
    void bad() {
        SecretKeySpec secretKeySpec = new SecretKeySpec("my secret here".getBytes(), "AES");
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Foo {
    void good() {
        SecretKeySpec secretKeySpec = new SecretKeySpec(Properties.getKey(), "AES");
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
