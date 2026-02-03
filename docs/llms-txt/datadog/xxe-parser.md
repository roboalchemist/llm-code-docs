# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-security/xxe-parser.md

---
title: Parser should not resolve external entiries
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Parser should not resolve external entiries
---

# Parser should not resolve external entiries

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `swift-security/xxe-parser`

**Language:** Swift

**Severity:** Warning

**Category:** Security

**CWE**: [611](https://cwe.mitre.org/data/definitions/611.html)

## Description{% #description %}

This rule ensures that XML parsers do not resolve external entities during parsing. Resolving external entities can expose applications to XML External Entity (XXE) attacks, where malicious XML input can access sensitive files, cause denial of service, or execute remote requests. Preventing the resolution of external entities helps protect the application from these security vulnerabilities.

It is important to disable the `shouldResolveExternalEntities` property on XML parser instances or leave it unset, as it defaults to `false` in most implementations. This reduces the attack surface by preventing the parser from fetching or processing external resources referenced in the XML content. Developers should explicitly set `parser.shouldResolveExternalEntities = false` or avoid enabling it unless absolutely necessary.

To comply with this rule, ensure your XML parsing code does not enable external entity resolution. For example, write `parser.shouldResolveExternalEntities = false` or omit this property entirely since it is disabled by default. Always validate and sanitize XML input and prefer safer parsing configurations to avoid introducing security risks related to external entities.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```swift
class XXEViewController: ViewController {


    func test(xml: String) {
        parser = NSXMLParser(data: rawXml.dataUsingEncoding(NSUTF8StringEncoding)!)
        parser.delegate = self
        parser.shouldResolveExternalEntities = true
        parser.parse()
    }
    
}
```

```swift
class XXEViewController: ViewController {
    func test() {
        var success: Bool
        var rawXmlConvToData: NSData = rawXml.data(using: NSUTF8StringEncoding)
        var myParser: XMLParser = NSXMLParser(data: rawXmlConvToData)
        myParser.shouldResolveExternalEntities = true
        myParser.delegate = self
        myParser.parse()
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```swift
class XXEViewController: ViewController {
    func test(xml: String) {
        parser = NSXMLParser(data: rawXml.dataUsingEncoding(NSUTF8StringEncoding)!)
        parser.delegate = self
        // ok: good xxe (external entities resolution disabled by default)
        parser.parse()
    }
}
```

```swift
class XXEViewController: ViewController {

    func test(xml: String) {
        parser = NSXMLParser(data: rawXml.dataUsingEncoding(NSUTF8StringEncoding)!)
        parser.delegate = self
        parser.shouldResolveExternalEntities = false
        parser.parse()
    }
    
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 