# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/ldap-without-password.md

---
title: Avoid connecting to a LDAP server without password
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid connecting to a LDAP server without password
---

# Avoid connecting to a LDAP server without password

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/ldap-without-password`

**Language:** PHP

**Severity:** Warning

**Category:** Security

**CWE**: [287](https://cwe.mitre.org/data/definitions/287.html)

## Description{% #description %}

This rule flags instances where a connection to an LDAP server is attempted without providing a password. Binding without a password can lead to anonymous access, which may expose sensitive directory information or allow unauthorized modifications.

To comply with this rule, always supply a valid password when calling `ldap_bind`. For example, use `ldap_bind($server, $dn, $password);` where `$password` is a non-empty string containing the correct credentials. If anonymous binding is necessary, ensure that it is a conscious decision backed by appropriate safeguards and documented accordingly.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?
ldap_bind($server, $dn, '');
ldap_bind($server, $dn, NULL);
?>
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?
ldap_bind($server, $dn, $password);
?>
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
