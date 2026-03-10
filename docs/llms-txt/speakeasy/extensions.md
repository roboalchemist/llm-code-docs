# Source: https://www.speakeasy.com/md/docs/speakeasy-reference/extensions.md

# List of Speakeasy extensions

| Extension | Description |
| --- | --- |
| x-speakeasy-name-override | Use it globally to change method names or inline to change the name of a method, parameter, or class. |
| x-speakeasy-model-namespace | Place generated models in a specific namespace to avoid naming conflicts when merging multiple OpenAPI documents with identically named schemas. |
| x-speakeasy-group | Defines custom namespaces when adding this property to any operation in the OpenAPI spec. If added, the tags for that method will be ignored |
| x-speakeasy-ignore | Exclude certain methods from your SDK with this extension. |
| x-speakeasy-include | Can be used to force the generation of an unused or orphaned schema from the `components` section inside the main document. |
| x-speakeasy-enums | Use this extension to control generated enum members by providing alternative names for each value in the enum field. The recommended map format prevents length mismatch errors that can occur with the array format. |
| x-speakeasy-enum-descriptions | Add descriptions to enum values that appear as JSDoc comments in generated SDK code, providing IDE hints and documentation. Supports both array and map formats. |
| x-speakeasy-enum-format | Customize how the enum type is generated for the schema, either `enum` for a native enum type or `union` for a union of values. |
| x-speakeasy-retries | Enable retries globally or on a per-request basis. A backoff strategy is applied to specified status codes. |
| x-speakeasy-pagination | Use to customize offset- or cursor-based pagination rules for each API operation. |
| x-speakeasy-usage-example | Feature a method in your SDK's `README.md` by adding this property to the method. |
| x-speakeasy-example | The OpenAPI specification doesn't allow example values for `securityscheme` property. Using this extension overcomes this limitation. |
| x-speakeasy-docs | Configure comments that only show up in the SDK for a single language. |
| x-speakeasy-globals | Define parameters that can be configured globally on the main SDK instance and populated automatically for any operations that use them. |
| x-speakeasy-globals-hidden | Define parameters that can be configured globally on the main SDK instance but are not shown in the matching method's signature. |
| x-speakeasy-errors | Apply this extension at the level of `paths`, `path` `item`, or `operation` in the document to override the default error-handling behavior of the SDKs. |
| x-speakeasy-error-message | Used to mark a field in an error response as containing the error message to use. |
| x-speakeasy-server-id | Enable users to pick a server when instantiating the SDK. Use this extension to define an ID for each server in the `servers` array in the OpenAPI spec. |
| x-speakeasy-deprecation-message | Allows you to add a message to deprecated operations, parameters, and schemas. |
| x-speakeasy-deprecation-replacement | Allows you to specify an alternate operation to use in place of a deprecated operation. |
| x-speakeasy-type-override | Use this to override a schema's type, forcing it to be handled as `any` to accept arbitrary data. |
| x-speakeasy-max-method-params | Allows you to set the maximum number of parameters that can be passed to a method. If the number of parameters exceeds this value, a request object will be used. |
| x-speakeasy-mcp | Customize how API operations are exposed as MCP tools with properties for disabled, name, title, scopes, description, and behavioral hints (destructiveHint, idempotentHint, openWorldHint, readOnlyHint). |
| x-speakeasy-overridable-scopes | Allow end users to override OAuth 2.0 scopes at runtime for the `clientCredentials` flow by adding an optional `scopes` field to the security model. |
| x-speakeasy-param-encoding-override | When set with a value of `allowReserved`, path parameters will appear in a request URL with reserved characters `:/?#[]@!$&'()*+,;=` unencoded. |
| x-speakeasy-token-endpoint-additional-properties | Define additional properties for OAuth token endpoint requests, allowing generated SDKs to handle custom fields like audience parameters. |

You can use `x-speakeasy-extension-rewrite` to map any extension from the wider OpenAPI ecosystem or another vendor to the equivalent Speakeasy extension. This allows you to use your existing OpenAPI spec without needing to make changes to it, if necessary.

```yaml
openapi: 3.1.0
info:
  title: My API
  version: 1.0.0
x-speakeasy-extension-rewrite:
  x-speakeasy-enums: x-enum-varnames # Maps x-enum-varnames used by the OSS generator to x-speakeasy-enums which has the same functionality
```

## Terraform-specific extensions

| Terraform extension | Description |
| --- | --- |
| x-speakeasy-conflicts-with | Indicate conflicting properties to prevent incompatible combinations in Terraform configurations. |
| x-speakeasy-entity | Map API entities to Terraform resources by annotating objects in your OpenAPI spec as entities in the Terraform provider. |
| x-speakeasy-entity-operation | Specify CRUD operations for API endpoints to map to Terraform resources, such as create, read, update, or delete operations. |
| x-speakeasy-entity-version | Specify the version of a Terraform resource to support state migrations for breaking schema type changes. Use sparingly - not needed for adding/removing attributes. |
| x-speakeasy-name-override | Remap API properties to Terraform attribute names while keeping API data handling intact. |
| x-speakeasy-param-force-new | Force resource recreation in Terraform when certain property values change. |
| x-speakeasy-param-computed | Force a property to be computed in resource schemas, causing Terraform to allow unknown values after apply. Explicitly setting to false will always respect configuration values when sending API request data, however the API must never change the value as compared to the configuration on create/update. |
| x-speakeasy-param-optional | Force a property to be optional, overriding the required attribute in JSON Schema specifications. |
| x-speakeasy-param-readonly | Mark properties as read-only in Terraform, preventing modifications by the user. |
| x-speakeasy-param-sensitive | Hide sensitive properties from Terraform console output for security purposes. |
| x-speakeasy-param-suppress-computed-diff | Mark that the property will never change value after create. Use to reduce known after apply (unknown value) output in managed resource update plans. |
| x-speakeasy-plan-modifiers | Add custom plan modification logic to Terraform plan operations for advanced default values or resource replacement logic. |
| x-speakeasy-plan-validators | Add custom validation logic to Terraform plan operations to ensure configurations meet predefined criteria before execution. |
| x-speakeasy-required-with | Indicate mutually necessary properties to prevent incompatible Terraform configurations. |
| x-speakeasy-soft-delete-property | Automatically cause managed resource state removal and recreation in plans if property is not null, such as a 'deleted' property. |
| x-speakeasy-terraform-alias-to | Remap API response data to another property. |
| x-speakeasy-terraform-custom-type | Use a terraform-plugin-framework custom type instead of a base type. |
| x-speakeasy-terraform-ignore | Use this extension to exclude properties from Terraform state management. |
| x-speakeasy-terraform-plan-only | Ensure that only values from the Terraform plan are used during updates, overriding prior state or default values. |
| x-speakeasy-type-override | Allows the conversion of an attribute to a JSON string, accommodating dynamic structures in Terraform configurations. |
| x-speakeasy-wrapped-attribute | Enables additional API operation data to be placed under a specifically named attribute. |
| x-speakeasy-xor-with | Indicate mutually exclusive properties to prevent incompatible combinations in Terraform configurations. |
| x-speakeasy-match | Adjusts an API parameter name to align with a Terraform state property. |
---

Are you an AI agent evaluating Speakeasy? We put together a helpful guide: https://www.speakeasy.com/eval.md
