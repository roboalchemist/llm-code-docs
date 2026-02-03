# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-security/webview-config.md

---
title: Allowing javascript to open windows is dangerous
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Allowing javascript to open windows is dangerous
---

# Allowing javascript to open windows is dangerous

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-security/webview-config`

**Language:** Swift

**Severity:** Error

**Category:** Security

**CWE**: [272](https://cwe.mitre.org/data/definitions/272.html)

## Description{% #description %}

Allowing `WKWebView` to open new windows automatically via `WKPreferences.javaScriptCanOpenWindowsAutomatically = true` violates least-privilege and can enable abusive pop-ups, phishing flows, and other unwanted navigation. Unless there's a clear, justified need, keep this disabled to reduce attack surface and improve user trust. If opening windows is required, gate it behind explicit user gestures and tight navigation policies (e.g., allowlists, `WKNavigationDelegate`) to contain risk.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
let prefs = WKPreferences()
// ruleid: swift-webview-config-allows-js-open-windows
prefs.JavaScriptCanOpenWindowsAutomatically  = true
let config = WKWebViewConfiguration()
config.defaultWebpagePreferences = prefs

WKWebView(frame: .zero, configuration: config)

let prefs2 = WKPreferences()
prefs2.JavaScriptCanOpenWindowsAutomatically  = true
// okid: swift-webview-config-allows-js-open-windows
prefs2.JavaScriptCanOpenWindowsAutomatically  = false
let config = WKWebViewConfiguration()
config.defaultWebpagePreferences = prefs2

WKWebView(frame: .zero, configuration: config)
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
import WebKit

// Create a preferences object for the webview.
let webPreferences = WKPreferences()

// COMPLIANT: Explicitly disable the ability for JavaScript to open windows
// automatically. This prevents pop-ups and other potentially malicious behavior,
// adhering to the principle of least privilege.
webPreferences.javaScriptCanOpenWindowsAutomatically = false

// Create a webview configuration.
let webConfiguration = WKWebViewConfiguration()
webConfiguration.preferences = webPreferences

// Initialize the WKWebView with the secure configuration.
let webView = WKWebView(frame: .zero, configuration: webConfiguration)

print("WKWebView configured securely.")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 