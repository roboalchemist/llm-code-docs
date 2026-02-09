# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/atomic-file-operations.md

---
title: Prefer atomic file operations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer atomic file operations
---

# Prefer atomic file operations

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/atomic-file-operations`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule "Prefer atomic file operations" is designed to promote the use of atomic operations when interacting with files or directories. This is important because non-atomic file operations can lead to race conditions, where the state of a file or directory changes between the time you check its state and the time you perform an operation on it. For example, if you check whether a directory exists and then try to create it if it doesn't, another process could create the directory after you check, but before you create it, leading to an error.

In Ruby, you can avoid this problem by using methods from the `FileUtils` module, which provide atomic operations. For example, instead of checking whether a directory exists and then creating it if it doesn't, you can use the `FileUtils.mkdir_p` method, which will create the directory if it doesn't exist, and do nothing if it does.

Non-compliant code often checks for the existence of a file or directory using `File.exist?` or `Dir.exist?` and then performs a file operation. To fix this, replace these checks and operations with equivalent atomic operations. For example, replace `unless Dir.exist?(path); FileUtils.mkdir(path); end` with `FileUtils.mkdir_p(path)`. Similarly, replace `if File.exist?(path); FileUtils.remove(path); end` with `FileUtils.rm_f(path)`. This will ensure that your file operations are atomic, and safe from race conditions.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
# The failing snippets check if a file or directory exists,
# then call a function from FileUtils on that file or directory.
unless Dir.exist?(path)
  FileUtils.mkdir(path)
end

unless not File.exist?(path)
  FileUtils.remove(path)
end

if File.exist?(path)
  FileUtils.remove(path)
end

if !Dir.exist?(path)
  FileUtils.mkdir(path)
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
# Preferred alternative to check-if-exist-then-mkdir
FileUtils.mkdir_p(path)
# Preferred alternative to check-if-exist-then-rm
FileUtils.rm_f(path)

# More than one argument to the operation
if File.exist?(path)
  FileUtils.doSomething(path, arg)
end

# These use different modules or methods
unless Foo.exist?(path)
  FileUtils.mkdir(path)
end

unless Dir.exists?(path)
  FileUtils.mkdir(path)
end

unless Dir.exist?(path)
  FileUtilities.mkdir(path)
end

# These check one thing then operate on another thing
unless Dir.exist?(path)
  FileUtils.mkdir(other_path)
end

# These check one thing then operate on another thing
if File.exist?(path)
  FileUtils.remove(other_path)
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 