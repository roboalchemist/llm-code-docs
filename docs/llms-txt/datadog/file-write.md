# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/file-write.md

---
title: Use helper functions to write files
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use helper functions to write files
---

# Use helper functions to write files

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/file-write`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The rule emphasizes the importance of using helper functions such as `File.write` or `File.binwrite` to write files in Ruby. These helper functions are not only simpler and more readable, but they also handle resource management automatically, reducing the risk of file leaks caused by not closing files properly.

This rule is crucial as it promotes efficient memory usage and cleaner code. By using these helper functions, you're ensuring that your files are closed after being written to, which prevents potential file and memory leaks in your application. This can be particularly important in larger applications, where such leaks could lead to significant performance issues.

To abide by this rule, always prefer `File.write` or `File.binwrite` over `File.open` when writing to a file. These methods open the file, write the content, and then close the file automatically. They also return the number of bytes written, which can be a useful piece of information. The code becomes more concise, more readable, and less prone to file leaks.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
File.open(filename, 'wb').write(content)
File.open(filename, 'wb') { |f| f.write(content) }
File.open(filename, 'wb') do |f|
  f.write(content)
end
```

```ruby
File.open(filename, 'w').write(content)
File.open(filename, 'w') { |f| f.write(content) }
File.open(filename, 'w') do |f|
  f.write(content)
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
File.binwrite(filename, content)
```

```ruby
File.write(filename, content)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 