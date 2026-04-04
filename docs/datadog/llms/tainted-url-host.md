# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/tainted-url-host.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/tainted-url-host.md

---
title: Prevent SSRF
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent SSRF
---

# Prevent SSRF

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/tainted-url-host`

**Language:** Java

**Severity:** Error

**Category:** Security

**CWE**: [918](https://cwe.mitre.org/data/definitions/918.html)

## Description{% #description %}

No description found

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
@RequestMapping("/redirect")
public void redirect(@RequestParam() String url, String a) throws MalformedURLException {
    URL newUrl = new URL(url);  // Bad: User-controlled input used directly
    URL newUrl = new URL(url + "/path");
}

@RequestMapping("/api")
public void apiEndpoint(@RequestParam String host) {
    String url1 = "http://" + host + "/api/resource";  // Bad: User input concatenated into URL

    String url2 = "http://".concat(host);

    String url3 = "https://";
    url3 += host;

    String url4 = String.format("https://%v", host);

    String url5 = "https://%v";

    String url6 = String.format(url5, host)
}

@RequestMapping("/fetch")
public void fetchData(@RequestParam String endpoint) {
    StringBuilder sb = new StringBuilder("https://example.com");
    sb.append(endpoint);  // Bad: User input appended to base URL
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
@RequestMapping("/safe-redirect")
public void safeRedirect(@RequestParam String path) throws MalformedURLException {
    String baseUrl = "https://safe.example.com";
    URL newUrl = new URL(baseUrl + URLEncoder.encode(path, "UTF-8"));  // Good: User input only affects the path, not the host
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
