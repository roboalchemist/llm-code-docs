# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-security/avoid-xml-xxe.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/avoid-xml-xxe.md

---
title: Prevent XXE attack from XML parser
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent XXE attack from XML parser
---

# Prevent XXE attack from XML parser

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/avoid-xml-xxe`

**Language:** C#

**Severity:** Warning

**Category:** Security

**CWE**: [611](https://cwe.mitre.org/data/definitions/611.html)

## Description{% #description %}

Enabling processing of external data can lead to XML External Entity (XXE) attacks. To prevent this, disable external processing or make sure the external processing you are using is safe. Note that this vulnerability is important for .NET Framework prior to 4.5.2, latest revision are safe by default.

#### Learn More{% #learn-more %}

- [CWE-611: Improper Restriction of XML External Entity Reference](https://cwe.mitre.org/data/definitions/611.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.Xml;

class MyClass {
    public static void payloadDecode()
    {

        if (foo) {
            var xmlDoc = new XmlDocument();
            xmlDoc.XmlResolver = new XmlUrlResolver();
            xmlDoc.LoadXml(xmlContent);
        }

    }
}
```

```csharp
using System.Xml;

class MyClass {
    public static void payloadDecode()
    {
        var xmlDoc = new XmlDocument();
        xmlDoc.XmlResolver = new XmlUrlResolver();
        xmlDoc.LoadXml(xmlContent);
    }
}
```

```csharp
using System.Xml;

class MyClass {
    public static void payloadDecode()
    {
        XmlDocument parser = new XmlDocument();
        parser.XmlResolver = new XmlUrlResolver();
        parser.LoadXml("myDocument.xml");
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System.Xml;

class MyClass {
    public static void payloadDecode()
    {
        XmlDocument parser = new XmlDocument();
        parser.XmlResolver = null;
        parser.LoadXml("myDocument.xml");
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
