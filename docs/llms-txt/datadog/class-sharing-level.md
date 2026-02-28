# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/apex-security/class-sharing-level.md

---
title: Classes with SOQL queries must specify sharing level
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Classes with SOQL queries must specify sharing level
---

# Classes with SOQL queries must specify sharing level

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `apex-security/class-sharing-level`

**Language:** Apex

**Severity:** Warning

**Category:** Security

**CWE**: [284](https://cwe.mitre.org/data/definitions/284.html)

## Description{% #description %}

This rule ensures that any Apex class that use SOQL or SOSL declares its sharing mode using one of the keywords: `with sharing`, `without sharing`, or `inherited sharing`. Specifying the sharing level is crucial because it controls whether the class respects the current user's record-level access permissions when accessing Salesforce data. Without an explicit sharing declaration, the default behavior can lead to unintended data exposure or security issues.

Note that exception classes and classes without any SOQL queries are exempt from this rule, as they do not directly access Salesforce records. Following this best practice ensures that your Apex code respects organizational security policies and prevents accidental data leaks.

## Learn More{% #learn-more %}

- [Sharing definitions](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```
global class MyGlobalClass {
  public List<Contact> getAllTheSecrets() {
    return [SELECT Name FROM Contact];
  }
}
```

```
public abstract class MyClass {
  public void foo(){
  }

  // SOQL query
  public List<Contact> getAllTheSecrets() {
    return [SELECT Name FROM Contact];
  }
}
```

```
public class MyClass {
  public void foo(){
    // SOSL query
    List<List<SObject>> results = [
        FIND 'acme*' IN ALL FIELDS
        RETURNING
            Account(Id, Name, Industry LIMIT 5),
            Contact(Id, Name, Email LIMIT 5),
            Case(Id, CaseNumber, Subject ORDER BY CreatedDate DESC LIMIT 5)
    ];

    List<Account> accounts = (List<Account>) results[0];
    List<Contact> contacts = (List<Contact>) results[1];
    List<Case>    cases    = (List<Case>)    results[2];
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```
public class MyClass {
  private void bar(){
  }
}
```

```
public without sharing abstract class MyClass {
  public List<Contact> getAllTheSecrets() {
    return [SELECT Name FROM Contact];
  }
}
```

```
public with sharing abstract class MyClass {
  public List<Contact> getAllTheSecrets() {
    return [SELECT Name FROM Contact];
  }
}
```

```gdscript3
public class MyException extends Exception {
  public List<Contact> getAllTheSecrets() {
    return [SELECT Name FROM Contact];
  }
}
```

```
public inherited sharing class MyClass {
  public List<Contact> getAllTheSecrets() {
    return [SELECT Name FROM Contact];
  }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
