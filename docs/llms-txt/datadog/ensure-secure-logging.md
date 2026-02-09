# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/ensure-secure-logging.md

---
title: Ensure no sensitive information is being logged
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure no sensitive information is being logged
---

# Ensure no sensitive information is being logged

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/ensure-secure-logging`

**Language:** C#

**Severity:** Error

**Category:** Security

**CWE**: [778](https://cwe.mitre.org/data/definitions/778.html)

## Description{% #description %}

This rule ensures that no sensitive information, such as passwords, personal identifiers, or confidential data, is written to logs. Logging sensitive data can lead to serious security vulnerabilities, including unauthorized access and data leaks, which can compromise user privacy and violate compliance requirements.

It is important to treat logs as potentially accessible by various parties, including developers, administrators, or attackers who gain access to the system. Therefore, sensitive information should never be recorded in logs in plaintext or any identifiable form.

To comply with this rule, developers should carefully review logging statements and avoid including sensitive parameters directly and sanitize information being logged. Log only non-sensitive metadata or sanitized information. For example, rather than logging `password` or full usernames, consider logging the occurrence of an event without sensitive details or use masking and sanitization techniques before logging.

By following these practices, you reduce the risk of sensitive data exposure while still maintaining useful logs for debugging and monitoring application behavior.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

public class AccountController : Controller
{
    private readonly ILogger<AccountController> _logger;

    public AccountController(ILogger<AccountController> logger)
    {
        _logger = logger;
    }

    [HttpPost]
    public IActionResult Login(string username, string password)
    {
        _logger.LogInformation("User {username} attempting to log in", username);

        // authentication logic...
        return Ok();
    }
}
```

```csharp
using System.Web;
using System.Web.Mvc;
using NLog;

public class UserController : Controller
{
    private static readonly Logger _logger = LogManager.GetCurrentClassLogger();
    
    [HttpPost]
    public ActionResult Register(string username)
    {
        if (!string.IsNullOrEmpty(username))
        {
            _logger.Warn("Registration attempt for user: " + username); // Noncompliant
        }
        return View();
    }
}

void main() {}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
public class UserController : Controller
{
    private static readonly Logger _logger = LogManager.GetCurrentClassLogger();
    
    [HttpPost]
    public ActionResult Register(string username)
    {
        if (!string.IsNullOrEmpty(username))
        {
            string sanitized = username.Replace('\n', ' ').Replace('\r', ' ').Replace('\t', ' ');
            _logger.Warn("Registration attempt for user: " + sanitized);
        }
        return View();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 