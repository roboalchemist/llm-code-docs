# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/elixir-security/unsafe-functions.md

---
title: A rule against functions that may have vulnerabilities.
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > A rule against functions that may have vulnerabilities.
---

# A rule against functions that may have vulnerabilities.

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `elixir-security/unsafe-functions`

**Language:** Elixir

**Severity:** Error

**Category:** Security

**CWE**: [94](https://cwe.mitre.org/data/definitions/94.html)

## Description{% #description %}

This rule is designed to prevent the execution of unsafe functions that could potentially expose your application to security risks. It specifically targets functions such as `Code.eval_string`, `Code.eval_file`, `Code.eval_quoted`, and `System.shell`, which are known to be potentially dangerous when used improperly. These functions can execute code or shell commands from user inputs, which might introduce vulnerabilities if the input is not properly sanitized.

The importance of this rule lies in its ability to mitigate the risk of code injection attacks. Code injection attacks occur when an attacker is able to insert malicious code into your application, often through unsanitized user inputs. This can lead to a variety of negative outcomes, including data breaches and unauthorized access to system resources.

To adhere to this rule, avoid using these potentially unsafe functions, especially with user inputs. Instead, consider using safer alternatives that do not execute code dynamically. For instance, if you need to perform a set of operations, you can define a map of allowed functions and their corresponding implementations. This way, you can control what operations are allowed and avoid executing arbitrary code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```elixir
# unsafe function eval_file on user_input
file_result = Code.eval_file(user_input)

# nested evals will each have their own error msg, depending on where
# your mouse is hovered.
single_nested = Code.eval_string(Code.eval_file(a))

# unsafe function eval_quoted ran on user_input
quoted_result = Code.eval_quoted(user_input, "1", "2")

# Concatenated results should also raise errors. Here, two errors are raised because of two different variables
concat = Code.eval_string("1 + 2 + #{variable} + 4", "1 + 2 + #{test}")

# We also want to look for shell commands.
shellcmd = System.shell(command)
```

## Compliant Code Examples{% #compliant-code-examples %}

```elixir
# Instead of letting the user eval commands/files, you can specify allowed functions using
# a predefined set of functions with their own error handling.
defmodule SafeREPL do
  @allowed_functions %{
    "add" => fn [a, b] -> a + b end,
    "subtract" => fn [a, b] -> a - b end,
    "multiply" => fn [a, b] -> a * b end,
    "divide" => fn [a, b] ->
      if b == 0, do: "Cannot divide by zero", else: a / b
    end
  }
end

# You can also opt to hard-code in your own values, as long as variables are not passed in.
Code.eval_string("1 + 2")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
