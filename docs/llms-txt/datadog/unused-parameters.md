# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/apex-code-style/unused-parameters.md

---
title: Avoid unused parameters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid unused parameters
---

# Avoid unused parameters

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `apex-code-style/unused-parameters`

**Language:** Apex

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule identifies method parameters that are declared but never used within the method body. Unused parameters can lead to confusion, as they suggest that a value is expected or utilized when it is not, reducing code clarity and maintainability.

To comply with this rule, ensure that every parameter declared in a method signature is actively used within the method. If a parameter is unnecessary, remove it from the method signature. For example, instead of having `public static List<Account> getActiveAccounts(Integer limitSize)` where `limitSize` is unused, either use it appropriately in your query or eliminate it entirely.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```
public with sharing class AccountHelper {
    public static Integer limitSize = 2;    
    // A method inside the class
    public static List<Account> getActiveAccounts(Integer limitSize) {
        this.limitSize = 5;
    }
}
```

```
public with sharing class AccountHelper {
    
    // A method inside the class
    public static List<Account> getActiveAccounts(Integer limitSize) {
        // Query Accounts where Active__c (a custom checkbox field) is true
        List<Account> activeAccounts = [
            SELECT Id, Name, Industry
            FROM Account
            WHERE Active__c = true
            ORDER BY Name
        ];
        
        return activeAccounts;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```
public with sharing class AccountHelper {
    
    // A method inside the class
    public static List<Account> getActiveAccounts(Integer limitSize) {
        // Query Accounts where Active__c (a custom checkbox field) is true
        List<Account> activeAccounts = [
            SELECT Id, Name, Industry
            FROM Account
            WHERE Active__c = true
            ORDER BY Name
            LIMIT :limitSize
        ];
        
        return activeAccounts;
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 