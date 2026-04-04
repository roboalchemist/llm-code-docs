# Source: https://redocly.com/docs/realm/content/markdoc-functions.md

# Markdoc functions

Markdoc functions add powerful capabilities to your Markdown content, enabling conditional logic and data manipulation.

Functions are typically used in two main ways:

1. **Conditional rendering:** Inside `{% if %}` tags to control whether a block of content is displayed based on variable values or other conditions.
2. **Direct output:** Within `{% ... %}` delimiters to directly output a computed value into the content.


## Call functions

Call functions using a syntax similar to programming languages:

`{% functionName(argument1, argument2, ...) %}`

Arguments can be literal values (strings, numbers, booleans), variables (like `$frontmatter.seo.title` or `$rbac.teams`), or results of other functions.

## Resources

- **[Built-in functions overview](/docs/realm/content/markdoc-functions/built-in)** - Explore standard Markdoc functions available for content manipulation and dynamic value generation
- **[Build custom Markdoc functions](/docs/realm/customization/build-custom-function)** - Learn to define and integrate your own custom functions for advanced content processing and dynamic features