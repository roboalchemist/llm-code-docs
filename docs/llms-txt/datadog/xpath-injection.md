# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-flask/xpath-injection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/xpath-injection.md

---
title: Detect an XPath input from an HTTP request
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Detect an XPath input from an HTTP request
---

# Detect an XPath input from an HTTP request

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/xpath-injection`

**Language:** C#

**Severity:** Error

**Category:** Security

**CWE**: [643](https://cwe.mitre.org/data/definitions/643.html)

## Description{% #description %}

This rule is designed to detect and prevent potential XPath Injection vulnerabilities in your C# code. XPath Injection is a type of attack where an attacker can manipulate the structure of an XPath query by injecting malicious input. This can lead to unauthorized data access or manipulation in XML databases or documents.

The importance of this rule lies in its ability to safeguard sensitive data and uphold the integrity of your application. If an attacker can control the structure of an XPath query, they could potentially access or manipulate data they should not have access to. This could lead to data breaches or unauthorized changes to your data.

## How to remediate{% #how-to-remediate %}

Avoid constructing XPath queries using string concatenation with user-controlled data. Instead, consider safer alternatives, such as parameterized XPath queries or validating user input before including it in an XPath query. For example, you could use regular expressions to ensure the user input only contains characters you expect. If user input must be included in an XPath query, it should be properly escaped or encoded to prevent the input from being interpreted as XPath syntax.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
// test_noncompliant_xpath.cs
using System;
using System.Xml;
using Microsoft.AspNetCore.Mvc; // For context

public class VulnerableXPathController : Controller
{
    // Noncompliant: Parameters concatenated directly
    [HttpGet]
    public IActionResult Authenticate(string user, string pass)
    {
        XmlDocument doc = new XmlDocument();
        // Assume doc is loaded with some XML data here...
        // doc.Load("users.xml");

        // Vulnerable concatenation
        String expression = "/users/user[@name='" + user + "' and @pass='" + pass + "']";

        // Method call using the concatenated string
        XmlNode userNode = doc.SelectSingleNode(expression); // Violation should be reported here

        return Json(userNode != null);
    }

    // Noncompliant: Only one parameter concatenated
    [HttpGet]
    public IActionResult FindUser(string username)
    {
        XmlDocument doc = new XmlDocument();
        // Assume doc is loaded...

        string query = "//user[@id='" + username + "']/data"; // Vulnerable

        XmlNodeList nodes = doc.SelectNodes(query); // Violation should be reported here

        // Process nodes...
        return Ok();
    }

    // Noncompliant: Concatenation inside the method call
    [HttpGet]
    public IActionResult FindUserDirect(string uid)
    {
         XmlDocument doc = new XmlDocument();
         // Assume doc is loaded...

         var node = doc.SelectSingleNode("/items/item[@uid='" + uid + "']"); // Violation here

         return Json(node != null);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
// test_compliant_xpath.cs
using System;
using System.Xml;
using Microsoft.AspNetCore.Mvc; // For context
using System.Text.RegularExpressions; // For validation example

public class SafeXPathController : Controller
{
    // Compliant: Hardcoded XPath query
    [HttpGet]
    public IActionResult GetAdmins()
    {
        XmlDocument doc = new XmlDocument();
        // Assume doc is loaded...

        // Safe: Query is constant
        String expression = "/users/user[@role='admin']";
        XmlNodeList adminNodes = doc.SelectNodes(expression); // OK

        // Process nodes...
        return Ok();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 