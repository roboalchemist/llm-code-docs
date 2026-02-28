# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/apex-code-style/mergeable-if.md

---
title: Encapsulated if should be merged
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Encapsulated if should be merged
---

# Encapsulated if should be merged

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `apex-code-style/mergeable-if`

**Language:** Apex

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

This rule identifies nested if statements that can be simplified by merging their conditions into a single if statement. Encapsulated if statements that do not contain else blocks or additional logic should be combined using logical operators such as `&&` to improve readability and reduce unnecessary code nesting.

To avoid violations of this rule, developers should look for opportunities to merge nested if conditions when there are no else blocks or separate logic involved. For example, instead of writing `if (something) { if (somethingElse) { ... } }`, it is better to write `if (something && somethingElse) { ... }`. This practice helps keep code clean and straightforward.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```
class MyClass {
    public void myFunction(){
        if (something)
        {
            /*
             something
            */
            if (somethingElse)
            {

            }
            /*
             something else
            */
        }
    }
}
```

```
class MyClass {
    public void myFunction(){
        if (something)
        {
            // something
            if (somethingElse)
            {

            }
            // something else
        }
    }
}
```

```
class MyClass {
    public void myFunction(){
        if (something)
        {
            if (somethingElse)
            {

            }
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```
class MyClass {
    public void myFunction(){

        if (something)
        {
            foo = bar;
            if (somethingElse)
            {

            }
        }

    }
}
```

```
class MyClass {
    public void myFunction(){
        if (something)
        {
            if (somethingElse)
            {

            }
            foo = bar;
        }

    }
}
```

```
class MyClass {
    public void myFunction(){
        if (something)
        {
            if (somethingElse)
            {

            } else {

            }
        }
    }
}
```

```
class MyClass {
    public void myFunction(){
        if (something)
        {
            if (somethingElse)
            {

            }
        } else {

        }
    }
}
```

```
class MyClass {
    public void myFunction(){
        if (something && somethingElse)
        {
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
