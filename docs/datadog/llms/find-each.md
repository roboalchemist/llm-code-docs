# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/rails-best-practices/find-each.md

---
title: Use find_each to iterate over a collection of AR objects
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use find_each to iterate over a collection of AR objects
---

# Use find_each to iterate over a collection of AR objects

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `rails-best-practices/find-each`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule ensures efficient use of memory when dealing with large collections of ActiveRecord (AR) objects. The `each` method loads all the objects at once into memory, which can cause significant performance issues if the collection is large. In contrast, `find_each` loads a batch of records (1000 by default) into memory, processes them, and then loads the next batch, significantly reducing memory usage.

This rule is especially relevant when dealing with large datasets, where the `each` method can lead to 'out of memory' errors.

To adhere to this rule, replace `each` with `find_each` when iterating over collections of ActiveRecord objects. For example, instead of writing `Foo.all.each`, write `Foo.all.find_each`. Similarly, replace `Foo.where('foo > 42').each` with `Foo.where('foo > 42').find_each`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
Foo.all.each do |foo_instance|
  foo_instance.do_awesome_stuff
end

Foo.where('foo > 42').each do |foo_instance|
  foo_instance.party_all_night!
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
Foo.all.find_each do |foo_instance|
  foo_instance.do_awesome_stuff
end

Foo.where('foo > 42').find_each do |foo_instance|
  foo_instance.party_all_night!
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
