# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/xml-parsing-xxe-xpath.md

---
title: XML parsing vulnerable to XXE for XPath
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > XML parsing vulnerable to XXE for XPath
---

# XML parsing vulnerable to XXE for XPath

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/xml-parsing-xxe-xpath`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [611](https://cwe.mitre.org/data/definitions/611.html)

## Description{% #description %}

Your code may be vulnerable XML if you process XML from an untrusted source.

Make sure to enable secure processing when you process XML data by setting `XMLConstants.FEATURE_SECURE_PROCESSING` to true.

#### Learn More{% #learn-more %}

- [XML parsing vulnerable to XXE (XPathExpression)](https://find-sec-bugs.github.io/bugs.htm#XXE_XPATH)
- [CWE-611: Improper Restriction of XML External Entity Reference](https://cwe.mitre.org/data/definitions/611.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class MyClass {

    public void test() {
        DocumentBuilderFactory df = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = df.newDocumentBuilder();

        DocumentBuilder db2 = DocumentBuilderFactory.newInstance().newDocumentBuilder();
    }
    
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class MyClass {

    public void test() {
        DocumentBuilderFactory df = DocumentBuilderFactory.newInstance();
        df.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);
        DocumentBuilder builder = df.newDocumentBuilder();
    }
    
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 