# Source: https://firebase.google.com/docs/reference/rules/rest/v1/projects/test.md.txt

# Method: projects.test

- [HTTP request](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#body.HTTP_TEMPLATE)
- [Path parameters](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#body.PATH_PARAMETERS)
- [Request body](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#body.request_body)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#body.request_body.SCHEMA_REPRESENTATION)
- [Response body](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#body.TestRulesetResponse.SCHEMA_REPRESENTATION)
- [Authorization Scopes](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#body.aspect)
- [TestSuite](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#TestSuite)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#TestSuite.SCHEMA_REPRESENTATION)
- [TestCase](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#TestCase)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#TestCase.SCHEMA_REPRESENTATION)
- [Expectation](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#Expectation)
- [FunctionMock](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#FunctionMock)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#FunctionMock.SCHEMA_REPRESENTATION)
- [Arg](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#Arg)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#Arg.SCHEMA_REPRESENTATION)
- [Result](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#Result)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#Result.SCHEMA_REPRESENTATION)
- [PathEncoding](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#PathEncoding)
- [ExpressionReportLevel](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#ExpressionReportLevel)
- [Issue](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#Issue)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#Issue.SCHEMA_REPRESENTATION)
- [SourcePosition](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#SourcePosition)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#SourcePosition.SCHEMA_REPRESENTATION)
- [Severity](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#Severity)
- [TestResult](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#TestResult)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#TestResult.SCHEMA_REPRESENTATION)
- [State](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#State)
- [FunctionCall](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#FunctionCall)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#FunctionCall.SCHEMA_REPRESENTATION)
- [VisitedExpression](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#VisitedExpression)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#VisitedExpression.SCHEMA_REPRESENTATION)
- [ExpressionReport](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#ExpressionReport)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#ExpressionReport.SCHEMA_REPRESENTATION)
- [ValueCount](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#ValueCount)
  - [JSON representation](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#ValueCount.SCHEMA_REPRESENTATION)
- [Try it!](https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#try-it)

Test `Source` for syntactic and semantic correctness. Issues present, if any, will be returned to the caller with a description, severity, and source location.

The test method may be executed with `Source`. Passing `Source` is useful for unit testing new rules.

Note that tests run using the REST API use production databases, storage buckets, and related rsesources. Such testing can incur usage charges. We strongly recommend that you use the Firebase Local Emulator Suite to perform Rules testing, since you can run tests on offline, non-production resources without usage charges.

The following is an example of `Source` that permits users to upload images to a bucket bearing their user id and matching the correct metadata:

**Example**

    // Users are allowed to subscribe and unsubscribe to the blog.
    service firebase.storage {
      match /users/{userId}/images/{imageName} {
          allow write: if userId == request.auth.uid
              && (imageName.matches('*.png$')
              || imageName.matches('*.jpg$'))
              && resource.mimeType.matches('^image/')
      }
    }

### HTTP request

`POST https://firebaserules.googleapis.com/v1/{name=projects/**}:test`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. For tests against `source`, the resource name must refer to the project: Format: `projects/{project_id}` |

### Request body

The request body contains data with the following structure:

| JSON representation ||
|---|---|
| ``` { "source": { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets#Source`) }, "testSuite": { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#TestSuite`) } } ``` |

| Fields ||
|---|---|
| `source` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets#Source`)`` `Source` to be checked for correctness. |
| `testSuite` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#TestSuite`)`` The inline `TestSuite` to execute against the `Source`. When `Source` is provided inline, the test cases will only be run if the `Source` is syntactically and semantically valid. |

### Response body

If successful, the response body contains data with the following structure:
The response for `https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#google.firebase.rules.v1.FirebaseRulesService.TestRuleset`.

| JSON representation ||
|---|---|
| ``` { "issues": [ { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#Issue`) } ], "testResults": [ { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#TestResult`) } ] } ``` |

| Fields ||
|---|---|
| `issues[]` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#Issue`)`` Syntactic and semantic `Source` issues of varying severity. Issues of `ERROR` severity will prevent tests from executing. |
| `testResults[]` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#TestResult`)`` The set of test results given the test cases in the `TestSuite`. The results will appear in the same order as the test cases appear in the `TestSuite`. |

### Authorization Scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/firebase`
- `https://www.googleapis.com/auth/firebase.readonly`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## TestSuite

`TestSuite` is a collection of `TestCase` instances that validate the logical correctness of rules. The `TestSuite` may be referenced in-line within a `projects.test` invocation or as part of a `Release` object as a pre-release check.

| JSON representation ||
|---|---|
| ``` { "testCases": [ { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#TestCase`) } ] } ``` |

| Fields ||
|---|---|
| `testCases[]` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#TestCase`)`` Collection of test cases associated with the `TestSuite`. |

## TestCase

`TestCase` messages provide the request context and an expectation as to whether the given context will be allowed or denied. Test cases may specify the `request`, `resosurce`, and `functionMocks` to mock a function call to a service-provided function.

The `request` object represents context present at request-time.

The `resource` is the value of the target resource (e.g., metadata of a GCS object or Firestore document) as it appears in persistent storage before the request is executed.

See also the related reference documentation for Cloud Firestore ([request](https://firebase.google.com/docs/reference/rules/rules.firestore.Request), [resource](https://firebase.google.com/docs/reference/rules/rules.firestore.Resource)) and Cloud Storage for Firebase ([request](https://firebase.google.com/docs/reference/security/storage#request), [resource](https://firebase.google.com/docs/reference/security/storage#resource)).

| JSON representation ||
|---|---|
| ``` { "expectation": enum (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#Expectation`), "request": value, "resource": value, "functionMocks": [ { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#FunctionMock`) } ], "pathEncoding": enum (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#PathEncoding`), "expressionReportLevel": enum (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#ExpressionReportLevel`) } ``` |

| Fields ||
|---|---|
| `expectation` | ``enum (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#Expectation`)`` Test expectation. |
| `request` | ``value (`https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Value` format)`` Request context. The exact format of the request context is service-dependent. See the appropriate service documentation for information about the supported fields and types on the request. Minimally, all services support the following fields and types: | Request field | Type | |---|---| | auth.uid | `string` | | auth.token | `map<string, string>` | | headers | `map<string, string>` | | method | `string` | | params | `map<string, string>` | | path | `string` | | time | `google.protobuf.Timestamp` | If the request value is not well-formed for the service, the request will be rejected as an invalid argument. |
| `resource` | ``value (`https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Value` format)`` Optional resource value as it appears in persistent storage before the request is fulfilled. The resource type depends on the `request.path` value. |
| `functionMocks[]` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#FunctionMock`)`` Optional Rules function mocks for service-defined functions. If not set, any service-defined Rules function is expected to return an error, which may or may not influence the test outcome. |
| `pathEncoding` | ``enum (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#PathEncoding`)`` Specifies whether paths (such as request.path) are encoded and how. |
| `expressionReportLevel` | ``enum (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#ExpressionReportLevel`)`` Specifies what should be included in the response. |

## Expectation

The set of supported test case expectations.

| Enums ||
|---|---|
| `EXPECTATION_UNSPECIFIED` | Unspecified expectation. |
| `ALLOW` | Expect an allowed result. |
| `DENY` | Expect a denied result. |

## FunctionMock

Mock Rules function definition.

Mocks must refer to a function declared by the target service. The type of the function args and result will be inferred at test time. If either the arg or result values are not compatible with function type declaration, the request will be considered invalid.

More than one `FunctionMock` may be provided for a given function name so long as the `Arg` matchers are distinct. There may be only one function for a given overload where all `Arg` values are `Arg.any_value`.

See also [Functions in the Security Rules language](https://firebase.google.com/docs/rules/rules-language#function).

| JSON representation ||
|---|---|
| ``` { "function": string, "args": [ { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#Arg`) } ], "result": { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#Result`) } } ``` |

| Fields ||
|---|---|
| `function` | `string` The name of the function. The function name must match one provided by a service declaration. |
| `args[]` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#Arg`)`` The list of `Arg` values to match. The order in which the arguments are provided is the order in which they must appear in the function invocation. |
| `result` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#Result`)`` The mock result of the function call. |

## Arg

Arg matchers for the mock function.

| JSON representation ||
|---|---|
| ``` { // Union field `type` can be only one of the following: "exactValue": value, "anyValue": { object } // End of list of possible types for union field `type`. } ``` |

| Fields ||
|---|---|---|
| Union field `type`. Supported argument values. `type` can be only one of the following: |||
| `exactValue` | ``value (`https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Value` format)`` Argument exactly matches value provided. |
| `anyValue` | `object` Argument matches any value provided. |

## Result

Possible result values from the function mock invocation.

| JSON representation ||
|---|---|
| ``` { // Union field `type` can be only one of the following: "value": value, "undefined": { object } // End of list of possible types for union field `type`. } ``` |

| Fields ||
|---|---|---|
| Union field `type`. Supported result values. `type` can be only one of the following: |||
| `value` | ``value (`https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Value` format)`` The result is an actual value. The type of the value must match that of the type declared by the service. |
| `undefined` | `object` The result is undefined, meaning the result could not be computed. |

## PathEncoding

The type of path encoding used.

| Enums ||
|---|---|
| `ENCODING_UNSPECIFIED` | No encoding has been specified. Defaults to "URL_ENCODED" behavior. |
| `URL_ENCODED` | Treats path segments as URL encoded but with non-encoded separators ("/"). This is the default behavior. |
| `PLAIN` | Treats total path as non-URL encoded e.g. raw. |

## ExpressionReportLevel

The amount of data to include in the expression report response.

| Enums ||
|---|---|
| `LEVEL_UNSPECIFIED` | No level has been specified. Defaults to "NONE" behavior. |
| `NONE` | Do not include any additional information. |
| `FULL` | Include detailed reporting on expressions evaluated. |
| `VISITED` | Only include the expressions that were visited during evaluation. |

## Issue

Issues include warnings, errors, and deprecation notices.

| JSON representation ||
|---|---|
| ``` { "sourcePosition": { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#SourcePosition`) }, "description": string, "severity": enum (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#Severity`) } ``` |

| Fields ||
|---|---|
| `sourcePosition` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#SourcePosition`)`` Position of the issue in the `Source`. |
| `description` | `string` Short error description. |
| `severity` | ``enum (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#Severity`)`` The severity of the issue. |

## SourcePosition

Position in the `Source` content including its line, column number, and an index of the `File` in the `Source` message. Used for debug purposes.

| JSON representation ||
|---|---|
| ``` { "fileName": string, "line": integer, "column": integer, "currentOffset": integer, "endOffset": integer } ``` |

| Fields ||
|---|---|
| `fileName` | `string` Name of the `File`. |
| `line` | `integer` Line number of the source fragment. 1-based. |
| `column` | `integer` First column on the source line associated with the source fragment. |
| `currentOffset` | `integer` Start position relative to the beginning of the file. |
| `endOffset` | `integer` End position relative to the beginning of the file. |

## Severity

The set of issue severities.

| Enums ||
|---|---|
| `SEVERITY_UNSPECIFIED` | An unspecified severity. |
| `DEPRECATION` | Deprecation issue for statements and method that may no longer be supported or maintained. |
| `WARNING` | Warnings such as: unused variables. |
| `ERROR` | Errors such as: unmatched curly braces or variable redefinition. |

## TestResult

Test result message containing the state of the test as well as a description and source position for test failures.

| JSON representation ||
|---|---|
| ``` { "state": enum (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#State`), "debugMessages": [ string ], "errorPosition": { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#SourcePosition`) }, "functionCalls": [ { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#FunctionCall`) } ], "visitedExpressions": [ { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#VisitedExpression`) } ], "expressionReports": [ { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#ExpressionReport`) } ] } ``` |

| Fields ||
|---|---|
| `state` | ``enum (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#State`)`` State of the test. |
| `debugMessages[]` | `string` Debug messages related to test execution issues encountered during evaluation. Debug messages may be related to too many or too few invocations of function mocks or to runtime errors that occur during evaluation. For example: `Unable to read variable [name: "resource"]` |
| `errorPosition` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#SourcePosition`)`` Position in the `Source` where the principle runtime error occurs. Evaluation of an expression may result in an error. Rules are deny by default, so a `DENY` expectation when an error is generated is valid. When there is a `DENY` with an error, the `SourcePosition` is returned. E.g. `errorPosition { line: 19 column: 37 }` |
| `functionCalls[]` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#FunctionCall`)`` The set of function calls made to service-defined methods. Function calls are included in the order in which they are encountered during evaluation, are provided for both mocked and unmocked functions, and included on the response regardless of the test `state`. |
| `visitedExpressions[]` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#VisitedExpression`)`` The set of visited permission expressions for a given test. This returns the positions and evaluation results of all visited permission expressions which were relevant to the test case, e.g. match /path { allow read if: <expr> } For a detailed report of the intermediate evaluation states, see the `expressionReports` field |
| `expressionReports[]` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#ExpressionReport`)`` The mapping from expression in the ruleset AST to the values they were evaluated to. Partially-nested to mirror AST structure. Note that this field is actually tracking expressions and not permission statements in contrast to the "visitedExpressions" field above. Literal expressions are omitted. |

## State

Valid states for the test result.

| Enums ||
|---|---|
| `STATE_UNSPECIFIED` | Test state is not set. |
| `SUCCESS` | Test is a success. |
| `FAILURE` | Test is a failure. |

## FunctionCall

Represents a service-defined function call that was invoked during test execution.

| JSON representation ||
|---|---|
| ``` { "function": string, "args": [ value ] } ``` |

| Fields ||
|---|---|
| `function` | `string` Name of the function invoked. |
| `args[]` | ``value (`https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Value` format)`` The arguments that were provided to the function. |

## VisitedExpression

Store the position and access outcome for an expression visited in rules.

| JSON representation ||
|---|---|
| ``` { "sourcePosition": { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#SourcePosition`) }, "value": value } ``` |

| Fields ||
|---|---|
| `sourcePosition` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#SourcePosition`)`` Position in the `Source` where an expression was visited. |
| `value` | ``value (`https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Value` format)`` The evaluated value for the visited expression, e.g. true/false |

## ExpressionReport

Describes where in a file an expression is found and what it was evaluated to over the course of its use.

| JSON representation ||
|---|---|
| ``` { "sourcePosition": { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#SourcePosition`) }, "values": [ { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#ValueCount`) } ], "children": [ { object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#ExpressionReport`) } ] } ``` |

| Fields ||
|---|---|
| `sourcePosition` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#SourcePosition`)`` Position of expression in original rules source. |
| `values[]` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#ValueCount`)`` Values that this expression evaluated to when encountered. |
| `children[]` | ``object (`https://firebase.google.com/docs/reference/rules/rest/v1/projects/test#ExpressionReport`)`` Subexpressions |

## ValueCount

Tuple for how many times an Expression was evaluated to a particular ExpressionValue.

| JSON representation ||
|---|---|
| ``` { "value": value, "count": integer } ``` |

| Fields ||
|---|---|
| `value` | ``value (`https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Value` format)`` The return value of the expression |
| `count` | `integer` The number of times that expression returned. |