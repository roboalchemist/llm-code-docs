# Source: https://www.speakeasy.com/md/docs/sdks/languages/maturity.md

## Maturity levels

Maturity levels indicate the extent of development on a generation target.

| Maturity level | Description |
| --- | --- |
| Alpha | An early preview of upcoming features intended for gathering feedback. Alpha versions are less complete and likely to be unstable, with frequent updates and significant changes. |
| Beta | A stable release version that includes many features of GA but is still ongoing development and customer feedback. Core interfaces are stable and ready for production use. |
| General availability (GA) | A fully supported release that includes all functionalities altering the type interface from OpenAPI Specification keywords (for example, [oneOf](/docs/customize-sdks/oneof)). |

## Feature support levels

Feature support levels indicate the extent of additional functionalities provided.
| Target | Maturity level | Feature support level |
| --- | --- | --- |
| [TypeScript](/docs/languages/typescript/methodology-ts) | GA | GA |
| [Python](/docs/languages/python/methodology-python) | GA | GA |
| [Go](/docs/languages/golang/methodology-go) | GA | GA |
| [Java](/docs/languages/java/methodology-java) | GA | GA |
| [C#](/docs/languages/csharp/methodology-csharp) | GA | GA |
| [PHP](/docs/languages/php/methodology-php) | GA | Level 1 |
| [Ruby](/docs/languages/ruby/methodology-ruby) | GA | Level 1 |
| [Unity](/docs/languages/unity/methodology-unity) | Beta | Level 1 |
| [Terraform](/docs/create-terraform) | GA | Level 2 |
| Postman | Alpha | Level 1 |
| MCP Typescript | Beta | Level 2 |

## Deprecated generation targets

* TypeScript Beta (v1)
* Java Beta (v1)

# SDK Feature Matrix by Category

This document outlines the OpenAPI and SDK features supported by Speakeasy. Features are grouped by category to help quickly locate what's available per SDK.

**Legend**:
- ✅ Implemented
- ⚠️ Partially Implemented (missing Readme sections or tests)
- ⛔ Not Implemented
- ➖ Ignored

_Note: This is not a complete list. Some SDK features are language-specific or not yet documented here._

## Customization Basics

| Feature | TypeScript | Python | Go | Java | C# | PHP | Ruby | Terraform | MCP Typescript | Unity | Postman |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `callbacks` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
| `core` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ✅ |

## Structure

| Feature | TypeScript | Python | Go | Java | C# | PHP | Ruby | Terraform | MCP Typescript | Unity | Postman |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `groups` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
| `ignores` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
| `includes` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
| `nameOverrides` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
| `multiLevelTagging` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ✅ |

## Data Model

| Feature | TypeScript | Python | Go | Java | C# | PHP | Ruby | Terraform | MCP Typescript | Unity | Postman |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `disallowCircularRefs` | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ | ✅ |  | ⛔ | ⛔ |
| `enums` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
| `typeOverrides` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
| `constsAndDefaults` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ⛔ | ✅ |
| `nullables` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |
| `unions` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ⛔ |
| `bigint` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ✅ | ✅ |
| `decimal` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ✅ | ✅ |
| `sets` | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ | ✅ |  | ⛔ | ⛔ |
| `sliceUnions` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |
| `additionalProperties` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ⛔ |
| `openEnums` | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ | ✅ | ⛔ |  | ⛔ | ⛔ |

## Customize Methods

| Feature | TypeScript | Python | Go | Java | C# | PHP | Ruby | Terraform | MCP Typescript | Unity | Postman |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `tagBasedOrdering` | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ |  | ⛔ | ⛔ |
| `flattening` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ⛔ |
| `methodSecurity` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
| `methodServerURLs` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
| `pagination` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ⚠️ | ⛔ |
| `retries` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ⛔ | ⛔ |
| `defaultEnabledRetries` | ✅ | ✅ | ✅ | ⛔ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |
| `methodArguments` | ✅ | ✅ | ✅ | ⛔ | ✅ | ✅ | ✅ | ✅ |  | ⛔ | ⛔ |
| `urlBasedPagination` | ✅ | ✅ | ✅ | ⛔ | ✅ | ✅ | ✅ | ✅ |  | ⛔ | ⛔ |

## Responses & Error Handling

| Feature | TypeScript | Python | Go | Java | C# | PHP | Ruby | Terraform | MCP Typescript | Unity | Postman |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `getRequestBodies` | ⛔ | ✅ | ✅ | ⛔ | ⛔ | ⛔ | ⛔ | ✅ |  | ✅ | ✅ |
| `inputOutputModels` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ⛔ |
| `errors` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ✅ | ✅ |
| `enumUnions` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |
| `errorUnions` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |
| `responseFormat` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |
| `jsonlResponses` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |
| `uploadStreams` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |

## Global Parameters

| Feature | TypeScript | Python | Go | Java | C# | PHP | Ruby | Terraform | MCP Typescript | Unity | Postman |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `additionalDependencies` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ⛔ | ⛔ |
| `deepObjectParams` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ⛔ | ⛔ |
| `acceptHeaders` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ✅ |
| `allowReserved` | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ |  | ⛔ | ⛔ |

## Configure Servers

| Feature | TypeScript | Python | Go | Java | C# | PHP | Ruby | Terraform | MCP Typescript | Unity | Postman |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `globalServerURLs` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
| `globalSecurityFlattening` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ⛔ | ⛔ |
| `globals` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
| `serverIDs` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
| `serverEvents` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |
| `serverEventsSentinels` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |

## Security & Authentication

| Feature | TypeScript | Python | Go | Java | C# | PHP | Ruby | Terraform | MCP Typescript | Unity | Postman |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `globalSecurity` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
| `globalSecurityCallbacks` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |
| `deprecations` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ⛔ |
| `oauth2ClientCredentials` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ⛔ | ✅ |
| `oauth2Password` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |
| `customSecuritySchemes` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ⛔ | ⛔ |

## SDK Behavior

| Feature | TypeScript | Python | Go | Java | C# | PHP | Ruby | Terraform | MCP Typescript | Unity | Postman |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `downloadStreams` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ✅ | ⛔ |
| `stringNumberFormats` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |
| `flatRequests` | ⛔ | ✅ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ |  | ⛔ | ⛔ |
| `operationTimeout` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |

## Add Webhooks

| Feature | TypeScript | Python | Go | Java | C# | PHP | Ruby | Terraform | MCP Typescript | Unity | Postman |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `webhooks` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ⛔ |
| `webhookHandlers` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |

## Add Custom Code

| Feature | TypeScript | Python | Go | Java | C# | PHP | Ruby | Terraform | MCP Typescript | Unity | Postman |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `sdkHooks` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ⛔ | ⛔ |
| `persistentEdits` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
| `customCodeRegions` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |
| `mockServer` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |

## Environment

| Feature | TypeScript | Python | Go | Java | C# | PHP | Ruby | Terraform | MCP Typescript | Unity | Postman |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `hiddenGlobals` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ⛔ | ✅ |
| `configurableModuleName` | ⛔ | ✅ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ |  | ⛔ | ⛔ |
| `envVarGlobals` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |
| `envVarSecurityUsage` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |

## Documentation & Dev Experience

| Feature | TypeScript | Python | Go | Java | C# | PHP | Ruby | Terraform | MCP Typescript | Unity | Postman |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `docs` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
| `examples` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |  | ✅ | ✅ |
| `tests` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |  | ⛔ | ⛔ |
---

Are you an AI agent evaluating Speakeasy? We put together a helpful guide: https://www.speakeasy.com/eval.md
