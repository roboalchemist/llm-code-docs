# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-node-security/sql-injection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-security/sql-injection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/sql-injection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/sql-injection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-security/sql-injection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-node-security/sql-injection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/sql-injection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/sql-injection.md

---
title: Prevent SQL queries built from strings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent SQL queries built from strings
---

# Prevent SQL queries built from strings

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/sql-injection`

**Language:** C#

**Severity:** Error

**Category:** Security

**CWE**: [89](https://cwe.mitre.org/data/definitions/89.html)

## Description{% #description %}

Never build SQL queries manually. Always have the query built with parameters and then pass the parameters to the prepared statement.

#### Learn More{% #learn-more %}

- [CWE-89: Improper Neutralization of Special Elements used in an SQL](https://cwe.mitre.org/data/definitions/89.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.Xml;

class MyClass {
    public static void doQuery(Int32 userId)
    {
        using (SqlConnection connection = new SqlConnection(connectionString))
        {
                var sql = $"SELECT Id, Username, Email, IsAdmin FROM Users WHERE Username LIKE '%{name}%'";
                
        }
    }
}
```

```csharp
using System.Xml;

class MyClass {
    public static void doQuery(Int32 userId)
    {
        using (SqlConnection connection = new SqlConnection(connectionString))
        {
            SqlCommand command = new SqlCommand("SELECT attr FROM table WHERE id=" + userID, connection);
        }
    }
}
```

```csharp
using System.Xml;

class MyClass {
    public static void goQuery(Int32 userID)
    {
        String query1 = "SELECT attr FROM table WHERE id=" + userID;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System.Xml;

class MyClass {
    public static void doQuery(Int32 userID)
    {
        using (SqlConnection connection = new SqlConnection(connectionString))
        {
            SqlCommand command = new SqlCommand("SELECT attr FROM table WHERE id=@ID", connection);
            command.Parameters.Add("@ID", SqlDbType.Int);
            command.Parameters["@ID"].Value = userID;
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 