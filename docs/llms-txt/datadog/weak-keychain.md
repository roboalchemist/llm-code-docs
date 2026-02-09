# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-security/weak-keychain.md

---
title: Weak keychain, allowing an attacker to get secret data
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Weak keychain, allowing an attacker to get secret data
---

# Weak keychain, allowing an attacker to get secret data

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-security/weak-keychain`

**Language:** Swift

**Severity:** Warning

**Category:** Security

**CWE**: [522](https://cwe.mitre.org/data/definitions/522.html)

## Description{% #description %}

This rule detects the use of weak keychain accessibility settings that can expose sensitive data to attackers. Using overly permissive accessibility constants like `kSecAttrAccessibleAlways` or `kSecAttrAccessibleAlwaysThisDeviceOnly` allows keychain items to be accessed even when the device is locked or without user authentication, increasing the risk of unauthorized data retrieval.

It is important to protect secret data stored in the keychain by limiting access to when the device is unlocked and ensuring the highest possible security level. Weak accessibility settings can undermine the security guarantees that the keychain provides, making sensitive information vulnerable to compromise if the device is lost or stolen.

To comply with this rule, developers should use strong accessibility constants such as `kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly` or `kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly`. These settings enforce stricter access controls, requiring the device to be unlocked or a passcode to be set before keychain items can be accessed. For example, use `kSecAttrAccessible: kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly` when adding or updating keychain items to ensure robust protection.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
class keychainController: keychainViewController {
    func test() {
        let token = "secret"
        var query = [String : AnyObject]()
        query[kSecClass as String] = kSecClassGenericPassword
        query[kSecValueData as String] = token as AnyObject?
        query[kSecAttrAccessible as String] = kSecAttrAccessibleAlwaysThisDeviceOnly
        SecItemAdd(query as CFDictionary, nil)
    }   
}
```

```swift
class keychainController: keychainViewController {
    func foo3() {
        let token = "secret"
        var query = [String : AnyObject]()
        query[kSecClass as String] = kSecClassGenericPassword
        query[kSecValueData as String] = token as AnyObject?
        query[kSecAttrAccessible as String] = kSecAttrAccessibleAlways
        SecItemAdd(query as CFDictionary, nil)
    }
}
```

```swift
class keychainController: keychainViewController {


    
    func test() {
        var query: [String: Any] = [kSecClass as String: kSecClassInternetPassword,
                                    kSecAttrAccount as String: account,
                                    kSecAttrServer as String: server,
                                    kSecValueData as String: password,
                                    kSecAttrAccessible as String: kSecAttrAccessibleAlways]
        SecItemAdd(query,r)
    }
    
    
       
}
```

```swift
class keychainController: keychainViewController {
    func test() {
        let keychainItemQuery = [
            kSecValueData: "test123".data(using: .utf8)!,
            kSecClass: kSecClassGenericPassword,
            kSecAttrAccessible: kSecAttrAccessibleAlwaysThisDeviceOnly
        ] as CFDictionary

        let status = SecItemAdd(keychainItemQuery, nil)
        print("Operation finished with status: \(status)")
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
class keychainController: keychainViewController {
    func test() {
        let keychainItemQuery = [
            kSecValueData: "test123".data(using: .utf8)!,
            kSecClass: kSecClassGenericPassword
        ] as CFDictionary

        let status = SecItemAdd(keychainItemQuery, nil)
        print("Operation finished with status: \(status)")
    } 
}
```

```swift
class keychainController: keychainViewController {
    func test() {
        // ok: good keychain
        let keychainItemQuery = [
            kSecValueData: "test123".data(using: .utf8)!,
            kSecClass: kSecClassGenericPassword,
            kSecAttrAccessible: kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly
        ] as CFDictionary
        
        let status = SecItemAdd(keychainItemQuery, nil)
        print("Operation finished with status: \(status)")
    }
}
```

```swift
class keychainController: keychainViewController {
    func foo7(_ data: Data, forKey key: String) {
        let query: [NSString: Any] = [
            kSecClass: secClass,
            kSecAttrAccount: key,
            kSecAttrAccessGroup: accessGroup
        ]
        let attributes: [NSString: Any] = [
            kSecValueData: data,
            kSecAttrAccessible: kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly
        ] 
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 