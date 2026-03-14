# Source: https://docs.airbyte.com/platform/connector-development/config-based/understanding-the-yaml-file/request-options.md

# Source: https://docs.airbyte.com/platform/2.0/connector-development/config-based/understanding-the-yaml-file/request-options.md

# Source: https://docs.airbyte.com/platform/1.8/connector-development/config-based/understanding-the-yaml-file/request-options.md

# Source: https://docs.airbyte.com/platform/1.7/connector-development/config-based/understanding-the-yaml-file/request-options.md

# Source: https://docs.airbyte.com/platform/1.6/connector-development/config-based/understanding-the-yaml-file/request-options.md

# Request Options

Copy Page

The primary way to set request parameters and headers is to define them as key-value pairs using a `RequestOptionsProvider`. Other components, such as an `Authenticator` can also set additional request params or headers as needed.

Additionally, some stateful components use a `RequestOption` to configure the options and update the value. Example of such components are [Paginators](/platform/1.6/connector-development/config-based/understanding-the-yaml-file/pagination.md) and [DatetimeBasedCursors](/platform/1.6/connector-development/config-based/understanding-the-yaml-file/incremental-syncs.md#DatetimeBasedCursor).

## Request Options Provider[​](#request-options-provider "Direct link to Request Options Provider")

The primary way to set request options is through the `Requester`'s `RequestOptionsProvider`. The options can be configured as key value pairs:

Schema:

```
RequestOptionsProvider:
  type: object
  anyOf:
    - "$ref": "#/definitions/InterpolatedRequestOptionsProvider"
InterpolatedRequestOptionsProvider:
  type: object
  additionalProperties: true
  properties:
    "$parameters":
      "$ref": "#/definitions/$parameters"
    request_parameters:
      "$ref": "#/definitions/RequestInput"
    request_headers:
      "$ref": "#/definitions/RequestInput"
    request_body_data:
      "$ref": "#/definitions/RequestInput"
    request_body_json:
      "$ref": "#/definitions/RequestInput"
```

Example:

```
requester:
  type: HttpRequester
  url_base: "https://api.exchangeratesapi.io/v1/"
  http_method: "GET"
  request_options_provider:
    request_parameters:
      k1: v1
      k2: v2
    request_headers:
      header_key1: header_value1
      header_key2: header_value2
```

It is also possible to configure add a json-encoded body to outgoing requests.

```
requester:
  type: HttpRequester
  url_base: "https://api.exchangeratesapi.io/v1/"
  http_method: "GET"
  request_options_provider:
    request_body_json:
      key: value
```

### Request Option Component[​](#request-option-component "Direct link to Request Option Component")

Some components can be configured to inject additional request options to the requests sent to the API endpoint.

Schema:

```
RequestOption:
  description: A component that specifies the key field and where in the request a component's value should be inserted into.
  type: object
  required:
    - type
    - inject_into
  properties:
    type:
      type: string
      enum: [RequestOption]
    inject_into:
      enum:
        - request_parameter
        - header
        - body_data
        - body_json
  oneOf:
    - properties:
      field_name:
        type: string
        description: The key where the value will be injected. Used for non-nested injection
      field_path:
        type: array
          items:
            type: string
          description: For body_json injection, specifies the nested path to the inject values. Particularly useful for GraphQL queries where values need to be injected into the variables object.
```

### GraphQL request injection[​](#graphql-request-injection "Direct link to GraphQL request injection")

For `body_json` injections, the `field_path` property is used to provide a list of strings representing a path to a nested key to inject. This is particularly useful when working with GraphQL APIs. GraphQL queries typically accept variables as a separate object in the request body, allowing values to be parameterized without string manipulation of the query itself. As an example, to inject a page size option into a GraphQL query, you might need to provide a `limit` key in the request's `variables` as:

```
page_size_option:
  request_option:
    type: RequestOption
    inject_into: body_json
    field_path:
      - variables
      - limit
```

This would inject the following value in the request body:

```
{ "variables": { "limit": value }}
```

Here's an example of what your final request might look like:

```
{
  "query": "query($limit: Int) { users(limit: $limit) { id name } }",
  "variables": {
    "limit": 10
  }
}
```

note

Nested key injection is ONLY available for `body_json` injection. All other injection types use the top-level `field_name` instead. The `field_name` field is slated to be deprecated in favor of `field_path` in the future.

### Request Path[​](#request-path "Direct link to Request Path")

As an alternative to adding various options to the request being sent, some components can be configured to modify the HTTP path of the API endpoint being accessed.

Schema:

```
RequestPath:
  description: A component that specifies where in the request path a component's value should be inserted into.
  type: object
  required:
    - type
  properties:
    type:
      type: string
      enum: [RequestPath]
```

## Authenticators[​](#authenticators "Direct link to Authenticators")

It is also possible for authenticators to set request parameters or headers as needed. For instance, the `BearerAuthenticator` will always set the `Authorization` header.

More details on the various authenticators can be found in the [authentication section](/platform/1.6/connector-development/config-based/understanding-the-yaml-file/authentication.md).

## Paginators[​](#paginators "Direct link to Paginators")

The `DefaultPaginator` can optionally set request options through the `page_size_option` and the `page_token_option`. The respective values can be set on the outgoing HTTP requests by specifying where it should be injected.

The following example will set the "page" request parameter value to the page to fetch, and the "page\_size" request parameter to 5:

```
paginator:
  type: "DefaultPaginator"
  page_size_option:
    type: "RequestOption"
    inject_into: request_parameter
    field_name: page_size
  pagination_strategy:
    type: "PageIncrement"
    page_size: 5
  page_token:
    type: "RequestOption"
    inject_into: "request_parameter"
    field_name: "page"
```

More details on paginators can be found in the [pagination section](/platform/1.6/connector-development/config-based/understanding-the-yaml-file/pagination.md).

## Incremental syncs[​](#incremental-syncs "Direct link to Incremental syncs")

The `DatetimeBasedCursor` can optionally set request options through the `start_time_option` and `end_time_option` fields. The respective values can be set on the outgoing HTTP requests by specifying where it should be injected.

The following example will set the "created\[gte]" request parameter value to the start of the time window, and "created\[lte]" to the end of the time window.

```
incremental_sync:
  type: DatetimeBasedCursor
  start_datetime: "2021-02-01T00:00:00.000000+0000",
  end_datetime: "2021-03-01T00:00:00.000000+0000",
  step: "P1D"
  start_time_option:
    type: "RequestOption"
    field_name: "created[gte]"
    inject_into: "request_parameter"
  end_time_option:
    type: "RequestOption"
    field_name: "created[lte]"
    inject_into: "request_parameter"
```

More details on incremental syncs can be found in the [incremental syncs section](/platform/1.6/connector-development/config-based/understanding-the-yaml-file/incremental-syncs.md).

## More readings[​](#more-readings "Direct link to More readings")

* [Requester](/platform/1.6/connector-development/config-based/understanding-the-yaml-file/requester.md)
* [Pagination](/platform/1.6/connector-development/config-based/understanding-the-yaml-file/pagination.md)
* [Incremental Syncs](/platform/1.6/connector-development/config-based/understanding-the-yaml-file/incremental-syncs.md)
