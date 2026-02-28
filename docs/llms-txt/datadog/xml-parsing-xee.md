# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/xml-parsing-xee.md

---
title: XML parsing vulnerable to XEE
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > XML parsing vulnerable to XEE
---

# XML parsing vulnerable to XEE

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/xml-parsing-xee`

**Language:** Java

**Severity:** Notice

**Category:** Security

**CWE**: [611](https://cwe.mitre.org/data/definitions/611.html)

## Description{% #description %}

Systems may be vulnerable to an XML External Entity attack when they process XML from untrusted sources.

#### Learn More{% #learn-more %}

- [CWE-611: Improper Restriction of XML External Entity Reference](https://cwe.mitre.org/data/definitions/611.html)
- [XML parsing vulnerable to XXE (XMLStreamReader)](https://find-sec-bugs.github.io/bugs.htm#XXE_XMLSTREAMREADER)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class TestClass {

    public void parseXML(InputStream input) throws XMLStreamException {

        XMLInputFactory factory = XMLInputFactory.newFactory();
        factory.setProperty("aproperty", false);
        XMLStreamReader reader = factory.createXMLStreamReader(input);
        factory.setProperty("anotherproperty", false);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class TestClass {

    public void parseXML(InputStream input) throws XMLStreamException {

        XMLInputFactory factory = XMLInputFactory.newFactory();
        factory.setProperty("aproperty", false);
        factory.setProperty(XMLInputFactory.SUPPORT_DTD, false);
        factory.setProperty("anotherproperty", false);
        XMLStreamReader reader = factory.createXMLStreamReader(input);
    }
}
```

```java
public class TestClass {

    public void parseXML(InputStream input) throws XMLStreamException {

        XMLInputFactory factory = XMLInputFactory.newFactory();
        factory.setProperty("aproperty", false);
        factory.setProperty(XMLInputFactory.IS_SUPPORTING_EXTERNAL_ENTITIES, false);
        factory.setProperty("anotherproperty", false);
        XMLStreamReader reader = factory.createXMLStreamReader(input);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
