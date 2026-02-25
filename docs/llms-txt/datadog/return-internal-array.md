# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/return-internal-array.md

---
title: Do not return internal array
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not return internal array
---

# Do not return internal array

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/return-internal-array`

**Language:** Java

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Avoid returning an array that was defined as a class member. If you want to return an array or the values of the array that is a class member, consider returning a copy of the array.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class SecureSystem {
    String foo;
    UserData [] ud;
    Object bar;
    public void something() {

    }
    public UserData [] getUserData() {
        return ud;
    }
    public void somethingElse() {

    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class SecureSystem {
    String foo;

    Object bar;
    public void something() {

    }
    public UserData [] getUserData() {
        UserData [] ud;
        return ud;
    }
    public void somethingElse() {

    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
