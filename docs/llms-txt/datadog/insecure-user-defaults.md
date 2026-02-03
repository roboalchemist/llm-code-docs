# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-security/insecure-user-defaults.md

---
title: Don't use UserDefaults to store sensitive data.
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Don't use UserDefaults to store sensitive data.
---

# Don't use UserDefaults to store sensitive data.

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-security/insecure-user-defaults`

**Language:** Swift

**Severity:** Error

**Category:** Security

**CWE**: [311](https://cwe.mitre.org/data/definitions/311.html)

## Description{% #description %}

This analysis pattern identifies the insecure storage of sensitive data in Swift applications for iOS and macOS. The weakness occurs when `UserDefaults.standard.set()` is used to save information that appears to be a credential, secret, or cryptographic key. A static analysis check can detect this by inspecting calls to this function and examining the key name or the variable being stored for common sensitive-data keywords, such as "password," "api_key," "secret_token," or "private_key."

Storing such information in `UserDefaults` constitutes a significant security vulnerability (CWE-311) because it saves the data in an unencrypted property list (plist) file on the device's filesystem. This file can be easily accessed by an attacker with local access to the device or through other system compromises, leading to sensitive data exposure. To mitigate this risk, applications should leverage the system **Keychain**, which is an encrypted and secure database provided by the operating system specifically for storing secrets.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
UserDefaults.standard.set(passphrase, forKey: "passphrase")
UserDefaults.standard.set(passWord, forKey: "userPassword")
UserDefaults.standard.set("123-456-789", forKey: "apiKey")
UserDefaults.standard.set(apiKey, forKey: "MY_TOKEN")
UserDefaults.standard.set(key, forKey: "cryptoKey")
UserDefaults.standard.set(key, forKey: "clientSecret")
UserDefaults.standard.set(key, forKey: "rsaPrivateKey")
UserDefaults.standard.set(passphrase, forKey: "pass_phrase")
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
UserDefaults.standard.set(username, forKey: "userName")
UserDefaults.standard.set("value", forKey: "key")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 