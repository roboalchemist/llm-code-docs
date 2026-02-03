# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/sql-injection-turbine.md

---
title: SQL injection in BasePeer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > SQL injection in BasePeer
---

# SQL injection in BasePeer

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/sql-injection-turbine`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [89](https://cwe.mitre.org/data/definitions/89.html)

## Description{% #description %}

When issuing a SQL query with Turbine, make sure you do not build your query manually and use all the utility functions available with the library.

#### Learn More{% #learn-more %}

- [CWE-89: Improper Neutralization of Special Elements used in an SQL Command](https://cwe.mitre.org/data/definitions/89.html)
- [Potential SQL Injection with Turbine](https://find-sec-bugs.github.io/bugs.htm#SQL_INJECTION_TURBINE)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Foobar {

    public void test() {
        List<Record> BasePeer.executeQuery( "select * from Customer where id=" + inputId );
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Foobar {

    public void test() {
        Criteria c = new Criteria();
        c.add( CustomerPeer.ID, inputId );

        List<Customer> customers = CustomerPeer.doSelect( c );
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 