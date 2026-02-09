# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-security/avoid-anonymous-ldap.md

---
title: LDAP connections must use explicit user credentials
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > LDAP connections must use explicit user credentials
---

# LDAP connections must use explicit user credentials

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-security/avoid-anonymous-ldap`

**Language:** Kotlin

**Severity:** Warning

**Category:** Security

**CWE**: [287](https://cwe.mitre.org/data/definitions/287.html)

## Description{% #description %}

This rule enforces that LDAP connections in Kotlin applications must utilize explicit user credentials for authentication. LDAP (Lightweight Directory Access Protocol) is a protocol used for accessing and maintaining distributed directory information services over an Internet Protocol (IP) network.

This rule is significant as it helps prevent unauthorized access to sensitive data. If LDAP connections are allowed to proceed without explicit user credentials, it might facilitate anonymous access, which can lead to data breaches or unauthorized modifications.

To comply with this rule, ensure that you are not enabling anonymous access when setting up LDAP connections. Instead, use methods like `setUserDn(username)` and `setPassword(password)` for Spring LDAP or `put(Context.SECURITY_PRINCIPAL, username)` and `put(Context.SECURITY_CREDENTIALS, password)` for Java's JNDI to set explicit user credentials. This authentication process ensures that only authorized users can access the LDAP resources, thereby maintaining the security and integrity of the data.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
import org.springframework.ldap.core.support.LdapContextSource

fun configureLDAP(): LdapContextSource {
    return LdapContextSource().apply {
        setUrl("ldap://localhost:389")
        // Dangerous: Enables anonymous access
        setAnonymousReadOnly(true)
        afterPropertiesSet()
    }
}
```

```kotlin
import javax.naming.Context
import javax.naming.directory.InitialDirContext

fun connectLDAP() {
    val env = Hashtable<String, Any>()
    env.apply {
        put(Context.INITIAL_CONTEXT_FACTORY, "com.sun.jndi.ldap.LdapCtxFactory")
        put(Context.PROVIDER_URL, "ldap://localhost:389")
        // Dangerous: Anonymous bind
        put(Context.SECURITY_AUTHENTICATION, "none")
    }
    env.put(Context.SECURITY_AUTHENTICATION, "none")
    val context = InitialDirContext(env)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
import org.springframework.ldap.core.support.LdapContextSource

fun configureLDAPSecurely(
    username: String,
    password: String
): LdapContextSource {
    return LdapContextSource().apply {
        setUrl("ldap://localhost:389")
        setUserDn(username)
        setPassword(password)
        // Optional: Enable connection pooling for better performance
        setPooled(true)
        afterPropertiesSet()
    }
}
```

```kotlin
import javax.naming.Context
import javax.naming.directory.InitialDirContext

fun connectLDAPSecurely(username: String, password: String) {
    val env = Hashtable<String, Any>()
    env.apply {
        put(Context.INITIAL_CONTEXT_FACTORY, "com.sun.jndi.ldap.LdapCtxFactory")
        put(Context.PROVIDER_URL, "ldap://localhost:389")
        // Secure: Using explicit authentication
        put(Context.SECURITY_AUTHENTICATION, "simple")
        put(Context.SECURITY_PRINCIPAL, username)
        put(Context.SECURITY_CREDENTIALS, password)
    }
    val context = InitialDirContext(env)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 