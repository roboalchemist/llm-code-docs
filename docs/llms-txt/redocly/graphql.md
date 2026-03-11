# Source: https://redocly.com/docs/realm/config/graphql.md

# `graphql`

Customize the behavior and appearance of integrated GraphQL documentation.
Requires a GraphQL schema.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| [menu](/docs/realm/config/graphql/menu) | object | Menu options. |
| [info](/docs/realm/config/graphql/info) | [Info object](/docs/realm/config/graphql/info#options) | API metadata including title, description, contact, and license information for the overview page. |
| [samplesMaxInlineArgs](/docs/realm/config/graphql/samples-max-inline-args) | number | Maximum number of inline arguments for samples. |
| [jsonSamplesDepth](/docs/realm/config/graphql/json-samples-depth) | number | Sets the default expand level for JSON payload samples. |
| [fieldExpandLevel](/docs/realm/config/graphql/field-expand-level) | number | Maximum depth of the `Return type` in the middle panel. |
| [feedback](/docs/realm/config/feedback) | [Feedback object](/docs/realm/config/feedback#options) | Hide or customize the type of or text included in the feedback form that displays at the end of each endpoint. |
| [showBuiltInScalars](/docs/realm/config/graphql/show-built-in-scalars) | boolean | Show GraphQL built-in scalar types in the navigation and pages. |
| [showBuiltInDirectives](/docs/realm/config/graphql/show-built-in-directives) | boolean | Show GraphQL built-in directives in the navigation and pages. |


## Resources

- **[GraphQL](https://graphql.org/)** - Official GraphQL specification and documentation for understanding query language fundamentals
- **[Add GraphQL documentation to your project](/docs/realm/content/api-docs/add-graphql-docs)** - Step-by-step guide to adding GraphQL API documentation to your Redocly project