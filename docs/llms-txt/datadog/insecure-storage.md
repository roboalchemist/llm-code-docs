# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-security/insecure-storage.md

---
title: Insecure storage mechanism used
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Insecure storage mechanism used
---

# Insecure storage mechanism used

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-security/insecure-storage`

**Language:** Swift

**Severity:** Warning

**Category:** Security

**CWE**: [922](https://cwe.mitre.org/data/definitions/922.html)

## Description{% #description %}

This rule identifies the use of insecure storage mechanisms, such as legacy or non-secure archiving APIs, that can expose sensitive data to tampering or unauthorized access. Storing data insecurely can lead to serious security vulnerabilities, including data leaks, integrity issues, and potential exploitation by attackers.

Developers can avoid violations of this rule by adopting secure archiving patterns, for example: `NSKeyedArchiver.archivedData(withRootObject:requiringSecureCoding:)` and `NSKeyedUnarchiver.unarchivedObject(ofClass:from:)`. Where applicable, encrypt archived data before saving it to disk or transmitting it. Following these best practices helps protect user data confidentiality and integrity in Swift applications.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
class SomeController: UIViewController {
    func foo(picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [NSObject : AnyObject]) {
        if let pickedImage = info[UIImagePickerControllerOriginalImage] as? UIImage {
            imageView.contentMode = .ScaleAspectFit
            imageView.image = pickedImage
        }
        NSKeyedArchiver.archivedData(pickedImage!)
        dismissViewControllerAnimated(true, completion: nil)
    }
}
```

```swift
class SomeController: UIViewController {
    func foo(picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [NSObject : AnyObject]) {
        if let pickedImage = info[UIImagePickerControllerOriginalImage] as? UIImage {
            imageView.contentMode = .ScaleAspectFit
            imageView.image = pickedImage
        }
        UIImageWriteToSavedPhotosAlbum(pickedImage!, self, nil, nil)
        dismissViewControllerAnimated(true, completion: nil)
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
import Foundation
import CryptoKit

enum SecureArchive {
    // Archive (secure coding required)
    static func archive<T: NSSecureCoding>(_ value: T) throws -> Data {
        try NSKeyedArchiver.archivedData(withRootObject: value, requiringSecureCoding: true)
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
