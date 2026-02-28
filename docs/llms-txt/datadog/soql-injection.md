# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/apex-security/soql-injection.md

---
title: Prevent SOQL injection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent SOQL injection
---

# Prevent SOQL injection

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `apex-security/soql-injection`

**Language:** Apex

**Severity:** Warning

**Category:** Security

**CWE**: [89](https://cwe.mitre.org/data/definitions/89.html)

## Description{% #description %}

This rule aims to prevent SOQL injection vulnerabilities in Apex code. SOQL injection occurs when untrusted user input is concatenated directly into dynamic SOQL queries, potentially allowing attackers to manipulate the query and access or modify unauthorized data. This can lead to serious security risks including data leakage or corruption.

To avoid SOQL injection, always sanitize user inputs before incorporating them into dynamic SOQL queries. The recommended approach is to use the `String.escapeSingleQuotes()` method on any string variables that are concatenated into query strings. This method escapes special characters that could alter the intended query structure.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```
public class ApexClass {
    public void method(String foo) {
        Database.query('SELECT Id FROM Account' + foo);
    }
}
```

```
public class ApexClass {
    public void method(String foo) {
        String bar = foo;
        Database.query('SELECT Id FROM Account' + bar);
    }
}
```

```
public class ApexClass {
    public void method(Integer i1, String s1, Integer s2) {
        Database.query('SELECT Id FROM Account' + s1);
    }

}
```

```
public class ApexClass {
    public static List<Person> findPerson(String table, String name) {
        List<Person> results = Database.query(
            'SELECT Id, Name ' +
                'FROM ' + objectName + ' ' +
                'WHERE Name LIKE \'%' + String.escapeSingleQuotes(searchKey)
        );

        return results;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```
public class ApexClass {
    public void method(String bar) {
        String foo = String.escapeSingleQuotes(bar);
        Database.query('SELECT Id FROM Account' + foo);
    }
}
```

```
public class ApexClass {
    public void method(String foo) {
        String bar = foo;
        String baz = String.escapeSingleQuotes(bar);
        Database.query('SELECT Id FROM Account' + baz);
    }
}
```

```
public class ApexClass {
    public void method(Integer arg1, String arg2, Integer arg3) {
        String foobar = String.escapeSingleQuotes(arg2);
        Database.query('SELECT Id FROM Account' + foobar);
    }
}
```

```
public class ApexClass {

    public void method(Integer arg1, String arg2, Integer arg3) {
        String str = arg2;
        String foobar = String.escapeSingleQuotes(str);
        Database.query('SELECT Id FROM Account' + foobar);
    }

}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
