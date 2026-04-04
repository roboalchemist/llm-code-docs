# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters.md.txt

# Method: projects.histories.executions.steps.accessibilityClusters

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#body.PATH_PARAMETERS)
- [Query parameters](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#body.ListStepAccessibilityClustersResponse.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#body.aspect)
- [SuggestionClusterProto](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SuggestionClusterProto)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SuggestionClusterProto.SCHEMA_REPRESENTATION)
- [SuggestionCategory](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SuggestionCategory)
- [SuggestionProto](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SuggestionProto)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SuggestionProto.SCHEMA_REPRESENTATION)
- [SafeHtmlProto](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SafeHtmlProto)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SafeHtmlProto.SCHEMA_REPRESENTATION)
- [SuggestionPriority](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SuggestionPriority)
- [RegionProto](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#RegionProto)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#RegionProto.SCHEMA_REPRESENTATION)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#try-it)

Lists accessibility clusters for a given Step

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read project
- INVALID_ARGUMENT - if the request is malformed
- FAILED_PRECONDITION - if an argument in the request happens to be invalid; e.g. if the locale format is incorrect
- NOT_FOUND - if the containing Step does not exist

### HTTP request

`GET https://toolresults.googleapis.com/toolresults/v1beta3/{name=projects/*/histories/*/executions/*/steps/*}:accessibilityClusters`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

|                                                                                      Parameters                                                                                       ||
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name` | `string` A full resource name of the step. For example, projects/my-project/histories/bh.1234567890abcdef/executions/ 1234567890123456789/steps/bs.1234567890abcdef Required. |

### Query parameters

|                                                                                                                                  Parameters                                                                                                                                   ||
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `locale` | `string` The accepted format is the canonical Unicode format with hyphen as a delimiter. Language must be lowercase, Language Script - Capitalized, Region - UPPERCASE. See <http://www.unicode.org/reports/tr35/#Unicode_locale_identifier> for details. Required. |

### Request body

The request body must be empty.

### Response body

Response message for AccessibilityService.ListStepAccessibilityClusters.

If successful, the response body contains data with the following structure:

|                                                                                                  JSON representation                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "name": string, "clusters": [ { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SuggestionClusterProto) } ] } ``` |

|                                                                                                                                                                                                                                                                      Fields                                                                                                                                                                                                                                                                      ||
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`       | `string` A full resource name of the step. For example, projects/my-project/histories/bh.1234567890abcdef/executions/ 1234567890123456789/steps/bs.1234567890abcdef Always presents.                                                                                                                                                                                                                                                                                                                                               |
| `clusters[]` | `object (`[SuggestionClusterProto](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SuggestionClusterProto)`)` A sequence of accessibility suggestions, grouped into clusters. Within the sequence, clusters that belong to the same SuggestionCategory should be adjacent. Within each category, clusters should be ordered by their SuggestionPriority (ERRORs first). The categories should be ordered by their highest priority cluster. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## SuggestionClusterProto

A set of similar suggestions that we suspect are closely related.

This proto and most of the nested protos are branched from foxandcrown.prelaunchreport.service.SuggestionClusterProto, replacing PLR's dependencies with FTL's.

|                                                                                                                                                                               JSON representation                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "category": enum (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SuggestionCategory), "suggestions": [ { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SuggestionProto) } ] } ``` |

|                                                                                                                                                                                                          Fields                                                                                                                                                                                                          ||
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `category`      | `enum (`[SuggestionCategory](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SuggestionCategory)`)` Category in which these types of suggestions should appear. Always set.                                                                                                                                      |
| `suggestions[]` | `object (`[SuggestionProto](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SuggestionProto)`)` A sequence of suggestions. All of the suggestions within a cluster must have the same SuggestionPriority and belong to the same SuggestionCategory. Suggestions with the same screenshot URL should be adjacent. |

## SuggestionCategory

|        Enums         ||
|-------------------|---|
| `unknownCategory` |   |
| `contentLabeling` |   |
| `touchTargetSize` |   |
| `lowContrast`     |   |
| `implementation`  |   |

## SuggestionProto

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               JSON representation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "title": string, "shortMessage": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SafeHtmlProto) }, "longMessage": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SafeHtmlProto) }, "priority": enum (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SuggestionPriority), "helpUrl": string, "region": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#RegionProto) }, "secondaryPriority": number, "screenId": string, // Union field `resource_id` can be only one of the following: "resourceName": string, "pseudoResourceId": string // End of list of possible types for union field `resource_id`. } ``` |

|                                                                                                                                                                         Fields                                                                                                                                                                          ||
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `title`             | `string` General title for the suggestion, in the user's language, without markup. Always set.                                                                                                                                                                                                                                     |
| `shortMessage`      | `object (`[SafeHtmlProto](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SafeHtmlProto)`)` Concise message, in the user's language, representing the suggestion, which may contain markup. Always set.                                     |
| `longMessage`       | `object (`[SafeHtmlProto](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SafeHtmlProto)`)` Message, in the user's language, explaining the suggestion, which may contain markup. Always set.                                               |
| `priority`          | `enum (`[SuggestionPriority](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#SuggestionPriority)`)` Relative importance of a suggestion. Always set.                                                                                        |
| `helpUrl`           | `string` Reference to a help center article concerning this type of suggestion. Always set.                                                                                                                                                                                                                                        |
| `region`            | `object (`[RegionProto](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.steps/accessibilityClusters#RegionProto)`)` Region within the screenshot that is relevant to this suggestion. Optional.                                                                         |
| `secondaryPriority` | `number` Relative importance of a suggestion as compared with other suggestions that have the same priority and category. This is a meaningless value that can be used to order suggestions that are in the same category and have the same priority. The larger values have higher priority (i.e., are more important). Optional. |
| `screenId`          | `string` ID of the screen for the suggestion. It is used for getting the corresponding screenshot path. For example, screenId "1" corresponds to "1.png" file in GCS. Always set.                                                                                                                                                  |
| Union field `resource_id`. `resource_id` can be only one of the following:                                                                                                                                                                                                                                                                              ||
| `resourceName`      | `string` Reference to a view element, identified by its resource name, if it has one.                                                                                                                                                                                                                                              |
| `pseudoResourceId`  | `string` A somewhat human readable identifier of the source view, if it does not have a resourceName. This is a path within the accessibility hierarchy, an element with resource name; similar to an XPath.                                                                                                                       |

## SafeHtmlProto

IMPORTANT: It is unsafe to accept this message from an untrusted source, since it's trivial for an attacker to forge serialized messages that don't fulfill the type's safety contract -- for example, it could contain attacker controlled script. A system which receives a SafeHtmlProto implicitly trusts the producer of the SafeHtmlProto. So, it's generally safe to return this message in RPC responses, but generally unsafe to accept it in RPC requests.

|                        JSON representation                         |
|--------------------------------------------------------------------|
| ``` { "privateDoNotAccessOrElseSafeHtmlWrappedValue": string } ``` |

|                                                                                                                           Fields                                                                                                                           ||
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `privateDoNotAccessOrElseSafeHtmlWrappedValue` | `string` IMPORTANT: Never set or read this field, even from tests, it is private. See documentation at the top of .proto file for programming language packages with which to create or read this message. |

## SuggestionPriority

|        Enums         ||
|-------------------|---|
| `unknownPriority` |   |
| `error`           |   |
| `warning`         |   |
| `info`            |   |

## RegionProto

A rectangular region.

|                                   JSON representation                                    |
|------------------------------------------------------------------------------------------|
| ``` { "topPx": integer, "leftPx": integer, "heightPx": integer, "widthPx": integer } ``` |

|                                    Fields                                    ||
|------------|------------------------------------------------------------------|
| `topPx`    | `integer` The top of the rectangle, in pixels. Always set.       |
| `leftPx`   | `integer` The left side of the rectangle, in pixels. Always set. |
| `heightPx` | `integer` The height, in pixels. Always set.                     |
| `widthPx`  | `integer` The width, in pixels. Always set.                      |