# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/avoid-autobinding.md

---
title: Unintended property updates expose sensitive data
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Unintended property updates expose sensitive data
---

# Unintended property updates expose sensitive data

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/avoid-autobinding`

**Language:** C#

**Severity:** Warning

**Category:** Security

**CWE**: [915](https://cwe.mitre.org/data/definitions/915.html)

## Description{% #description %}

The product receives input from an upstream component that specifies multiple attributes, properties, or fields that are to be initialized or updated in an object, but it does not properly control which attributes can be modified.

If the object contains attributes that were only intended for internal use, then their unexpected modification could lead to a vulnerability.

This weakness is sometimes known by the language-specific mechanisms that make it possible, such as mass assignment, autobinding, or object injection.

### Learn More{% #learn-more %}

- [CWE-915: Improperly Controlled Modification of Dynamically-Determined Object Attributes](https://cwe.mitre.org/data/definitions/915.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using WebGoatCore.ViewModels;

namespace WebGoatCore.Controllers
{
    [AllowAnonymous]
    [IgnoreAntiforgeryToken]
    public class StatusCodeController : Controller
    {
        public const string NAME = "StatusCode";

        public StatusCodeController()
        {
            mycall = mycall + 1;
            View(mycall));
        }

        [HttpGet, Route(NAME)]
        public IActionResult StatusCodeView([FromQuery] int code, int morecode, [Bind] int some)
        {
            var foo = bar + baz;
            var view = View(StatusCodeViewModel.Create(new ApiResponse(code)));
            view.StatusCode = code;
            return view;
        }


        public OtherStatusCodeController()
        {
            View(mycall));
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using Microsoft.AspNetCore.Authorization;
using WebGoatCore.ViewModels;

namespace WebGoatCore.Controllers
{
    [AllowAnonymous]
    [IgnoreAntiforgeryToken]
    public class StatusCodeController : Controller
    {
        public const string NAME = "StatusCode";

        public StatusCodeController()
        {
            mycall = mycall + 1;
            View(mycall));
        }

        [HttpGet, Route(NAME)]
        public IActionResult StatusCodeView(int code, int morecode, [Bind] int some)
        {
            var view = View(StatusCodeViewModel.Create(new ApiResponse(morecode)));
            view.StatusCode = code;
            return view;
        }


        public OtherStatusCodeController()
        {
            View(mycall));
        }
    }
}
```

```csharp
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using WebGoatCore.ViewModels;

namespace WebGoatCore.Controllers
{
    [AllowAnonymous]
    [IgnoreAntiforgeryToken]
    public class StatusCodeController : Controller
    {
        public const string NAME = "StatusCode";

        public StatusCodeController()
        {
            mycall = mycall + 1;
            View(mycall));
        }

        [HttpGet, Route(NAME)]
        public NotIActionResult StatusCodeView([FromQuery] int code, int morecode, [Bind] int some)
        {
            var view = View(StatusCodeViewModel.Create(new ApiResponse(code)));
            view.StatusCode = code;
            return view;
        }


        public OtherStatusCodeController()
        {
            View(mycall));
        }
    }
}
```

```csharp
using Microsoft.AspNetCore.Authorization;
using WebGoatCore.ViewModels;

namespace WebGoatCore.Controllers
{
    [AllowAnonymous]
    [IgnoreAntiforgeryToken]
    public class StatusCodeController : Controller
    {
        public const string NAME = "StatusCode";

        public StatusCodeController()
        {
            mycall = mycall + 1;
            View(mycall));
        }

        [HttpGet, Route(NAME)]
        public IActionResult StatusCodeView([Bind] int code, int morecode, [Bind] int some)
        {
            var view = View(StatusCodeViewModel.Create(new ApiResponse(morecode)));
            view.StatusCode = code;
            return view;
        }


        public OtherStatusCodeController()
        {
            View(mycall));
        }
    }
}
```

```csharp
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using WebGoatCore.ViewModels;

namespace WebGoatCore.Controllers
{
    [AllowAnonymous]
    [IgnoreAntiforgeryToken]
    public class StatusCodeController : Controller
    {
        public const string NAME = "StatusCode";

        public StatusCodeController()
        {
            mycall = mycall + 1;
            View(mycall));
        }

        [HttpGet, Route(NAME)]
        public IActionResult StatusCodeView([FromQuery] int code, int morecode, [Bind] int some)
        {
            try {
                validateCode(code);
            } catch exception(e) {
                return View(401);
            }
            var view = View(StatusCodeViewModel.Create(new ApiResponse(code)));
            view.StatusCode = code;
            return view;
        }


        public OtherStatusCodeController()
        {
            View(mycall));
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
