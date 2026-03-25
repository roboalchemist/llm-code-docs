# Source: https://redocly.com/docs/realm/content/api-docs/openapi-extensions.md

# OpenAPI extensions

OpenAPI supports [extensions to the specification](https://spec.openapis.org/oas/v3.1.0#specification-extensions).

The list of extensions supported in OpenAPI by Redoc is as follows:

- [x-additionalPropertiesName](/docs/realm/content/api-docs/openapi-extensions/x-additional-properties-name) - Display a field name for an `additionalProperties` description.
- [x-assertionType](/docs/realm/content/api-docs/openapi-extensions/x-assertion-type) - Specify the OAuth Flow assertion type for the operation.
- [x-badges](/docs/realm/content/api-docs/openapi-extensions/x-badges) - Add visible badges as indicators to API operations.
- [x-codeSamples](/docs/realm/content/api-docs/openapi-extensions/x-code-samples) - Provide the code sample to display for an operation.
- [x-displayName](/docs/realm/content/api-docs/openapi-extensions/x-display-name) - Use a human-friendly display name for a tag.
- [x-enumDescriptions](/docs/realm/content/api-docs/openapi-extensions/x-enum-descriptions) - Readable labels for enum values.
- [x-hideReplay](/docs/realm/content/api-docs/openapi-extensions/x-hide-replay) - Disable the Replay for the specific operation.
- [x-keywords](/docs/realm/config/search#apply-curation-to-files) - Promote or exclude description files, operations, or tags in search results for specified keywords.
- [x-mcp](/docs/realm/content/api-docs/openapi-extensions/x-mcp) - Document MCP servers and tools.
- [x-metadata](/docs/realm/content/api-docs/openapi-extensions/x-metadata) - Add custom metadata at the top of the info section.
- [x-rbac](/docs/realm/content/api-docs/openapi-extensions/x-rbac) - Control access to OpenAPI objects.
- [x-traitTag](/docs/realm/content/api-docs/openapi-extensions/x-trait-tag) - Indicate tags that label operations rather than grouping them.
- [x-tagGroups](/docs/realm/content/api-docs/openapi-extensions/x-tag-groups) - Higher-level grouping for tags, used in the sidebar.
- [x-tags](/docs/realm/content/api-docs/openapi-extensions/x-tags) - Add individual schemas to navigation sections alongside operations.
- [x-summary](/docs/realm/content/api-docs/openapi-extensions/x-summary) - Add short summary of the response.
- [x-webhooks](/docs/realm/content/api-docs/openapi-extensions/x-webhooks) - Add webhooks support to older API description (3.0 or earlier).
- [x-usePkce](/docs/realm/content/api-docs/openapi-extensions/x-use-pkce) - Enable Proof Key for Code Exchange (PKCE) for the Oauth2 or OpenID Connect authorization code flow.


Additionally, the following extensions are supported for the older OpenAPI 2.x format:

- [x-examples](/docs/realm/content/api-docs/openapi-extensions/x-examples) - Add custom examples to a request (make OpenAPI 3 `example(s)` keywords available)
- [x-nullable](/docs/realm/content/api-docs/openapi-extensions/x-nullable) - Mark schemas as nullable in the API documentation.
- [x-servers](/docs/realm/content/api-docs/openapi-extensions/x-servers) - Add one or more target hosts for the API.


## Resources

- **[Add OpenAPI definitions to your project](/docs/realm/content/api-docs/add-openapi-docs)** - Complete guide for integrating OpenAPI documentation into your Redocly project with extensions support