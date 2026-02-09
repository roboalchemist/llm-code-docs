# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-security/trustkit-pinning.md

---
title: Flag insecure TrustKit certificate pinning settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Flag insecure TrustKit certificate pinning settings
---

# Flag insecure TrustKit certificate pinning settings

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-security/trustkit-pinning`

**Language:** Swift

**Severity:** Error

**Category:** Security

**CWE**: [295](https://cwe.mitre.org/data/definitions/295.html)

## Description{% #description %}

This rule detects improper or disabled certificate pinning when using TrustKit in iOS applications. Without strict pinning, attackers could intercept and manipulate network traffic through Man-in-the-Middle (MitM) attacks, compromising confidentiality and integrity of user data. To mitigate this, applications should enforce proper certificate pinning configurations in line with Apple guidelines.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
import Foundation
import TrustKit

// --- NON-COMPLIANT EXAMPLE 1: Pinning is not enforced ---

// ruleid: trustkit_pinning_enforce_disabled
let trustKitConfigEnforceDisabled: [String: Any] = [
    kTSKPinnedDomains: [
        "www.datatheorem.com": [
            kTSKEnforcePinning: false, // VULNERABILITY: Pinning is explicitly disabled.
            kTSKIncludeSubdomains: true,
            kTSKPublicKeyHashes: [
                "someHash1",
                "someHash2"
            ]
        ]
    ]
]

TrustKit.init(configuration: trustKitConfigEnforceDisabled)


// --- NON-COMPLIANT EXAMPLE 2: Subdomain pinning is disabled ---

// ruleid: trustkit_pinning_subdomain_disabled
let trustKitConfigSubdomainDisabled: [String: Any] = [
    kTSKPinnedDomains: [
        "example.com": [
            kTSKEnforcePinning: true,
            kTSKIncludeSubdomains: false, // VULNERABILITY: Subdomains are not pinned.
            kTSKPublicKeyHashes: [
                "anotherHash1",
                "anotherHash2"
            ]
        ]
    ]
]

TrustKit.init(configuration: trustKitConfigSubdomainDisabled)
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
import Foundation
import TrustKit

// This file demonstrates the SECURE and COMPLIANT way to configure TrustKit.

// Define the TrustKit configuration dictionary.
let trustKitConfig: [String: Any] = [
    kTSKPinnedDomains: [
        "www.datatheorem.com": [
            // COMPLIANT: Pinning is explicitly enforced. This is the most critical setting
            // to prevent MitM attacks.
            kTSKEnforcePinning: true,
            
            // COMPLIANT: Pinning is also enforced for all subdomains, ensuring
            // comprehensive security coverage for the entire domain.
            kTSKIncludeSubdomains: true,
            
            // Provide the valid Base64-encoded SHA-256 hashes of the public keys.
            kTSKPublicKeyHashes: [
                "khh4hgtv9b0z6yioj2l8f9d6h3j3b2b1j6g6f8d3d2c2b1a0", // Primary key
                "jhh5igtv9b0z6yioj2l8f9d6h3j3b2b1j6g6f8d3d2c2b1a1"  // Backup key
            ],
        ]
    ]
]

// Initialize TrustKit with the secure configuration.
// This should be done early in the app's lifecycle, e.g., in AppDelegate.
TrustKit.init(configuration: trustKitConfig)

print("TrustKit has been initialized with a SECURE pinning configuration.")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 