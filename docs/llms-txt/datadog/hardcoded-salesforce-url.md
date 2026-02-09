# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/apex-security/hardcoded-salesforce-url.md

---
title: Avoid hardcoded salesforce URL
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid hardcoded salesforce URL
---

# Avoid hardcoded salesforce URL

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `apex-security/hardcoded-salesforce-url`

**Language:** Apex

**Severity:** Notice

**Category:** Security

## Description{% #description %}

Using absolute URLs to reference Salesforce pages introduces fragility, as sandbox and production environments are assigned different instance names. Code written with absolute URLs will only function within the corresponding Salesforce instance and will fail once deployed elsewhere. To ensure portability and reliability, always use relative URLsâomitting both domain and subdomainâwhen linking to Salesforce pages.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```
public class AccountHelper {
    
    // A method inside the class
    public List<Account> getActiveAccounts(Integer limitSize) {
        String foo = 'https://subdomain.salesforce.com/something';
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```
public class AccountHelper {
    
    // A method inside the class
    public List<Account> getActiveAccounts(Integer limitSize) {
        String foo = URL.getSalesforceBaseUrl().toExternalForm() + '/something';
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 