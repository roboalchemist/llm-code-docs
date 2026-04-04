# Source: https://www.apollographql.com/docs/apollo-server/testing/testing.md

# Source: https://www.apollographql.com/docs/react/api/react/testing.md

# Source: https://www.apollographql.com/docs/react/development-testing/testing.md

# Source: https://www.apollographql.com/docs/graphos/connectors/testing.md

# Connectors Testing Framework

The Connectors Testing Framework is a testing automation tool for Connectors to ensure that API changes don't break your current implementation.

Test suites are YAML files in the `./tests/` directory with the `.connector.yml` extension. Each test suite can have multiple test cases, and each test case can target a different Connector in your schema.

```text
.
└── tests/
    ├── test-a.connectors.yaml
    ├── test-b.connectors.yaml
    └── ...
```

## Usage

```shell
rover connector test
```

[See all available CLI options](https://www.apollographql.com/docs/graphos/connectors/tooling/cli-tools#rover-connectors-test).

## Test suite example

```yaml title=tests/my_test_suite.connector.yml
config:
  schema: path/to/schema.graphql

tests:
  - name: Get Slideshow
    connector: Query.slideshow
    apiResponseBody: |
      {"data": {"author":"Yours Truly","title":"Sample Slide Show","slides":["Wake up to WonderWidgets!","Overview"]}}
    expect:
      connectorRequest:
        method: GET
        url: http://my-url.com/path/segments
      connectorResponse: |
        {"author":"Yours Truly","title":"Sample Slide Show","slides":["Wake up to WonderWidgets!","Overview"]} 
```

## Test suites

A test suite contains two main blocks:

* `config`: the test suite configuration, where you name the test suite and define the path to the schema
* `tests`: the test cases, where you define the assertions for Connector requests and responses

```yaml title=tests/my_test_suite.connector.yml
# Test suite configuration
config:
  # Path to the GraphQL schema. Can also be provided in the CLI using `--schema-file`
  schema: fixtures/schema.graphql
  # Test suite name. If omitted, defaults to the YAML file relative path.
  name: "my_test_suite_name"

# Array of test cases
tests:
  - # Some test case
```

If a path is absolute, for example, it starts with `/` on Unix or `C:/` on Windows, the tool uses it directly. If a path is relative, it's resolved from the project's root directory.

## Test cases

Test cases are the building blocks of a test suite and contain the following sections:

* `name`: the name of the test case. Required.
* `connector`: the target Connector, defined using the Connector ID or the Connector coordinates. See [Connector IDs](https://www.apollographql.com/docs/graphos/connectors/tooling/cli-tools#connector-ids) for more information. Required.
* `skip`: a Boolean to indicate if you want to skip this specific test case. Defaults to `false`.
* `variables`: the variables the Connector uses to make requests. See [Variables documentation](https://www.apollographql.com/docs/graphos/connectors/mapping/variables) for more information.
* `apiResponseBody` or `apiResponseBodyFile`: the API response body to pass to the Connector. Use `apiResponseBody` to include a simple response body inline, or `apiResponseBodyFile` for a path to a file for more complex responses.
* `apiResponseHeaders`: the API response headers to pass to the Connector.
* `status`: the API response status to pass to the Connector.
* `expect`: the expectations and assertions for the target Connector.

```yaml
# Array of test cases
tests:
    # Generic test name to display. Required.
  - name: ShouldGreetWithArgName

    # The target Connector, defined using the Connector ID or the Connector coordinates. Required.
    connector: query_helloWorld

    # Skips test case and all its expectations. Defaults to `false`.
    skip: true

    # Any variables needed for the Connector
    variables:

      # variables map under `$args`
      $args:
        name: "Name to greet"

      # variables map under `$context`
      $context:
        key: value

      # variables map under `$this`
      $this:
        key: value

      # variables array of maps under `$batch`
      $batch:
        - id: product-id

      # variables map under `$config`
      $config:
        key: value

      # variables map under `$request.headers`
      $requestHeaders:
        key: value

    ### API Responses ###
    ## Mock responses expected by the Connector.
    ## Use either `apiResponseBody` or `apiResponseBodyFile`. If either are missing, `apiResponseBody` will be set to `Json::null`, with no response mapping guarantees.

    # Mock API response body. Use this when the API response body is simple.
    apiResponseBody: |
        {
          "greeting": "Hello Some Name"
        }

    # Mock API response body file. Use this when the API response body is complex or too large for the YAML file.
    apiResponseBodyFile: fixtures/mocks/responseFile.json

    # Any necessary response headers from the Mock API. Optional.
    apiResponseHeaders:
      content-type: application/json; charset=utf-8

    # Response status, used to check if `is_success` field is correct. Optional. Defaults to `200`.
    status: 200

    ### Test Expectation ###
    expect: # Test expectations
```

## Test expectations

Define expectations for Connector request, response, problems, and errors in the `expect` block of a test case.

### Connector request

You can define Connector request expectations in the following ways:

* Descriptive form, where you identify each parameter of the request
* URL based request
* Using the results from [analyzed](https://www.apollographql.com/docs/graphos/connectors/tooling/cli-tools#rover-connectors-analyze) data request

#### Descriptive form

In this format, you identify each parameter of the Connector request explicitly.

```yaml
    connectorRequest:
        # Checks if the HTTP::Method called is as expected. Optional. Defaults to `GET`
        method: GET

        # Expected request body. Use `body` for simple requests
        body: |
          <Some request body>
        # Expected request body file. Use `bodyFile` for complex requests that need to be stored in a file
        bodyFile: path/to/requestBody.json

        ## The following fields are used to verify if the called URI is as expected.

        # URI scheme. Optional. Defaults to `http`
        scheme: https

        # URL. Optional. Defaults to `localhost:8080`
        origin: jsonplaceholder.typicode.com

        # URI Path, Optional. Defaults to `/`
        path: /greeting

        # URI query params. Optional. Defaults to empty.
        queryParams:
          name: "Some Name"

        # Verifies expected request headers. Optional.
        headers:
          "content-type": "application/json; charset=utf-8"
```

#### URL based request

```yaml
    connectorRequest:
        # Checks if the HTTP::Method called is as expected. Optional. Defaults to `GET`
        method: GET

        # Expected request body. Use `body` for simple requests
        body: |
            <Some request body>
        # Expected request body file. Use `bodyFile` for complex requests that need to be stored in a file
        bodyFile: path/to/requestBody.json

        # Specifies the URL of the request
        url: https://jsonplaceholder.typicode.com/greeting?name=SomeName

        # Verifies expected request headers. Optional.
        headers:
            "content-type": "application/json; charset=utf-8"
```

#### Using the results from `rover connector analyze`

You need an analysis to use this format. See [Analyze Connector requests](https://www.apollographql.com/docs/graphos/connectors/tooling/cli-tools#rover-connectors-analyze) for more information.

```yaml
    # Uses all the data in the analyze `.http` to create a mock expectation.
    # Use this for complex requests
    connectorRequestHttp: "path/to/analyzed/request/<id>_request.http"
```

### Connector response

The Connector response is optional. You can define it inline or in a file. You can also define optional response headers.

```yaml
      # Use `connectorResponse` for simple responses
      connectorResponse: '{"helloWorld":{"greeting":"Name to greet"}}'
      # Use `connectorResponseFile` for complex/large responses
      connectorResponseFile: "path/to/analyzed/request/<id>_response.json"
      # Verifies expected response headers. Optional. Defaults to empty.
      connectorResponseHeaders:
        "content-type": "application/json; charset=utf-8"
```

### Connectors errors and problems

Errors are standard GraphQL [`errors` output](https://graphql.org/learn/response/#errors), which can be request errors, field errors, or network errors.

Problems are issues in the Connector that occurred during selection mapping, including runtime issues such as missing fields, or incorrect method arguments.

You can define expectations for errors and problems by matching the full message string using `message` or matching partially with a substring using `contains_message`.

#### Matching the full message string

```yaml
      # Vec of `{message: String, path: String}`. Optional.
      problems:
          # Match the full message string
        - message: "my message"
          # Path to the field that caused the problem. Optional.
          path: "path"

      # Vec of `{message: String, extensions: IndexMap<String, JSON>}`. Optional.
      errors:
          # Match the full message string
        - message: Request failed
          # Emits a warning in Verbose mode if this differs from the asserted value. Optional.
          extensions:
            code: CONNECTOR_FETCH
            service: test_connector
            connector:
              coordinate: test_connector:Query.helloWorld[0]
```

#### Matching a substring of the message string

```yaml
      # Vec of `{message: String, path: String}`. Optional.
      problems:
          # Check if message contains a substring (`message` always supersedes `contains_message`)
        - contains_message: "some substring"
          # Path to the field that caused the problem. Optional.
          path: "path"

      # Vec of `{message: String, extensions: IndexMap<String, JSON>}`. Optional.
      errors:
          # Check if message contains a substring (`message` always supersedes `contains_message`)
        - contains_message: "some substring"
          # Emits a warning in Verbose mode if this differs from the asserted value. Optional.
          extensions:
            code: CONNECTOR_FETCH
            service: test_connector
            connector:
              coordinate: test_connector:Query.helloWorld[0]
```

If any Connector contains an unexpected `Problem` or `Error`, an assertion fails. For example: `GraphQL::Error::UNEXPECTED`.

## Current limitations

* The Connector Testing Framework only supports JSON and plaintext requests and responses.
* It doesn't support non-JSON values in the `body` field.
* Variables only support string values

## Full test suite example

```yaml
# Test suite configuration
config:
  # Path to the GraphQL schema. Can also be provided in the CLI using `--schema-file`
  schema: path/to/schema.graphql
  # Test suite name. If omitted, defaults to the YAML file relative path.
  name: "my_test_suite_name"

# Array of test cases
tests:
  # The name of the test case. Required.
  - name: ShouldGreetWithArgName

    # The target Connector, defined using the Connector ID or the Connector coordinatesRequired.
    connector: Query.helloWorld

    # Skips test case and all its expectations. Defaults to `false`.
    skip: false

    # Any variables needed for the Connector
    variables:
      # variables map under `$args`
      $args:
        name: "Name to greet"
      # variables map under `$context`
      $context:
        key: value
      # variables map under `$this`
      $this:
        key: value
      # variables array of maps under `$batch`
      $batch:
        - id: product-id
      # variables map under `$config`
      $config:
        key: value
      # variables map under `$request.headers`
      $requestHeaders:
        key: value

    ### API Responses ###
    ## Mock responses expected by the Connector.
    ## Use either `apiResponseBody` or `apiResponseBodyFile`. If either are missing, `apiResponseBody` will be set to `Json::null`, with no response mapping guarantees.

    # Mock API response body. Use this when the API response body is simple.
    apiResponseBody: |
        {
          "greeting": "Hello Name to greet"
        }
    
    ### OR ###
    
    # Mock API response body file. Use this when the API response body is complex or too large for the YAML file.
    apiResponseBodyFile: fixtures/mocks/responseFile.json

    # Any necessary response headers from the Mock API. Optional.
    apiResponseHeaders:
      content-type: application/json; charset=utf-8

    # Response status, used to check if `is_success` field is correct. Optional. Defaults to `200`.
    status: 200

    ### Test Expectation ###
    expect:
      # Uses all the data in the analyze `.http` to create a mock expectation.
      # Use this for complex requests
      connectorRequestHttp: "path/to/analyzed/request/00000000-0000-0000-0000-000000000000_request.http"

      ### OR ###

      # Connector request expectations
      connectorRequest:
        # Checks if the HTTP method called is as expected. Optional. Defaults to `GET`
        method: GET
        # Expected request body. Use `body` for simple requests
        body: |
          <Some request body>
        
        ### OR ###
        # Expected request body file. Use `bodyFile` for complex requests that need to be stored in a file
        bodyFile: path/to/requestBody.json

        ### OR ###

        # Specifies the URL of the request
        url: https://jsonplaceholder.typicode.com/greeting?name=Name to greet

        ### OR ###

        # URI components for building the expected request URL
        # URI scheme. Optional. Defaults to `http`
        scheme: https
        # URL origin. Optional. Defaults to `localhost:8080`
        origin: jsonplaceholder.typicode.com
        # URI path. Optional. Defaults to `/`
        path: /greeting
        # URI query params. Optional. Defaults to empty.
        queryParams:
          name: "Name to greet"
        # Verifies expected request headers. Optional.
        headers:
          "content-type": "application/json; charset=utf-8"

      # Use `connectorResponseFile` for complex/large responses
      connectorResponseFile: fixtures/expected/some_response_file.json

      ### OR ###

      # Use `connectorResponse` for simple responses
      connectorResponse: '{"helloWorld":{"greeting":"Name to greet"}}'

      # Verifies expected response headers. Optional. Defaults to empty.
      connectorResponseHeaders:
        "content-type": "application/json; charset=utf-8"

      # Asserts problems related to Connectors request and response. Optional.
      # Vec of `{message: String, path: String}`
      problems:
          # Match the full message string
        - message: "my message"
          # Check if message contains a substring (`message` always supersedes `contains_message`)
          contains_message: "some substring"
          # Optional
          path: "path"

      # Asserts errors related to Connectors request and response. Optional.
      # Vec of `{message: String, extensions: IndexMap<String, JSON>}`
      errors:
          # Match the full message string
        - message: Request failed
          # Check if message contains a substring (`message` always supersedes `contains_message`)
          contains_message: "some substring"
          # Optional field and will emit a warning in Verbose mode if they differ from the asserted value or are present.
          extensions:
            code: CONNECTOR_FETCH
            service: test_connector
            connector:
              coordinate: test_connector:Query.helloWorld[0]
```

## Defining shared configurations across test cases

If your tests have shared configuration values, you can define a `config.common` property. This helps avoid defining the same values in each test case. All fields in `common` are optional.

When a common value is present in the test case, it replaces the common value. For example, if you define a `common` value for `variables.$args`, and a test case defines a value for `variables.$args`, the test case value replaces the common value.

For structured data such as `headers`, the tool appends the common data instead of replacing it.

```yaml
config:
  schema: path/to/schema.graphql
  common: # Set of common test case configuration for this test suite
    connector: helloworld
    variables:
      $args: # only used if test case `variables.$args` is empty or not present
        key: value
      $context: # only used if test case `variables.$context` is empty or not present
        key: value
      $this: # only used if test case `variables.$this` is empty or not present
        key: value
      $batch: # only used if test case `variables.$batch` is empty or not present
        - id: some-id
      $config: # only used if test case `variables.$config` is empty or not present
        key: value
      $requestHeaders: # only used if test case `variables.$requestHeaders` is empty or not present
        key: value
    apiResponseBody: | # can be overridden by test case `apiResponseBody`
        <some body>
    apiResponseBodyFile: path/to/api/responseBody.json # can be overridden by test case `apiResponseBodyFile`
    apiResponseHeaders: # can be overridden by test case `apiResponseHeaders`
      content-type: application/json; charset=utf-8
    status: 200 # can be overridden by test case `status`
    expectedResponseFile: path/to/expectedResponse.json # can be overridden by test case `expected.connectorResponseFile`
    expectedResponse: | # can be overridden by test case `expected.connectorResponse`
      <some response>
    expectedRequestMethod: PUT # can be overridden by test case `expected.connectorRequest.method`
    ### URI ###
    expectedRequestScheme: https # can be overridden by test case `expected.connectorRequest.scheme`
    expectedRequestOrigin: localhost:8080 # can be overridden by test case `expected.connectorRequest.origin`
    expectedRequestPath: /greeting # can be overridden by test case `expected.connectorRequest.path`
    expectedRequestQueryParams: # can be overridden by test case `expected.connectorRequest.queryParams`
      # only used if test case `expected.connectorRequest.queryParams` is empty or not present
      key: "value"

    ### OR ###
    # If you prefer using a full URI
    expectedRequestUrl: https://localhost:8080/greeting?key=value

tests:
  - name: Should map the greeting including the provided name
    expect:
      connectorRequest:
        method: GET # overrides `expectedRequestMethod`
        origin: someurl.com # overrides `expectedRequestOrigin`

```

## More examples

```yaml
config:
  schema: fixtures/schema.graphql

tests:
  - name: GreetsWithProperName
    connector: helloworld
    variables:
      $args:
        name: Some Name
      $context:
        key: value
    apiResponseBody: |
        {
          "greeting": "Hello Some Name"
        }
    apiResponseHeaders:
      content-type: application/json; charset=utf-8
    status: 200
    expect:
      connectorRequest:
        method: GET
        scheme: https
        origin: jsonplaceholder.typicode.com
        path: /greeting
        queryParams:
          name: "Some Name"
      connectorResponse: |
        {
           "greeting": "Hello Some Name"
        }
      connectorResponseHeaders:
        "content-type": "application/json; charset=utf-8"
```

```graphql
extend schema
  @link(url: "https://specs.apollo.dev/federation/v2.11", import: ["@key"])
  @link(url: "https://specs.apollo.dev/connect/v0.2", import: ["@connect", "@source"])        
  @source(name: "myApi", http: { baseURL: "https://jsonplaceholder.typicode.com" } )

type Query {
  helloWorld(name: String): String
  @connect(
    id: "helloworld"
    source: "myApi"
    errors: {
      message: """$("a custom error message")"""
    }
    http: { GET: "/greeting?name={$args.name}"}
    selection: """
    greeting
    """
  )
}
```

```yaml
config:
  schema: tests/schema.graphql

tests:
  - name: FromCurlGenerated
    connector: slideshow_by_name
    variables:
      $args:
        name: Your-Name
      $config:
        user_key: 123
    apiResponseBodyFile: "path/to/analyzed/request/00000000-0000-0000-0000-000000000000_body.json"
    expect:
      connectorRequestHttp: "path/to/analyzed/request/00000000-0000-0000-0000-000000000000_request.http"
      connectorResponse: '{"author":"Yours Truly","title":"Sample Slide Show","slides":["Wake up to WonderWidgets!","Overview"]}'
```

Based on [generated](https://www.apollographql.com/docs/graphos/connectors/tooling/cli-tools#rover-connectors-generate) schema:

```graphql
extend schema
  @link(url: "https://specs.apollo.dev/federation/v2.10", import: ["@key"])
  @link(url: "https://specs.apollo.dev/connect/v0.2", import: ["@source", "@connect"])
  @source(
    name: "httpbin"
    http: {
      baseURL: "https://httpbin.org/"
    }
  )

type Mutation {
  json(name: String): Json @connect(
    source: "httpbin"
    id: "slideshow_by_name"
    http: {
      GET: "json?name={$args.name}"
      headers: [
        { name: "accept", value: "{$config.accept}" }
        { name: "x-user", value: "{$config.user}" }
      ]
    }
    selection: """
      accessControlAllowOrigin: {$request.headers.'access-control-allow-origin'->first}
      accessControlAllowCredentials: {$request.headers.'access-control-allow-credentials'->first}
      slideshow {
        author
        date
        slides
        title
      }

    """
  )
}

type Slides {
  title: String
  type: String
  items: [String]
}

type Slideshow {
  author: String
  date: String
  slides: [Slides]
  title: String
}

type Json {
  accessControlAllowOrigin: String
  accessControlAllowCredentials: String
  slideshow: Slideshow
}
```

Test Suite:

```yaml
config:
  schema: schemas/schema.graphql
  name: mapping_problems

tests:
  - name: Should Handle Mapping Problems
    connector: helloworld
    variables:
      $args:
        name: Some Name
      $context:
        key: value
    apiResponseBody: |
      {
        "randomField": "Hello Some Name"
      }
    apiResponseHeaders:
      content-type: application/json; charset=utf-8
    status: 200
    expect:
      connectorRequest:
        method: GET
        scheme: https
        origin: jsonplaceholder.typicode.com
        path: /greeting
        queryParams:
          name: "Some Name"
      connectorResponse: '{}'
      problems:
        - message: "my message"
          path: "path"
```

> For `tests/cases/mapping_problems.connector.yml`

```sh
TEST SUITE: mapping_problems - SCHEMA: schemas/schema.graphql
TEST CASE: Should Handle Mapping Problems @helloworld
[SUCCESS]: HTTP::Request::Method Should Handle Mapping Problems@helloworld
[SUCCESS]: HTTP::Request::URI Should Handle Mapping Problems@helloworld
[SUCCESS]: HTTP::Response::Status: 200 Should Handle Mapping Problems@helloworld
[SUCCESS]: HTTP::Response::Body Should Handle Mapping Problems@helloworld
[FAILURE]: Expected GraphQL::Problem NOT FOUND N°1 Should Handle Mapping Problems@helloworld
- Message: {"message":"my message","path":"path"}
[FAILURE]: UNMATCHED GraphQL::Problem Occurred N°1 Should Handle Mapping Problems@helloworld
- Message: {"message":"Property .greeting not found in object","path":"greeting","count":1,"location":"Selection"}

FAILURES:

TEST SUITE: mapping_problems

TEST CASE Should map the greeting including the provided named
[FAIL]: Expected GraphQL::Problem NOT FOUND
Message: {"message":"my message","path":"path"}
[FAIL]: UNMATCHED GraphQL::Problem Occurred
Message: {"message":"Property .greeting not found in object","path":"greeting","count":1,"location":"Selection"}
TEST RESULTS: FAILED 4 passed; 2 failed; 0 skipped
```
