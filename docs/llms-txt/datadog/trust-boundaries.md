# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/trust-boundaries.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/trust-boundaries.md

---
title: Enforce trust boundaries
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce trust boundaries
---

# Enforce trust boundaries

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/trust-boundaries`

**Language:** C#

**Severity:** Error

**Category:** Security

**CWE**: [501](https://cwe.mitre.org/data/definitions/501.html)

## Description{% #description %}

The 'Enforce trust boundaries' rule is crucial in maintaining the security and integrity of your application. This rule is designed to prevent unauthorized access or manipulation of sensitive data by ensuring that trust boundaries are properly implemented and respected. Trust boundaries are interfaces where data is exchanged between components with different levels of trust.

Violations of this rule can lead to serious security issues such as data breaches, unauthorized access to sensitive data, and other forms of security compromise. In the non-compliant code sample, the user's input is directly stored into the session without any form of validation or sanitization, which could lead to Cross-Site Scripting (XSS) or SQL Injection attacks if the input data is used in a context that interprets it as code.

## How to remediate{% #how-to-remediate %}

Validate and sanitize all inputs, especially those that cross trust boundaries. This could be achieved by using functions that ensure the input matches expected patterns and by encoding or escaping inputs before using them in a different context. In the compliant code sample, the input data is URL decoded and used in a way that doesn't interpret it as code, which reduces the risk of XSS attacks. Also, the session cookie is set to be secure and has an expiration time, which limits the time window for potential attacks.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc.Filters;
using Microsoft.AspNetCore.Mvc.Controllers;
using System.Linq;
using System;

namespace OwaspBenchmarkTest.Controllers
{
    public class BenchmarkTest00031Controller : Controller
    {
        [HttpGet("/trustbound-00/BenchmarkTest00031")]
        [HttpPost("/trustbound-00/BenchmarkTest00031")]
        public IActionResult Index()
        {
            var param = Request.Query["BenchmarkTest00031"].FirstOrDefault();

            HttpContext.Session.SetString("userid", param);

            return Content("Item: 'userid' with value: '" + Microsoft.Security.Encoder.Encoder.HtmlEncode(param) + "' saved in session.", "text/html;charset=UTF-8");
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using System;
using System.IO;
using System.Net;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Routing;
using Microsoft.AspNetCore.Session;
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Hosting;
using System.Text;

namespace OwaspBenchmarkTest.Controllers
{
    public class BenchmarkTest00097Controller : Controller
    {
        private readonly IHttpContextAccessor _httpContextAccessor;

        public BenchmarkTest00097Controller(IHttpContextAccessor httpContextAccessor)
        {
            _httpContextAccessor = httpContextAccessor;
        }

        [HttpGet("/trustbound-00/BenchmarkTest00097")]
        public IActionResult Get()
        {
            CookieOptions option = new CookieOptions();
            option.Expires = DateTime.Now.AddMinutes(3);
            option.Secure = true;
            string requestURI = _httpContextAccessor.HttpContext.Request.Path.ToString();
            _httpContextAccessor.HttpContext.Response.Cookies.Append("BenchmarkTest00097", "color", option);
            return View();
        }

        [HttpPost("/trustbound-00/BenchmarkTest00097")]
        public IActionResult Post()
        {
            string param = "noCookieValueSupplied";
            if (_httpContextAccessor.HttpContext.Request.Cookies.ContainsKey("BenchmarkTest00097"))
            {
                //Vulnerability is maintained
                param = WebUtility.UrlDecode(_httpContextAccessor.HttpContext.Request.Cookies["BenchmarkTest00097"]);
            }

            string bar;

            int num = 106;

            bar = (7 * 18) + num > 200 ? "This_should_always_happen" : param;

            HttpContext.Session.SetString(bar, "10340");

            return Content("Item: '" + System.Security.SecurityElement.Escape(bar) + "' with value: 10340 saved in session.");
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 