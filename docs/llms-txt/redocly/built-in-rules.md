# Source: https://redocly.com/docs/cli/rules/built-in-rules.md

# Source: https://redocly.com/docs/cli/v1/rules/built-in-rules.md

# Built-in rules

The built-in rules are the ones we use ourselves and think apply to the majority of APIs. Some have some additional [configuration](/docs/cli/v1/rules/configure-rules), but otherwise all you need to do is decide whether each rule should `error`, `warn` or be `off`.

All the built-in rules are listed here, roughly grouped by the OpenAPI object they apply to.
The *Special rules* group contains rules that may apply to multiple objects or to the entire OpenAPI document.

Build [configurable rules](/docs/cli/v1/rules/configurable-rules) if the rule you need isn't listed.

## Rules for each API description format

Redocly CLI can lint multiple API description formats:

- [OpenAPI](#openapi-rules)
- [AsyncAPI](#asyncapi-rules)
- [Arazzo](#arazzo-rules)


Visit each page for details of what the rule does, additional configuration options, and examples of it in use.

## OpenAPI rules

The rules list is split into sections.

### Special rules

- [no-unresolved-refs](/docs/cli/v1/rules/oas/no-unresolved-refs): Every `$ref` must exist
- [no-unused-components](/docs/cli/v1/rules/oas/no-unused-components): All components must be used
- [security-defined](/docs/cli/v1/rules/oas/security-defined): Security rules must be defined, either globally or per-operation
- [struct](/docs/cli/v1/rules/oas/struct): Conform to the declared OpenAPI specification version
- [spec-components-invalid-map-name](/docs/cli/v1/rules/oas/spec-components-invalid-map-name): Use only alphanumeric and basic punctuation as key names in the components section
- [spec-strict-refs](/docs/cli/v1/rules/oas/spec-strict-refs) Restricts the usage of the `$ref` keyword.


### Info

- [info-contact](/docs/cli/v1/rules/oas/info-contact): Contact section is defined under `info`
- [info-license](/docs/cli/v1/rules/oas/info-license): License section is defined under `info`
- [info-license-url](/docs/cli/v1/rules/oas/info-license-url): License section contains a `url` to the license


### Operations

- [operation-2xx-response](/docs/cli/v1/rules/oas/operation-2xx-response): Every operation needs at least one 2xx response
- [operation-4xx-response](/docs/cli/v1/rules/oas/operation-4xx-response): Every operation needs at least one 4xx response
- [operation-4xx-problem-details-rfc7807](/docs/cli/v1/rules/oas/operation-4xx-problem-details-rfc7807): All 4xx responses use RFC7807 format
- [operation-description](/docs/cli/v1/rules/oas/operation-description): Description field is required for every operation
- [operation-operationId](/docs/cli/v1/rules/oas/operation-operationId): OperationId is required for every operation
- [operation-operationId-unique](/docs/cli/v1/rules/oas/operation-operationId-unique): OperationId must be unique
- [operation-operationId-url-safe](/docs/cli/v1/rules/oas/operation-operationId-url-safe): OperationIds can only contain characters that are safe to use in URLs
- [operation-summary](/docs/cli/v1/rules/oas/operation-summary): Summary is required for every operation


### Parameters

- [array-parameter-serialization](/docs/cli/v1/rules/oas/array-parameter-serialization): Require `style` and `explode` for parameters with array type
- [boolean-parameter-prefixes](/docs/cli/v1/rules/oas/boolean-parameter-prefixes): All boolean paramater names start with a particular prefix (such as "is")
- [no-invalid-parameter-examples](/docs/cli/v1/rules/oas/no-invalid-parameter-examples): Parameter examples must match declared schema types
- [operation-parameters-unique](/docs/cli/v1/rules/oas/operation-parameters-unique): No repeated parameter names within an operation
- [parameter-description](/docs/cli/v1/rules/oas/parameter-description): Parameters must all have descriptions
- [path-declaration-must-exist](/docs/cli/v1/rules/oas/path-declaration-must-exist): Paths must define template variables where placeholders are needed
- [path-not-include-query](/docs/cli/v1/rules/oas/path-not-include-query): No query parameters in path declarations (declare them as parameters with `in: query`)
- [path-parameters-defined](/docs/cli/v1/rules/oas/path-parameters-defined): Path template variables must be defined as parameters


### Paths

- [no-ambiguous-paths](/docs/cli/v1/rules/oas/no-ambiguous-paths): No path can match more than one PathItem entry, including template variables
- [no-http-verbs-in-paths](/docs/cli/v1/rules/oas/no-http-verbs-in-paths): Verbs like "get" cannot be used in paths
- [no-identical-paths](/docs/cli/v1/rules/oas/no-identical-paths): Paths cannot be identical, including template variables
- [no-path-trailing-slash](/docs/cli/v1/rules/oas/no-path-trailing-slash): No trailing slashes on paths
- [path-excludes-patterns](/docs/cli/v1/rules/oas/path-excludes-patterns): Set a regular expression that cannot be used in paths
- [path-segment-plural](/docs/cli/v1/rules/oas/path-segment-plural): All URL segments in a path must be plural (exceptions can be configured)
- [paths-kebab-case](/docs/cli/v1/rules/oas/paths-kebab-case): Paths must be in `kebab-case` format


### Requests, Responses, and Schemas

- [component-name-unique](/docs/cli/v1/rules/oas/component-name-unique): Check for schema-wide unqiue naming of parameters, schemas, request bodies and responses
- [no-enum-type-mismatch](/docs/cli/v1/rules/oas/no-enum-type-mismatch): Enum options must match the data type declared in the schema
- [no-example-value-and-externalValue](/docs/cli/v1/rules/oas/no-example-value-and-externalValue): Either the `value` or `externalValue` may be present, but not both
- [no-invalid-media-type-examples](/docs/cli/v1/rules/oas/no-invalid-media-type-examples): Example request bodies must match the declared schema
- [no-invalid-schema-examples](/docs/cli/v1/rules/oas/no-invalid-schema-examples): Schema examples must match declared types
- [no-required-schema-properties-undefined](/docs/cli/v1/rules/oas/no-required-schema-properties-undefined): All properties marked as required must be defined
- [no-schema-type-mismatch](/docs/cli/v1/rules/oas/no-schema-type-mismatch): Detects schemas with type mismatches between object and items fields, and array and properties fields.
- [request-mime-type](/docs/cli/v1/rules/oas/request-mine-type): Configure allowed mime types for requests
- [response-mime-type](/docs/cli/v1/rules/oas/response-mime-type): Configure allowed mime types for responses
- [response-contains-header](/docs/cli/v1/rules/oas/response-contains-header): List headers that must be included with specific response types
- [response-contains-property](/docs/cli/v1/rules/oas/response-contains-property): Specify properties that should be present in specific response types
- [scalar-property-missing-example](/docs/cli/v1/rules/oas/scalar-property-missing-example): All required scalar (non-object) properties must have examples defined
- [required-string-property-missing-min-length](/docs/cli/v1/rules/oas/required-string-property-missing-min-length): All required properties of type string must have a `minLength` configured


### Servers

- [no-empty-servers](/docs/cli/v1/rules/oas/no-empty-servers): Servers array must be defined
- [no-server-example.com](/docs/cli/v1/rules/oas/no-server-example-com): `example.com` is not acceptable as a server URL
- [no-server-trailing-slash](/docs/cli/v1/rules/oas/no-server-trailing-slash): Server URLs cannot end with a slash (paths usually start with a slash)
- [no-server-variables-empty-enum](/docs/cli/v1/rules/oas/no-server-variables-empty-enum): Require that enum values are set if variables are used in server definition
- [no-undefined-server-variable](/docs/cli/v1/rules/oas/no-undefined-server-variable): All variables in server definition must be defined


### Tags

- [operation-singular-tag](/docs/cli/v1/rules/oas/operation-singular-tag): Each operation may only have one tag
- [operation-tag-defined](/docs/cli/v1/rules/oas/operation-tag-defined): Tags can only be used if they are defined at the top level
- [tag-description](/docs/cli/v1/rules/oas/tag-description): Tags must have descriptions
- [tags-alphabetical](/docs/cli/v1/rules/oas/tags-alphabetical): Tags in the top-level `tags` section must appear alphabetically


## AsyncAPI rules

Use the rules in this section for AsyncAPI-specific linting.
Other rules such as the `spec` and `info.*` rules also apply to AsyncAPI.

- [channels-kebab-case](/docs/cli/v1/rules/async/channels-kebab-case): Channels must be in `kebab-case` format
- [no-channel-trailing-slash](/docs/cli/v1/rules/async/no-channel-trailing-slash): No trailing slashes on channels


## Arazzo rules

Within the Arazzo family of rules, there are rules for the main Arazzo specification format, and some additional rules for extensions supported by Respect, the Redocly testing utility.

### Arazzo

- [criteria-unique](/docs/cli/v1/rules/arazzo/criteria-unique): the criteria list must not contain duplicated assertions
- [parameters-unique](/docs/cli/v1/rules/arazzo/parameters-unique): the `parameters` list must not include duplicate parameters
- [requestBody-replacements-unique](/docs/cli/v1/rules/arazzo/requestbody-replacements-unique): the `replacements` of the `requestBody` object must be unique
- [sourceDescriptions-name-unique](/docs/cli/v1/rules/arazzo/sourcedescriptions-name-unique): the `name` property of the `sourceDescription` object must be unique across all source descriptions
- [sourceDescriptions-type](/docs/cli/v1/rules/arazzo/sourcedescriptions-type): the `type` property of the `sourceDescription` object must be either `openapi` or `arazzo`
- [stepId-unique](/docs/cli/v1/rules/arazzo/stepid-unique): the `stepId` must be unique amongst all steps described in the workflow
- [step-onFailure-unique](/docs/cli/v1/rules/arazzo/step-onfailure-unique): the `onFailure` actions of the `step` object must be unique
- [step-onSuccess-unique](/docs/cli/v1/rules/arazzo/step-onsuccess-unique): the `onSuccess` actions of the `step` object must be unique
- [workflow-dependsOn](/docs/cli/v1/rules/arazzo/workflow-dependson): the items in the `workflow` `dependsOn` property must exist and be unique
- [workflowId-unique](/docs/cli/v1/rules/arazzo/workflowid-unique): the `workflowId` property must be unique across all workflows
- [sourceDescriptions-not-empty](/docs/cli/v1/rules/arazzo/sourcedescriptions-not-empty): the `sourceDescriptions` must be defined and the list must have at least one entry.


### Respect

The below rules are being migrated to Respect:

- [no-criteria-xpath](/docs/cli/v1/rules/respect/no-criteria-xpath): the `xpath` type criteria is not supported by Respect.
- [respect-supported-versions](/docs/cli/v1/rules/respect/respect-supported-versions): the `version` property must be one of the supported values.


## Resources

- Learn more about [API linting](/docs/cli/v1/api-standards), or follow the [guide to configuring a ruleset](/docs/cli/v1/guides/configure-rules).
- Visit the [documentation on per-API configuration](/docs/cli/v1/configuration/apis).
- If you didn't find the rule you need, build a [configurable rule](/docs/cli/v1/rules/configurable-rules) for a perfect linting fit.