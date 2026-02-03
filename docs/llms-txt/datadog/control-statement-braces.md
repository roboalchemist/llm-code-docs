# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-code-style/control-statement-braces.md

---
title: Enforce using control statement brackets
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce using control statement brackets
---

# Enforce using control statement brackets

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-code-style/control-statement-braces`

**Language:** Java

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Omitting braces `{}` is valid in multiple statements, such as, for loops, if statements, and while loops. However, enforcing the use of control braces throughout your codebase will make the code more consistent and can make it easier to add statements in the future.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Foo {
    int x = 0;

    public void bar() {
        String message;
        if (randomNumber < something)
            message = "foo";
        else
            message = "bar";

        if (randomNumber < something) {
            message = "foo";
        }
        else
            message = "bar";

        if (randomNumber < something)
            message = "foo";
        else {
            message = "bar";
        }
    }
}
```

```java
public class Foo {
    int x = 0;

    public void bar() {
        // while loop - no braces
        while (true)
            x++;

        // for loop - no braces
        for (int i = 0; i < 42; i++)
            x++;

        // if only - no braces
        if (true)
            x++;
        
        // if/else - no braces
        if (true)
            x++;
         else 
            x--;
        
        // do/while - no braces
        do
            i++;
        while (true);
        
        // case - no braces - allowed by default
        switch(i) {
            case (i < 42):
                return "foo";
            default: 
                return "bar";
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Foo {
    List list = new ArrayList();

    public void bar() {
        String message;
        if(list.size() == 0) {
            message = "empty";
        } else if (list.size() == 1) {
            message = "solo";
        } else {
            message = "multiple";
        }
    }
}
```

```java
public class Foo {
    int x = 0;

    public void bar() {
        // while loop - with braces
        while (true) {
            x++;
        }

        // for loop - with braces
        for (int i = 0; i < 42; i++) {
            x++;
        }

        // if only - with braces
        if (true) {
            x++;
        }
            
        // if/else - with braces
        if (true) {
            x++;
        } else {
            x--;
        }
    
        // do/while - with braces
        do {
            i++;
        }
        while (true);
        
        // case - with braces
        switch(i) {
            case (i < 42) {
                return "foo";
            }
            default {
                return "bar"
            }
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 