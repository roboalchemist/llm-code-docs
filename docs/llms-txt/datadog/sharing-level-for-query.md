# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/apex-security/sharing-level-for-query.md

---
title: Check sharing level for queries
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Check sharing level for queries
---

# Check sharing level for queries

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `apex-security/sharing-level-for-query`

**Language:** Apex

**Severity:** Notice

**Category:** Security

**CWE**: [284](https://cwe.mitre.org/data/definitions/284.html)

## Description{% #description %}

It is [recommended to use](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm) **with sharing** by default to respect the organization's sharing rules. The mode **without sharing** should be used cautiously, only when elevated access is necessary, such as allowing community users to view certain records. **inherited sharing** is ideal for service classes that need to adapt to the calling context's sharing mode.

### Review your code carefully{% #review-your-code-carefully %}

- Does this code access or modify restricted records?
- Could this code be executed by users who should not have access to those records?
- If the class is marked **inherited sharing**, could it be invoked by a class marked **without sharing**?

If you answered **yes** to any of these, there is a security risk.

### **Recommended Secure Coding Practices**{% #recommended-secure-coding-practices %}

- **Prefer with sharing** whenever possible.
- Use **without sharing** only after confirming the code cannot be accessed by unauthorized users.
- Use **inherited sharing** only if all calling classes marked **without sharing** are verified as safe.

### Learn more{% #learn-more %}

- [Salesforce documentation](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_keywords_sharing.htm)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```
public without sharing class MyClass {
  public void test() {
    // SOSL query
    List<List<SObject>> searchList = [
        FIND 'Acme*'
        IN ALL FIELDS
        RETURNING Account(Id, Name), Contact(Id, FirstName, LastName), Opportunity(Id, Name)
    ];

    List<Account> accounts = (List<Account>) searchList[0];
    List<Contact> contacts = (List<Contact>) searchList[1];
    List<Opportunity> opportunities = (List<Opportunity>) searchList[2];

    System.debug('Accounts found: ' + accounts);
    System.debug('Contacts found: ' + contacts);
    System.debug('Opportunities found: ' + opportunities);
  }
}
```

```
public without sharing class MyClass {
  public testAccount {
    Account acc = new Account(Name = 'Big Corp');
    // dml expression
    insert acc;

    acc.Name = 'Acme Corp - Updated';
    update acc;

    delete acc;
  }
}
```

```
public inherited sharing class MyClass {
  public List<String> getAllNames() {
    return [SELECT Name FROM Contact];
  }
}
```

```
public without sharing class MyClass {
  public List<String> getAllNames() {
    return [SELECT Name FROM Contact];
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```
public with sharing class MyClass {
  public List<String> getAllNames() {
    return [SELECT Name FROM Contact];
  }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
