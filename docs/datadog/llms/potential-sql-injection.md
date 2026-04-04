# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/potential-sql-injection.md

---
title: SQL injection in SqlUtil.execQuery
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > SQL injection in SqlUtil.execQuery
---

# SQL injection in SqlUtil.execQuery

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/potential-sql-injection`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [89](https://cwe.mitre.org/data/definitions/89.html)

## Description{% #description %}

The parameter of the SQL query should be properly escaped and validated.

#### Learn More{% #learn-more %}

- [CWE-89: Improper Neutralization of Special Elements used in an SQL Command](https://cwe.mitre.org/data/definitions/89.html)
- [Potential Injection](https://find-sec-bugs.github.io/bugs.htm#CUSTOM_INJECTION)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Foobar {

    public void test() {
        SqlUtil.execQuery("select * from UserEntity t where id = " + parameterInput);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Foobar {

    public void test() {
        SqlUtil.execQuery("select * from UserEntity t where id = " + sanitize(parameterInput));
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
