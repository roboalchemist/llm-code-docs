# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-security/exportable-keychain.md

---
title: Prevent export of sensitive data
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent export of sensitive data
---

# Prevent export of sensitive data

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-security/exportable-keychain`

**Language:** Swift

**Severity:** Notice

**Category:** Security

**CWE**: [320](https://cwe.mitre.org/data/definitions/320.html)

## Description{% #description %}

This rule aims to prevent the export of sensitive data by ensuring secure keychain accessibility settings in Swift applications. Exporting sensitive data with improper keychain access attributes, such as `kSecAttrAccessibleAlways` or `kSecAttrAccessibleAfterFirstUnlock`, increases the risk of unauthorized access, especially if the device is compromised or stolen.

To comply with this rule, always set the `kSecAttrAccessible` attribute to a secure value that limits data accessibility to the device only and requires user authentication or passcode protection. For example, use `query[kSecAttrAccessible as String] = kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly` instead of less secure options. This practice minimizes the risk of sensitive data leakage from your app's keychain storage.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
class keychainController: keychainViewController {
    func foo(_ data: Data, forKey key: String) {
        let query: [NSString: Any] = [
            kSecClass: secClass,
            kSecAttrAccount: key,
            kSecAttrAccessGroup: accessGroup
        ]
        let attributes: [NSString: Any] = [
            kSecValueData: data,
            kSecAttrAccessible: kSecAttrAccessibleAfterFirstUnlock
        ]
    }

}
```

```swift
class keychainController: keychainViewController {
    func foo() {
        let keychainItemQuery = [
            kSecValueData: "test123".data(using: .utf8)!,
            kSecClass: kSecClassGenericPassword,
            kSecAttrAccessible: kSecAttrAccessibleAfterFirstUnlock
        ] as CFDictionary
        SecItemAdd(keychainItemQuery, nil)
    }
}
```

```swift
class keychainController: keychainViewController {
    func foo() {
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
    func foo() {
        var query = [String : AnyObject]()
        query[kSecAttrAccessible as String] = kSecAttrAccessibleAlways
        SecItemAdd(query as CFDictionary, nil)
    }
}
```

```swift
class keychainController: keychainViewController {
    func foo() {
        var query = [String : AnyObject]()
        query[kSecAttrAccessible as String] = kSecAttrAccessibleAlways
        SecItemAdd(query as CFDictionary, nil)
    }


}
```

```swift
class keychainController: keychainViewController {
    func foo() {
        var query = [String : AnyObject]()
        query[kSecAttrAccessible as String] = kSecAttrAccessibleAfterFirstUnlock
        SecItemAdd(query as CFDictionary, nil)
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
class keychainController: keychainViewController {

    func foo(_ data: Data, forKey key: String) {
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

```swift
class keychainController: keychainViewController {
    func foo() {
        var query = [String : AnyObject]()
        query[kSecAttrAccessible as String] = kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly
        SecItemAdd(query as CFDictionary, nil)
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
