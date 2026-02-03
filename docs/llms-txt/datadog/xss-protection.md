# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/xss-protection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/xss-protection.md

---
title: Prevent XSS attacks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent XSS attacks
---

# Prevent XSS attacks

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/xss-protection`

**Language:** C#

**Severity:** Error

**Category:** Security

**CWE**: [79](https://cwe.mitre.org/data/definitions/79.html)

## Description{% #description %}

This rule is designed to prevent Cross-Site Scripting (XSS) attacks, which occur when an application includes untrusted data in a new web page without proper validation or escaping. XSS attacks allow attackers to execute scripts in the victim's browser, which can lead to a variety of malicious outcomes such as stealing sensitive data or performing actions on behalf of the user.

The importance of this rule lies in the potential for significant security breaches. XSS attacks can lead to unauthorized access, data theft, and other serious consequences. Therefore, it is crucial to ensure that your C# code is not susceptible to such vulnerabilities.

Good coding practices to avoid XSS attacks include always encoding user input before including it in HTML content, using functions like `HtmlEncoder.Default.Encode` or `HttpUtility.HtmlEncode`. Avoid using methods that might introduce vulnerabilities, such as `Html.Raw` or direct `Response.Write` with user input. Even when the input comes from a seemingly trusted source, it's still a good idea to encode it, as it might contain dangerous payloads that were injected earlier.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using Microsoft.AspNetCore.Mvc;

public class AccountController : Controller
{
    [HttpGet]
    public IActionResult Login(string message)
    {
        string html = $"<html><body><h2>Login Page</h2><p>{message}</p></body></html>";
        return Content(html, "text/html");
    }
}
```

```csharp
using Microsoft.AspNetCore.Mvc;
using System.Web;

namespace VulnerableApp
{
    public class VulnerableController : Controller
    {
        [HttpGet("/profile")]
        public IActionResult ShowProfile(string username)
        {
            // Non-compliant: Unencoded user input in Content
            return Content("<div>Hello, " + username + "</div>", "text/html");
        }
        
        [HttpGet("/comment")]
        public IActionResult ShowComment(string comment)
        {
            // Non-compliant: Html.Raw with user input
            ViewBag.UserComment = Html.Raw(comment);
            return View();
        }
        
        [HttpGet("/search")]
        public IActionResult Search(string query)
        {
            // Non-compliant: Direct Response.Write with user input
            Response.ContentType = "text/html";
            Response.Write("<h2>Search results for: " + query + "</h2>");
            
            return new EmptyResult();
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using Microsoft.AspNetCore.Mvc;
using System.Web;
using System.Text.Encodings.Web;

namespace SecureApp
{
    public class SecureController : Controller
    {
        [HttpGet("/user-profile")]
        public IActionResult ShowUserProfile(string username)
        {
            // Compliant: Using HTML encoding
            return Content("<div>Hello, " + HtmlEncoder.Default.Encode(username) + "</div>", "text/html");
            
            // Also compliant: Using HttpUtility
            // return Content("<div>Hello, " + HttpUtility.HtmlEncode(username) + "</div>", "text/html");
        }
        
        [HttpGet("/welcome")]
        public IActionResult Welcome(string name)
        {
            // Compliant: Static string without user input
            return Content("<h1>Welcome to our site!</h1>", "text/html");
        }
        
        [HttpGet("/product")]
        public IActionResult ShowProduct(int id)
        {
            string productName = GetProductName(id); // From database, not user input
            
            // Compliant: Values from trusted sources
            ViewBag.ProductName = productName;
            return View();
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 