# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/annotate-producesresponsetype.md

---
title: API method explicitly documents its type
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > API method explicitly documents its type
---

# API method explicitly documents its type

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/annotate-producesresponsetype`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

This rule ensures that API methods explicitly document their response types using attributes like `ProducesResponseType`. By clearly specifying the type of data returned and the corresponding HTTP status codes, the API becomes more self-descriptive and easier to understand for both developers and automated tools.

Explicitly documenting response types improves API discoverability and helps client code generators produce accurate models. It also enhances maintainability by making the expected outputs of each endpoint clear, reducing ambiguity and potential bugs during integration or testing phases.

To comply with this rule, always annotate your controller methods with `ProducesResponseType` attributes that specify the response type and status code, especially when returning `IActionResult` or similar abstractions. For example, use `[ProducesResponseType(typeof(Customer), StatusCodes.Status200OK)]` alongside other relevant status codes to clearly communicate the possible responses. Alternatively, returning a strongly typed `ActionResult<T>` can also implicitly document the response type.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
public class Foo {
    [HttpGet("{id}")]
    public Task<IActionResult> method(int id)
    {
        var customer = _repository.GetById(id);
        if (customer == null)
            return NotFound();

        return Ok(customer);
    }
}
```

```csharp
public class Foo {
    [HttpGet("{id}")]
    public IActionResult GetCustomer(int id)
    {
        var customer = _repository.GetById(id);
        if (customer == null)
            return NotFound();

        return Ok(customer);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
public class Foo {
    [HttpGet("{id}")]
    [ProducesResponseType(typeof(Customer), StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public Task<IActionResult> GetCustomer(int id)
    {
        var customer = _repository.GetById(id);
        if (customer == null)
            return NotFound();

        return Ok(customer);
    }
}
```

```csharp
public class Foo {
    [HttpGet("{id}")]
    public ActionResult<Customer> GetCustomer(int id)
    {
        var customer = _repository.GetById(id);
        if (customer == null)
            return NotFound();

        return customer; // Automatically infers ProducesResponseType<Customer>(200)
    }
}
```

```csharp
public class Foo {
    [HttpGet("{id}")]
    [ProducesResponseType(typeof(Customer), StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public IActionResult GetCustomer(int id)
    {
        var customer = _repository.GetById(id);
        if (customer == null)
            return NotFound();

        return Ok(customer);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 