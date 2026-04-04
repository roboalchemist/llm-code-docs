# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-best-practices/loop-with-break.md

---
title: Prefer using Kernel#loop with break for post-loop tests
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer using Kernel#loop with break for post-loop tests
---

# Prefer using Kernel#loop with break for post-loop tests

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-best-practices/loop-with-break`

**Language:** Ruby

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

This rule emphasizes the importance of using `Kernel#loop` with a `break` statement for post-loop tests in Ruby. The `Kernel#loop` with `break` construct is more idiomatic and readable in Ruby than using `begin..end while` or `begin..end until`. It also avoids potential confusion about whether the loop will execute at all if the condition is not met initially.

Good readability and clarity are crucial in programming, especially in large codebases where multiple developers are working. It becomes easier for others to understand and maintain the code when it's written in a more idiomatic way.

To adhere to this rule and improve your coding practices, always use the `Kernel#loop` with a `break` statement when you need to perform post-loop tests. This way, you can increase the readability of your code and make it more Ruby-like. For example, instead of writing `begin..end while`, you can write `loop do..break unless..end`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
require_relative '../../spec_helper'
require_relative 'fixtures/classes'

describe "Thread.list" do
  it "includes the current and main thread" do
    Thread.list.should include(Thread.current)
    Thread.list.should include(Thread.main)
  end

  it "includes threads of non-default thread groups" do
    t = Thread.new { sleep }
    begin
      ThreadGroup.new.add(t)
      Thread.list.should include(t)
    ensure
      t.kill
      t.join
    end
  end

  it "does not include deceased threads" do
    t = Thread.new { 1; }
    t.join
    Thread.list.should_not include(t)
  end

  it "includes waiting threads" do
    q = Queue.new
    t = Thread.new { q.pop }
    begin
      Thread.pass while t.status and t.status != 'sleep'
      Thread.list.should include(t)
    ensure
      q << nil
      t.join
    end
  end

  it "returns instances of Thread and not null or nil values" do
    spawner = Thread.new do
      Array.new(100) do
        Thread.new {}
      end
    end

    begin
      Thread.list.each { |th|
        th.should be_kind_of(Thread)
      }
    end while spawner.alive?

    threads = spawner.value
    threads.each(&:join)
  end
end
```

```ruby
value = -10
begin
  puts value
  value += 1
end while value < 0

value = -10
begin
  puts value
  value += 1
end until value == 0
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
value = -10
loop do
  puts value
  value += 1
  break unless value < 0
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
