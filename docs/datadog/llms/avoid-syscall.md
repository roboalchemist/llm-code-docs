# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/avoid-syscall.md

---
title: Avoid syscall
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid syscall
---

# Avoid syscall

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/avoid-syscall`

**Language:** Ruby

**Severity:** Info

**Category:** Security

**CWE**: [94](https://cwe.mitre.org/data/definitions/94.html)

## Description{% #description %}

The `syscall` function is a direct interface to the operating system's system calls. This rule is important because using `syscall` can lead to non-portable and difficult to maintain code. Different operating systems have different system calls and different numbers assigned to them. Therefore, the code that uses `syscall` may behave differently on different systems, which can lead to unexpected results and bugs that are hard to track down.

Furthermore, `syscall` is considered to be a low-level interface, which should be avoided in high-level programming languages like Ruby. It bypasses the abstractions that Ruby provides, which can lead to less readable and more error-prone code.

Instead of using `syscall`, use the abstractions that Ruby provides. For example, if you want to write to a file, use Ruby's File class, which provides a high-level, portable interface for file operations. This way, you can ensure that your code is portable and easier to maintain. For instance, you can replace the `syscall` function in the non-compliant code with `File.write('filename', 'hello\n')`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
# See https://ruby-doc.org/core-2.4.1/Kernel.html
syscall 4, 1, "hello\n", 6   # '4' is write(2) on our box
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
