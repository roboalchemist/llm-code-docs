# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/ldap-entry-poisoning.md

---
title: Prevent LDAP Entry Poisoning
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent LDAP Entry Poisoning
---

# Prevent LDAP Entry Poisoning

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/ldap-entry-poisoning`

**Language:** Java

**Severity:** Info

**Category:** Security

## Description{% #description %}

JNDI API support the binding of serialize object in LDAP directories and can lead to remove code execution. Generally, object deserialization should be consider a risky operation that can lead to remote code execution. This exploitation has been demonstrated at Black Hat USA 2016.

#### Learn More{% #learn-more %}

- [Black Hat 2016 Exploitation](https://www.blackhat.com/docs/us-16/materials/us-16-Munoz-A-Journey-From-JNDI-LDAP-Manipulation-To-RCE-wp.pdf)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class NotCompliant {
    public void myMethod() {
        DirContext ctx = new InitialDirContext();

        ctx.search(query, filter,
                new SearchControls(scope, countLimit, timeLimit, attributes,
                    true,
                    deref));
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Compliant {
    public void myMethod() {
        DirContext ctx = new InitialDirContext();

        ctx.search(query, filter,
                new SearchControls(scope, countLimit, timeLimit, attributes,
                    false,
                    deref));
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 