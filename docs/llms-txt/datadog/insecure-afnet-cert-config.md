# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-security/insecure-afnet-cert-config.md

---
title: Insecure AFNetworking certificate pinning configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Insecure AFNetworking certificate pinning configuration
---

# Insecure AFNetworking certificate pinning configuration

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-security/insecure-afnet-cert-config`

**Language:** Swift

**Severity:** Error

**Category:** Security

**CWE**: [295](https://cwe.mitre.org/data/definitions/295.html)

## Description{% #description %}

The rule detects insecure configurations of AFNetworking's `AFSecurityPolicy` that disable or weaken certificate pinning. Certificate pinning is a critical security mechanism that prevents Man-in-the-Middle (MitM) attacks by ensuring the application only communicates with servers presenting a known, trusted certificate or public key.

This rule flags the following insecure patterns:

- **Use of `AFSecurityPolicy.default()`:** The default policy has certificate pinning disabled.
- **Explicitly disabling pinning:** The policy is initialized with `pinningMode` set to `AFSSLPinningMode.none`.
- **Allowing invalid certificates:** The `allowInvalidCertificates` property is set to `true`, which bypasses certificate chain validation and effectively disables pinning.
- **Disabling domain name validation:** The `validatesDomainName` property is set to `false`, which means the certificate's common name is not checked against the server's domain, weakening security.

An attacker could exploit this vulnerability to intercept and tamper with traffic between the mobile application and its backend servers. It is strongly recommended to enable certificate pinning by setting the `pinningMode` to `AFSSLPinningMode.certificate` or `AFSSLPinningMode.publicKey` and ensuring that certificate validation checks are not disabled.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
import AFNetworking

class NetworkManager {
    func createInsecureSessionWithDefaultPolicy() -> AFHTTPSessionManager {
        let manager = AFHTTPSessionManager()

        // NON-COMPLIANT: The default policy has pinning disabled (AFSSLPinningMode.none).
        // This will be flagged by the rule.
        manager.securityPolicy = AFSecurityPolicy.default()

        return manager
    }

    func createInsecureSessionWithInvalidCerts() -> AFHTTPSessionManager {
        let manager = AFHTTPSessionManager()

        // This policy seems secure at first glance...
        let policy = AFSecurityPolicy(pinningMode: .publicKey)

        // NON-COMPLIANT: ...but setting allowInvalidCertificates to true bypasses all
        // certificate validation, making pinning useless. This will be flagged.
        policy.allowInvalidCertificates = true

        manager.securityPolicy = policy
        return manager
    }

    func createInsecureSessionWithNoDomainValidation() -> AFHTTPSessionManager {
        let manager = AFHTTPSessionManager()

        let policy = AFSecurityPolicy(pinningMode: .publicKey)

        // NON-COMPLIANT: Disabling domain name validation is a security risk,
        // as it allows a certificate for a different domain to be accepted.
        // This will be flagged by the rule.
        policy.validatesDomainName = false

        manager.securityPolicy = policy
        return manager
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
import AFNetworking

class SecureNetworkManager {

    func createSecureSessionManager() -> AFHTTPSessionManager {
        let manager = AFHTTPSessionManager()

        // COMPLIANT: Initialize the policy with a secure pinning mode,
        // such as .publicKey or .certificate.
        let policy = AFSecurityPolicy(pinningMode: .publicKey)

        // COMPLIANT: Ensure that self-signed or otherwise invalid certificates are not allowed.
        // This is the default, but it is good practice to be explicit.
        policy.allowInvalidCertificates = false

        // COMPLIANT: Ensure that the certificate's domain name is validated against the server's domain.
        // This is also the default.
        policy.validatesDomainName = true

        // To complete the implementation, you must provide the public keys or certificates
        // of the servers you want to trust.
        // For example, load certificates from your app's bundle.
        if let certificateData = loadPinnedCertificates() {
            policy.pinnedCertificates = NSSet(array: certificateData) as? Set<Data>
        } else {
            // Handle the error case where certificates could not be loaded.
            // For security, you might want to prevent the manager from being used.
            fatalError("Could not load pinned certificates.")
        }

        manager.securityPolicy = policy

        return manager
    }

    private func loadPinnedCertificates() -> [Data]? {
        var certificates: [Data] = []
        // Assuming you have .cer files (in DER format) in your project bundle.
        if let paths = Bundle.main.paths(forResourcesOfType: "cer", inDirectory: ".") as [String]? {
            for path in paths {
                if let certificateData = NSData(contentsOfFile: path) {
                    certificates.append(certificateData as Data)
                }
            }
        }
        return certificates.isEmpty ? nil : certificates
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
