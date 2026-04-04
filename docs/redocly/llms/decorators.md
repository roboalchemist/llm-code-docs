# Source: https://redocly.com/docs/cli/configuration/reference/decorators.md

# Source: https://redocly.com/docs/cli/v1/configuration/reference/decorators.md

# Source: https://redocly.com/docs/realm/config/openapi/decorators.md

# Source: https://redocly.com/docs/cli/decorators.md

# Source: https://redocly.com/docs/cli/v1/decorators.md

# Decorators

Decorators are a way of changing an API description during bundling. This updating during bundling can be useful for the following use cases:

- removing some endpoints from an OpenAPI description before publishing
- updating description fields
- adding extra elements, such as examples, or metadata for other tools to use


To learn how to configure decorators, read more about their [configuration syntax](#decorator-configuration-syntax).

## List of decorators

Some common decorator use cases are already built in to Redocly. Check the list below for the decorators you can use immediately.

### Update descriptions

- [info-description-override](/docs/cli/v1/decorators/info-description-override)
- [info-override](/docs/cli/v1/decorators/info-override)
- [operation-description-override](/docs/cli/v1/decorators/operation-description-override)
- [tag-description-override](/docs/cli/v1/decorators/tag-description-override)


### Change examples

- [media-type-examples-override](/docs/cli/v1/decorators/media-type-examples-override)


### Remove content

- [filter-in](/docs/cli/v1/decorators/filter-in)
- [filter-out](/docs/cli/v1/decorators/filter-out)
- [remove-unused-components](/docs/cli/v1/decorators/remove-unused-components)
- [remove-x-internal](/docs/cli/v1/decorators/remove-x-internal)


Have an idea for a decorator?
We might build it for you and give it to the world.
Open a [GitHub issue](https://github.com/Redocly/redocly-cli/issues) and let us know.

## Decorator configuration syntax

The following example shows how to configure a decorator in the [Redocly configuration file](/docs/cli/v1/configuration).


```yaml
apis:
  main:
    root: ./openapi/openapi.yaml
    decorators:
      decorator-name:
        decorator-option: example-value
decorators:
  decorator-name:
    decorator-option: example-value
```

Optionally, you may specify `severity` as one of decorator options in the configuration. Severity can be set to `error`, `warn` or `off`, similar to how it works with [rules](/docs/cli/v1/rules). When it's specified, any problem reported from the decorator is treated according to the configured severity. Setting `severity: off` disables the decorator altogether. Generally, it's not necessary to specify `severity` for decorator configuration except for troubleshooting purposes.

## Custom decorators

If you don't see the decorator you need, you can create your own decorators using [custom plugins](/docs/cli/v1/custom-plugins/custom-decorators).