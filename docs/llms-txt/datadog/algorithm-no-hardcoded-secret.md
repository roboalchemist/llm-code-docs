# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/algorithm-no-hardcoded-secret.md

---
title: No hardcoded secret with algorithm methods
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > No hardcoded secret with algorithm methods
---

# No hardcoded secret with algorithm methods

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/algorithm-no-hardcoded-secret`

**Language:** Java

**Severity:** Error

**Category:** Security

**CWE**: [798](https://cwe.mitre.org/data/definitions/798.html)

## Description{% #description %}

Do not use hardcoded secrets. Instead, use secrets coming from a vault and a secure source.

#### Learn More{% #learn-more %}

- [CWE-798 - Use of hardcoded credentials](https://cwe.mitre.org/data/definitions/798.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class App {
    private static void error1() {
        Algorithm algorithm = Algorithm.HMAC256("secret");
        Algorithm algorithm = Algorithm.HMAC512("secret");
        Algorithm algorithm = Algorithm.HMAC384("secret");
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class App {
    @Test
    public void myFunctionToTest() {
        Algorithm algorithm = Algorithm.HMAC256("secret");
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 