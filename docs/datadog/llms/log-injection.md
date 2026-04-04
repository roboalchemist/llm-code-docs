# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-security/log-injection.md

---
title: Untrusted user input is logged without sanitization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Untrusted user input is logged without sanitization
---

# Untrusted user input is logged without sanitization

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-security/log-injection`

**Language:** Swift

**Severity:** Warning

**Category:** Security

**CWE**: [117](https://cwe.mitre.org/data/definitions/117.html)

## Description{% #description %}

The application logs data that appears to originate from an untrusted source, such as a user-editable text field or a web view, without proper neutralization. This can lead to a log injection vulnerability.

An attacker could insert fake log entries, corrupt the log format, or inject malicious content (e.g., stored XSS payloads) that could be executed by a log viewing application. This manipulation can be used to cover tracks, mislead administrators, or attack other systems that consume the logs.

To mitigate this vulnerability, all untrusted input should be validated and sanitized before being written to logs. Specifically, newline characters (`\r`, `\n`) and other control characters should be removed or escaped to prevent log entry forgery.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
import UIKit
import WebKit
import os.log

class UserProfileViewController: UIViewController, WKNavigationDelegate {

    var nicknameField: UITextField!
    var webView: WKWebView!

    func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
        if let url = navigationAction.request.url {
            // --- VULNERABLE ---
            // The 'query' part of a URL can contain malicious input.
            print("Processing navigation action with query: \(url.query ?? "none")")
        }
        decisionHandler(.allow)
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
import UIKit
import WebKit
import os.log

class UserProfileViewController: UIViewController, WKNavigationDelegate {

    var nicknameField: UITextField!
    var webView: WKWebView!

    // A helper function to sanitize strings before logging.
    // It removes characters that could be used to forge log entries.
    private func sanitizeForLogging(_ input: String) -> String {
        return input.replacingOccurrences(of: "\r", with: "")
                    .replacingOccurrences(of: "\n", with: "")
    }

    func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
        if let url = navigationAction.request.url, let query = url.query {
             // --- FIXED ---
            // The query string is sanitized before being logged.
            let sanitizedQuery = sanitizeForLogging(query)
            print("Processing navigation action with sanitized query: \(sanitizedQuery)")
        }
        decisionHandler(.allow)
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
