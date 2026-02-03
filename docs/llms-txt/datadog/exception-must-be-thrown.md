# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-best-practices/exception-must-be-thrown.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/exception-must-be-thrown.md

---
title: Exceptions must be thrown
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Exceptions must be thrown
---

# Exceptions must be thrown

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/exception-must-be-thrown`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Exceptions should be thrown and not just created. An expression such as `new Exception(...)` does not throw the exception. You should use the keyword `throw` to throw the exception`.

#### Learn More{% #learn-more %}

- [Exceptions in C#](https://learn.microsoft.com/en-us/dotnet/api/system.exception?view=net-8.0)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.Xml;

class MyClass {
    public void myMethod()
    {
        var a = new MyException("something bad happened");
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System.Xml;

class MyClass {
    public void myMethod()
    {
        var bla = new MyClass("something bad happened");
    }
    public void foo() {
            Formatter formatter = language switch
            {
                SqlLanguage.Sql => new StandardSqlFormatter(),
                SqlLanguage.Tsql => new TSqlFormatter(),
                SqlLanguage.Spark => new SparkSqlFormatter(),
                SqlLanguage.RedShift => new RedshiftFormatter(),
                SqlLanguage.PostgreSql => new PostgreSqlFormatter(),
                SqlLanguage.PlSql => new PlSqlFormatter(),
                SqlLanguage.N1ql => new N1qlFormatter(),
                SqlLanguage.MySql => new MySqlFormatter(),
                SqlLanguage.MariaDb => new MariaDbFormatter(),
                SqlLanguage.Db2 => new Db2Formatter(),
                _ => throw new NotSupportedException(),
            };
    }
}
```

```csharp
using System.Xml;

class MyClass {
    public void myMethod()
    {
        throw new MyException("something bad happened");
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 