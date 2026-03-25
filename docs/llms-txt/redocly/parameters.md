# Source: https://redocly.com/learn/openapi/openapi-visual-reference/parameters.md

# Named Parameters

> An object to hold reusable [Parameter Objects](/learn/openapi/openapi-visual-reference/parameter).


Declare named parameters in the components object.

> Holds a set of reusable objects for different aspects of the OAS. All objects defined within the components object will have no effect on the API unless they are explicitly referenced from properties outside the components object.



```yaml
components:
  parameters:
    AnyNameYouWant:
      # Parameter Object
    AnotherNameYouWant:
      # Parameter Object
```

## Visuals

See the [Parameter Object](/learn/openapi/openapi-visual-reference/parameter).

## Types

- `NamedParameters` is a map of `Parameter`