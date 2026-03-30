# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-security/weak-random.md

---
title: Use of cryptographically weak Pseudo-Random Number Generator
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use of cryptographically weak Pseudo-Random Number Generator
---

# Use of cryptographically weak Pseudo-Random Number Generator

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-security/weak-random`

**Language:** Swift

**Severity:** Error

**Category:** Security

**CWE**: [338](https://cwe.mitre.org/data/definitions/338.html)

## Description{% #description %}

This rule detects the use of random number generators that are not guaranteed to be cryptographically secure. Functions like `arc4random()` and `Int.random()` are suitable for general-purpose tasks like simulations or games, but they do not provide the strong guarantees of unpredictability required for security-sensitive operations.

Using a weak PRNG for cryptographic purposes (such as generating keys, initialization vectors, nonces, or salts) can expose an application to vulnerabilities where an attacker could predict the random values, compromising the security of the system. This corresponds to [CWE-338: Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG)](https://cwe.mitre.org/data/definitions/338.html).

For generating random values for security-sensitive contexts, Apple's Security framework provides the `SecRandomCopyBytes` function, which is the recommended API for obtaining cryptographically secure random data.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
import Foundation

// This function generates a simple numeric "token" for a non-security purpose, like a game ID.
// While fine for that use case, it would be flagged if used for security.
func generateGameSessionID() -> UInt32 {
    // VIOLATION: arc4random_uniform is not a cryptographically secure PRNG.
    return arc4random_uniform(1000000)
}

// This function generates a random integer within a range.
func rollDice() -> Int {
    // VIOLATION: Int.random(in:) is not guaranteed to be cryptographically secure.
    // It is suitable for simulations or games, but not for generating secrets.
    return Int.random(in: 1...6)
}

// This function attempts to generate a random key.
func generateWeakKey() -> String {
    let letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    // VIOLATION: String.randomElement() relies on the default non-secure PRNG.
    let randomChar = letters.randomElement()!
    return "key-\(randomChar)"
}

// Using the legacy C-style random function.
func legacyRandom() -> Int32 {
    // VIOLATION: random() is a weak, predictable PRNG and should not be used.
    return random()
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
import Foundation
import Security // Must import the Security framework

// This function generates a cryptographically secure token of a specified length.
func generateSecureToken(length: Int) -> String? {
    // 1. Create a buffer of the desired size to hold the random bytes.
    var randomBytes = [UInt8](repeating: 0, count: length)

    // 2. Call SecRandomCopyBytes to fill the buffer with cryptographically secure random data.
    // This is the recommended, compliant method.
    let status = SecRandomCopyBytes(kSecRandomDefault, randomBytes.count, &randomBytes)

    // 3. Check if the operation was successful.
    if status == errSecSuccess {
        // 4. Convert the raw bytes into a usable format, like a Base64 encoded string.
        return Data(randomBytes).base64EncodedString()
    } else {
        // Handle the failure case. It is critical to not proceed if secure random data cannot be generated.
        print("Error: Unable to generate secure random bytes. Status: \(status)")
        return nil
    }
}

// Example usage:
// let secureAPIToken = generateSecureToken(length: 32)
// let initializationVector = generateSecureToken(length: 16)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
