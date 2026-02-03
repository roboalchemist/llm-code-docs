# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/xml-parsing-xxe-saxparser.md

---
title: XML parsing vulnerable to XXE for SAX Parsers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > XML parsing vulnerable to XXE for SAX Parsers
---

# XML parsing vulnerable to XXE for SAX Parsers

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/xml-parsing-xxe-saxparser`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [611](https://cwe.mitre.org/data/definitions/611.html)

## Description{% #description %}

Your code may be vulnerable XML if you process XML from an untrusted source.

Make sure to enable secure processing when you process XML data by setting `XMLConstants.FEATURE_SECURE_PROCESSING` to true.

#### Learn More{% #learn-more %}

- [XML parsing vulnerable to XXE (SAX Parser)](https://find-sec-bugs.github.io/bugs.htm#XXE_SAXPARSER)
- [CWE-611: Improper Restriction of XML External Entity Reference](https://cwe.mitre.org/data/definitions/611.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class MyClass {

    public void test() {
        SAXParser parser = SAXParserFactory.newInstance().newSAXParser();
        parser.parse(inputStream, customHandler);

        SAXParserFactory spf2 = SAXParserFactory.newInstance();
        SAXParser parser = spf2.newSAXParser();
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class MyClass {

    public void test() {
        SAXParserFactory spf = SAXParserFactory.newInstance();
        spf.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);
        SAXParser parser = spf.newSAXParser();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 