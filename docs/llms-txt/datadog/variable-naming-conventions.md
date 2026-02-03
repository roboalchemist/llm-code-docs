# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-code-style/variable-naming-conventions.md

---
title: Follow variable naming conventions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Follow variable naming conventions
---

# Follow variable naming conventions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-code-style/variable-naming-conventions`

**Language:** C#

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Variable names should follow the `camelCase` pattern and start with a lowercase letter, except for private and protected fields that should start with `_`.

#### Learn More{% #learn-more %}

- [C# Google Style Guide](https://google.github.io/styleguide/csharp-style.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class My_Class {
    int MyVariable = 10;

    public void foo() {
        int FooBar = 14;
        int BAZ_QUUX = 3;
        DateTimeOffset t1 = TimeZoneInfo.ConvertTime();
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
public class CertificateHelperTests {
    private const string PemCertPublic = "";
}
```

```csharp
class My_Class {
    int _myVariable = 10;
    [TestMethod]
    public void BooleanToIntegerConverterTest()
    {
        var converter = new BooleanToIntegerConverter
        {
            ValueOnTrue = 1,
            ValueOnFalse = 2
        };

        Assert.AreEqual(1, converter.Convert(true, typeof(int), null, null));
        Assert.AreEqual(2, converter.Convert(false, typeof(int), null, null));
    }
}
```

```csharp
class My_Class {
    int myVariable = 10;
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 