# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-flask/ldap-injection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/ldap-injection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/ldap-injection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/ldap-injection.md

---
title: Prevent LDAP injection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent LDAP injection
---

# Prevent LDAP injection

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/ldap-injection`

**Language:** C#

**Severity:** Warning

**Category:** Security

**CWE**: [90](https://cwe.mitre.org/data/definitions/90.html)

## Description{% #description %}

Unvalidated user inputs may lead to LDAP injection. Always escape characters in your LDAP queries. Do not build LDAP queries manually.

#### Learn More{% #learn-more %}

- [Escaping non special characters in string for LDAP query](https://stackoverflow.com/questions/12550358/escaping-non-special-characters-in-string-for-ldap-query)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
public class MyController : Controller
{
    public bool userExists(string user, string pass)
    {
        DirectoryEntry directory  = new DirectoryEntry();
        DirectorySearcher directorySearch  = new DirectorySearcher(directory);

        directorySearch.Filter = "(&(uid=" + user + ")(userPassword=" + pass + "))";

        return directorySearch.FindOne() != null;
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 