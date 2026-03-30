# Source: https://redocly.com/docs/cli/decorators/info-override.md

# Source: https://redocly.com/docs/cli/v1/decorators/info-override.md

# info-override

Extends the info object with the designated value.

## API design principles

Sometimes developers generate OpenAPI and the info object need to be improved after the fact.
This generally happens when you have no permission to edit the source.
This decorator provides a way to "overlay" a new info section over the source so that as the source changes, the modifications can be reapplied.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| *additionalProperties* | any | **REQUIRED.** Any properties from the OpenAPI info object. |


Example of a configuration:


```yaml
decorators:
  info-override:
    title: Updated title
    x-meta: Custom metadata
```

## Examples

![info-override](https://user-images.githubusercontent.com/3975738/214524591-328377a5-9004-4222-8040-57e49e07604a.png)

## Related decorators

- [info-description-override](/docs/cli/v1/decorators/info-description-override)
- [operation-description-override](/docs/cli/v1/decorators/operation-description-override)
- [tag-description-override](/docs/cli/v1/decorators/tag-description-override)


## Resources

- [Decorator source](https://github.com/Redocly/redocly-cli/blob/main/packages/core/src/decorators/common/info-description-override.ts)
- [Blog post about Overlays](https://redocly.com/blog/openapi-overlays/)