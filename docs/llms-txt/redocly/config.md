# Source: https://redocly.com/docs/redoc/v3.x/config.md

# Source: https://redocly.com/docs/redoc/config.md

# Source: https://redocly.com/docs/realm/config.md

# Configure Redocly

The `redocly.yaml` file is the single place to configure everything Redocly.
This configuration file allows you to customize your API documentation, developer projects, and other Redocly services according to your needs.

This guide provides a comprehensive overview of available configuration options organized by functional areas.

API Management
Navigation elements
User interface
Content management
Security and access management
Customization
Analytics and SEO
Developer experience
## Example configuration

The following example demonstrates a typical `redocly.yaml` configuration combining various options:


```yaml
logo:
  srcSet: './images/redocly-logo.svg light, ./images/redocly-logo-inverted.svg dark'
  altText: Redocly logo
  link: '/'
navbar:
  items:
    - page: index.md
      label: '{{ process.env.HOME_LABEL }}' 
    - page: config/index.md
      label: Config
feedback:
  type: sentiment
  settings:
    comment:
      likeLabel: What was most helpful?
      dislikeLabel: What can we improve?

apis:
  redocly-museum:
    root: './openapi-files/redocly-museum.yaml'

extends:
  - recommended

rules:
  info-license: error
  no-ambiguous-paths: error
  no-http-verbs-in-paths:
    severity: error
    splitIntoWords: true
  rule/operationId-casing:
    subject:
      type: Operation
      property: operationId
    assertions:
      casing: camelCase
  rule/no-description-start-with-the-a-an:
    subject:
      type: any
      property: description
    assertions:
      notPattern: /^(The\s|A\s|An\s)/

rbac:
  content:
    '**'
      authenticated: read

redirects:
  '/concepts/categories/':
    to: 'author/concepts/categories/'
  '/concepts/navigation/':
    to: 'author/concepts/navigation/'
```

This example includes logo customization, navigation setup, feedback controls, API descriptions, rule configurations, access controls, and redirects.

## Configuration principles

Redocly has a few important configuration philosophies:

- universal config (all configuration in one place)
- zero config (you don't need to do any configuration because we have sane defaults)
- config-as-code (all configuration should be writable in a simple source-control friendly format)


Some options have multiple levels of nesting.
Pay attention to the indentation and nesting when modifying the file.

## Next steps

After configuring your `redocly.yaml` file, you can validate it using the Redocly CLI with `npx @redocly/cli check-config`.
For more detailed information about specific configuration options, follow the links in each section.