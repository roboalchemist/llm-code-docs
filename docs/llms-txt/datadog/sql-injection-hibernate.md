# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/sql-injection-hibernate.md

---
title: SQL injection in Hibernate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > SQL injection in Hibernate
---

# SQL injection in Hibernate

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/sql-injection-hibernate`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [89](https://cwe.mitre.org/data/definitions/89.html)

## Description{% #description %}

Never build a SQL query by concatenating string. Instead, make sure that you use Hibernate functionalities to prevent SQL Injection.

#### Learn More{% #learn-more %}

- [CWE-89: Improper Neutralization of Special Elements used in an SQL Command](https://cwe.mitre.org/data/definitions/89.html)
- [Potential SQL Injection with Hibernate](https://find-sec-bugs.github.io/bugs.htm#SQL_INJECTION_HIBERNATE)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Foobar {

    public void test() {
        Session session = sessionFactory.openSession();
        Query q = session.createQuery("select t from UserEntity t where id = " + input);
        q.execute();
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Foobar {

    public void test() {
        Session session = sessionFactory.openSession();
        Query q = session.createQuery("select t from UserEntity t where id = :userId");
        q.setString("userId",input);
        q.execute();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
