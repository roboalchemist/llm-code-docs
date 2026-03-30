# Source: https://redocly.com/learn/openapi/openapi-visual-reference/examples.md

# Named examples

You can name examples in the components object.


```yaml
components:
  examples:
    lightning:
      # Example object
```

It is a map with strings as the name, and the [Example Object](/learn/openapi/openapi-visual-reference/example) as the value.

## Visuals

See the [Example Object](/learn/openapi/openapi-visual-reference/example).

## Types

- NamedExamples
- Example



```ts
  NamedExamples: mapOf('Example'),
```