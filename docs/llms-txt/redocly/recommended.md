# Source: https://redocly.com/docs/cli/rules/recommended.md

# Source: https://redocly.com/docs/cli/v1/rules/recommended.md

# Recommended ruleset

These are the rules in the `recommended` set, grouped by their severity.

Errors:

- [no-empty-servers](/docs/cli/v1/rules/oas/no-empty-servers)
- [no-enum-type-mismatch](/docs/cli/v1/rules/oas/no-enum-type-mismatch)
- [no-example-value-and-externalValue](/docs/cli/v1/rules/oas/no-example-value-and-externalValue)
- [no-identical-paths](/docs/cli/v1/rules/oas/no-identical-paths)
- [no-path-trailing-slash](/docs/cli/v1/rules/oas/no-path-trailing-slash)
- [no-server-trailing-slash](/docs/cli/v1/rules/oas/no-server-trailing-slash)
- [no-server-variables-empty-enum](/docs/cli/v1/rules/oas/no-server-variables-empty-enum)
- [no-undefined-server-variable](/docs/cli/v1/rules/oas/no-undefined-server-variable)
- [no-unresolved-refs](/docs/cli/v1/rules/oas/no-unresolved-refs)
- [operation-operationId-unique](/docs/cli/v1/rules/oas/operation-operationId-unique)
- [operation-operationId-url-safe](/docs/cli/v1/rules/oas/operation-operationId-url-safe)
- [operation-parameters-unique](/docs/cli/v1/rules/oas/operation-parameters-unique)
- [operation-summary](/docs/cli/v1/rules/oas/operation-summary)
- [path-declaration-must-exist](/docs/cli/v1/rules/oas/path-declaration-must-exist)
- [path-not-include-query](/docs/cli/v1/rules/oas/path-not-include-query)
- [path-parameters-defined](/docs/cli/v1/rules/oas/path-parameters-defined)
- [security-defined](/docs/cli/v1/rules/oas/security-defined)
- [spec-components-invalid-map-name](/docs/cli/v1/rules/oas/spec-components-invalid-map-name)
- [struct](/docs/cli/v1/rules/oas/struct)
- [parameters-unique](/docs/cli/v1/rules/arazzo/parameters-unique)
- [sourceDescription-type](/docs/cli/v1/rules/arazzo/sourcedescriptions-type)
- [sourceDescription-name-unique](/docs/cli/v1/rules/arazzo/sourcedescriptions-name-unique)
- [stepId-unique](/docs/cli/v1/rules/arazzo/stepid-unique)
- [workflow-dependsOn](/docs/cli/v1/rules/arazzo/workflow-dependson)
- [workflowId-unique](/docs/cli/v1/rules/arazzo/workflowid-unique)


Warnings:

- [configurable rules](/docs/cli/v1/rules/configurable-rules)
- [info-license-url](/docs/cli/v1/rules/oas/info-license-url)
- [info-license](/docs/cli/v1/rules/oas/info-license)
- [no-ambiguous-paths](/docs/cli/v1/rules/oas/no-ambiguous-paths)
- [no-invalid-media-type-examples](/docs/cli/v1/rules/oas/no-invalid-media-type-examples)
- [no-server-example.com](/docs/cli/v1/rules/oas/no-server-example-com)
- [no-unused-components](/docs/cli/v1/rules/oas/no-unused-components)
- [operation-2xx-response](/docs/cli/v1/rules/oas/operation-2xx-response)
- [operation-4xx-response](/docs/cli/v1/rules/oas/operation-4xx-response)
- [operation-operationId](/docs/cli/v1/rules/oas/operation-operationId)
- [tag-description](/docs/cli/v1/rules/oas/tag-description)
- [requestBody-replacements-unique](/docs/cli/v1/rules/arazzo/requestbody-replacements-unique)
- [step-onFailure-unique](/docs/cli/v1/rules/arazzo/step-onfailure-unique)
- [step-onSuccess-unique](/docs/cli/v1/rules/arazzo/step-onsuccess-unique)


## Recommended strict ruleset

There is also a `recommended-strict` version of `recommended`, which elevates all warnings to errors.

## Ruleset template

A copy-pastable version of this ruleset is available as a [ruleset template](/docs/cli/v1/rules/ruleset-templates).