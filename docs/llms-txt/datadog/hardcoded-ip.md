# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-security/hardcoded-ip.md

---
title: Avoid hardcoding IP addresses
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid hardcoding IP addresses
---

# Avoid hardcoding IP addresses

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-security/hardcoded-ip`

**Language:** Swift

**Severity:** Warning

**Category:** Security

**CWE**: [547](https://cwe.mitre.org/data/definitions/547.html)

## Description{% #description %}

Use environment variables, configuration files, or similar methods to configure the IP address instead of hard-coding it. If confidentiality isn't required, prefer a domain name to allow destination changes without rebuilding the software.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
let dnsServer = "8.8.8.8"
let cdnEndpoint = "2600:9000:2136:3400:15:a631:400:93a1"
struct API {
    static let baseURL = "https://10.1.5.120/data"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
// Test file: pass.swift
// Expected annotations: 0

import Foundation

// Compliant: IP is loaded from a configuration object
let primaryServer = configuration.serverIp

// Exception: IPv4 loopback address for local development
let localServer = "127.0.0.1"

// Exception: IPv4 documentation address from RFC 5737
let testNetServer = "198.51.100.50"

// Exception: IPv6 documentation address from RFC 3849
let ipv6Example = "2001:db8:85a3::8a2e:370:7334"

// A version number that looks like an IP but fails the validation
let appVersion = "Application version 3.1.123.900 is not an IP."
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 