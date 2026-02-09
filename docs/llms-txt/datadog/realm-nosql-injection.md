# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-security/realm-nosql-injection.md

---
title: Potential NoSQL injection in Realm query
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Potential NoSQL injection in Realm query
---

# Potential NoSQL injection in Realm query

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-security/realm-nosql-injection`

**Language:** Swift

**Severity:** Error

**Category:** Security

**CWE**: [943](https://cwe.mitre.org/data/definitions/943.html)

## Description{% #description %}

This rule detects potential NoSQL injection vulnerabilities in iOS applications using the Realm database. The vulnerability occurs when a Realm query predicate is constructed by concatenating a static string with untrusted user input.

An attacker could provide specially crafted input that alters the logic of the NoSQL query. A successful exploit could allow the attacker to bypass authentication, access or modify sensitive data, or disrupt the application's functionality.

To remediate this, avoid building queries using string concatenation. Instead, use parameterized queries with `NSPredicate`, which safely separates the query logic from user-provided values. For example, use `NSPredicate(format: "name = %@", userInput)` instead of `"name = '\(userInput)'"`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
import RealmSwift

class User: Object {
    @objc dynamic var username = ""
    @objc dynamic var isAdmin = false
}

func findUser(username: String) {
    let realm = try! Realm()
    
    // --- NON-COMPLIANT ---
    // The query predicate is built by concatenating a string with user input
    // *directly inside the filter call*. This pattern is detected by the rule.
    let results = realm.objects(User.self).filter("username = '" + username + "'")

    print("Found \(results.count) users.")
}

// Example usage
findUser(username: "guest' OR isAdmin = true")
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
import Foundation
import RealmSwift

class User: Object {
    @objc dynamic var username = ""
    @objc dynamic var isAdmin = false
}

func findUserSafely(username: String) {
    let realm = try! Realm()

    // --- COMPLIANT ---
    // The query uses NSPredicate, which safely handles user input.
    // There is no `additive_expression` here for the rule to find.
    let safePredicate = NSPredicate(format: "username = %@", username)
    let results = realm.objects(User.self).filter(safePredicate)

    print("Found \(results.count) users.")
}

// Example usage
findUserSafely(username: "guest' OR isAdmin = true")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 