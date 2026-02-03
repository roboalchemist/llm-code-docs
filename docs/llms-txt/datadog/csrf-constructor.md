# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/apex-security/csrf-constructor.md

---
title: Avoid DML statements in constructor
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid DML statements in constructor
---

# Avoid DML statements in constructor

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `apex-security/csrf-constructor`

**Language:** Apex

**Severity:** Warning

**Category:** Security

**CWE**: [352](https://cwe.mitre.org/data/definitions/352.html)

## Description{% #description %}

Placing DML operations inside an Apex class constructor or initializer can cause **unintended side effects**. For example, simply loading a Visualforce page or initializing a component could automatically run inserts, updates, or deletes â modifying the database without any explicit user action. This makes the behavior unpredictable and potentially insecure. In contrast, performing **SOQL queries** in constructors or initializers is allowed, since queries do not modify data.

For example, consider the code below, accessing a page that references AccountHandler will cause a database insert, even if the user didn't intend to create a record.

```
public class AccountHandler {
    public AccountHandler() {
        // Dangerous: Just initializing this class will insert a record
        Account acc = new Account(Name = 'Auto Created');
        insert acc; 
    }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```
public class MyClass {
    public MyClass() {
        insert something;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```
public class MyClass {
    public MyClass() {
        // anything but a DML statement
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 