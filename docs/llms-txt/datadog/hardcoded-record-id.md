# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/apex-code-style/hardcoded-record-id.md

---
title: Avoid hardcoded Record Id
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid hardcoded Record Id
---

# Avoid hardcoded Record Id

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `apex-code-style/hardcoded-record-id`

**Language:** Apex

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

This rule encourages developers to avoid hardcoding full Salesforce record IDs directly in Apex code. Hardcoded IDs, typically 15 or 18 characters long, can lead to fragile and environment-dependent code that breaks when deployed across sandboxes or production orgs where record IDs differ.

Using hardcoded IDs is problematic because record IDs vary between Salesforce environments and can change if records are deleted and recreated. This causes maintenance issues and potential runtime errors when the code references nonexistent records.

To comply with this rule, developers should use alternative approaches such as querying records dynamically based on unique fields, using custom settings or custom metadata to store IDs, or referencing record types by their developer names or other stable identifiers. For example, instead of `foo.RecordTypeId = '0123000000095Km';`, use a query like `foo.RecordTypeId = [SELECT Id FROM RecordType WHERE DeveloperName = 'MyRecordType' AND SobjectType = 'MyObject__c'].Id;`.

Adopting these best practices ensures that Apex code is more robust, maintainable, and portable across different Salesforce environments. It also facilitates easier updates and reduces the risk of hard-to-diagnose errors related to invalid record references.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```
// 15 characters
foo.RecordTypeId ='0123000000095Km'
```

```
// 15 characters
foo.RecordTypeId ='0123000000095Kmwer'
```

## Compliant Code Examples{% #compliant-code-examples %}

```
// 5 characters
foo.RecordTypeId ='4532d'

// 15 characters with a non-alphabetic one
foo.RecordTypeId ='01230000000 5Km'
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
