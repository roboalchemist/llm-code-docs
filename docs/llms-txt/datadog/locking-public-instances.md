# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/locking-public-instances.md

---
title: Do not lock on  on publicly accessible instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not lock on on publicly accessible instance
---

# Do not lock on on publicly accessible instance

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/locking-public-instances`

**Language:** C#

**Severity:** Warning

**Category:** Performance

## Description{% #description %}

The rule "Do not lock on publicly accessible instance" is a crucial guideline in multithreaded programming in C#. It is designed to prevent potential deadlocks and other synchronization issues that can occur when multiple threads try to acquire a lock on the same publicly accessible object.

Locking on a public object can lead to deadlocks if another thread outside your code also locks on that object. This is because locking on 'this' or other publicly accessible instances exposes your lock to external manipulation and can cause unpredictable behavior.

## How to remediate{% #how-to-remediate %}

To avoid this, always use a private, readonly object to lock on. This practice ensures that the lock is not accessible from outside the class and that its state can't be modified, providing a controlled environment for synchronization. For example, you can create a private, readonly object specifically for locking like so: `private readonly object _lockObject = new object();`. Then, use this object in your `lock` statement: `lock (_lockObject) {...}`. This way, you adhere to encapsulation principles and maintain control over the synchronization process.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
public class SharedResource
{
    public object LockObject = new object();

    public void DoSomething()
    {
        if (something) {
            lock (this)
            {

            }
        }

    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
public class SharedResource
{
    public object LockObject = new object();

    public void DoSomething()
    {
        lock (LockObject)
        {

        }
    }
}
```

```csharp
private readonly object _lockObject = new object();

public void Foo()
{
    lock (_lockObject)
    {
    }
}
```

```csharp
class SharedResource
{
    public object LockObject = new object();

    public void DoSomething()
    {
        if (something) {
            lock (this)
            {

            }
        }

    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
