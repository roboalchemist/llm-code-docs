# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/path-injection.md

---
title: Prevent path injection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent path injection
---

# Prevent path injection

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/path-injection`

**Language:** Ruby

**Severity:** Error

**Category:** Security

**CWE**: [22](https://cwe.mitre.org/data/definitions/22.html)

## Description{% #description %}

This rule detects potential path injection vulnerabilities where user-controlled input is used directly in file system paths or command executions. Path injection can allow attackers to manipulate file paths, leading to unauthorized file access, data leakage, or arbitrary command execution.

It is important to prevent path injection to maintain the integrity and security of your application and the underlying system. Without proper validation or sanitization, attackers might craft input that traverses directories, accesses sensitive files, or executes malicious commands.

To avoid path injection, always validate and sanitize user inputs before incorporating them into file paths or system commands. Use safe methods to construct paths, such as whitelisting allowed filenames or directories, and avoid directly interpolating user input into system calls. For example, instead of `File.open("/tmp/#{params[:file]}")`, sanitize the filename first: `filename = sanitize(params[:file])` followed by `File.open("/safe/path/#{filename}")`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
File.open(params[:file])
```

```ruby
filename = params[:file]
File.open(filename)
```

```ruby
File.open("/tmp/#{params[:file]}")
system("ls #{params[:dir]}")
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
File.open("/safe/path/#{sanitize(filename)}")
File.open("/safe/path/params")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 