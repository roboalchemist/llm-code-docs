# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-code-style/method-parens.md

---
title: Avoid parentheses for methods without arguments
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid parentheses for methods without arguments
---

# Avoid parentheses for methods without arguments

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-code-style/method-parens`

**Language:** Ruby

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

In Ruby, parentheses are not required when defining methods without arguments. The rule "Avoid parentheses for methods without arguments" encourages this practice, making the code cleaner and more readable.

This rule is crucial because it promotes consistency and clarity in your code. Ruby is known for its elegant and human-readable syntax, and following this rule maintains that reputation. Using parentheses for methods without arguments can cause unnecessary confusion and clutter in your code.

To adhere to this rule, omit parentheses when defining methods without arguments. For instance, instead of `def method()`, use `def method`. For methods with arguments, continue using parentheses to separate the method name from its arguments, like `def method(arg1, arg2)`. Following this rule will make your Ruby code cleaner and easier to read.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
def emptyparens()
end

def noparensargs arg1, arg2
end

def singleton.emptyparens()
end

def singleton.noparensargs arg1, arg2
end

module Mod
    def modemptyparens()
    end

    def modnoparensargs arg1, arg2
    end
end

class Clz
    def clzemptyparens()
    end

    def clznoparensargs arg1, arg2
    end
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
def noparens
end

def parensargs(arg1, arg2)
end

def single.noparens
end

def single.parensargs(arg1, arg2)
end

module Mod
    def modnoparens
    end

    def modparensargs(arg1, arg2)
    end
end

class Clz
    def clznoparens
    end

    def clzparensargs(arg1, arg2)
    end
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 