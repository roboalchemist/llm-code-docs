# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/file-read.md

---
title: Use helper functions to read files
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use helper functions to read files
---

# Use helper functions to read files

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/file-read`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

This rule emphasizes the usage of helper functions like `File.read` or `File.binread` for reading files in Ruby. Using these functions is a more efficient and safer approach when compared to the traditional method of opening a file, reading its content, and then closing it.

The importance of this rule lies in the fact that it helps prevent common mistakes that can lead to resource leaks. If you use `File.open` without a block, you must remember to close the file manually. Forgetting to do so can leave the file open indefinitely, which is a waste of system resources. In contrast, helper functions like `File.read` and `File.binread` automatically close the file once the content is read, ensuring that resources are properly managed.

To adhere to this rule, always use `File.read` or `File.binread` when you need to read the entire contents of a file. Avoid using `File.open` methods without a block for file reading operations. By following this rule, you will write more efficient, safer, and cleaner code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
File.open(filename, 'rb').read
File.open(filename, 'rb', &:read)
File.open(filename, 'rb') { |f| f.read }
File.open(filename, 'rb') do |f|
  f.read
end
```

```ruby
File.open(filename).read
File.open(filename, &:read)
File.open(filename) { |f| f.read }
File.open(filename) do |f|
  f.read
end
File.open(filename, 'r').read
File.open(filename, 'r', &:read)
File.open(filename, 'r') { |f| f.read }
File.open(filename, 'r') do |f|
  f.read
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
File.binread(filename)
```

```ruby
File.read(filename)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 