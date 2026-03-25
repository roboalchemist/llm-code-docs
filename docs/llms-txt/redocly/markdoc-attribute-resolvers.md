# Source: https://redocly.com/docs/realm/customization/markdoc-attribute-resolvers.md

# Built-in Markdoc attribute resolvers

Custom Markdoc attribute resolvers define special attributes that resolve during build time.
Use this functionality to transform file paths into proper slugs and load file content.

## Available resolvers

The following resolvers are available for use in your Markdoc schema attributes:

- [`link`](/docs/realm/customization/markdoc-attribute-resolvers/link) - Transforms file paths into proper route slugs or static asset URLs.
- [`rawContent`](/docs/realm/customization/markdoc-attribute-resolvers/raw-content) - Loads the raw content of files as strings.