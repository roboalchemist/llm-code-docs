# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-express/path-traversal.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-express/path-traversal.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/path-traversal.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/path-traversal.md

---
title: Avoid path traversal
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid path traversal
---

# Avoid path traversal

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/path-traversal`

**Language:** C#

**Severity:** Error

**Category:** Security

**CWE**: [22](https://cwe.mitre.org/data/definitions/22.html)

## Description{% #description %}

The rule "Avoid path traversal" is crucial to prevent unauthorized file access and potential data breaches in your application. Path traversal vulnerabilities occur when an attacker is able to manipulate a file path used in an operation, typically with '..' sequences, to access files outside of the intended directory. This can lead to sensitive data exposure, unauthorized data modification or even code execution in some cases.

It is important because an attacker could potentially read, write, or delete sensitive files on the server, leading to a serious breach of data security. The severity of a path traversal attack can vary from information disclosure to complete system compromise depending on the system privileges of the application being attacked.

## How to remediate{% #how-to-remediate %}

Never use user input to form a file path, always use constant or server-generated values. If user input must be used in file paths, it should be properly sanitized to remove any '..' sequences or similar path navigation constructs. Also, using a whitelist of acceptable inputs is a strong defensive option. Always adhere to the principle of least privilege when setting access permissions for files and directories.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using System.IO;
using System.Web;
using System.Text;

namespace Controllers
{
    public class VulnerableController : Controller
    {
        private readonly string _rootPath;

        public VulnerableController(string rootPath)
        {
            _rootPath = rootPath;
        }

        [HttpPost("/path-test")]
        public IActionResult Post()
        {
            // Get parameter from cookies
            string param = "defaultValue";
            if (Request.Cookies != null)
            {
                foreach (var cookie in Request.Cookies)
                {
                    if (cookie.Key.Equals("TestCookie"))
                    {
                        param = HttpUtility.UrlDecode(cookie.Value, Encoding.UTF8);
                        break;
                    }
                }
            }

            // Vulnerable: User input directly in Path.Combine
            string fileName = Path.Combine(_rootPath, "files", param);
            
            // Use the unsafe value
            FileStream fs = null;
            try
            {
                fs = new FileStream(fileName, FileMode.Open);
                // Read file...
            }
            catch (Exception e)
            {
                // Handle error...
            }
            finally
            {
                fs?.Close();
            }

            return Ok();
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using System.IO;
using System.Web;
using System.Text;

namespace Controllers
{
    public class SafeController : Controller
    {
        [HttpPost("/path-test")]
        public IActionResult Post()
        {
            // Get parameter from cookies
            string param = "defaultValue";
            if (Request.Cookies != null)
            {
                foreach (var cookie in Request.Cookies)
                {
                    if (cookie.Key.Equals("TestCookie"))
                    {
                        param = HttpUtility.UrlDecode(cookie.Value, Encoding.UTF8);
                        break;
                    }
                }
            }

            // Safe: Uses ternary that always evaluates to a constant
            string filePath = (7 * 18) + 106 > 200 ? "safe_constant_filename" : param;

            string fullPath = Path.Combine(AppContext.BaseDirectory, "test");

            // Use the safe value
            FileStream fs = null;
            try
            {
                string fullPath = Constants.FILES_DIR + filePath;
                fs = new FileStream(fullPath, FileMode.Open);
                // Read file...
            }
            catch (Exception e)
            {
                // Handle error...
            }
            finally
            {
                fs?.Close();
            }

            return Ok();
        }
    }

    public static class Constants
    {
        public static string FILES_DIR = "files/";
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 