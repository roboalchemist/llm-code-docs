# Source: https://redocly.com/docs/realm/content/api-docs/openapi-extensions/x-display-name.md

# OpenAPI extension: `x-displayName`

Tags are used in Redoc to group API endpoints into logical sets for navigation purposes.
Use `x-displayName` to give your tag a better presentation in the navigation bar on the left.

Adjusting the display name is very useful where the tags are either too long to be readable in the left-hand bar, or where the tag isn't a human-readable string.
Making the improved tag details part of the OpenAPI description means that the information can be used everywhere that the OpenAPI file is used.

## Location

Use the `x-displayName` extension in a Tag declaration.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| x-displayName | string | The text to use when presenting this tag as a navigation item and section header.
Default is to use the tag name. |


## Examples

The following configuration renames the short tag name `finserv` to "Finance Services":


```yaml
tags:
  - name: finserv
    description: Operations for the Finance Services department.
    x-displayName: Finance Services
```

## Resources

- **[x-tagGroups extension](/docs/realm/content/api-docs/openapi-extensions/x-tag-groups)** - Group tags into logical sections for improved navigation structure and organization
- **[x-traitTag extension](/docs/realm/content/api-docs/openapi-extensions/x-trait-tag)** - Mark tags as traits rather than navigation elements for specialized tagging functionality
- **[Show extensions configuration](/docs/realm/config/openapi/show-extensions)** - Control which extensions are included in your API reference documentation for optimal presentation
- **[OpenAPI configuration settings](/docs/realm/config/openapi)** - Complete reference for all available OpenAPI configuration options and customization settings
- **[Supported OpenAPI extensions](/docs/realm/content/api-docs/openapi-extensions)** - Complete list of all OpenAPI extensions supported by Redocly for enhanced API documentation