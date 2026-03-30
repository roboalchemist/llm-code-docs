# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/ldap-authenticate-connection.md

---
title: LDAP connections should be authenticated
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > LDAP connections should be authenticated
---

# LDAP connections should be authenticated

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/ldap-authenticate-connection`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [521](https://cwe.mitre.org/data/definitions/521.html)

## Description{% #description %}

Lightweight Directory Access Protocol (LDAP) is a protocol used for accessing and maintaining distributed directory information services over a network. It's often used for user authentication and authorization, among other things.

Unauthenticated LDAP connections can pose a significant security risk. Without proper authentication, sensitive data can be exposed to unauthorized users, and the system could be vulnerable to malicious attacks.

To avoid violating this rule, always provide authentication credentials when binding to an LDAP server using the `ldap_bind()` function in PHP. This function takes three parameters: the LDAP link identifier, the bind RDN (username), and the bind password. Providing the username and password ensures that the LDAP connection is authenticated. So, instead of `ldap_bind($ldap)`, use `ldap_bind($ldap, $username, $password)` to securely connect to the LDAP server.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
$ldap = ldap_connect("ldap.example.com");
$ldapbind = ldap_bind($ldap); // Insecure: no authentication provided
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
$username = "username";
$password = "password";
$ldap = ldap_connect("ldap.example.com");
$ldapbind = ldap_bind($ldap, $username, $password); // Secure: authentication provided
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
