# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/apex-security/avoid-dml-native-statements.md

---
title: Avoid DML native statements
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid DML native statements
---

# Avoid DML native statements

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `apex-security/avoid-dml-native-statements`

**Language:** Apex

**Severity:** Warning

**Category:** Security

**CWE**: [863](https://cwe.mitre.org/data/definitions/863.html)

## Description{% #description %}

Native DML code executes in system context by default, which ignores the current user's object permissions, field-level security (FLS), and sharing rules. In practice, this allows your code to read, update, or delete records and fields that the user wouldn't normally have access to in the UI or API. If you don't explicitly add CRUD/FLS and sharing checks, you risk exposing or modifying sensitive data â for example, letting a user indirectly change ownership, flip a restricted flag, or view confidential fields.

When using DML statement, always check if you could not implement this code using traditional CRUD operations.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```
Account acc = new Account(External_Id__c = 'EX123', Name = 'Acme Global');
upsert acc External_Id__c;  // specify external Id field
```

```
Account acc = [SELECT Id FROM Account WHERE Name = 'Acme Corp Updated' LIMIT 1];
delete acc;
```

```

Account acc = new Account(Name = 'Acme Corporation');
insert acc;
```

```
Account acc = [SELECT Id, Name FROM Account WHERE Name = 'Acme Corporation' LIMIT 1];
acc.Name = 'Acme Corp Updated';

update acc;
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
