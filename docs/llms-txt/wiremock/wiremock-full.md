# Wiremock Documentation

Source: https://docs.wiremock.io/llms-full.txt

---

# Advanced Stubbing
Source: https://docs.wiremock.io/advanced-stubbing

Advanced request matching, using query, header and body matching with regexes, JSONPath, XPath and others.

In some cases matching on the URL alone is not specific enough. For instance you may want to simulate creation of a new
to-do item in a RESTful API by stubbing `POST` to `/api/to-do`. In order to test both success and failure cases it will be
necessary to return different responses depending on the post body (since the URL would always be the same).

We can do this by adding a body matching clause in the Advanced portion of the Request section.

Click the button to add the clause, select the match type from the drop-down, then write (or paste) the expected value or expression into the text area.

If your API uses JSON as its serialisation format you might want to match using `equalToJson`:

<img title="Advanced" />

For quick reference, here are the options available to you:

* ***Equals*** - matches if the request body is equal to the expected body
* ***Matches Regex*** - matches if the request body matches the specified regex
* ***Does Not Match Regex*** - matches if the request body does not match the specified regex
* ***Contains*** - matches if the request body contains the expected body
* ***Equals XML*** - matches if the request body is equal to the expected XML
* ***Matches XPath*** - matches if the request body matches the specified XPath
* ***Equals JSON*** - matches if the request body is equal to the expected JSON
* ***Matches JSONPath*** - matches if the request body matches the specified JSONPath
* ***Matches JSON Schema*** - matches if the request body matches the specified JSON schema
* ***Is Absent*** - matches if the request body is absent

**Note** that the `NOT` checkbox can be used to negate the selected matcher.

## Request method matching

The HTTP method that required for this stub to match. This defaults to `ANY`, meaning that a request with any method
will match.

## Request priority matching

Requests of a higher priority (i.e. lower number) will be matched first, in cases where more than one stub mapping in the
list would match a given request.

Normally it's fine to leave the priority at its default. However it can sometimes be useful to so create a low priority,
broadly matching stub defining some default behaviour e.g. a 404 page, and then create a set of higher priority, more specific
stubs for testing individual cases. See [Serving Default Responses](/default-responses/) for more details.

## URL matching

Determines how the URL will be matched. The options are:

* **Path and query** - exactly matches the path and query string parts of the URL
* **Path and query regex** - matches the path and query string parts of the URL against a regular expression
* **Path** - exactly matches the path part of the URL
* **Path regex** - matches the path part of the URL against a regular expression
* **Any URL** - matches any URL

<img title="URL match types" />

## Advanced - Query parameters, headers and more

In addition to the URL and body, requests can be matched on:

* Headers
* Query parameters
* Cookies

Parameter match clauses can use the same set of match operations as body clauses:

<img title="Request parameters" />

It's usually a good idea to use path only URL matching with query parameter matches.

When multiple match clauses are added a request must match all of them for the response to be served (they are combined
with logical AND).

### Logical AND OR matchers

You can build complex logic using AND OR operators for Headers, Query parameters, Cookies, Form parameters and Path parameters.

These operators can be nested to help build realistic matching logic into your stubs.

<img title="OR predicate" />

## Matching JSON request bodies

Two specific match types exist for JSON formatted request bodies: equality (`equalToJson`) and JSONPath (`matchesJsonPath`).

### Equality

`equalToJson` performs a semantic comparison between the incoming JSON and the expected value, meaning that
it will return a match even when, for instance, the two documents have different amounts of whitespace.

You can also specify that array order an additional elements in the request JSON be ignored.

<img title="JSON equality" />

### JSON Placeholders

JSON equality matching is implemented by [JsonUnit](https://github.com/lukas-krecan/JsonUnit), and
therefore supports placeholder syntax, allowing looser specification of fields within the document.

For instance, consider a request body like this, where `transaction_id` is unique to
each request:

```json theme={null}
{
  "event": "details-updated",
  "transaction_id": "abc-123-def"
}
```

Requiring an exact match on this document would ensure no match could ever be made, since
the same transaction ID would never be repeated.

This can be solved using a placeholder:

```json theme={null}
{
  "event": "details-updated",
  "transaction_id": "${json-unit.ignore}"
}
```

If you want to constrain the value to a specific type or pattern the following placeholders are also valid:

* `${json-unit.regex}[A-Z]+` (any Java-style regular expression can be used)
* `${json-unit.any-string}`
* `${json-unit.any-boolean}`
* `${json-unit.any-number}`

### JSONPath

`matchesJsonPath` allows request bodies to be matched according to a [JSONPath](https://github.com/json-path/JsonPath) expression. The
JSONPath expression is used to select one or more values from the request body, then the result is matched against sub-matcher (`equal to`, `contains` etc.).
It is also possible to simply assert that the expression returns something, by selecting `is present` from the list.

<img title="JSONPath matching" />

The expression in the above screenshot (`$.event` `equal to` `description-updated`) would match a request body of

```json theme={null}
{
  "event": "description-updated"
}
```

but not

```json theme={null}
{
  "event": "document-created"
}
```

## Matching XML request bodies

As with JSON matching, there are two match types available for working with XML: `equalToXml` and `matchesXPath`.

### Equality

`equalToXml` performs a semantic comparison between the incoming and expected XML documents, meaning that it will return a match regardless of whitespace, comments and node order.

### XML placeholders

When using `equalToXml` it is possible to ignore the value of specific elements using [XMLUnit](https://github.com/xmlunit/user-guide/wiki/Placeholders)'s placeholder syntax. For instance if you
expected to receive an XML request body containing a transaction ID that changed on every request you could ignore that value like this:

```xml theme={null}
<transaction>
  <id>${xmlunit.ignore}</id>
  <value>1234</value>
</transaction>
```

To use XML placeholders you must enable them by ticking the box:

<img title="Enable XML placeholders" />

### XPath

`matchesXPath` allows XML request bodies to be matched according to an [XPath](https://www.w3schools.com/xml/xpath_syntax.asp) expression.

For instance, an XML request body like

```xml theme={null}
<stuff>
  <id>abc123</id>
</stuff>
```

could be matched using the XPath expression

```
//stuff[id='abc123']
```

## Setting the response status

The HTTP status code to be sent with the response.

## Sending response headers

Headers can be set on the response:

<img title="Response headers" />

## Response body

A response body can optionally be specified. If [response templating](/response-templating/)
is enabled, certain parts can be dynamically generated using request attributes and random data.


# WireMock Cloud AI
Source: https://docs.wiremock.io/ai-mcp/ai-101

API simulation tools for AI-assisted development workflows

WireMock Cloud provides API simulation capabilities that integrate with AI development tools through the Model Context Protocol (MCP). This enables AI assistants to create, manage, and test against mock APIs directly within your development environment.

## Key Capabilities

**API Simulation**\
Create mock APIs from existing code, OpenAPI specifications, or natural language descriptions using AI assistance.

**Codebase Integration**\
Generate mocks that reflect your existing API patterns and data structures by analyzing your codebase.

**Testing with AI Agents**\
Allow AI coding assistants to validate generated code by testing against realistic mock responses.

**Independent Development**\
Work on features that depend on APIs still in development by creating temporary mock implementations.

## Installation

Install the WireMock CLI and configure your AI tool:

1. Install the CLI: `npm i -g @wiremock/cli`
2. Log in: `wiremock login`
3. Configure MCP integration

[**View Full Installation Guide →**](/ai-mcp/installation)

## Supported Tools

WireMock integrates with AI development environments via the Model Context Protocol:

<div>
  <div>
    <img alt="Cursor" />

    <span>Cursor</span>
  </div>

  <div>
    <img alt="VS Code" />

    <span>VS Code</span>
  </div>

  <div>
    <div>C</div>
    <span>Claude</span>
  </div>

  <div>
    <img alt="GitHub" />

    <span>Copilot</span>
  </div>
</div>

Compatible with: Cursor, VS Code, Claude Code, Claude Desktop, GitHub Copilot, Augment, Windsurf, and other MCP-compatible tools.

[**View All Available Tools →**](/ai-mcp/mcp-tools)

## Use Cases

<div>
  <div>
    <h3>Creating Stateful Mock APIs</h3>
    <p>Transform static mock APIs into dynamic, stateful versions that maintain state between requests. AI assists in validating mock behavior as it evolves, enabling realistic simulation of complex API interactions and multi-step workflows.</p>
    <p><a href="https://www.youtube.com/watch?v=lS7Ytj2GkUo">📺 Watch: Converting Static APIs to Dynamic</a></p>
  </div>

  <div>
    <h3>API Discovery and Documentation</h3>
    <p>Use AI to explore and document undocumented APIs by automatically discovering endpoints, analyzing responses, and generating comprehensive documentation. This is especially valuable when working with legacy systems or third-party APIs.</p>
    <p><a href="https://www.youtube.com/watch?v=ogK6_7FYxv0">📺 Watch: AI-Powered API Exploration</a></p>
  </div>

  <div>
    <h3>Mock Drift Detection</h3>
    <p>Detect and resolve discrepancies between mock APIs and their OpenAPI specifications using AI assistance. Automatically identify when mocks drift from intended behavior and update them to maintain consistency with API contracts.</p>
    <p><a href="https://www.youtube.com/watch?v=kvDyXbKBJDE">📺 Watch: Resolving Mock Drift</a></p>
  </div>

  <div>
    <h3>GraphQL API Behavior Definition</h3>
    <p>Prototype a GraphQL API schema, instantly simulate it then refine its data and improve realism.</p>
    <p><a href="https://www.youtube.com/watch?v=e8fI4ZjYwVM">📺 Watch: GraphQL API with AI</a></p>
  </div>

  <div>
    <h3>API Dependency Isolation</h3>
    <p>Generate mock endpoints for your application's API dependencies and swap real APIs for mocks during development and testing. This enables isolated development without external service dependencies, improving reliability and reducing development costs.</p>
    <p><a href="https://www.youtube.com/watch?v=JHcbFhFbBCY">📺 Watch: Swapping APIs for Mocks</a></p>
  </div>

  <div>
    <h3>AI-Driven API Prototyping</h3>
    <p>Leverage AI agents to prototype APIs that don't yet exist, allowing teams to develop against future services before backend implementation. Create realistic endpoint behaviors and response patterns to unblock frontend development and testing workflows.</p>
    <p><a href="https://www.youtube.com/watch?v=usBZNA4Zc7c">📺 Watch: API Prototyping with AI</a></p>
  </div>

  <div>
    <h3>Authenticated HTTP Requests</h3>
    <p>Configure automatic authentication for AI-driven HTTP requests without exposing credentials to the language model. Set up domain-based authentication with OAuth, API keys, or custom headers to enable secure API exploration and testing workflows.</p>
    <p><a href="/ai-mcp/http-request-authentication">🔐 Learn: HTTP Request Authentication</a></p>
  </div>
</div>

## Webinars

<div>
  <div>
    <iframe title="WireMock AI Webinar" />
  </div>

  <div>
    <iframe title="WireMock AI Deep Dive" />
  </div>
</div>


# HTTP Request Authentication
Source: https://docs.wiremock.io/ai-mcp/http-request-authentication

Authenticating HTTP requests made with the `make_http_request` MCP tool using authenticators

## Overview

The `make_http_request` tool in WireMock CLI provides automatic authentication support for HTTP requests through configurable authenticators.
This allows AI agents to make authenticated HTTP calls without credentials being visible to the LLM.

This is most useful when using an AI plus WireMock MCP to explore or "crawl" an API, recording it in order
to create a mock API and OpenAPI description.

For instance, if you wanted to automate the exploration of an internal microservice's API you would first add an authenticator to your configuration file, start your AI tool, then instruct it to start
crawling the API.

## How Authentication Works

1. **Domain-based Matching**: When making an HTTP request, the tool extracts the domain and port from the target URL
2. **Authenticator Lookup**: It searches for a matching authenticator configuration based on the domain
3. **Automatic Header Injection**: If a matching authenticator is found, the appropriate authentication header is automatically added to the request
4. **Request Execution**: The request is executed with the authentication header included

### Domain Matching Format

The domain matching key follows this format:

* `hostname:port` for non-standard ports (e.g., `api.example.com:8443`)
* `hostname` for standard ports (e.g., `api.example.com` for HTTPS on port 443)

## Configuration Format

Authentication configurations are stored in the `config.yaml` configuration file under your home directory, in the `authenticators` section.

### Configuration File Location

The configuration file is located at:

* **macOS/Linux**: `~/.wiremock/config.yaml`
* **Windows**: `%USERPROFILE%\.wiremock\config.yaml`

### Basic Structure

```yaml theme={null}
authenticators:
  "api.example.com":
    type: "header_token"
    headerName: "Authorization"
    prefix: "Bearer"
    token: "your-secret-token"
  
  "internal-api.company.com:8080":
    type: "header_token"
    headerName: "x-api-key"
    prefix: "Token"
    token: "very-secret-123"
```

## Supported Authenticator Types

### 1. Header Token Authenticator

The most common authentication method using a static token in a header.

**Type**: `header_token`

**Configuration Parameters**:

* `headerName` (string): The name of the HTTP header (e.g., "Authorization", "X-API-Key")
* `prefix` (string): Optional prefix for the token value (e.g., "Bearer", "Token")
* `token` (string): The authentication token value

**Example Configuration**:

```yaml theme={null}
authenticators:
  "api.example.com":
    type: "header_token"
    headerName: "Authorization"
    prefix: "Bearer"
    token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  
  "api.service.com":
    type: "header_token"
    headerName: "X-API-Key"
    prefix: ""
    token: "sk-1234567890abcdef"
```

**Generated Header Examples**:

* With prefix: `Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`
* Without prefix: `X-API-Key: sk-1234567890abcdef`


# Installing WireMock Cloud AI
Source: https://docs.wiremock.io/ai-mcp/installation

How to install the WireMock Cloud MCP server and integrate it with your AI tool

This guide walks you through configuring the MCP (Model Context Protocol) server necessary to natively use WireMock Cloud from an MCP-compatible AI tool such as Cursor or Claude Desktop.

This enables automatic API discovery, mocking and test abstraction from any codebase as part of prompt-driven development with your chosen AI tool.

Additionally, it enables you to skip the complexity of building out new services early on - which can hamper the rapid development by introducing more failure points - and instead use simulated APIs on WireMock to prototype new capabilities with less system overhead.

**Note** that while this article documents use with Cursor, Claude Desktop and VSCode specifically, WireMock Cloud’s MCP server will work with any AI-powered tool that supports MCP.

## Prerequisites

* Node.js 18+ (to install the CLI)
* An existing WireMock Cloud account (if you don’t have one, you can sign up during the login step)

## Step 1: Install the WireMock CLI

Install the CLI globally using npm:

```bash theme={null}
npm i -g @wiremock/cli
```

## Step 2: Log in to WireMock Cloud

If you already have a WireMock Cloud account, simply log in. Otherwise, the login process will guide you through creating an account:

```bash theme={null}
wiremock login
```

## Step 3: Configure your AI tool

<Tabs>
  <Tab title="Cursor">
    Click this button to install with Cursor:

    <a href="cursor://anysphere.cursor-deeplink/mcp/install?name=WireMock&config=eyJjb21tYW5kIjoid2lyZW1vY2sgbWNwIn0=">
      <img alt="Add WireMock MCP server to Cursor" />
    </a>

    Or, follow these instructions:

    * Open Settings->Cursor settings.
    * Navigate to MCP.
    * Click Add new MCP server.
    * In the dialog, configure your server to run this command:

    ```bash theme={null}
    wiremock mcp
    ```

    <img alt="Configure MCP server" />

    * Verify Installation by looking for the green status dot next to the MCP server and the list of tool names.

    <img alt="Verify the MCP server is active" />

    If you have an existing real API integration, you can replace it with a WireMock stub. Generate the mock from documentation, source code, or other external description formats. This enables you to test your app in isolation without depending on live services.

    ### Step 6: Confirm Your Setup

    To confirm everything is working correctly, check that you’re logged in to WireMock Cloud by running the following prompt:

    ```
    Am I logged into WireMock Cloud?
    ```

    If logged in, you’ll see your account details rather than being prompted to sign in.

    <img alt="Confirm you are logged in via the CLI" />
  </Tab>

  <Tab title="VSCode + GitHub Copilot">
    * In VSCode, open the `settings.json` file via Settings...->Settings then clicking the Open Settings (JSON) link in the top right.
    * Add the `mcp` element to the settings JSON:
      ```json theme={null}
      {
        "mcp": {
                "servers": {
                    "WireMock": {
                        "type": "stdio",
                        "command": "wiremock",
                        "args": [
                            "mcp"
                        ]
                    }
                }
            }
      }
      ```
    * Restart VSCode

    ### Step 6: Confirm Your Setup

    Open the Copilot chat window and confirm that the tools icon is present with a number above zero:

    <img alt="Copilot tools icon" />

    To confirm everything is working correctly, check that you’re logged in to WireMock Cloud by running the following prompt:

    ```
    Who am I logged into WireMock Cloud as?
    ```

    If logged in, you’ll see your account details rather than being prompted to sign in.

    <img alt="Confirm you are logged in via the CLI" />
  </Tab>

  <Tab title="Claude Code">
    * Open your terminal or command prompt.
    * Add the WireMock MCP server using the Claude CLI:

    ```bash theme={null}
    claude mcp add wiremock -- wiremock mcp
    ```

    * Verify the server was added successfully:

    ```bash theme={null}
    claude mcp list
    ```

    <img alt="Claude Code MCP install" />

    * You should see "wiremock" in the list of configured MCP servers.

    ### Step 6: Confirm Your Setup

    To confirm everything is working correctly, check that you're logged in to WireMock Cloud by running the following prompt in Claude Code:

    ```
    Am I logged into WireMock Cloud?
    ```

    If logged in, you'll see your account details:

    <img alt="Claude Code MCP success" />
  </Tab>

  <Tab title="Claude Desktop">
    * Open Settings->Developer.
    * Click Edit Config and open the config file in your preferred editor.
    * Add the WireMock MCP server to the file. The whole file will look like this if this is the first MCP server installed:

    ```json theme={null}
    {
        "mcpServers": {
        "wiremock": {
        "command": "wiremock",
        "args": [
        "mcp"
        ]
    }
    }
    }
    ```

    * Restart Claude Desktop.

    ### Step 6: Confirm Your Setup

    To confirm everything is working correctly, check that you’re logged in to WireMock Cloud by running the following prompt:

    ```
    Am I logged into WireMock Cloud?
    ```

    After confirming it is OK for Claude to use the tool, if logged in, you’ll see your account details rather than being prompted to sign in.

    <img alt="Confirm you are logged in via the CLI" />
  </Tab>

  <Tab title="Windsurf">
    * Navigate to **Windsurf Settings** > **Cascade** > **Plugins**.
    * Click **Manage plugins** to access the raw configuration.
    * Click **View raw config** to edit the `mcp_config.json` file (located at `~/.codeium/windsurf/mcp_config.json`) and add:

      ```json theme={null}
      {
        "mcpServers": {
          "wiremock": {
            "command": "wiremock",
            "args": ["mcp"]
          }
        }
      }
      ```

      * Save the configuration and press the refresh button in the Plugin Store.

      <img alt="Windsurf Manage Plugins" />

      ### Step 6: Confirm Your Setup

      To confirm everything is working correctly, check that you're logged in to WireMock Cloud by running the following prompt in Cascade:

      ```
      Am I logged into WireMock Cloud?
      ```

      If logged in, you'll see your account details rather than being prompted to sign in.
  </Tab>
</Tabs>

## Next Steps

With WireMock MCP successfully installed, you can begin creating and using mocks in your development workflow:

### Generate a new feature and mock a new API

Develop a new feature in your application that calls a fresh API. Quickly generate a WireMock stub for this API, and then wire it up to your app while in development mode.

### Swap an existing API connection for a mock

If you have an existing real API integration, you can replace it with a WireMock Cloud mock. Generate the mock from documentation, source code, or other external description formats. This enables you to test your app in isolation without depending on live services.


# MCP Tools
Source: https://docs.wiremock.io/ai-mcp/mcp-tools

Tools implemented by WireMock's MCP server

This page lists all the tools implemented by WireMock Cloud's MCP server.

## Authentication

### `who_am_i`

Returns the username with which you are currently logged into WireMock Cloud

**Input**

None

**Output**

User ID and username information

## Mock API Management

### `list_my_mock_apis`

Lists all mock APIs in WireMock Cloud that you have access to

**Input**

None

**Output**

List of mock APIs with their IDs and names

### `search_my_mock_apis`

Searches for mock APIs by text query

**Input**

`query` (string): The search query

**Output**

List of matching mock APIs

### `create_mock_api`

Creates a new mock API in WireMock Cloud

**Input**

`name` (string, required): The name of the mock API
`hostname` (string, optional): Custom hostname for the mock API
`type` (string, optional): Type of the mock API (e.g., openapi, graphql). Defaults to openapi if not specified.

**Output**

Confirmation with mock API details

### `delete_mock_api`

Deletes a mock API by its ID

**Input**

`mockApiId` (string): The ID of the mock API to delete

**Output**

Confirmation message

### `clear_mock_api`

Deletes all stubs in a specified mock API

**Input**

`mockApiId` (string): The ID of the mock API to clear

**Output**

Confirmation message

## Stub Management

### `import_stubs_to_mock_api`

Imports a list of stubs to a specific mock API

**Input**

`mockApiId` (string): The ID of the mock API
`stubsJson` (string): WireMock stub mappings in JSON format

**Output**

Confirmation message

### `get_stub_mappings`

Fetches stub mappings for a given Mock API. Supports pagination to avoid token limits when dealing with large numbers of stubs.

**Input**

`mockApiId` (string): The ID of the mock API
`page` (integer, optional): Page number for pagination (1-based). If not specified, returns all stubs.
`limit` (integer, optional): Maximum number of stubs to return per page. If not specified, returns all stubs.

**Output**

JSON containing stub mappings

### `update_stub_mapping`

Updates a specific stub mapping

**Input**

`mockApiId` (string): The ID of the mock API
`stubId` (string): The ID of the stub mapping to update
`stubJson` (string): The new stub mapping definition in JSON format

**Output**

Confirmation message

### `delete_stub_mapping`

Deletes a specific stub mapping

**Input**

`mockApiId` (string): The ID of the mock API
`stubId` (string): The ID of the stub mapping to delete

**Output**

Confirmation message

## API Specifications

### `get_openapi`

Fetches the OpenAPI document for a mock API

**Input**

`mockApiId` (string): The ID of the mock API to fetch the OpenAPI document from

**Output**

OpenAPI document content

### `put_openapi`

Pushes an OpenAPI document to a mock API

**Input**

`mockApiId` (string): The ID of the mock API to push the OpenAPI document to
`openApiDocument` (string): The OpenAPI document content in YAML or JSON format

**Output**

Confirmation message

### `get_graphql`

Fetches the GraphQL schema document for a mock API

**Input**

`mockApiId` (string): The ID of the mock API to fetch the GraphQL schema from

**Output**

GraphQL schema document content

### `put_graphql`

Pushes a GraphQL schema document to a mock API

**Input**

`mockApiId` (string): The ID of the mock API to push the GraphQL schema to
`graphQLDocument` (string): The GraphQL schema document content

**Output**

Confirmation message

## Request Journal

### `get_request_journal`

Fetches the request journal for a mock API

**Input**

`mockApiId` (string): The ID of the mock API to fetch the request journal from

**Output**

Request journal data

### `reset_request_journal`

Resets the request journal for a mock API

**Input**

`mockApiId` (string): The ID of the mock API to reset the request journal for

**Output**

Confirmation message

## Recording

### `start_recording`

Starts recording HTTP traffic from a target service. The recording will proxy requests to the specified base URL and capture all traffic for later analysis. Only one recording session can be active at a time.

**Input**

`baseUrl` (string): The base URL of the target service to record traffic from
`destination` (string, optional): The destination to save recorded events to (format: cloud:mock\_api\_id). If omitted, events will not be persisted.

**Output**

Recording session details including proxy port

### `get_recording_status`

Checks the status of the current recording session. Returns information about whether a recording is active and, if so, the target URL and proxy port being used.

**Input**

None

**Output**

Recording status information

### `stop_recording`

Stops the currently active recording session and returns the number of requests that were recorded. If no recording is active, returns an error.

**Input**

None

**Output**

Number of recorded requests

### `capture_record_event`

Captures a request/response event in the currently active recording session. This allows you to manually add HTTP interactions to the recording that weren't captured through the proxy. The recording session must be active (started with start\_recording) before using this tool.

**Input**

`request` (object): The HTTP request object to capture
`response` (object): The HTTP response object to capture

**Output**

Confirmation message

## Data Sources

### `list_data_sources`

Lists all data sources accessible by the user. This includes both CSV and database data sources that the user has permission to access.

**Input**

`q` (string, optional): A filter for the retrieved items. Only items whose name contains the filter value will be retrieved. The filter is case insensitive.
`page` (integer, optional): The index of the page to retrieve.
`limit` (integer, optional): The amount of page items to retrieve.

**Output**

List of data sources with metadata

### `get_data_source`

Fetches the metadata for a single data source by its ID. This includes information about the data source such as its name, type (CSV or DATABASE), column metadata, state, and other properties.

**Input**

`dataSourceId` (string): The ID of the data source to fetch metadata for

**Output**

Data source metadata

### `get_data_source_data`

Fetches the actual data from a data source as CSV format. This returns the raw CSV data that can be used for analysis, processing, or display purposes.

**Input**

`dataSourceId` (string): The ID of the data source to fetch data from

**Output**

CSV data content

### `create_data_source`

Creates a new data source in WireMock Cloud. Supports both CSV and DATABASE data source types.

For CSV data sources, you must provide:

* name: Display name for the data source
* type: "CSV"
* columnsMetadata: Array of column definitions with name and type information
* rows: Array of data rows, where each row is an array of string values

For DATABASE data sources, you must provide:

* name: Display name for the data source
* type: "DATABASE"
* databaseConnection: ID of the database connection to use
* tableName: Name of the table or view to retrieve data from

**Input**

`dataSource` (object): The data source configuration object

**Output**

Created data source details

### `update_data_source`

Updates an existing data source in WireMock Cloud. Supports both CSV and DATABASE data source types.

**Input**

`dataSourceId` (string): The ID of the data source to update
`dataSource` (object): The updated data source configuration object

**Output**

Confirmation message

### `update_data_source_data`

Updates the data for a data source from CSV content. This replaces all existing data in the data source with the provided CSV data.

**Input**

`dataSourceId` (string): The ID of the data source to update data for
`csvData` (string): The CSV data to upload. Should be properly formatted CSV with headers in the first row and data rows following.

**Output**

Confirmation message

### `delete_data_source`

Deletes a data source by its ID from WireMock Cloud. This operation permanently removes the data source and cannot be undone.

**Input**

`dataSourceId` (string): The ID of the data source to delete

**Output**

Confirmation message

## HTTP Client

### `make_http_request`

Makes an HTTP request to any endpoint and returns the response. Supports all HTTP methods, custom headers, and request bodies.

HTTP requests can optionally be authenticated using configured authenticators. See [HTTP Request Authentication](/ai-mcp/http-request-authentication/) for more details.

**Input**

`method` (string): The HTTP request method (e.g., GET, POST, PUT, DELETE)
`absoluteUrl` (string): The full URL to make the request to
`headers` (object, optional): HTTP headers as key-value pairs
`body` (string, optional): Request body content
`bodyAsBase64` (string, optional): Base64 encoded body content

**Output**

HTTP response including status, headers, and body

## Documentation

### `look_up_documentation`

Look up documentation articles to help with WireMock usage and best practices. Returns the content of the specified documentation article.

**Input**

`document` (string): The documentation article to retrieve (enum values: stub\_creation, stateful\_stubbing, api\_crawling, data\_driven\_stubbing, validating\_and\_fixing)

**Output**

Documentation article content


# Getting Started with the API
Source: https://docs.wiremock.io/api-getting-started

How to use the WireMock Cloud REST API

The WireMock Cloud REST API is served from [https://api.wiremock.cloud/v1](https://api.wiremock.cloud/v1). It accepts and returns `application/json`.

## Authentication

There are three ways to authenticate yourself with the WireMock Cloud API:

### 1. API Token authentication (preferred)

Pass an `Authorization` header of the form `Token <api-key>`:

```http request theme={null}
GET /v1
Authorization: Token <api-key>
Accept: application/json
```

Your API key can be retrieved from the web application at [https://app.wiremock.cloud/account/security](https://app.wiremock.cloud/account/security).

Unfortunately while this is our preferred authentication mechanism, it is not supported by the OpenAPI 3.x specification
so it is not the one that features in the generated documentation examples.

### 2. Basic authentication (legacy)

Pass an `Authorization` header of the form `Basic <encoded-value>`, where `<encoded-value>` is the base64-encoded string
`username:api-key`.

```http request theme={null}
GET /v1
Authorization: Basic <encoded-value>
Accept: application/json
```

Your API key can be retrieved from the web application at [https://app.wiremock.cloud/account/security](https://app.wiremock.cloud/account/security).

Unfortunately the generated documentation erroneously describes the `<encoded-value>` as the base64-encoded string
`username:password` rather than `username:api-key` - at present we cannot fix this.

### 3. OAuth 2.0 Device Authorization Flow

An enterprise customer wishing to use OAuth 2.0 Access Tokens to authenticate to the WireMock Cloud API, e.g. from their
own CLI, and happy to do more integration work, may request access by
[contacting the WireMock team](https://www.wiremock.io/contact-now) and then
[implement the device authorization flow](/device-authorization-flow).

They can then pass an `Authorization` header of the form `{token_response.token_type} {token_response.access_token}`:

```http request theme={null}
GET /v1
Authorization: {token_response.token_type} {token_response.access_token}
Accept: application/json
```

## Documentation

The full API is documented under [API Reference](/api-reference/users/get-self).


# Delete an entry from an entity's ACL.
Source: https://docs.wiremock.io/api-reference/access-control/delete-an-entry-from-an-entitys-acl

api-reference/openapi.yaml delete /v1/{entityCollection}/{entityId}/acl/{subjectType}/{subjectEntityId}
Remove a team or user to an entity's ACL.



# Get ACL candidates
Source: https://docs.wiremock.io/api-reference/access-control/get-acl-candidates

api-reference/openapi.yaml get /v1/{entityCollection}/{entityId}/acl/candidates
Get candidate users and teams that can be added to this entity's ACL



# Update an entity's ACL
Source: https://docs.wiremock.io/api-reference/access-control/update-an-entitys-acl

api-reference/openapi.yaml put /v1/{entityCollection}/{entityId}/acl/{subjectType}/{subjectEntityId}
Add or update a team or user to an entity's ACL.



# Create a data source
Source: https://docs.wiremock.io/api-reference/data-sources/create-a-data-source

api-reference/openapi.yaml post /v1/users/{userId}/data-sources



# Delete data source by ID
Source: https://docs.wiremock.io/api-reference/data-sources/delete-data-source-by-id

api-reference/openapi.yaml delete /v1/data-sources/{dataSourceId}



# Get data source by ID
Source: https://docs.wiremock.io/api-reference/data-sources/get-data-source-by-id

api-reference/openapi.yaml get /v1/data-sources/{dataSourceId}



# Get data sources accessible by a user
Source: https://docs.wiremock.io/api-reference/data-sources/get-data-sources-accessible-by-a-user

api-reference/openapi.yaml get /v1/users/{userId}/data-sources



# Update data source
Source: https://docs.wiremock.io/api-reference/data-sources/update-data-source

api-reference/openapi.yaml put /v1/data-sources/{dataSourceId}



# Update data source CSV data
Source: https://docs.wiremock.io/api-reference/data-sources/update-data-source-csv-data

api-reference/openapi.yaml put /v1/data-sources/{dataSourceId}/data
Updates the rows of a CSV data source



# Create a database connection
Source: https://docs.wiremock.io/api-reference/database-connections/create-a-database-connection

api-reference/openapi.yaml post /v1/users/{userId}/database-connections



# Delete database connection by ID
Source: https://docs.wiremock.io/api-reference/database-connections/delete-database-connection-by-id

api-reference/openapi.yaml delete /v1/database-connections/{databaseConnectionId}



# Get database connection by ID
Source: https://docs.wiremock.io/api-reference/database-connections/get-database-connection-by-id

api-reference/openapi.yaml get /v1/database-connections/{databaseConnectionId}



# Get database connections accessible by a user
Source: https://docs.wiremock.io/api-reference/database-connections/get-database-connections-accessible-by-a-user

api-reference/openapi.yaml get /v1/users/{userId}/database-connections



# Test a database connection
Source: https://docs.wiremock.io/api-reference/database-connections/test-a-database-connection

api-reference/openapi.yaml post /v1/users/{userId}/database-connections/test



# Update database connection
Source: https://docs.wiremock.io/api-reference/database-connections/update-database-connection

api-reference/openapi.yaml patch /v1/database-connections/{databaseConnectionId}



# Import into a mock API
Source: https://docs.wiremock.io/api-reference/imports/import-into-a-mock-api

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/imports
Import any supported format into your Mock API. The supplied data will be converted into stubs that your Mock API will be populated with. Supported formats include WireMock mappings JSON files, OpenAPI specifications, Postman collections, HAR (HTTP Archive) logs, WireMock request log JSON files and WireMock directories.



# Get a mock API's versions
Source: https://docs.wiremock.io/api-reference/mock-api-versioning/get-a-mock-apis-versions

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/version-history/commits



# Get a version by ID
Source: https://docs.wiremock.io/api-reference/mock-api-versioning/get-a-version-by-id

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/version-history/commits/{versionCommitId}



# Get all changes between one version and another
Source: https://docs.wiremock.io/api-reference/mock-api-versioning/get-all-changes-between-one-version-and-another

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/version-history/commits/{versionCommitId}/changes



# Get all entities in a given version
Source: https://docs.wiremock.io/api-reference/mock-api-versioning/get-all-entities-in-a-given-version

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/version-history/commits/{versionCommitId}/items



# Get the change to an entity between one version and another
Source: https://docs.wiremock.io/api-reference/mock-api-versioning/get-the-change-to-an-entity-between-one-version-and-another

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/version-history/commits/{versionCommitId}/changes/{entityType}/{entityId}



# Get the contents of a entity at a given version
Source: https://docs.wiremock.io/api-reference/mock-api-versioning/get-the-contents-of-a-entity-at-a-given-version

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/version-history/commits/{versionCommitId}/blob/{entityType}/{entityId}



# Restore the contents of all mock API entities to a given version
Source: https://docs.wiremock.io/api-reference/mock-api-versioning/restore-the-contents-of-all-mock-api-entities-to-a-given-version

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/version-history/commits/{versionCommitId}/restore



# Restore the contents of an entity to a given version
Source: https://docs.wiremock.io/api-reference/mock-api-versioning/restore-the-contents-of-an-entity-to-a-given-version

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/version-history/commits/{versionCommitId}/restore/{entityType}/{entityId}



# Create a new mock API
Source: https://docs.wiremock.io/api-reference/mock-apis/create-a-new-mock-api

api-reference/openapi.yaml post /v1/mock-apis



# Delete mock API
Source: https://docs.wiremock.io/api-reference/mock-apis/delete-mock-api

api-reference/openapi.yaml delete /v1/mock-apis/{mockApiId}



# Get mock API by ID
Source: https://docs.wiremock.io/api-reference/mock-apis/get-mock-api-by-id

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}



# Get mock APIs accessible to a user
Source: https://docs.wiremock.io/api-reference/mock-apis/get-mock-apis-accessible-to-a-user

api-reference/openapi.yaml get /v1/users/{userId}/apis



# Move a mock API to a different mock host
Source: https://docs.wiremock.io/api-reference/mock-apis/move-a-mock-api-to-a-different-mock-host

api-reference/openapi.yaml put /v1/mock-apis/{mockApiId}/host



# Update mock API
Source: https://docs.wiremock.io/api-reference/mock-apis/update-mock-api

api-reference/openapi.yaml put /v1/mock-apis/{mockApiId}



# Retrieve a mock host by ID
Source: https://docs.wiremock.io/api-reference/mock-hosts/retrieve-a-mock-host-by-id

api-reference/openapi.yaml get /v1/hosts/{mockHostId}



# Get OpenAPI document for mock API
Source: https://docs.wiremock.io/api-reference/openapi/get-openapi-document-for-mock-api

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/open-api



# Pull OpenAPI document from Git
Source: https://docs.wiremock.io/api-reference/openapi/pull-openapi-document-from-git

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/open-api/pull



# Push OpenAPI document to Git
Source: https://docs.wiremock.io/api-reference/openapi/push-openapi-document-to-git

api-reference/openapi.yaml put /v1/mock-apis/{mockApiId}/open-api/push



# Update OpenAPI document for mock API
Source: https://docs.wiremock.io/api-reference/openapi/update-openapi-document-for-mock-api

api-reference/openapi.yaml put /v1/mock-apis/{mockApiId}/open-api



# Delete organisation
Source: https://docs.wiremock.io/api-reference/organisations/delete-organisation

api-reference/openapi.yaml delete /v1/organisations/{organisationId}



# Delete organisation member user
Source: https://docs.wiremock.io/api-reference/organisations/delete-organisation-member-user

api-reference/openapi.yaml delete /v1/organisations/{organisationId}/members/{userId}



# Get organisation by ID
Source: https://docs.wiremock.io/api-reference/organisations/get-organisation-by-id

api-reference/openapi.yaml get /v1/organisations/{organisationId}



# Get pending invitations for organisation
Source: https://docs.wiremock.io/api-reference/organisations/get-pending-invitations-for-organisation

api-reference/openapi.yaml get /v1/organisations/{organisationId}/invitations



# Get users in an organisation
Source: https://docs.wiremock.io/api-reference/organisations/get-users-in-an-organisation

api-reference/openapi.yaml get /v1/organisations/{organisationId}/users
Gets the users under a specific organisation, optionally filtered by username/email address.



# Invite a user to an organisation
Source: https://docs.wiremock.io/api-reference/organisations/invite-a-user-to-an-organisation

api-reference/openapi.yaml post /v1/organisations/{organisationId}/invitations



# Retrieve an organisation's mock hosts
Source: https://docs.wiremock.io/api-reference/organisations/retrieve-an-organisations-mock-hosts

api-reference/openapi.yaml get /v1/organisations/{organisationId}/hosts



# Update organisation
Source: https://docs.wiremock.io/api-reference/organisations/update-organisation

api-reference/openapi.yaml put /v1/organisations/{organisationId}



# Get recording status
Source: https://docs.wiremock.io/api-reference/recordings/get-recording-status

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/recordings/status



# Start recording
Source: https://docs.wiremock.io/api-reference/recordings/start-recording

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/recordings/start
Begin recording stub mappings



# Stop recording
Source: https://docs.wiremock.io/api-reference/recordings/stop-recording

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/recordings/stop
End recording of stub mappings



# Take a snapshot recording
Source: https://docs.wiremock.io/api-reference/recordings/take-a-snapshot-recording

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/recordings/snapshot



# Count requests by criteria
Source: https://docs.wiremock.io/api-reference/requests/count-requests-by-criteria

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/requests/count
Count requests logged in the journal matching the specified criteria



# Delete all requests in journal
Source: https://docs.wiremock.io/api-reference/requests/delete-all-requests-in-journal

api-reference/openapi.yaml delete /v1/mock-apis/{mockApiId}/requests



# Delete request by ID
Source: https://docs.wiremock.io/api-reference/requests/delete-request-by-id

api-reference/openapi.yaml delete /v1/mock-apis/{mockApiId}/requests/{requestId}



# Delete requests mappings matching metadata
Source: https://docs.wiremock.io/api-reference/requests/delete-requests-mappings-matching-metadata

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/requests/remove-by-metadata



# Empty the request journal
Source: https://docs.wiremock.io/api-reference/requests/empty-the-request-journal

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/requests/reset



# Find requests by criteria
Source: https://docs.wiremock.io/api-reference/requests/find-requests-by-criteria

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/requests/find
Retrieve details of requests logged in the journal matching the specified criteria



# Find unmatched requests
Source: https://docs.wiremock.io/api-reference/requests/find-unmatched-requests

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/requests/unmatched
Get details of logged requests that weren't matched by any stub mapping



# Get all requests in journal
Source: https://docs.wiremock.io/api-reference/requests/get-all-requests-in-journal

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/requests



# Get request by ID
Source: https://docs.wiremock.io/api-reference/requests/get-request-by-id

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/requests/{requestId}



# Remove requests by criteria
Source: https://docs.wiremock.io/api-reference/requests/remove-requests-by-criteria

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/requests/remove
Removed requests logged in the journal matching the specified criteria



# Regenerate a user's API token
Source: https://docs.wiremock.io/api-reference/security/regenerate-a-users-api-token

api-reference/openapi.yaml post /v1/users/{userId}/regenerate-api-token



# Create a rate limit
Source: https://docs.wiremock.io/api-reference/settings/create-a-rate-limit

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/settings/rateLimits



# Delete a rate limit
Source: https://docs.wiremock.io/api-reference/settings/delete-a-rate-limit

api-reference/openapi.yaml delete /v1/mock-apis/{mockApiId}/settings/rateLimits/{rateLimitId}



# Get a rate limit by ID
Source: https://docs.wiremock.io/api-reference/settings/get-a-rate-limit-by-id

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/settings/rateLimits/{rateLimitId}



# Get all rate limits
Source: https://docs.wiremock.io/api-reference/settings/get-all-rate-limits

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/settings/rateLimits



# Get chaos settings
Source: https://docs.wiremock.io/api-reference/settings/get-chaos-settings

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/settings/chaos



# Get delay distribution
Source: https://docs.wiremock.io/api-reference/settings/get-delay-distribution

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/settings/delayDistribution



# Get OpenAPI settings
Source: https://docs.wiremock.io/api-reference/settings/get-openapi-settings

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/settings/openapi



# Get state settings
Source: https://docs.wiremock.io/api-reference/settings/get-state-settings

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/settings/state



# Replace all rate limits
Source: https://docs.wiremock.io/api-reference/settings/replace-all-rate-limits

api-reference/openapi.yaml put /v1/mock-apis/{mockApiId}/settings/rateLimits



# Update a rate limit
Source: https://docs.wiremock.io/api-reference/settings/update-a-rate-limit

api-reference/openapi.yaml put /v1/mock-apis/{mockApiId}/settings/rateLimits/{rateLimitId}



# Update chaos settings
Source: https://docs.wiremock.io/api-reference/settings/update-chaos-settings

api-reference/openapi.yaml put /v1/mock-apis/{mockApiId}/settings/chaos



# Update delay distribution
Source: https://docs.wiremock.io/api-reference/settings/update-delay-distribution

api-reference/openapi.yaml put /v1/mock-apis/{mockApiId}/settings/delayDistribution



# Update OpenAPI settings
Source: https://docs.wiremock.io/api-reference/settings/update-openapi-settings

api-reference/openapi.yaml put /v1/mock-apis/{mockApiId}/settings/openapi



# Update state settings
Source: https://docs.wiremock.io/api-reference/settings/update-state-settings

api-reference/openapi.yaml put /v1/mock-apis/{mockApiId}/settings/state



# Get all scenarios
Source: https://docs.wiremock.io/api-reference/state/get-all-scenarios

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/scenarios



# Reset all state
Source: https://docs.wiremock.io/api-reference/state/reset-all-state

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/scenarios/reset
Resets all scenario and dynamic state



# Create a new stub mapping
Source: https://docs.wiremock.io/api-reference/stub-mappings/create-a-new-stub-mapping

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/mappings



# Delete a stub mapping
Source: https://docs.wiremock.io/api-reference/stub-mappings/delete-a-stub-mapping

api-reference/openapi.yaml delete /v1/mock-apis/{mockApiId}/mappings/{stubMappingId}



# Delete all stub mappings
Source: https://docs.wiremock.io/api-reference/stub-mappings/delete-all-stub-mappings

api-reference/openapi.yaml delete /v1/mock-apis/{mockApiId}/mappings



# Delete stub mappings matching metadata
Source: https://docs.wiremock.io/api-reference/stub-mappings/delete-stub-mappings-matching-metadata

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/mappings/remove-by-metadata



# Find stub mappings matching metadata
Source: https://docs.wiremock.io/api-reference/stub-mappings/find-stub-mappings-matching-metadata

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/mappings/find-by-metadata
Find stubs by matching on their metadata



# Get all stub mappings
Source: https://docs.wiremock.io/api-reference/stub-mappings/get-all-stub-mappings

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/mappings



# Get stub mapping by ID
Source: https://docs.wiremock.io/api-reference/stub-mappings/get-stub-mapping-by-id

api-reference/openapi.yaml get /v1/mock-apis/{mockApiId}/mappings/{stubMappingId}



# Import stub mappings
Source: https://docs.wiremock.io/api-reference/stub-mappings/import-stub-mappings

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/mappings/import
Import a collection of stub mappings.
Note: a more flexible import operation is available at the [Import endpoint](../imports/import).




# Persist stub mappings
Source: https://docs.wiremock.io/api-reference/stub-mappings/persist-stub-mappings

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/mappings/save
Save all persistent stub mappings to the backing store



# Reset stub mappings
Source: https://docs.wiremock.io/api-reference/stub-mappings/reset-stub-mappings

api-reference/openapi.yaml post /v1/mock-apis/{mockApiId}/mappings/reset
Restores stub mappings to the defaults defined back in the backing store



# Update a stub mapping
Source: https://docs.wiremock.io/api-reference/stub-mappings/update-a-stub-mapping

api-reference/openapi.yaml put /v1/mock-apis/{mockApiId}/mappings/{stubMappingId}



# Add team member
Source: https://docs.wiremock.io/api-reference/teams/add-team-member

api-reference/openapi.yaml post /v1/teams/{teamId}/members



# Create a team
Source: https://docs.wiremock.io/api-reference/teams/create-a-team

api-reference/openapi.yaml post /v1/teams



# Delete a team by ID
Source: https://docs.wiremock.io/api-reference/teams/delete-a-team-by-id

api-reference/openapi.yaml delete /v1/teams/{teamId}



# Delete a team member
Source: https://docs.wiremock.io/api-reference/teams/delete-a-team-member

api-reference/openapi.yaml delete /v1/teams/{teamId}/members/{userId}



# Get a team by ID
Source: https://docs.wiremock.io/api-reference/teams/get-a-team-by-id

api-reference/openapi.yaml get /v1/teams/{teamId}



# Get all teams in an organisation
Source: https://docs.wiremock.io/api-reference/teams/get-all-teams-in-an-organisation

api-reference/openapi.yaml get /v1/organisations/{organisationId}/teams



# Get all teams readable by a user
Source: https://docs.wiremock.io/api-reference/teams/get-all-teams-readable-by-a-user

api-reference/openapi.yaml get /v1/users/{userId}/teams



# Get team members
Source: https://docs.wiremock.io/api-reference/teams/get-team-members

api-reference/openapi.yaml get /v1/teams/{teamId}/members



# Get usage
Source: https://docs.wiremock.io/api-reference/usage/get-usage

api-reference/openapi.yaml get /v1/subscriptions/{subscriptionId}/usage
Get product usage for the current billing period for a subscription



# Delete user by ID
Source: https://docs.wiremock.io/api-reference/users/delete-user-by-id

api-reference/openapi.yaml delete /v1/users/{userId}



# Get self
Source: https://docs.wiremock.io/api-reference/users/get-self

api-reference/openapi.yaml get /v1/users/self
Redirect to the user account owned by the authenticated user



# Get user by ID
Source: https://docs.wiremock.io/api-reference/users/get-user-by-id

api-reference/openapi.yaml get /v1/users/{userId}



# Update user
Source: https://docs.wiremock.io/api-reference/users/update-user

api-reference/openapi.yaml put /v1/users/{userId}



# Audit Events Overview
Source: https://docs.wiremock.io/audit-events/overview

Send WireMock Cloud audit events to an AWS S3 bucket you own

WireMock Cloud generates audit events when you perform various actions within your account.  For example, creating or
deleting Mock APIs, changing settings or logging in and many more.  For our enterprise customers we provide the ability
to push these audit events to an AWS S3 bucket stored within your AWS account.

## Usage

The audit event feature is only available to users on our Enterprise or Enterprise Trial plans and you will need to be
an organisation administrator to create and manage audit event destinations.

To create and manage your S3 bucket destination, navigate to the [Organisation Page](https://app.wiremock.cloud/account/organisation)
on your account. On this page you will see the `Audit Events` section.

<img alt="Empty S3 audit event destination" />

This is where you will create and manage your S3 audit event destination. To set up an S3 audit event destination you
will need to configure your AWS account with an S3 bucket and a role to allow WireMock Cloud to push audit events to that
bucket.

## Configure Your AWS Account

The first step in setting up your S3 audit event destination is to configure your AWS account to allow WireMock Cloud
to save audit events to your bucket.  You can do this in the following way:

* Create the S3 bucket `<your-company-name>-wiremock-cloud-audit-events` (you can use any bucket name if you have your own naming
  convention but be sure to update the bucket name in the examples below)
* Create a policy called `wiremock-cloud-put-audit-events` with `s3:PutObject` on `arn:aws:s3:::<your-company-name>-wiremock-cloud-audit-events/*`

```json theme={null}
{
  "Version": "2012-10-17",
  "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "s3:PutObject"
        ],
        "Resource": "arn:aws:s3:::<your-company-name>-wiremock-cloud-audit-events/*"
      }
    ]
}
```

* Create an AWS account role for another AWS account
  * Specify account id `499333472133`.
  * Do **NOT** require external ID or MFA.
  * Choose `wiremock-cloud-put-audit-events` as the policy (the one you created above)
  * Name it `wiremock-cloud-put-audit-events`
  * Set the trust policy as so:

```json theme={null}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::499333472133:root"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

Once you have completed the steps above, you can navigate to the [Organisation Page](https://app.wiremock.cloud/account/organisation)
and continue the configuration there.

## Configure Your WireMock Cloud Account

Now you have configured your AWS account with the new bucket and role, you can add those details to the `Audit Events`
section on the Organisations page:

* Enter the bucket name into the `Bucket name` field
* Enter the full role arn into the `Role ARN` field

<img alt="Populated S3 audit event destination" />

* Click on the `Save` button to add the S3 audit destination to your organisation

Once you have saved the audit destination, you will see some documentation you can copy to make sure the role permission
and trust relationship you created above is correct.  For a newly created audit destination you should see the status
message - `Status: Audit events are yet to be sent to this destination`

<img alt="Saved S3 audit event destination" />

## Testing Your S3 Audit Event Destination

Now you saved the S3 audit event destination you can test it to make sure everything works end to end.  Clicking on the
`Test` button will make WireMock Cloud attempt to post a test file to the bucket you created above.  If all works
correctly the button will turn green and you should have a new file saved to your S3 bucket called `test-wiremock-cloud-integration.txt`.
This file will contain the date and time the test was performed.

<img alt="S3 audit event destination test success" />

Should an error occur trying to post the file to your S3 bucket, an error will be displayed to help you diagnose the issue.

<img alt="S3 audit event destination test failure" />

## Deleting Your S3 Audit Event Destination

If you no longer require audit events to be sent to your S3 bucket you can delete the audit event destination from your
organisation.  This will stop audit events being set to your S3 bucket.  To do this you can click on the `Delete`
button.  This will display a confirmation dialog to allow you to confirm the deletion.

<img alt="Delete S3 audit event destination confirmation" />

Clicking on `No` will close the dialog and no action will be taken, clicking on `Yes` will delete your S3 audit event
destination and no more audit events will be sent.

## Sending Audit Events To Your S3 Bucket

WireMock Cloud will send audit events to your S3 bucket in batches every 10 minutes.  There is a lookback window of
7 days for audit events.  This means if you are setting up an S3 audit event destination and have been a customer for
a while, the first batch of audit events sent to your bucket will span back 7 days prior to the date you setup the
destination.

Once audit events are successfully being sent to your bucket you will see the status message update on the Organisation page:

<img alt="Successfully sent audit events" />

If WireMock Cloud encounters an error while sending audit events to your S3 bucket, the status will be updated to
highlight the error. If audit events have been successfully sent in the past, the error will also contain the date the
last successful attempt was made:

<img alt="Failure to send audit events" />

Audit events are saved in your S3 bucket using the following structure:

```
|── 2025-02
|   |── 01
|   |   |── 2025-02-01T13-45-12-789Z-wjg0yr69.json
|   |── 02
|       |── 2025-02-02T13-32-12-789Z-16oe0mgo.json
|       |── 2025-02-02T14-29-12-789Z-9lrrjdm6.json
|── 2025-03
    |── 02
    |   |── 2025-03-02T13-23-12-789Z-kr731z1.json
    |── 03
        |── 2025-03-03T13-45-12-789Z-9odlj3w3.json
        |── 2025-03-03T14-29-12-789Z-38o4klr7.json
```

Each file follows the [new line delimited JSON specification](https://github.com/ndjson/ndjson-spec).

Audit events for the following items in WireMock Cloud are sent to your S3 bucket:

* Mock APIs
* Users
* Teams
* Organisations
* API Templates
* API Template Catalogues
* Data Sources
* Database Connections
* Keys
* Stub Mappings
* Mock API Settings
* Subscriptions
* Open API Git Integrations
* API Keys
* S3 Audit Destinations

More information about working with the audit event json can be found [here](./working-with-audit-events).

## Limits

You can read more about [plan limits here](./plan-limits/).


# Audit Event Destinations - Plan Limits
Source: https://docs.wiremock.io/audit-events/plan-limits

Limitations of your audit destination usage.

WireMock Cloud applies limits to audit event destinations dependent upon the plan your organisation is subscribed to.

On the enterprise or enterprise trial plans, an account is limited to 1 audit event destination.  Accounts on the free
plan do not have access to this feature. If you are on the free plan and would like access to this feature,
[contact the WireMock team today](https://www.wiremock.io/contact-now) to discuss an enterprise plan for your organisation.

## Disabled Audit Event Destinations

If an account/organisation is downgraded to a plan that causes their audit event destinations to exceed the new plan's
limits, the exceeding destinations will be disabled.  This means WireMock Cloud will no longer send audit events to
those destinations.

Disabled destinations can be enabled at any time by [upgrading to a different plan](https://www.wiremock.io/contact-now).


# Working with Audit Event JSON
Source: https://docs.wiremock.io/audit-events/working-with-audit-events

Programmatically working with Audit Event JSON

Each file saved in your S3 bucket follows the [new line delimited JSON specification](https://github.com/ndjson/ndjson-spec).

Each line of json in the file conforms to the following json schema:

```json theme={null}
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "eventId": {
      "type": "string",
      "format": "uuid"
    },
    "entity": { "$ref": "#/definitions/entity" },
    "parentEntity": { "$ref": "#/definitions/entity" },
    "organisation": { "$ref": "#/definitions/entity" },
    "principal": { "$ref": "#/definitions/entity" },
    "clientType": {
      "anyOf": [
        {
          "type": "string",
          "enum": [
            "UI",
            "API",
            "SYSTEM",
            "ADMIN",
            "CLI"
          ]
        },
        { "type": "string" }
      ]
    },
    "action": {
      "anyOf": [
        {
          "type": "string",
          "enum": [
            "CREATE",
            "UPDATE",
            "DELETE",
            "SIGNUP",
            "LOGIN",
            "ACL_GRANT",
            "ACL_REVOKE",
            "INVITE"
          ]
        },
        { "type": "string" }
      ]
    },
    "before": {
      "type": "object"
    },
    "after": {
      "type": "object"
    },
    "subject": { "$ref": "#/definitions/entity" },
    "permission": {
      "oneOf": [
        {
          "type": "string",
          "const": "ALL_PERMISSIONS"
        },
        {
          "type": "object",
          "properties": {
            "permissions": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string"
                  },
                  "friendlyId": {
                    "type": "string"
                  }
                },
                "required": [
                  "id",
                  "friendlyId"
                ]
              }
            }
          },
          "required": ["permissions"]
        }
      ]
    }
  },
  "required": [
    "timestamp",
    "eventId",
    "entity",
    "organisation",
    "principal",
    "clientType",
    "action"
  ],
  "definitions": {
    "entity": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "entityType": {
          "anyOf": [
            {
              "type": "string",
              "enum": [
                "MOCK_API",
                "USER",
                "TEAM",
                "ORGANISATION",
                "API_TEMPLATE",
                "API_TEMPLATE_CATALOGUE",
                "DATA_SOURCE",
                "KEY",
                "DATABASE_CONNECTION",
                "STUB_MAPPING",
                "MOCK_API_SETTINGS",
                "SUBSCRIPTION",
                "OPENAPI_GIT_INTEGRATION",
                "API_KEY",
                "S3_AUDIT_SINK"
              ]
            },
            { "type": "string" }
          ]
        }
      },
      "required": ["id", "name", "entityType"]
    }
  }
}
```


# Authentication
Source: https://docs.wiremock.io/authentication

How to make authenticated calls to the WireMock Cloud API

## Getting your API token

Each WireMock Cloud user has their own API token which can be found in the [account security page](https://app.wiremock.cloud/user/security).
Copy this token value and make a note of your username, which is usually your email address.

## Making an authenticated call

The WireMock Cloud API uses HTTP Basic authentication, where the username is your username and the password is your API key.

HTTP Basic authentication is achieved by setting the value of the `Authorization` header to `<username>:<password>` base64 encoded.
However, nearly all HTTP clients will construct this for you, taking these two parameters as inputs e.g. curl:

```bash theme={null}
curl -u 'jeff@example.com:aaaabbbbcccddd11122233' \
  https://api.wiremock.cloud/v1/users/self
```

<Note>
  You can try particular API calls from within the API reference docs by pasting your username and token into the security fields.
  Since you're hitting live API be careful when making calls to endpoints that can modify data (anything that's a POST, PUT or DELETE)
  as this will affect the change in your account.
</Note>


# Chaos settings - Basics
Source: https://docs.wiremock.io/chaos

Proxying requests to other systems

The idea of the chaos settings is to introduce an element of failure into your
environment and observe how clients cope with it.

WireMock Cloud now allows introducing a random element of chaos across all the
calls to a particular API. This would allow you to check that your client
behaves appropriately; closes resources correctly, times out correctly, conveys
sensible error messages to the end user and to your monitoring systems, perhaps
opens circuit breakers to take load off the upstream system or other resilience
mechanisms.

## Enabling Chaos

You enable chaos by toggling the "Enable chaos" switch.

<img alt="Enable chaos" />

Once chaos is enabled, you can set a percentage of requests to that API to
experience a failure using the slider, or type it directly.

<img alt="Chaos percentage slider" />

The configured percentage of failures will be distributed evenly among the
failure modes.

We support five failure modes:

### [Socket close](#socket-close)

A request will just have the socket closed, with no data returned to the client
at all. This would allow you to check that your client closes all resources
appropriately in response.

### [Socket reset](#socket-reset)

The server will close the connection, setting `SO_LINGER` to 0 and thus
preventing the `TIME_WAIT` state being entered. Typically causes a
"Connection reset by peer" type error to be thrown by the client.

Note: this only seems to work properly on \*nix OSs. On Windows it will most
likely cause the connection to hang rather than reset.

This would allow you to check that your client closes all resources
appropriately in response.

### [Invalid HTTP](#invalid-http)

The server will start by responding with a valid HTTP status line, then will
return random bytes, so an invalid HTTP response. Then it will close the
connection.

### [Long delay](#long-delay)

The server will delay for the configured amount of time before responding. This
would allow you to check that you have appropriately configured timeouts.

<img alt="Chaos long delay" />

### [HTTP Error status](#http-error-status)

The server will return valid HTTP responses with the configured error status
codes.

<img alt="Chaos http errors" />


# CLI Command Reference
Source: https://docs.wiremock.io/cli/command-reference

Complete reference documentation for all WireMock CLI commands

This reference documents all available commands, subcommands, and options in the WireMock CLI. For general usage and installation instructions, see [Installation and basic usage](/cli/overview).

## Global options

These options are available for all commands:

### -V, --version

Show the version and exit.

```shell theme={null}
wiremock --version
```

### -h, --help

Show help message and exit. Can be used with any command or subcommand.

```shell theme={null}
wiremock --help
wiremock record --help
```

## Authentication commands

### login

Login to WireMock Cloud. This command must have been executed at least once before executing most other commands.

```shell theme={null}
wiremock login
```

Opens a browser window for authentication. Once complete, your credentials are stored locally.

<Info>
  If you have [set your API endpoint](/cli/config#configuring-your-api-endpoint) to a custom endpoint, `wiremock login` will no longer work. Use [config set](/cli/config#configuring-your-api-token) to set your API token directly.
</Info>

### logout

Remove all WireMock Cloud user information from the CLI configuration.

```shell theme={null}
wiremock logout
```

### whoami

View information on the currently logged in user.

```shell theme={null}
wiremock whoami
```

Displays the username and email of the authenticated user. Exits with an error if not logged in.

## config

Commands to manage your local WireMock CLI configuration.

See [Configuring the CLI](/cli/config) for detailed documentation.

### config get

View a config value.

```shell theme={null}
wiremock config get <key>
```

**Arguments:**

* `<key>` - Configuration key to retrieve. Valid options:
  * `api_token` - The API token to use when calling the WireMock Cloud API
  * `api_endpoint` - The API endpoint to the WireMock Cloud API

**Example:**

```shell theme={null}
wiremock config get api_endpoint
```

### config set

Set a config value.

```shell theme={null}
wiremock config set <key> [<value>]
```

**Arguments:**

* `<key>` - Configuration key to set. Valid options:
  * `api_token` - The API token to use when calling the WireMock Cloud API
  * `api_endpoint` - The API endpoint to the WireMock Cloud API
* `<value>` - The value to set (optional). Omit this argument to enter the value interactively (recommended for confidential config values)

**Example:**

```shell theme={null}
wiremock config set api_token
wiremock config set api_endpoint https://api.wiremock.cloud
```

### config unset

Clear a single config value.

```shell theme={null}
wiremock config unset <key>
```

**Arguments:**

* `<key>` - Configuration key to clear. Valid options:
  * `api_token` - The API token to use when calling the WireMock Cloud API
  * `api_endpoint` - The API endpoint to the WireMock Cloud API

**Example:**

```shell theme={null}
wiremock config unset api_token
```

### config clear

Clear all config values.

```shell theme={null}
wiremock config clear
```

Removes all stored configuration including authentication credentials.

## mock-apis

Commands to interact with your mock APIs.

See [Managing Mock APIs with the CLI](/cli/mock-apis) for detailed documentation.

### mock-apis list

List your mock APIs.

```shell theme={null}
wiremock mock-apis list [<options>]
```

**Options:**

* `--limit=<int>` - The maximum number of mock APIs to return (default: 20)
* `--page=<int>` - The page of mock APIs to return (default: 1)
* `--query=<text>` - The query with which to filter mock APIs
* `-o, --output=(text|json)` - The output format to use (default: text)

**Examples:**

```shell theme={null}
wiremock mock-apis list
wiremock mock-apis list --limit=50 --page=2
wiremock mock-apis list --query="payment" --output=json
```

### mock-apis create

Create a new mock API.

```shell theme={null}
wiremock mock-apis create [<options>] <name>
```

**Arguments:**

* `<name>` - The name of the mock API to create (required)

**Options:**

* `-o, --hostname=<text>` - Optional hostname for the mock API
* `-t, --type=(REST|Unstructured|gRPC|GraphQL)` - Type of the mock API (default: REST)

**Examples:**

```shell theme={null}
wiremock mock-apis create "My API"
wiremock mock-apis create "GraphQL Service" --type=GraphQL
wiremock mock-apis create "Payment API" --hostname=payment-api
```

### mock-apis delete

Delete a mock API by ID.

```shell theme={null}
wiremock mock-apis delete [<options>] <mock_api_id>
```

**Arguments:**

* `<mock_api_id>` - The ID of the mock API to delete (required)

**Options:**

* `-f, --force` - Force delete the mock API without confirmation

**Examples:**

```shell theme={null}
wiremock mock-apis delete abc123xyz
wiremock mock-apis delete abc123xyz --force
```

## record

Record requests to a proxied API and import the converted stubs into a mock API.

See [Recording using the WireMock CLI](/cli/recording) for detailed documentation.

```shell theme={null}
wiremock record [<options>] <from>
```

**Arguments:**

* `<from>` - The URL of the target API to record from (required)

**Options:**

#### Recording behavior

* `--to=<cloud:mock_api_id>` - The ID of the mock API to import recorded stubs into. You will be prompted to choose a mock API if omitted.
* `-p, --reverse-proxy-port=<int>` - The local port to proxy requests through. Set to '0', '-1', or 'random' to assign a random port (default: 8000)

#### Logging

* `--request-log-level=(off|summary|full)` - How recorded requests are displayed in the console during recording (default: summary for interactive sessions, off for non-interactive sessions)
* `-q` - Equivalent of `--request-log-level=off`
* `-v` - Equivalent of `--request-log-level=full`

#### Import configuration

* `--import-config-file=<path>` - Path to a file containing custom configuration for handling how recorded requests are converted into stubs
* `--max-batch-requests, --batch-size=<int>` - The maximum amount of requests to import to the mock API in a single batch while recording. Given a max batch of N requests, an import to the mock API will occur for every N requests recorded. If omitted, all requests will be imported at the end of the session in a single batch.
* `--max-batch-bytes=<binary_size>` - The maximum amount of bytes to import to the mock API in a single batch while recording. Given a max batch of N bytes, an import to the mock API will occur for every N bytes recorded. Note, if a single recorded request exceeds the maximum number of bytes, this request will still be sent (in a batch of one). If omitted, all requests will be imported at the end of the session in a single batch. (examples: 5120, 5kB, 5kiB, 10 MB)

#### TLS/Client certificates

* `-c, --client-certificate=<path>` - Path to a PEM-encoded RSA private key and X509 certificate needed to authenticate against the target API using mutual TLS. Alternative to `--client-certificate-store`.
* `--client-certificate-store=<path>` - Path to a keystore (pkcs12, jks etc.) containing the private key and certificate needed to authenticate against the target API using mutual TLS. Alternative to `--client-certificate`.
* `--client-certificate-store-password=<value>` - Password to unlock the client certificate store if provided.

**Examples:**

```shell theme={null}
wiremock record https://api.example.com
wiremock record https://api.example.com --to=cloud:abc123xyz
wiremock record https://api.example.com -p 9000 -v
wiremock record https://api.example.com --import-config-file=./config.yaml
wiremock record https://api.example.com --max-batch-requests=100
wiremock record https://secure-api.example.com --client-certificate=./cert.pem
```

## record-many

Record requests to multiple proxied APIs and import the converted stubs into a mock API for each target API.

See [Multi-domain recording using the WireMock CLI](/cli/multi-domain-recording) for detailed documentation.

```shell theme={null}
wiremock record-many [<options>]
```

**Options:**

#### Recording configuration

* `--wiremock-dir=<path>` - The path to the wiremock directory, containing services to record (default: .wiremock)
* `-p, --profile=<text>` - Profile name to use for this environment eg dev or staging
* `--include-services=<text>` - Comma separated list of service keys from the recording configuration file which should be recorded. All services will still proxy. If omitted, all services will be recorded.

#### Logging

* `--request-log-level=(off|summary|full)` - How recorded requests are displayed in the console during recording (default: summary for interactive sessions, off for non-interactive sessions)
* `-q` - Equivalent of `--request-log-level=off`
* `-v` - Equivalent of `--request-log-level=full`

#### Import configuration

* `--import-config-file=<path>` - Path to a file containing custom configuration for handling how recorded requests are converted into stubs
* `--max-batch-requests, --batch-size=<int>` - The maximum amount of requests to import to the mock API in a single batch while recording. Given a max batch of N requests, an import to the mock API will occur for every N requests recorded. If omitted, all requests will be imported at the end of the session in a single batch.
* `--max-batch-bytes=<binary_size>` - The maximum amount of bytes to import to the mock API in a single batch while recording. Given a max batch of N bytes, an import to the mock API will occur for every N bytes recorded. Note, if a single recorded request exceeds the maximum number of bytes, this request will still be sent (in a batch of one). If omitted, all requests will be imported at the end of the session in a single batch. (examples: 5120, 5kB, 5kiB, 10 MB)

#### TLS/Client certificates

* `-c, --client-certificate=<path>` - Path to a PEM-encoded RSA private key and X509 certificate needed to authenticate against the target API using mutual TLS. Alternative to `--client-certificate-store`.
* `--client-certificate-store=<path>` - Path to a keystore (pkcs12, jks etc.) containing the private key and certificate needed to authenticate against the target API using mutual TLS. Alternative to `--client-certificate`.
* `--client-certificate-store-password=<value>` - Password to unlock the client certificate store if provided.

**Examples:**

```shell theme={null}
wiremock record-many
wiremock record-many --wiremock-dir=./my-wiremock
wiremock record-many --profile=staging -v
wiremock record-many --include-services=api1,api2
```

## import

Import files or directories into WireMock Cloud.

See [Importing using the CLI](/cli/import) for detailed documentation.

```shell theme={null}
wiremock import [<options>] <file_or_directory>
```

**Arguments:**

* `<file_or_directory>` - The file or directory to import (required)

**Options:**

* `--to=<value>` - The ID of the mock API to import into (required)
* `--import-config-file=<path>` - YAML file containing import configuration

**Examples:**

```shell theme={null}
wiremock import ./stubs --to=cloud:abc123xyz
wiremock import ./api.har --to=cloud:abc123xyz --import-config-file=./config.yaml
```

## push

Commands to push resources to WireMock Cloud.

See [Push and Pull](/cli/push-pull) for detailed documentation.

### push open-api

Push an OpenAPI document to a mock API.

```shell theme={null}
wiremock push open-api [<options>] <mock_api_id>
```

**Arguments:**

* `<mock_api_id>` - The ID of the mock API to push the OpenAPI document to (required)

**Options:**

* `-f, --file=<path>` - The filename to read the OpenAPI document from (if not specified, reads from stdin)
* `-w, --watch` - Watch the file for changes and push on each change

**Examples:**

```shell theme={null}
wiremock push open-api abc123xyz --file=./openapi.yaml
wiremock push open-api abc123xyz --file=./openapi.yaml --watch
cat openapi.yaml | wiremock push open-api abc123xyz
```

### push graphql

Push a GraphQL schema to a mock API.

```shell theme={null}
wiremock push graphql [<options>] <mock_api_id>
```

**Arguments:**

* `<mock_api_id>` - The ID of the mock API to push the GraphQL schema to (required)

**Options:**

* `-f, --file=<path>` - The filename to read the GraphQL schema from (if not specified, reads from stdin)
* `-w, --watch` - Watch the file for changes and push on each change

**Examples:**

```shell theme={null}
wiremock push graphql abc123xyz --file=./schema.graphql
wiremock push graphql abc123xyz --file=./schema.graphql --watch
```

### push mock-api

Push a local mock API configuration to WireMock Cloud.

See [Push and Pull Mock APIs](/cli/push-pull-mock-api) for detailed documentation.

```shell theme={null}
wiremock push mock-api [<options>] [<local_service_ids>]...
```

**Arguments:**

* `<local_service_ids>` - The service IDs defined in your WireMock environment file to push (optional)

**Options:**

* `--all` - Push all mock APIs in your local WireMock environment file. To be used instead of specifying a mock API service ID
* `--wiremock-dir=<path>` - The path to the wiremock directory, containing mock APIs to push (default: .wiremock)
* `-p, --profile=<text>` - Profile name to use for this environment eg dev or staging
* `--to=<value>` - The ID of the destination mock API in the cloud. Use 'cloud:new' to force creation of a new mock API even if cloud\_id is present. If not specified, uses the cloud\_id from wiremock.yaml or creates a new mock API

**Examples:**

```shell theme={null}
wiremock push mock-api my-service
wiremock push mock-api my-service --to=cloud:abc123xyz
wiremock push mock-api --all
wiremock push mock-api --wiremock-dir=./my-wiremock --profile=staging
```

## pull

Commands to pull resources from WireMock Cloud.

See [Push and Pull](/cli/push-pull) for detailed documentation.

### pull open-api

Pull the OpenAPI document from a mock API and save it locally.

```shell theme={null}
wiremock pull open-api [<options>] <mock_api_id>
```

**Arguments:**

* `<mock_api_id>` - The ID of the mock API to pull the OpenAPI document from (required)

**Options:**

* `-f, --file=<path>` - The filename to save the OpenAPI document to

**Examples:**

```shell theme={null}
wiremock pull open-api abc123xyz --file=./openapi.yaml
wiremock pull open-api abc123xyz
```

### pull graphql

Pull the GraphQL schema document from a mock API and save it locally.

```shell theme={null}
wiremock pull graphql [<options>] <mock_api_id>
```

**Arguments:**

* `<mock_api_id>` - The ID of the mock API to pull the GraphQL schema document from (required)

**Options:**

* `-f, --file=<path>` - The filename to save the GraphQL schema document to

**Examples:**

```shell theme={null}
wiremock pull graphql abc123xyz --file=./schema.graphql
```

### pull mock-api

Pull a mock API's stub mappings and create a local configuration.

See [Push and Pull Mock APIs](/cli/push-pull-mock-api) for detailed documentation.

```shell theme={null}
wiremock pull mock-api [<options>] [<mock_api_ids or local service_names>]...
```

**Arguments:**

* `<mock_api_ids or local service_names>` - The IDs of the mock APIs to pull or the names of the services defined in your WireMock environment file to pull (optional)

**Options:**

* `--wiremock-dir=<path>` - The path to the wiremock directory, to which all pulled mock APIs will be written (default: .wiremock)
* `-p, --profile=<text>` - Profile name to use for this environment eg dev or staging
* `--all` - Pull all mock APIs in your local WireMock environment file. To be used instead of specifying a mock API ID or service name
* `--into=<text>` - The name of an existing service in wiremock.yaml to pull data into. Only stub mappings and API documents will be updated; service settings in wiremock.yaml will remain unchanged.

**Examples:**

```shell theme={null}
wiremock pull mock-api abc123xyz
wiremock pull mock-api my-service
wiremock pull mock-api --all
wiremock pull mock-api abc123xyz --into=existing-service
wiremock pull mock-api --wiremock-dir=./my-wiremock --profile=staging
```

## run

Start the local host runner.

See [Running Mock APIs Locally](/cli/local-playback) for detailed documentation.

```shell theme={null}
wiremock run [<options>]
```

**Options:**

* `--wiremock-dir=<path>` - The path to the wiremock directory, containing mock APIs to run (default: .wiremock)
* `-p, --profile=<text>` - Profile name to use for this environment eg dev or staging

**Examples:**

```shell theme={null}
wiremock run
wiremock run --wiremock-dir=./my-wiremock
wiremock run --profile=staging
```

## environments

Commands to manage WireMock Cloud environments.

See [Managing Environments](/cli/environments) for detailed documentation.

### environments create

Create a new WireMock Cloud environment.

```shell theme={null}
wiremock environments create [<options>]
```

**Options:**

* `-p, --profile=<text>` - Profile name to use for this environment eg dev or staging (required)
* `--wiremock-dir=<path>` - The path to the wiremock directory, this is where your environment file will be created (default: .wiremock)

**Examples:**

```shell theme={null}
wiremock environments create --profile=staging
wiremock environments create --profile=dev --wiremock-dir=./my-wiremock
```

## mcp

Start an MCP server for use with AI tools. Intended to be called from the AI tool's MCP configuration rather than directly in the terminal.

See [WireMock Cloud AI](/ai-mcp/installation) for detailed documentation.

```shell theme={null}
wiremock mcp
```

This command starts the Model Context Protocol (MCP) server which provides WireMock functionality to AI assistants and tools.

## See also

* [Installation and basic usage](/cli/overview)
* [Configuring the CLI](/cli/config)
* [Managing Mock APIs with the CLI](/cli/mock-apis)
* [Recording using the WireMock CLI](/cli/recording)
* [Multi-domain recording](/cli/multi-domain-recording)
* [Push and Pull](/cli/push-pull)
* [Running Mock APIs Locally](/cli/local-playback)
* [Managing Environments](/cli/environments)


# Configuring the WireMock CLI
Source: https://docs.wiremock.io/cli/config

Managing the configuration of your local WireMock CLI installation

The WireMock CLI provides a `config` subcommand that allows you to configure the behavior of your CLI installation.

Configuration values can be retrieved using `wiremock config get <key>`, set using `wiremock config set <key> <value>`,
and unset using `wiremock config unset <key>`.
You can clear all configured keys by executing `wiremock config clear`.
Available config keys that you can set are [api\_token](#configuring-your-api-token) and
[api\_endpoint](#configuring-your-api-endpoint).

For comprehensive documentation of how each config command works, in the CLI, you can append a `-h` or `--help` to the
end of any subcommand to view the command's help text.
For example, `wiremock config set -h`.

## Configuring your API token

Your API token is used to authenticate with WireMock Cloud when performing actions like [recording](/cli/recording) or
[managing your mock APIs](/cli/mock-apis).
Setting your API token using the `config` subcommand is an alternative to [the login command](/cli/overview#login).
To set your API token, execute the following command

```shell theme={null}
wiremock config set api_token <API_TOKEN>
```

with `<API_TOKEN>` replaced with your API token, available at [https://app.wiremock.cloud/account/security](https://app.wiremock.cloud/account/security).

## Configuring your API endpoint

<Tip>
  Configuring your WireMock CLI installation to use a custom API endpoint is only relevant to customers using WireMock
  Cloud's on-premise edition. To learn more, [contact the WireMock team today](https://www.wiremock.io/contact-now) to
  discuss an enterprise plan for your organisation.
</Tip>

The CLI's configured API endpoint is the base URL of the API server that the CLI uses to perform actions like
[recording](/cli/recording) or [managing your mock APIs](/cli/mock-apis).
By default, this endpoint is [https://api.wiremock.cloud](https://api.wiremock.cloud), the endpoint used by WireMock Cloud's SaaS edition (more
information on using WireMock Cloud's API can be found in the [API reference](/api-reference)).
To set your API endpoint to a custom URL, execute the following command

```shell theme={null}
wiremock config set api_endpoint <API_ENDPOINT>
```

with `<API_ENDPOINT>` replaced with your API endpoint URL. The API endpoint for your on-premise installation of WireMock
Cloud will have the format `https://api.wiremock.<your_subdomain>`. Consult your system administrator if you are unsure
of the exact URL to use.

<Warning>
  If you have set your API endpoint to a custom endpoint, `wiremock login` will no longer work. Please authenticate by
  [setting your API token using the config subcommand](#configuring-your-api-token) instead.
</Warning>


# Managing Environments with the CLI
Source: https://docs.wiremock.io/cli/environments

How to create and manage environments using the WireMock CLI

The CLI provides commands for creating and managing environments in WireMock Cloud.

## What is an Environment?

An environment is effectively a set of cloud mock APIs that represent an environment like `dev` or `staging`. Locally,
environments are represented by YAML config files which are overlaid on the base environment file and are activated via
the `--profile` CLI parameter for supported operations.

## Creating an Environment

You can create a new environment using the `environments create` command specifying the profile name.

```shell theme={null}
wiremock environments create --profile staging
```

Given a base wiremock environment file (`wiremock.yaml`) containing the following:

```yaml theme={null}
services:
  invoicing-api:
    type: REST
    cloud_id: 1234
    name: "Invoicing API"
    port: 8888
  payment-api:
    type: REST
    cloud_id: 4321
    name: "Payment API"
    port: 9999
```

The above `environments create` command will first check to see if an environment file exists (`wiremock-<profile-name>.yaml`)
for the given profile. If one does not exist, it will create a new mock API in WireMock Cloud for each service defined in
the base environment file.  The type of the new mock API will match the type defined in the base environment file. The
names of those mock APIs will be the same as the service names with the addition of a suffix of `[<profile-name>]`. A new
environment profile file will be created alongside the base environment file - `wiremock-<profile-name>.yaml`.

The contents of the new environment profile file will contain the same list of services with the `cloud_id` of the
new mock APIs created in WireMock Cloud:

```yaml theme={null}
services:
  invoicing-api:
    cloud_id: <mock-api-id>
  payment-api:
    cloud_id: <mock-api-id>
```

Before creating a new environment profile, the CLI will check to see if any mock APIs exist with the same name as
it will be creating. If there are any mock APIs with the same name, the CLI will not allow the creation of the new
profile file.

## Using an Environment

Using an environment is as simple as specifying the profile name when running any commands that support environments.
Doing so will read the profile file (`wiremock-<profile-name>.yaml`) and overlay it onto the configuration from
`wiremock.yaml`, overriding any matching attributes.

For example, given the following `wiremock.yaml` file:

```yaml theme={null}
services:
  invoicing-api:
    type: REST
    name: "Invoicing API"
    port: 8888
    cloud_id: 1234
    originals:
      default: http://private-endpoint1
  payment-api:
    type: REST
    name: "Payment API"
    port: 9999
    cloud_id: 4321
    originals:
      default: http://private-endpoint2
```

and the following environment `wiremock-staging.yaml` file:

```yaml theme={null}
services:
  invoicing-api:
    cloud_id: 6789
  payment-api:
    cloud_id: 9876
```

running the command:

```shell theme={null}
wiremock record-many --profile staging
```

would result in the file `wiremock-staging.yaml` being overlaid onto the main `wiremock.yaml` file and the following
configuration being used:

```yaml theme={null}
services:
  invoicing-api:
    type: REST
    name: "Invoicing API"
    port: 8888
    cloud_id: 6789
    originals:
      default: http://private-endpoint1
  payment-api:
    type: REST
    name: "Payment API"
    port: 9999
    cloud_id: 9876
    originals:
      default: http://private-endpoint2
```

In this instance, any recordings made using the `staging` environment will be imported to the `staging` mock APIs.

### Pulling Mock APIs from an Environment

The CLI provides the ability to [pull mock APIs from WireMock Cloud](/cli/push-pull-mock-api) into your local environment.
The pull mock APIs command also supports environments allowing you to specify the profile parameter to pull from a
specific environment, but the pull command works in a slightly different way when a profile is specified.

When pulling a mock API without specifying a profile, the CLI will pull the mock API from the base environment file and
download any stubs and API definition files to a directory named after the mock API.  The base environment file is updated
to include the information about the mock API (e.g. `cloud_id`, `name`, `path`, etc.).

When pulling a mock API with a profile specified, the CLI will pull the environment mock API but will only pull the data (stubs,
API definition files, etc.) and it will be pulled into the same `path` directory as specified in the base environment file.\
The base environment file will not be updated with the information about the environment mock API, effectively pulling
the mock API content but not the mock API metadata.

This feature supports the ability to manage ongoing changes to sets of mock APIs via a git-based workflow, using
environments and merge requests to control change to mock API configuration in the following way:

1. Your main environment file (`wiremock.yaml`) is checked into source control and defines your `production` environment and mock APIs.
2. You `pull` your production environment into your local environment using the `pull` command.
3. You create a new environment (`development`) using the `environments create` command. This will also create the mock APIs for the new environment.
4. You make changes to the environment mock APIs using WireMock Cloud or using the CLI `record-many` command and specifying the `development` profile.
5. When you are happy with the changes, you `pull` the `development` environment into your local environment using the `pull` command specifying the `development` profile.
   This will update your local environment with the changes from the `development` environment but only overwrite the content of the mock APIs as described above.
6. You create a merge request to merge the changes from the `development` environment into the `production` environment.
7. Your team members review the merge request and approve it.
8. The merge request is merged effectively updating the `production` environment with the changes from the `development`
   environment.

This workflow allows you to manage a version-controlled set of mock APIs where all changes are performed via environments
and git merge requests.

## Restrictions

The following restrictions apply when using environments:

1. The `wiremock-<profile-name>.yaml` file must not exist when creating a new environment.
2. No services can be added or removed via the environment profile file.  The same services with the same service keys
   must be present in the environment profile file as in the base environment file.
3. Certain information cannot be changed via the environment profile file.  The following attributes cannot be changed:
   * `type`


# Importing into WireMock Cloud
Source: https://docs.wiremock.io/cli/import

How to use the WireMock CLI to import stubs from WireMock OSS, HAR files, Postman collections, and OpenAPI/Swagger specifications

The WireMock CLI provides an `import` command that allows you to import stub mappings into WireMock Cloud from multiple sources:

* **WireMock OSS** projects (stub mapping JSON files)
* **HAR (HTTP Archive)** files captured from browser developer tools or proxy tools
* **Postman** collections
* **OpenAPI/Swagger** specifications

This is useful when migrating from other tools to WireMock Cloud, reusing existing API definitions, or converting recorded traffic into mock stubs.

## Basic Usage

To import stubs from a file or directory, use the following command:

```shell theme={null}
wiremock import <file_or_directory> --to=<mock-api-id>
```

where:

* `<file_or_directory>` is the path to file for import, or a WireMock project directory
* `<mock-api-id>` is the ID of the Mock API in WireMock Cloud that should receive the imported stubs

### Getting the Mock API ID

You can get the Mock API ID by browsing to your Mock API at [https://app.wiremock.cloud](https://app.wiremock.cloud) and extracting it from the URL. For instance, in the URL `https://app.wiremock.cloud/mock-apis/33eye3l9/stubs/1e0d7dc0-06a0-49a2-81a7-f5d6a40bfa3d`, the ID is `33eye3l9`.

## Supported Import Formats

The import command automatically detects the format of the input file or directory and processes it accordingly.

### WireMock OSS Format

WireMock OSS stub mappings are JSON files that define request matchers and responses.

#### Importing from a WireMock OSS Project Directory

When importing from a WireMock OSS project, you should specify the **parent directory** that contains the `mappings` and `__files` subdirectories, not the `mappings` directory itself.

For example, if you have a typical WireMock OSS project structure:

```
my-wiremock-project/
├── mappings/
│   ├── get-users.json
│   ├── post-user.json
│   └── delete-user.json
└── __files/
    └── users-response.json
```

You should import by pointing to the parent directory:

```shell theme={null}
wiremock import ./my-wiremock-project --to=33eye3l9
```

The CLI will automatically look for the `mappings` subdirectory within the specified path and import all stub mappings found there. If your stubs reference files in the `__files` directory (for body files), those will also be imported correctly.

#### Importing a Single WireMock Stub File

To import a single stub mapping file:

```shell theme={null}
wiremock import my-stub.json --to=33eye3l9
```

### HAR (HTTP Archive) Format

HAR files are JSON files that contain recorded HTTP traffic, typically captured from browser developer tools or HTTP proxy tools like Charles Proxy or Fiddler.

To import a HAR file:

```shell theme={null}
wiremock import recording.har --to=33eye3l9
```

The CLI will convert each HTTP request/response pair in the HAR file into a WireMock stub mapping.

**Example HAR file structure:**

```json theme={null}
{
  "log": {
    "entries": [
      {
        "request": {
          "method": "GET",
          "url": "https://api.example.com/users"
        },
        "response": {
          "status": 200,
          "content": {
            "text": "{\"users\": []}"
          }
        }
      }
    ]
  }
}
```

### Postman Collections

Postman collections can be exported from Postman and imported into WireMock Cloud. The CLI supports both Collection v2.0 and v2.1 formats.

To import a Postman collection:

```shell theme={null}
wiremock import my-collection.postman_collection.json --to=33eye3l9
```

The CLI will convert each request in the collection into a stub mapping, using:

* The request method, URL, headers, and body as matchers
* Example responses (if defined) as the stub response

### OpenAPI/Swagger Specifications

OpenAPI (formerly Swagger) specifications can be imported to automatically generate stub mappings for all defined endpoints.

To import an OpenAPI specification:

```shell theme={null}
wiremock import openapi-spec.yaml --to=33eye3l9
```

Or for JSON format:

```shell theme={null}
wiremock import openapi-spec.json --to=33eye3l9
```

The CLI will generate stub mappings for each endpoint defined in the specification, using:

* Path and method from the operation definition
* Example responses from the specification (if provided)
* Schema-based response generation (if no examples are provided)

<Note>Both OpenAPI 3.x and Swagger 2.0 formats are supported.</Note>

## Format Detection

The import command automatically detects the format of the input based on:

* File extension (`.har`, `.json`, `.yaml`, `.yml`)
* File content structure (Postman collection schema, OpenAPI schema, HAR format, WireMock stub format)
* Directory structure (presence of `mappings` and `__files` subdirectories for WireMock OSS)

You don't need to specify the format explicitly - the CLI will determine it automatically and process the file accordingly.

## Advanced Configuration

The `import` command supports advanced configuration through an import configuration file. This allows you to transform stub mappings during import, similar to how the [recording configuration](/cli/recording-configuration) works.

### Using an Import Configuration File

To use an import configuration file:

```shell theme={null}
wiremock import <file_or_directory> \
  --to=<mock-api-id> \
  --import-config-file=<path>
```

where `<path>` is the path to a YAML file containing import configuration.

The import configuration file uses the same format as the recording configuration file, allowing you to apply transformation rules to the imported stubs. This works with **all import formats** (WireMock OSS, HAR, Postman, OpenAPI/Swagger). This is useful when you need to:

* Modify request matchers to be more or less specific
* Add additional matching criteria
* Standardize stub definitions from different sources
* Apply consistent transformations when importing from multiple formats

For details on the configuration file format, see the [Advanced Recording Configuration](/cli/recording-configuration) page and the [import-config-file-schema](/cli/import-config-file-schema) reference.

## Notes

* The import command **adds** stubs to the specified Mock API without removing existing stubs
* If you want to replace all stubs in a Mock API, the [push](/cli/push-pull-mock-api) command may be more suitable

## See Also

* [Advanced Recording Configuration](/cli/recording-configuration) - for details on transformation rules
* [Import Config File Schema](/cli/import-config-file-schema) - for the complete schema reference
* [Pushing and Pulling Mock APIs](/cli/push-pull-mock-api) - for alternative ways to manage Mock API content


# Running Mock APIs Locally
Source: https://docs.wiremock.io/cli/local-playback

How to use the WireMock CLI to run your Mock APIs locally with the same capabilities as on WireMock Cloud

For enterprise customers the CLI offers the possibility of running your Mock APIs locally, removing the need to have a
connection to the internet.

## Getting Access

[Contact the WireMock team](https://www.wiremock.io/contact-now) to request a license file, which should be placed in
the appropriate configuration location for your operating system:

* Windows: `%LOCALAPPDATA%\wiremock-cli` (typically `C:\Users\{username}\AppData\Local\wiremock-cli`)
* macOs: `/Users/{username}/.config/wiremock-cli`
* Linux: `$XDG_CONFIG_HOME/wiremock-cli` (typically `/home/{username}/.config/wiremock-cli`)

## Usage

First you will need to pull one or more of your Mock APIs locally.  This can be done by running the `pull mock-api`
command as detailed [here](./push-pull-mock-api).

Once you have pulled one or more of your Mock APIs, you can then run them as so:

```shell theme={null}
wiremock run
```

This will run all the Mock APIs you have pulled down into the `.wiremock` directory. A table will be printed showing you
which port is being used for which API.

(Naturally you can pass the same `--wiremock-dir` argument to override the default `.wiremock` directory.)

### TLS Usage

You can run your Mock APIs locally using a TLS certificate of your choice. You configure this by editing the local
environment config file, `.wiremock/wiremock.yaml`, and specifying your https settings:

```yaml theme={null}
services:
  local-running-service-name:
    https:
      port: <local port to bind to>
      certificate: <certificate details>
```

If you have a file containing a PEM encoded RSA private key and X509 certificate, you can provide it as so:

```yaml theme={null}
certificate:
  pem: /path/to/file.pem
```

A PEM encoded file should look something like this:

```
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDHIpsyRDeM1lFQ
<multiple lines of base64 encoded data>
GhxuZ3ceXiqwvhH8Yt5gNs0=
-----END PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
MIIDrzCCApegAwIBAgIUR24W6NZN7xPwSqc59usFQ37HPYswDQYJKoZIhvcNAQEL
<multiple lines of base64 encoded data>
dHhXPaefkEhrsUbnXGYRfwQhf4SzdYCMCJno7KKsNn6RLIo=
-----END CERTIFICATE-----
```

If you have a PKCS 12 key store containing your private key and X509 certificate, you can provide it as so:

```yaml theme={null}
certificate:
  keystore: /path/to/keystore.p12
  password: very_secret
  alias: key_alias # optional - if omitted, the first entry in the key store is used
```

If you wish to use the same certificate across multiple services, you may specify it as so:

```yaml theme={null}
global:
  https:
    certificate: <certificate details>
services:
  local-running-service-name:
    https:
      port: <local port to bind to>
```

Any service with an `https` section will then use that certificate by default.

You may still provide a specific certificate for any individual service:

```yaml theme={null}
global:
  https:
    certificate:
      pem: /path/to/global-cert.pem
services:
  service-using-specific-certificate:
    https:
      port: <local port to bind to>
      certificate:
        pem: /path/to/specific-cert.pem
  service-using-default-certificate:
    https:
      port: <local port to bind to>
```

In addition, you can specify a global keystore but reference different certificates in it by alias for a given service:

```yaml theme={null}
global:
  https:
    certificate:
      keystore: /path/to/keystore.p12
      password: very_secret
      alias: default_key_alias
services:
  service-using-specific-alias:
    https:
      port: <local port to bind to>
      certificate:
        alias: service_specific_key_alias
  service-using-default-alias:
    https:
      port: <local port to bind to>
```

If you do not provide any certificate details, your services will run using our default self-signed certificate.

## Running in a Container

The CLI is published to Docker Hub as [`wiremock/wiremock-cli`](https://hub.docker.com/r/wiremock/wiremock-cli). By
default, it executes the `run` command, but in order for the `run` command to be able to operate you must mount your
config directory to `/etc/wiremock-cli` and the working directory containing your mock APIs to `/work`.

You will also need to [publish the appropriate ports](https://docs.docker.com/reference/cli/docker/container/run/#publish)
for the services you are running.

Here is a typical example on Linux or macOs when running two Mock APIs:

```shell theme={null}
docker run \
  -v ~/.config/wiremock-cli:/etc/wiremock-cli \
  -v $(pwd):/work \
  -p 8080:8080 \
  -p 8081:8081 \
  wiremock/wiremock-cli:latest
```

## Telemetry

The `wiremock run` command can be configured to export OpenTelemetry signals to a backend of your choice.
Configuration is done via environment variables, as specified by [the OpenTelemetry specification](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/).

For example, to emit logs to a backend that supports [OTLP](https://opentelemetry.io/docs/specs/otel/protocol/)
at the endpoint `https://my-telemetry-service:8080`, set the following environment variables:

* `OTEL_LOGS_EXPORTER=otlp`.
* `OTEL_EXPORTER_OTLP_ENDPOINT=https://my-telemetry-service:8080`.

Supported values for `OTEL_TRACES_EXPORTER`, `OTEL_METRICS_EXPORTER`, `OTEL_LOGS_EXPORTER` are:

* `otlp`: [OTLP](https://opentelemetry.io/docs/specs/otel/protocol/exporter/)
* `console`: [Standard Output](https://opentelemetry.io/docs/specs/otel/logs/sdk_exporters/stdout/)
* `none`: No automatically configured exporter.

If no OTEL environment variables are set, the specification defaults are obeyed, except `OTEL_TRACES_EXPORTER`,
`OTEL_METRICS_EXPORTER`, and `OTEL_LOGS_EXPORTER`, which are all set to `none` by default, rather than `otlp`.

These telemetry options also apply to [the WireMock Runner's `serve` mode](/runner/serve#telemetry).


# Managing Mock APIs with the CLI
Source: https://docs.wiremock.io/cli/mock-apis

How to list and manage your mock APIs using the WireMock CLI

The CLI provides commands for interacting with your mock APIs in WireMock Cloud.

## Listing Mock APIs

You can list your mock APIs using:

```shell theme={null}
wiremock mock-apis list
```

This will display your mock APIs in a human-readable text format. By default, it shows up to 20 results on the first page.

### Options

The list command supports several options to customize the output:

* `--limit=<int>` - Set the maximum number of mock APIs to return (default: 20)
* `--page=<int>` - Select which page of results to show (default: 1)
* `--query=<text>` - Filter mock APIs using a search query
* `-o, --output=(text|json)` - Choose between text or JSON output format (default: text)

### Examples

List first 5 mock APIs:

```shell theme={null}
wiremock mock-apis list --limit 5
```

Search for mock APIs containing "test":

```shell theme={null}
wiremock mock-apis list --query test
```

Get results in JSON format:

```shell theme={null}
wiremock mock-apis list --output json
```

## Creating Mock APIs

You can create a new mock API using:

```shell theme={null}
wiremock mock-apis create <name>
```

This will create a new mock API with the given name.

### Options

The create command supports the following options:

* `-o, --hostname=<text>` - Optional custom hostname for the mock API
* `-t, --type=(REST|Unstructured|gRPC|GraphQL)` - Type of the mock API (default: REST)

### Examples

Create a new mock API called `NewName`

```shell theme={null}
wiremock mock-apis create NewName
```

Create a new mock API of type `GraphQL`

```shell theme={null}
wiremock mock-apis create --type GraphQL NewName
```

Create a new mock API of type `Unstructured` with a custom hostname

```shell theme={null}
wiremock mock-apis create --type Unstructured -o newname NewName
```

## Delete a mock API

You can delete a new mock API using:

```shell theme={null}
wiremock wiremock mock-apis delete <mock_api_id>
```

This will delete the mock API with the given ID.  By default, it will prompt you for confirmation before deleting the
mock API.

### Options

The delete command supports the following options:

* `-f, --force` - Force delete the mock API without confirmation

### Examples

Delete a mock API with ID `v16kg`

```shell theme={null}
wiremock mock-apis delete v16kg
```

Force delete a mock API with ID `v16kg`

```shell theme={null}
wiremock mock-apis delete -f v16kg
```


# Multi-domain recording using the WireMock CLI
Source: https://docs.wiremock.io/cli/multi-domain-recording

How to use the WireMock CLI to record stubs from multiple private endpoints

The CLI offers a convenient way to record stubs from multiple endpoints that are accessible from the computer running
the CLI, but not accessible from the internet. This is achieved by the use of the cli `record-many` command and the
WireMock environment config file, `wiremock.yaml`. The environment configuration file specifies all the services you are
recording:

```yaml theme={null}
services:
  invoicing-api:
    type: <mock_api_type>
    name: "Invoicing API"
    port: 8888
    cloud_id: <mock_api_id>
    originals:
      default: http://private-endpoint1
  payment-api:
    type: <mock_api_type>
    name: "Payment API"
    port: 9999
    cloud_id: <mock_api_id>
    originals:
      default: http://private-endpoint2
```

In the above configuration file, the `cloud_id` field specifies the Mock API you want to save to where `<mock_api_id>`
is the ID of the Mock API that should receive the recorded stubs. At present you can get that value by browsing into a
Mock API at [https://app.wiremock.cloud](https://app.wiremock.cloud) and extracting it from the URL - for instance in the URL
`https://app.wiremock.cloud/mock-apis/33eye3l9/stubs/1e0d7dc0-06a0-49a2-81a7-f5d6a40bfa3d`, the ID is `33eye3l9`.

If you don't already have a Mock API in WireMock Cloud that you are recording to, you can omit the `cloud_id` field
from your service definition and the WireMock CLI will create a new Mock API for you before saving the recorded stubs.
The environment config file will be updated with the ID of the created Mock Api.

The `type` field specifies the type of the Mock API you are saving to. This field allows the 4 Mock API types supported
by WireMock Cloud:

* REST
* gRPC
* GraphQL
* Unstructured

The `port` field allows you to specify the port number the WireMock CLI will listen on when recording to the endpoint
specified in the `originals` -> `default` field. The `port` field specified should be unique across all the services
you are specifying in your environment configuration.  This is unless you are using a dynamic port where you would
specify `0` or `-1` as the port.

To start a multi-domain recording session, you would run:

```shell theme={null}
wiremock record-many --wiremock-dir <path>
```

Where `<path>` is the path to the directory containing your saved `wiremock.yaml` environment configuration file. By
default this will be a directory called `.wiremock` in the current working directory, so the CLI will look for
`./.wiremock/wiremock.yaml`.

The CLI will then run a proxy server for each of the services you have configured, bound to `http://localhost:<port>`
where the port is the port you specified in the configuration file. Requests to those endpoints will be proxied to the
endpoint you want to record from. When you have finished the journey you want to record, press `<enter>` to save the
stubs to your Mock API in WireMock Cloud and the CLI will exit.

## Choosing which services to record

It may be convenient to run a multi-domain recording session where all services defined in the environment configuration
file are proxying through to the real service, but you only wish to actually record stubs for a subset of those
services.

You can achieve this using the `--include-services` option with a value that is a comma separated list of the  YAML keys
(as defined in the environment configuration file) of the services you wish to record.

```shell theme={null}
wiremock record-many --include-services invoicing-api,payment-api
```

Only services in this list will be recorded; however, if the option is omitted entirely all services in the environment
configuration file will be recorded.

## Importing recordings as you go along

By default, all the recorded requests are held in memory, and sent to the destination Mock API in WireMock Cloud at the
end of the recording session.

This may not be desirable; if you are doing a long recording session this may be prone to losing too much work. If you
are doing a very large recording session the resulting import may be too large for WireMock Cloud (or other intermediate
infrastructure) to cope.

You may use the `--max-batch-requests` option to specify the maximum amount of requests to import into the destination
Mock API in a single request.
Given a max batch of N requests, an import to the mock API will occur for every N requests recorded.

The `--max-batch-bytes` option is also available if you need control over the exact amount of bytes that can be sent in
a single request to the destination Mock API.
Given a max batch of N bytes, an import to the mock API will occur for every N bytes recorded.
Note, if a single recorded request exceeds the maximum number of bytes, this request will still be sent (in a batch of
one).

## Advanced Recording

The WireMock CLI accepts a configuration file to control how stubs are recorded:

```shell theme={null}
wiremock record-many --import-config-file=<path>
```

The format of this file is documented in the [advanced recording configuration page](/cli/recording-configuration).

## Recording with TLS

You can run your recording proxy using a TLS certificate of your choice.
This can be configured by editing the local environment config file, `.wiremock/wiremock.yaml`, and specifying your HTTPS settings:

```yaml theme={null}
services:
  local-running-service-name:
    https:
      port: <local port to bind to>
      certificate: <certificate details>
```

If you have a file containing a PEM encoded RSA private key and X509 certificate, you can provide it as so:

```yaml theme={null}
certificate:
  pem: /path/to/file.pem
```

A PEM encoded file should look something like this:

```
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDHIpsyRDeM1lFQ
<multiple lines of base64 encoded data>
GhxuZ3ceXiqwvhH8Yt5gNs0=
-----END PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
MIIDrzCCApegAwIBAgIUR24W6NZN7xPwSqc59usFQ37HPYswDQYJKoZIhvcNAQEL
<multiple lines of base64 encoded data>
dHhXPaefkEhrsUbnXGYRfwQhf4SzdYCMCJno7KKsNn6RLIo=
-----END CERTIFICATE-----
```

If you have a PKCS 12 key store containing your private key and X509 certificate, you can provide it as so:

```yaml theme={null}
certificate:
  keystore: /path/to/keystore.p12
  password: very_secret
  alias: key_alias # optional - if omitted, the first entry in the key store is used
```

If you wish to use the same certificate across multiple services, you may specify it as so:

```yaml theme={null}
global:
  https:
    certificate: <certificate details>
services:
  local-running-service-name:
    https:
      port: <local port to bind to>
```

Any service with an `https` section will then use that certificate by default.

You may still provide a specific certificate for any individual service:

```yaml theme={null}
global:
  https:
    certificate:
      pem: /path/to/global-cert.pem
services:
  service-using-specific-certificate:
    https:
      port: <local port to bind to>
      certificate:
        pem: /path/to/specific-cert.pem
  service-using-default-certificate:
    https:
      port: <local port to bind to>
```

In addition, you can specify a global keystore but reference different certificates in it by alias for a given service:

```yaml theme={null}
global:
  https:
    certificate:
      keystore: /path/to/keystore.p12
      password: very_secret
      alias: default_key_alias
services:
  service-using-specific-alias:
    https:
      port: <local port to bind to>
      certificate:
        alias: service_specific_key_alias
  service-using-default-alias:
    https:
      port: <local port to bind to>
```

If you do not provide any certificate details, the proxy will use our default self-signed certificate.

## Recording with Mutual TLS

If you need to record from an API that authenticates clients with mutual TLS, the CLI can present your private client
certificate in one of two ways:

### Via a PEM file

If you have a file containing a PEM encoded RSA private key and X509 certificate, you can provide it as so:

```shell theme={null}
wiremock record-many \
  --client-certificate=/path/to/file.pem
```

A PEM encoded file should look something like this:

```
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDHIpsyRDeM1lFQ
<multiple lines of base64 encoded data>
GhxuZ3ceXiqwvhH8Yt5gNs0=
-----END PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
MIIDrzCCApegAwIBAgIUR24W6NZN7xPwSqc59usFQ37HPYswDQYJKoZIhvcNAQEL
<multiple lines of base64 encoded data>
dHhXPaefkEhrsUbnXGYRfwQhf4SzdYCMCJno7KKsNn6RLIo=
-----END CERTIFICATE-----
```

### Using a PKCS 12 certificate store

Keeping a private key in PEM format is a security risk, so we also support supplying your client certificate in a
password protected PKCS 12 store as so:

```shell theme={null}
wiremock record-many \
  --client-certificate-store=/path/to/file.pkcs12
```

You will be challenged for a password to decrypt the store and the private key. The same password must be able to
decrypt both.

## Hostname rewriting

Often API responses contain absolute links and other content that refers to the domain name of the API's origin.
When recording an API this can be undesirable as the local proxy is different from the API being recorded, and thus any
client following such a link would make its next request directly to the proxy target rather than the local CLI running
the proxy.

To remedy this issue, the Record-Many command has **hostname rewriting enabled by default**, which will replace any
instances of the proxy target's domain name and port in the response headers or body with the local proxy's domain name
and port.

If this is not the behaviour you want when recording, you can configure hostname rewriting on a per-service basis by adding
the `rewriteOriginHostname` field to the service:

```yaml theme={null}
services:
  invoicing-api:
    type: <mock_api_type>
    name: "Invoicing API"
    port: 8888
    cloud_id: <mock_api_id>
    rewriteOriginHostname: false
    originals:
      default: http://private-endpoint1
  payment-api:
    type: <mock_api_type>
    name: "Payment API"
    port: 9999
    cloud_id: <mock_api_id>
    originals:
      default: http://private-endpoint2
```

This can also be configured for all services in the `global` configuration section of your `wiremock.yaml` file:

```yaml theme={null}
global:
  rewriteOriginHostname: false

services:
  invoicing-api:
    type: <mock_api_type>
    name: "Invoicing API"
    port: 8888
    cloud_id: <mock_api_id>
    originals:
      default: http://private-endpoint1
  payment-api:
    type: <mock_api_type>
    name: "Payment API"
    port: 9999
    cloud_id: <mock_api_id>
    originals:
      default: http://private-endpoint2
```

After setting `rewriteOriginHostname: false` globally, you can still enable it for specific services.

## Non-interactive Recording Sessions

The WireMock CLI `record-many` command supports running in non-interactive mode, making it ideal for
CI/CD pipelines and automated environments where user interaction is not possible or desired. See the
[Non-interactive Recording](/cli/non-interactive-recording) for more details.

## Recording to an Environment

The WireMock CLI `record-many` command supports recording to an environment via the use of the `--profile` parameter.
See the [Environments](/cli/environments) page for more details.

## Recording gRPC Services

The WireMock CLI and WireMock Runner support recording gRPC APIs, but require some additional configuration to other API types.
In order for the recorder to intercept and marshall gRPC requests and responses, a [descriptor file](/grpc/overview#generating-a-descriptor-set-file) must be provided.

If a gRPC mock API already exists in WireMock Cloud ([with a descriptor file uploaded](/grpc/overview#uploading-a-descriptor-set-file)),
then running the `pull mock-api` command, as detailed [here](/cli/push-pull-mock-api), will ensure the descriptor file is available to the recorder.

For newly recorded gRPC APIs, add a `path` field to the gRPC service configuration in your `.wiremock/wiremock.yaml`
file whose value is a file path pointing to a directory containing a descriptor file named `grpc.dsc`.
For example, given a `wiremock.yaml` file with the following contents

```yaml theme={null}
services:
  my-grpc-service:
    type: gRPC
    name: "My gRPC Service"
    port: 8888
    path: ./my-grpc-service
    originals:
      default: https://grpc.example.com
```

the file tree must resemble the following structure

```
.wiremock
├── my-grpc-service
│   └── grpc.dsc
└── wiremock.yaml
```


# Non-interactive Recording Sessions
Source: https://docs.wiremock.io/cli/non-interactive-recording

How to use the WireMock CLI to record in a non-interactive way

As of version `0.28.0`, the WireMock CLI supports running recording commands in non-interactive mode, making it ideal
for CI/CD pipelines and automated environments where user interaction is not possible or desired. The CLI automatically
detects whether it's running in an interactive terminal and adjusts its behavior accordingly.

## Interactive vs Non-Interactive Mode

There are a number of differences between interactive and non-interactive modes:

### Interactive Mode (Default)

* **User Control**: User presses Enter to stop recording or ESC to cancel
* **Request Logging**: Default request log level is `summary` - shows incoming requests during recording
* **Output**: Displays progress messages and prompts in the terminal for user input

### Non-Interactive Mode

* **Signal Control**: Process responds to system signals (SIGTERM) for termination
* **Request Logging**: Default request log level is `off` - minimal console output for cleaner logs.  This can still be
  overridden with the `--request-log-level` option.
* **Output**: Reduced console output optimized for log parsing

## Signal Handling and Process Termination

### Graceful Shutdown

Non-interactive recording sessions respond to the standard **SIGTERM** Unix signal:

* **SIGTERM**: Graceful shutdown - stops recording and processes all captured traffic

### Using `pkill` for Termination

The recommended approach for terminating recording processes is using `pkill` with the SIGTERM signal:

```bash theme={null}
# Start recording in background
wiremock record --to=cloud:<mock_api_id> https://api.example.com > wiremock.log 2>&1 &
WIREMOCK_PID=$!

# Later, gracefully terminate the process and
pkill -TERM -P $WIREMOCK_PID
```

### Example Termination Script

```bash theme={null}
#!/bin/bash

# Start WireMock recording
wiremock record --to=cloud:<mock_api_id> https://api.example.com > wiremock.log 2>&1 &
WIREMOCK_PID=$!

# Perform your HTTP requests here
# ...

# Graceful termination
echo "Terminating WireMock CLI (PID: $WIREMOCK_PID)..."
pkill -TERM -P $WIREMOCK_PID 2>/dev/null

# Wait for graceful shutdown (with timeout)
TIMEOUT=10
COUNT=0
while kill -0 $WIREMOCK_PID 2>/dev/null && [ $COUNT -lt $TIMEOUT ]; do
    sleep 1
    COUNT=$((COUNT + 1))
done

# Display the captured output
echo ""
echo "=== WireMock CLI Output ==="
cat wiremock.log

echo ""
```

The above examples show the `record` command, but the same approach applies to `record-many`.  They also show output
redirection to a log file.


# WireMock CLI
Source: https://docs.wiremock.io/cli/overview

How to use the WireMock CLI

## Overview

The WireMock CLI offers ways to get benefits of WireMock Cloud that are hard or impossible to achieve using the web
interface.

## Installation

You can install the WireMock CLI using npm:

```shell theme={null}
npm install --global @wiremock/cli
```

## Usage

A list of available commands can be found as follows:

```shell theme={null}
wiremock -h
```

For any given command, additional help can be found as follows:

```shell theme={null}
wiremock <command> -h
```

e.g.

```shell theme={null}
wiremock record -h
```

### Setting command options

Most commands provided by the WireMock CLI take options that control how the command is executed.
For example, the `record-many` command can take a `--request-log-level` option like so:

```shell theme={null}
wiremock record-many --request-log-level=full
```

In some cases, specifying these options directly on the command line is undesirable.
For instance, if you wanted to always execute the `record-many` command with a default set of option values, it would
be simpler to persist these values somewhere that the CLI could read without having to type them into the terminal
every time.

Another use case where writing values on the command line is problematic is when sensitive data is contained within
option values.
For options that commonly take sensitive data, the WireMock CLI will revert to prompting you for the option value via
stdin (if it's not provided directly on the command line), but interactive prompting is not possible on non-interactive
terminals.

For the cases where providing option values via the command line is not desirable, it is possible to set command
options via environment variables and/or in a values file:

#### Environment variables

All CLI options (except for helper options like `--help`) can be specified via environment variables.
The name of the environment variable always follows the pattern `WMC_<SUBCOMMAND_NAME>_<OPTION_NAME>` where
`<SUBCOMMAND_NAME>` is the name of the subcommand, that the option is relevant to, and `<OPTION_NAME>` is the name of
the option itself.
Note that all dashes (`-`) are replaced by underscores (`_`).
For example,

```shell theme={null}
WMC_RECORD_MANY_REQUEST_LOG_LEVEL=full wiremock record-many
```

is equivalent to

```shell theme={null}
wiremock record-many --request-log-level=full
```

Options for nested subcommands, such as `wiremock mock-apis list`, delimit their subcommand names with underscores
(`_`), like so:

```shell theme={null}
WMC_MOCK_APIS_LIST_OUTPUT=json wiremock mock-apis list
```

Flag options, such as the `--watch` option of `wiremock push open-api`, can be specified via a boolean value.
For example,

```shell theme={null}
WMC_PUSH_OPEN_API_WATCH=true wiremock push open-api
```

#### Values file

All CLI options (except for helper options like `--help`) can be specified within a YAML values file.
Option values must be provided as nested fields within their respective subcommand objects.
Note that all dashes (`-`) are replaced by underscores (`_`).
For example, consider the following values file:

```yaml theme={null}
record_many:
  request_log_level: full
```

Running `wiremock record-many` with this values file is equivalent to

```shell theme={null}
wiremock record-many --request-log-level=full
```

The default path that the CLI will use to look for a values file is `.wiremock/config.yaml` within the working
directory that the command was executed in.
This path can be overridden by setting the environment variable `WMC_VALUES_CONFIG_FILE` to a custom file path.

<Note>
  Note that setting the `--wiremock-dir` option on commands such as `record-many` will not affect where the CLI will
  search for the default values file.
</Note>

Options for nested subcommands, such as `wiremock mock-apis list`, are nested like so:

```yaml theme={null}
mock_apis:
  list:
    output: json
```

Flag options, such as the `--watch` option of `wiremock push open-api`, can be specified via a boolean value.
For example,

```yaml theme={null}
push:
  open_api:
    watch: true
```

#### Precedence

Providing options via the command line, environment variables and a values files can be used interchangeably and mixed.
Option values provided via the command line take precedence over those provided via environment variables, which in
turn take precedence over those specified in the values file.

### Installing command completion

The WireMock CLI includes a command completion feature that enables you to use the `Tab` key to complete a partially entered command, argument or option.
To set up this feature for your shell, run the following command

```shell theme={null}
wiremock completion init
```

This will take you through the steps required to install the completion script and configure your shell to use this script.

Currently supported shells are [bash](https://www.gnu.org/software/bash/), [zsh](https://www.zsh.org/), and [fish](https://fishshell.com/).

## Current Commands

### Login

Most commands require you to have authenticated with WireMock Cloud. You can achieve this by running:

```shell theme={null}
wiremock login
```

and following the instructions.

<Info>
  If you have [set your API endpoint](/cli/config#configuring-your-api-endpoint) to a custom endpoint,
  `wiremock login` will no longer work, so [setting your API token using the config
  subcommand](/cli/config#configuring-your-api-token) is the only available method for authenticating.
</Info>

### Checking if logged in

Running

```shell theme={null}
wiremock whoami
```

will either report the currently logged in user and exit successfully, or fail reporting that no-one is logged in.

### Logout

Running

```shell theme={null}
wiremock logout
```

will log the current user out.

### Config

Command for configuring your WireMock CLI installation. See [Configuring the CLI](/cli/config) for details.

### Mock APIs

Commands for managing your mock APIs. See [Managing Mock APIs with the CLI](/cli/mock-apis) for details.

### Local Run

Command for running your mock APIs locally. See [Running Mock APIs Locally](/cli/local-playback) for details.

### Record

See detailed documentation at [Recording using the WireMock CLI](/cli/recording/)

### Record Many

See detailed documentation at [Multi-domain recording using the WireMock CLI](/cli/multi-domain-recording/)

### MCP

Runs an MCP server for use with AI tools. Intended to be called from the AI tool's MCP configuration rather than directly in the terminal.

See detailed documentation at [WireMock Cloud AI](/ai-mcp/installation/)


# Pushing and Pulling Documents
Source: https://docs.wiremock.io/cli/push-pull

How to use the WireMock CLI to push and pull OpenAPI documents and GraphQL schemas to your Mock APIs

Some types of Mock APIs have documents associated with them: REST APIs have an OpenAPI document, and GraphQL APIs have a
GraphQL schema.

The CLI allows you to both pull these documents down to your local machine and push them from your local machine into
the WireMock Cloud Mock API.

In addition it can watch a file on your local machine, pushing it into the WireMock Cloud Mock API every time it
changes.

## Usage

Both pull and push commands accept a document type as the first argument and a Mock API ID as the second:

```shell theme={null}
wiremock <pull|push> <document-type> <mock-api-id>
```

where `<mock_api_id>` is the ID of the Mock API that should receive the recorded stubs. At present you can get that
value by browsing into a Mock API at [https://app.wiremock.cloud](https://app.wiremock.cloud) and extracting it from the URL - for instance in the URL
`https://app.wiremock.cloud/mock-apis/zwg1l/stubs/1e0d7dc0-06a0-49a2-81a7-f5d6a40bfa3d`, the ID is `zwg1l` so you
should pull its OpenAPI as so:

```shell theme={null}
wiremock pull open-api zwg1l
```

At present, valid document types are `open-api` and `graphql`. The Mock API should be of the appropriate type (defined
at Mock API creation time).

All the commands have an optional `-f` or `--file` option, specifying the file to either save the document to (for pull)
or send as the document (for push):

```shell theme={null}
wiremock pull open-api zwg1l --file /tmp/zwg1l-open-api.yaml
wiremock push open-api zwg1l --file /tmp/zwg1l-open-api.yaml
```

If omitted, the document is printed to stdout (for pull) or read from stdin (for push).

### Watching

The `push` commands have an additional `-w` / `--watch` which require the file to be defined with `-f` / `--file`.

It will leave the CLI running and automatically push the file whenever it is saved.


# Pushing and Pulling Mock API
Source: https://docs.wiremock.io/cli/push-pull-mock-api

How to use the WireMock CLI to push and pull entire Mock APIs

## Pulling a Mock API from WireMock Cloud

The CLI allows you to pull down a Mock API from WireMock Cloud.  This is required if you want to run a Mock API locally
via the [local runner](./local-playback).

Mock APIs can be pulled down by running the following command:

```shell theme={null}
wiremock pull mock-api <mock-api-id>
```

Multiple Mock APIs can be pulled with one command by appending multiple ids:

```shell theme={null}
wiremock pull mock-api <mock-api-id> <mock-api-id> <mock-api-id>
```

At present you can get the Mock API ID by browsing into a Mock API at [https://app.wiremock.cloud](https://app.wiremock.cloud) and extracting it from
the URL - for instance in the URL `https://app.wiremock.cloud/mock-apis/33eye3l9/stubs/1e0d7dc0-06a0-49a2-81a7-f5d6a40bfa3d`,
the ID is `33eye3l9`.

This will create a `.wiremock` directory in the current working dir, and populate it with the necessary files to be able
to run the identified Mock API.

You can pass a `--wiremock-dir` argument to override the default `.wiremock` directory.

Inside the `.wiremock` directory you will find the WireMock environment file which contains all the Mock APIs you have
pulled down.  This is a `yaml` file in the following format:

```yaml theme={null}
services:
  <service-id>:
    type: '<mock_api_type>'
    name: 'Mock API name'
    cloud_id: '<mock-api-id>'
    path: './mock-api-name'
    port: 8080
```

The `type` field specifies the type of the Mock API you have just pulled down. This field allows the 4 Mock API types
supported by WireMock Cloud:

* REST
* gRPC
* GraphQL
* Unstructured

The `port` field specifies the port that the local mock api will run on.

The `path` field specifies the path to the Mock API directory.  This is where all the files relating to the Mock API
will be stored.  If the Mock API contains any stubs, they will be stored in the `stub-mappings.yaml` file along with
the OpenAPI specification if the Mock API is a REST Mock API and the GraphQL schema if the Mock API is a GraphQL Mock API.

### Re-pulling Mock APIs defined in the WireMock environment file

If you have modified your Mock APIs in WireMock Cloud, you can re-pull them by running the `pull mock-api` command
again.  This will overwrite any changes you have made locally.  To do this you can run the same command as before\
specifying the Mock API ID:

```shell theme={null}
wiremock pull mock-api <mock-api-id>
```

Or multiple Mock APIs can be pulled with one command by appending multiple ids:

```shell theme={null}
wiremock pull mock-api <mock-api-id> <mock-api-id> <mock-api-id>
```

Or you can run the `pull mock-api` command specifying the `<service-id>` from your local WireMock environment file:

For example, if your WireMock environment file contains the following:

```yaml theme={null}
services:
  payment-mock-api:
    type: 'Unstructured'
    name: 'Payment Mock API'
    cloud_id: '23der3'
    path: './payment-mock-api'
    port: 8080
```

You can re-pull the Mock API by running the following command:

```shell theme={null}
wiremock pull mock-api payment-mock-api
```

As with pulling multiple Mock APIs, you can re-pull multiple services by appending multiple `<service-id>`:

```shell theme={null}
wiremock pull mock-api payment-mock-api order-mock-api
```

If you want to re-pull all the Mock APIs you have defined in your local WireMock environment file, you can run the
`pull mock-api` command without any mock API ID or service ID and specifying the `--all` flag:

```shell theme={null}
wiremock pull mock-api --all
```

The `--into=<service-id>` flag can be used to pull data into an existing service in the WireMock environment file. In
this case, only stub mappings and API documents will be updated; service settings in wiremock.yaml will remain unchanged.

### Pulling Mock APIs from an Environment

The WireMock CLI `pull` command supports pulling mock APIs from an environment via the use of the `--profile` parameter.
When doing so, the `--into` parameter is not allowed to be used.  The `--profile` parameter can be used to specify the
name of the environment to pull from.  When pulling from an environment, the pull command only pulls the content of the
mock APIs and the environment file is not updated.

See the [Environments](/cli/environments#pulling-mock-apis-from-an-environment) page for more details.

## Pushing a Mock API to WireMock Cloud

As well as pulling down Mock APIs, you can push them back up to the WireMock Cloud.  This is useful if you have made any
changes to your stubs or api definition documents locally and want those changes to be reflected in the WireMock Cloud.

To push a Mock API to WireMock Cloud, run the following command:

```shell theme={null}
wiremock push mock-api <service-id>
```

You can also push multiple Mock APIs at once by appending multiple `<service-id>`:

```shell theme={null}
wiremock push mock-api payment-mock-api order-mock-api
```

By default, the local Mock API will be pushed to the Mock API with the same `cloud_id` from the WireMock environment file.
This can be overridden by specifying the `--to=cloud:<cloud-id>` flag.  If you want to push the local Mock API to a
new Mock API, you can specify the `--to=cloud:new` flag.

As with the `pull` command, you can pass a `--wiremock-dir` argument to override the default `.wiremock` directory.

If the `cloud_id` is missing from the local mock api definition, the `push` command will try to create a new Mock API
in WireMock Cloud before pushing the local Mock API.

If you want to push all the Mock APIs defined in your local WireMock environment file, you can run the `push mock-api`
command without any service ID and specifying the `--all` flag:

```shell theme={null}
wiremock push mock-api --all
```

<Warning>
  It is important to note that pushing a local Mock API to WireMock Cloud will overwrite the existing Mock API.  This
  means that any stubs added or modified or changes made to the api definition documents (OpenApi document or GraphQL
  schema) will be lost when you push the local Mock API via the CLI.  This feature is to be used with care.
</Warning>


# Recording via the CLI
Source: https://docs.wiremock.io/cli/recording

How to use the WireMock CLI to record stubs from private endpoints

<Note>
  Recording gRPC APIs is currently only supported by the `record-many` command.
  See [here](/cli/multi-domain-recording#recording-grpc-services) for details.
</Note>

The CLI offers a convenient way to record stubs from endpoints that are accessible from the computer running the CLI,
but not accessible from the internet. Run:

```shell theme={null}
wiremock record http://private-endpoint
```

At the end of your recording you will be asked to choose the Mock API to which you would like to save the recorded
stubs, or create a new Mock API.

If you know the ID of the Mock API you want to save to, you can skip the prompt by passing it as an argument:

```shell theme={null}
wiremock record http://private-endpoint --to=cloud:<mock_api_id>
```

where `<mock_api_id>` is the ID of the Mock API that should receive the recorded stubs. At present you can get that
value by browsing into a Mock API at [https://app.wiremock.cloud](https://app.wiremock.cloud) and extracting it from the URL - for instance in the URL
`https://app.wiremock.cloud/mock-apis/33eye3l9/stubs/1e0d7dc0-06a0-49a2-81a7-f5d6a40bfa3d`, the ID is `33eye3l9` so you
should record as so:

```shell theme={null}
wiremock record http://private-endpoint --to=cloud:33eye3l9
```

This will be made easier in future versions!

The CLI will then run a proxy server bound to [http://localhost:8000](http://localhost:8000). Requests to this endpoint will be proxied to the
endpoint you want to record from. When you have finished the journey you want to record, press `<enter>` to save the
stubs to your Mock API in WireMock Cloud and the CLI will exit.

You can specify the port the server should listen on using `-p` or `--reverse-proxy-port`:

```shell theme={null}
wiremock record http://private-endpoint --to=cloud:33eye3l9 \
  --reverse-proxy-port=8080
```

## Importing recordings as you go along

By default, all the recorded requests are held in memory, and sent to the destination Mock API in WireMock Cloud at the
end of the recording session.

This may not be desirable; if you are doing a long recording session this may be prone to losing too much work. If you
are doing a very large recording session the resulting import may be too large for WireMock Cloud (or other intermediate
infrastructure) to cope.

You may use the `--max-batch-requests` option to specify the maximum amount of requests to import into the destination
Mock API in a single request.
Given a max batch of N requests, an import to the mock API will occur for every N requests recorded.
This requires you to specify the ID of the Mock API you want to save to via the `--to` option when launching the session.

The `--max-batch-bytes` option is also available if you need control over the exact amount of bytes that can be sent in
a single request to the destination Mock API.
Given a max batch of N bytes, an import to the mock API will occur for every N bytes recorded.
Note, if a single recorded request exceeds the maximum number of bytes, this request will still be sent (in a batch of
one).
Like `max-batch-requests`, this option requires you to provide a value to the `--to` option when launching the session.

## Hostname rewriting

Often API responses contain absolute links and other content that refers to the domain name of the API's origin.
When recording an API this can be undesirable as the local proxy is different from the API being recorded, and thus any
client following such a link would make its next request directly to the proxy target rather than the local CLI running
the proxy.

To remedy this issue, the Record command has **hostname rewriting enabled by default**, which will replace any instances
of the proxy target's domain name and port in the response headers or body with the local proxy's domain name and port.

If this is not the behaviour you want when recording, you can turn off hostname rewriting using the `--no-rewrite-origin-hostname`
flag on the `record` command:

```shell theme={null}
wiremock record http://private-endpoint --no-rewrite-origin-hostname
```

## Advanced Recording

The WireMock CLI accepts a configuration file to control how stubs are recorded:

```shell theme={null}
wiremock record http://private-endpoint --import-config-file=<path>
```

The format of this file is documented in the [advanced recording configuration page](/cli/recording-configuration).

## Recording with Mutual TLS

If you need to record from an API that authenticates clients with mutual TLS, the CLI can present your private client
certificate in one of two ways:

### Via a PEM file

If you have a file containing a PEM encoded RSA private key and X509 certificate, you can provide it as so:

```shell theme={null}
wiremock record http://mutual-tls-endpoint --to=cloud:33eye3l9 \
  --client-certificate=/path/to/file.pem
```

A PEM encoded file should look something like this:

```
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDHIpsyRDeM1lFQ
<multiple lines of base64 encoded data>
GhxuZ3ceXiqwvhH8Yt5gNs0=
-----END PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
MIIDrzCCApegAwIBAgIUR24W6NZN7xPwSqc59usFQ37HPYswDQYJKoZIhvcNAQEL
<multiple lines of base64 encoded data>
dHhXPaefkEhrsUbnXGYRfwQhf4SzdYCMCJno7KKsNn6RLIo=
-----END CERTIFICATE-----
```

### Using a PKCS 12 certificate store

Keeping a private key in PEM format is a security risk, so we also support supplying your client certificate in a
password protected PKCS 12 store as so:

```shell theme={null}
wiremock record http://mutual-tls-endpoint --to=cloud:33eye3l9 \
  --client-certificate-store=/path/to/file.pkcs12
```

You will be challenged for a password to decrypt the store and the private key. The same password must be able to
decrypt both.

## Non-interactive Recording Sessions

The WireMock CLI `record` command supports running in non-interactive mode, making it ideal for
CI/CD pipelines and automated environments where user interaction is not possible or desired. See the
[Non-interactive Recording](/cli/non-interactive-recording) for more details.


# Import & Recording Configuration Reference
Source: https://docs.wiremock.io/cli/recording-configuration

Reference for the config file used to customize imports and recordings using the WireMock CLI

The WireMock CLI accepts an import configuration file, which controls how stubs are created during a recording.

This file can be used to specify a duplicate policy, indicating what should be done when two recorded events are
recorded that would result in the same stub request being generated.

It can also be used to specify a set of stub transformation rules, allowing you to modify a number of aspects of the
generated stubs e.g. matching the body using a few `matchesJsonPath` expressions rather than a single `equalToJson`
matcher (which can be both brittle and slow for large/complex JSON documents).

## Usage

```shell theme={null}
wiremock record http://private-endpoint --import-config-file=<path>
```

Or for multi-domain recording:

```shell theme={null}
wiremock record-many --import-config-file=<path>
```

## Duplicate policy

The duplicate policy determines what happens if the stub generated from a recorded request has a request pattern identical
to that of an existing stub.

The available policies are:

1. `ignore` - the existing stub is left unchanged and the new request is discarded
2. `overwrite` - the existing stub is updated to the attributes of the new one
3. `create_new` - a new stub is created
4. `create_scenarios` - all stubs are created as part of a scenario

The default policy is `overwrite`.

When specifying `create_new` the new stub will be inserted above the existing one, so the new one will be matched first
unless further edits are applied.

The policy can be specified in the config file as follows:

```yaml theme={null}
import:
  duplicatePolicy: ignore # overwrite|create_new|ignore|create_scenarios
```

### Scenarios

When using the `create_scenarios` duplicate policy, all stubs imported with the same request pattern will be added to the
same scenario (a scenario with the same name). You can read more about scenarios in the [Simple Scenarios](/dynamic-state/stateful-scenarios)
section.

All scenarios are created within a recording session.  Depending on your recording batching configuration, your recording
session may contain multiple imports into your mock API, and the scenarios are created and managed across all the imports
within the same recording session. The scenarios created during a recording session have the recording session id in
their name, so there are no scenario clashes across multiple recording sessions.  Scenarios are named in the following
format:

`scenario-<request-method>-<request-path>-<recording-session-id>-<request-pattern-hash>`

This means that if you record a set of stubs into a scenario in one recording session and then record the same set of
stubs into a scenario in a different recording session, the scenarios will be named differently to isolate them from
each other.  The stubs recorded second will be inserted above the previous import so will match first unless further
edits are applied.

Scenarios are created in the order the stubs are imported.  For example, importing 3 stubs with the same request pattern
will result in the following scenario being created:

* Third stub importd
  * Scenario name set to the same as the first stub
  * Required scenario state - `step-3-<scenario-name>`
  * New scenario state - empty as this is the terminal state
* Second stub importd
  * Scenario name set to the same as the first stub
  * Required scenario state - `step-2-<scenario-name>`
  * New scenario state - `step-3-<scenario-name>`
* First stub importd
  * Scenario name set using the format above
  * Required scenario state - `Started`
  * New scenario state - `step-2-<scenario-name>`

## Transformation rules

By default recording produces a stub that matches on the specific method and full path and query of each request.
The config file can specify any number of rules for generating more or less specific matching criteria:

```yaml theme={null}
import:
  stubTemplateTransformationRules:
  - filter: {}
    template: {}
```

Each rule has two elements:

1. a `filter` which controls whether the rule is applied to the generated stub. This is optional - if omitted the
   template will *always* be applied.
2. a `template` which generates request matchers to apply to the stub

The rules are additive - all the rules which have a `filter` which matches the recorded request will be used to generate
matchers, which will be added in turn to the generated stub.

When more than one rule could both match and specify different matchers for the same element (for instance the first
specifies that the `Content-Type` header is `equalTo` `"application/json"`, and the second that the `Content-Type`
header `contains` `"json"`), the last defined rule will win.

Finally a check is made that the generated stub would still match the recorded request from which it was generated. If
it would not the entire stub is discarded and no stub is generated at all for that request.

### Templating

Where matchers have a right hand side the `{{ recordedValue }}` macro may be used to capture what that value had
on the recorded request. For instance, the following rule:

```yaml theme={null}
import:
  stubTemplateTransformationRules:
  - filter:
      request:
        headers:
          Security-Context:
            matchesJsonPath: "$.userId"
    template:
      request:
        headers:
          Security-Context:
            matchesJsonPath:
              expression: "$.userId"
              equalTo: "{{ recordedValue }}"
```

when matched against this request:

```http request theme={null}
GET /
Security-Context: { "userId": "usr_123" }
```

would produce a stub mapping with the following request matcher:

```json theme={null}
{
  "request": {
    "method": "GET",
    "url": "/",
    "headers": {
      "Security-Context": {
        "matchesJsonPath": {
          "expression": "$.userId",
          "equalTo": "usr_123"
        }
      }
    }
  }
}
```

This would allow recording different stubs for requests made by different users.

### Limitations

1. At present no logic other than replacement of the `{{ recordedValue }}` macro can be applied in the template, though
   request matchers can be hard coded.

2. The `{{ recordedValue }}` macro cannot currently be used in an `equalToJson`, `equalToXml` or `matching` request
   matcher.

3. The `filter` only contains a `request` matcher - it is not yet possible to apply rules conditionally based on the
   response.

4. The `template` only contains a `request` matcher - it is not yet possible to define changes to the response
   definition in these rules.

## Reference

The format of the import config file is defined by the [import-config-file-schema](https://static.wiremock.io/schemas/wiremock-import-config.yaml-schema.json)
JSON schema.


# wiremock.yaml Configuration Reference
Source: https://docs.wiremock.io/cli/wiremock-yaml-reference

Complete reference documentation for the wiremock.yaml configuration file format

The `wiremock.yaml` file is used by the WireMock CLI to configure local mock services. It defines service configurations including HTTP/HTTPS ports, TLS certificates, API types, and cloud synchronization settings.

## File location

The `wiremock.yaml` file should be placed in your WireMock working directory (typically `.wiremock` by default, or as specified with the `--wiremock-dir` argument).

## Schema validation

The configuration file conforms to the JSON Schema specification available at:
[https://static.wiremock.io/schemas/wiremock.yaml-schema.json](https://static.wiremock.io/schemas/wiremock.yaml-schema.json)

## Root structure

```yaml theme={null}
global:
  # Global configuration (optional)
services:
  # Service definitions (required)
```

## Global configuration

The `global` section contains configuration that applies to all services by default.

### Global HTTPS settings

```yaml theme={null}
global:
  https:
    certificate:
      # Certificate configuration (see Certificate Configuration section)
```

When a global certificate is configured, all services with an `https` section will use it by default unless they specify their own certificate.

## Services

The `services` section is a map of service names to their configurations. Service names are user-defined identifiers.

```yaml theme={null}
services:
  my-service-name:
    # Service configuration
  another-service:
    # Service configuration
```

### Required service properties

Each service must define these properties:

#### type

The type of mock API.

* **Type:** `string`
* **Required:** Yes
* **Valid values:** `REST`, `Unstructured`, `gRPC`, `GraphQL` (case insensitive)

```yaml theme={null}
type: REST
```

#### name

Human-readable name for the service.

* **Type:** `string`
* **Required:** Yes

```yaml theme={null}
name: "Invoicing API"
```

#### port

HTTP port number for the service.

* **Type:** `integer`
* **Required:** Yes (or `https` must be provided)
* **Valid range:** 1-65535

```yaml theme={null}
port: 8080
```

### Optional service properties

#### description

Optional description of the service.

* **Type:** `string`
* **Required:** No

```yaml theme={null}
description: "Mock API for the invoicing system"
```

#### cloud\_id

WireMock Cloud mock API ID for syncing with cloud.

* **Type:** `string`
* **Required:** No
* **Pattern:** 4-15 lowercase alphanumeric characters

```yaml theme={null}
cloud_id: abc123xyz
```

This field is automatically populated when pulling a mock API from WireMock Cloud.

#### path

Path to the directory containing stub mappings, files, and API specifications. The path is relative to the location of `wiremock.yaml`.

* **Type:** `string`
* **Required:** No

```yaml theme={null}
path: ./my-service
```

This directory typically contains items needed to run the service.  For example:

* `stub-mappings.yaml` - Stub mapping yaml file
* `schema.graphql` or `openapi.yaml` - Mock API IDL documents such as OpenAPI/GraphQL schema

#### open\_api

OpenAPI-specific configuration for validation.

* **Type:** `object`
* **Required:** No

```yaml theme={null}
open_api:
  validation_mode: soft
```

**Properties:**

* `validation_mode` - Controls OpenAPI request/response validation
  * **Type:** `string`
  * **Valid values:** `none`, `soft`, `hard`
  * **Default:** `none`
  * `none` - No validation
  * `soft` - Validation warnings logged but requests not rejected
  * `hard` - Invalid requests are rejected

#### https

HTTPS configuration for the service. See the [TLS/HTTPS Configuration](#tlshttps-configuration) section below.

* **Type:** `object`
* **Required:** No (but either `port` or `https` must be provided)

```yaml theme={null}
https:
  port: 8443
  certificate:
    pem: /path/to/cert.pem
```

#### originals

Map of original service URLs for recording and proxying.

* **Type:** `object`
* **Required:** No

```yaml theme={null}
originals:
  default: https://api.example.com
  staging: https://staging-api.example.com
```

The keys in this map can be referenced when using recording features to specify which target service to record from.

## TLS/HTTPS configuration

Services can be configured to run over HTTPS using TLS certificates. TLS can be configured globally (for all services) or per-service.

### HTTPS service configuration

```yaml theme={null}
services:
  my-service:
    type: REST
    name: "Secure API"
    https:
      port: 8443
      certificate:
        # Certificate configuration
```

**Properties:**

* `port` - HTTPS port number (required, 1-65535)
* `certificate` - Certificate configuration (optional, inherits from global if not specified)

### Certificate configuration

Certificates can be configured in three ways:

#### PEM file

A PEM-encoded file containing both the RSA private key and X509 certificate.

```yaml theme={null}
certificate:
  pem: /path/to/certificate.pem
```

The path can be absolute or relative to the `wiremock.yaml` file.

**PEM file format:**

```
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDHIpsyRDeM1lFQ
... (base64-encoded content)
GhxuZ3ceXiqwvhH8Yt5gNs0=
-----END PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
MIIDrzCCApegAwIBAgIUR24W6NZN7xPwSqc59usFQ37HPYswDQYJKoZIhvcNAQEL
... (base64-encoded content)
dHhXPaefkEhrsUbnXGYRfwQhf4SzdYCMCJno7KKsNn6RLIo=
-----END CERTIFICATE-----
```

#### PKCS12 or JKS keystore

A keystore file (PKCS12 or JKS format) containing the private key and certificate.

```yaml theme={null}
certificate:
  keystore: /path/to/keystore.p12
  password: very_secret
  alias: my_cert  # optional
```

**Properties:**

* `keystore` - Path to the keystore file (absolute or relative to `wiremock.yaml`)
* `password` - Password to unlock the keystore (required)
* `alias` - Optional alias to select a specific certificate if the keystore contains multiple entries. If omitted, the first entry is used.

#### Certificate alias reference

When a global keystore is configured, individual services can reference specific certificates by alias:

```yaml theme={null}
global:
  https:
    certificate:
      keystore: /path/to/keystore.p12
      password: very_secret

services:
  service-one:
    type: REST
    name: "Service One"
    https:
      port: 8443
      certificate:
        alias: service_one_cert

  service-two:
    type: REST
    name: "Service Two"
    https:
      port: 8444
      certificate:
        alias: service_two_cert
```

### Default self-signed certificate

If no certificate is configured, services will use WireMock's default self-signed certificate.

## Profiles

Configuration overrides can be defined in profile files named `wiremock-<profile-name>.yaml`.
These files overlay the base configuration when running commands with the `--profile`/`-p` flag.

See [Managing Environments](/cli/environments) for more information about using profiles to manage environments in WireMock Cloud.

## Complete example

```yaml theme={null}
global:
  https:
    certificate:
      keystore: /etc/wiremock/certs/global-keystore.p12
      password: global_password
      alias: default_cert

services:
  invoicing-api:
    type: REST
    name: "Invoicing API"
    description: "Mock API for invoicing system"
    cloud_id: ndzew
    port: 8080
    https:
      port: 8443
    path: ./invoicing-api
    open_api:
      validation_mode: soft
    originals:
      default: https://api.example.com/invoicing

  payment-api:
    type: REST
    name: "Payment API"
    cloud_id: wroog
    port: 8081
    https:
      port: 8444
      certificate:
        alias: payment_cert
    path: ./payment-api

  graphql-service:
    type: GraphQL
    name: "GraphQL Gateway"
    port: 9090
    path: ./graphql-gateway
    originals:
      default: https://graphql.example.com

  grpc-service:
    type: gRPC
    name: "gRPC Service"
    https:
      port: 50051
      certificate:
        pem: ./certs/grpc-service.pem
    path: ./grpc-service
```

## See also

* [Running mock APIs locally](/cli/local-playback)
* [Recording configuration](/cli/recording-configuration)


# Deployment
Source: https://docs.wiremock.io/concepts/deployment

Understanding the different ways to deploy WireMock

## Deployment Modes

WireMock can be deployed in three distinct modes, each suited to different organizational needs and constraints:

1. **Cloud** - Fully managed hosting
2. **Self-hosted** - Complete on-premises deployment
3. **Hybrid** - Control plane in the cloud, data plane on-premises

## Cloud Deployment

With Cloud deployment, WireMock hosts everything for you:

* **Control plane** - The management interface and API
* **Data plane** - The mock API endpoints that respond to requests
* **User interface** - The web-based UI for managing your simulations

All components are accessible from the internet with nothing to install or maintain. This mode provides:

* Immediate availability with no infrastructure setup
* Automatic updates and maintenance
* Built-in scalability and high availability
* Public accessibility for remote teams and external integrations

Cloud deployment is ideal for:

* Quick prototyping and experimentation
* Teams without dedicated infrastructure
* Scenarios where public internet accessibility is acceptable
* Organizations wanting zero operational overhead

## Self-Hosted Deployment

Self-hosted deployment involves running the entire WireMock product stack on your own Kubernetes cluster.

This mode requires you to:

* Provide and manage a Kubernetes cluster
* Provide and manage a Postgres database
* Handle installation, updates, and maintenance
* Configure networking, DNS, certificates and security
* Monitor and scale infrastructure as needed

Self-hosted deployment offers:

* Complete control over data and infrastructure
* Ability to keep all traffic within private networks
* Customization of deployment topology
* Compliance with strict data residency requirements

This mode is appropriate for:

* Organizations with security policies prohibiting cloud services
* Scenarios requiring air-gapped or isolated network environments
* Teams with existing Kubernetes expertise and infrastructure
* Situations demanding complete data sovereignty

## Hybrid Deployment

[Hybrid deployment](/concepts/runner) balances convenience with control by splitting the architecture:
the control plane an UI remain in the cloud while API simulations are hosted in your infrastructure
using WireMock Runner.

Benefits of hybrid deployment:

* Simplified management through the cloud-hosted UI
* Data plane traffic stays within your network
* Flexibility to deploy mock APIs where they're needed
* Reduced operational burden compared to full self-hosting

Hybrid deployment suits:

* Development and testing workflows requiring local or private simulated APIs
* CI/CD pipelines that can't access public internet services
* Organizations comfortable with cloud management but requiring private data planes
* Scenarios needing simulated APIs in multiple diverse locations


# Profiles
Source: https://docs.wiremock.io/concepts/profiles

Understanding WireMock Runner profiles and their use cases

*This page explains the concept of profiles in WireMock. For practical instructions on creating and using profiles to manage environments, see [Managing Environments](/cli/environments).*

**Profiles** provide a mechanism for applying named configuration overrides to your mock API services. They allow you to maintain a single base configuration while selectively modifying specific aspects for different use cases, contexts, or runtime scenarios.

## What are profiles?

A profile is a named configuration overlay that modifies specific aspects of your base WireMock configuration without duplicating the entire configuration structure.

Each profile is stored in a separate file named `wiremock-<profile-name>.yaml` that sits alongside your base `wiremock.yaml` configuration. When you activate a profile using the `--profile` flag, its configuration merges with and overrides matching values in the base configuration.

This overlay mechanism means you define only what changes, not what stays the same.

## Why profiles exist

Mock API configurations often need to vary depending on context:

* Different target URLs for recording (local, staging, production APIs)
* Different port assignments to avoid conflicts
* Different TLS certificates for security contexts
* Different cloud API IDs for environment isolation
* Different validation modes for testing vs. production use

Without profiles, managing these variations requires either maintaining completely separate configuration files (which leads to duplication and drift) or manually editing configurations when switching contexts (which is error-prone and doesn't scale).

Profiles solve this by treating configuration variance as explicit, minimal, named overrides. This makes the relationships between configurations clear and keeps common elements in one place.

## How profiles work

### Configuration overlay

When you specify a profile, WireMock reads both the base configuration and the profile configuration, then merges them. The profile values override any matching base values while inheriting everything else.

For example, given this base configuration:

```yaml theme={null}
services:
  invoicing-api:
    type: REST
    name: "Invoicing API"
    port: 8888
    cloud_id: prod123
    originals:
      default: https://api.example.com
```

And this `wiremock-staging.yaml` profile:

```yaml theme={null}
services:
  invoicing-api:
    cloud_id: staging456
    originals:
      default: https://staging-api.example.com
```

Using `--profile staging` produces this effective configuration:

```yaml theme={null}
services:
  invoicing-api:
    type: REST
    name: "Invoicing API"
    port: 8888
    cloud_id: staging456
    originals:
      default: https://staging-api.example.com
```

The profile changed only the `cloud_id` and the `originals.default` URL—everything else came from the base configuration.

### Profile scope

Profiles can override specific service properties, but they maintain structural constraints:

* The same services must exist in both base and profile configurations
* Service structure (service keys/names) cannot change
* The service `type` cannot be overridden
* New services cannot be added via profiles

These constraints ensure that profiles remain true overrides rather than separate, divergent configurations.

### Common profile use cases

**Recording from different sources:** Override the `originals` section to record from different target services—production APIs, staging APIs, or local instances—depending on your current task.

**Port conflict avoidance:** Change port assignments when multiple developers or processes need to run mock services simultaneously on the same machine.

**Security context switching:** Apply different TLS certificates or validation modes depending on whether you're doing local development, integration testing, or simulating production-like behavior.

**API specification variants:** Use different OpenAPI validation modes—`none` for exploratory development, `soft` for testing with warnings, `hard` for strict contract validation.

## Profiles for managing environments

One of the most common uses of profiles is managing environment-specific configurations—development, staging, production, and other deployment contexts where the same logical services need different runtime characteristics.

### Environment isolation with cloud APIs

When working with WireMock Cloud, different environments typically map to different mock API instances. A `staging` profile might override the `cloud_id` field to point to staging-specific mock APIs, while a `production` profile points to production mock APIs. This allows the same local configuration structure to sync with environment-appropriate cloud instances.

For example:

```yaml theme={null}
# wiremock.yaml (base configuration)
services:
  invoicing-api:
    type: REST
    name: "Invoicing API"
    cloud_id: prod123
    port: 8888
```

```yaml theme={null}
# wiremock-staging.yaml (staging profile)
services:
  invoicing-api:
    cloud_id: staging456
```

Using `--profile staging` targets the staging cloud API while preserving all other configuration.

### Environment-specific recording sources

Recording often needs environment-specific source URLs. Development might record from localhost, staging from internal services, and production from live APIs:

```yaml theme={null}
# wiremock.yaml
services:
  payment-api:
    originals:
      default: https://api.production.example.com
```

```yaml theme={null}
# wiremock-dev.yaml
services:
  payment-api:
    originals:
      default: http://localhost:3000
```

## Learn more

For details on the profile file format and how profile overlays work, see the [wiremock.yaml Reference](/cli/wiremock-yaml-reference#profiles).

For instructions on using profiles to manage WireMock Cloud environments, see [Managing Environments](/cli/environments).

For information on using profiles with Runner, see [Serve Mode](/runner/serve) and [Runner Environment Variables](/runner/environment-variables).

For details on WireMock Runner's architecture and capabilities, see [WireMock Runner](/concepts/runner).


# WireMock Runner
Source: https://docs.wiremock.io/concepts/runner

Understanding how WireMock Runner enables hybrid workflows, local-first development and CI/CD integration

*This page explains concepts behind WireMock Runner. To start using the Runner right away, [follow the instructions here](/runner/overview)*

**WireMock Runner** runs as a service anywhere you want and enables you to record, to sync with Cloud, and to host mock APIs in your own infrastructure while continuing to use WireMock Cloud's management interface and collaboration features as a centralized control plane.

This hybrid mode splits the difference between Cloud-only and fully self-managed, letting you mix the benefits of Cloud with local development workflows and execution in your own private cloud infrastructure.

## What is WireMock Runner?

WireMock Runner is a long-running service packaged as a container that can be run anywhere you can deploy it. It connects to WireMock Cloud for configuration and collaboration, but executes recordngs and runs mock APIs locally in your environment.

This architecture creates a clear separation of concerns:

* The **control plane** (management, UI, collaboration) remains in WireMock Cloud
* The **execution plane** (mock API execution) runs wherever you need it - locally via CLI, in your environments via **WireMock Runner** or in WireMock Cloud.

This is what makes hybrid deployment possible, and it's why **WireMock Runner** is sometimes referred to as "hybrid mode."

## Why WireMock Runner Exists

Traditional API mocking solutions force teams to choose between two extremes:

**Fully cloud-based** approaches offer convenience and collaboration but struggle when APIs live behind firewalls, when teams need fast local feedback loops, or when security policies prohibit external connections.

**Fully self-hosted** approaches provide control and privacy but require significant infrastructure investment, eliminate the benefits of cloud collaboration, and create maintenance overhead.

WireMock Runner was designed to resolve this tension. It enables teams to adopt the workflow that matches their needs rather than adapting their needs to match the tool's constraints.

## How WireMock Runner Works

The Runner operates as a containerized service with two primary modes:

### Record Mode

In record mode, the Runner automatically creates or updates mock APIs by capturing real API traffic. This allows teams to build or refresh mock specifications from actual service behavior, keeping mocks aligned with reality as APIs evolve.

Recording can happen locally during development, in CI/CD during integration tests or deployments, or in any environment where you need to capture API interactions (see [Recording on Kubernetes](/runner/recording-multiple-apis-on-kubernetes) for an example).

### Run Mode

In Run / serve mode, the Runner retrieves mock specifications from WireMock Cloud (or uses already locally stored mock configurations) and serves them locally. Incoming requests are matched against these specifications and responded to according to the stub definitions—all without the request ever leaving your infrastructure.

This enables development, testing, and even production-like environments to operate with simulated APIs while remaining completely isolated from external networks.

### Mode Switching

The Runner can be switched between modes dynamically via its HTTP management interface. This allows the same Runner instance to record new interactions during certain workflows and serve those interactions during others—orchestrated by your existing automation.

## Using WireMock Runner

### Git and CI/CD Integration

Mock specifications can live in version control alongside the code they support. WireMock Runner can pull the latest mocks at the start of a CI run, record new interactions during tests, and push updated specifications back to Git—all automated within your existing CI/CD pipeline.

This treats mocks as first-class artifacts: versioned, reviewed through pull requests, and promoted through environments just like application code. See [Promoting APIs with Git and CI/CD](/runner/promoting-apis-with-git-and-ci) for a detailed workflow guide.

### Environment-Specific Configuration

Different environments often require different mock behavior. WireMock Runner supports environment-specific profiles, allowing you to maintain variations for local development, CI, staging, and production-like environments—all in the same repository, all promoted through the same workflow.

### Multi-Location Deployment

Because Runner is a container, it can be deployed anywhere:

* On a developer's laptop for fast local iteration
* Inside a CI pipeline for automated testing
* In a Kubernetes cluster behind the firewall for team environments (see [Running on Kubernetes](/runner/running-on-kubernetes))
* In multiple regions or data centers for distributed teams

All of these instances connect to the same WireMock Cloud control plane for management and collaboration, while serving mocks locally in each environment.

## When to Use WireMock Runner

WireMock Runner is particularly valuable when:

### APIs Are Not Publicly Accessible

If the APIs you need to simulate live behind corporate firewalls, VPNs, or in regulated environments with strict network controls, cloud-only mocking won't work. Runner brings mock execution into your network while keeping management tools accessible.

### Fast Feedback Loops Matter

Local development benefits from tight feedback loops. Depending on cloud-hosted mocks adds network latency and potential connectivity issues. Running mocks locally with Runner eliminates these dependencies and speeds up the development cycle.

### CI/CD Cannot Access External Services

Many CI environments operate in isolated networks without internet access. Runner can be packaged into these environments, allowing CI pipelines to use sophisticated API simulation without requiring external connectivity.

### Configuration as Code (or Gitflow) Is Required

Teams practicing GitOps or infrastructure-as-code need their tooling to fit that model. Runner's integration with version control and CI/CD makes mock management programmable and auditable, rather than manual and UI-driven.

### Security Policies Restrict Data Movement

Some organizations cannot allow request/response data to transit to external services, even temporarily. Runner processes all mock traffic locally, sending only metadata and specifications to the cloud for management purposes.

## Relation to WireMock CLI

WireMock CLI and WireMock Runner share the same underlying implementation but are packaged separately. The CLI is optimized for interactive, short-lived operations—typically for individual developers working on single machines. WireMock Runner is optimized for long-lived, service-based operation.

Most developers will use the CLI for day-to-day work and encounter Runner when their mocks are deployed to shared environments or when their CI/CD pipelines execute tests against simulated APIs.

## Learn More

For details on installing and running WireMock Runner, see the [WireMock Runner documentation](/runner/overview).

For a comparison of deployment modes and their trade-offs, see [Deployment](/concepts/deployment).

For practical examples of how Runner can be used in a real-world software delivery workflow, see:

* [Running on Kubernetes](/runner/running-on-kubernetes)
* [Recording on Kubernetes](/runner/recording-multiple-apis-on-kubernetes)
* [Promoting APIs with Git and CI/CD](/runner/promoting-apis-with-git-and-ci)


# Stubbing
Source: https://docs.wiremock.io/concepts/stubbing

Understanding stubs: the building blocks of API simulation

The fundamental building block of a simulation is a **stub**. A stub represents a rule that tells WireMock how to respond when it receives certain kinds of requests.

A stub consists of two main parts:

1. **Request matching criteria** - The conditions that an incoming request must satisfy to trigger this stub
2. **Response definition** - A recipe for generating and returning a response when the criteria match

## How Stubs Work

When WireMock receives an HTTP request, it evaluates that request against each stub in order, from top to bottom. The first stub whose request criteria fully match the incoming request is selected, and its response definition is used to generate the response.

This top-to-bottom matching order is important: more specific stubs should typically be placed before more general ones to ensure they are evaluated first.

## Request Matching

Request matching can examine any part of an incoming HTTP request:

* **HTTP method** (GET, POST, PUT, DELETE, etc.)
* **URL path** and path patterns
* **Query parameters**
* **HTTP headers**
* **Request body content**
* **Cookies**

Matching can use simple equality checks or more sophisticated criteria:

* Exact matches for precise control
* Pattern matching with wildcards or regular expressions
* Content-type specific matching (e.g., JSON path queries, XML XPath expressions)
* Absence checks (matching when something is NOT present)
* Multiple criteria combined with logical AND/OR operations

The flexibility of request matching allows you to create both broad catch-all stubs and highly specific stubs that only match very particular requests.

## Response Definitions

Once a stub matches a request, it uses its response definition to determine what to return. Response definitions can be:

* **Static responses** - Fixed, pre-defined data returned every time
* **Templated responses** - Dynamic content generated using variables, request data, and helper functions
* **Fault responses** - Simulated network errors, timeouts, or malformed data
* **Proxy responses** - Forward the request to another system and return its response

Responses can include:

* HTTP status codes
* Headers
* Body content (JSON, XML, plain text, binary data, etc.)
* Delays to simulate latency
* State changes for stateful scenarios

A stub can also optionally trigger a [webhook](/webhooks) call.

## Stub Organization

Stubs are organized within Mock APIs, which are collections of related stubs that simulate a particular API or service. Within a Mock API:

* Stubs can be created, edited and deleted independently
* The order of stubs affects which one matches first
* A priority can be set on a stub explicitly, which will take precedence of the order


# Templating
Source: https://docs.wiremock.io/concepts/templating

Understanding how dynamic content is generated throughout WireMock Cloud

WireMock Cloud uses **Handlebars templating** to generate dynamic content wherever responses, data, or outbound requests need to be customized based on runtime information. This templating system enables you to create flexible, context-aware simulations that respond intelligently to incoming requests, state changes, and data sources.

## What is Templating?

Templating is a mechanism for generating content dynamically by combining a template with data from the current context. A template contains both static content and special expressions (called "helpers") that are evaluated at runtime to produce dynamic values.

For example, this simple template:

```handlebars theme={null}
Hello {{request.query.name}}!
```

Will output "Hello Alice!" when a request arrives with `?name=Alice` in the query string.

## Where Templating is Used

Templating can be applied throughout WireMock Cloud wherever dynamic content needs to be produced:

### Stub Response Bodies

The most common use of templating is in stub response bodies, where you need to return data that reflects information from the incoming request. This allows a single stub to serve many variations of a response rather than requiring separate stubs for each case.

For example, a templated response body can echo back data from the request, generate unique identifiers, incorporate current timestamps, or extract and transform request data using JSONPath or XPath.

### Response Headers

Response header values can be templated to return dynamic metadata. This is useful for generating correlation IDs, setting cache headers based on request parameters, or returning computed values in custom headers.

### Webhook Request Bodies

When [webhooks](/webhooks) are triggered by incoming requests, their request bodies can be templated to include data from the original request, current state, or data sources. This allows webhooks to send contextual notifications or trigger downstream systems with relevant information.

### Webhook URLs and Headers

Similarly, webhook request URLs and header values can use templating to determine the destination or metadata for outbound calls dynamically. This enables patterns like routing webhooks to different endpoints based on request content or environment.

### Proxy URLs

When using the proxy feature, the target URL can be templated to determine the destination dynamically based on the incoming request. This supports sophisticated routing scenarios where different requests should be forwarded to different backend services.

## The Templating Engine

WireMock Cloud uses [Handlebars](https://handlebarsjs.com/), a mature and widely-used templating language. Handlebars provides:

* **Variable substitution** - Access to request data, state, and data sources
* **Helper functions** - Built-in and custom functions for transformations and logic
* **Conditional logic** - If/else blocks for branching behavior
* **Iteration** - Loops over collections of data
* **Nested expressions** - Combining helpers to build complex transformations

The basic syntax uses double curly braces `{{...}}` to mark dynamic expressions within otherwise static content.

## Helpers for Specific Tasks

WireMock Cloud provides an extensive library of helper functions that extend Handlebars with capabilities specifically designed for API simulation:

* **JSONPath helpers** - Extract values from JSON request bodies using path expressions
* **XPath helpers** - Query XML request bodies
* **String manipulation** - Substring, replace, case conversion, and more
* **Date and time** - Format dates, parse timestamps, generate dates relative to now
* **Random data generation** - UUIDs, random numbers, realistic fake data
* **Encoding and decoding** - Base64, URL encoding, JSON escaping
* **Cryptographic functions** - Hashing, signing, JWT generation and validation
* **State access** - Read and reference values from stateful scenarios
* **Data source queries** - Retrieve data from CSV or database sources

These helpers can be combined and nested to build sophisticated dynamic responses from simple templates.

## The Request Model

When templates are evaluated, they have access to a data model that represents the current context. The primary element of this model is the `request` object, which contains all attributes of the incoming HTTP request:

* URL path, query parameters, and path segments
* HTTP method, headers, and cookies
* Request body (as text or Base64)
* Multipart form data and file uploads

This request data can be accessed directly in templates using expressions like `{{request.headers.Authorization}}` or `{{request.query.productId}}`.

In webhook templates, the triggering request is available as `originalRequest` to distinguish it from any request data that might be constructed for the webhook itself.

For a complete reference of all available request attributes and how to access them, see the [Request Model Reference](/response-templating/request-model).

## Enabling Templating

Templating must be explicitly enabled on a per-stub basis by checking the "Enable templating" option when configuring a stub response. This ensures that static responses remain performant and that template expressions are only evaluated when needed.

Once enabled, templating applies to:

* Response body
* Response header values
* Proxy URL (if using proxy mode)
* Any configured webhook attributes

## Learn More

For a comprehensive guide to using templating in stub responses, including syntax details and the request data model, see [Response Templating](/response-templating/basics).

For a complete reference of all available helpers organized by category, see the [Templating reference section](/response-templating/conditional-logic-and-iteration) in the documentation.


# Deleting Data Sources
Source: https://docs.wiremock.io/data-sources/deleting-data-sources

How to remove data sources from your account

## Deleting a Data Source

Data sources can be deleted from your organisation. To delete a data source:

* Navigate to the [Data sources page](https://app.wiremock.io/data-sources).
* Click on the delete icon for the data source you want to remove.

<p>
  <img alt="Delete a data source" title="Delete a data source" />
</p>

Clicking on the delete icon will open a confirmation dialog. Click the `Confirm` button to confirm the deletion or
`Cancel` to close the dialog without deleting the data source.

<p>
  <img alt="Delete data source confirmation" title="Delete data source confirmation" />
</p>

Clicking `Confirm` will delete the data source, but it will not remove the data source from any stubs that are using it.
These stubs will continue to reference the deleted data source, but will act as if no data was returned when the data
source is queried. See below for more details on stub matching and response templating when a data source is deleted.

When a data source is deleted, any data source limits you may have reached will be re-evaluated. If you have any
disabled data sources, they will be re-enabled if you now have available capacity within your data source limits. You
can read more about [plan limits and disabled data sources here](./plan-limits).

Any stubs that are using the deleted data source will now have a warning message displayed on the stub informing you
that `The data source that this stub was referencing no longer exists.`  You will also see a warning icon next to
the data source summary in the stub form.

<p>
  <img alt="Data source stub warning icon" title="Data source stub warning icon" />
</p>

If you have other data sources within your organisation you can attach one of these to the stub to replace the deleted
data source. If you do not have another data source that you can use, you will need to update the stub to remove the
reference to the deleted data source.

You can do this by clicking on the delete icon next to the data source in the stub form.

<p>
  <img alt="Delete data source stub warning" title="Delete data source stub warning" />
</p>

### Stub Matching

If a stub is using a data source that has been deleted, the stub will no longer match incoming requests if the
`Matches stub only if data is found` tick box is checked on the Stub form. If this tick box is not checked, the stub
will continue to match incoming requests, but the data source will not be queried.

### Data source response templating

If a data source is deleted, any response templates that are using the data source will no longer be able to access the
data source data. The response template will still be rendered, but the data source data will not be available.


# Creating & Editing CSV Data Sources
Source: https://docs.wiremock.io/data-sources/managing-csv-data-sources

Setting up your external test data from a CSV file

## Creating a CSV data source

Data sources can be created at the organisation level, meaning that the Data sources you create can be shared among the
members of your organisation.

To create a data source:

* Navigate to the Data Sources page.

  <img alt="Data source menu item" />

* Click on the button, `+Create new data source`.

  <img alt="Create Data source button" />

* Choose `CSV based` from the dropdown and select the CSV file containing your data.

  <img alt="Choose the CSV file" />

* Provide a name for your data source.

  <img alt="Add a name for the data source" />

* Click `save` at the bottom of the page.

  <img alt="New data source save button" />

## Editing a CSV data source

Data sources can be updated after creation.

To edit a data source:

* Navigate to the Data Sources page.
* Click on the data source you wish to edit, from the list provided.
* Update your data source.
* Click on the `save` at the bottom of the page.

<img alt="New data source save button" />

Once in the data source page, you will be able to:

* Replace the csv file
* Rename the data source
* Change the column types

## Columns

### Column names

When uploading the CSV file, please ensure the following requirements for the column names:

* Column names must be unique within the CSV file.
* Column names must be between 1 and 128 characters in length.
* Column names can only contain letters, digits, the underscore character and spaces, and must not start with an
  underscore.
* Column names cannot be any of the following reserved keywords:

  `all`, `and`, `any`, `array`, `as`, `at`, `between`, `both`, `by`, `call`, `case`, `cast`, `check`, `coalesce`, `constraint`, `convert`, `corresponding`, `create`, `cross`, `cube`, `default`, `distinct`, `do`, `drop`, `else`, `every`, `except`, `exists`, `fetch`, `for`, `foreign`, `from`, `full`, `grant`, `group`, `grouping`, `having`, `in`, `inner`, `intersect`, `into`, `is`, `join`, `leading`, `left`, `like`, `natural`, `not`, `nullif`, `on`, `or`, `order`, `outer`, `primary`, `references`, `right`, `rollup`, `select`, `set`, `some`, `sum`, `table`, `then`, `to`, `trailing`, `trigger`, `union`, `unique`, `using`, `values`, `when`, `where`, `with`

Also notice that column names will be lowered case.

### Column types

Before saving the data source (or when editing it), you are able to amend the column data types. You will find a\
setting icon below the column name and, when clicking on it, you will be able to select the correct type for the column,
as shown in the following figure.

<img alt="Data source column editting" />

The default data type is `STRING`, however you can pick any of the following types:

| Data source type            |
| --------------------------- |
| `BOOLEAN`                   |
| `DECIMAL`                   |
| `INTEGER`                   |
| `STRING`                    |
| `DATE`                      |
| `TIME` (time zoned)         |
| `TIME` (not time zoned)     |
| `DATETIME` (time zoned)     |
| `DATETIME` (not time zoned) |

Example

| username (STRING) | age (INTEGER) | first\_name (STRING) | height (DECIMAL) | email (STRING)                              | dob (DATETIME, time zoned)               | premium (BOOLEAN) |
| ----------------- | ------------- | -------------------- | ---------------- | ------------------------------------------- | ---------------------------------------- | ----------------- |
| admin             | 64            | Bob                  | 1.8              | [bob@example.com](mailto:bob@example.com)   | 1962-12-31T16:50:31+05:00                | true              |
| bill              | 27            | Bill                 | 1.92             | [bill@example.com](mailto:bill@example.com) | 1997-05-24T19:18:12Z                     | false             |
| jill              | 15            | Jill                 | 1.70             | [jill@example.com](mailto:jill@example.com) | 2009-11-07T04:34:01+01:00\[Europe/Paris] | false             |
| jane              | 74            | Jane                 | 1.81             | [jane@example.com](mailto:jane@example.com) | 1952-01-13T10:10:10-12:00                | true              |

#### Date type

For `DATE`, `TIME` and `DATETIME` types, you can specify your own format string using the elements in the following table:

| Letter | Date or Time Component                           | Presentation       | Examples                              |
| ------ | ------------------------------------------------ | ------------------ | ------------------------------------- |
| G      | Era designator                                   | Text               | AD                                    |
| y      | Year                                             | Year               | 1996; 96                              |
| Y      | Week year                                        | Year               | 2009; 09                              |
| M      | Month in year                                    | Month              | July; Jul; 07                         |
| w      | Week in year                                     | Number             | 27                                    |
| W      | Week in month                                    | Number             | 2                                     |
| D      | Day in year                                      | Number             | 189                                   |
| d      | Day in month                                     | Number             | 10                                    |
| F      | Day of week in month                             | Number             | 2                                     |
| E      | Day name in week                                 | Text               | Tuesday; Tue                          |
| u      | Day number of week (1 = Monday, ..., 7 = Sunday) | Number             | 1                                     |
| a      | Am/pm marker                                     | Text               | PM                                    |
| H      | Hour in day (0-23)                               | Number             | 0                                     |
| k      | Hour in day (1-24)                               | Number             | 24                                    |
| K      | Hour in am/pm (0-11)                             | Number             | 0                                     |
| h      | Hour in am/pm (1-12)                             | Number             | 12                                    |
| m      | Minute in hour                                   | Number             | 30                                    |
| s      | Second in minute                                 | Number             | 55                                    |
| S      | Millisecond                                      | Number             | 978                                   |
| z      | Time zone                                        | General time zone  | Pacific Standard Time; PST; GMT-08:00 |
| Z      | Time zone                                        | RFC 822 time zone  | -0800                                 |
| X      | Time zone                                        | ISO 8601 time zone | -08; -0800;  -08:00                   |


# Managing Database Connections
Source: https://docs.wiremock.io/data-sources/managing-database-connections

Creating and editing the database connection to your test database

<Tip>
  The database connection feature is currently in **private beta**.  If you would like access to this feature contact us
  via the `Get Support` link in the menu bar
</Tip>

## Creating a database connection

Database connections can be created at the organisation level, meaning that the database connections you create can
be shared among the members of your organisation.

To create a database connection, you must be an administrator of your organisation and your database must be
accessible - either publicly or via our AWS VPC.  If you would like to explore the VPC option please contact us.

To create a database connection:

* Navigate to the Data Sources page.

<img alt="Data source menu item" />

* Click on the link, `View Connections`

<img alt="View database connections link" />

* Click on the button, `Create new database connection`

<img alt="Create database connection button" />

* Fill out the form with the details of your database connection

<img alt="Create database connection button" />

The connection details you will need are:

* A name for the connection.  This must be unique across all the database connections in you organisation
* A database type - we currently support `Postgresql`, `MySql`, `Oracle` and `MS SQL Server`
* The hostname for the connection
* The port the database is running on
* The name of the database
* The username used to connect to the database
* The password used to connect to the database

Once you have entered all the details for your database connection you can test that they allow a successful connection
to your database by clicking on the `Test connection` button.

<img alt="Database connection test connection success" />

If the connection request is unsuccessful, an error message will be displayed.

<img alt="Database connection test connection unsuccessful" />

* Once you are happy with your database connection details, click on the `Save` button to save your connection details.

<Tip>
  All database passwords you provide will be encrypted before they are stored to ensure maximum security to your data.
</Tip>

You are now ready to create your first [database connection data source](./managing-database-data-sources).

## Editing a database connection

Database connections can be updated after creation. To edit a database connection, you must be an administrator of your
organisation.

To edit a connection:

* Navigate to the [Database connections page](https://app.dev.wiremock.cloud/data-sources/connections).
* Click on the connection you wish to edit, from the list provided.
* Update your database connection.
* Click on the `save` at the bottom of the page.

<img alt="Edit database connection" />

For security, the password is not returned on the edit screen.  You can still update any of the fields and if you
leave the password field blank it will keep the existing password and update all other fields.  To update your
password or re-test the connection you will need to enter your password in the field provided.

## Deleting a database connection

Database connections can be deleted from your organisation. To delete a database connection, you must be an
administrator of your organisation.

To delete a database connection:

* Navigate to the [Database connections page](https://app.dev.wiremock.cloud/data-sources/connections).
* Click on the delete icon for the connection you want to remove.

<p>
  <img alt="Delete a database connection" title="Delete a database connection" />
</p>

Clicking on the delete icon will open a confirmation dialog. Click the `Confirm` button to confirm the deletion or
`Cancel` to close the dialog without deleting the connection.

<p>
  <img alt="Delete a database connection confirmation" title="Delete a database connection confirmation" />
</p>

Clicking `Confirm` will delete the data source, only if there are no data sources in your organisation that are
currently using it.  If the database connection you are trying to delete is in use an error will be displayed, and you
will not be able to delete the connection.  You will need to update or delete the data sources that are using the
connection and then try to delete again.

<p>
  <img alt="Delete a database connection confirmation error" title="Delete a database connection confirmation error" />
</p>


# Creating & Editing Database Data Sources
Source: https://docs.wiremock.io/data-sources/managing-database-data-sources

Setting up your external test data from a database

<Tip>
  The database data source feature is currently in **private beta**.  If you would like access to this feature contact us
  via the `Get Support` link in the menu bar
</Tip>

## Creating a database data source

Data sources can be created at the organisation level, meaning that the Data sources you create can be shared among the
members of your organisation.

To create a database data source, you first need to create a [database connection](./managing-database-connections)

To create a data source:

* Navigate to the Data Sources page.

  <img alt="Data source menu item" />

* Click on the button, `+Create new data source`.

  <img alt="Create Data source button" />

* Choose `Database based` from the dropdown

  <img alt="Create database data source" />

* Provide a name for your data source.

* Select the database connection you wish to use with this data source

* Enter the name of the table you wish to use with this data source. This can be the name of a table, or a view within
  your database.

* Click `save` at the bottom of the page.

Once the data source has been saved you can view a preview (the first 10 rows) of the data returned from the specified
table by navigating to the data sources page and clicking on the data source you wish to preview.

If the specified table could not be found, an error will be displayed.

<img alt="Edit database data source" />

## Editing a database data source

Data sources can be updated after creation.

To edit a data source:

* Navigate to the Data Sources page.
* Click on the data source you wish to edit, from the list provided.
* Update your data source.
* Click on the `save` at the bottom of the page.

Once in the data source page, you will be able to:

* Change the name of the data source
* Change the database connection used by the data source
* Change the table name referenced by the data source


# Data Sources - Using External Test Data
Source: https://docs.wiremock.io/data-sources/overview

Using External Test Data.

WireMock Cloud provides the ability to use your own test data in your mock APIs, when both matching and rendering responses.

## Usage

To use a data source, it must be [attached](#attaching-a-data-source-to-a-stub) to one (or more) stub(s) of a mock API.
Data sources have two primary functions when attached to a stub mapping:

* [Custom stub matching](#custom-stub-matching) based on the result of a configurable query
* [Providing data](#rendering-data-in-response) to be used in a stub's [response template](/response-templating/basics).

### Attaching a data source to a stub

Once your data source has been set up correctly, following the steps in [creating a CSV data source](./managing-csv-data-sources),
or [creating a database data source](./managing-database-data-sources) it can be attached to a stub.

To attach a data source to a stub in WireMock Cloud, navigate to the desired stub and open the "Data source" section.

<img alt="Stub Data Source Section" />

Select the data source you wish to attach from the dropdown list.

<img alt="Stub Data Source Dropdown List" />

Enter a `WHERE` clause, or leave blank. The `WHERE` clause allows you to use `ORDER BY`, `LIMIT` and `OFFSET` to get
consistent ordering and pagination.

<img alt="Stub Data Source Where Clause" />

Once saved, your data source is now attached to your stub and will be used when [matching incoming requests](./overview#custom-stub-matching) and [rendering responses](./overview#rendering-data-in-response).

#### Deleting a data source from a stub

If you no longer wish for your stub to have the capabilities provided by data sources, you can detach/delete the data source from the stub at any time.
To detach a data source from a stub, simply open the "Data source" section of the desired stub and click the delete button, then save.

<img alt="Stub Data Source Detach Button" />

#### Which stubs can reference attached data sources?

Once a data source has been created, it can be used by all stubs within the organization.
However, a stub can only have a single data source attached to it at a time

### Custom stub matching

Attaching a data source to a stub allows the stub to only match a request when the data source returns non-empty data.
The data that a data source returns for a given request and stub can be filtered via a configurable ANSI standard SQL query.
This query is attached to a stub alongside the data source.

<img alt="Stub Data Source Where Clause" />

This query acts as the `WHERE` clause of a standard SQL statement that is executed on the data source.
The columns of a data source can be queried as if they were columns of an SQL table.
For instance, if your data source has an "age" column of type `INTEGER`, you can retrieve all rows where age is greater than twenty-five using the query `age > 25`.
Each data source column type maps to an SQL column type:

| Data source type            | SQL type                   |
| --------------------------- | -------------------------- |
| `BOOLEAN`                   | `BOOLEAN`                  |
| `DECIMAL`                   | `FLOAT`                    |
| `INTEGER`                   | `INTEGER`                  |
| `STRING`                    | `VARCHAR`                  |
| `DATE`                      | `DATE`                     |
| `TIME` (time zoned)         | `TIME WITH TIME ZONE`      |
| `TIME` (not time zoned)     | `TIME`                     |
| `DATETIME` (time zoned)     | `TIMESTAMP WITH TIME ZONE` |
| `DATETIME` (not time zoned) | `TIMESTAMP`                |

All standard SQL operators of each type are supported in the attached query (e.g. `+`, `-`, `=`, `<`, `>`, `AND`, `OR`, `EXISTS`, `BETWEEN`, etc.).

#### Handlebars templating in query

The data source query supports handlebars templating in order to dynamically create queries based off the contents of an incoming request.
The model available in the template is [the same request data model that is provided in the response template](/response-templating/basics/#the-data-model).

For example, if your data source contains a "first\_name" column, you can filter the data source via a query parameter provided in the request like so: `first_name = '{{request.query.name}}'`.
When a request is sent to the mock API with a `name` query parameter, the value of this parameter will be inserted into the `WHERE` clause.
So a query string that contains `name=alice` will result in a `WHERE` clause of `first_name = 'alice'`.

#### Potential pitfalls

As in standard SQL, to reference a column whose name contains whitespace or starts with a digit, the column name must be surrounded by double quotes (e.g. `"first name" == 'bob'`).
Quoting a column name also enforces case sensitivity (i.e. the casing in the query must match the casing of the column name exactly).

Currently, only simple `WHERE` clause expressions that are part of the ANSI standard SQL specification are supported including
`ORDER BY`, `LIMIT` and `OFFSET`.  Sub-queries are not officially supported.

An empty query will return the entirety of the data source.
Thus, the stub's data matcher will always return a match, as long as the data source itself is not empty.

#### Disabling matching

This matching functionality can be disabled via a checkbox.

<img alt="Stub Data Source Match Checkbox" />

When disabled, no matching based on the returned data will be performed.
In other words, if all other matchers of a stub return a match for a particular request, the stub will be considered a match, even if the data source returned no data.
In this scenario, the available data items in the [response template](#rendering-data-in-response) will be an empty list.

### Rendering data in response

Attaching a data source to a stub allows the data contained in the data source to be rendered in the response via [response templating](/response-templating/basics).
The data available from the data source for a particular request's response is the result of evaluating the stub's [data source query](#custom-stub-matching) for that request.

For instance, if a stub is configured with a query of `age > 25`, then the data available in the response template will be limited to all rows whose "age" column exceeds twenty-five.
This data can be referenced in the response template via the `data.items` property.
This property is a list of all the rows returned by the data source query.
For example, to render a JSON array of the name of each returned row, the following response template could be used:

```handlebars theme={null}
[
  {{~#arrayJoin ',' data.items as |item|~}}
    {
      "id": {{item.id}},
      "name": "{{item.name}}"
    }
  {{/arrayJoin}}
]
```

As well as iterating over the entire result list, rows can be referenced by their individual index (e.g. `{{ data.items.0.name }}'`).

#### Potential pitfalls

Field names containing whitespace or starting with a digit must be surrounded by square brackets.
For example, a column with the name "first name" would be referenced like so: `{{ data.items.0.[first name] }}'`.

Supplying an empty query will provide the entirety of the data source to the template model.


# Data Sources - Plan Limits
Source: https://docs.wiremock.io/data-sources/plan-limits

Limitations of your data source usage.

WireMock Cloud applies limits to data sources dependent upon the plan your organisation is subscribed to.

On the WireMock Cloud free plan, an account is limited to a maximum of 3 data sources.
Each data source can contain up to 100 rows and each row must not exceed 10KB in size.
During the enterprise trial period, this limit is increased to 1000 rows with a maximum row size of 100KB.

To increase the limits applied to your organisation, [contact the WireMock team today](https://www.wiremock.io/contact-now).

## Disabled data sources

If an account/organisation is downgraded to a plan that causes their data sources to exceed the new plan's limits, these exceeding data sources will be disabled.
Any stubs with disabled data sources attached will lose their [data matching abilities](#stub-matching) and [access to the data](#data-source-response-templating) in their response template.
Disabled data sources can be enabled at any time by updating them to fit within the account plan's limits or, of course, by [upgrading to a different plan](https://www.wiremock.io/contact-now).

### Stub Matching

If a stub is using a data source that has been disabled, the stub will no longer [match incoming requests](./overview#custom-stub-matching) if the
`Matches stub only if data is found` tick box is checked on the Stub form. If this tick box is not checked, the stub
will continue to match incoming requests, but the data source will not be queried.

### Data source response templating

If a data source is disabled, any [response templates](./overview#rendering-data-in-response) that are using the data source will no longer be able to access the
data source data. The response template will still be rendered, but the data source data will not be available.


# Sharing Data Sources
Source: https://docs.wiremock.io/data-sources/sharing-data-sources

Sharing your data source with other members within your organisation.

Like other entities in WireMock Cloud (e.g. mock APIs, API templates, teams etc.), a data source belongs to a particular organisation.

Namely, the organisation that the user that created the data source belongs to.

By default, when a data source is created, the user that created it will be assigned as an admin of that data source.

As with other WireMock Cloud entities, all organisation admins will also receive the admin role for the created data source.

The admin role allows the assigned user to read, write and delete the data source, as well as assign other users/teams roles over the data source.

To assign a role to a user/team for a data source, simply navigate to the desired data source, open the "Share" dialog window and search for the user/team.

<img alt="Stub Data Source Share Button" />

<img alt="Stub Data Source Share Window" />

Once you have selected the desired subject and picked the appropriate role for that subject, click the "Invite"/ "Share" button.
The subject(s) should not be able to view the data source from their WireMock Cloud account.


# Serving a Default Response
Source: https://docs.wiremock.io/default-responses

Configuring a stub to serve a default response when a specific match for the request is not is found

By default, WireMock Cloud will serve a generic 404 page if an incoming HTTP request is not matched to any stub mapping.
Often this is not a problem, but in some instances it is desirable to serve your own response.

This can be achieved using the Priority parameter when creating stubs. By creating a stub which has loose (non-specific)
matching criteria and a low priority setting, requests will "fall through" to this if they're not matched to a more specific stub.

## Example

Suppose you want to serve a `403 Unauthorized` response with a meaningful response body when a request is not matched rather than the default 404. Additionally you
want to serve 200 response when a `GET` request is made to `/examples/12`.

Start by creating a stub with `ANY` as the method. Open the Advanced section and change the URL match type to `Any URL`.
Also in the Advanced section set the Priority to 10 (the lowest).

<img title="Default request" />

In the Response section, set the Status to `403` and the body content to `"Sorry, you can't do that"`.

<img title="Default response" />

Create a second stub with the method set to `GET`, the URL to `/examples/12` and the response body to `"Example 12 body"` (keeping the Status as `200`).

Now if you make a request that matches the specific stub you will see a response with a `200` status and the success message:

```
$ curl -v http://example.wiremockapi.cloud/examples/12

> GET /examples/12 HTTP/1.1
> Host: example.wiremockapi.cloud
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Transfer-Encoding: chunked
<
Example 12 body
```

Whereas if you make a request to a URL with no stub to match you will see the default `403` response.

```
$ curl -v http://example.wiremockapi.cloud/examples/12222222

> GET /examples/12222222 HTTP/1.1
> Host: example.wiremockapi.cloud
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 403 Forbidden
< Transfer-Encoding: chunked
<
Sorry, you can't do that
```


# Response Delays
Source: https://docs.wiremock.io/delays

Adding delays to stub responses

Calls over a network to an API can be delayed for many reasons e.g. network congestion or excessive server load. For applications
to be resilient they must be designed to cope with this inevitable variability, and tested to ensure they behave as expected
when conditions aren't optimal.

In particular it is important to check that timeouts work as configured, and that your end user's experience is maintained.

WireMock Cloud stubs can be served with a fixed or random delay, or can be "dribbled" back in chunks over a defined time period.

## Fixed delay

A fixed delay straightforwardly adds a pause for the specified number of milliseconds before serving the stub's response.

<img title="Fixed delay" />

## Random delay

Random delay adds a random pause before serving the response. Two statistical distributions are available:

### Uniform

<img title="Random uniform delay" />

### Log normal

<img title="Random lognormal delay" />

## Chunked dribble delay

Chunked dribble delay flushes the response body out in chunks over the total defined period:

<img title="Chunked dribble delay" />

## Delays and proxying

Fixed or random delays can be added to proxy responses in addition to direct responses, however chunked delays cannot at present.


# WireMock API Device Authorization Flow
Source: https://docs.wiremock.io/device-authorization-flow

How to use the OAuth 2.0 Device Authorization Flow to authenticate to the WireMock Cloud API

Enterprise customers may wish to interact with the WireMock Cloud API from their own clients using
OAuth 2.0. WireMock Cloud supports the OAuth 2.0 Device Authorization Flow for these customers.

## Requirements

You will need to have requested the creation of a new OAuth Client by WireMock Cloud.

You will need to tell us:

* The maximum time you allow between interactions before the user has to reauthenticate
* The maximum total time you allow between authentications, eve if the user is regularly interacting

## Inputs

* `{client_id}`: The OAuth client (in Auth0, the Application id) provided by WireMock Cloud

### Initiate the Client

```http request theme={null}
GET https://login.wiremock.cloud/.well-known/openid-configuration
Accept: application/json
```

returns:

#### `discover_urls`

```json theme={null}
{
  "token_endpoint": "{fully_qualified_url}",
  "device_authorization_endpoint": "{fully_qualified_url}",
  "revocation_endpoint": "{fully_qualified_url}"
}
```

### Initiate the Device Authorization Flow

```http request theme={null}
POST {discover_urls.device_authorization_endpoint}
Content-Type: application/x-www-form-urlencoded

client_id={inputs.client_id}&audience=https%3A%2F%2Fapi.wiremock.cloud&scope=openid+email+offline_access
```

returns:

#### `device_authorization`

```json theme={null}
{
  "device_code": "{random_value}",
  "user_code": "{legible_random_value}",
  "verification_uri": "{fully_qualified_url}",
  "expires_in": 900,
  "interval": 5,
  "verification_uri_complete": "{fully_qualified_url}"
}
```

`expires_in` and `interval` are values in seconds.

### Pass control to the user to authenticate

Something like this should be rendered:

```
Attempting to automatically open the authentication page in your default browser.

Code: {device_authorization.user_code}

If the browser does not open or you wish to use a different device to authorize this request, open the following URL:

{device_authorization.verification_uri_complete}

Waiting for login...
```

if possible, `{device_authorization.verification_uri_complete}` should be opened automatically in
the user's browser.

### Poll for successful authentication

Every `{device_authorization.interval}` seconds until `{device_authorization.expires_in}` seconds have passed you poll
as so:

```http request theme={null}
POST {discover_urls.token_endpoint}
Content-Type: application/x-www-form-urlencoded

client_id={inputs.client_id}&device_code={device_authorization.device_code}&grant_type=urn:ietf:params:oauth:grant-type:device_code
```

You should be returned one of these two responses:

```http response theme={null}
HTTP/2 403 Forbidden
Content-Type: application/json

{
  "error": "authorization_pending",
  "error_description": "User has yet to authorize device code."
}
```

which means "poll again in `{device_authorization.interval}` unless
`{device_authorization.expires_in}` has passed"

or

#### `token_response`

```http response theme={null}
HTTP/2 200 OK
Content-Type: application/json

{
  "access_token": "{access_token}",
  "token_type": "{token_type}",
  "expires_in": 300,
  "refresh_token": "{refresh_token}",
  "id_token": {id_token}
}
```

You can then interact with the API using this request header:

`Authorization: {token_response.token_type} {token_response.access_token}`

### Refresh Tokens

WireMock access tokens are JWTs, and cannot be revoked. Consequently they are short-lived (sub 10
minutes).

In order to avoid having to authenticate regularly, the client may exchange a refresh token (which
can be revoked) for a new access token.

A refresh token, once used, becomes invalid - a new one is returned along with the new access token.
Any attempt to use an invalid refresh token will also invalidate the current valid refresh token,
forcing a reauthentication.

Refresh tokens can be explicitly revoked on logout.

#### Exchanging a refresh token for a new access token

```http request theme={null}
POST {discover_urls.token_endpoint}
Content-Type: application/x-www-form-urlencoded

client_id={inputs.client_id}&refresh_token={token_response.refresh_token}&grant_type=refresh_token
```

returns

##### `token_response`

```json theme={null}
{
  "access_token": "{access_token}",
  "token_type": "{token_type}",
  "expires_in": 300,
  "refresh_token": "{refresh_token}"
}
```

#### Invalidating a refresh token

```http request theme={null}
POST {discover_urls.revocation_endpoint}
Content-Type: application/x-www-form-urlencoded

client_id={inputs.client_id}&token={token_response.refresh_token}
```


# Dynamic State Shopping Basket Example
Source: https://docs.wiremock.io/dynamic-state/basket-example

A workable example of using dynamic state to mock CRUD operations on a shopping basket

To learn how to use WireMock Cloud's Dynamic State capabilities, let's look at a working example of using dynamic state
to mock CRUD operations on a shopping basket.

## Getting started

You can start your own copy of this example Mock API from a template just by clicking on this link:
[Launch Shopping Basket Mock](https://app.wiremock.cloud/new-mock/stateful-shopping)

## Exploring the behaviour

### Get an empty basket

Let's start by seeing what is in a shopping basket. Make a request to any basket:

```bash theme={null}
curl -v 'https://my-basket-demo.wiremockapi.cloud/baskets/1/items'
```

You should see a response that looks like this:

```json theme={null}
{
  "items" : [ ],
  "total" : 0
}
```

You'll get the same thing if you request this:

```bash theme={null}
curl -v 'https://my-basket-demo.wiremockapi.cloud/baskets/2/items'
```

### Add some items to some baskets & retrieve those baskets

Let's add some items to some baskets. First let's add a couple of items to the basket with id `1`:

```bash theme={null}
curl -v -X POST \
  -d '{ "id": "1", "item": "Socks", "quantity": 5 }' \
  'https://my-basket-demo.wiremockapi.cloud/baskets/1/items'
  
curl -v -X POST \
  -d '{ "id": "2", "item": "Shoes", "quantity": 3 }' \
  'https://my-basket-demo.wiremockapi.cloud/baskets/1/items'
```

Now when we get the items in the basket with id `1` we should see the items we just added:

```bash theme={null}
curl -v 'https://my-basket-demo.wiremockapi.cloud/baskets/1/items'
```

returns

```json theme={null}
{
  "items" : [ {
    "id" : "1",
    "item" : "Socks",
    "quantity" : 5
  }, {
    "id" : "2",
    "item" : "Shoes",
    "quantity" : 3
  } ],
  "total" : 2
}
```

However, when we retrieve a *different* basket it will still be empty:

```bash theme={null}
curl -v 'https://my-basket-demo.wiremockapi.cloud/baskets/2/items'
```

returns

```json theme={null}
{
  "items" : [ ],
  "total" : 0
}
```

Have a play with adding items to different baskets and retrieving those baskets; you can use just about anything as the
`basketId` in the path template `/baskets/{basketId}/items`.

### Retrieve specific items from a basket

We can also retrieve a specific item from a basket by id. Try this:

```bash theme={null}
curl -v 'https://my-basket-demo.wiremockapi.cloud/baskets/1/items/2'
```

It should return

```json theme={null}
{
  "id" : "2",
  "item" : "Shoes",
  "quantity" : 3
}
```

However, if you try and get an item you never added, you should get a 404:

```bash theme={null}
curl -v 'https://my-basket-demo.wiremockapi.cloud/baskets/1/items/56'
```

returns

```json theme={null}
{
  "error": "Cannot find item id 56 in basket 1"
}
```

### Remove an item from a basket

You can also remove a single item from a basket. Try this:

```bash theme={null}
curl -v -X DELETE \
  'https://my-basket-demo.wiremockapi.cloud/baskets/1/items/2'  
```

```bash theme={null}
curl -v 'https://my-basket-demo.wiremockapi.cloud/baskets/1/items'
```

should now return

```json theme={null}
{
  "items" : [ {
    "id" : "1",
    "item" : "Socks",
    "quantity" : 5
  } ],
  "total" : 1
}
```

and

```bash theme={null}
curl -v 'https://my-basket-demo.wiremockapi.cloud/baskets/1/items/2'
```

should now return

```json theme={null}
{
  "error": "Cannot find item id 2 in basket 1"
}
```

### Entirely empty the basket

You can remove all items from a basket. Try this:

```bash theme={null}
curl -v -X DELETE \
  'https://my-basket-demo.wiremockapi.cloud/baskets/1/items'  
```

```bash theme={null}
curl -v 'https://my-basket-demo.wiremockapi.cloud/baskets/1/items'
```

should now return

```json theme={null}
{
  "items" : [ ],
  "total" : 0
}
```

### Conclusion

You should now be pretty happy that your Mock API that you have spun up from the template is behaving like a fairly
orthodox JSON over HTTP API, and crucially that it is both stateful, and that the state is localized to a specific
basket id.

So let's start to understand how it works.

## How it Works

We'll take it stub by stub, examining how the stub delivers the functionality we need.

### The "Get basket contents" Stub

This stub uses the "Path template" match type for a method `GET` and a path of `/baskets/{basketId}/items`. That means
it will accept any valid URI path segment as a `basketId`. It will be available to Handlebars templates as
`request.path.basketId`.

You will note that the "State" section is still folded up. That's because this is a read only stub; it doesn't alter
state at all. Any stub can render state variables in its response, you don't need to toggle Dynamic State on to do that.

The stateful configuration comes in the Response definition. Unsurprisingly "Enable dynamic response templating" is
checked. The body contains the following Handlebars template:

```handlebars theme={null}
{{val (state 'basketItems' context=request.path.basketId) or='[]' assign='basketItems'}}
{
    "items": {{basketItems}},
    "total": {{size (parseJson basketItems)}}
}
```

Let's break it down.

In the first line, the [`state` helper](./overview/#setting-and-rendering-simple-state) reads the value of the key
`'basketItems'` in the context `request.path.basketId`. You'll notice the key there is a string, but the context
parameter is not - it looks up the `basketId` path parameter from the request. Those two values are combined to look up
the items.

At first the lookup will return `null`, because we have never initialised the `'basketItems'` key in any context,
including the current value of `request.path.basketId`. To handle that case we use the [`val` helper](/response-templating/misc-helpers/#val-helper),
which takes a value as its context, but can use an `or` option to default to a different value should that value be
`null`. In this case we default it to `'[]'`; state values are all stored as strings, and we interpret them as JSON when
we retrieve them.

Finally, we use the `assign` option on the `val` helper to put the result of the `val` helper into the Handlebars model
with the key `basketItems`. From now on we can just use `basketItems` in Handlebars helpers, or
`{{ basketItems }}` to render them.

Now let's look at what we actually output:

```handlebars theme={null}
{
    "items": {{basketItems}},
    "total": {{size (parseJson basketItems)}}
}
```

This is just JSON with some Handlebars interpolations. `"items": {{basketItems}}` renders the
`basketItems` key we defined in the `val` helper above - either the value of the `basketItems` state key or `[]` if it
was `null`.

`"total": {{size (parseJson basketItems)}}` uses a combination of the `parseJson` helper to turn
`basketItems` into JSON in memory (remember state is just stored as a string) and the
[`size` helper](/response-templating/misc-helpers/#size) to work out how big the resulting array is.

Let's move on to adding items.

### The "Add item" Stub

Like the "Get basket contents" stub, this stub uses the "Path template" match type for a path of
`/baskets/{basketId}/items`, but this time it matches if the method is `POST`.

It also has a [Body matcher](/request-matching/json/), which uses
[JsonUnit expressions](/request-matching/json/#using-placeholders-to-ignore-specific-json-attributes)
to only match the format of JSON we expect in a new item.

This time the "State" panel is opened, and "Dynamic state" is toggled on. This is because we now have a single "State
operation" defined.

It has its "Context" set to `{{request.path.basketId}}`. "Context" identifiers are just strings,
but they can be built using Handlebars templates. In this case the context is derived from the `basketId` path parameter
on the request. It has its "Key" set to `'basketItems'`, its "Operation" to `SET` and its "Value" to

```handlebars theme={null}
{{jsonArrayAdd (val previousValue or='[]') request.body}}
```

Just like context identifiers, state values are just strings emitted by Handlebars templates. They have a special key
provided to them, `previousValue`; it is set to the value of the key in the context when the operation runs. It will be
`null` if the key has no value in this context. In this case we use the `val` helper described above to default it to an
empty JSON array string. We then use the [`jsonArrayAdd` helper](/response-templating/json/#adding-to-a-json-array) to
append the entire request body as a new item in the array. We know the request body will be a valid JSON object because
of the Body matcher defined above.

### The "Get item by ID (success)" Stub

This stub uses the "Path template" match type for a method `GET` and a path of `/baskets/{basketId}/items/{itemId}`.
That means it will accept any valid URI path segment as a `basketId` or an `itemId` and expose them to Handlebars
templates as `request.path.basketId` and `request.path.itemId` respectively.

Like the "Add item" stub, the "State" panel is opened, and "Dynamic state" is toggled on. However, instead of a state
operation, this stub defines a request matcher. The matcher has its "Context" set to
`{{request.path.basketId}}` and its "Key" set to `'basketItems'`, just like the "Add item" state
operation. However, it then has the standard matching form. In this case we use the ["matches JSONPath" matcher](/request-matching/matcher-types/#matchesjsonpath)
to say that this stub only matches if the [JSONPath](https://www.ietf.org/archive/id/draft-goessner-dispatch-jsonpath-00.html)
expression `$.[?(@.id == '{{request.path.itemId}}')]` finds an object. This expression assumes the
top level JSON is an array, and looks for an item inside that array with a key `id` and a value
`'{{request.path.itemId}}'`. You'll note that the expression here is actually a Handlebars
template, so it is able to match against parts of the request model.

This means that this entire stub will only match if the `itemId` is in the `basketItems` for the current `basketId`
context.

The request body ("Enable dynamic response templating" checked) then looks like this:

```handlebars theme={null}
{{#assign 'findExpression'}}$.[?(@.id == '{{request.path.itemId}}')]{{/assign}}
{{jsonPath (jsonPath (state 'basketItems' context=request.path.basketId) findExpression) '$[0]'}}
```

We've built up exactly the same JSONPath expression as in the matcher, and assigned it to the key
`findExpression`. We have inlined retrieving the `basketItems` key from the state with the correct context using `(state
'basketItems' context=request.path.basketId)`. We can then use the
[`jsonPath` helper](/response-templating/json/#extracting-data-with-jsonPath)
to extract that item from the `basketItems` as so: `jsonPath (state 'basketItems' context=request.path.basketId)
findExpression`. We know it will be there because otherwise the stub would not have matched. Unfortunately [JSONPath
provides no way to debrief a result array as part of the expression](https://github.com/json-path/JsonPath/issues/272),
so we have to wrap it in a further `jsonPath` helper call to retrieve the single element of the resulting array.

### The "Get item by ID (not found)" Stub

The "Get item by ID (not found)" stub uses exactly the same `GET` and path template `/baskets/{basketId}/items/{itemId}`
matchers as the "Get item by ID (success)" stub. However, it is set to a lower Priority (7) than the success stub (5),
and consequently it only matches if the success stub does *not* match. This means we do not need to do any cleverness
with dynamic state; we can simply make it return a 404 with a useful error message derived dynamically from the path.

### The "Delete item by ID" Stub

The "Delete item by ID" stub uses the same path template `/baskets/{basketId}/items/{itemId}` matcher as the "Get item
by ID (success)" stub, but with the `DELETE` method.

The "State" panel is opened, and "Dynamic state" is toggled on, with a single state operation very similar to the "Add
item" stub. As we are used to it has its "Context" set to `{{request.path.basketId}}`, its
"Key" set to `'basketItems'` and its "Operation" to `SET`. However, its "Value" is

```handlebars theme={null}
{{#assign 'removalExpression'}}$.[?(@.id == '{{request.path.itemId}}')]{{/assign}}
{{jsonRemove previousValue removalExpression}}
```

The `removalExpression` should be familiar - it's the same JSONPath expression as we used in the "Get item by ID
(success)" stub, both to match and to render the item in the `basketItems` array. This time however we pass it to the
[`jsonRemove` helper](/response-templating/json/#removing-from-a-json-array-or-object) which will render an array
without any of the elements from the `previousValue` that match the expression.

### The "Empty Basket" Stub

The "Empty Basket" stub uses the same path template `/baskets/{basketId}/items` matcher as the "Get basket contents"
stub, but with the `DELETE` method.

The "State" panel is opened, and "Dynamic state" is toggled on, with a single state operation very similar to the "Add
item" stub. As we are used to it has its "Context" set to `{{request.path.basketId}}` and its
"Key" set to `'basketItems'`. However, its "Operation" is set to `DELETE`. This means that when this stub matches the
`basketItems` key will be entirely removed in the `{{request.path.basketId}}` context.

(We could instead have used a `SET` operation with a "Value" of `[]`.)


# Create Stateful Endpoint Set
Source: https://docs.wiremock.io/dynamic-state/create-stateful-set

Assisted Creation of Stateful Mock APIs

The **Create Stateful Endpoint Set** feature in WireMock Cloud automates the creation of pre-configured stateful stubs. This allows for quick setup of RESTful API mocks with built-in request-response handling and state management across multiple HTTP methods.

Using this feature, WireMock Cloud automatically generates:

* **GET, POST, PUT, and DELETE** stubs for the specified resource
* A **default 404 response** for unmatched requests

This feature requires the **REST mock API template**.  It is not available in the Unstructured / Blank mock API template.

## How It Works

You provide:

1. Create a new **REST mock API**

2. Click the **Stateful Set** button near the bottom of the stub list:

   <img alt="Stateful set button" />

3. Supply a **POST endpoint page** (e.g., `/users`):

   <img alt="Stateful set post endpoint" />

4. Provide a **sample request body** for the `POST`
   e.g.:

   ```json theme={null}
   {
       "firstName": "Betty",
       "lastName": "Boop",
       "organization": "Finance"
   }
   ```

   <img alt="Stateful set request body" />

5. Input a **correlated sample response body** for the given request body
   e.g.:

   ```json theme={null}
   {
       "contactId": "4",
       "firstName": "Betty",
       "lastName": "Boop",
       "organization": "Finance",
       "created_utc": "2025-02-28T15:58:35Z"
   }
   ```

   <img alt="Stateful set response body" />

6. At the bottom of the dialog, select which operations you'd like stubs to be created for:

   <img alt="Stateful set target operation selection" />

7. Click the **Create Stateful set** button:

   <img alt="Create Stateful set button" />

New stubs will be created that are automatically configured with stateful functionality.

* A **POST** stub that creates a new resource in the mock API's stateful memory
* A **GET** stub that lists all of the resources stored in the mock API's stateful memory
* A **GET** stub that retrieves a stored resource by its identifier
* A **PUT** stub that updates the stored data of a resource
* A **DELETE** stub that removes the stored resource
* A **DELETE** stub that removes all stored resources from the mock API's stateful memory
* A fallback **404 response** for unknown requests

You will want to further modify the stubs to better simulate the API's real-world stateful behavior.


# Dynamic State Basics
Source: https://docs.wiremock.io/dynamic-state/overview

Creating and Calling Stateful Stubs

WireMock Cloud provides the ability to set and use dynamic state in your stubs. This allows you to mock stateful
journeys, such as creating a resource and then retrieving it. This is useful for situations where you may want to mock
things like account balances, changing user attributes or any session where the data may need to be dynamically
modified.

State can be managed within a *context* of your choosing. This could, for instance, allow you to use a context per user
so that the same stateful journey using the same stubs can be run multiple times simultaneously without affecting each
other. It could also be used to allow you to use the same set of stubs to do CRUD operations on the state of multiple
collections - see [the workable Dynamic Shopping Basket example](./basket-example/).

Dynamic State is a more sophisticated and powerful replacement for
[the existing Scenarios functionality](/dynamic-state/stateful-scenarios), which only offers a simple global state machine.

## Concepts

* **State Value**\
  A State Value is a mutable string, stored against a Key within a Context. It can be used in request matching; created,
  changed or removed in State Operations; and rendered in response bodies and webhook request bodies. It is typically
  defined dynamically using a [Handlebars template](https://handlebarsjs.com/). It is also worth knowing that state values can be used in webhook headers and webhook URLs, as well.

  State Values are stored in a Least Recently Used cache, and no guarantee is made about how long they will persist.
* **Variable**\
  A Variable is similar to a State Value, but it does not have a Context and does not need the `state` Handlebars helper
  to render it in a Handlebars template. Instead, it lives only for the lifetime of the request, and is accessible at
  the top level of the Handlebars model. It can be used in State Operations and Variable Definitions, and rendered in
  response bodies and webhook request bodies. It is typically defined dynamically using a Handlebars template. It cannot
  be one of our reserved words: `request`, `response`, `parameters`, `data`, `event`, `config`, `originalRequest` or
  `originalResponse`.
* **Key**\
  A key is a string identifier such as `itemId`. A State Value is stored and looked up using a Key. A Key references
  different State Values in different Contexts. For keys defined on state operations, a Handlebars template that has
  access to the request model, such as `{{ request.path.userId }}`, can be used to build the key. This is not the case
  for keys defined on request variables, which must be plain strings.
* **Context**\
  A Context is a string identifier. It is typically built dynamically using a Handlebars template that has access to the
  request model. The combination of a Key in a Context identifies a unique State Value. Contexts are all scoped to a
  Mock API, so no State Value can be retrieved in a different Mock API.
* **Request Matcher**\
  When using Dynamic State, a Request Matcher is part of a stub's definition that uses a State Value to decide
  whether the current stub matches. Matching occurs **before** State Operations and Variable Definitions are evaluated,
  and operations and definitions are only evaluated if the stub matches.
* **State Operation**\
  A State Operation is a part of a stub's definition that mutates a State Value - either by setting it or deleting it.
  It requires a Key and a Context to identify the Value. A `SET` operation uses a Handlebars template that has access to
  the request model and the `previousValue` (`null` if not present in that Context) of the State Value in order to emit
  the new State Value.
* **Variable Definition**\
  A Variable Definition is a part of a stub's definition that defines a Variable and its value for the rest of the
  stub serve event's lifecycle. It uses a Handlebars template that has access to the request model to emit the value of
  the Variable.

When a stub matches, and its configuration contains multiple State Operations and / or Variable Definitions, they are
applied **in order**. The result of a State Operation / Variable Definition is visible in the Handlebars model available
to subsequent State Operations and Variable Definitions, and when rendering the response body and any webhook request
bodies.

## Usage

### Setting & rendering simple state

In a stub's request definition, change the method to `POST` and the path to `/setAnItemName`.

Open the "State" section and toggle on "Dynamic state":

<img alt="Enable Dynamic state" />

Under "State operations", click "Add operation":

<img alt="Add operation button" />

For now, leave the Context as "Default context" and the Operation as `SET`. Add a Key called `itemName` with a value of
"Socks":

<img alt="Set dynamic state example" />

Under Response, check "Enable dynamic response templating" and put the following in the body text area:

```handlebars theme={null}
State itemName was set to {{ state 'itemName' }}
```

<img alt="Set dynamic state example" />

Try making a `POST` to `/setAnItemName` - you should get a response with a body "State itemName was set to Socks".

You can now use the Handlebars helper `{{ state 'itemName' }}` in the Response body of any stub to return the state
value currently associated with the `itemName` key in the default context. For instance if you add a new stub for
`GET /someItemName`, check "Enable dynamic response templating" and put the following in the body
text area:

```handlebars theme={null}
The current itemName is {{ state 'itemName' }}
```

then subsequent requests for that stub will return "The current itemName is Socks"

### Setting state dynamically

The "Value" field on a `SET` State operation supports Handlebars templating in order to dynamically set the value based
on the contents of an incoming request. The model available in the template is [the same request data model that is provided in the response template](/response-templating/basics/#the-data-model),
along with a `previousValue` containing the value of the Key in this Context before the operation was run, or `null` if
it had no value.

For example, we could change the "Value" in the example above to `{{ request.body }}`. Now the
`itemName` state key in the default context will be associated with the request body that was last sent as a `POST` to
`/setAnItemName`. For instance a `POST` to `/setAnItemName` with body "Shoes" will return "State itemName was set to
Shoes", and a subsequent `GET` to `/someItemName` will then return "The current itemName is Shoes".

While state values are stored as strings, it is normally convenient to make those strings valid JSON and use
[WireMock Cloud's rich set of JSON helpers](/response-templating/json) to manipulate those values using the template
in the "Value" field.

### Setting state in a context

When a value is assigned to a key, this value is confined to a particular context. That context can be defaulted for an
entire Mock API, and unless changed it is effectively a global context. When you render a value in a template using
`{{ state '<key>' }}` you will be rendering the value from the Mock API's default context.

You can specify an explicit context both when setting state and when rendering it.

#### Setting state in an explicit context

When you define a State operation you can click in the "Context" field and enter a template. The model available in the
template is once again [the same request data model that is provided in the response template](/response-templating/basics/#the-data-model).

For instance you could set it to:

```handlebars theme={null}
{{ request.headers.x-test-id }}
```

Now a `POST` to `/setAnItemName` with a body of "Shirts" and a header `x-test-id: 1`, and a `POST` to `/setAnItemName` with a body
of "Trousers" and a header `x-test-id: 2` will set `itemName` to "Shirts" in the context called "1" and to "Trousers" in
the context called "2".

#### Rendering a state value from an explicit context

There are two ways to render state from an explicit context:

Inline:

```handlebars theme={null}
The current itemName is {{ state 'itemName' context=request.headers.x-test-id }}
```

Here we pass the context as a parameter to the `state` helper. You can see it can be a template, allowing you to set the
context dynamically on render just as you could set it dynamically when making a State operation.

Block:

```handlebars theme={null}
{{#stateContext request.headers.x-test-id}}
The current itemName is {{ state 'itemName' }}
{{/stateContext}}
```

Here all `state` helpers within the `stateContext` block are evaluated with the context specified in that block, saving
unnecessary repetition.

#### Rendering all state values within a context

It is possible to access all values within a given context using the `listState` helper.

Template:

```handlebars theme={null}
{{ listState request.headers.x-test-id }}
```

Example result:

```
[my-value-1, a second value, third-value]
```

The `listState` helper returns a collection containing every state value within the provided context. In the case above,
the context to list items from is `request.headers.x-test-id`, which will resolve to the request's `x-test-id` header.

### Setting the default context

It is common to want all or most state values to have the same dynamic context; for instance you may want all state to
be scoped by a user's current `Authorization` header so that they are isolated from changes made by any other user.
Having to specify `{{request.headers.Authorization}}` as the context of every state SET operation, and wrap every
template that uses state in `{{#stateContext request.headers.Authorization}}{{/stateContext}}` would be tedious.
Consequently WireMock Cloud allows setting a template for the default context

In the Mock API's Settings, find the State section. Here you can set the Default context to e.g.
`{{request.headers.x-test-id}}`. State operations using the Default context will now use that value as the context, and
`{{ state }}` helpers which do not specify a context and are not nested in a `{{#stateContext}}` block will also use that
value as the context.

### Removing state values

A stub can delete a key / value pair from a context. Under "State operations" click "Add operation". Set the "Operation"
to `DELETE`. The "Context" & "Key" fields are the same as for a `SET` operation. Whenever this stub matches it will now
delete the given key from the given context.

### Deleting state contexts

A stub can delete all key / value pairs in a context. Under "State operations" click "Add operation". Set the
"Operation" to `DELETE_CONTEXT`. The "Context" field is the same as for a `SET` or `DELETE` operation. Whenever this
stub matches it will now delete all keys from the given context.

### Matching on state

In addition to setting and deleting state values, a stub can use a state value as part of its matching criteria.

For instance, you may want to define two `GET /someItemName` stubs, the existing one which returns a `200` with the `itemName`
value if it exists, and one which returns a 404 if it does not.

Under "State -> Request matching" click "Add request matcher".

For the `200` stub add a matcher with Key: `itemId` NOT `is absent`.

For the `404` stub add a matcher with Key: `itemId` `is absent`.

### Resetting state

All state for the Mock API (including any Scenarios) can be reset using the "Reset state" button on the Mock API:

<img alt="Reset Dynamic state" />

### State concurrency semantics

A Mock API can receive multiple concurrent requests. These may contain state operations that operate on a
`previousValue`; for instance you might store a `requestCount` state value, and make the SET operation increment it as
so: `{{math previousValue '+' 1}}`. WireMock Cloud guarantees that SET operations on a particular
Key in a particular Context will happen sequentially, so 5 concurrent requests to that stub would increment the
`requestCount` 5 times.

## Limits

You can read more about [plan limits here](./plan-limits/).

## Examples

* [An example of modelling a shopping basket with dynamic state](./basket-example/)


# Dynamic State - Plan Limits
Source: https://docs.wiremock.io/dynamic-state/plan-limits

Limitations of your dynamic state usage.

State values are ephemeral; they are stored in a Least Recently Used cache, and whilst WireMock Cloud makes a best
effort attempt to maintain them no guarantee is made about their survival.

In order to prevent resource exhaustion we apply some limits.

Any state value cannot exceed 100,000 characters.

On Enterprise plans, up to 100,000 values can be defined before the least recently used values start being ejected from
the store.

On other plans with Dynamic State enabled only 100 values are maintained in the store.


# Stateful Mocking and Scenarios
Source: https://docs.wiremock.io/dynamic-state/stateful-scenarios

Return different responses based on a state machine

Some testing activities require that different responses be served for a sequence of identical requests. For instance if you are testing a to-do list application [such as this one](../samples/exploratory-testing-tutorial/) you may wish to start with no to-do list items, post a new item, then see the item appear in the list.

Assuming there is a "list to-do items" API call used to fetch the list, this must be called twice during the above test, returning no items on the first invocation, and the newly added item on the second. Since both of these requests will be identical (same URL, method, request headers), something additional is required for WireMock Cloud to differentiate the first and
second cases.

WireMock Cloud's Scenarios solve this problem by providing finite state machines that can be used as additional stub matching conditions.

They allow more than one definition of an otherwise identical stub with different responses based on the current state of the machine.

## Stateful mocking vs. Scenarios

WireMock Cloud provides scenarios as a way to create advanced, pre-defined testing conditions. Alternatively, you can use our [dynamic states feature](../dynamic-state/overview) for truly stateful mocking that allows you to define operations and context to use in dynamic test sessions concurrently.

## Example

To implement the above case, you would declare that the stub returning the empty list is only matched when the scenario state is "Started",
while the stub returning the list with one item is only matched when the scenario state is "First item added".

Start by creating the empty list stub, which is matched only when the scenario named "To do list" is in the "Started" state:

<img title="Empty to-do list stub" />

Then create a stub to handle posting of the first list item. When triggered this stub will move the scenario state to "First item added":

<img title="To-do list POST stub" />

Finally, create a stub to return the list containing one item, which is matched only when the scenario is in the "First item added" state:

<img title="Single item to-do list stub" />

## Testing

First, make a `GET` request to fetch the list, which should be empty. You should be able to do this any number of times
without the result changing:

```
$ curl http://example.wiremockapi.cloud/todo-items
{
  "items": []
}
```

Now `POST` a new item (it actually doesn't matter what the request body contains, since we didn't specify a body matcher in the stub):

```
$ curl http://example.wiremockapi.cloud/todo-items -X POST
```

This should now have moved the scenario state to "First item added". Getting the list of items again should now return one item:

```
$ curl http://example.wiremockapi.cloud/todo-items
{
  "items": [
    {
      "id": "1",
      "description": "Read all about Scenarios"
    }
  ]
}
```

## Scenario reset

All scenarios can be reset to their "Started" state by clicking Reset.


# Simulating federated GraphQL APIs
Source: https://docs.wiremock.io/graphql/federation

Using mock APIs to create a federated GraphQL API.

GraphQL Federation is an architectural pattern that allows multiple, independently managed GraphQL APIs (called
"subgraphs") to be combined and queried from a single, overarching GraphQL API (called a "supergraph").
WireMock Cloud provides support for GraphQL Federation, allowing your GraphQL mock APIs to be used as subgraphs.

## Usage

To enable GraphQL Federation in your GraphQL mock API, click the Federation toggle on the GraphQL page of your mock API.

<img alt="GraphQL Federation toggle" />

Enabling Federation will add the appropriate federation fields to your GraphQL schema that an Apollo Federation
supergraph requires to make calls to your subgraph.
It also ensures that data returned by [mock data generation stubs](/graphql/overview#configuring-the-default-graphql-stub)
is compliant with the entity queries supplied by the supergraph.

Now that Federation is enabled, you can upload a Federation compliant GraphQL schema to your mock API.
Once your subgraph mock API is ready, point your supergraph at this subgraph and start making requests to the supergraph.
Your supergraph will begin making calls to your subgraph to retrieve the requested data.
To add more subgraph mocks to your supergraph, create multiple GraphQL mock APIs and repeat the above steps in each.

## Usage Example

Below is a simple example showcasing how to set up some GraphQL mock subgraphs in WireMock Cloud, and query them from a
supergraph running on your local machine.

This example uses [Apollo's Rover CLI tool](https://www.apollographql.com/docs/rover) to run a supergraph locally.
If you want to try out this example yourself, ensure that you have Rover installed on your machine.
More information on installing Rover can be found [here](https://www.apollographql.com/docs/rover/getting-started).

First, we need to configure some subgraphs to point our supergraph at.
We'll set up three subgraph mock APIs in WireMock Cloud: a `users` subgraph, a `products` subgraph and a `review`
subgraph.
The schemas for each subgraph are below:

<AccordionGroup>
  <Accordion title="Users">
    ```graphql theme={null}
    extend schema
        @link(url: "https://specs.apollo.dev/federation/v2.0", import: ["@key"])

    type Query {
        user: User
    }

    type User @key(fields: "id") {
        id: ID!
        username: String!
        previousSessions: [ID!]
        loyaltyPoints: Int
    }
    ```
  </Accordion>

  <Accordion title="Products">
    ```graphql theme={null}
    extend schema
        @link(url: "https://specs.apollo.dev/federation/v2.0", import: ["@key"])

    type Query {
        listAllProducts: [Product]
        product(id: ID!): Product
    }

    type Product @key(fields: "id") @key(fields: "upc") {
        id: ID!
        upc: ID!
        title: String
        description: String
    }
    ```
  </Accordion>

  <Accordion title="Reviews">
    ```graphql theme={null}
    extend schema
        @link(url: "https://specs.apollo.dev/federation/v2.0", import: ["@key"])

    type Review @key(fields: "id") {
        id: ID!
        body: String
        user: User
        product: Product
    }

    type Product @key(fields: "upc") {
        upc: ID!
        reviews: [Review!]
    }

    type User @key(fields: "id", resolvable: false) {
        id: ID!
    }
    ```
  </Accordion>
</AccordionGroup>

To configure each subgraph, create a GraphQL mock API in WireMock Cloud, enable GraphQL Federation, and upload the
respective subgraph schema to each.
Make a note of the URL for each of these mock APIs, as we will need these to configure our supergraph.

Next, create a supergraph configuration file on our machine called `supergraph-config.yaml`.
Rover will use this file to run a supergraph that will call our mock subgraphs.
Paste the following config into the file, replacing the `subgraph_url` values with the URLs of your subgraph mock APIs:

```yaml supergraph-config.yaml theme={null}
federation_version: =2.8.1
subgraphs:
  users:
    schema:
      subgraph_url: https://users-federated-graphql.wiremockapi.cloud
  products:
    schema:
      subgraph_url: https://products-federated-graphql.wiremockapi.cloud
  reviews:
    schema:
      subgraph_url: https://reviews-federated-graphql.wiremockapi.cloud
```

In your terminal, run the following command to start up a supergraph:

```shell theme={null}
rover dev --supergraph-config supergraph-config.yaml
```

Once up and running, the terminal should display the address where your supergraph is running (e.g.
`http://localhost:4000`).
Navigate to your supergraph's address in your browser where you'll be greeted with [the Apollo Sandbox](https://www.apollographql.com/docs/apollo-sandbox).
Execute some queries to your supergraph and observe that your subgraph mocks are receiving requests.

To stop your supergraph, enter `Ctrl` + `C` in your terminal window where rover is running.

You have successfully creating a GraphQL Federation supergraph, powered by subgraphs running in WireMock Cloud!
For more information on the concepts of GraphQL Federation and designing subgraph schemas, see [the official GraphQL
documentation](https://graphql.org/learn/federation/),
as well as [the Apollo Federation documentation](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/federation).

If you have feedback or questions on our GraphQL functionality as it evolves, we'd love to hear from you.
Please [get in touch](mailto:support@wiremock.io).


# Simulating GraphQL APIs
Source: https://docs.wiremock.io/graphql/overview

Simulating your GraphQL APIs.

As well as REST, SOAP and gRPC support, WireMock Cloud has native support for mocking your GraphQL APIs.
Out of the box, GraphQL mock APIs will respond with generated mock data for any valid GraphQL queries, and more
fine-grained control over response data can be added with ease.

## Usage

### Creating a GraphQL mock API

To create a GraphQL mock API, select the GraphQL API template on the mock API creation page and give it a name (and
optional custom hostname) of your choosing.

<img alt="GraphQL API template" />

### Uploading a schema

Once your API is created, the first step to take before you can configure your stubs is to upload a GraphQL schema that
describes the operations you want to perform with your mock API.
Navigate to your mock API's GraphQL page and select a schema file from your file system or paste a schema directly into
the schema text field.

<img alt="Uploading a GraphQL schema" />

An example of a very simple GraphQL schema for querying user data is provided below:

```graphql theme={null}
type Query {
    user(id: ID): User
    users: [User]
}

type User {
    id: ID
    name: String
    dob: String
    enabled: Boolean
    loginCount: Int
    hobbies: [String]
}
```

From this page, you can edit your API's schema at any time.

### Querying your mock API

Now that your mock API has a schema to work with, it can automatically respond to any valid GraphQL query it receives
that matches the schema.
The simplest way to start querying your mock API is via the [Apollo Sandbox](https://studio.apollographql.com/sandbox/explorer),
but any spec compliant GraphQL client will work.

To start querying your mock API using [Apollo Sandbox](https://studio.apollographql.com/sandbox/explorer), copy your
mock API's base URL into the sandbox endpoint input.

<img alt="Copying your mock API base URL" />

<img alt="Apollo sandbox endpoint input" />

Once the sandbox is pointing at your mock API, it should pick up the API's schema and present a helpful interface for
constructing queries. Construct a query, either by writing one manually or with the help of the sandbox's documentation
interface, then execute the query. You should see a matching response that contains generated mock data. Executing the
query multiple times should return new data each time.

<img alt="Querying in Apollo Sandbox" />

### Configuring the default GraphQL stub

As we've seen, the default behaviour for a GraphQL mock API is to respond to valid queries with automatically generated
mock data.
This behaviour is defined by a default stub that is added to all GraphQL mock APIs on creation.
You can view this stub on the Stubs page of your mock API.

<img alt="Default mock data stub" />

Out-of-the-box, this stub will attempt to serve any HTTP request the API receives, regardless of HTTP method or path.
The stub expects the request to contain a GraphQL query, either in the request query parameters for `GET` requests, or
the request body for all other request methods.
More detail on the request query format can be found on [the official GraphQL site](https://graphql.org/learn/serving-over-http/#methods).
If the request query is valid and matches [the API's schema](#uploading-a-schema), the stub will respond with a 200
status and a JSON payload with [the standard GraphQL response body format](https://graphql.org/learn/serving-over-http/#body).

If you want more control over the format of the data that this default stub generates, there are a few configuration
options available for GraphQL's built-in types.

<img alt="Configuring mock data generation" />

String and ID values can be configured to always return a fixed value, values with a minimum and/or maximum length, or
values that match a given regular expression pattern, such as `[A-F0-9]+` (a string of one or more random characters
between `A` and `F` or `0` and `9`) or `(enabled|disabled)` (either `enabled` or `disabled`).

Int and float values can be configured to only return values above a minimum and/or below a maximum.
An additional option is available for floats that sets the scale of all float values (i.e. the number of digits to the
right of the decimal point). For example, in the number `123.45`, the scale is `2`. The default scale is `2`.

Boolean values can be fixed to always return `true` or always return `false`.

Lists can be configured to always return a fixed amount of items. The default is `3`.

### Configuring custom GraphQL stubs

The default GraphQL stub is a great starting point for configuring your mock API, but often we want more control over
the data our mock API returns for a given query.
That's where creating and configuring our own stubs comes in.
Custom stubs allow your mock API to match on specific GraphQL queries and return static or dynamic responses to those
requests.

To match on a specific query, enter a valid GraphQL query into the `Match query` field of your stub.
When matching, the GraphQL query matcher retrieves a request's query (either from the query parameters for `GET`
requests, or from the request body for other request methods) and check if it is [*semantically* similar](#semantic-query-matching)
to the expected query.
If it is, this will be considered a match.

To return a specific response body, enter this into the `Response body` field as usual.
If you want to return a valid GraphQL response body in JSON format, you'll need to specify the full JSON, including
the root fields (i.e. `"data"`, `"errors"`, `"extensions"`), [as outlined in the GraphQL official documentation](https://graphql.org/learn/serving-over-http/#body).
[Dynamic response templating](/response-templating) is available for GraphQL stubs, like all other API types.

<img alt="Customizing your stub" />

### Converting request logs to stubs

The simplest way to create a stub with some pre-configured data is to navigate to an existing request in your mock
API's Request Log and click the `Convert to stub` button at the bottom of the page.

<img alt="Convert to stub button" />

This will create a new stub in your mock API with a query matcher containing the same query that was sent in the
original request, as well as a response body that matches the one returned to that request.

From here, you can customize your stub to suit your needs.

## Semantic query matching

Similar to WireMock Cloud's JSON equality matcher, WireMock Cloud's GraphQL query matcher performs semantic comparison
when checking if a request's query matches the expected query.
This means that the ordering of a query's fields, arguments, etc. is irrelevant.
For example, the two queries below would be considered a semantic match:

```graphql theme={null}
query GetPosts { posts(limit: 20, offset: 60) { id name } }
```

```graphql theme={null}
query GetPosts { posts(offset: 60, limit: 20) { name id } }
```

### Ignoring unused definitions

Additionally, schema definitions (SDL) and unused operations are ignored when comparing two queries.
For example, consider the two queries below:

```graphql theme={null}
query GetUser { user(id: 123) { id } }

type User { id: ID }
```

```graphql theme={null}
query GetUser { user(id: 123) { id } }

query GetUsers { users { id username } }

union StringOrBool = String | Boolean

schema { query: Query }
```

When these two queries are compared, the SDL definitions (i.e. `type User`, `union StringOrBool` and `schema`) will
always be ignored.
As for the queries, only the query operation that was specified in the request will be compared.
If the supplied operation name for the request was `GetUser`, the two queries would be considered a match, as the only
part being compared would be

```graphql theme={null}
query GetUser { user(id: 123) { id } }
```

However, if the supplied operation name was `GetUsers`, the two queries would not be considered a match, as the first
query does not even contain an operation with that name.

### Variable resolution

When a request uses variables in its query, these variables are resolved *before* matching is performed.
This means that the names of variables and their definitions are irrelevant when matching.
Only their resolved values, supplied in the request, are relevant.
For example, consider the following queries:

```graphql theme={null}
query GetUser { user(id: 123) { id } }
```

```graphql theme={null}
query GetUser($userId: ID) { user(id: $userId) { id } }
```

When comparing these two queries, the variable definition (`$userId: ID`) will be removed, and all references to this
variable (e.g. `id: $userId`) will be replaced with the value of `$userId` supplied by the request.
So, if the request's variables looked like

```json theme={null}
{ "userId": 123 }
```

then the second query defined above would resolve to

```graphql theme={null}
query GetUser { user(id: 123) { id } }
```

which is identical to the first query, so would be considered a match.

Note that variable resolution is performed on both the expected query and the request query.
Therefore, it's possible to specify that a particular value in a query is irrelevant by using a variable reference for
that value in both the expected query and request query.
For example, the following query will always match itself, regardless of what the `$userId` variable resolves to.

```graphql theme={null}
query GetUser($userId: ID) { user(id: $userId) { id } }
```

Variable defaults (e.g. `$userId: ID = 321`) will be used if no variable is supplied in the request.
If a variable is defined in the query, but is not supplied by the request and does not have a default value, the
variable's value will resolve to `null`.

## GraphQL Validation

Validation settings can be used to ensure that requests made to your mock API and responses returned by your mock API
are compliant with your GraphQL schema, as well as [the GraphQL specification](https://spec.graphql.org/draft/).
Settings for GraphQL validation can be found on the GraphQL page of your mock API.
There are three options for GraphQL validation: no validation (the default), soft validation, and hard validation.

<img />

The "No validation" option will have no effect on your mock API.

Enabling soft validation will cause non-compliant requests to contain validation warnings in your mock API's request log.
Any request to the mock API and/or any response returned by the mock API containing data/attributes that do not conform
to the GraphQL spec or the mock API's GraphQL schema will be highlighted on the request log page.
Details of how the request/response was invalid can also be viewed in the request log.

<img alt="GraphQL validation logs" />

Enabling hard validation will cause the same request log behavior as soft validation, with the added functionality of
returning `4xx`/`5xx` error responses containing details of validation issues.

## Current limitations

There are certain features that are not yet supported by GraphQL stubs:

* [Advanced stubbing](/advanced-stubbing)
* [Webhooks](/webhooks)
* [Chaos testing](/chaos)
* [Response delays](/delays)
* [Proxying requests](/proxying)
* [API rate limits](/user-rate-limits)

As well as additional GraphQL specific matchers and template helpers.

If you have feedback or questions on our GraphQL functionality as it evolves, we'd love to hear from you.
Please [get in touch](mailto:support@wiremock.io).


# Simulating gRPC services
Source: https://docs.wiremock.io/grpc/overview

Simulating your gRPC APIs.

WireMock Cloud enables you to mock your gRPC APIs in a similar fashion to a general HTTP/HTTPS mock API.
Incoming gRPC messages are converted to JSON for the purpose of request matching and templating.
JSON responses are also converted to gRPC messages before being sent to the client.

## Usage

### Creating a gRPC mock API

To create a gRPC mock API, select the gRPC API template on the mock API creation page and give it a name (and optional
custom hostname) of your choosing.

<img alt="gRPC API template" />

### Uploading a descriptor set file

Once your API is created, the first step to take before you can configure your stubs is to upload a gRPC descriptor set
file that describes your gRPC services, methods and messages.
Navigate to your mock API's gRPC page and select a file from your file system to upload.

<img alt="Uploading a gRPC descriptor set file" />

See [generating a descriptor set file](#generating-a-descriptor-set-file) for details of how to obtain a descriptor set.

### Configuring gRPC stubs.

Once you've successfully uploaded your descriptor set file you can create stubs for your gRPC API.
The stub form for a gRPC mock API is similar to a general HTTP/HTTPS mock API with a few key differences.
Firstly, each gRPC stub must be associated with a particular service and method defined in the uploaded descriptor set
file.

<img alt="Selecting a stub's associated gRPC service and method" />

Request matching for gRPC stubs is limited to body matchers.
Additionally, body matchers are constrained to only JSON related matchers (e.g. "equals JSON", "matches JSONPath").

Response statuses can be configured to any valid gRPC status.

<img alt="Selecting a stub's associated gRPC service and method" />

Response bodies must return valid JSON that conforms to the gRPC method's response message.
For example, given a descriptor set file that was generated from the following proto file:

```protobuf theme={null}
syntax = "proto3";

service BookingService {
  rpc booking(BookingRequest) returns (BookingResponse);
}

message BookingRequest {
  string id = 1;
}

message BookingResponse {
  string id = 1;
  string created = 2;
  repeated Participant participants = 3;
}

message Participant {
  string name = 1;
}
```

The stub response body for the `booking` method would look something like the following:

```json theme={null}
{
  "id": "123",
  "created": "2024-08-13T10:12:00",
  "participants": [
    {
      "name": "Bob"
    },
    {
      "name": "Alice"
    }
  ]
}
```

When the response status of your stub is set to a non `OK` status, the response body is not used and a `Status Reason`
must be provided.

An example response body is generated for your stub after selecting the service and method, to help guide the shape of
your responses.
An example request body is also generated for JSON equality body matchers that you add to your stub.

### Testing your stubs

Like with traditional mock APIs, gRPC mock APIs come with a test requester built into the WireMock Cloud app.
This test requester can be used to make real gRPC requests to your mock API via a simple interface.

To use the test requester, make sure to navigate to the gRPC mock API you wish to test in WireMock Cloud, then open the
Test Requester tab on the right side of your browser window.
Select the service and method that you want to make a request to, add any headers you want to include and supply a
request body, if desired.

<img alt="Using the gRPC test requester" />

After clicking "Send" to perform the request, the response will be displayed, including the status and body.
You will also be able to view this request in your mock API's request log page.

A handy "Copy gRPCurl command" button is also provided by the test requester that allows you to make a similar request
using the popular [gRPCurl CLI tool](https://github.com/fullstorydev/grpcurl).
Clicking this button will copy a gRPCurl command to your clipboard that you can then paste into your favourite terminal
to execute (provided you have gRPCurl installed).

## Generating a descriptor set file

To generate a descriptor set file from your proto file, simply add the `--descriptor_set_out` option to your protoc
command.
For example,

```bash theme={null}
protoc --descriptor_set_out my-api.dsc MyApi.proto
```


# Support for WireMock OSS
Source: https://docs.wiremock.io/ide-integrations/jetbrains/oss-features

Features supporting the OSS (non-WireMock Cloud) side of WireMock

## Create WireMock stubs

### Create basic WireMock stub from scratch

If a JSON file is placed in the **mappings** folder or contains the `"mappings"` key, the plugin recognizes it as a WireMock stub file and provides appropriate coding assistance.

1. In the **Project** tool window, right-click a folder (or press <kbd>⌘Сmd</kbd><kbd>N</kbd> or <kbd>Alt</kbd><kbd>Insert</kbd>) and select **New | File**.
2. In the **New File** dialog that opens, enter a name of the file. For example, you can enter `mappings/my-stub.json`, and the plugin will create the **mappings** folder and place the new file within it.
3. Start typing a key to get suggestions for applicable keys and their quick documentation.

<img alt="WireMock Coding Assistance" />

### Create WireMock stubs from Endpoints tool window

1. Open the **Endpoints** tool window (**View | Tool Windows | Endpoints**).
2. Right-click an endpoint and select **Generate WireMock Stubs**.

<img alt="Creating WireMock stub from Endpoints" />

The new stub file is saved as a [scratch](https://www.jetbrains.com/help/idea/scratches.html) under **Scratches and Consoles | WireMock Stubs**.

### Create WireMock stubs from OpenAPI specification

1. Open an OpenAPI specification file.
2. Click <img /> and select **Generate WireMock Stubs**.

<img alt="Creating WireMock stub from OpenAPI Specs" />

The new stub file is saved as a [scratch](https://www.jetbrains.com/help/idea/scratches.html) under **Scratches and Consoles | WireMock Stubs**.

## Run WireMock server

1. Open your stub file.
2. Click <img alt="Run WireMock" /> in the upper-right part of the editor.

<img alt="Run WireMock server" />

This will start the WireMock server, and you can see it running in the **Services** tool window (**View | Tool Windows | Services** or press <kbd>⌘Сmd</kbd><kbd>8</kbd> or <kbd>Alt</kbd><kbd>8</kbd>).

<img alt="A running WireMock server in the Services tool window" />

To customize how IntelliJ IDEA starts the WireMock server, you can [modify the WireMock run configuration](#wiremock-run-configuration) or create a new one.

## Send HTTP requests

Use the IntelliJ IDEA [HTTP Client](https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html) to send HTTP request to the WireMock server and preview responses.

1. [Run your WireMock server.](#run-wiremock-server)
2. Open your stub JSON file.
3. Place the caret at your endpoint URL, press <kbd>⌥Option</kbd><kbd>↩Enter</kbd> or <kbd>Alt</kbd><kbd>↩Enter</kbd> (**Show Context Actions**), and select **Generate request in HTTP Client**.

You can view the stub response in the **Services** tool window.

<img alt="WireMock send HTTP request" />

## Enable support for Handlebars templates

IntelliJ IDEA provides coding assistance for templating language used in WireMock response templates. To use this feature, you need the [Handlebars/Mustache](https://plugins.jetbrains.com/plugin/6884-handlebars-mustache) plugin to be installed and enabled.

1. Open your stub JSON file.
2. In the upper-right part of the editor, click <img /> (**Use Handlebars Templates**). If the [Handlebars/Mustache](https://plugins.jetbrains.com/plugin/6884-handlebars-mustache) plugin is not installed, the action will install it.

This will make IntelliJ IDEA treat JSON files placed in the `__files` directory as response templates and provide appropriate Handlebars coding assistance including completion for [Handlebars helpers](https://wiremock.org/docs/response-templating/#handlebars-helpers).

<img alt="Enable support for Handlebars templates" />

## WireMock run configuration

<Info>Create: Run | Edit Configurations | + | WireMock</Info>

IntelliJ IDEA comes with a dedicated **WireMock** run configuration, which allows you to customize how to start the WireMock server.

<img alt="WireMock run configuration" />

### Main parameters

* **Name**: Specify a name for the run configuration.
* **Stubs file**: Location of the JSON file with WireMock stubs to run.
* **Server port**: HTTP port number for the WireMock server. Enter `0` to dynamically determine a port.

### Modify options

* **Verbose output**: Turn on verbose logging to stdout (equivalent for the `--verbose` option).
* **Enable global Handlebars templating**: Render all response definitions using Handlebars templates by passing the `--global-response-templating` [WireMock command line option](https://wiremock.org/docs/standalone/java-jar/#command-line-options).
* **JRE**: Select a JRE if you wish to run WireMock in a different runtime environment than JBR.

### Logs

Specify which log files generated while running the application should be displayed in the console on the dedicated tabs of the [Run](https://www.jetbrains.com/help/idea/2025.3/run-tool-window.html) tool window.

### Before launch

Select tasks to be performed before starting the selected run/debug configuration.


# Integration with WireMock Cloud
Source: https://docs.wiremock.io/ide-integrations/jetbrains/wiremock-cloud-integration

Log in to your WireMock Cloud account in the IDE and create mock APIs from your local files

This IDE plugin provides support for various WireMock OSS features as well as integration with WireMock Cloud.

## Install the WireMock plugin

The plugin is available on the [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/23695-wiremock).

1. Press <kbd>⌘Сmd</kbd><kbd>,</kbd> on Mac or <kbd>Ctrl</kbd><kbd>Alt</kbd><kbd>S</kbd> on other platforms to open settings and then select **Plugins**.
2. Open the **Marketplace** tab, find the *WireMock* plugin, and click **Install** (restart the IDE if prompted).

## Setup

The WireMock plugin comes with features that utilize users' existing WireMock Cloud accounts and integrates local
files with them, e.g. creating remote mock APIs from local stub mappings.

So, if you have a WireMock Cloud account and want to connect to it and use Cloud specific features, head to the plugin settings
at **Settings | Tools | WireMock** and log in to your account.

Otherwise, no specific setup is required.

## Log in to WireMock Cloud

When WireMock is first installed, it is necessary to log in to your WireMock Cloud account, in order to be able to use related features.

Logging in can happen at two different locations: via an editor notification after opening stub mappings files, or from the plugin's settings UI.

<Note>
  Credentials are stored safely by the IDE (on the IDE level), so

  <ul>
    <li>they are completely separate from any WireMock CLI installation on the system,</li>
    <li>and if you are using the plugin in multiple IDEs, you have to log in in each of them.</li>
  </ul>
</Note>

### From the editor notification

Upon opening a stub mapping JSON file, the following notification appears at the top of the editor.
It provides a way to create an account if you haven't already, or to use your existing account.

<img alt="WireMock Cloud editor notification when not logged in" />

To start the login process, click on the **Log in** link. This performs two things:

* shows a balloon popup with your verification code
* opens the login page in your web browser showing you a verification code

In case the page would not open, you can copy the verification URL from the popup.

<img alt="WireMock Cloud authentication confirmation balloon" />

Make sure that the two codes match, then confirm the device code. In a few seconds the IDE will show you another balloon
confirming your login.

### From the plugin settings

You can also log in to your account via the plugin settings at **Settings | Tools | WireMock**.
The flow is similar to the one described in the previous section, but it is handled entirely on the settings UI,
and you also have the option to **Cancel Login**.

<img alt="WireMock Cloud settings not logged in" />

When the login is successful, the UI will show you the email address you are logged in with,
or will notify you if a problem occurred during the login.

#### Use with On-Premise Edition

The plugin also supports work with the on-premise edition of WireMock Cloud. To turn on this feature, enable
the **Use with On-Premise Edition** option, update the necessary configuration values, and log in.

If you are already logged into a different installment of WireMock Cloud, make sure to log out, save the settings,
and log in again.

<img alt="WireMock Cloud settings on-premise" />

## Create mock APIs and import stubs

If you want to convert local stub mappings to remotely hosted WireMock Cloud mock APIs, you can do so: open a stub mapping file,
then click on the **Create mock API** link in the top notification,
or the <img /> icon
in the floating toolbar.

<img alt="WireMock Cloud create mock API options" />

<Note>
  These actions are shown only when you are logged in to a WireMock Cloud account.
</Note>

This will display a dialog (detailed in the sections below) to specify the properties of the new mock API.

Submitting the dialog creates an empty, remote mock API with the specified name and custom hostname, and immediately imports/uploads the
stubs from the open mapping file into that new API.

### Mock API properties and types

When you initiate the mock API creation, you are presented with a dialog to specify the API name, an optional custom hostname
and the type of the API to create.

<img alt="WireMock Cloud create mock API dialog" />

The following API types are supported:

* Unstructured (WireMock)
* REST
* [GraphQL](/graphql/overview) (+ non-federated schema)
* [gRPC](/grpc/overview) (+ descriptor file)

If you choose GraphQL or gRPC you must also upload a schema/descriptor file with them. Creating a mock API without them is not permitted.

<img alt="WireMock Cloud create mock API with GraphQL" />

### Completion of the API creation

The creation of the mock API and data upload into it is performed in two or three separate phases depending on the API type:

* API creation and stub upload for Unstructured and REST,
* API creation, stub upload and schema/descriptor upload for GraphQL and gRPC

Thus, when all phases finish without any issue, a separate balloon notification appears for each phase.
The first one also provides a link with which you can easily open the new API in your browser.

<img alt="WireMock Cloud create mock API with GraphQL" />

If any phase fails for any reason, notifications with appropriate messages will let you know of the failure and the reason of it.

## Import stubs into existing mock APIs

Besides uploading stubs into newly created APIs, you can also upload them into APIs that already exist in your WireMock Cloud account.
You can do so by opening a stub mapping file, then clicking on the
<img /> icon in the floating toolbar.

<img alt="WireMock Cloud import stubs into existing mock API options" />

<Note>
  This action is shown only when you are logged in to a WireMock Cloud account.

  This feature adds the uploaded stubs to the target mock API without deleting existing stubs.
</Note>

In the appearing dialog you can find and select the target API to upload stubs into.

<img alt="WireMock Cloud select mock API dialog" />

### Search

When opening the dialog, it displays all available mock APIs. After that you can perform searches with arbitrary query strings (it is case-insensitive)
either by clicking the <img /> button or by hitting <kbd>Enter</kbd>.

It looks for matches in APIs' names, base URLs and descriptions too. (Showing descriptions is not yet supported.)

If you'd like to reset the results and see all available mock APIs, perform a search with an empty string.

### Mock APIs list

The matching mock APIs are listed in this table with their names, base URLs and types shown.

Each result page shows up to 20 items (that value is not customizable), and the table allows selecting at most 1
mock API as the target. If no API is selected, the dialog cannot be OKed.

On top of initiating the stub import using the **OK** button, double-clicking on a mock API also does the same.

To locate an API easier on the current page, you can use speed search: click somewhere in the table, then start typing.
When there is a match, the first matching row will be selected.

<img alt="WireMock Cloud select mock API speed search" />

### Pagination

This component lets you navigate through the current result set. It supports moving to the **First**, **Previous**, **Next** and **Last** pages when applicable,
as well as to arbitrary pages.

To initiate the navigation to a specific page, specify a valid page number and hit <kbd>Enter</kbd>. If it is initiated with a number

* less than 1, or a non-integer, it will load the first page
* greater than the total number of pages, it will load the last page

In addition, when an invalid page number is entered, the field displays an appropriate message, for example:

<img alt="WireMock Cloud select mock API pagination error" />

### Initiating the stub import

When the dialog is OKed, the stub import begins, and the same logic, including handling failure scenarios,
is performed as when uploading stubs via the [Create mock APIs and import stubs](#create-mock-apis-and-import-stubs) feature.


# Import & Export - Via the API
Source: https://docs.wiremock.io/import-export/api

Automating import and export of mock API stubs via WireMock Cloud's API.

A mock API's stubs can be exported in bulk via the admin API. This can be useful for backing
up your API to source control, or cloning the contents of one API into another.

## Importing

To import any of the supported formats (Swagger, OpenAPI, WireMock Cloud WireMock JSON),
execute a `POST` request to the stub import URL e.g.:

```bash theme={null}
curl -v \
  --data-binary @my-swagger-spec.yaml \
  -H 'Authorization:Token my-api-token' \
  https://my-api.wiremockapi.cloud/__admin/ext/imports
```

More detail can be found in our [API reference](../api-reference/imports/import-into-a-mock-api).

## Exporting in WireMock Cloud/WireMock JSON format

To export an API's stubs, execute a `GET` request to the stub mappings admin URL e.g.:

```bash theme={null}
curl --output my-stubs.json \
  -H 'Authorization:Token my-api-token' \
  https://my-api.wiremockapi.cloud/__admin/mappings
```

You can find your API token at [https://app.wiremock.cloud/account/security](https://app.wiremock.cloud/account/security).


# Importing Via HAR
Source: https://docs.wiremock.io/import-export/har

Importing HAR logs into WireMock Cloud.

HAR is a widely-used, JSON-based HTTP log format. It can be generated by a variety of tools and products, including from the Chrome dev tools Network tab.

WireMock Cloud can import your HAR log and convert it into a collection of stubs.

HAR files are imported in exactly the same way as other formats.
See [Import and Export Overview](./) for basic importing instructions via the UI and
[Importing and Export via the API](./api) for directions on automating
imports via WireMock Cloud's API.


# Import & Export - Mountebank
Source: https://docs.wiremock.io/import-export/mountebank

Importing Mountebank stubs into WireMock Cloud.

Mountebank is an open source service virtualization tool, and WireMock Cloud supports
importing your Mountebank stubs and converting them into a collection of WireMock stubs.

Mountebank files are imported in exactly the same way as other formats.
See [Import and Export Overview](./) for basic importing instructions via the UI and
[Importing and Export via the API](./api) for directions on automating
imports via WireMock Cloud's API.


# Import & Export - Overview
Source: https://docs.wiremock.io/import-export/overview

Importing and exporting mock API stubs in Swagger, OpenAPI and WireMock Cloud/WireMock format.

You can import your [Mountebank stubs](../import-export/mountebank), [Har log](../import-export/har),
[Swagger](/openAPI/swagger/) and [OpenAPI](/openAPI/swagger/) specifications and [Postman](../import-export/postman)
collections into WireMock Cloud in order to auto-generate stubs in your mock API. Swagger 2.x and OpenAPI 3.x are supported,
in both JSON and YAML format.

You can also import and export stubs in [WireMock](../import-export/wiremock/) JSON format. This can be used to move projects between WireMock and WireMock Cloud, store your mock APIs in source control and make copies of WireMock Cloud APIs.

## Importing - basics

To import from any of the supported formats, navigate to the Stubs page of the
mock API you'd like to import into, then click the Import button.

<img alt="Import button" />

Then either paste the content to be imported:

<img alt="Import text" />

Or upload it as a file:

<img alt="Import file" />

The WireMock JSON format is also WireMock Cloud's native format, so when a file of this type is imported,
the stubs created correspond exactly to the file contents.

However, when importing from Swagger and OpenAPI, stubs are generated according to
a set of conversion rules. These can be [tweaked and customised in a number of ways](/openAPI/swagger#customising-the-import).

You can also automate imports via [WireMock Cloud's API](../import-export/api).

## Exporting

To export the current mock API's stubs in WireMock Cloud/WireMock JSON format, click the Export button:

<img alt="Export button" />

Then click the download link:

<img alt="Export dialog" />


# Import & Export - Postman
Source: https://docs.wiremock.io/import-export/postman

Importing Postman collections into WireMock Cloud.

<img alt="Postman" />

Postman is one of the most widely used tools for testing HTTP services, and its
collection format has become a de-facto standard for representing request and response examples.

WireMock Cloud can import your Postman collection and convert it into a collection of stubs.

Postman files are imported in exactly the same way as other formats.
See [Import and Export Overview](./) for basic importing instructions via the UI and
[Importing and Export via the API](./api) for directions on automating
imports via WireMock Cloud's API.


# Import & Export - WireMock
Source: https://docs.wiremock.io/import-export/wiremock

Importing and exporting mock APIs between WireMock and WireMock Cloud.

WireMock Cloud and WireMock OSS share the same native JSON format for stubs, so mock APIs
can be imported and exported between the two.

JSON exports can also be stored in source control, and used to clone or move stubs
between WireMock Cloud APIs.

## Importing a mock API into WireMock Cloud from WireMock

Assuming you're running a WireMock instance on port 8080, you can export all the
stubs currently defined via the admin API:

```
curl --output example-stubs.json http://localhost:8080/__admin/mappings
```

Then to import into WireMock Cloud, open the Import dialog and drop or upload the `example-stubs.json`:

<img alt="Import file" />

<Note>A current limitation of this approach is that response bodies represented as files under the `__files` directory will not be imported. See how this can be worked around by [uploading a WireMock project folder](#uploading-a-wiremock-folder) and via the [WireMock Java API](#pushing-stubs-to-wiremock-cloud-using-wiremocks-java-api).</Note>

## Importing a mock API into WireMock from WireMock Cloud

First, export the stubs via the Export dialog in the Stubs page:

<img alt="Export dialog" />

Then call the WireMock import API with the file you downloaded:

```
curl -v -d @example-stubs.json http://localhost:8080/__admin/mappings/import
```

Alternatively you can copy `example-stubs.json` into the `mappings` directory
under your WireMock root and either restart WireMock or make a `POST` request to the
reset API:

```
curl -v -X POST http://localhost:8080/__admin/mappings/reset
```

<Note>If any of your stubs make use of **response templating** then you'll need to ensure WireMock is started with the `--local-response-templating` CLI parameter or [Java equivalent](https://wiremock.org/docs/response-templating/).</Note>

<Note>It is not currently possible to import stubs that use the JWT and JWKS template helpers into WireMock.</Note>

## Uploading a WireMock folder

If you have a WireMock project that consists of individual JSON stub mapping
files under the `mappings` directory that refer to response body files under `__files`
you can import this by dragging and dropping the project folder into the dialog.
Unlike the method involving a single JSON file described above, this will cause the
response bodies under `__files` to be inlined.

<img alt="Import file" />

## Pushing stubs to WireMock Cloud using WireMock's Java API

Another way to import a WireMock project that has a `__files` directory is to push it using WireMock's Java API.
This method also inlines response bodies before sending them to WireMock Cloud:

```java theme={null}
WireMock wireMock = WireMock.create()
    .scheme("https")
    // The domain name of the mock API you wish to import into
    .host("my-api.wiremockapi.cloud")
    .port(443)
    // API token from https://app.wiremock.cloud/account/security
    .authenticator(new ClientTokenAuthenticator("mytokenabc123"))
    .build();

// The root directory of the WireMock project, under which the mappings and __files directories should be found
wireMock.loadMappingsFrom("/wiremock");
```


# Mock APIs
Source: https://docs.wiremock.io/mock-apis

Creating, updating, deleting and permissioning mock APIs via the API.

## Creating and permissioning a new mock API

Follow these steps to create a mock API then grant a single user permission to use it:

<Steps>
  <Step title="Create a new mock API">
    Start by calling the [create new mock API](/api-reference/mock-apis/create-a-new-mock-api) endpoint, specifying
    the name, type and hostname of the API.

    The type can be left blank for an unstructured, or it can be `grpc` or `openapi`.

    The hostname is the friendly unqualified domain name used in the base URL. It is optional, and if omitted the
    generated ID for the mock API will be used in the domain name.

    Save the mock API's ID from the response.
  </Step>

  <Step title="Get the ACL candidates">
    Follow the `mockApi.links.acl` link in the response gained in the previous step, which will return
    [ACL candidates](/api-reference/access-control/get-acl-candidates).

    From within the returned data, find the user to whom you wish to grant access to the mock API and follow the link to the user resource.
    Save the user's ID.
  </Step>

  <Step title="Grant access to the user">
    Call [update an entity's ACL](/api-reference/access-control/update-an-entitys-acl), setting the following parameters:

    `entityCollection` = `mock-apis`

    `entityId` = \<the mock API ID>

    `subjectType` = `user`

    `subjectEntityId` = \<the user's ID>

    The body must contain the role to be granted e.g. `mock_api_editor`.
  </Step>
</Steps>

Similar steps can be taken when adding a team rather than a single user to the permissions.


# OpenAPI Mocking and Prototyping
Source: https://docs.wiremock.io/openAPI/openapi

Overview of the OpenAPI mock API type and two-way mock generation

WireMock Cloud supports an OpenAPI mock API type that provides both incremental generation of stubs from OpenAPI and OpenAPI generation from stubs. Mock APIs of this type also have an associated auto-generated set of public documentation pages.

This supports two types of workflow:

1. Automatic generation/amendment of a mock API from an existing OpenAPI doc as it evolves,
2. API prototyping - defining API behaviour via stubs and auto-generating OpenAPI + documentation.

These workflows can be combined i.e. when prototyping new behaviour for an existing API.

## Getting started

From the app's home screen, create a new mock API and choose the OpenAPI type:

<img alt="New mock API type picker" />

When the new mock API is created an extra item will be present on the left-hand nav bar, taking you to the OpenAPI editor page:

<img alt="OpenAPI editor navigation item" />

Navigating to the Settings tab on the same page, toggling on "Enable public API documentation" and clicking the link underneath will show the public API documentation (which will be initially empty apart from header information since there are no paths defined in the OpenAPI doc).

<img alt="Public API documentation settings" />

## Generating stubs from OpenAPI

Stubs will be created or updated whenever changes are saved to the OpenAPI doc.

Add a new path entry and click Save:

<img alt="Add customer path to OpenAPI" />

Then navigate to the Stubs page and see that two new stubs have been created - one with specific request parameters required and one "default" i.e. will match regardless of specific parameter values provided the method and URL path are correct.

<img alt="Generated customer stubs" />

Stubs will be generated following the [stub generation rules](#stub-generation-rules).

### Updating an OpenAPI doc

When an OpenAPI doc is updated, for every `path-method-status-contentType`, existing stubs will be updated if any of the following apply:

* The existing stub was generated from an example and the example hasn't changed its name.
* If there is one example within the given `path-method-status-contentType` which shares the response body with the existing stub.
* If the `path-method-status-contentType` only provides a single example.
* If the `path-method-status-contentType` doesn't provide examples at all.

If none of the conditions above are satisfied, one or more stubs will be generated following the [stub generation rules](#stub-generation-rules).

WireMock Cloud takes a non-destructive approach to your stubs.  This means that if you delete a path, method, status
or contentType, the stub that represents that OpenAPI element will remain in your Mock API. This also applies to updating
elements in your OpenAPI.  For example, if you update a path in your OpenAPI from `/orders` to `/v1/orders` the path
will be classed as a new path and a new stub will be created.  The old stub will not be deleted.

If you are modeling new data scenarios and you add new stubs to your Mock API after generating stubs from an OpenAPI
specification, these stubs will not always be updated when you update your OpenAPI specification.  If those new stubs
do not match an example in your OpenAPI specification, they will not be updated when you update your OpenAPI specification
(adding a new parameter for example) and you will need to update those manually.

### Stub generation rules

When updating an OpenAPI doc, the resulting stubs from new OpenAPI elements will be added.
Stub generation will be based on the following rules:

* `304` response:
  * Request header matcher `If-None-Match` with specific value `12345`.
* `422` response:
  * Only one stub will be generated, with a request body matcher not matching the schema or missing.
  * If more than one response example provided, it will pick one randomly as the response body.
  * If no response example provided, the response body will be autogenerated based on the schema.
* `400` response:
  * Only one stub will be generated, with neither request parameters nor body present or matching the schema.
  * If more than one response example provided, it will pick one randomly as the response body.
  * If no response example provided, the response body will be autogenerated based on the schema.
* Any other response status:
  * If no example is provided, it will generate a stub with autogenerated request parameters and response, based on schema.
  * If at least one example is provided:
    * It will generate one stub per example, using specific request parameter matchers and taking the example as the response body.
    * The request parameter matchers will be autogenerated based on the schema, unless the extension `x-parameter-values` is provided (as explained [here](./swagger)), in which case it will be used to generate the expected values of the parameter matchers.

### Controlling generated parameter values in your stubs

If an OpenAPI element has a parameter (header for example) that is set to `required: true` then the stub will be generated
or updated with that parameter. WireMock Cloud adds a value for that parameter to match on.  You can control the value
generated in your stubs using various OpenAPI elements:

If no min or max length are provided in the schema, defaults of a minimum of 3 and a maximum of
200 is used. Therefore, an OpenAPI specification snippet like the following:

```yaml theme={null}
paths:
  /trips/{tripId}:
    delete:
      summary: Cancel a booked trip
      parameters:
        - name: tripId
      in: path
      required: true
```

Could generate a `tripId` equalsTo matcher with the following value - `gtpq1fggnuolb31tya6rrc1tye1am5bkzw5kjxxeyscx9lb3zhla`

Adding a `minLength` and a `maxLength` to the schema will control the size of the random string. The snippet below:

```yaml theme={null}
paths:
  /trips/{tripId}:
    delete:
      summary: Cancel a booked trip
      parameters:
        - name: tripId
      in: path
      required: true
      schema:
        type: string
      maxLength: 5
      minLength: 2
```

Could generate a `tripId` equalsTo matcher with the following value - `aspp`

You can force a value to be used in the matcher by creating an enum with only one value. This is effectively the same as
generating a constant:

```yaml theme={null}
paths:
  /trips/{tripId}:
    delete:
      summary: Cancel a booked trip
      parameters:
        - name: tripId
      in: path
      required: true
      schema:
        type: string
      enum:
        - "1"
```

If an enum is used with multiple values, then a random item from the enum is used in the matcher.

Alternatively, a regex pattern can be used in the schema to further control the value used in the matcher:

```yaml theme={null}
paths:
  /trips/{tripId}:
    delete:
      summary: Cancel a booked trip
      parameters:
        - name: tripId
      in: path
      required: true
      schema:
        type: string
      pattern: "^trip-id-\\d{8}$"
```

Could generate a `tripId` equalsTo matcher with the following value - `trip-id-68975013`.

Optional `minLength` and `maxLength` elements can be used to further control the generated value:

```yaml theme={null}
paths:
  /trips/{tripId}:
    delete:
      summary: Cancel a booked trip
      parameters:
        - name: tripId
      in: path
      required: true
      schema:
        type: string
      pattern: "^trip-id-\\d{8}$"
      maxLength: 9
      minLength: 2
```

Could generate a `tripId` equalsTo matcher with the following value - `trip-id-6`.

#### Default stubs

[//]: # "WARNING: This heading is referenced by the UI. Do not change it without changing the link in the UI."

Optionally, for each path and method in the OpenAPI specification with a response status of 2xx, a "default" stub can also be generated.
This default stub will not contain any specific request parameter matchers, only a request body matcher that matches the request body schema in the OpenAPI specification, if a schema is provided.
To turn on/off the generation of default stubs, go to the Settings tab of the OpenAPI page, where the toggle is located.

<img alt="Generate default stubs toggle" />

## Prototyping - generating OpenAPI from stubs

OpenAPI elements will be generated or updated when stubs are created or changed.

Try creating a stub with a new path template that doesn't yet exist in the OpenAPI document:

<img alt="Stub request with new path template" />

<img alt="Stub response with new path template" />

On save, the path plus operation, responses, schemas and examples will be added to the OpenAPI spec and also to the public documentation.

Automatic generation of OpenAPI to stubs and vice versa can be turned off in the Settings tab of the OpenAPI page.

<img alt="Stub and OpenAPI generation settings" />


# OpenAPI Git Integration
Source: https://docs.wiremock.io/openAPI/openapi-git-integration

Integrating your Git repository with your mock API

WireMock Cloud offers the ability to synchronize your mock API's OpenAPI spec with a Git repository.
This synchronization is bidirectional, allowing you to pull your spec from Git to WireMock Cloud, as well as push
updates from WireMock Cloud to Git.

This enables WireMock Cloud to be integrated into your workflows seamlessly.
Your stubs can be kept up to date without having to manually copy your specification into WireMock Cloud each time it is
updated, and you can prototype your OpenAPI specification in WireMock Cloud before pushing it to your code base.

## Configuring your Git integration

To configure your mock API to synchronize its OpenAPI document with a Git repository, navigate to the Settings tab of
the OpenAPI page.

Toggle "Enable synchronization" in the Git repository settings section.

Fill in the fields with the appropriate Git configuration data, including the SSH address of your Git repository and
the path to the OpenAPI file within the repository.

The key that WireMock Cloud will use to authenticate calls to your Git repository must also be configured here.
You can either select an existing key or create a new one.

You can learn more about keys in WireMock Cloud [here](/security/key-management).

Once you have entered the relevant Git repository configuration, save your changes.

<img alt="OpenAPI Git integration settings" />

The SSH public key for the key you selected will be displayed at the bottom of the configuration.
[Add this key to your Git repository.](#adding-ssh-keys-to-your-git-repository)

When you navigate to the Document tab of the OpenAPI page, there will be buttons for performing Git operations on your
OpenAPI document.

<img alt="OpenAPI Git integration buttons" />

Clicking the Pull button will retrieve the contents of the file at the configured path in your Git repository and save
it in WireMock Cloud.
The document will be validated and stubs generated like normal.
The pulled document will appear in the document text area.
Note, this will not immediately overwrite any local changes you have made to the specification (see
[Git conflicts](#handling-git-conflicts) for details).

Clicking the Push button in the Document tab of the OpenAPI page will push your currently saved OpenAPI document on
WireMock Cloud to the configured Git repository.
If the file does not exist on the configured branch of the Git repository, then it will be created by this action.

If you wish to push to your Git repository, ensure that write access is granted to the SSH key when you add it to your
repository, if required by the platform (e.g. GitHub).

With the Git integration enabled, changes can still be saved to WireMock Cloud's copy of the OpenAPI document
independently of the configured Git repository.
WireMock Cloud and your Git repository are only synchronized when the document is pulled or pushed.

## Handling Git Conflicts

[//]: # "WARNING: This heading is referenced by the UI. Do not change it without changing the link in the UI."

There are circumstances where performing a pull or push will cause conflicts with your mock API's copy of your OpenAPI
specification.
This can occur when a pull is attempted after changes have been applied to your mock API's copy of the specification
that have yet to be pushed to your repository, or when pushing after changes have been made to the file in the
repository since the last time it was pulled into WireMock.

In these cases, attempting a pull or push will display a dialog explaining that your mock API is out of sync with the
repository and ask if you wish to overwrite the document on WireMock (when pulling) or the document in the repository
(when pushing).
If this dialog is cancelled, no changes will occur in WireMock or your repository.

If you are receiving these conflict messages and are unsure of what action to perform, WireMock recommends performing
an overwriting push to the repository, rather than an overwriting pull to your mock API, and resolving any issues using
external Git tooling.
This ensures that no data is lost, since all changes will be logged in version control.

## Testing Connections to Your Git Repository

If you want to test that your Git configuration is correct before attempting a pull or push (or even saving the
configuration), you can use the "Test Connection" button on the settings page.
Simply fill in the configuration fields and press the button.
If WireMock Cloud is able to connect to your Git repository, then a success will be displayed.
Otherwise, a message will be displayed explaining what went wrong.

## Adding SSH Keys to Your Git Repository

[//]: # "WARNING: This heading is referenced by the UI. Do not change it without changing the link in the UI."

In order for WireMock Cloud to be able to communicate with your Git repository, you must add the SSH public key displayed in your mock API's OpenAPI settings to the repository.
The process for adding the public key to your Git repository depends on the method you are using to host your Git
repository.

Below are instructions for adding keys to your repository on popular hosting platforms.
These instructions are up-to-date as of writing, but are subject to changes outside WireMock's control.

### GitHub

If you are hosting a repository on [GitHub](https://github.com), you can add the key to your repository via the "Deploy
keys" page of the repository settings tab.

<img alt="GitHub Deploy Keys Page" />

Make sure to allow the key write access if you want to push to the repository from WireMock Cloud.

<img alt="GitHub Add Deploy Key Page" />

### Bitbucket

If you are hosting a repository on [Bitbucket](https://bitbucket.org), you can add the key to your repository via the
repository's "Access keys" page.

<img alt="Bitbucket Access Keys Page" />

Bitbucket's access keys are limited to read-only access to a repository.
This means pushing from WireMock Cloud is not possible when using access keys.
If write access is required, the key can be added to a user's personal SSH keys.

<img alt="Bitbucket Personal SSH Keys Page" />

This will allow the key write access to all repositories that the user has access to.
Therefore, it may be advisable to create a specific user for WireMock Cloud in your Bitbucket organisation that only has
access to the desired repository.

### Gitlab

If you are hosting a repository on [Gitlab](https://gitlab.com), you can add the key to your repository via the
repository's "Deploy keys" section of the repository settings page.
Make sure to grant the key write permissions if you want to push to the repository from WireMock Cloud.

<img alt="Gitlab Add SSH Key Settings" />

### Self-Hosted Server

If you are hosting a repository on a server that you maintain, adding the key to your repository will generally involve
adding it to the Git user's `.ssh/authorized_keys` file.
For example, if your Git repository address is `git-user@my-git-server.com:path/to/repository.git`, you will likely have
to append the key to the contents of `/home/git-user/.ssh/authorized_keys` on the server that `my-git-server.com`
addresses.
Approaches may vary, so it is best to consult your system administrator.

For security purposes, WireMock recommends creating a specific user for WireMock Cloud on your server with read
permission on the Git repository directory only (and write permission if pushing from WireMock Cloud is desired).


# OpenAPI Validation
Source: https://docs.wiremock.io/openAPI/openapi-validation

Validating mock API requests and responses against OpenAPI

Validation settings can be used to ensure that requests made to your mock API and responses returned by your mock API
are compliant with your OpenAPI specification.
Settings for OpenAPI validation can be found in the Settings tab on the OpenAPI page.
There are three options for OpenAPI validation: no validation (the default), soft validation, and hard validation.

<img />

The "no validation" option will have no effect on your mock API.

Enabling soft validation will cause non-compliant requests to contain validation warnings in your mock API's request log.
Any request to the mock API and/or any response returned by the mock API containing data/attributes that do not conform
to the mock API's OpenAPI document will be highlighted on the request log page.
Details of how the request was invalid can also be viewed in the request log.

<img alt="OpenAPI validation logs" />

Enabling hard validation will cause the same request log behavior as soft validation, with the added functionality of
returning error responses containing details of validation issues to invalid requests.


# Import & Export - Swagger and OpenAPI
Source: https://docs.wiremock.io/openAPI/swagger

Generate your mock API automatically from a Swagger or OpenAPI definition.

Swagger / OpenAPI is undoubtedly the most widely used description language for REST and REST-like APIs. WireMock Cloud supports automatic generation of mock APIs from imported Swagger and OpenAPI specifications.

See [Import and Export Overview](/import-export/overview) for basic importing instructions via the UI and [Importing and Export via the API](../import-export/api) for directions on automating
imports via WireMock Cloud's API.

## Customising the import

When importing from a Swagger/OpenAPI spec, it's often useful to be able to control
how certain aspects of the generated stubs are produced. WireMock Cloud supports a number
of extension attributes that can be added to your spec document for this purpose.

### Specifying URL path and query parameters

When WireMock Cloud converts a response example to a stub, by default it will generate random values for URL path and query parameters.

However, if a response uses the multiple example format, you can specify the exact parameter values you wish to be required
by the stub. This can be useful if your test cases or application under test expects specific
responses to be available in your mock API.

For instance, given the following Open API path element:

```yaml theme={null}
/people/{id}:
    description: People by ID
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: string

    get:
      description: Get a person
      parameters:
        - name: fields
          in: query
          required: true
          schema:
            type: string
            enum:
              - full
              - summary

      responses:
        '200':
          description: People search returned successfully
          content:
            application/json:
              examples:
                one:
                  summary: First example
                  x-parameter-values:
                    id: abc123
                    fields: summary
                  value: |
                    { "name": "John" }

                two:
                  summary: Second example
                  x-parameter-values:
                    id: cba321
                    fields: full
                  value: |
                    { "name": "Jeff", id: "cba123" }
```

Two stubs will be created from the above example.
One will have a URL path equal to `/people/abc123` and a required query parameter of `fields=summary`.
The other will have a URL path equal to `/people/cba321` and a required query parameter of `fields=full`.

Any values not specified in this manner will be randomly generated based on the parameter's schema.

### Controlling data generation from schemas

When importing a response with a schema but no examples, WireMock Cloud will randomly generate an example
that conforms to the schema.

For each schema attribute an attempt will be made to determine the data type, using the
`format` if present, but if not making a guess based on the field name. For instance,
a `string` attribute named `date_of_birth` will result in the generation of an ISO8601 local
date within the past 99 years e.g. `1971-08-02`.

However, you can override this behaviour and specify which data generation strategy should be used.
WireMock Cloud uses [Faker](https://github.com/DiUS/java-faker) to generate example data, and
you can specify the specific faker to use by adding an `x-faker` attribute to your schema element e.g.

```yaml theme={null}
schema:
  type: string
  x-faker: name.first_name
```

This can be used both in parameter declarations and response body schemas.

All of the fakers [listed here](https://github.com/DiUS/java-faker/tree/master/src/main/resources/en)
can be used, plus there are some additional rules supplied by WireMock Cloud. The following lists all of the most commonly used, plus all supplied by WireMock Cloud:

* `name.name`
* `name.first_name`
* `name.last_name`
* `name.name_with_middle`
* `name.title`
* `name.prefix`
* `name.suffix`
* `name.username`
* `id.alphanumeric_id`
* `id.uuid`
* `date_and_time.birthday`
* `date_and_time.past_date_time`
* `date_and_time.future_date_time`
* `uri.url`
* `lorem.word`
* `lorem.sentence`
* `lorem.paragraph`
* `currency.code`
* `address.street_address`
* `address.secondary_address`
* `address.city_name`
* `address.state`
* `address.postcode`
* `country.name`
* `country.code2`
* `country.code3`
* `phone_number.phone_number`
* `avatar.image`

<Note>Only required query parameters will be included in the stubs' request criteria. Non-required query parameters will be excluded, meaning that any or no value will be accepted.</Note>


# Organisation Info and Members
Source: https://docs.wiremock.io/organisation-info-and-members

Getting and updating your organisation information, and managing members

## Finding your organisation ID

<Steps>
  <Step title="Get your own user account">
    Find your org ID on your user account info by calling the [get self](/api-reference/users/get-self),
    ensuring you follow the redirect.
  </Step>

  <Step title="Get the organisation">
    Follow the `organisation` link in the response to get the organisation details.
  </Step>

  <Step title="Read the ID">
    Read the `id` field from the response.
  </Step>
</Steps>

## Updating your organisation name

You can update your organisation's name by calling [update organisation](/api-reference/organisations/update-organisation).

## Removing an organisation member

A user can be completely removed from your organisation by using the
[delete organisation member user](/api-reference/organisations/delete-organisation-member-user) endpoint.

If you need to find the user's ID first you can do so via [get users in an organisation](/api-reference/organisations/get-users-in-an-organisation).

Removing a user from the organisastion won't delete their user account completely but will move them to a new organisation
containing only themselves which is subscribed to the Individual (free) plan.


# Overview of API simulation with WireMock Cloud
Source: https://docs.wiremock.io/overview

Get started with WireMock Cloud.

WireMock Cloud is a platform for rapidly building stateful, high quality simulations of production services that run as easy to use mock APIs.

You can use these simulated services locally, in dev environments and in test environments to replace production API dependencies that slow you down and cost you money.

If you're new to WireMock Cloud or API virtualization, we recommend:

* [Reading our product overview page](https://www.wiremock.io/cloud-overview)
* [Watching the WireMock Cloud Academy on YouTube](https://www.youtube.com/playlist?list=PL4V1b_lhwTrWf10Q0BUepsBqn4fMZ3q4u)
* [Learn about our plans and pricing](https://www.wiremock.io/get-pricing)

WireMock Cloud supports SOAP, REST, OpenAPI, GRPC and GraphQL.

## Platform Overview

WireMock Cloud's platform provides a number of Enterprise-grade features that you can learn more about in the documentation here.

* Easily design, import or record any new virtualized API
* Team management with SSO and RBAC
* Activity logging to monitor service usage
* Use Git as a source of truth for API specs
* Inject fault, Chaos and other forms of rainy day behavior
* Create synthetic test data or import data from a CSV or database

## API Creation

WireMock Cloud provides a number of ways to set up a mock API:

* Manually via the web app
* OpenAPI, Swagger, Postman or HAR import
* Record traffic to and from another API
* Import an existing project from WireMock OSS
* Automate via WireMock's own REST APIs

## Getting Started

### Create Account

To get started, [first create your free account](https://app.wiremock.cloud/login?for=signup). You'll have 30 days of unlimited Enterprise features, after which you'll revert to our forever free plan. [Learn more about our plans and pricing here.](https://www.wiremock.io/get-pricing)

### Creating Your First Simulated API

#### Manually

Creating stubs manually in the web UI is often the simplest way forward if:

* The API you're mocking is quite simple (or you only need a small part of it)
* You're working from a specification document and you want to copy/paste examples into a running simulation
* You just want to quickly explore what WireMock Cloud can do

More details on manual creation can be found in the [Stubbing](./stubbing/) and [Advanced stubbing](./advanced-stubbing/) articles.

#### Swagger and OpenAPI import

If you already have a Swagger or OpenAPI specification, you can import it and WireMock Cloud will auto-generate a set of stubs.

Swaggerhub users can integrate with WireMock Cloud via a webhook, so that the mock API
will be updated each time a change is saved.

See [Swagger Import](/openAPI/swagger/) for details.

#### Record An API

If you want to create a mock of an existing API which is accessible over the internet,
you can configure WireMock Cloud to proxy (forward) traffic to it and record requests as stubs.

See [Recording Stubs](./recording-stubs/) for details.

#### Importing from WireMock OSS

WireMock Cloud uses WireMock OSS as its underlying engine, so mock APIs created within WireMock
can be directly imported into WireMock Cloud (and vice versa).

This can be useful when you need to record APIs that are only accessible inside your
organisation or from a private network, or if you have existing projects utilising
WireMock that you'd like to host in the cloud.

See [import and export](./import-export/) for details.

### Next Steps

After creating your first API, we recommend diving into the [WireMock Cloud Academy](https://www.youtube.com/playlist?list=PL4V1b_lhwTrWf10Q0BUepsBqn4fMZ3q4u) to learn all the possible ways of building and consuming your new mock API.

You can also hit **command+K** to use our AI-powered documentation search and ask any question you want (example: *"How do I add a data source?"*).

You can also [contact us](mailto:support@wiremock.io) anytime you want to ask a question!


# Proxying
Source: https://docs.wiremock.io/proxying

Proxying requests to other systems

When working with an existing API it can be useful to pass some requests through to it for testing, while
serving stubbed responses for others.

For instance, if an API is not yet fully implemented then testing progress can still be made
for the calling application by stubbing the parts not yet completed.

Additionally, proxying all but a selection of requests enables testing of edge and failure cases that would be hard to
replicate predictably in the target API.

## Usage

Proxying is configured per-stub. When a stub is configured to serve a proxy response, all of the normal request matching rules
apply, but instead of returning a canned response, the request is forwarded to the target.

Proxying is enabled by selecting the Proxy tab in the stub's Response section and completing (at a minimum) the base URL field.

Additional request headers can optionally be specified. These will be added to the proxy request if not already present,
or will override the existing value if present.

<img title="Proxy response" />

The relative part of a request's URL will be appended onto the base URL, so given a proxy base URL of `http://my-site.com/base`, a
request made to `http://my-mock-api.wiremockapi.cloud/things/1` would result in a proxy request to `http://my-site.com/base/things/1`.

## Templating the base URL

When the Enable templating check box is ticked, the base URL can be a handlebars template, meaning that properties from the
incoming request can be used to determine the URL. See [Response Templating](/response-templating/basics/) for details of the
model and syntax used.

<img title="Proxy response with templating" />

## Hostname rewriting

Often API responses contain absolute links and other content that refers to the domain name of the API's origin.
When proxying to another API this can be undesirable as the mock API's domain is different from the proxy target and thus a client following such a link would make its next request directly to the proxy target rather than the mock API.

To remedy this issue we can enable hostname rewriting, which will replace any instances of the proxy target's domain name in the response headers or body with the mock API's domain name.

For instance, if we configured a stub in a mock API `https://my-mock-api.wiremockapi.cloud` to with a proxy target of `https://api.github.com` and a proxied response body contained `"self": "https://api.github.com/users/123"`, with hostname rewriting enabled this would be changed to `"self": "https://my-mock-api.wiremockapi.cloud/users/123"`.

<img title="Proxy hostname rewriting" />

## The proxy/intercept pattern

It is often desirable to proxy requests by default while stubbing a few specific cases. This can be achieved using a variation
of the [Default Responses](./default-responses/) approach.

In summary, the proxy stub is created to be the default, with broad request matching criteria and a low priority value. Then
individual stubs are created at higher priorities with specific request URLs, bodies or anything else distinguishing.

Examples of things these specific stubs can be used for are:

* Return an HTTP 503 response
* Return response data in a format not expected by your app's client
* Close the connection prematurely without sending a response (see [Simulating Faults](./simulating-faults/))


# Recording via the Cloud
Source: https://docs.wiremock.io/recording-stubs

Creating new stubs by recording traffic to another API

If the API you're mocking already exists you can speed up the process of stubbing responses using WireMock Cloud's record feature.
This essentially involves telling WireMock Cloud to act as a proxy to the target API then directing some HTTP requests to WireMock Cloud
representing the resources you'd like to stub.

## A simple recording example

Once you have logged into WireMock Cloud and created a mock API, navigate to the Stubs page.

Then hit the Record button, enter `http://ip-api.com` as the target URL and hit Start.

<img title="Record dialog" />

Now make a request to your mock API (substituting `my-mock-api` for your own sub domain name):

```bash theme={null}
$ curl -v http://my-mock-api.wiremockapi.cloud/json
```

This request will be proxied through WireMock Cloud, so that a `GET` request will be made to `http://ip-api.com/json` and the result captured.

Now hit Stop, and you should see that an extra stub has been added to the list.

## Request matching rules when recording

When a request with no body is received during recording, the recorder will create a stub matched on HTTP method and URL only.

When a request with a body is received a body pattern is also included. If the request body is a valid JSON document,
then the `equalToJson` operator will be used. If XML, the `equalToXml` operator will be used. Otherwise the operator will be `equalTo` i.e. simple string equality.

## Recording from Private Endpoints

For obvious reasons, WireMock Cloud cannot record by proxying to an endpoint that is not accessible via the internet.
Nor can it record from an endpoint that requires authentication via mutual TLS. However, this can be achieved using
the WireMock CLI. See [Recording using the WireMock CLI](/cli/recording/).


# Request Matching – Expression Matcher
Source: https://docs.wiremock.io/request-matching/expression-matcher

Advanced expression-based matching

The Expression Matcher allows you to define complex request matching logic using
Handlebars templates. This feature enables matching scenarios that go beyond what
standard matchers can achieve.

<Note>
  The Expression Matcher is an Enterprise only feature. Accounts on the free and trial
  plan do not have access to this feature. If you are on the free or trial plans and would
  like access to this feature, [contact the WireMock team today](https://www.wiremock.io/contact-now)
  to discuss an enterprise plan for your organisation.
</Note>

## How It Works

The Expression Matcher evaluates a Handlebars template that must return the string
`true` for the request to match. If the template evaluates to anything other than `true`
then the stub won't match. You have access to the full `request` object within the
template, for example:

* `request.body` - the request body as a string
* `request.query.<paramName>.[0]` - query parameter values (as arrays)
* `request.headers.<headerName>` - header values
* `request.method` - the HTTP method
* `request.path` - the request path

The expression matcher can be found in the **Advanced Matching** section of the stub
editor.  Unlike the other matchers, only one expression matcher can be defined per stub:

<img alt="Expression Matcher in the stub editor" />

## When to Use The Expression Matcher

**Prefer standard matchers when possible.** WireMock's built-in matchers (equality,
regex, JSON path, etc.) are optimized for their specific tasks and should be your
first choice. Use the Expression Matcher when you need:

* **Comparative logic** – comparing values from different parts of the request
* **OR conditions** - matching when any one of several conditions is true
* **Complex boolean logic** – combining multiple conditions with AND/OR/NOT
* **Cross-field validation** – validating relationships between different request fields

> **Note:** The Expression Matcher works alongside standard matchers. You can use
> query parameter matchers, header matchers, body matchers, and the Expression Matcher
> together on the same stub. The request will only match if ALL matchers pass.

## Examples

### Example 1: Comparing Date Query Parameters

**Scenario:** You have an API endpoint that accepts `startDate` and `endDate` query
parameters as ISO 8601 timestamps. You want to ensure `startDate` is before `endDate`.

Standard matchers can validate that each date exists and matches a format, but they
cannot compare the two values against each other.

**Expression Matcher Template:**

```handlebars theme={null}
{{lt request.query.startDate.[0] request.query.endDate.[0]}}
```

**Combined with standard matchers:**

* Query param `startDate` matches regex `^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$`
* Query param `endDate` matches regex `^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$`
* Expression Matcher: `{{lt request.query.startDate.[0] request.query.endDate.[0]}}`

**Example request:**

```
GET /api/events?startDate=2025-05-27T07:01:01.000Z&endDate=2025-06-15T14:30:00.000Z
```

This ensures both dates are in the correct ISO 8601 format (via standard matchers) AND
that the start date is less than the end date (via Expression Matcher). Since ISO 8601
timestamps are lexicographically sortable, string comparison works correctly for date
ordering.

To change this into a match for an error stub that matches if the `endDate` is before
`startDate`, you can change the Expression Matcher to:

```handlebars theme={null}
{{gt request.query.startDate.[0] request.query.endDate.[0]}}
```

### Example 2: OR Logic for Query Parameter Validation

**Scenario:** Your API requires query parameters `W`, `X`, `Y`, and `Z`, each needing
to match a specific regex pattern. If ANY parameter fails validation, you want to
return a 400 Bad Request with a helpful error message.

Without the Expression Matcher, you would need to create 4 separate stubs—one for
each parameter that could fail. With the Expression Matcher, you can handle this with
a single stub.

**Expression Matcher Template (matches when ANY parameter is invalid):**

```handlebars theme={null}
{{or
  (not (matches request.query.W.[0] '^[A-Z]{3}$'))
  (not (matches request.query.X.[0] '^\d{4}$'))
  (not (matches request.query.Y.[0] '^[a-z]+@[a-z]+\.[a-z]+$'))
  (not (matches request.query.Z.[0] '^(true|false)$'))
}}
```

**Example request:**

```
GET /my-api?W=ABC&X=1234&Y=test@example.com&Z=NOTTRUE
```

Again, this can be combined with standard matchers to ensure the query parameters are
present

### Example 3: Validating JSON Body Field Relationships

**Scenario:** You're mocking a payment API where the request body contains `amount`
and `currency`. For GBP transactions, the amount must be at least 100 (100 pence).
For USD transactions, the amount must be at least 50 (50 cents).

**Expression Matcher Template:**

```handlebars theme={null}
{{or
  (and
    (eq (jsonPath request.body '$.currency') 'GBP')
    (gte (jsonPath request.body '$.amount') 100)
  )
  (and
    (eq (jsonPath request.body '$.currency') 'USD')
    (gte (jsonPath request.body '$.amount') 50)
  )
}}
```

**Request body example:**

```json theme={null}
{
  "currency": "GBP",
  "amount": 150,
  "description": "Test payment"
}
```

This template ensures the minimum amount rule is applied based on the currency in the same request.

### Example 4: Header-Based Conditional Matching

**Scenario:** Your API supports both API key and Bearer token authentication. You
want a stub that matches requests with EITHER a valid `X-API-Key` header OR a valid
`Authorization` header with a Bearer token.

**Expression Matcher Template:**

```handlebars theme={null}
{{or
  (matches (val request.headers.X-API-Key.[0] or='') "^sk_live_[A-Za-z0-9]{24}$")
  (matches (val request.headers.Authorization.[0] or='') "^Bearer [A-Za-z0-9\\-_]+\\.[A-Za-z0-9\\-_]+\\.[A-Za-z0-9\\-_]+$")
}}
```

```
POST /payments
X-API-Key: sk_live_REDACTED_EXAMPLE_KEY_VALUE
Content-Type: application/json

{
  "amount": 1000,
  "currency": "GBP"
}
```

This allows the stub to match requests using either authentication method, without
needing to create duplicate stubs. The use of the `val` helper ensures the header value
is extracted as a string and handles empty values correctly.

### Example 5: Cross-Request Validation (Header Must Match Body Field)

**Scenario:** Your API requires that the `X-Idempotency-Key` header matches the
`requestId` field in the JSON body. This ensures clients are correctly correlating
their idempotency keys with their request payloads.

**Expression Matcher Template:**

```handlebars theme={null}
{{eq (val request.headers.X-Idempotency-Key.[0] or='') (jsonPath request.body '$.requestId')}}
```

**Example matching request:**

```
POST /api/orders
X-Idempotency-Key: order-12345
Content-Type: application/json

{
  "requestId": "order-12345",
  "items": [...]
}
```

This validates that the header and body field are synchronized.

***

## Debugging

When your Expression Matcher template isn't working as expected, you can use the
request log to help debug the issue.

**How it works:** Any content in your Handlebars template that doesn't resolve to
`true` or `false` will be output in the serve event for the request in the request log.
This allows you to inspect the actual values being evaluated.

**Debugging technique:** Temporarily modify your template to output the values you're working with:

```handlebars theme={null}
startDate: {{request.query.startDate.[0]}} 
endDate: {{request.query.endDate.[0]}}

{{lt request.query.startDate.[0] request.query.endDate.[0]}}
```

When a request is made, check the request log's serve event to see the rendered output:

```
startDate: 2025-05-27T07:01:01.000Z endDate: 2025-05-10T14:30:00.000Z
```

This helps you verify:

* That you're accessing the correct request fields
* The actual values being compared
* Whether values are in the expected format

Once you've identified the issue, update your template to the correct boolean expression and the output will return to `true` or `false`.

***

## Available Helpers

The Expression Matcher supports all the same helpers you can use when writing [dynamic response templates](/response-templating/helper-reference).

## Best Practices

1. **Use standard matchers first** - They're optimized for their specific tasks
2. **Combine matchers** - Use standard matchers for basic validation, Expression Matcher for complex logic
3. **Use debugging output** - When templates aren't working, output values to the request log to diagnose issues


# Request Matching - Matching JSON requests
Source: https://docs.wiremock.io/request-matching/json

Matching JSON

When stubbing API functions that accept JSON request bodies we may want to
return different responses based on the JSON sent. WireMock Cloud provides two match types
to supports this case - `equalToJson` and `matchesJsonPath`, which are described
in detail in this article.

## Matching via JSON equality

The `equalToJson` match operator performs a semantic comparison of the input JSON
against the expected JSON. This has a number of advantages over a straight string
comparison:

* Ignores differences in whitespace
* Can be configured to ignore differences in array order
* Can be configured to ignore extra object attributes
* Supports placeholders so that specific attributes can be excluded from the comparison

By default `equalToJson` will match only if all of the elements in the input JSON
are the same as the expected JSON, arrays are in the same order and no additional
attributes are present.

For instance, given an expected JSON document like

<img title="Default equal to JSON" />

You would need to send in the request body for the stub to match exactly that JSON
in order for the stub to be matched:

```
$ curl https://example.wiremockapi.cloud/json -d '{
  "itemId": 102938,
  "sizes": ["S", "M", "L"]
}'

{ "result": "OK" }
```

Changing the `sizes` order would cause a non-match:

```
$ curl https://example.wiremockapi.cloud/json -d '{
  "itemId": 102938,
  "sizes": ["L", "M", "S"]
}'

                                               Request was not matched
                                               =======================

-----------------------------------------------------------------------------------------------------------------------
| Closest stub                                             | Request                                                  |
-----------------------------------------------------------------------------------------------------------------------
                                                           |
JSON body matching                                         |
                                                           |
POST                                                       | POST
/json                                                      | /json
                                                           |
{                                                          | {                                                   <<<<< Body does not match
  "itemId" : 102938,                                       |   "itemId" : 102938,
  "sizes" : [ "S", "M", "L" ]                              |   "sizes" : [ "L", "M", "S" ]
}                                                          | }
                                                           |
-----------------------------------------------------------------------------------------------------------------------
```

Adding an extra attribute would also cause a non-match:

```
$ curl https://example.wiremockapi.cloud/json -d '{
  "itemId": 102938,
  "sizes": ["S", "M", "L"],
  "tag": "essentials"
}'

                                               Request was not matched
                                               =======================

-----------------------------------------------------------------------------------------------------------------------
| Closest stub                                             | Request                                                  |
-----------------------------------------------------------------------------------------------------------------------
                                                           |
JSON body matching                                         |
                                                           |
POST                                                       | POST
/json                                                      | /json
                                                           |
{                                                          | {                                                   <<<<< Body does not match
  "itemId" : 102938,                                       |   "itemId" : 102938,
  "sizes" : [ "S", "M", "L" ]                              |   "sizes" : [ "S", "M", "L" ],
}                                                          |   "tag" : "essentials"
                                                           | }
                                                           |
-----------------------------------------------------------------------------------------------------------------------
```

### Ignoring array order

Sometimes the order of elements in an array is unimportant and can change arbitrarily
between multiple requests. In this case it's undesirable for your stub match to fail
due to array order, so to remedy this you can simply tick "Ignore array order".

<img title="Equal to JSON ignoring array order" />

This will allow requests like the following to succeed:

```
$ curl https://example.wiremockapi.cloud/json -d '{
  "itemId": 102938,
  "sizes": ["S", "L", "M"]
}'                   

{ "result": "OK" }
```

### Ignoring extra elements

If you're only interested in matching a specific set of JSON elements and don't mind
if additional elements are present you can tick "Ignore extra elements".

<img title="Equal to JSON ignoring extra elements" />

This would permit the following to match:

```
$ curl https://example.wiremockapi.cloud/json -d '{
  "itemId": 102938,
  "sizes": ["S", "M", "L"],
  "tag": "essentials"
}'
```

### Using placeholders to ignore specific JSON attributes

If you want to check that an element is present, but don't care what the value is
then you can use JSONUnit placeholder syntax to achieve this.

Note: unlike with XML placeholders this is enabled by default.

For instance, given the following configuration:

<img title="Equal to JSON with placeholder" />

This would permit the the following to match:

```
$ curl https://example.wiremockapi.cloud/json -d '{
  "itemId": 8888888888,
  "sizes": ["S", "M", "L"],
  "tag": "essentials"
}'
```

When using `${json-unit.ignore}`, the element's type is also ignored (in addition to its value),
so in the above case a string, boolean etc. could have been used in place of the numeric ID.

If you want to constrain an element to a specific type but still ignore the value
you can use one of the following placeholders:

* `${json-unit.regex}[A-Z]+` (any Java-style regular expression can be used)
* `${json-unit.any-string}`
* `${json-unit.any-boolean}`
* `${json-unit.any-number}`

## Matching via JSONPath - `matchesJsonPath`

[JSONPath](https://github.com/json-path/JsonPath) is an expression language,
similar in concept to XPath that permits elements or collections of elements
to be queried from a JSON document.

WireMock Cloud supports stub matching using JSONPath expressions, optionally sub-matching
the result using WireMock Cloud's own operators (`equalTo`, `matches` etc.).

Given the following configration:

<img title="JSONPath with equal to" />

The following JSON will be matched:

```
$ curl https://example.wiremockapi.cloud/json -d '{
  "itemId": 102938,
  "itemName": "Socks"
}'
```

### Expression only vs. expression + sub-match

It is possible to match a JSON document without a sub-match by selecting "is present"
from the drop-down:

<img title="JSONPath with equal to" />

If you do this, the JSON input will be considered a match if the expression returns
1 or more elements.

This feature is primarily present for compatibility with WireMock projects, and
generally it is better to use sub-matches as this results in simpler JSONPath
expressions and more useful debug output when there is a non-match.

### Common JSONPath examples

Matching on a specific array element by position.

`$.sizes[1]` `equal to` `M`

would match:

```json theme={null}
{
  "sizes": ["S", "M", "L"]
}
```

Matching on an element of an object found via another element.

`$.addresses[?(@.type == 'business')].postcode` `contains` `N11NN`

would match:

```json theme={null}
{
  "addresses": [
    {
      "type": "home",
      "postcode": "Z55ZZ"
    },
    {
      "type": "business",
      "postcode": "N11NN"
    }
  ]
}
```

It is necessary to use `contains` in this instance as a JSONPath expression containing
a query part (between the `[?` and `]`) will always return a collection
of results.

Matching an element found recursively.

`$..postcode` `contains` `N11NN`

would match:

```json theme={null}
{
  "addresses": [
    {
      "type": "home",
      "postcode": "Z55ZZ"
    },
    {
      "type": "business",
      "postcode": "N11NN"
    }
  ]
}
```

and would also match:

```json theme={null}
{
  "address": {
    "type": "business",
    "postcode": "N11NN"
  }
}
```


# Request Matching - Overview of Matcher Types
Source: https://docs.wiremock.io/request-matching/matcher-types

Overview of the match operations supported by WireMock Cloud

WireMock Cloud (via WireMock) supports a set of match operations that can be used against
the request's query, headers, cookies and body.

This article provides an overview of these matchers. The names shown are the exact
keys used in the WireMock/WireMock Cloud JSON API.

## `equalTo`

Only matches if the input string is exactly equal to the expected value.

## `binaryEqualTo`

Like `equalTo` but compares bytes rather than strings. Useful when you need to match
e.g. an uploaded image.

## `matches`

Matches the input string against a [Java style regular expression](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html).

## `doesNotMatch`

The negative of `matches`. Will match if the incoming value does **not** match the regular expression.

## `contains`

Matches if the input string contains the expected value.

## `doesNotContain`

The negative of `contains`. Will match if the input string does **not** contain the expected value.

## `equalToJson`

Matches if the input string is valid JSON and is semantically equal to the expected value.
This is often a better choice than `equalTo` when dealing with JSON as it will ignore
differences in whitespace, and it is optionally possible to ignore array orderings
and extra object attributes. It also provides the concept of placeholders, allowing
you to selectively ignore or merely constrain specific JSON elements.

The underlying implementation for `equalToJson` is supplied by
[JSONUnit](https://github.com/lukas-krecan/JsonUnit).

You can learn more about working with JSON in the [Matching JSON](./json/) article.

## `matchesJsonPath`

Tests the input JSON string against a JSONPath expression, and returns a match if
one or more elements are returned. No match will be returned if the input is not valid
JSON.

The actual JSONPath evaluation is performed by the [Java JSONPath implementation](https://github.com/json-path/JsonPath).

## `equalToXml`

Matches if the input string is valid XML and is semantically equal to the expected value.
Like with `matchesJsonPath` this ignores differences in whitespace and supports placeholders
so that specific element values can be ignored.

The underlying implementation for `equalToXml` is supplied by
[XMLUnit](https://www.xmlunit.org/).

You can learn more about working with XML in the [Matching XML](./xml/) article.

## `matchesXPath`

Tests the input XML string against an XPath 1.0 expression, and returns a match if
one or more elements are returned. No match will be returned if the input is not valid
XML.

## `before, after and equals(date/time)`

Tests the input matches a date/time. Date/times can be Absolute or Relative and the expected format can also be configured using Java's date time format.

### `before`

The date/time must be **before** the expected date config.

### `after`

The date/time must be **after** the expected date config.

### `equals (date/time)`

The date/time must exactly match the expected date config.

You can read more about the possible configure options available for [wiremock here](https://wiremock.org/docs/request-matching/#dates-and-times)

You can match numbers in their String representation using `equalTo`. For matching based on their numeric value, use
the following matchers:

### `equalToNumber`

For matching based on a numeric value.

### `greaterThanNumber`

For matching based on whether a numeric value is greater than the expected value.

### `greaterThanEqualNumber`

For matching based on whether a numeric value is greater than or equal to the expected value.

### `lessThanNumber`

For matching based on whether a numeric value is less than the expected value.

### `lessThanEqualNumber`

For matching based on whether a numeric value is less than or equal to the expected value.

These matchers always report inputs that cannot be parsed to a number as not matching. It can be used for matching both strings and numbers.


# Request Matching - Matching URLs
Source: https://docs.wiremock.io/request-matching/url

Matching the request's URL

For most HTTP APIs the URL is the primary means by which the appropriate action
is selected. WireMock Cloud provides a number of different options for matching the
URL of an incoming request to a stub.

## Path vs path + query

It's important to be clear exactly which part(s) of the URL you wish to match.

The default strategy WireMock Cloud uses is to match both the path and query parts of the
URL. For instance, if you were you to enter the following in a stub's URL field:

```
/my/path?q=abc&limit=10
```

then the stub would only be matched if that exact path and query were present e.g.
for the URL:

```
https://my-api.wiremockapi.cloud/my/path?q=abc&limit=10
```

<img title="Path and query matching" />

However, it's often desirable just to look at the path part of the URL, and either
ignore the query completely or specify it more flexibly using dedicated query parameter
matchers (see [Query Parameters](/advanced-stubbing/#advanced-request-parameter-matching)).
Dedicated query matchers can be useful if the parameter order in the URL can change,
or if you need to match more loosely on the value e.g. using `contains` rater than
exact equality.

To do this, you need to change the URL match type in the Advanced section to `Path`
and ensure you only specify a path in the URL field e.g.

```
/my/path
```

This would now match any of the following URLs:

```
https://my-api.wiremockapi.cloud/my/path?q=abc
https://my-api.wiremockapi.cloud/my/path?q=abc&limit=10
https://my-api.wiremockapi.cloud/my/path
https://my-api.wiremockapi.cloud/my/path?randomqueryparam=123
```

<img title="Path and query matching" />

## Match type - exact vs. regular expression

In addition to choosing the URL part(s) you wish to match, you can also choose whether
to check for exact equality or a regular expression match. By default WireMock Cloud uses
an equality check, but this can be changed in the Advanced section.

<img title="URL match types" />

Choosing the `Path regex` match type can be particularly useful in cases where
the API you're mocking uses path parameters and you wish to provide a meaningful response
to a specific URL pattern regardless of the specific parameter values.

For instance, choosing `Path regex` as the match type with the following URL

```
/users/[0-9]+
```

would match any of the following request URLs:

```
/users/1
/users/9832749823
/users/321
```

A powerful approach is to combine this with [Response Templating](/response-templating/basics/)
so that the ID used in the URL can be inserted into the response body.

<Note>Using the Path and query regex is generally not advised. This exists primarily for compatibility with projects exported to/from WireMock.</Note>

## Path template (path parameters)

If you require a stub's URL to allow dynamic path variables, you can use the path template URL match type.
This URL match type provides a convenient way to match URLs whose path segments match certain values and/or a way to
reference a request's dynamic path segments by name in a response template, rather than the usual indexed method
(e.g. `request.path.thingId` rather than `request.path.1`).

To configure a stub to use the path template URL match type, enter a path value that declares one or more path variables
using square bracket syntax (e.g. `/things/{thingId}`) and select the "Path template" URL match type.
Now you can add path parameters that match against the value of a request's path variables.

<img title="URL path template and parameter" />

You can also now reference the value of a request's path variables by name in the response template.

<img title="Referencing a URL path parameter in a template" />

## Matching any URL

In some cases you need a stub to match any request URL. A common use case for this
is providing a low priority default response which is matched only if nothing else does.
You might also choose to proxy the request to another endpoint in this case.

For this purpose use the `Any URL` option from the URL match type list under Advanced.


# Request Matching - Matching XML bodies
Source: https://docs.wiremock.io/request-matching/xml

Matching XML

When stubbing API functions that accept XML request bodies we may want to
return different responses based on the XML sent. WireMock Cloud provides two match types
to supports this case - `equalToXml` and `matchesXPath`, which are described
in detail in this article.

## Matching via XML equality - `equalToXml`

The `equalToXml` match operator performs a semantic comparison of the input XML
against the expected XML. This has a number of advantages over a straight string
comparison:

* Ignores differences in whitespace
* Ignores element and attribute order
* Supports placeholders so that specific elements or attributes can be excluded from the comparison

By default `equalToXml` will match the input to the expected XML if all elements
and attributes are present, have the same value and there are no additional
elements or attributes.

For instance, given the following configuration:

<img title="Default equal to XML" />

The following XML would match:

```xml theme={null}
<things>
  <two id="234" val="2"/>
  <one val="1" id="123" />

</things>
```

### Using placeholders to ignore specific elements or attributes

As with JSON equality matching, placeholders can be used with XML to ignore specific
elements or attributes.

Given the following configuration:

<img title="Equal to XML with placeholders" />

The following XML will match:

```xml theme={null}
<things>
  <one id="123" val="123456789"/>
  <two id="234" val="2"/>
  <three>999999</three>
</things>
```

## Matching via XPath - `matchesXPath`

WireMock Cloud supports matching incoming XML using XPath 1.0 expressions. The most common
use case for this is when accepting XML request bodies, although it can be used
with other request fields such as headers.

The input XML is deemed a match if any elements are returned when the XPath
expression is evaluated against it.

Given a body match on the XPath expression `/things/thing[@name = 'socks']`.

<img title="Matching on XPath" />

The following XML will match:

```xml theme={null}
<things>
  <thing name="socks"></thing>
  <thing name="shoes"></thing>
</things>
```


# Dynamic Responses with Templates
Source: https://docs.wiremock.io/response-templating/basics

Returning dynamic responses using Handlebars templates

Some elements of WireMock Cloud stub responses can be configured generated dynamically, via the use of [Handlebars templates](https://github.com/jknack/handlebars.java).

Most commonly this is used in the response body but response header values can also
be templated. For proxy responses, the target URL can be a template.

## Enabling templating

Enable templating for a stub by ticking the "Enable templating" box in the Response section:

<img title="Enable templating" />

Ticking this box means that header values can be templated e.g.

<img title="Header template" />

And also the response body e.g.

<img title="Body template" />

## Handlebars overview

A complete description of the Handlebars syntax and core helpers can be found on the [Handlebars JS](https://handlebarsjs.com/guide/), but we'll cover the essentials here.

Handlebars works like many other template languages - a template is provided a data model
and uses a special tag syntax to denote dynamic elements, referred to as a "helper" in this case.

Helpers are always delimited by double or triple curly braces (`{` and `}`). In the simplest case a helper can
simply output the value of a variable in the model:

```handlebars theme={null}
{{myVariable}}        // Top-level model variable
{{outerVar.innerVar}} // Nested model variable
```

### Helper parameters

Helpers can take both positional and named parameters. In both cases they are delimited by spaces.

The following helper takes three positional parameters -
the string in which the replacement should take place, the substring to find and the
replacement value:

```handlebars theme={null}
{{replace myString 'foo' 'bar'}}
```

Named values are of the form `name=value`. The following helper has a single
positional parameter followed by a parameter named `format`:

```handlebars theme={null}
{{dateFormat myDate format='yyyy-MM-dd'}}
```

### Nesting helpers

Sometimes it's necessary to apply a helper to the result of another one. This can
be achieved by nesting helpers using bracket syntax. For example, this template
will truncate the input string, then capitalise the first letter:

```handlebars theme={null}
{{capitalize (substring myString 0 4)}}
```

### Blocks

Blocks can be used to apply processing to an inner piece of content.

```handlebars theme={null}
{{#if productExists}}
  // do something with the product
{{else}}
  // product not found
{{/if}}
```

Blocks form the foundation of logical and looping structures in Handlebars and are [described here in more detail](/response-templating/conditional-logic-and-iteration/).

### HTML escaping

We mentioned earlier that double or triple curly braces are used to delimit helpers.
The difference between these two forms is that with double braces, Handlebars will
automatically HTML escape the output of the helper, whereas with triple braces no escaping will be
applied.

For instance, suppose we have a data model where the variable `tag` has the value `<html>`.

The template

```handlebars theme={null}
{{tag}}
```

will output

```
&lt;html&gt;
```

whereas the template

```handlebars theme={null}
{{{tag}}}
```

will output

```
<html>
```

## The request model

When templates are evaluated, they have access to a data model containing information about the incoming request. For a complete reference of all available request attributes and how to access them, see the [Request Model Reference](/response-templating/request-model).

## Handlebars helpers

WireMock Cloud provides a set of Handlebars helpers that perform a variety of logical functions and transformations inside templates. These include all of the standard helpers from the [Java Handlebars implementation by jknack](https://github.com/jknack/handlebars.java).

All of the available helpers are described in detail in these articles:

* [Conditional Logic and Iteration](./conditional-logic-and-iteration/)
* [Strings](./string-helpers/)
* [String Encodings](./string-encodings/)
* [Dates & Times](./dates-and-times/)
* [Random Values](./random-values/)
* [Random Faker](./random-faker/)
* [XML](./xml/)
* [JSON](./json/)
* [JSON Web Tokens](./jwt/)
* [Miscellaneous Helpers](./misc-helpers/)


# Response Templating - Conditional Logic and Iteration
Source: https://docs.wiremock.io/response-templating/conditional-logic-and-iteration

Working with if statements, loops and collections.

Taking actions conditionally and looping over collections of data are very common
requirements from a templating system. This article explains how these are achieved
in WireMock Cloud.

## Conditional logic with if / else and unless

Handlebars provides a set of core helpers that implement if / else if / else logic
of the kind found in many programming languages.

As with most implementations of if, the simples form is to take an action only if
the condition is true:

```handlebars theme={null}
{{#if showDetails}}
  <div id="details">...</div>
{{/if}}
```

An else clause can be used:

```handlebars theme={null}
{{#if showDetails}}
  <div id="details">...</div>
{{else}}
  <div id="details" class="hidden">...</div>
{{/if}}
```

And any number of else if clauses can also be added:

```handlebars theme={null}
{{#if showVariantA}}
  <div id="var-a">...</div>
{{else if showVariantB}}
  <div id="var-b">...</div>
{{else if showVariantC}}
  <div id="var-c">...</div>
{{else}}
  <div id="default-var">...</div>
{{/if}}
```

Finally, you can take an action if a condition is false using `unless`:

```handlebars theme={null}
{{#unless hideDetails}}
  <div id="details">...</div>
{{/unless}}
```

## Comparison helpers

The `if`, `else if` and `unless` helpers all take a single boolean value
as their parameter. In practice you often need to derive that value by comparing
other values, and for this we have a set of helpers implementing common comparison operations.

For instance if you needed to check that a variable equalled a particular string
you would use the `eq` helper:

```handlebars theme={null}
{{#eq name 'Dan'}}
  <div id="dan">...</div>
{{/eq}}
```

You can nest comparison helpers inside the `if` helper:

```handlebars theme={null}
{{#if (eq name 'Dan')}}
  <div id="dan">...</div>
{{/if}}
```

You can also use comparison helpers with `else`:

```handlebars theme={null}
{{#eq name 'Dan'}}
  <div id="dan">...</div>
{{else eq name 'Mark'}}
  <div id="mark">...</div>
{{else}}
  <div id="anon">...</div>
{{/eq}}
```

The following comparison helpers are available:

`eq` - equal

```handlebars theme={null}
{{#eq name 'Jeff'}}...{{/eq}}
```

`neq` - not equal

```handlebars theme={null}
{{#neq name 'Jeff'}}...{{/neq}}
```

`gt` - greater than

```handlebars theme={null}
{{#gt itemCount 3}}...{{/gt}}
```

`gte` - greater than or equal to

```handlebars theme={null}
{{#gte itemCount 3}}...{{/gte}}
```

`lt` - less than

```handlebars theme={null}
{{#lt itemCount 3}}...{{/lt}}
```

`lte` - less than or equal

```handlebars theme={null}
{{#lte itemCount 3}}...{{/lte}}
```

`and` - logical AND

```handlebars theme={null}
{{#and (lt itemCount 10) (gt itemCount 5)}}...{{/and}}
```

`or` - logical OR

```handlebars theme={null}
{{#or (eq itemCount 1) (eq itemCount 2)}}...{{/or}}
```

`not` - logical NOT

```handlebars theme={null}
{{#not (eq itemCount 1)}}...{{/not}}
```

## Iteration

You can loop over collections of data using the `each` helper.

```handlebars theme={null}
{{#each request.query.things as |thing|}}
  thing: {{{thing}}}
{{/each}}
```

### Iterating over JSON and XML elements

The `jsonPath` and `xPath` helpers both output collections so these can be used
in an `each` loop. See [Working with JSON](./json/#iterating-over-json-elements) and
[Working with XML](./xml/#iterating-over-xml-elements) for details.

### Detecting the first and last element while looping

Often it can be useful to know when you're processing the first or last element
in a collection e.g. so that you can decide whether to output a separate character.

You can do this using the `@first` and `@last` variables that are automatically
provided to the scope inside the `each` block.

For instance, if you wanted to output a list of JSON objects, separated with
commas and avoiding an extraneous comma at the end:

```handlebars theme={null}
{{#each (jsonPath request.body '$.things') as |thing|}}
  {{#if @last}}
    { "thing": {{{thing}}} }
  {{else}}
    { "thing": {{{thing}}} },
  {{/if}}
{{/each}}
```

### Getting the loop index

The `each` helper also creates an `@index` variable in its scope which you can use
to get at the (zero-indexed) element counter:

```handlebars theme={null}
{{#each (jsonPath request.body '$.things') as |thing|}}
  {{@index}}: {{thing}}
{{/each}}
```

## String and collection conditionals

### Contains helper

The `contains` helper returns a boolean value indicating whether the string or array passed as the first parameter
contains the string passed in the second.

It can be used as parameter to the `if` helper:

```handlebars theme={null}
{{#if (contains 'abcde' 'abc')}}YES{{/if}}
{{#if (contains (array 'a' 'b' 'c') 'a')}}YES{{/if}}
```

Or as a block element on its own:

```handlebars theme={null}
{{#contains 'abcde' 'abc'}}YES{{/contains}}
{{#contains (array 'a' 'b' 'c') 'a'}}YES{{/contains}}
```

### Matches helper

The `matches` helper returns a boolean value indicating whether the string passed as the first parameter matches the
regular expression passed in the second:

Like the `contains` helper it can be used as parameter to the `if` helper:

```handlebars theme={null}
{{#if (matches '123' '[0-9]+')}}YES{{/if}}
```

Or as a block element on its own:

```handlebars theme={null}
{{#matches '123' '[0-9]+'}}YES{{/matches}}
```


# Response Templating - Cryptographic Helpers
Source: https://docs.wiremock.io/response-templating/cryptographic-helpers

Using helpers to perform cryptographic operations

## Hashing

You can create a hash of some text using the `hash` helper.

```handlebars theme={null}
{{#hash algorithm='sha-256' encoding='hex'}}text to hash{{/hash}}
```

The output of the helper is a binary encoded string.
The encoding used is determined by the `encoding` option supplied to the helper.
Supported encoding values are `hex` and `base64`.

The `algorithm` option determines the hashing algorithm that will be applied to the input text.
Supported algorithm values are:

* `sha-1`
* `sha-224`
* `sha-256`
* `sha-384`
* `sha-512`
* `sha3-224`
* `sha3-256`
* `sha3-384`
* `sha3-512`
* `md2`
* `md5`

### Examples

SHA-256 hex encoding:

```handlebars theme={null}
{{#hash algorithm='sha-256' encoding='hex'}}text to hash{{/hash}}
```

will output `119e3f0d28cf6a92d29399d5787f90308b6b87670d8c2386ec42cb36e293b5c4`

***

MD5 base64 encoding:

```handlebars theme={null}
{{#hash algorithm='md5' encoding='base64'}}text to hash{{/hash}}
```

will output `J3A5Rbm86ssJVG0uEDrTYA==`

## Signing

You can digitally sign data using the sign helper. This uses the RSA private key\
configured in your certificate settings to create an `SHA-256` with RSA signature.

```handlebars theme={null}
{{ sign "text to sign" }}
```

The output of the helper is a Base64-encoded signature by default. You can control the
output encoding using the encoding option. Supported encoding values are `hex` and
`base64`.

The sign helper supports both inline and block forms:

Inline form:

```handlebars theme={null}
{{ sign "text to sign" }}
```

Block form:

```handlebars theme={null}
{{#sign}}text to sign{{/sign}}
```

With a variable:

```handlebars theme={null}
{{{ sign myVariable }}}
```

### Examples

Sign a string literal with default Base64 encoding:

```handlebars theme={null}
{{{ sign "some data" }}}
```

will output a Base64-encoded RSA signature, e.g. MEUCIQDz...

Sign with hex encoding:

```handlebars theme={null}
{{{ sign "some data" encoding="hex" }}}
```

will output a hex-encoded RSA signature.

The sign helper is particularly useful when constructing signed documents such as SAML
responses, where you need to sign a computed digest or XML fragment. For example, you
can combine it with the hash helper to create a signed SAML assertion:

```handlebars theme={null}
{{#assign 'digest'}}{{#hash algorithm='sha-256' encoding='base64'}}content to
hash{{/hash}}{{/assign}}
{{#assign 'signedInfo'}}...{{digest}}...{{/assign}}
{{ sign signedInfo }}
```

## X.509 Certificate

You can output the X.509 certificate configured in your certificate settings using the
`x509Certificate` helper. This is useful when building signed documents like SAML
responses that need to include the signing certificate.

```handlebars theme={null}
{{ x509Certificate }}
```

The output format is controlled by the format option. Supported format values are `pem`
(default) and `base64`.

### Examples

Output the certificate in PEM format (default):

```handlebars theme={null}
{{ x509Certificate }}
```

will output the full PEM-encoded certificate including headers:

```
-----BEGIN CERTIFICATE-----
MIIBkTCB+wIGAZO...
-----END CERTIFICATE-----
```

Output the raw Base64-encoded certificate (without PEM headers):

```handlebars theme={null}
{{ x509Certificate format="base64" }}
```

will output just the Base64-encoded certificate bytes, e.g. `MIIBkTCB+wIGAZO...`

This is useful when embedding the certificate inside an XML document such as a SAML
response, where PEM headers are not required:

```handlebars theme={null}
<X509Certificate>{{ x509Certificate format="base64" }}</X509Certificate>
```

## Base64 Inflate

You can decode a Base64-encoded, DEFLATE-compressed string in a single operation using
the `base64Inflate` helper. This is primarily designed for decoding SAML requests that
have been compressed and encoded according to the SAML HTTP-Redirect binding
specification.

```handlebars theme={null}
{{ base64Inflate request.query.SAMLRequest }}
```

SAML requests sent via the HTTP-Redirect binding are first DEFLATE-compressed and then
Base64-encoded. Decoding this requires Base64 decoding followed by DEFLATE
inflation. This helper provides these two options in one convenient helper.

The helper accepts a single parameter: the Base64-encoded, DEFLATE-compressed string.
This is typically a query parameter from the incoming request.

Given a valid Base64-encoded, DEFLATE-compressed SAML AuthnRequest in the SAMLRequest
query parameter, this will output the decoded XML, e.g.:

```xml theme={null}
<samlp:AuthnRequest xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"    
                    Destination="https://example-destination.wiremockapi.cloud/login"    
                    ID="_b9ef70230dj5972308i121395cbe9f4a"    
                    IssueInstant="2026-02-09T11:56:42Z"    
                    ProtocolBinding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" 
                    Version="2.0">
    <saml:Issuer xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">urn:auth0:example:connection-id</saml:Issuer>
</samlp:AuthnRequest>
```


# Response Templating - Dates and Times
Source: https://docs.wiremock.io/response-templating/dates-and-times

Working with dates and times

WireMock Cloud has two helpers for manipulating dates - `now` and `date`.

## Current date/time

The `now` helper renders the current date/time, with the ability to specify the format (see [full reference](#format-string-reference)) and offset.

```handlebars theme={null}
{{now}}
{{now offset='3 days'}}
{{now offset='-24 seconds'}}
{{now offset='1 years'}}
{{now offset='10 years' format='yyyy-MM-dd'}}
```

Dates can be rendered in a specific timezone (the default is UTC):

```handlebars theme={null}
{{now timezone='Australia/Sydney' format='yyyy-MM-dd HH:mm:ssZ'}}
```

Pass `epoch` as the format to render the date as UNIX epoch time (in milliseconds), or `unix` as the format to render
the UNIX timestamp in seconds.

```handlebars theme={null}
{{now offset='2 years' format='epoch'}}
{{now offset='2 years' format='unix'}}
```

## Random date values

You can combine the `now` helper with [random helpers](./random-values#random-numbers) to generate random dates:

```handlebars theme={null}
{{now offset=(join (randomInt lower=-365 upper=365) ' days' '')}} // a date somewhere between a year ago and a year in the future
```

## Existing date values

The `date` helper can be used to manipulate existing date values, changing the
offset, timezone and print format in exactly the same manner as with the `now` helper.

```handlebars theme={null}
{{date myDate offset='-1 days' timezone='America/New_York' format='yyyy-MM-dd'}}
```

## Parsing dates from strings

Dates can be parsed from other model elements. This is mostly useful when passed to
the `date` helper for further processing:

```handlebars theme={null}
{{date (parseDate request.headers.MyDate) offset='-1 days'}}
```

### Specifying parser format

You can specify the format to use when parsing a date via a [format string](#format-string-reference):

```handlebars theme={null}
{{parseDate '10/11/2021' format="dd/MM/yyyy"}}
```

Output: `2021-11-10T00:00:00Z`.

Additionally you can specify `unix` or `epoch` as the format which will interpret
parse a large integer denoting (respectively) seconds or milliseconds since 1st of January 1970:

```handlebars theme={null}
{{parseDate '1577964091000' format="epoch"}}
```

Output: `2020-01-02T11:21:31Z`.

## Formatting dates

Date values can be formatted to strings using the `dateFormat` helper. You can
either select a named format from the following:

* `full`: full date format. For example: Tuesday, June 19, 2012
* `long`: long date format. For example: June 19, 2012
* `medium`: medium date format. For example: Jun 19, 2012
* `short`: short date format. For example: 6/19/12

e.g.

```handlebars theme={null}
{{dateFormat (parseDate '2020-01-01T11:11:11Z') 'full'}} // Wednesday, January 1, 2020
```

Or you can specify your own format string ([full reference here](#format-string-reference)):

```handlebars theme={null}
{{dateFormat (parseDate '2020-01-01T11:11:11Z') format='yyyy-MM-dd'}} // 2020-01-01
```

## Format string reference

The following details all of the format string elements used when formatting and parsing dates and times:

| Letter | Date or Time Component                           | Presentation       | Examples                                |
| ------ | ------------------------------------------------ | ------------------ | --------------------------------------- |
| G      | Era designator                                   | Text               | AD                                      |
| y      | Year                                             | Year               | 1996 (yyyy); 96 (yy)                    |
| Y      | Week year                                        | Year               | 2009 (YYYY); 09 (YY)                    |
| M      | Month in year                                    | Month              | July (MMMM); Jul (MMM); 07 (MM)         |
| w      | Week in year                                     | Number             | 27                                      |
| W      | Week in month                                    | Number             | 2                                       |
| D      | Day in year                                      | Number             | 189                                     |
| d      | Day in month                                     | Number             | 10                                      |
| F      | Day of week in month                             | Number             | 2                                       |
| E      | Day name in week                                 | Text               | Tuesday (EEEEEE); Tue (EEE)             |
| u      | Day number of week (1 = Monday, ..., 7 = Sunday) | Number             | 1                                       |
| a      | Am/pm marker                                     | Text               | PM                                      |
| H      | Hour in day (0-23)                               | Number             | 0                                       |
| k      | Hour in day (1-24)                               | Number             | 24                                      |
| K      | Hour in am/pm (0-11)                             | Number             | 0                                       |
| h      | Hour in am/pm (1-12)                             | Number             | 12                                      |
| m      | Minute in hour                                   | Number             | 30                                      |
| s      | Second in minute                                 | Number             | 55                                      |
| S      | Millisecond                                      | Number             | 978                                     |
| z      | Time zone                                        | General time zone  | Pacific Standard Time (zzzz); PST (zzz) |
| Z      | Time zone                                        | RFC 822 time zone  | -0800                                   |
| X      | Time zone                                        | ISO 8601 time zone | -08 (X); -0800 (XX);  -08:00 (XXX)      |

## Truncating dates

The `truncateDate` helper will truncate date/times to specific points e.g.

```handlebars theme={null}
{{truncateDate (parseDate '2021-06-14T00:00:00Z') 'last day of month'}}
```

Output: `Wed Jun 30 00:00:00 UTC 2021`.

The full list of available truncations is:

* `first minute of hour`
* `first hour of day`
* `first day of month`
* `first day of next month`
* `last day of month`
* `first day of year`
* `first day of next year`
* `last day of year`


# Response Templating - Helper Reference
Source: https://docs.wiremock.io/response-templating/helper-reference

Complete reference of all available Handlebars helpers

This article provides a comprehensive reference for all Handlebars helpers available in WireMock Cloud's response templating system.

## Date and Time Helpers

### now

Renders the current date/time with optional formatting and offset.

**Parameters:**

* `format`: Date format string (optional, defaults to ISO8601)
* `offset`: Time offset (e.g., '3 days', '-24 seconds')
* `timezone`: Timezone (optional, defaults to UTC)

**Usage:**

```handlebars theme={null}
{{now}}
{{now offset='3 days'}}
{{now offset='-24 seconds'}}
{{now offset='10 years' format='yyyy-MM-dd'}}
{{now timezone='Australia/Sydney' format='yyyy-MM-dd HH:mm:ssZ'}}
{{now format='epoch'}}
{{now format='unix'}}
```

See [Dates and Times](./dates-and-times#current-datetime) for more details.

***

### date

Manipulates existing date values with offset, timezone, and format changes.

**Parameters:**

* First parameter: Date value
* `format`: Date format string (optional)
* `offset`: Time offset (optional)
* `timezone`: Timezone (optional)

**Usage:**

```handlebars theme={null}
{{date myDate offset='-1 days' timezone='America/New_York' format='yyyy-MM-dd'}}
```

See [Dates and Times](./dates-and-times#existing-date-values) for more details.

***

### parseDate

Parses date strings into date objects.

**Parameters:**

* First parameter: Date string
* `format`: Parser format string (optional)

**Usage:**

```handlebars theme={null}
{{parseDate request.headers.MyDate}}
{{parseDate '10/11/2021' format="dd/MM/yyyy"}}
{{parseDate '1577964091000' format="epoch"}}
{{parseDate '1577964091' format="unix"}}
```

See [Dates and Times](./dates-and-times#parsing-dates-from-strings) for more details.

***

### dateFormat

Formats date values to strings using predefined or custom formats.

**Parameters:**

* First parameter: Date value
* Second parameter: Format name (`full`, `long`, `medium`, `short`) or custom format string
* `format`: Alternative way to specify format string

**Usage:**

```handlebars theme={null}
{{dateFormat (parseDate '2020-01-01T11:11:11Z') 'full'}}
{{dateFormat (parseDate '2020-01-01T11:11:11Z') format='yyyy-MM-dd'}}
```

See [Dates and Times](./dates-and-times#formatting-dates) for more details.

***

### truncateDate

Truncates date/times to specific points.

**Parameters:**

* First parameter: Date value
* Second parameter: Truncation point

**Truncation points:**

* `first minute of hour`
* `first hour of day`
* `first day of month`
* `first day of next month`
* `last day of month`
* `first day of year`
* `first day of next year`
* `last day of year`

**Usage:**

```handlebars theme={null}
{{truncateDate (parseDate '2021-06-14T00:00:00Z') 'last day of month'}}
```

See [Dates and Times](./dates-and-times#truncating-dates) for more details.

***

## String Helpers

### regexExtract

Extracts values from strings using regular expressions.

**Parameters:**

* First parameter: Input string
* Second parameter: Regular expression pattern
* Third parameter (optional): Variable name to assign captured groups

**Usage:**

```handlebars theme={null}
{{regexExtract request.body '[A-Z]+'}}
{{regexExtract request.body '([a-z]+)-([A-Z]+)-([0-9]+)' 'parts'}}
{{parts.0}},{{parts.1}},{{parts.2}}
```

See [String Helpers](./string-helpers#regular-expression-extract) for more details.

***

### trim

Removes whitespace from the start and end of strings.

**Usage:**

```handlebars theme={null}
{{trim request.headers.X-Padded-Header}}

{{#trim}}
    Some stuff with whitespace
{{/trim}}
```

See [String Helpers](./string-helpers#trim) for more details.

***

### abbreviate

Truncates strings that exceed a specified length, adding ellipsis.

**Parameters:**

* First parameter: Input string
* Second parameter: Maximum length

**Usage:**

```handlebars theme={null}
{{abbreviate 'Mocking APIs helps you develop faster' 21}}
```

Output: `Mocking APIs helps...`

See [String Helpers](./string-helpers#abbreviate) for more details.

***

### capitalize

Capitalizes the first letter of each word.

**Parameters:**

* First parameter: Input string

**Usage:**

```handlebars theme={null}
{{capitalize 'mock my stuff'}}
```

Output: `Mock My Stuff`

See [String Helpers](./string-helpers#capitalisation) for more details.

***

### capitalizeFirst

Capitalizes only the first character of the string.

**Parameters:**

* First parameter: Input string

**Usage:**

```handlebars theme={null}
{{capitalizeFirst 'mock my stuff'}}
```

Output: `Mock my stuff`

See [String Helpers](./string-helpers#capitalisation) for more details.

***

### center

Centers text in a field of given width.

**Parameters:**

* First parameter: Input string
* `size`: Field width (required)
* `pad`: Padding character (optional, defaults to space)

**Usage:**

```handlebars theme={null}
{{center 'hello' size=21}}
{{center 'hello' size=21 pad='#'}}
```

See [String Helpers](./string-helpers#center) for more details.

***

### cut

Removes all instances of a specified substring.

**Parameters:**

* First parameter: Input string
* Second parameter: Substring to remove

**Usage:**

```handlebars theme={null}
{{cut 'mocking, stubbing, faults' ','}}
```

Output: `mocking stubbing faults`

See [String Helpers](./string-helpers#cut) for more details.

***

### defaultIfEmpty

Returns the input value if not empty, otherwise returns a default.

**Parameters:**

* First parameter: Input value
* Second parameter: Default value

**Usage:**

```handlebars theme={null}
{{defaultIfEmpty 'my value' 'default'}}
{{defaultIfEmpty '' 'default'}}
```

See [String Helpers](./string-helpers#default-if-empty) for more details.

***

### join

Joins multiple values or collections into a single string.

**Parameters:**

* Multiple values to join
* Last parameter: Separator string
* `prefix`: Optional prefix
* `suffix`: Optional suffix

**Usage:**

```handlebars theme={null}
{{join 'Mark' 'Rob' 'Dan' ', '}}
{{join 'Mark' 'Rob' 'Dan' ', ' prefix='[' suffix=']'}}
```

See [String Helpers](./string-helpers#join) for more details.

***

### ljust

Left-aligns text in a field of given width.

**Parameters:**

* First parameter: Input string
* `size`: Field width (required)
* `pad`: Padding character (optional)

**Usage:**

```handlebars theme={null}
{{ljust 'things' size=20}}
{{ljust 'things' size=20 pad='#'}}
```

See [String Helpers](./string-helpers#justify-left-and-right) for more details.

***

### rjust

Right-aligns text in a field of given width.

**Parameters:**

* First parameter: Input string
* `size`: Field width (required)
* `pad`: Padding character (optional)

**Usage:**

```handlebars theme={null}
{{rjust 'things' size=20}}
{{rjust 'things' size=20 pad='#'}}
```

See [String Helpers](./string-helpers#justify-left-and-right) for more details.

***

### lower

Converts string to lowercase.

**Parameters:**

* First parameter: Input string

**Usage:**

```handlebars theme={null}
{{lower 'WireMock Cloud'}}
```

Output: `wiremock cloud`

See [String Helpers](./string-helpers#lower-and-upper-case) for more details.

***

### upper

Converts string to uppercase.

**Parameters:**

* First parameter: Input string

**Usage:**

```handlebars theme={null}
{{upper 'WireMock Cloud'}}
```

Output: `WIREMOCK CLOUD`

See [String Helpers](./string-helpers#lower-and-upper-case) for more details.

***

### replace

Replaces all occurrences of a substring with another.

**Parameters:**

* First parameter: Input string
* Second parameter: Substring to find
* Third parameter: Replacement string

**Usage:**

```handlebars theme={null}
{{replace 'the wrong way' 'wrong' 'right'}}
```

Output: `the right way`

See [String Helpers](./string-helpers#replace) for more details.

***

### slugify

Converts text to URL-friendly slug format.

**Parameters:**

* First parameter: Input string

**Usage:**

```handlebars theme={null}
{{slugify 'Mock my APIs'}}
```

Output: `mock-my-apis`

See [String Helpers](./string-helpers#slugify) for more details.

***

### stripTags

Removes all HTML/XML tags from string.

**Parameters:**

* First parameter: Input string

**Usage:**

```handlebars theme={null}
{{stripTags '<greeting>hi</greeting>'}}
```

Output: `hi`

See [String Helpers](./string-helpers#strip-tags) for more details.

***

### substring

Extracts a portion of a string between indices.

**Parameters:**

* First parameter: Input string
* Second parameter: Start index
* Third parameter (optional): End index

**Usage:**

```handlebars theme={null}
{{substring 'one two' 4}}
{{substring 'one two' 0 3}}
```

See [String Helpers](./string-helpers#substring) for more details.

***

### wordWrap

Wraps text at specified line length.

**Parameters:**

* First parameter: Input string
* Second parameter: Line length

**Usage:**

```handlebars theme={null}
{{wordWrap 'one two three' 4}}
```

See [String Helpers](./string-helpers#word-wrap) for more details.

***

### yesno

Maps boolean/null values to customizable yes/no/maybe strings.

**Parameters:**

* First parameter: Boolean or null value
* `yes`: Custom yes string (optional)
* `no`: Custom no string (optional)
* `maybe`: Custom maybe/null string (optional)

**Usage:**

```handlebars theme={null}
{{yesno true}}
{{yesno false}}
{{yesno null}}
{{yesno true yes='aye'}}
{{yesno false no='nay'}}
{{yesno null maybe='meh'}}
```

See [String Helpers](./string-helpers#yesno) for more details.

***

## Encoding Helpers

### base64

Encodes or decodes Base64 strings.

**Parameters:**

* First parameter: Input string
* `decode`: Set to `true` for decoding (optional)
* `padding`: Set to `false` to disable padding (optional)

**Usage:**

```handlebars theme={null}
{{{base64 request.headers.X-Plain-Header}}}
{{{base64 request.headers.X-Plain-Header padding=false}}}
{{{base64 request.headers.X-Encoded-Header decode=true}}}

{{#base64}}Content to encode{{/base64}}

{{#base64 decode=true}}Q29udGVudCB0byBkZWNvZGUK{{/base64}}
```

See [String Encodings](./string-encodings#base64) for more details.

***

### urlEncode

Encodes or decodes URL strings according to HTTP URL encoding standard.

**Parameters:**

* First parameter: Input string
* `decode`: Set to `true` for decoding (optional)

**Usage:**

```handlebars theme={null}
{{{urlEncode request.headers.X-Plain-Header}}}
{{{urlEncode request.headers.X-Encoded-Header decode=true}}}

{{#urlEncode}}Content to encode{{/urlEncode}}

{{#urlEncode decode=true}}Content%20to%20decode{{/urlEncode}}
```

See [String Encodings](./string-encodings#urls) for more details.

***

### formData

Parses HTTP form data into an object.

**Parameters:**

* First parameter: Form data string
* Second parameter: Variable name to assign
* `urlDecode`: Set to `true` to URL decode values (optional)

**Usage:**

```handlebars theme={null}
{{formData request.body 'form' urlDecode=true}}{{{form.formField3}}}
{{formData request.body 'form' urlDecode=true}}{{{form.multiValueField.1}}}
{{formData request.body 'form' urlDecode=true}}{{{form.multiValueField.first}}}
```

See [String Encodings](./string-encodings#forms) for more details.

***

## Number Helpers

### math

Performs arithmetic operations.

**Parameters:**

* First parameter: Left operand
* Second parameter: Operator (`+`, `-`, `*`, `/`, `%`)
* Third parameter: Right operand

**Operators:**

* `+`: Addition
* `-`: Subtraction
* `*`: Multiplication
* `/`: Division
* `%`: Modulo (remainder)

**Usage:**

```handlebars theme={null}
{{math 1 '+' 2}}
{{math 4 '-' 2}}
{{math 2 '*' 3}}
{{math 8 '/' 2}}
{{math 10 '%' 3}}
```

See [Number Helpers](./number-helpers#math-helper) for more details.

***

### numberFormat

Formats numbers with control over style, decimal places, and locale.

**Parameters:**

* First parameter: Number to format
* Second parameter (optional): Format type (`integer`, `currency`, `percent`) or format string
* Third parameter (optional): Locale string
* `maximumFractionDigits`: Maximum decimal places
* `minimumFractionDigits`: Minimum decimal places
* `maximumIntegerDigits`: Maximum integer digits
* `minimumIntegerDigits`: Minimum integer digits
* `groupingUsed`: Enable/disable digit grouping (default true)
* `roundingMode`: Rounding mode (`up`, `down`, `half_up`, `half_down`, `half_even`, `ceiling`, `floor`)

**Usage:**

```handlebars theme={null}
{{{numberFormat 123.4567 'currency' 'en_GB'}}}
{{{numberFormat 123.4567 'percent' 'en_GB'}}}
{{{numberFormat 123.4567 '###.000000' 'en_GB'}}}
{{{numberFormat 1234.567 maximumIntegerDigits=3 minimumFractionDigits=6}}}
{{{numberFormat 12345.678 groupingUsed=false}}}
{{{numberFormat 1.239 roundingMode='down' maximumFractionDigits=2}}}
```

See [Number Helpers](./number-helpers#formatting-numbers) for more details.

***

## Random Value Helpers

### randomValue

Generates random strings of specified type and length.

**Parameters:**

* `length`: Length of string (required for most types)
* `type`: Type of random string (required)
* `uppercase`: Convert to uppercase (optional)

**Types:**

* `ALPHANUMERIC`: Letters and numbers
* `ALPHABETIC`: Letters only
* `NUMERIC`: Numbers only
* `ALPHANUMERIC_AND_SYMBOLS`: Letters, numbers, and symbols
* `HEXADECIMAL`: Hex characters (0-9, A-F)
* `UUID`: UUID format (length not needed)

**Usage:**

```handlebars theme={null}
{{randomValue length=33 type='ALPHANUMERIC'}}
{{randomValue length=12 type='ALPHANUMERIC' uppercase=true}}
{{randomValue length=55 type='ALPHABETIC'}}
{{randomValue length=27 type='ALPHABETIC' uppercase=true}}
{{randomValue length=10 type='NUMERIC'}}
{{randomValue length=5 type='ALPHANUMERIC_AND_SYMBOLS'}}
{{randomValue length=5 type='HEXADECIMAL' uppercase=true}}
{{randomValue type='UUID'}}
```

See [Random Values](./random-values#random-strings) for more details.

***

### randomInt

Generates random integers with optional bounds.

**Parameters:**

* `lower`: Lower bound (optional)
* `upper`: Upper bound (optional)

**Usage:**

```handlebars theme={null}
{{randomInt}}
{{randomInt lower=5 upper=9}}
{{randomInt upper=54323}}
{{randomInt lower=-24}}
```

See [Random Values](./random-values#random-numbers) for more details.

***

### randomDecimal

Generates random decimal numbers with optional bounds.

**Parameters:**

* `lower`: Lower bound (optional)
* `upper`: Upper bound (optional)

**Usage:**

```handlebars theme={null}
{{randomDecimal}}
{{randomDecimal lower=-10.1 upper=-0.9}}
{{randomDecimal upper=12.5}}
{{randomDecimal lower=-24.01}}
```

See [Random Values](./random-values#random-numbers) for more details.

***

### pickRandom

Randomly selects a value from parameters or collection.

**Parameters:**

* First parameter: Collection (optional) or first value
* Additional parameters: More values to choose from
* `count`: Number of unique items to select (optional)

**Usage:**

```handlebars theme={null}
{{pickRandom '1' '2' '3'}}
{{pickRandom numberList}}
{{pickRandom 1 2 3 4 5 count=3}}
```

See [Random Values](./random-values#pick-random) for more details.

***

### random

Generates random test data using Faker library.

**Parameters:**

* First parameter: Faker key (e.g., 'Name.firstName', 'Address.city')

**Usage:**

```handlebars theme={null}
{{random 'Name.firstName'}}
{{random 'Name.lastName'}}
{{random 'Internet.emailAddress'}}
{{random 'Address.city'}}
{{random 'PhoneNumber.phoneNumber'}}
```

See [Generate Test Data](./random-faker) for the complete list of available keys.

***

## JSON Helpers

### jsonPath

Extracts values from JSON documents using JSONPath expressions.

**Parameters:**

* First parameter: JSON string or object
* Second parameter: JSONPath expression

**Usage:**

```handlebars theme={null}
{{jsonPath request.body '$.outer.inner'}}
{{jsonPath request.body '$.things[0].id'}}
```

See [Working with JSON](./json) for more details.

***

### jsonArrayAdd

Appends elements to a JSON array.

**Parameters:**

* First parameter: Existing array
* Second parameter (optional): Item to add
* `maxItems`: Maximum array size (optional)
* `flatten`: Flatten nested arrays (optional)
* `jsonPath`: Path to nested array (optional)

**Usage:**

```handlebars theme={null}
{{jsonArrayAdd existingArray newItem}}

{{#jsonArrayAdd existingArray}}
{
  "id": 321,
  "name": "sam"
}
{{/jsonArrayAdd}}

{{#jsonArrayAdd existingArray maxItems=2}}
{
  "id": 456,
  "name": "bob"
}
{{/jsonArrayAdd}}

{{#jsonArrayAdd existingArray flatten=true}}
[
  {
    "id": 456,
    "name": "bob"
  }
]
{{/jsonArrayAdd}}

{{jsonArrayAdd existingArray itemToAdd jsonPath='$[0].names'}}
```

See [Working with JSON](./json#adding-to-a-json-array) for more details.

***

### jsonRemove

Removes elements from JSON arrays or keys from objects using JSONPath.

**Parameters:**

* First parameter: JSON object or array
* Second parameter: JSONPath expression

**Usage:**

```handlebars theme={null}
{{jsonRemove existingArray '$.[?(@.id == 123)]'}}
{{jsonRemove existingObject '$.name'}}
```

See [Working with JSON](./json#removing-from-a-json-array-or-object) for more details.

***

### jsonMerge

Merges two JSON objects recursively.

**Parameters:**

* First parameter: Base object
* Second parameter (optional): Object to merge
* `removeNulls`: Remove null-valued attributes (optional)

**Usage:**

```handlebars theme={null}
{{jsonMerge object1 object2}}

{{#jsonMerge object1}}
{
  "name": "Robert",
  "nickname": "Bob"
}
{{/jsonMerge}}

{{#jsonMerge object1 removeNulls=true}}
{
  "removeMe": null
}
{{/jsonMerge}}
```

See [Working with JSON](./json#merging-json-objects) for more details.

***

### formatJson

Formats JSON in pretty or compact style.

**Parameters:**

* First parameter (optional): JSON to format
* `format`: Style (`pretty` or `compact`, defaults to `pretty`)

**Usage:**

```handlebars theme={null}
{{formatJson object1}}
{{formatJson object1 format='compact'}}

{{#formatJson}}
{"id": 456, "name": "Robert"}
{{/formatJson}}
```

See [Working with JSON](./json#formatting-json) for more details.

***

### parseJson

Parses JSON string into object and assigns to variable.

**Parameters:**

* First parameter: JSON string or variable name
* Second parameter (optional): Variable name to assign

**Usage:**

```handlebars theme={null}
{{#parseJson 'newVariableName'}}
    [ "shoes", "socks" ]
{{/parseJson}}

{{parseJson inputString 'newVariableName'}}
```

See [Working with JSON](./json#reading-object-as-json) for more details.

***

### toJson

Converts any object to JSON string.

**Parameters:**

* First parameter: Object to convert

**Usage:**

```handlebars theme={null}
{{toJson (array 1 2 3)}}
```

See [Working with JSON](./json#writing-data-as-a-json-string) for more details.

***

## XML Helpers

### xPath

Extracts values or sub-documents from XML using XPath 1.0 expressions.

**Parameters:**

* First parameter: XML string
* Second parameter: XPath expression

**Usage:**

```handlebars theme={null}
{{{xPath request.body '/outer/inner/text()'}}}
{{{xPath request.body '/outer/inner/@id'}}}
```

See [Working with XML](./xml) for more details.

***

### soapXPath

Convenience helper for extracting values from SOAP body elements.

**Parameters:**

* First parameter: SOAP XML string
* Second parameter: XPath expression (relative to SOAP body)

**Usage:**

```handlebars theme={null}
{{{soapXPath request.body '/a/test/text()'}}}
```

See [Working with XML](./xml#soap-xpath) for more details.

***

### formatXml

Formats XML in pretty or compact style.

**Parameters:**

* First parameter (optional): XML to format
* `format`: Style (`pretty` or `compact`, defaults to `pretty`)

**Usage:**

```handlebars theme={null}
{{formatXml object1}}
{{formatXml object1 format='compact'}}

{{#formatXml}}
<foo><bar>wh</bar></foo>
{{/formatXml}}
```

See [Working with XML](./xml#formatting-xml) for more details.

***

## Cryptographic Helpers

### hash

Creates cryptographic hashes of text.

**Parameters:**

* `algorithm`: Hashing algorithm (required)
* `encoding`: Output encoding (`hex` or `base64`, required)

**Algorithms:**

* `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`
* `sha3-224`, `sha3-256`, `sha3-384`, `sha3-512`
* `md2`, `md5`

**Usage:**

```handlebars theme={null}
{{#hash algorithm='sha-256' encoding='hex'}}text to hash{{/hash}}
{{#hash algorithm='md5' encoding='base64'}}text to hash{{/hash}}
```

See [Cryptographic Helpers](./cryptographic-helpers) for more details.

***

## JWT Helpers

### jwt

Generates signed JSON Web Tokens.

**Parameters:**

* `alg`: Signing algorithm (`HS256` or `RS256`, defaults to `HS256`)
* `maxAge`: Expiry duration (e.g., '12 days')
* `exp`: Expiry date (alternative to maxAge)
* `nbf`: Not before date (optional)
* `iss`: Issuer claim (optional)
* `aud`: Audience claim (optional)
* `sub`: Subject claim (optional)
* Any additional parameters become custom claims

**Usage:**

```handlebars theme={null}
{{{jwt maxAge='12 days'}}}
{{{jwt exp=(parseDate '2040-02-23T21:22:23Z')}}}
{{{jwt nbf=(parseDate '2018-02-23T21:22:23Z')}}}
{{{jwt iss='https://jwt-example.wiremockapi.cloud/'}}}
{{{jwt aud='https://jwt-target.wiremockapi.cloud/'}}}
{{{jwt sub='jonsmith'}}}
{{{jwt
    isAdmin=true
    quota=23
    score=0.96
    email='jonsmith@example.com'
}}}
{{{jwt alg='RS256'}}}
```

See [JWT Web Tokens](./jwt#generating-a-token) for more details.

***

### jwks

Generates JSON Web Key Set for RS256 public keys.

**Usage:**

```handlebars theme={null}
{{{jwks}}}
```

See [JWT Web Tokens](./jwt#the-json-web-key-set-jwks) for more details.

***

## Dynamic State Helpers

### state

Retrieves a state value stored in a context by its key.

**Parameters:**

* First parameter: Key name (required)
* `context`: Context name (optional, uses default context if not specified)

**Usage:**

```handlebars theme={null}
{{state 'itemName'}}
{{state 'userId' context='v1_users'}}
{{state 'id' context=collectionContext}}
```

See [Dynamic State Basics](../dynamic-state/overview#setting--rendering-simple-state) for more details.

***

### stateContext

Sets the default context for all `state` helpers within its block, avoiding repetition.

**Parameters:**

* First parameter: Context name or expression (required)

**Usage:**

```handlebars theme={null}
{{#stateContext request.headers.x-test-id}}
  The current itemName is {{state 'itemName'}}
  The current userId is {{state 'userId'}}
{{/stateContext}}

{{#stateContext collectionContext}}
  {{#formatJson}}
    {{state id}}
  {{/formatJson}}
{{/stateContext}}
```

See [Dynamic State Basics](../dynamic-state/overview#rendering-a-state-value-from-an-explicit-context) for more details.

***

### listState

Returns all state values within a given context as a collection.

**Parameters:**

* First parameter: Context name or expression (required)

**Usage:**

```handlebars theme={null}
{{listState request.headers.x-test-id}}
{{listState collectionContext}}

{{#formatJson}}
{
  "users" : [{{#arrayJoin ',' (listState collectionContext) as |item|}}
    {{jsonPath item '$.user'}}
  {{/arrayJoin}}]
}
{{/formatJson}}

{{#formatJson}}
  [{{arrayJoin ',' (listState collectionContext)}}]
{{/formatJson}}
```

See [Dynamic State Basics](../dynamic-state/overview#rendering-all-state-values-within-a-context) for more details.

***

## Collection and Utility Helpers

### assign

Creates a string variable for later use.

**Parameters:**

* First parameter: Variable name

**Usage:**

```handlebars theme={null}
{{#assign 'myCapitalisedQuery'}}{{capitalize request.query.search}}{{/assign}}

Capitalised query: {{myCapitalisedQuery}}
```

See [Miscellaneous Helpers](./misc-helpers#assignment) for more details.

***

### val

Accesses values with default fallback, maintains type (unlike assign).

**Parameters:**

* First parameter: Value or expression
* `or`/`default`: Default value if first parameter is absent
* `assign`: Variable name to assign result

**Usage:**

```handlebars theme={null}
{{val request.query.search or='default'}}
{{val request.query.search default='default'}}
{{val request.query.search}}
{{val request.query.search or='default' assign='myVar'}}
{{val request.query.search assign='myVar'}}
{{val (array 1 2 3) default='123'}}
{{val 'value for myVar' assign='myVar'}}{{myVar}}
{{val 10 assign='myVar'}}{{#lt myVar 20}}Less Than{{else}}More Than{{/lt}}
```

See [Miscellaneous Helpers](./misc-helpers#val-helper) for more details.

***

### size

Returns the size of a string, list, or map.

**Parameters:**

* First parameter: String, list, or map

**Usage:**

```handlebars theme={null}
{{size 'abcde'}}
{{size request.query.things}}
```

See [Miscellaneous Helpers](./misc-helpers#size) for more details.

***

### with

Creates a nested scope for accessing object properties.

**Parameters:**

* First parameter: Object

**Usage:**

```handlebars theme={null}
{{#with myObject}}
  ID: {{{id}}}
  Position: {{{position}}}
{{/with}}
```

See [Miscellaneous Helpers](./misc-helpers#with) for more details.

***

### range

Generates an array of integers between two bounds.

**Parameters:**

* First parameter: Lower bound (inclusive)
* Second parameter: Upper bound (exclusive)

**Usage:**

```handlebars theme={null}
{{range 3 8}}
{{range -2 2}}
{{#each (range 0 (randomInt lower=1 upper=10)) as |index|}}
id: {{index}}
{{/each}}
```

See [Miscellaneous Helpers](./misc-helpers#range) for more details.

***

### array

Creates an array containing the specified values.

**Parameters:**

* Any number of values

**Usage:**

```handlebars theme={null}
{{array 1 'two' true}}
{{array}}
```

See [Miscellaneous Helpers](./misc-helpers#array) for more details.

***

### arrayAdd

Adds an element to an array at specified position.

**Parameters:**

* First parameter: Array
* Second parameter: Element to add
* `position`: Index, `start`, or `end` (optional, defaults to end)

**Usage:**

```handlebars theme={null}
{{arrayAdd (array 1 'three') 2 position=1}}
{{arrayAdd (array 1 'three') 2 position='start'}}
{{arrayAdd (array 1 'three') 2 position='end'}}
{{arrayAdd (array 1 'three') 2}}
```

See [Miscellaneous Helpers](./misc-helpers#array-add--remove-helpers) for more details.

***

### arrayRemove

Removes an element from an array at specified position.

**Parameters:**

* First parameter: Array
* `position`: Index, `start`, or `end` (optional, defaults to end)

**Usage:**

```handlebars theme={null}
{{arrayRemove (array 1 2 'three') position=1}}
{{arrayRemove (array 1 2 'three') position='start'}}
{{arrayRemove (array 1 2 'three') position='end'}}
{{arrayRemove (array 1 2 'three')}}
```

See [Miscellaneous Helpers](./misc-helpers#array-add--remove-helpers) for more details.

***

### arrayJoin

Concatenates array values with a separator.

**Parameters:**

* First parameter: Separator string
* Additional parameters: Values or array to join
* `prefix`: String to prepend (optional)
* `suffix`: String to append (optional)

**Usage:**

```handlebars theme={null}
{{arrayJoin ',' (array 'One' 'Two' 'Three')}}
{{arrayJoin ' - ' 'a' 'b' 'c'}}
{{arrayJoin ', ' (range 1 5)}}
{{arrayJoin ',' (array 'One' 'Two' 'Three') prefix='[' suffix=']'}}

{{#arrayJoin ',' myThings as |item|}}
{
  "name{{item.id}}": "{{item.name}}"
}
{{/arrayJoin}}

{{#arrayJoin ',' myThings prefix='[' suffix=']' as |item|}}
{
  "name{{item.id}}": "{{item.name}}"
}
{{/arrayJoin}}
```

See [Miscellaneous Helpers](./misc-helpers#arrayjoin-helper) for more details.

***

### hostname

Returns the hostname of the mock API.

**Usage:**

```handlebars theme={null}
{{hostname}}
```

***

## Conditional Logic Helpers

### if

Evaluates condition and renders block if true.

**Usage:**

```handlebars theme={null}
{{#if showDetails}}
  <div id="details">...</div>
{{/if}}

{{#if showVariantA}}
  <div id="var-a">...</div>
{{else if showVariantB}}
  <div id="var-b">...</div>
{{else}}
  <div id="default">...</div>
{{/if}}
```

See [Conditional Logic](./conditional-logic-and-iteration#conditional-logic-with-if--else-and-unless) for more details.

***

### unless

Evaluates condition and renders block if false.

**Usage:**

```handlebars theme={null}
{{#unless hideDetails}}
  <div id="details">...</div>
{{/unless}}
```

See [Conditional Logic](./conditional-logic-and-iteration#conditional-logic-with-if--else-and-unless) for more details.

***

### eq

Tests equality.

**Parameters:**

* First parameter: Left value
* Second parameter: Right value

**Usage:**

```handlebars theme={null}
{{#eq name 'Dan'}}
  <div id="dan">...</div>
{{/eq}}

{{#if (eq name 'Dan')}}
  <div id="dan">...</div>
{{/if}}
```

See [Conditional Logic](./conditional-logic-and-iteration#comparison-helpers) for more details.

***

### neq

Tests inequality.

**Parameters:**

* First parameter: Left value
* Second parameter: Right value

**Usage:**

```handlebars theme={null}
{{#neq name 'Jeff'}}...{{/neq}}
```

See [Conditional Logic](./conditional-logic-and-iteration#comparison-helpers) for more details.

***

### gt

Tests greater than.

**Parameters:**

* First parameter: Left value
* Second parameter: Right value

**Usage:**

```handlebars theme={null}
{{#gt itemCount 3}}...{{/gt}}
```

See [Conditional Logic](./conditional-logic-and-iteration#comparison-helpers) for more details.

***

### gte

Tests greater than or equal to.

**Parameters:**

* First parameter: Left value
* Second parameter: Right value

**Usage:**

```handlebars theme={null}
{{#gte itemCount 3}}...{{/gte}}
```

See [Conditional Logic](./conditional-logic-and-iteration#comparison-helpers) for more details.

***

### lt

Tests less than.

**Parameters:**

* First parameter: Left value
* Second parameter: Right value

**Usage:**

```handlebars theme={null}
{{#lt itemCount 3}}...{{/lt}}
```

See [Conditional Logic](./conditional-logic-and-iteration#comparison-helpers) for more details.

***

### lte

Tests less than or equal to.

**Parameters:**

* First parameter: Left value
* Second parameter: Right value

**Usage:**

```handlebars theme={null}
{{#lte itemCount 3}}...{{/lte}}
```

See [Conditional Logic](./conditional-logic-and-iteration#comparison-helpers) for more details.

***

### and

Logical AND operation.

**Parameters:**

* Multiple boolean expressions

**Usage:**

```handlebars theme={null}
{{#and (lt itemCount 10) (gt itemCount 5)}}...{{/and}}
```

See [Conditional Logic](./conditional-logic-and-iteration#comparison-helpers) for more details.

***

### or

Logical OR operation.

**Parameters:**

* Multiple boolean expressions

**Usage:**

```handlebars theme={null}
{{#or (eq itemCount 1) (eq itemCount 2)}}...{{/or}}
```

See [Conditional Logic](./conditional-logic-and-iteration#comparison-helpers) for more details.

***

### not

Logical NOT operation.

**Parameters:**

* One boolean expression

**Usage:**

```handlebars theme={null}
{{#not (eq itemCount 1)}}...{{/not}}
```

See [Conditional Logic](./conditional-logic-and-iteration#comparison-helpers) for more details.

***

### contains

Tests if string or array contains a value.

**Parameters:**

* First parameter: String or array
* Second parameter: Value to find

**Usage:**

```handlebars theme={null}
{{#if (contains 'abcde' 'abc')}}YES{{/if}}
{{#if (contains (array 'a' 'b' 'c') 'a')}}YES{{/if}}

{{#contains 'abcde' 'abc'}}YES{{/contains}}
{{#contains (array 'a' 'b' 'c') 'a'}}YES{{/contains}}
```

See [Conditional Logic](./conditional-logic-and-iteration#contains-helper) for more details.

***

### matches

Tests if string matches a regular expression.

**Parameters:**

* First parameter: String to test
* Second parameter: Regular expression pattern

**Usage:**

```handlebars theme={null}
{{#if (matches '123' '[0-9]+')}}YES{{/if}}

{{#matches '123' '[0-9]+'}}YES{{/matches}}
```

See [Conditional Logic](./conditional-logic-and-iteration#matches-helper) for more details.

***

## Iteration Helpers

### each

Iterates over collections (arrays or objects).

**Usage:**

```handlebars theme={null}
{{#each request.query.things as |thing|}}
  thing: {{{thing}}}
{{/each}}

{{#each (jsonPath request.body '$.things') as |value key|}}
  {{{key}}}={{{value}}}
{{/each}}

{{#each (range 0 5) as |index|}}
  {{@index}}: {{index}}
  {{#if @first}}First!{{/if}}
  {{#if @last}}Last!{{/if}}
{{/each}}
```

**Special variables:**

* `@index`: Current iteration index (zero-based)
* `@first`: True if first iteration
* `@last`: True if last iteration

See [Conditional Logic](./conditional-logic-and-iteration#iteration) for more details.

***


# Response Templating - Working with JSON
Source: https://docs.wiremock.io/response-templating/json

Working with JSON and JSONPath

## Extracting data with JSONPath

WireMock Cloud provides the `jsonPath` helper which will extract values from a JSON document
using the [JSONPath](https://github.com/json-path/JsonPath) expression language.

Similar in concept to XPath, JSONPath permits selection of individual values or sub-documents
via a query expression.

For example, given the JSON

```json theme={null}
{
  "outer": {
    "inner": "Stuff"
  }
}
```

The following will render "Stuff" into the output:

```handlebars theme={null}
{{jsonPath request.body '$.outer.inner'}}
```

And for the same JSON the following will render `{ "inner": "Stuff" }`:

```handlebars theme={null}
{{jsonPath request.body '$.outer'}}
```

## Iterating over JSON elements

The `jsonPath` helper outputs a "one or many" collection, which can either
be printed directly, or passed to further helpers such as [`each`](./conditional-logic-and-iteration/#iteration) or [`join`](./string-helpers/#join).

For instance, given a request body of the form:

```json theme={null}
{
  "things": [
    {
      "id": 1
    },
    {
      "id": 2
    },
    {
      "id": 3
    }
  ]
}
```

And the following response body template:

```handlebars theme={null}
{{#each (jsonPath request.body '$.things') as |thing|}}
thing: {{{thing.id}}}{{/each}}
```

The response body will contain:

```
thing: 1
thing: 2
thing: 3
```

The above will only work if the JSONPath expression selects an array from the
request JSON. However, `each` can also be used to iterate over maps/objects, so given
the request JSON:

```json theme={null}
{
  "things": {
    "one": 1,
    "two": 2,
    "three": 3
  }
}
```

And the template:

```handlebars theme={null}
{{#each (jsonPath request.body '$.things') as |value key|}}
{{{key}}}={{{value}}}{{/each}}
```

The output would contain:

```
one=1
two=2
three=3
```

## Adding to a JSON Array

The `jsonArrayAdd` helper allows you to append an element to an existing json array.

Its simplest form just takes two parameters, the array to append to and the item to be added:

```handlebars theme={null}
{{jsonArrayAdd existingArray newItem}}
```

The above template will produce the following JSON:

```json theme={null}
[
    {
        "id": 123,
        "name": "alice"
    },
    {
        "id": 321,
        "name": "sam"
    }
]
```

You can also use it in block form to parse the contents of the block as the new item to add:

```handlebars theme={null}
{{#jsonArrayAdd existingArray}}
{
  "id": 321,
  "name": "sam"
}
{{/jsonArrayAdd}}
```

It may be convenient to default the array to an empty array if it does not exist:

```handlebars theme={null}
{{#jsonArrayAdd (val existingArray or='[]')}}
{
  "id": 321,
  "name": "sam"
}
{{/jsonArrayAdd}}
```

The number of items in the array can be limited by using the `maxItems` parameter:

```handlebars theme={null}
{{#assign 'existingArray'}}
[
    {
        "id": 123,
        "name": "alice"
    },
    {
        "id": 321,
        "name": "sam"
    }
]
{{/assign}}

{{#jsonArrayAdd existingArray maxItems=2}}
{
    "id": 456,
    "name": "bob"
}
{{/jsonArrayAdd}}
```

The above template will produce the following JSON.  The first item in the array has been removed to maintain the
number of items in the array as specified by the `maxItems` parameter:

```json theme={null}
[
  {
    "id": 321,
    "name": "sam"
  },
  {
    "id": 456,
    "name": "bob"
  }
]
```

You can add arrays to the existing json array using this helper:

```handlebars theme={null}
{{#assign 'existingArray'}}
[
    {
        "id": 123,
        "name": "alice"
    },
    {
        "id": 321,
        "name": "sam"
    }
]
{{/assign}}

{{#jsonArrayAdd existingArray}}
[
    {
        "id": 456,
        "name": "bob"
    }
]
{{/jsonArrayAdd}}
```

The above template will produce the following JSON:

```json theme={null}
[
  {
    "id": 123,
    "name": "alice"
  },
  {
    "id": 321,
    "name": "sam"
  },
  [
    {
      "id": 456,
      "name": "bob"
    }
  ]
]
```

If you want the end result to be a single json array, you can use the `flatten` attribute:

```handlebars theme={null}
{{#assign 'existingArray'}}
[
    {
        "id": 123,
        "name": "alice"
    },
    {
        "id": 321,
        "name": "sam"
    }
]
{{/assign}}

{{#jsonArrayAdd existingArray flatten=true}}
[
    {
        "id": 456,
        "name": "bob"
    }
]
{{/jsonArrayAdd}}
```

The above template will produce the following JSON:

```json theme={null}
[
  {
    "id": 123,
    "name": "alice"
  },
  {
    "id": 321,
    "name": "sam"
  },
  {
    "id": 456,
    "name": "bob"
  }
]
```

You can use the `jsonArrayAdd` helper to add items to a nested array.  This is achieved using the `jsonPath` property
and referencing the array you want to add an item to:

```handlebars theme={null}
{{#assign 'existingArray'}}
[
    {
        "id": 123,
        "names":["alice", "sam"]
    },
    {
        "id": 321,
        "names":["fred", "neil"]
    }
]
{{/assign}}

{{#assign 'itemToAdd'}}"bob"{{/assign}}

{{jsonArrayAdd existingArray itemToAdd jsonPath='$[0].names'}}
```

The above template will produce the following JSON:

```json theme={null}
[
  {
    "id": 123,
    "names": [ "alice", "sam", "bob" ]
  },
  {
    "id": 321,
    "names": [ "fred", "neil" ]
  }
]
```

## Removing from a JSON Array or Object

The `jsonRemove` helper allows you to remove an element from an existing json array, or remove a key from an existing
json object, by identifying it using a [json path](https://datatracker.ietf.org/doc/rfc9535/) expression.

For instance, given an existing array like this:

```handlebars theme={null}
{{#assign 'existingArray'}}
[
  { "id": 456, "name": "bob"},
  { "id": 123, "name": "alice"},
  { "id": 321, "name": "sam"}
]
{{/assign}}
```

application of this helper, which selects the object with id `123`:

```handlebars theme={null}
{{jsonRemove existingArray '$.[?(@.id == 123)]'}}
```

will return this array:

```json theme={null}
[
  { "id": 456, "name": "bob"},
  { "id": 321, "name": "sam"}
]
```

Given an object like this:

```handlebars theme={null}
{{#assign 'existingObject'}}
{ "id": 456, "name": "bob"}
{{/assign}}
```

application of this helper, which selects the key `name`:

```handlebars theme={null}
{{jsonRemove existingObject '$.name'}}
```

will return this object:

```json theme={null}
{ "id": 456 }
```

## Merging JSON objects

The `jsonMerge` helper allows you to merge two json objects. Merging will recurse into any common keys where the values
are both objects, but not into any array values, where the value in the second object will overwrite that in the first.

Given these two objects:

```handlebars theme={null}
{{#assign 'object1'}}
{
  "id": 456, 
  "forename": "Robert",
  "surname": "Smith",
  "address": {
    "number": "12"
  },
  "hobbies": [ "chess", "football" ]
}
{{/assign}}
{{#assign 'object2'}}
{
  "name": "Robert",
  "nickname": "Bob",
  "address": {
    "street": "High Street"
  },
  "hobbies": [ "rugby" ]
}
{{/assign}}
```

```handlebars theme={null}
{{jsonMerge object1 object2}}
```

will return this object:

```json theme={null}
{
  "id": 456,
  "forename": "Robert",
  "surname": "Smith",
  "nickname": "Bob",
  "address": {
    "number": "12",
    "street": "High Street"
  },
  "hobbies": [ "rugby" ]
}
```

Like the `jsonArrayAdd` helper, the second object can be provided as a block:

```handlebars theme={null}
{{#jsonMerge object1}}
{
  "name": "Robert",
  "nickname": "Bob",
  "address": {
    "street": "High Street"
  },
  "hobbies": [ "rugby" ]
}
{{/jsonMerge}}
```

### Removing attributes

The `jsonMerge` helper has an optional `removeNulls` parameter which, when set to true will remove any attributes from the resulting JSON that
have null values in the second JSON document.

So for instance, given the following template:

```handlebars theme={null}
{{#assign 'object1'}}
{
    "keepMe": 1,
    "removeMe": 2
}
{{/assign}}

{{#jsonMerge object1 removeNulls=true}}
{
    "removeMe": null
}
{{/jsonMerge}}
```

The resulting JSON would be:

```json theme={null}
{
    "keepMe": 1
}
```

## Formatting JSON

The `formatJson` helper allows you to output JSON in either a pretty or a compact format. The default is pretty:

```handlebars theme={null}
{{#assign 'object1'}}
{"id": 456,
     "forename": "Robert", "surname": "Smith",
  "address": {
    "number": "12"
},
"hobbies": [ "chess", 
"football" ]
}
{{/assign}}
{{formatJson object1}}
```

emits:

```json theme={null}
{
  "id" : 456,
  "forename" : "Robert",
  "surname" : "Smith",
  "address" : {
    "number" : "12"
  },
  "hobbies" : [ "chess", "football" ]
}
```

Whereas

```handlebars theme={null}
{{formatJson object1 format='compact'}}
```

emits

```json theme={null}
{"id":456,"forename":"Robert","surname":"Smith","address":{"number":"12"},"hobbies":["chess","football"]}
```

The json to format can also be supplied as a block body:

```handlebars theme={null}
{{#formatJson}}
{"id": 456,
     "forename": "Robert", "surname": "Smith",
  "address": {
    "number": "12"
},
"hobbies": [ "chess", 
"football" ]
}
{{/formatJson}}
```

## Sorting JSON Arrays

The `jsonSort` helper allows you to specify a field within a JSON array to sort by.
The field is referenced using a JSON path expression, and all sort field values must be
of the same comparable type (Number, String, or Boolean).  For example:

```handlebars theme={null}
{{#assign 'jsonArray'}}
[
    {
        "id": 123,
        "name": "sam"
    },
    {
        "id": 321,
        "name": "alice"
    }
]
{{/assign}}

{{jsonSort jsonArray '$[*].name'}}
```

The above template will produce the following JSON:

```json theme={null}
[
  {
    "id": 321,
    "name": "alice"
  },
  {
    "id": 123,
    "name": "sam"
  }
]
```

The order of the sorting is `ascending (asc)` by default.  This can be changed by supplying `desc` for the `order` parameter.
For example:

```handlebars theme={null}
{{#assign 'jsonArray'}}
[
    {
        "id": 123,
        "name": "sam"
    },
    {
        "id": 321,
        "name": "alice"
    }
]
{{/assign}}

{{jsonSort jsonArray '$[*].id' order='desc'}}
```

The above template will produce the following JSON:

```json theme={null}
[
  {
    "id": 321,
    "name": "alice"
  },
  {
    "id": 123,
    "name": "sam"
  }
]
```

The array being referenced in the JSON path expression must be an array, but it doesn't have to be a top-level array.
For example:

```handlebars theme={null}
{{#assign 'jsonArray'}}
{"users":[{"name":"fred"},{"name":"bob"}]}
{{/assign}}

{{jsonSort jsonArray '$.users[*].name'}}
```

The above template will produce the following JSON:

```json theme={null}
{"users":[{"name":"bob"},{"name":"fred"}]}
```

Even though all sort field values must be of the same comparable type (Number, String, or Boolean), this equally works for
dates where they can be compared as strings. For example:

```handlebars theme={null}
{{#assign 'jsonArray'}}
[{"id":1,"created":"2025-03-15T14:30:00Z"},{"id":2,"created":"2025-01-10T09:15:00Z"},{"id":3,"created":"2025-12-01T18:45:00Z"}]
{{/assign}}

{{jsonSort jsonArray '$[*].created'}}
```

The above template will produce the following JSON:

```json theme={null}
 [{"id":2,"created":"2025-01-10T09:15:00Z"},{"id":1,"created":"2025-03-15T14:30:00Z"},{"id":3,"created":"2025-12-01T18:45:00Z"}]
```

Simple arrays can also be sorted using the `jsonSort` helper:

```handlebars theme={null}
{{#assign 'jsonArray'}}
["charlie","alice","bob"]
{{/assign}}

{{jsonSort jsonArray '$[*]'}}
```

The above template will produce the following JSON:

```json theme={null}
["alice","bob","charlie"]
```

You can also reference arrays in a specific index position using the `jsonPath` parameter:

```handlebars theme={null}
{{#assign 'jsonArray'}}
[{"items":[{"price":30},{"price":10},{"price":20}]},{"items":[{"price":100},{"price":50}]}]
{{/assign}}

{{jsonSort jsonArray '$[0].items[*].price'}}
```

The above template will produce the following JSON:

```json theme={null}
[{"items":[{"price":10},{"price":20},{"price":30}]},{"items":[{"price":100},{"price":50}]}]
```

### Handling null when sorting

The `jsonSort` helper allows you to sort on a field that can be missing or null. When
sorting, missing fields are treated as null.  By default, nulls are added to the
beginning of the sorted array:

```handlebars theme={null}
{{#assign 'jsonArray'}}
[{"id":1,"name":"alice"},{"id":2},{"id":3,"name":"bob"}]
{{/assign}}

{{jsonSort jsonArray '$[*].name'}}
```

The above template will produce the following JSON:

```json theme={null}
[{"id":2},{"id":1,"name":"alice"},{"id":3,"name":"bob"}]
```

This can be changed by supplying a `nulls` parameter and setting the value to `last` - `nulls='last'`.  This will
move nulls to the end of the sorted array:

```handlebars theme={null}
{{#assign 'jsonArray'}}
[{"id":1,"name":"alice"},{"id":2},{"id":3,"name":"bob"}]
{{/assign}}

{{jsonSort jsonArray '$[*].name' nulls='last'}}
```

The above template will produce the following JSON:

```json theme={null}
[{"id":1,"name":"alice"},{"id":3,"name":"bob"},{"id":2}]
```

The `nulls` parameter can also be set to `first` or `last`.

### Stable Sorting

The `jsonSort` helper provides a 'stable' sort where the order of equal values are preserved. For example, sorting on
a field that contains duplicate values will maintain the order within the array.  This is demonstrated in the following
example:

```handlebars theme={null}
{{#assign 'jsonArray'}}
[{"id":"a","score":100},{"id":"b","score":50},{"id":"c","score":50},{"id":"d","score":25},{"id":"e","score":50}]""";
{{/assign}}

{{jsonSort jsonArray '$[*].score'}}
```

The above template will produce the following JSON where the order of the duplicate items is preserved:

```json theme={null}
[{"id":"d","score":25},{"id":"b","score":50},{"id":"c","score":50},{"id":"e","score":50},{"id":"a","score":100}]
```

## Reading object as JSON

The `parseJson` helper will take the string value of the provided variable (or the contents of the block) and parse it
into an object or array, and assign it to the given variable.

e.g.

```handlebars theme={null}
{{#parseJson 'newVariableName'}}
    [ "shoes", "socks" ]
{{/parseJson}}
```

will add an array called `newVariableName` that can be used in subsequent helpers.

The contents to parse can also be supplied inline:

```handlebars theme={null}
{{#assign 'inputString'}}
    [ "shoes", "socks" ]
{{/assign}}
{{parseJson inputString 'newVariableName'}}
```

If no variable name is supplied the result of the parsing is output.

## Writing data as a JSON string

The `toJson` helper will convert any object into a JSON string.

```handlebars theme={null}
{{toJson (array 1 2 3)}}
```

emits

```json theme={null}
[ 1, 2, 3 ]
```


# Response Templating - JSON Web Tokens (JWT)
Source: https://docs.wiremock.io/response-templating/jwt

Working with JSON Web Tokens (JWTs)

Many modern APIs, in particular those concerned with authentication and authorization,
generate [JSON Web Tokens (JWTs)](https://jwt.io/) for their clients to use.

JWTs must be cryptographically signed in order to be valid, which means they cannot
be simply be generated using ordinary templating primitives. Signing can be via
one of a number of algorithms, but by far the two most common are `HS256` (shared secret)
and `RS256` (public/private key).

In order to enable creation of valid JWTs WireMock Cloud provides a pair of template helpers
specifically for this purpose: `jwt` and `jwks`.

Both `HS256` and `RS256` signed tokens are supported.

If you'd like to see these features in action, take a look at the [OAuth2 mock](../security/oauth2-mock/)
hosted by WireMock Cloud, which is also available to use as an template when creating your own mock API.

## Generating a token

You can generate a token in a stub response by enabling templating
and simply adding the following to the respobse body:

```handlebars theme={null}
{{{jwt maxAge='12 days'}}}
```

This will select defaults
for all the required values, set a 100 year expiry term and sign the token using `HS256` (shared secret).

### Expiry date

You can customise expiry term either by setting the `maxAge` parameter e.g.

```handlebars theme={null}
{{{jwt maxAge='12 days'}}}
```

or by setting an absolute expiry date e.g.

```handlebars theme={null}
{{{jwt exp=(parseDate '2040-02-23T21:22:23Z')}}}
```

You can similarly set the `nbf` (not before) date:

```handlebars theme={null}
{{{jwt nbf=(parseDate '2018-02-23T21:22:23Z')}}}
```

### Standard claims

Standard claims can be set as follows.

Issuer:

```handlebars theme={null}
{{{jwt iss='https://jwt-example.wiremockapi.cloud/'}}}
```

Audience:

```handlebars theme={null}
{{{jwt aud='https://jwt-target.wiremockapi.cloud/'}}}
```

Subject:

```handlebars theme={null}
{{{jwt sub='jonsmith'}}}
```

### Custom claims

You can also set any custom claim you wish via named parameters e.g.

```handlebars theme={null}
{{{jwt
    isAdmin=true
    quota=23
    score=0.96
    email='jonsmith@example.wiremockapi.cloud'
    signupDate=(parseDate '2017-01-02T03:04:05Z')
}}}
```

### Signing with RS256

By setting the `alg` parameter, the token can be signed using the public/private key
algorithm:

```handlebars theme={null}
{{{jwt alg='RS256'}}}
```

## Retrieving keys

For clients to be able to validate JWTs, they need to be able to retrieve either
the shared secret or the public key, depending on the signing algorithm.

### Getting all keys for your mock API

The keys used to sign tokens for a particular mock API can be retrieved via the
settings admin API resource. To fetch these via curl, you can do the following:

```
curl -H 'Authorization:Token <your WireMock Cloud API token>' https://your-mock-api.wiremockapi.cloud/__admin/settings
```

This will return a JSON document like this, from which you can retrieve the any of the
keys:

```json theme={null}
{
  "settings": {
    "extended": {
      "jwt": {
        "hs256Secret": "...",
        "rs256PublicKeyId": "...",
        "rs256PublicKey": "-----BEGIN RSA PUBLIC KEY-----\n...\n-----END RSA PUBLIC KEY-----\n",
        "rs256PrivateKey": "-----BEGIN RSA PRIVATE KEY-----\n...\n-----END RSA PRIVATE KEY-----\n"
      }
    }
  }
}
```

### The JSON Web Key Set (JWKS)

When using `RS256` (public/private key) signing, it is common for clients to fetch
the public key for verification via a JSON Web Key Set (JWKS) endpoint. You serve
a JWKS from your mock API simply by adding a stub containing the following response
body (with templating enabled):

```handlebars theme={null}
{{{jwks}}}
```


# Response Templating - Miscellaneous Helpers
Source: https://docs.wiremock.io/response-templating/misc-helpers

Other assorted useful helpers

This article describes some useful helpers that don't neatly fit into any of the other categories.

## Assignment

You can create a string variable of own using the `assign` helper, then use it
later in your template e.g.:

```handlebars theme={null}
{{#assign 'myCapitalisedQuery'}}{{capitalize request.query.search}}{{/assign}}

Capitalised query: {{myCapitalisedQuery}}
```

## Val helper

The `val` helper can be used to access values or provide a default if the value is not present. It can also be used to
assign a value to a variable much like the `assign` helper.  The main difference between `val` and `assign` is that `val`
will maintain the type of the date being assigned whereas `assign` will always assign a string.

```handlebars theme={null}
{{val request.query.search or='default'}} // the value of request.query.search or 'default' if it's not present
{{val request.query.search default='default'}} // the value of request.query.search or 'default' if it's not present
{{val request.query.search}} // the value of request.query.search or null if it's not present
{{val request.query.search or='default' assign='myVar'}} // assign the value of request.query.search or 'default' to myVar
{{val request.query.search assign='myVar'}} // assign the value of request.query.search to myVar


{{val (array 1 2 3) default='123'}} // [1, 2, 3]
{{val 'value for myVar' assign='myVar'}}{{myVar}} // value for myVar
{{val null or='other value for myVar' assign='myVar'}}{{myVar}} // other value for myVar
{{val 10 assign='myVar'}}{{#lt myVar 20}}Less Than{{else}}More Than{{/lt}} // Less Than
```

## Size

The `size` helper returns the size of a string, list or map:

```handlebars theme={null}
{{size 'abcde'}}               // Returns 5
{{size request.query.things}}  // Returns number of values in query param 'things'
```

## With

The `with` helper creates a nested scope, allowing you to reference attributes on
an object without fully qualifying it each time.

For instance, given a variable whose value is an object with the properties `id` and `position`,
`with` allows these to be accessed without qualifying each time:

```handlebars theme={null}
{{#with myObject}}
  ID: {{{id}}}
  Position: {{{position}}}
{{/with}}
```

## Range

The `range` helper emits an array of integers between the bounds specified in the
first and second parameters (both of which are mandatory).

```handlebars theme={null}
{{range 3 8}}
{{range -2 2}}
```

As mentioned above, you can use this with `randomInt` and `each` to output random length, repeating pieces of content e.g.

```handlebars theme={null}
{{#each (range 0 (randomInt lower=1 upper=10)) as |index|}}
id: {{index}}
{{/each}}
```

## Array

The `array` helper emits an array containing exactly the values specified as parameters.

```handlebars theme={null}
{{array 1 'two' true}}
```

Passing no parameters will result in an empty array being returned.

```handlebars theme={null}
{{array}}
```

## Array add & remove helpers

The `arrayAdd` and `arrayRemove` helpers can be used to add or remove elements from an array based on a position value
or the `start` or `end` keywords. If no position is specified, the element will be added or removed from the end of the
array.

```handlebars theme={null}
{{arrayAdd (array 1 'three') 2 position=1}} // [1, 2, three]
{{arrayAdd (array 1 'three') 2 position='start'}} // [2, 1, three]
{{arrayAdd (array 1 'three') 2 position='end'}} // [1, three, 2]
{{arrayAdd (array 1 'three') 2}} // [1, three, 2]

{{arrayRemove (array 1 2 'three') position=1}} // [1, three]
{{arrayRemove (array 1 2 'three') position='start'}} // [2, three]
{{arrayRemove (array 1 2 'three') position='end'}} // [1, 2]
{{arrayRemove (array 1 2 'three')}} // [1, 2]
```

## arrayJoin helper

The `arrayJoin` helper will concatenate the values passed to it with the separator specified:

```handlebars theme={null}
{{arrayJoin ',' (array 'One' 'Two' 'Three')}} // One,Two,Three
{{arrayJoin ' - ' 'a' 'b' 'c'}} // a - b - c
{{arrayJoin ', ' (range 1 5)}} // 1, 2, 3, 4, 5
{{arrayJoin (pickRandom ':') (array 'One' 'Two' 'Three')}} // One:Two:Three
{{arrayJoin '' (array 'W' 'i' 'r' 'e' 'M' 'o' 'c' 'k' ' ' 'R' 'o' 'c' 'k' 's')}} // WireMock Rocks
```

You can also specify a `prefix` and `suffix` to be added to the start and end of the result:

```handlebars theme={null}
{{arrayJoin ',' (array 'One' 'Two' 'Three') prefix='[' suffix=']'}} // [One,Two,Three]
{{arrayJoin ' * ' (array 1 2 3) prefix='(' suffix=')'}} // (1 * 2 * 3)
```

The `arrayJoin` helper can also be used as a block helper:

```handlebars theme={null}
{{#parseJson 'myThings'}}
[
  { "id": 1, "name": "One" },
  { "id": 2, "name": "Two" },
  { "id": 3, "name": "Three" }
]
{{/parseJson}}
[{{#arrayJoin ',' myThings as |item|}}
{
"name{{item.id}}": "{{item.name}}"
}
{{/arrayJoin}}] // [{ "name1": "One" }, { "name2": "Two" }, { "name3": "Three" }]


// or the same example with the prefix and suffix parameters
{{#parseJson 'myThings'}}
    [
    { "id": 1, "name": "One" },
    { "id": 2, "name": "Two" },
    { "id": 3, "name": "Three" }
    ]
{{/parseJson}}
{{#arrayJoin ',' myThings prefix='[' suffix=']' as |item|}}
    {
    "name{{item.id}}": "{{item.name}}"
    }
{{/arrayJoin}} // [{ "name1": "One" }, { "name2": "Two" }, { "name3": "Three" }]
```


# Response Templating - Number Helpers
Source: https://docs.wiremock.io/response-templating/number-helpers

Working with numbers

## Math helper

The `math` helper performs common arithmetic operations. It can accept integers, decimals
or strings as its operands and will always yield a number as its output rather than a string.

Addition, subtraction, multiplication, division and remainder (mod) are supported.

```handlebars theme={null}
{{math 1 '+' 2}}
{{math 4 '-' 2}}
{{math 2 '*' 3}}
{{math 8 '/' 2}}
{{math 10 '%' 3}}
```

## Formatting numbers

The `numberFormat` helper allows you to specify how numbers are printed. It supports
a number of predefined formats, custom format strings and various other options
including rounding mode, decimal places and locale.

### Predefined formats

`numberFormat` supports the following predefined formats:

* `integer`
* `currency`
* `percent`

Predefined formats can be affected by locale, so it's usually a good idea to explicitly
specify this.

For example, to format a decimal number as currency, specifically British pounds:

```handlebars theme={null}
{{{numberFormat 123.4567 'currency' 'en_GB'}}}
```

Output: `£123.46`.

Alternatively, if we wanted to output the number as a percentage:

```handlebars theme={null}
{{{numberFormat 123.4567 'percent' 'en_GB'}}}
```

Output: `12,346%`.

### Custom format string

For maximum control over the number format you can specify a format string:

```handlebars theme={null}
{{{numberFormat 123.4567 '###.000000' 'en_GB'}}}
```

Output: `123.456700`.

See the [Java DecimalFormat documentation](https://docs.oracle.com/javase/8/docs/api/java/text/DecimalFormat.html)
for details on how to use format strings.

### Configuring number of digits

Separate from the format parameter, the number of digits before and after the
decimal place can be bounded using one or more of four parameters:
`maximumFractionDigits`, `minimumFractionDigits`, `maximumIntegerDigits`, `minimumIntegerDigits`.

```handlebars theme={null}
{{{numberFormat 1234.567 maximumIntegerDigits=3 minimumFractionDigits=6}}}
```

Output: `234.567000`.

### Disabling grouping

By default `numberFormat` will insert commas, periods etc. per the locale between
groups of digits e.g. `1,234.5`.

This behaviour can be disabled with `groupingUsed`.

```handlebars theme={null}
{{{numberFormat 12345.678 groupingUsed=false}}}
```

Output: `12345.678`.

### Rounding mode

The `roundingMode` parameter affects how numbers will be rounded up or down when
it's necessary to do so.

For instance, to always round down:

```handlebars theme={null}
{{{numberFormat 1.239 roundingMode='down' maximumFractionDigits=2}}}
```

Output: `1.23`.

Available rounding modes are:

* `up`
* `down`
* `half_up`
* `half_down`
* `half_even`
* `ceiling`
* `floor`.

See the [Java RoundingMode documentation](https://docs.oracle.com/javase/8/docs/api/java/math/RoundingMode.html) for the exact meaning of each of these.


# Response Templating - Random Faker
Source: https://docs.wiremock.io/response-templating/random-faker

Generating random faker values

WireMock Cloud provides a helper to generate random values in a number of different categories.  The `random` helper
generates the random values based on the key provided.  The key is a string that represents the category of the random
value to generate.

## Getting started

To get started with the random faker generation, you first need to create a stub with dynamic response templating
enabled. Once you have response templating enabled, you can use the `random` helper to generate random values using the
following pattern in your stub responses:

```handlebars theme={null}
{{ random 'Name.firstName' }}
```

<img title="Random Faker Example" />

When you request the stub, the `random` helper will populate those fields with random values based on the key provided.
The above example will generate something that looks similar to the following output:

```json theme={null}
{
  "id": "b37f9d89c35a6a9d17f5555ffb5bd4646cdb096cd4bf2529dbc00a98b6d0be64",
  "username": "jarvis.gorczany",
  "name": "Dr. Magda Rohan",
  "email": "karol.orn@example.com",
  "ssn": "861-67-1370",
  "company": "Sanford LLC",
  "role": "Supervisor",
  "status": "Idle",
  "last_ip": "132.29.169.80",
  "address": "737 Burma Meadows, North Dolly, IA 37183",
  "phone": {
    "home": "+1 815-419-9640",
    "work": "(502) 606-4468 x3739",
    "mobile": "518-317-6223"
  },
  "avatar": "https://robohash.org/lcgrxnvh.png",
  "spirit_animal": "manatee",
  "favorite_color": "sky blue"
}
```

Every time you request the stub, the `random` helper will generate new random values for the fields based on the key.

## Reference

The following keys are supported for use with the `random` helper:

### Category - Base

#### Key - Address

```handlebars theme={null}
{{ random 'Address.state' }}
{{ random 'Address.country' }}
{{ random 'Address.streetName' }}
{{ random 'Address.zipCode' }}
{{ random 'Address.postcode' }}
{{ random 'Address.stateAbbr' }}
{{ random 'Address.citySuffix' }}
{{ random 'Address.cityPrefix' }}
{{ random 'Address.city' }}
{{ random 'Address.cityName' }}
{{ random 'Address.latitude' }}
{{ random 'Address.longitude' }}
{{ random 'Address.latLon' }}
{{ random 'Address.lonLat' }}
{{ random 'Address.timeZone' }}
{{ random 'Address.mailBox' }}
{{ random 'Address.streetAddressNumber' }}
{{ random 'Address.streetAddress' }}
{{ random 'Address.secondaryAddress' }}
{{ random 'Address.zipCodePlus4' }}
{{ random 'Address.streetSuffix' }}
{{ random 'Address.streetPrefix' }}
{{ random 'Address.countryCode' }}
{{ random 'Address.buildingNumber' }}
{{ random 'Address.fullAddress' }}
```

#### Key - Ancient

```handlebars theme={null}
{{ random 'Ancient.god' }}
{{ random 'Ancient.primordial' }}
{{ random 'Ancient.titan' }}
{{ random 'Ancient.hero' }}
```

#### Key - Animal

```handlebars theme={null}
{{ random 'Animal.name' }}
{{ random 'Animal.species' }}
{{ random 'Animal.genus' }}
{{ random 'Animal.scientificName' }}
```

#### Key - App

```handlebars theme={null}
{{ random 'App.name' }}
{{ random 'App.version' }}
{{ random 'App.author' }}
```

#### Key - Appliance

```handlebars theme={null}
{{ random 'Appliance.brand' }}
{{ random 'Appliance.equipment' }}
```

#### Key - Artist

```handlebars theme={null}
{{ random 'Artist.name' }}
```

#### Key - Australia

```handlebars theme={null}
{{ random 'Australia.locations' }}
{{ random 'Australia.animals' }}
{{ random 'Australia.states' }}
```

#### Key - Aviation

```handlebars theme={null}
{{ random 'Aviation.aircraft' }}
{{ random 'Aviation.airport' }}
{{ random 'Aviation.METAR' }}
{{ random 'Aviation.flight' }}
{{ random 'Aviation.airline' }}
```

#### Key - Aws

```handlebars theme={null}
{{ random 'Aws.region' }}
{{ random 'Aws.accountId' }}
{{ random 'Aws.acmARN' }}
{{ random 'Aws.albARN' }}
{{ random 'Aws.subnetId' }}
{{ random 'Aws.vpcId' }}
{{ random 'Aws.albTargetGroupARN' }}
{{ random 'Aws.route53ZoneId' }}
{{ random 'Aws.securityGroupId' }}
```

#### Key - Azure

```handlebars theme={null}
{{ random 'Azure.region' }}
{{ random 'Azure.tenantId' }}
{{ random 'Azure.firewall' }}
{{ random 'Azure.virtualWan' }}
{{ random 'Azure.serviceBus' }}
{{ random 'Azure.keyVault' }}
{{ random 'Azure.subscriptionId' }}
{{ random 'Azure.resourceGroup' }}
{{ random 'Azure.managementGroup' }}
{{ random 'Azure.applicationGateway' }}
{{ random 'Azure.bastionHost' }}
{{ random 'Azure.loadBalancer' }}
{{ random 'Azure.networkSecurityGroup' }}
{{ random 'Azure.virtualNetwork' }}
{{ random 'Azure.appServiceEnvironment' }}
{{ random 'Azure.appServicePlan' }}
{{ random 'Azure.loadTesting' }}
{{ random 'Azure.staticWebApp' }}
{{ random 'Azure.virtualMachine' }}
{{ random 'Azure.storageAccount' }}
{{ random 'Azure.containerRegistry' }}
{{ random 'Azure.containerApps' }}
{{ random 'Azure.containerAppsEnvironment' }}
{{ random 'Azure.containerInstance' }}
{{ random 'Azure.cosmosDBDatabase' }}
{{ random 'Azure.sqlDatabase' }}
{{ random 'Azure.mysqlDatabase' }}
{{ random 'Azure.postgreSQLDatabase' }}
{{ random 'Azure.serviceBusQueue' }}
{{ random 'Azure.serviceBusTopic' }}
{{ random 'Azure.logAnalytics' }}
```

#### Key - Barcode

```handlebars theme={null}
{{ random 'Barcode.type' }}
{{ random 'Barcode.ean8' }}
{{ random 'Barcode.gtin8' }}
{{ random 'Barcode.gtin13' }}
{{ random 'Barcode.ean13' }}
{{ random 'Barcode.gtin14' }}
{{ random 'Barcode.gtin12' }}
```

#### Key - BloodType

```handlebars theme={null}
{{ random 'BloodType.aboTypes' }}
{{ random 'BloodType.rhTypes' }}
{{ random 'BloodType.pTypes' }}
{{ random 'BloodType.bloodGroup' }}
```

#### Key - Book

```handlebars theme={null}
{{ random 'Book.title' }}
{{ random 'Book.author' }}
{{ random 'Book.publisher' }}
{{ random 'Book.genre' }}
```

#### Key - Bool

```handlebars theme={null}
{{ random 'Bool.bool' }}
```

#### Key - Business

```handlebars theme={null}
{{ random 'Business.creditCardNumber' }}
{{ random 'Business.creditCardType' }}
{{ random 'Business.creditCardExpiry' }}
{{ random 'Business.securityCode' }}
```

#### Key - CNPJ

```handlebars theme={null}
{{ random 'CNPJ.valid' }}
{{ random 'CNPJ.invalid' }}
```

#### Key - CPF

```handlebars theme={null}
{{ random 'CPF.valid' }}
{{ random 'CPF.invalid' }}
```

#### Key - Camera

```handlebars theme={null}
{{ random 'Camera.brand' }}
{{ random 'Camera.model' }}
{{ random 'Camera.brandWithModel' }}
```

#### Key - Cannabis

```handlebars theme={null}
{{ random 'Cannabis.types' }}
{{ random 'Cannabis.strains' }}
{{ random 'Cannabis.terpenes' }}
{{ random 'Cannabis.categories' }}
{{ random 'Cannabis.buzzwords' }}
{{ random 'Cannabis.brands' }}
{{ random 'Cannabis.cannabinoidAbbreviations' }}
{{ random 'Cannabis.cannabinoids' }}
{{ random 'Cannabis.medicalUses' }}
{{ random 'Cannabis.healthBenefits' }}
```

#### Key - Cat

```handlebars theme={null}
{{ random 'Cat.name' }}
{{ random 'Cat.breed' }}
{{ random 'Cat.registry' }}
```

#### Key - Chiquito

```handlebars theme={null}
{{ random 'Chiquito.terms' }}
{{ random 'Chiquito.sentences' }}
{{ random 'Chiquito.jokes' }}
{{ random 'Chiquito.expressions' }}
```

#### Key - Code

```handlebars theme={null}
{{ random 'Code.asin' }}
{{ random 'Code.isbnGs1' }}
{{ random 'Code.isbnGroup' }}
{{ random 'Code.isbn10' }}
{{ random 'Code.isbn13' }}
{{ random 'Code.imei' }}
{{ random 'Code.ean8' }}
{{ random 'Code.gtin8' }}
{{ random 'Code.gtin13' }}
{{ random 'Code.ean13' }}
{{ random 'Code.isbnRegistrant' }}
```

#### Key - Coin

```handlebars theme={null}
{{ random 'Coin.flip' }}
```

#### Key - Color

```handlebars theme={null}
{{ random 'Color.name' }}
{{ random 'Color.hex' }}
```

#### Key - Commerce

```handlebars theme={null}
{{ random 'Commerce.brand' }}
{{ random 'Commerce.department' }}
{{ random 'Commerce.material' }}
{{ random 'Commerce.vendor' }}
{{ random 'Commerce.price' }}
{{ random 'Commerce.productName' }}
{{ random 'Commerce.promotionCode' }}
```

#### Key - Community

```handlebars theme={null}
{{ random 'Community.quote' }}
{{ random 'Community.character' }}
```

#### Key - Company

```handlebars theme={null}
{{ random 'Company.name' }}
{{ random 'Company.bs' }}
{{ random 'Company.suffix' }}
{{ random 'Company.url' }}
{{ random 'Company.industry' }}
{{ random 'Company.profession' }}
{{ random 'Company.buzzword' }}
{{ random 'Company.logo' }}
{{ random 'Company.catchPhrase' }}
```

#### Key - Compass

```handlebars theme={null}
{{ random 'Compass.word' }}
{{ random 'Compass.azimuth' }}
{{ random 'Compass.abbreviation' }}
```

#### Key - Computer

```handlebars theme={null}
{{ random 'Computer.type' }}
{{ random 'Computer.platform' }}
{{ random 'Computer.linux' }}
{{ random 'Computer.macos' }}
{{ random 'Computer.windows' }}
{{ random 'Computer.operatingSystem' }}
```

#### Key - Construction

```handlebars theme={null}
{{ random 'Construction.materials' }}
{{ random 'Construction.roles' }}
{{ random 'Construction.trades' }}
{{ random 'Construction.heavyEquipment' }}
{{ random 'Construction.subcontractCategories' }}
{{ random 'Construction.standardCostCodes' }}
```

#### Key - Cosmere

```handlebars theme={null}
{{ random 'Cosmere.aons' }}
{{ random 'Cosmere.shards' }}
{{ random 'Cosmere.surges' }}
{{ random 'Cosmere.metals' }}
{{ random 'Cosmere.heralds' }}
{{ random 'Cosmere.sprens' }}
{{ random 'Cosmere.shardWorlds' }}
{{ random 'Cosmere.knightsRadiant' }}
{{ random 'Cosmere.allomancers' }}
{{ random 'Cosmere.feruchemists' }}
```

#### Key - Country

```handlebars theme={null}
{{ random 'Country.name' }}
{{ random 'Country.flag' }}
{{ random 'Country.currency' }}
{{ random 'Country.currencyCode' }}
{{ random 'Country.capital' }}
{{ random 'Country.countryCode2' }}
{{ random 'Country.countryCode3' }}
```

#### Key - CryptoCoin

```handlebars theme={null}
{{ random 'CryptoCoin.coin' }}
```

#### Key - CultureSeries

```handlebars theme={null}
{{ random 'CultureSeries.books' }}
{{ random 'CultureSeries.civs' }}
{{ random 'CultureSeries.planets' }}
{{ random 'CultureSeries.cultureShips' }}
{{ random 'CultureSeries.cultureShipClasses' }}
{{ random 'CultureSeries.cultureShipClassAbvs' }}
```

#### Key - Currency

```handlebars theme={null}
{{ random 'Currency.name' }}
{{ random 'Currency.code' }}
```

#### Key - DcComics

```handlebars theme={null}
{{ random 'DcComics.name' }}
{{ random 'DcComics.hero' }}
{{ random 'DcComics.heroine' }}
{{ random 'DcComics.villain' }}
{{ random 'DcComics.title' }}
```

#### Key - Demographic

```handlebars theme={null}
{{ random 'Demographic.race' }}
{{ random 'Demographic.demonym' }}
{{ random 'Demographic.sex' }}
{{ random 'Demographic.educationalAttainment' }}
{{ random 'Demographic.maritalStatus' }}
```

#### Key - Device

```handlebars theme={null}
{{ random 'Device.platform' }}
{{ random 'Device.modelName' }}
{{ random 'Device.serial' }}
{{ random 'Device.manufacturer' }}
```

#### Key - Disease

```handlebars theme={null}
{{ random 'Disease.ophthalmologyAndOtorhinolaryngology' }}
{{ random 'Disease.neurology' }}
{{ random 'Disease.surgery' }}
{{ random 'Disease.internalDisease' }}
{{ random 'Disease.paediatrics' }}
{{ random 'Disease.gynecologyAndObstetrics' }}
{{ random 'Disease.dermatolory' }}
```

#### Key - Dog

```handlebars theme={null}
{{ random 'Dog.name' }}
{{ random 'Dog.size' }}
{{ random 'Dog.breed' }}
{{ random 'Dog.sound' }}
{{ random 'Dog.memePhrase' }}
{{ random 'Dog.age' }}
{{ random 'Dog.coatLength' }}
{{ random 'Dog.gender' }}
```

#### Key - Drone

```handlebars theme={null}
{{ random 'Drone.name' }}
{{ random 'Drone.iso' }}
{{ random 'Drone.weight' }}
{{ random 'Drone.flightTime' }}
{{ random 'Drone.maxSpeed' }}
{{ random 'Drone.maxAscentSpeed' }}
{{ random 'Drone.maxDescentSpeed' }}
{{ random 'Drone.maxAltitude' }}
{{ random 'Drone.maxFlightDistance' }}
{{ random 'Drone.maxWindResistance' }}
{{ random 'Drone.maxAngularVelocity' }}
{{ random 'Drone.maxTiltAngle' }}
{{ random 'Drone.operatingTemperature' }}
{{ random 'Drone.batteryCapacity' }}
{{ random 'Drone.batteryVoltage' }}
{{ random 'Drone.batteryType' }}
{{ random 'Drone.batteryWeight' }}
{{ random 'Drone.chargingTemperature' }}
{{ random 'Drone.maxChargingPower' }}
{{ random 'Drone.maxResolution' }}
{{ random 'Drone.photoFormat' }}
{{ random 'Drone.videoFormat' }}
{{ random 'Drone.maxShutterSpeed' }}
{{ random 'Drone.minShutterSpeed' }}
{{ random 'Drone.shutterSpeedUnits' }}
```

#### Key - DungeonsAndDragons

```handlebars theme={null}
{{ random 'DungeonsAndDragons.alignments' }}
{{ random 'DungeonsAndDragons.cities' }}
{{ random 'DungeonsAndDragons.klasses' }}
{{ random 'DungeonsAndDragons.languages' }}
{{ random 'DungeonsAndDragons.monsters' }}
{{ random 'DungeonsAndDragons.races' }}
{{ random 'DungeonsAndDragons.backgrounds' }}
{{ random 'DungeonsAndDragons.meleeWeapons' }}
{{ random 'DungeonsAndDragons.rangedWeapons' }}
```

#### Key - Educator

```handlebars theme={null}
{{ random 'Educator.course' }}
{{ random 'Educator.campus' }}
{{ random 'Educator.university' }}
{{ random 'Educator.subjectWithNumber' }}
{{ random 'Educator.secondarySchool' }}
```

#### Key - EldenRing

```handlebars theme={null}
{{ random 'EldenRing.location' }}
{{ random 'EldenRing.weapon' }}
{{ random 'EldenRing.skill' }}
{{ random 'EldenRing.spell' }}
{{ random 'EldenRing.npc' }}
```

#### Key - ElectricalComponents

```handlebars theme={null}
{{ random 'ElectricalComponents.active' }}
{{ random 'ElectricalComponents.passive' }}
{{ random 'ElectricalComponents.electromechanical' }}
```

#### Key - Emoji

```handlebars theme={null}
{{ random 'Emoji.cat' }}
{{ random 'Emoji.smiley' }}
```

#### Key - FamousLastWords

```handlebars theme={null}
{{ random 'FamousLastWords.lastWords' }}
```

#### Key - File

```handlebars theme={null}
{{ random 'File.fileName' }}
{{ random 'File.extension' }}
{{ random 'File.mimeType' }}
```

#### Key - Finance

```handlebars theme={null}
{{ random 'Finance.nyseTicker' }}
{{ random 'Finance.creditCard' }}
{{ random 'Finance.bic' }}
{{ random 'Finance.iban' }}
{{ random 'Finance.nasdaqTicker' }}
{{ random 'Finance.stockMarket' }}
```

#### Key - FreshPrinceOfBelAir

```handlebars theme={null}
{{ random 'FreshPrinceOfBelAir.characters' }}
{{ random 'FreshPrinceOfBelAir.quotes' }}
{{ random 'FreshPrinceOfBelAir.celebrities' }}
```

#### Key - FunnyName

```handlebars theme={null}
{{ random 'FunnyName.name' }}
```

#### Key - GarmentSize

```handlebars theme={null}
{{ random 'GarmentSize.size' }}
```

#### Key - Gender

```handlebars theme={null}
{{ random 'Gender.types' }}
{{ random 'Gender.binaryTypes' }}
{{ random 'Gender.shortBinaryTypes' }}
```

#### Key - GratefulDead

```handlebars theme={null}
{{ random 'GratefulDead.players' }}
{{ random 'GratefulDead.songs' }}
```

#### Key - GreekPhilosopher

```handlebars theme={null}
{{ random 'GreekPhilosopher.name' }}
{{ random 'GreekPhilosopher.quote' }}
```

#### Key - Hacker

```handlebars theme={null}
{{ random 'Hacker.noun' }}
{{ random 'Hacker.ingverb' }}
{{ random 'Hacker.adjective' }}
{{ random 'Hacker.verb' }}
{{ random 'Hacker.abbreviation' }}
```

#### Key - Hashing

```handlebars theme={null}
{{ random 'Hashing.md2' }}
{{ random 'Hashing.md5' }}
{{ random 'Hashing.sha1' }}
{{ random 'Hashing.sha384' }}
{{ random 'Hashing.sha256' }}
{{ random 'Hashing.sha512' }}
```

#### Key - Hipster

```handlebars theme={null}
{{ random 'Hipster.word' }}
```

#### Key - Hobby

```handlebars theme={null}
{{ random 'Hobby.activity' }}
```

#### Key - Hololive

```handlebars theme={null}
{{ random 'Hololive.talent' }}
```

#### Key - Horse

```handlebars theme={null}
{{ random 'Horse.name' }}
{{ random 'Horse.breed' }}
```

#### Key - House

```handlebars theme={null}
{{ random 'House.room' }}
{{ random 'House.furniture' }}
```

#### Key - IdNumber

```handlebars theme={null}
{{ random 'IdNumber.valid' }}
{{ random 'IdNumber.invalid' }}
{{ random 'IdNumber.ssnValid' }}
{{ random 'IdNumber.validPtNif' }}
{{ random 'IdNumber.validSvSeSsn' }}
{{ random 'IdNumber.validEnZaSsn' }}
{{ random 'IdNumber.inValidEnZaSsn' }}
{{ random 'IdNumber.invalidSvSeSsn' }}
{{ random 'IdNumber.singaporeanFin' }}
{{ random 'IdNumber.singaporeanFinBefore2000' }}
{{ random 'IdNumber.singaporeanUin' }}
{{ random 'IdNumber.singaporeanUinBefore2000' }}
{{ random 'IdNumber.validZhCNSsn' }}
{{ random 'IdNumber.invalidPtNif' }}
{{ random 'IdNumber.validEsMXSsn' }}
{{ random 'IdNumber.invalidEsMXSsn' }}
{{ random 'IdNumber.peselNumber' }}
```

#### Key - IndustrySegments

```handlebars theme={null}
{{ random 'IndustrySegments.industry' }}
{{ random 'IndustrySegments.sector' }}
{{ random 'IndustrySegments.subSector' }}
{{ random 'IndustrySegments.superSector' }}
```

#### Key - Internet

```handlebars theme={null}
{{ random 'Internet.url' }}
{{ random 'Internet.port' }}
{{ random 'Internet.image' }}
{{ random 'Internet.domainWord' }}
{{ random 'Internet.httpMethod' }}
{{ random 'Internet.macAddress' }}
{{ random 'Internet.ipV4Cidr' }}
{{ random 'Internet.ipV6Cidr' }}
{{ random 'Internet.uuidv3' }}
{{ random 'Internet.userAgent' }}
{{ random 'Internet.slug' }}
{{ random 'Internet.uuid' }}
{{ random 'Internet.domainName' }}
{{ random 'Internet.password' }}
{{ random 'Internet.emailAddress' }}
{{ random 'Internet.safeEmailAddress' }}
{{ random 'Internet.ipV4Address' }}
{{ random 'Internet.getIpV4Address' }}
{{ random 'Internet.privateIpV4Address' }}
{{ random 'Internet.getPrivateIpV4Address' }}
{{ random 'Internet.publicIpV4Address' }}
{{ random 'Internet.getPublicIpV4Address' }}
{{ random 'Internet.ipV6Address' }}
{{ random 'Internet.getIpV6Address' }}
{{ random 'Internet.botUserAgentAny' }}
{{ random 'Internet.domainSuffix' }}
```

#### Key - Job

```handlebars theme={null}
{{ random 'Job.position' }}
{{ random 'Job.field' }}
{{ random 'Job.seniority' }}
{{ random 'Job.keySkills' }}
{{ random 'Job.title' }}
```

#### Key - Kpop

```handlebars theme={null}
{{ random 'Kpop.iGroups' }}
{{ random 'Kpop.iiGroups' }}
{{ random 'Kpop.iiiGroups' }}
{{ random 'Kpop.girlGroups' }}
{{ random 'Kpop.boyBands' }}
{{ random 'Kpop.solo' }}
```

#### Key - Lorem

```handlebars theme={null}
{{ random 'Lorem.words' }}
{{ random 'Lorem.word' }}
{{ random 'Lorem.character' }}
{{ random 'Lorem.sentence' }}
{{ random 'Lorem.paragraph' }}
{{ random 'Lorem.characters' }}
```

#### Key - Marketing

```handlebars theme={null}
{{ random 'Marketing.buzzwords' }}
```

#### Key - Matz

```handlebars theme={null}
{{ random 'Matz.quote' }}
```

#### Key - Mbti

```handlebars theme={null}
{{ random 'Mbti.name' }}
{{ random 'Mbti.type' }}
{{ random 'Mbti.personage' }}
{{ random 'Mbti.merit' }}
{{ random 'Mbti.weakness' }}
{{ random 'Mbti.characteristic' }}
```

#### Key - Measurement

```handlebars theme={null}
{{ random 'Measurement.length' }}
{{ random 'Measurement.height' }}
{{ random 'Measurement.weight' }}
{{ random 'Measurement.volume' }}
{{ random 'Measurement.metricHeight' }}
{{ random 'Measurement.metricLength' }}
{{ random 'Measurement.metricVolume' }}
{{ random 'Measurement.metricWeight' }}
```

#### Key - Medical

```handlebars theme={null}
{{ random 'Medical.symptoms' }}
{{ random 'Medical.medicineName' }}
{{ random 'Medical.diseaseName' }}
{{ random 'Medical.hospitalName' }}
{{ random 'Medical.diagnosisCode' }}
{{ random 'Medical.procedureCode' }}
```

#### Key - Military

```handlebars theme={null}
{{ random 'Military.armyRank' }}
{{ random 'Military.navyRank' }}
{{ random 'Military.marinesRank' }}
{{ random 'Military.airForceRank' }}
{{ random 'Military.dodPaygrade' }}
```

#### Key - Money

```handlebars theme={null}
{{ random 'Money.currency' }}
{{ random 'Money.currencyCode' }}
```

#### Key - Mood

```handlebars theme={null}
{{ random 'Mood.feeling' }}
{{ random 'Mood.emotion' }}
{{ random 'Mood.tone' }}
```

#### Key - Mountain

```handlebars theme={null}
{{ random 'Mountain.name' }}
{{ random 'Mountain.range' }}
```

#### Key - Mountaineering

```handlebars theme={null}
{{ random 'Mountaineering.mountaineer' }}
```

#### Key - Music

```handlebars theme={null}
{{ random 'Music.key' }}
{{ random 'Music.instrument' }}
{{ random 'Music.chord' }}
{{ random 'Music.genre' }}
```

#### Key - Name

```handlebars theme={null}
{{ random 'Name.name' }}
{{ random 'Name.prefix' }}
{{ random 'Name.suffix' }}
{{ random 'Name.lastName' }}
{{ random 'Name.fullName' }}
{{ random 'Name.firstName' }}
{{ random 'Name.title' }}
{{ random 'Name.username' }}
{{ random 'Name.nameWithMiddle' }}
```

#### Key - Nation

```handlebars theme={null}
{{ random 'Nation.flag' }}
{{ random 'Nation.language' }}
{{ random 'Nation.isoCountry' }}
{{ random 'Nation.nationality' }}
{{ random 'Nation.capitalCity' }}
{{ random 'Nation.isoLanguage' }}
```

#### Key - NatoPhoneticAlphabet

```handlebars theme={null}
{{ random 'NatoPhoneticAlphabet.codeWord' }}
```

#### Key - Nigeria

```handlebars theme={null}
{{ random 'Nigeria.name' }}
{{ random 'Nigeria.places' }}
{{ random 'Nigeria.schools' }}
{{ random 'Nigeria.food' }}
{{ random 'Nigeria.celebrities' }}
```

#### Key - Number

```handlebars theme={null}
{{ random 'Number.digit' }}
{{ random 'Number.negative' }}
{{ random 'Number.positive' }}
{{ random 'Number.randomDigit' }}
{{ random 'Number.randomDigitNotZero' }}
{{ random 'Number.randomNumber' }}
```

#### Key - Passport

```handlebars theme={null}
{{ random 'Passport.valid' }}
```

#### Key - PhoneNumber

```handlebars theme={null}
{{ random 'PhoneNumber.extension' }}
{{ random 'PhoneNumber.cellPhone' }}
{{ random 'PhoneNumber.phoneNumberInternational' }}
{{ random 'PhoneNumber.phoneNumberNational' }}
{{ random 'PhoneNumber.subscriberNumber' }}
{{ random 'PhoneNumber.phoneNumber' }}
```

#### Key - Photography

```handlebars theme={null}
{{ random 'Photography.iso' }}
{{ random 'Photography.brand' }}
{{ random 'Photography.genre' }}
{{ random 'Photography.lens' }}
{{ random 'Photography.imageTag' }}
{{ random 'Photography.aperture' }}
{{ random 'Photography.shutter' }}
{{ random 'Photography.camera' }}
{{ random 'Photography.term' }}
```

#### Key - ProgrammingLanguage

```handlebars theme={null}
{{ random 'ProgrammingLanguage.name' }}
{{ random 'ProgrammingLanguage.creator' }}
```

#### Key - Relationship

```handlebars theme={null}
{{ random 'Relationship.parent' }}
{{ random 'Relationship.inLaw' }}
{{ random 'Relationship.spouse' }}
{{ random 'Relationship.sibling' }}
```

#### Key - Restaurant

```handlebars theme={null}
{{ random 'Restaurant.name' }}
{{ random 'Restaurant.type' }}
{{ random 'Restaurant.description' }}
{{ random 'Restaurant.namePrefix' }}
{{ random 'Restaurant.nameSuffix' }}
{{ random 'Restaurant.review' }}
```

#### Key - Robin

```handlebars theme={null}
{{ random 'Robin.quote' }}
```

#### Key - RockBand

```handlebars theme={null}
{{ random 'RockBand.name' }}
```

#### Key - Science

```handlebars theme={null}
{{ random 'Science.element' }}
{{ random 'Science.unit' }}
{{ random 'Science.scientist' }}
{{ random 'Science.tool' }}
{{ random 'Science.quark' }}
{{ random 'Science.leptons' }}
{{ random 'Science.bosons' }}
{{ random 'Science.elementSymbol' }}
```

#### Key - Shakespeare

```handlebars theme={null}
{{ random 'Shakespeare.hamletQuote' }}
{{ random 'Shakespeare.asYouLikeItQuote' }}
{{ random 'Shakespeare.kingRichardIIIQuote' }}
{{ random 'Shakespeare.romeoAndJulietQuote' }}
```

#### Key - Sip

```handlebars theme={null}
{{ random 'Sip.method' }}
{{ random 'Sip.rtpPort' }}
{{ random 'Sip.bodyString' }}
{{ random 'Sip.bodyBytes' }}
{{ random 'Sip.contentType' }}
{{ random 'Sip.messagingPort' }}
{{ random 'Sip.provisionalResponseCode' }}
{{ random 'Sip.successResponseCode' }}
{{ random 'Sip.redirectResponseCode' }}
{{ random 'Sip.clientErrorResponseCode' }}
{{ random 'Sip.serverErrorResponseCode' }}
{{ random 'Sip.globalErrorResponseCode' }}
{{ random 'Sip.provisionalResponsePhrase' }}
{{ random 'Sip.successResponsePhrase' }}
{{ random 'Sip.redirectResponsePhrase' }}
{{ random 'Sip.clientErrorResponsePhrase' }}
{{ random 'Sip.serverErrorResponsePhrase' }}
{{ random 'Sip.globalErrorResponsePhrase' }}
{{ random 'Sip.nameAddress' }}
```

#### Key - Size

```handlebars theme={null}
{{ random 'Size.adjective' }}
```

#### Key - SlackEmoji

```handlebars theme={null}
{{ random 'SlackEmoji.people' }}
{{ random 'SlackEmoji.nature' }}
{{ random 'SlackEmoji.custom' }}
{{ random 'SlackEmoji.activity' }}
{{ random 'SlackEmoji.emoji' }}
{{ random 'SlackEmoji.foodAndDrink' }}
{{ random 'SlackEmoji.celebration' }}
{{ random 'SlackEmoji.travelAndPlaces' }}
{{ random 'SlackEmoji.objectsAndSymbols' }}
```

#### Key - Space

```handlebars theme={null}
{{ random 'Space.planet' }}
{{ random 'Space.moon' }}
{{ random 'Space.galaxy' }}
{{ random 'Space.nebula' }}
{{ random 'Space.star' }}
{{ random 'Space.agency' }}
{{ random 'Space.meteorite' }}
{{ random 'Space.company' }}
{{ random 'Space.starCluster' }}
{{ random 'Space.constellation' }}
{{ random 'Space.agencyAbbreviation' }}
{{ random 'Space.nasaSpaceCraft' }}
{{ random 'Space.distanceMeasurement' }}
```

#### Key - Stock

```handlebars theme={null}
{{ random 'Stock.nsdqSymbol' }}
{{ random 'Stock.nyseSymbol' }}
```

#### Key - Subscription

```handlebars theme={null}
{{ random 'Subscription.plans' }}
{{ random 'Subscription.statuses' }}
{{ random 'Subscription.paymentMethods' }}
{{ random 'Subscription.subscriptionTerms' }}
{{ random 'Subscription.paymentTerms' }}
```

#### Key - Superhero

```handlebars theme={null}
{{ random 'Superhero.name' }}
{{ random 'Superhero.prefix' }}
{{ random 'Superhero.suffix' }}
{{ random 'Superhero.descriptor' }}
{{ random 'Superhero.power' }}
```

#### Key - Team

```handlebars theme={null}
{{ random 'Team.name' }}
{{ random 'Team.state' }}
{{ random 'Team.sport' }}
{{ random 'Team.creature' }}
```

#### Key - Text

```handlebars theme={null}
{{ random 'Text.text' }}
{{ random 'Text.character' }}
{{ random 'Text.uppercaseCharacter' }}
{{ random 'Text.lowercaseCharacter' }}
```

#### Key - Tron

```handlebars theme={null}
{{ random 'Tron.location' }}
{{ random 'Tron.quote' }}
{{ random 'Tron.character' }}
{{ random 'Tron.game' }}
{{ random 'Tron.tagline' }}
{{ random 'Tron.vehicle' }}
{{ random 'Tron.alternateCharacterSpelling' }}
```

#### Key - Twitter

```handlebars theme={null}
{{ random 'Twitter.userName' }}
{{ random 'Twitter.userId' }}
```

#### Key - University

```handlebars theme={null}
{{ random 'University.name' }}
{{ random 'University.prefix' }}
{{ random 'University.suffix' }}
```

#### Key - Vehicle

```handlebars theme={null}
{{ random 'Vehicle.make' }}
{{ random 'Vehicle.color' }}
{{ random 'Vehicle.style' }}
{{ random 'Vehicle.vin' }}
{{ random 'Vehicle.upholstery' }}
{{ random 'Vehicle.driveType' }}
{{ random 'Vehicle.fuelType' }}
{{ random 'Vehicle.carType' }}
{{ random 'Vehicle.engine' }}
{{ random 'Vehicle.carOptions' }}
{{ random 'Vehicle.doors' }}
{{ random 'Vehicle.model' }}
{{ random 'Vehicle.manufacturer' }}
{{ random 'Vehicle.makeAndModel' }}
{{ random 'Vehicle.upholsteryColor' }}
{{ random 'Vehicle.upholsteryFabric' }}
{{ random 'Vehicle.transmission' }}
{{ random 'Vehicle.standardSpecs' }}
{{ random 'Vehicle.licensePlate' }}
```

#### Key - Verb

```handlebars theme={null}
{{ random 'Verb.base' }}
{{ random 'Verb.ingForm' }}
{{ random 'Verb.past' }}
{{ random 'Verb.pastParticiple' }}
{{ random 'Verb.simplePresent' }}
```

#### Key - Weather

```handlebars theme={null}
{{ random 'Weather.description' }}
{{ random 'Weather.temperatureCelsius' }}
{{ random 'Weather.temperatureFahrenheit' }}
```

#### Key - Yoda

```handlebars theme={null}
{{ random 'Yoda.quote' }}
```

### Category - Food

#### Key - Beer

```handlebars theme={null}
{{ random 'Beer.name' }}
{{ random 'Beer.style' }}
{{ random 'Beer.hop' }}
{{ random 'Beer.yeast' }}
{{ random 'Beer.malt' }}
```

#### Key - Coffee

```handlebars theme={null}
{{ random 'Coffee.descriptor' }}
{{ random 'Coffee.name1' }}
{{ random 'Coffee.name2' }}
{{ random 'Coffee.body' }}
{{ random 'Coffee.country' }}
{{ random 'Coffee.region' }}
{{ random 'Coffee.variety' }}
{{ random 'Coffee.notes' }}
{{ random 'Coffee.blendName' }}
{{ random 'Coffee.intensifier' }}
```

#### Key - Dessert

```handlebars theme={null}
{{ random 'Dessert.variety' }}
{{ random 'Dessert.topping' }}
{{ random 'Dessert.flavor' }}
```

#### Key - Food

```handlebars theme={null}
{{ random 'Food.ingredient' }}
{{ random 'Food.spice' }}
{{ random 'Food.dish' }}
{{ random 'Food.fruit' }}
{{ random 'Food.vegetable' }}
{{ random 'Food.sushi' }}
{{ random 'Food.measurement' }}
```

#### Key - Tea

```handlebars theme={null}
{{ random 'Tea.type' }}
{{ random 'Tea.variety' }}
```

### Category - Movie

#### Key - AquaTeenHungerForce

```handlebars theme={null}
{{ random 'AquaTeenHungerForce.character' }}
```

#### Key - Avatar

```handlebars theme={null}
{{ random 'Avatar.image' }}
```

#### Key - Babylon5

```handlebars theme={null}
{{ random 'Babylon5.quote' }}
{{ random 'Babylon5.character' }}
```

#### Key - BackToTheFuture

```handlebars theme={null}
{{ random 'BackToTheFuture.quote' }}
{{ random 'BackToTheFuture.date' }}
{{ random 'BackToTheFuture.character' }}
```

#### Key - BigBangTheory

```handlebars theme={null}
{{ random 'BigBangTheory.quote' }}
{{ random 'BigBangTheory.character' }}
```

#### Key - BojackHorseman

```handlebars theme={null}
{{ random 'BojackHorseman.characters' }}
{{ random 'BojackHorseman.quotes' }}
{{ random 'BojackHorseman.tongueTwisters' }}
```

#### Key - BossaNova

```handlebars theme={null}
{{ random 'BossaNova.artist' }}
{{ random 'BossaNova.song' }}
```

#### Key - BreakingBad

```handlebars theme={null}
{{ random 'BreakingBad.character' }}
{{ random 'BreakingBad.episode' }}
```

#### Key - BrooklynNineNine

```handlebars theme={null}
{{ random 'BrooklynNineNine.characters' }}
{{ random 'BrooklynNineNine.quotes' }}
```

#### Key - Buffy

```handlebars theme={null}
{{ random 'Buffy.characters' }}
{{ random 'Buffy.quotes' }}
{{ random 'Buffy.bigBads' }}
{{ random 'Buffy.episodes' }}
{{ random 'Buffy.celebrities' }}
```

#### Key - ChuckNorris

```handlebars theme={null}
{{ random 'ChuckNorris.fact' }}
```

#### Key - DarkSoul

```handlebars theme={null}
{{ random 'DarkSoul.classes' }}
{{ random 'DarkSoul.stats' }}
{{ random 'DarkSoul.covenants' }}
{{ random 'DarkSoul.shield' }}
```

#### Key - Departed

```handlebars theme={null}
{{ random 'Departed.quote' }}
{{ random 'Departed.character' }}
{{ random 'Departed.actor' }}
```

#### Key - DetectiveConan

```handlebars theme={null}
{{ random 'DetectiveConan.characters' }}
{{ random 'DetectiveConan.gadgets' }}
{{ random 'DetectiveConan.vehicles' }}
```

#### Key - DoctorWho

```handlebars theme={null}
{{ random 'DoctorWho.quote' }}
{{ random 'DoctorWho.character' }}
{{ random 'DoctorWho.species' }}
{{ random 'DoctorWho.actor' }}
{{ random 'DoctorWho.villain' }}
{{ random 'DoctorWho.doctor' }}
{{ random 'DoctorWho.catchPhrase' }}
```

#### Key - Doraemon

```handlebars theme={null}
{{ random 'Doraemon.location' }}
{{ random 'Doraemon.character' }}
{{ random 'Doraemon.gadget' }}
```

#### Key - DragonBall

```handlebars theme={null}
{{ random 'DragonBall.character' }}
```

#### Key - DumbAndDumber

```handlebars theme={null}
{{ random 'DumbAndDumber.quote' }}
{{ random 'DumbAndDumber.character' }}
{{ random 'DumbAndDumber.actor' }}
```

#### Key - Dune

```handlebars theme={null}
{{ random 'Dune.quote' }}
{{ random 'Dune.character' }}
{{ random 'Dune.title' }}
{{ random 'Dune.planet' }}
{{ random 'Dune.saying' }}
```

#### Key - FamilyGuy

```handlebars theme={null}
{{ random 'FamilyGuy.location' }}
{{ random 'FamilyGuy.quote' }}
{{ random 'FamilyGuy.character' }}
```

#### Key - FinalSpace

```handlebars theme={null}
{{ random 'FinalSpace.quote' }}
{{ random 'FinalSpace.character' }}
{{ random 'FinalSpace.vehicle' }}
```

#### Key - Friends

```handlebars theme={null}
{{ random 'Friends.location' }}
{{ random 'Friends.quote' }}
{{ random 'Friends.character' }}
```

#### Key - FullmetalAlchemist

```handlebars theme={null}
{{ random 'FullmetalAlchemist.country' }}
{{ random 'FullmetalAlchemist.character' }}
{{ random 'FullmetalAlchemist.city' }}
```

#### Key - GameOfThrones

```handlebars theme={null}
{{ random 'GameOfThrones.quote' }}
{{ random 'GameOfThrones.character' }}
{{ random 'GameOfThrones.city' }}
{{ random 'GameOfThrones.house' }}
{{ random 'GameOfThrones.dragon' }}
```

#### Key - Ghostbusters

```handlebars theme={null}
{{ random 'Ghostbusters.quote' }}
{{ random 'Ghostbusters.character' }}
{{ random 'Ghostbusters.actor' }}
```

#### Key - HarryPotter

```handlebars theme={null}
{{ random 'HarryPotter.location' }}
{{ random 'HarryPotter.quote' }}
{{ random 'HarryPotter.character' }}
{{ random 'HarryPotter.spell' }}
{{ random 'HarryPotter.book' }}
{{ random 'HarryPotter.house' }}
```

#### Key - HeyArnold

```handlebars theme={null}
{{ random 'HeyArnold.locations' }}
{{ random 'HeyArnold.characters' }}
{{ random 'HeyArnold.quotes' }}
```

#### Key - HitchhikersGuideToTheGalaxy

```handlebars theme={null}
{{ random 'HitchhikersGuideToTheGalaxy.location' }}
{{ random 'HitchhikersGuideToTheGalaxy.quote' }}
{{ random 'HitchhikersGuideToTheGalaxy.character' }}
{{ random 'HitchhikersGuideToTheGalaxy.species' }}
{{ random 'HitchhikersGuideToTheGalaxy.planet' }}
{{ random 'HitchhikersGuideToTheGalaxy.starship' }}
{{ random 'HitchhikersGuideToTheGalaxy.marvinQuote' }}
```

#### Key - Hobbit

```handlebars theme={null}
{{ random 'Hobbit.location' }}
{{ random 'Hobbit.quote' }}
{{ random 'Hobbit.character' }}
{{ random 'Hobbit.thorinsCompany' }}
```

#### Key - HowIMetYourMother

```handlebars theme={null}
{{ random 'HowIMetYourMother.quote' }}
{{ random 'HowIMetYourMother.character' }}
{{ random 'HowIMetYourMother.highFive' }}
{{ random 'HowIMetYourMother.catchPhrase' }}
```

#### Key - Kaamelott

```handlebars theme={null}
{{ random 'Kaamelott.quote' }}
{{ random 'Kaamelott.character' }}
```

#### Key - Lebowski

```handlebars theme={null}
{{ random 'Lebowski.quote' }}
{{ random 'Lebowski.character' }}
{{ random 'Lebowski.actor' }}
```

#### Key - LordOfTheRings

```handlebars theme={null}
{{ random 'LordOfTheRings.location' }}
{{ random 'LordOfTheRings.character' }}
```

#### Key - MoneyHeist

```handlebars theme={null}
{{ random 'MoneyHeist.quote' }}
{{ random 'MoneyHeist.character' }}
{{ random 'MoneyHeist.heist' }}
```

#### Key - Movie

```handlebars theme={null}
{{ random 'Movie.quote' }}
```

#### Key - OnePiece

```handlebars theme={null}
{{ random 'OnePiece.location' }}
{{ random 'OnePiece.quote' }}
{{ random 'OnePiece.character' }}
{{ random 'OnePiece.sea' }}
{{ random 'OnePiece.island' }}
{{ random 'OnePiece.akumasNoMi' }}
```

#### Key - OscarMovie

```handlebars theme={null}
{{ random 'OscarMovie.quote' }}
{{ random 'OscarMovie.getYear' }}
{{ random 'OscarMovie.character' }}
{{ random 'OscarMovie.actor' }}
{{ random 'OscarMovie.getChoice' }}
{{ random 'OscarMovie.movieName' }}
{{ random 'OscarMovie.releaseDate' }}
```

#### Key - Pokemon

```handlebars theme={null}
{{ random 'Pokemon.name' }}
{{ random 'Pokemon.type' }}
{{ random 'Pokemon.location' }}
{{ random 'Pokemon.move' }}
```

#### Key - PrincessBride

```handlebars theme={null}
{{ random 'PrincessBride.quote' }}
{{ random 'PrincessBride.character' }}
```

#### Key - ResidentEvil

```handlebars theme={null}
{{ random 'ResidentEvil.location' }}
{{ random 'ResidentEvil.character' }}
{{ random 'ResidentEvil.equipment' }}
{{ random 'ResidentEvil.creature' }}
{{ random 'ResidentEvil.biologicalAgent' }}
```

#### Key - RickAndMorty

```handlebars theme={null}
{{ random 'RickAndMorty.location' }}
{{ random 'RickAndMorty.quote' }}
{{ random 'RickAndMorty.character' }}
```

#### Key - RuPaulDragRace

```handlebars theme={null}
{{ random 'RuPaulDragRace.quote' }}
{{ random 'RuPaulDragRace.queen' }}
```

#### Key - Seinfeld

```handlebars theme={null}
{{ random 'Seinfeld.quote' }}
{{ random 'Seinfeld.character' }}
{{ random 'Seinfeld.business' }}
```

#### Key - Simpsons

```handlebars theme={null}
{{ random 'Simpsons.location' }}
{{ random 'Simpsons.quote' }}
{{ random 'Simpsons.character' }}
```

#### Key - StarTrek

```handlebars theme={null}
{{ random 'StarTrek.location' }}
{{ random 'StarTrek.character' }}
{{ random 'StarTrek.species' }}
{{ random 'StarTrek.villain' }}
{{ random 'StarTrek.klingon' }}
```

#### Key - StarWars

```handlebars theme={null}
{{ random 'StarWars.character' }}
{{ random 'StarWars.species' }}
{{ random 'StarWars.planets' }}
{{ random 'StarWars.quotes' }}
{{ random 'StarWars.callSign' }}
{{ random 'StarWars.vehicles' }}
{{ random 'StarWars.droids' }}
{{ random 'StarWars.alternateCharacterSpelling' }}
{{ random 'StarWars.wookieWords' }}
```

#### Key - StudioGhibli

```handlebars theme={null}
{{ random 'StudioGhibli.quote' }}
{{ random 'StudioGhibli.character' }}
{{ random 'StudioGhibli.movie' }}
```

#### Key - TheItCrowd

```handlebars theme={null}
{{ random 'TheItCrowd.characters' }}
{{ random 'TheItCrowd.quotes' }}
{{ random 'TheItCrowd.actors' }}
{{ random 'TheItCrowd.emails' }}
```

#### Key - TwinPeaks

```handlebars theme={null}
{{ random 'TwinPeaks.location' }}
{{ random 'TwinPeaks.quote' }}
{{ random 'TwinPeaks.character' }}
```

#### Key - Witcher

```handlebars theme={null}
{{ random 'Witcher.location' }}
{{ random 'Witcher.sign' }}
{{ random 'Witcher.quote' }}
{{ random 'Witcher.character' }}
{{ random 'Witcher.witcher' }}
{{ random 'Witcher.school' }}
{{ random 'Witcher.monster' }}
{{ random 'Witcher.potion' }}
{{ random 'Witcher.book' }}
```

### Category - Sport

#### Key - Baseball

```handlebars theme={null}
{{ random 'Baseball.positions' }}
{{ random 'Baseball.players' }}
{{ random 'Baseball.teams' }}
{{ random 'Baseball.coaches' }}
```

#### Key - Basketball

```handlebars theme={null}
{{ random 'Basketball.positions' }}
{{ random 'Basketball.players' }}
{{ random 'Basketball.teams' }}
{{ random 'Basketball.coaches' }}
```

#### Key - Cricket

```handlebars theme={null}
{{ random 'Cricket.formats' }}
{{ random 'Cricket.players' }}
{{ random 'Cricket.teams' }}
{{ random 'Cricket.tournaments' }}
```

#### Key - EnglandFootBall

```handlebars theme={null}
{{ random 'EnglandFootBall.team' }}
{{ random 'EnglandFootBall.league' }}
```

#### Key - Football

```handlebars theme={null}
{{ random 'Football.positions' }}
{{ random 'Football.players' }}
{{ random 'Football.teams' }}
{{ random 'Football.coaches' }}
{{ random 'Football.competitions' }}
```

#### Key - Formula1

```handlebars theme={null}
{{ random 'Formula1.team' }}
{{ random 'Formula1.driver' }}
{{ random 'Formula1.circuit' }}
{{ random 'Formula1.grandPrix' }}
```

#### Key - Volleyball

```handlebars theme={null}
{{ random 'Volleyball.position' }}
{{ random 'Volleyball.team' }}
{{ random 'Volleyball.player' }}
{{ random 'Volleyball.coach' }}
{{ random 'Volleyball.formation' }}
```

### Category - Video Games

#### Key - Battlefield1

```handlebars theme={null}
{{ random 'Battlefield1.map' }}
{{ random 'Battlefield1.classes' }}
{{ random 'Battlefield1.weapon' }}
{{ random 'Battlefield1.vehicle' }}
{{ random 'Battlefield1.faction' }}
```

#### Key - ClashOfClans

```handlebars theme={null}
{{ random 'ClashOfClans.troop' }}
{{ random 'ClashOfClans.rank' }}
{{ random 'ClashOfClans.defensiveBuilding' }}
```

#### Key - Control

```handlebars theme={null}
{{ random 'Control.location' }}
{{ random 'Control.quote' }}
{{ random 'Control.character' }}
{{ random 'Control.hiss' }}
{{ random 'Control.theBoard' }}
{{ random 'Control.objectOfPower' }}
{{ random 'Control.alteredItem' }}
{{ random 'Control.alteredWorldEvent' }}
```

#### Key - ElderScrolls

```handlebars theme={null}
{{ random 'ElderScrolls.quote' }}
{{ random 'ElderScrolls.lastName' }}
{{ random 'ElderScrolls.region' }}
{{ random 'ElderScrolls.race' }}
{{ random 'ElderScrolls.creature' }}
{{ random 'ElderScrolls.firstName' }}
{{ random 'ElderScrolls.city' }}
{{ random 'ElderScrolls.dragon' }}
```

#### Key - Esports

```handlebars theme={null}
{{ random 'Esports.event' }}
{{ random 'Esports.game' }}
{{ random 'Esports.team' }}
{{ random 'Esports.player' }}
{{ random 'Esports.league' }}
```

#### Key - Fallout

```handlebars theme={null}
{{ random 'Fallout.location' }}
{{ random 'Fallout.quote' }}
{{ random 'Fallout.character' }}
{{ random 'Fallout.faction' }}
```

#### Key - Hearthstone

```handlebars theme={null}
{{ random 'Hearthstone.wildRank' }}
{{ random 'Hearthstone.mainProfession' }}
{{ random 'Hearthstone.mainCharacter' }}
{{ random 'Hearthstone.mainPattern' }}
{{ random 'Hearthstone.battlegroundsScore' }}
{{ random 'Hearthstone.standardRank' }}
```

#### Key - HeroesOfTheStorm

```handlebars theme={null}
{{ random 'HeroesOfTheStorm.quote' }}
{{ random 'HeroesOfTheStorm.hero' }}
{{ random 'HeroesOfTheStorm.heroClass' }}
{{ random 'HeroesOfTheStorm.battleground' }}
```

#### Key - LeagueOfLegends

```handlebars theme={null}
{{ random 'LeagueOfLegends.location' }}
{{ random 'LeagueOfLegends.quote' }}
{{ random 'LeagueOfLegends.rank' }}
{{ random 'LeagueOfLegends.champion' }}
{{ random 'LeagueOfLegends.masteries' }}
{{ random 'LeagueOfLegends.summonerSpell' }}
```

#### Key - MassEffect

```handlebars theme={null}
{{ random 'MassEffect.quote' }}
{{ random 'MassEffect.character' }}
{{ random 'MassEffect.planet' }}
{{ random 'MassEffect.specie' }}
{{ random 'MassEffect.cluster' }}
```

#### Key - Minecraft

```handlebars theme={null}
{{ random 'Minecraft.itemName' }}
{{ random 'Minecraft.tileName' }}
{{ random 'Minecraft.entityName' }}
{{ random 'Minecraft.animalName' }}
{{ random 'Minecraft.monsterName' }}
{{ random 'Minecraft.tileItemName' }}
```

#### Key - Overwatch

```handlebars theme={null}
{{ random 'Overwatch.location' }}
{{ random 'Overwatch.quote' }}
{{ random 'Overwatch.hero' }}
```

#### Key - SoulKnight

```handlebars theme={null}
{{ random 'SoulKnight.characters' }}
{{ random 'SoulKnight.buffs' }}
{{ random 'SoulKnight.statues' }}
{{ random 'SoulKnight.weapons' }}
{{ random 'SoulKnight.bosses' }}
{{ random 'SoulKnight.enemies' }}
```

#### Key - StarCraft

```handlebars theme={null}
{{ random 'StarCraft.unit' }}
{{ random 'StarCraft.character' }}
{{ random 'StarCraft.planet' }}
{{ random 'StarCraft.building' }}
```

#### Key - SuperMario

```handlebars theme={null}
{{ random 'SuperMario.locations' }}
{{ random 'SuperMario.games' }}
{{ random 'SuperMario.characters' }}
```

#### Key - Touhou

```handlebars theme={null}
{{ random 'Touhou.trackName' }}
{{ random 'Touhou.gameName' }}
{{ random 'Touhou.characterName' }}
{{ random 'Touhou.characterFirstName' }}
{{ random 'Touhou.characterLastName' }}
```

#### Key - Zelda

```handlebars theme={null}
{{ random 'Zelda.character' }}
{{ random 'Zelda.game' }}
```


# Response Templating - Random Values
Source: https://docs.wiremock.io/response-templating/random-values

Generating random values

WireMock Cloud provides two random value helpers - `randomValue` and `pickRandom`.

## Random strings

The `randomValue` helper generates random strings of a specific type and length.
Optionally, values containing alphabetic characters can be made upper case via the `uppercase` parameter.

```handlebars theme={null}
{{randomValue length=33 type='ALPHANUMERIC'}}

{{randomValue length=12 type='ALPHANUMERIC' uppercase=true}}

{{randomValue length=55 type='ALPHABETIC'}}

{{randomValue length=27 type='ALPHABETIC' uppercase=true}}

{{randomValue length=10 type='NUMERIC'}}

{{randomValue length=5 type='ALPHANUMERIC_AND_SYMBOLS'}}

{{randomValue length=5 type='HEXADECIMAL' uppercase=true}}

{{randomValue type='UUID'}}
```

## Random numbers

While the `randomValue` helper can generate a number as a string when type `NUMERIC` is requested,
sometimes it can be useful to emit an actual typed number with the ability to control
lower and upper bounds. Working with numbers this way supports further processing
with the `math` helper or can serve as input to the `range` helper, among other uses.

The `randomInt` helper emits random integers with one, both or neither bound specified.

```handlebars theme={null}
{{randomInt}}
{{randomInt lower=5 upper=9}}
{{randomInt upper=54323}}
{{randomInt lower=-24}}
```

Likewise `randomDecimal` will emit random decimals:

```handlebars theme={null}
{{randomDecimal}}
{{randomDecimal lower=-10.1 upper=-0.9}}
{{randomDecimal upper=12.5}}
{{randomDecimal lower=-24.01}}
```

## Pick random

The `pickRandom` helper randomly selects a value from its parameters.

If the first parameter is a collection then the value will be randomly selected
from within this:

```handlebars theme={null}
{{#parseJson 'numberList'}}
    [1,2,3]
{{/parseJson}}

{{pickRandom numberList}} // One of 1, 2 or 3
```

Otherwise a value will be picked from the list of parameters provided:

```handlebars theme={null}
{{pickRandom '1' '2' '3'}} // One of 1, 2 or 3
```

If you desire multiple unique elements to be randomly pulled from the list, a `count` option can be supplied to the
helper.
In this case, the result will be a list, instead of a single value.
For example, the following template:

```
{{pickRandom 1 2 3 4 5 count=3}}
```

will produce a list similar to the following:

```
[3, 5, 2]
```


# Request Model Reference
Source: https://docs.wiremock.io/response-templating/request-model

Complete reference for accessing request data in templates

When templates are evaluated, they have access to a data model that represents the incoming HTTP request. This page provides a complete reference of all available request attributes and how to access them in your templates.

## The Request Object

The data model supplied to response templates contains a single top-level object called `request` which represents the incoming HTTP request. All request attributes are accessed as properties of this object.

## URL Attributes

### request.url

The full URL path and query string.

**Example:** `/products/123?color=red&size=large`

### request.path

The URL path without query parameters.

**Example:** `/products/123`

### request.path.\[n]

Individual URL path segments, accessed by zero-based index.

**Example:** For path `/api/products/123`, `request.path.[2]` returns `123`

## Query Parameters

### request.query.key

The values for a specific query parameter.

**Example:** `request.query.search` returns `laptop` for `?search=laptop`

<Warning>
  Referencing a query parameter in this manner will return a list of values, but as a convenience only the first will be printed.
  As a general rule if you wish to use the first (or only) value of a query parameter in a further expression rather than printing it,
  it is necessary to reference it by index explicitly as shown below e.g. `request.query.productId.[0]`
</Warning>

### request.query.key.\[n]

nth value of a query parameter (zero-indexed), for parameters with multiple values.

**Example:** `request.query.tags.[1]` returns `electronics` for `?tags=new&tags=electronics`

## HTTP Method and Protocol

### request.method

The HTTP request method.

**Example:** `POST`, `GET`, `PUT`, `DELETE`

### request.scheme

The protocol part of the URL.

**Example:** `https`, `http`

## Host and Port

### request.host

The hostname part of the URL.

**Example:** `api.example.com`

### request.port

The port number.

**Example:** `8080`, `443`

### request.baseUrl

The full URL up to the start of the path, including scheme, host, and port.

**Example:** `https://api.example.com:8080`

## Headers

### request.headers.key

First value of a request header. Header names are case-insensitive.

**Example:** `request.headers.X-Request-Id` or `request.headers.Content-Type`

<Warning>
  Referencing a header in this manner will return a list of values, but as a convenience only the first will be printed.
  As a general rule if you wish to use the first (or only) value of a header in a further expression rather than printing it,
  it is necessary to reference it by index explicitly as shown below e.g. `request.headers.X-Proxied-Via.[0]`
</Warning>

### request.headers.\[key]

Alternative syntax for headers with special characters that aren't valid in property names.

**Example:** `request.headers.[$?blah]`

### request.headers.key.\[n]

nth value of a header (zero-indexed), for headers with multiple values.

**Example:** `request.headers.Accept.[1]`

## Cookies

### request.cookies.key

First value of a request cookie.

**Example:** `request.cookies.JSESSIONID`

<Warning>
  Referencing a cookie in this manner will return a list of values, but as a convenience only the first will be printed.
  As a general rule if you wish to use the first (or only) value of a cookie in a further expression rather than printing it,
  it is necessary to reference it by index explicitly as shown below e.g. `request.cookies.X-Proxied-Via.[0]`
</Warning>

### request.cookies.key.\[n]

nth value of a cookie (zero-indexed), for cookies with multiple values.

**Example:** `request.cookies.tracking.[2]`

## Request Body

### request.body

The request body as text. Avoid using this for binary content.

**Example:** For JSON request body, `request.body` contains the raw JSON string

### request.bodyAsBase64

The Base64-encoded representation of the request body. Use this for binary content.

## Request Identity

### request.id

A random UUID assigned by WireMock Cloud to every request. Useful for correlation and debugging.

**Example:** `a3c5e8f2-4b1d-4e9a-8f7c-2d1e3b4a5c6d`

## Multipart Requests

### request.multipart

Boolean indicating whether the request is a multipart request.

**Example:** `true` or `false`

### request.parts

For multipart requests, the individual parts are exposed via the template model. Each part can be referenced by its name and exposes several properties.

For a multipart request with a part named `text`, the following properties are available:

#### request.parts.text.binary

Boolean indicating if the part contains binary data.

#### request.parts.text.headers.key

First value of a header within the multipart part.

**Example:** `request.parts.text.headers.content-type`

#### request.parts.text.body

The part's body content as text.

#### request.parts.text.bodyAsBase64

The part's body content as Base64-encoded string.

## Values That Can Be One or Many

A number of HTTP elements (query parameters, form fields, headers, cookies) can be single or multiple valued. The template request model handles this elegantly with a "list or single" type that:

* Returns the first (and often only) value when no index is specified
* Supports indexed access for multiple values
* Provides convenience accessors like `first` and `last`

### Accessing Single or Multiple Values

Given a request URL like `/multi-query?things=1&things=2&things=3`, you can extract query data in several ways:

```handlebars theme={null}
{{request.query.things}}       // Returns: 1
{{request.query.things.0}}     // Returns: 1
{{request.query.things.first}} // Returns: 1
{{request.query.things.1}}     // Returns: 2
{{request.query.things.[-1]}}  // Returns: 2
{{request.query.things.last}}  // Returns: 3
```

### Important Note About Comparisons

When using the `eq` helper with one-or-many values, you must use the indexed form, even if only one value is present.

The non-indexed form returns the wrapper type (not a String), which will fail comparisons with String values.

**Correct:**

```handlebars theme={null}
{{#if (eq request.query.status.0 "active")}}
  Status is active
{{/if}}
```

**Incorrect:**

```handlebars theme={null}
{{#if (eq request.query.status "active")}}
  This will not work as expected
{{/if}}
```

## Using the Request Model in Webhooks

In [webhook](/webhooks) templates, the triggering request is available as `originalRequest` instead of `request`. This distinguishes it from any request data being constructed for the webhook itself.

**Example:** `{{originalRequest.headers.X-Correlation-Id}}`


# Response Templating - String Encodings
Source: https://docs.wiremock.io/response-templating/string-encodings

Working with base64, URL and form encodings.

WireMock Cloud provides several helpers for encoding and decoding values to/from various
formats.

## Base64

The `base64` helper encodes and decodes Base64:

```handlebars theme={null}
{{{base64 request.headers.X-Plain-Header}}}
{{{base64 request.headers.X-Plain-Header padding=false}}}
{{{base64 request.headers.X-Encoded-Header decode=true}}}

{{#base64}}Content to encode{{/base64}}

{{#base64 decode=true}}Q29udGVudCB0byBkZWNvZGUK{{/base64}}
```

## URLs

The `urlEncode` helper encode and decode values according to the [HTTP URL encoding standard](https://en.wikipedia.org/wiki/Percent-encoding).

```handlebars theme={null}
{{{urlEncode request.headers.X-Plain-Header}}}
{{{urlEncode request.headers.X-Encoded-Header decode=true}}}

{{#urlEncode}}Content to encode{{/urlEncode}}

{{#urlEncode decode=true}}Content%20to%20decode{{/urlEncode}}
```

## Forms

The `formData` helper parses its input as an HTTP form, returning an object containing the individual fields as attributes.
The helper takes the input string and variable name as its required parameters, with an optional `urlDecode` parameter
indicating that values should be URL decoded.

The following example will parse the request body as a form, then output a single field `formField3`:

```handlebars theme={null}
{{formData request.body 'form' urlDecode=true}}{{{form.formField3}}
```

If the form submitted has multiple values for a given field, these can be accessed by index:

```handlebars theme={null}
{{formData request.body 'form' urlDecode=true}}}{{{form.multiValueField.1}}, {{{form.multiValueField.2}}
{{formData request.body 'form' urlDecode=true}}}{{{form.multiValueField.first}}, {{{form.multiValueField.last}}
```


# Response Templating - String Helpers
Source: https://docs.wiremock.io/response-templating/string-helpers

Working with strings

WireMock Cloud provides a set of string manipulation helpers.

## Regular expression extract

The `regexExtract` helper supports extraction of values matching a regular expression from a string.

A single value can be extracted like this:

```handlebars theme={null}
{{regexExtract request.body '[A-Z]+'}}"
```

Regex groups can be used to extract multiple parts into an object for later use (the last parameter is a variable name to which the object will be assigned):

```handlebars theme={null}
{{regexExtract request.body '([a-z]+)-([A-Z]+)-([0-9]+)' 'parts'}}
{{parts.0}},{{parts.1}},{{parts.2}}
```

## String transformation helpers

### Trim

Use the `trim` helper to remove whitespace from the start and end of the input:

```handlebars theme={null}
{{trim request.headers.X-Padded-Header}} // Inline

{{#trim}}                                // Block

    Some stuff with whitespace

{{/trim}}
```

### Abbreviate

`abbreviate` truncates a string if it is longer than the specified number of characters.
Truncated strings will end with a translatable ellipsis sequence ("...").

For instance the following template:

```handlebars theme={null}
{{abbreviate 'Mocking APIs helps you develop faster' 21 }} // Mocking APIs helps...
```

### Capitalisation

`capitalize` will make the first letter of each word in the passed string a capital e.g.

```handlebars theme={null}
{{capitalize 'mock my stuff'}} // Mock My Stuff
```

`capitalizeFirst` will capitalise the first character of the value passed e.g.

```handlebars theme={null}
{{capitalizeFirst 'mock my stuff'}} // Mock my stuff
```

### Center

`center` centers the value in a field of a given width e.g.

```handlebars theme={null}
{{center 'hello' size=21}}
```

will output:

```
        hello        
```

You can also specify the padding character e.g.

```handlebars theme={null}
{{center 'hello' size=21 pad='#'}}
```

will output:

```
########hello########
```

### Cut

`cut` removes all instances of the parameter from the given string.

```handlebars theme={null}
{{cut 'mocking, stubbing, faults' ','}} // mocking stubbing faults
```

### Default if empty

`defaultIfEmpty` outputs the passed value if it is not empty, or the default otherwise e.g.

```handlebars theme={null}
{{defaultIfEmpty 'my value' 'default'}} // my value

{{defaultIfEmpty '' 'default'}}         // default
```

### Join

`join` takes a set of parameters or a collection and builds a single string, with
each item separated by the specified parameter.

```handlebars theme={null}
{{join 'Mark' 'Rob' 'Dan' ', '}} // Mark, Rob, Dan
```

You can optionally specify a prefix and suffix:

```handlebars theme={null}
{{join 'Mark' 'Rob' 'Dan' ', ' prefix='[' suffix=']'}} // [Mark, Rob, Dan]
```

### Justify left and right

`ljust` left-aligns the value in a field of a given width, optionally taking a padding character.

```handlebars theme={null}
{{ljust 'things' size=20}}         // 'things              '
{{ljust 'things' size=20 pad='#'}} // 'things##############'
```

`rjust` right-aligns the value in the same manner

```handlebars theme={null}
{{rjust 'things' size=20}}         // '              things'
{{rjust 'things' size=20 pad='#'}} // '##############things'
```

### Lower and upper case

`lower` and `upper` convert the value to all lowercase and all uppercase:

```handlebars theme={null}
{{lower 'WireMock Cloud'}} // wiremock cloud
{{upper 'WireMock Cloud'}} // WIREMOCK CLOUD
```

### Replace

`replace` replaces all occurrences of the specified substring with the replacement value.

```handlebars theme={null}
{{replace 'the wrong way' 'wrong' 'right' }} // the right way
```

### Slugify

`slugify` converts to lowercase, removes non-word characters (alphanumerics and
underscores) and converts spaces to hyphens. Also strips leading and trailing whitespace.

```handlebars theme={null}
{{slugify 'Mock my APIs'}} // mock-my-apis
```

### Strip tags

`stripTags` strips all \[X]HTML tags.

```handlebars theme={null}
{{stripTags '<greeting>hi</greeting>'}} // hi
```

### Substring

`substring` outputs the portion of a string value between two indices. If only
one index is specified the substring between this point and the end will be returned.

```handlebars theme={null}
{{substring 'one two' 4}}   // two
{{substring 'one two' 0 3}} // one
```

### Word wrap

`wordWrap` wraps words at specified line length.

```handlebars theme={null}
{{wordWrap 'one two three' 4}}
```

will output:

```
one
two
three
```

### Yes/no

`yesno` maps values for true, false and optionally null, to the strings "yes",
"no", "maybe".

```handlebars theme={null}
{{yesno true}}   // yes
{{yesno false}}  // no
{{yesno null}}   // maybe
```

You can also specify different strings to represent each state:

```handlebars theme={null}
{{yesno true yes='aye'}}    // aye
{{yesno false no='nay'}}    // nay
{{yesno null maybe='meh'}}  // meh
```


# Response Templating - Working with XML
Source: https://docs.wiremock.io/response-templating/xml

Working with XML

This article describes WireMock Cloud's helpers for processing and manipulating XML.

## XPath

The `xPath` helper can be used to extract values or sub documents via an XPath 1.0 expression from an XML string.
Most commonly this is used to extract values from the request body.

For example, given a request body of:

```xml theme={null}
<outer>
    <inner>Stuff</inner>
</outer>
```

The following will render "Stuff" into the output:

```handlebars theme={null}
{{{xPath request.body '/outer/inner/text()'}}}
```

And given the same XML the following will render `<inner>Stuff</inner>`:

```handlebars theme={null}
{{{xPath request.body '/outer/inner'}}}
```

### Extracting attributes

XPath also permits extraction of attributes e.g. for a request body of:

```xml theme={null}
<outer>
    <inner id="123"/>
</outer>
```

The following will render "123" into the output:

```handlebars theme={null}
{{{xPath request.body '/outer/inner/@id'}}}
```

## SOAP XPath

As a convenience the `soapXPath` helper also exists for extracting values from SOAP bodies e.g. for the SOAP document:

```xml theme={null}
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope/">
    <soap:Body>
        <m:a>
            <m:test>success</m:test>
        </m:a>
    </soap:Body>
</soap:Envelope>
```

The following will render "success" in the output:

```handlebars theme={null}
{{{soapXPath request.body '/a/test/text()'}}}
```

## Iterating over XML elements

The `xPath` helper returns "one or many" collections results, which can either
be printed directly, or passed to further helpers such as [`each`](/response-templating/conditional-logic-and-iteration/#iteration) or [`join`](/response-templating/string-helpers/#join).

For instance, given a request body of the form:

```xml theme={null}
<?xml version="1.0"?>
<stuff>
    <thing>One</thing>
    <thing>Two</thing>
    <thing>Three</thing>
</stuff>
```

and the following template:

```handlebars theme={null}
{{#each (xPath request.body '/stuff/thing') as |element|}}{{{element.text}}} {{/each}}
```

the resulting output will be:

```
One Two Three
```

### XML element attributes

Elements in the collection returned by `xPath` have the following properties:

`text`: The text content of the element.

`name`: The element's name.

`attributes`: A map of attribute names and values e.g. given an XML element has
been selected:

```xml theme={null}
<thing id="123" position="top"/>
```

Its attributes can be referenced:

```handlebars theme={null}
      ID: {{{element.attributes.id}}}
Position: {{{element.attributes.position}}}
```

## Formatting XML

The `formatXml` helper allows you to output XML in either a pretty or a compact format. The default is pretty:

```handlebars theme={null}
{{#assign 'object1'}}
<foo><bar
    >wh</bar></foo
    >
{{/assign}}
{{formatXml object1}}
```

emits:

```xml theme={null}
<foo>
  <bar>wh</bar>
</foo>
```

Whereas

```handlebars theme={null}
{{formatXml object1 format='compact'}}
```

emits

```xml theme={null}
<foo><bar>wh</bar></foo>
```

The xml to format can also be supplied as a block body:

```handlebars theme={null}
{{#formatXml}}
<foo><bar
    >wh</bar></foo
    >
{{/formatXml}}
```


# Runner environment variables
Source: https://docs.wiremock.io/runner/environment-variables

Reference documentation for all environment variables that can be used with WireMock Runner

This page documents all environment variables that can be used to configure the WireMock Runner.

## Core Runner configuration

These environment variables control the fundamental behavior of the WireMock Runner.

### WMC\_RUNNER\_ENABLED

Enables Runner mode when using the WireMock binary. By default, the binary runs the CLI tool, but setting this variable to `true` will execute the Runner instead.

**Type:** Boolean
**Default:** `false`
**Example:**

```shell theme={null}
WMC_RUNNER_ENABLED=true wiremock
```

<Note>
  You should never need to set this variable yourself except when building your own Docker image to wrap WireMock Runner.

  This can be safely ignored if using WireMock's official Docker image.
</Note>

### WMC\_DEFAULT\_MODE

The mode that the Runner starts in. Once running, the mode can be changed via the [HTTP switch endpoint](/runner/overview#switching-mode).

**Type:** String
**Valid values:** `record-many`, `serve`
**Default:** `serve`
**Example:**

```shell theme={null}
docker run \
  -e WMC_DEFAULT_MODE='record-many' \
  wiremock/wiremock-runner:latest
```

### WMC\_ADMIN\_PORT

The port that the Runner's admin interface is exposed on. The admin interface provides endpoints for switching modes and flushing recordings.

**Type:** Integer
**Default:** Random available port
**Example:**

```shell theme={null}
docker run \
  -e WMC_ADMIN_PORT='9999' \
  -p 9999:9999 \
  wiremock/wiremock-runner:latest
```

### WMC\_API\_TOKEN

The API token used to authenticate with WireMock Cloud. This token is required for operations that interact with WireMock Cloud, such as flushing recordings in `record-many` mode or pulling stub mappings.

**Type:** String
**Required:** Yes
**Example:**

```shell theme={null}
docker run \
  -e WMC_API_TOKEN='your-api-token-here' \
  wiremock/wiremock-runner:latest
```

<Note>
  You can find your API token in the [WireMock Cloud console](https://app.wiremock.cloud/account/security) or by running `wiremock config get api-token` if you've logged in via the CLI.
</Note>

## Configuration file location

### WMC\_VALUES\_CONFIG\_FILE

Overrides the default path for the values configuration file. By default, the Runner looks for `.wiremock/config.yaml` in the working directory.

**Type:** String (file path)
**Default:** `.wiremock/config.yaml`
**Example:**

```shell theme={null}
docker run \
  -e WMC_VALUES_CONFIG_FILE='/custom/path/config.yaml' \
  wiremock/wiremock-runner:latest
```

<Note>
  Setting the `--wiremock-dir` option does not affect where the CLI/Runner searches for the default values file. Use `WMC_VALUES_CONFIG_FILE` to specify a custom location.
</Note>

## Mode-specific configuration

The Runner supports the same configuration options as the WireMock CLI for its respective modes. You can set any CLI option using environment variables following the pattern `WMC_<MODE_NAME>_<OPTION_NAME>`.

### Pattern for mode-specific variables

Environment variable names follow this pattern:

* Prefix: `WMC_`
* Mode name: `RUN_` (for serve mode) or `RECORD_MANY_` (for record-many mode)
* Option name: The CLI option name with dashes replaced by underscores

### Examples

#### Serve mode configuration

For `serve` mode, equivalent to the [`run` CLI command](/cli/local-playback):

```shell theme={null}
# Set the request log level for serve mode
WMC_RUN_REQUEST_LOG_LEVEL=full

# Set the WireMock directory for serve mode
WMC_RUN_WIREMOCK_DIR=/custom/path

# Enable watch mode for serve mode
WMC_RUN_WATCH=true
```

#### Record-many mode configuration

For `record-many` mode, equivalent to the [`record-many` CLI command](/cli/multi-domain-recording):

```shell theme={null}
# Set the request log level for record-many mode
WMC_RECORD_MANY_REQUEST_LOG_LEVEL=full

# Configure services to include in recording
WMC_RECORD_MANY_INCLUDE_SERVICES=api1,api2

# Configure batch size for recording
WMC_RECORD_MANY_MAX_BATCH_BYTES=128MB
```

### Profile configuration via mode-specific variables

Profiles define which Mock APIs in WireMock Cloud are mapped to which local services. These environment variables allow you to specify which profile to use for different Runner modes.

#### WMC\_RUN\_PROFILE

Specifies the profile to use when the Runner is in `serve` mode. This determines which Mock APIs are served and on which ports.

**Type:** String
**Default:** `default` profile from `wiremock.yaml`
**Example:**

```yaml theme={null}
# In Kubernetes manifest
- name: WMC_RUN_PROFILE
  value: "development"
```

#### WMC\_RECORD\_MANY\_PROFILE

Specifies the profile to use when the Runner is in `record-many` mode. This determines which services are recorded and which Mock APIs in WireMock Cloud receive the recorded stubs.

**Type:** String
**Default:** `default` profile from `wiremock.yaml`
**Example:**

```yaml theme={null}
# In Kubernetes manifest
- name: WMC_RECORD_MANY_PROFILE
  value: "development"
```

### Available options

For a complete list of available options for each mode, see:

* [Local playback (`run`) options](/cli/local-playback) for `serve` mode
* [Multi-domain recording (`record-many`) options](/cli/multi-domain-recording) for `record-many` mode

## Configuration precedence

When the same option is configured in multiple places, the following precedence order applies (highest to lowest):

1. HTTP request body (when switching modes via the [switch endpoint](/runner/overview#mode-configuration))
2. Environment variables
3. Values file (`.wiremock/config.yaml`)
4. Default values

This allows you to set baseline configuration in a values file, override it with environment variables for different deployments, and temporarily override specific options when switching modes.

## See also

* [Runner overview](/runner/overview) - General information about the WireMock Runner
* [CLI configuration](/cli/overview#environment-variables) - Details on CLI environment variable patterns
* [Serve mode](/runner/serve) - Using the Runner in serve mode
* [Record-many mode](/runner/record-many) - Using the Runner in record-many mode


# WireMock Runner
Source: https://docs.wiremock.io/runner/overview

How to use the WireMock Runner

## Overview

The WireMock Runner offers a way to deploy and run long-lived WireMock tasks and control the lifecycle of those tasks
via an HTTP interface.

## Installation

The Runner is published to Docker Hub as [`wiremock/wiremock-runner`](https://hub.docker.com/r/wiremock/wiremock-runner).
Running the image will start the runner and expose the HTTP interface based on the configuration specified via
environment variables.

The following environment variables can be used to configure the runner:

* `WMC_DEFAULT_MODE`: The mode that the runner starts in. Currently, supports `record-many`, `serve`. Defaults to `serve` if omitted.
* `WMC_ADMIN_PORT`: The port that the admin interface is exposed on. Defaults to an available random port.
* `WMC_API_TOKEN`: The API token to use for accessing WireMock Cloud.

You will also need to [publish the appropriate ports](https://docs.docker.com/reference/cli/docker/container/run/#publish)
for the services defined in your environment file along with the port you have configured for the Runner.

Here is a typical example on Linux or macOS when starting the Runner in `record-many` mode:

```shell theme={null}
docker run \
  -e WMC_DEFAULT_MODE='record-many' \
  -e WMC_ADMIN_PORT='9999' \
  -e WMC_API_TOKEN='<wmc-api-token>' \
  -p 9999:9999 \
  wiremock/wiremock-runner:latest
```

## Switching mode

The Runner will always start in the default mode, configurable via `WMC_DEFAULT_MODE`.
Once running, the Runner's current mode can be changed via an HTTP `PUT` request to `/v1/mode` on the Runner's admin
port, configurable via `WMC_ADMIN_PORT`.
The request must contain a JSON body of the form

```json theme={null}
{ "mode" : "<DESIRED_MODE>" }
```

with `<DESIRED_MODE>` replaced with one of the Runner's available modes.

Example:

```http request theme={null}
PUT http://localhost:8080/v1/mode
Content-Type: application/json

{ "mode": "serve" }
```

### Mode configuration

Similar to the WireMock CLI, WireMock Runner modes can be configured in a number of ways:
[via a values file](/cli/overview#values-file), [via environment variables](/cli/overview#environment-variables), or via the body of the HTTP switch request.

To configure the mode via the HTTP switch request, a `"config"` field can be provided alongside the `"mode"` field in
the request body.
This `"config"` field must be an object, whose keys have string values and correspond to a relevant configuration field
of the requested mode.
For example, the following HTTP request would configure the WireMock directory and the [batching](/cli/multi-domain-recording#importing-recordings-as-you–go-along)
of the record-many mode:

```http request theme={null}
PUT http://localhost:8080/v1/mode
Content-Type: application/json

{
  "mode": "record-many",
  "config": {
    "wiremock-dir": "path/to/wiremock",
    "max-batch-bytes": "128 MB"
  }
}
```

For details of the specific configuration available to each Runner mode, see the relevant mode's own documentation page.

## Record Many Mode

One of the Runner's available modes is `record-many` mode.
This mode starts a [multi-domain recording](/cli/multi-domain-recording) session that will record requests to your
configured services and flush the results to WireMock Cloud.
More information on this mode can be found in the [WireMock Runner Record Many documentation](/runner/record-many).

## Serve Mode

One of the Runner's available modes is `serve` mode.
This mode starts a [local playback](/cli/local-playback) session that serves your configured services from the Runner's
container.
More information on this mode can be found in the [WireMock Runner Serve documentation](/runner/serve).

## WireMock Runner vs WireMock CLI

[The WireMock CLI](/cli) and the WireMock Runner offer very similar functionality to each other (with the caveat that
the Runner currently exposes a limited subset of the capabilities of the CLI).
In fact, both tools are packaged within the same binary published to [the NPM registry](https://www.npmjs.com/package/@wiremock/cli)
and [Docker Hub](https://hub.docker.com/u/wiremock).
By default, the binary will run the CLI tool, but this can be overridden to execute the Runner by setting the
environment variable `WMC_RUNNER_ENABLED` to `true`.

Example:

```shell theme={null}
WMC_RUNNER_ENABLED=true wiremock
```

## Runner health check

The WireMock Runner exposes a health check endpoint at `/__/health`.
Performing a `GET` request to this endpoint will return a 200 status code when the Runner is healthy.

This health check can be used by orchestration systems like Kubernetes to detect issues, and is built-in to the Runner's [published docker image](https://hub.docker.com/r/wiremock/wiremock-runner).
More information on using the WireMock Runner in your Kubernetes cluster can be found [here](/runner/running-on-kubernetes).


# Promoting Mock APIs with Git and CI/CD
Source: https://docs.wiremock.io/runner/promoting-apis-with-git-and-ci

How to promote WireMock mock APIs across environments using Git version control and CI/CD pipelines

This guide shows you how to promote your WireMock mock APIs across multiple environments using Git version control and CI/CD automation. You'll set up a workflow where changes are recorded in a development environment, reviewed through pull requests, and automatically deployed to staging via GitHub Actions.

## Prerequisites

Before you begin, ensure you have:

* Completed the [Running on Kubernetes](/runner/running-on-kubernetes) guide
* WireMock Runner deployed and running in your Kubernetes cluster
* WireMock CLI installed and authenticated
* A GitHub account and repository for version control
* Git installed and configured locally

<Note>
  While this guide uses GitHub and GitHub Actions, the same principles apply to other Git platforms (GitLab, Bitbucket) and CI/CD tools (Jenkins, CircleCI, GitLab CI).
</Note>

## Initial setup

### Set up development environment

<Note>
  If you have already completed the [Recording Multiple APIs on Kubernetes](/runner/recording-multiple-apis-on-kubernetes) guide,
  you can skip this step as you will already have a development environment.
</Note>

Create a development environment to keep your experimental changes separate from production:

```bash theme={null}
wiremock environments create --profile development
```

This creates new mock APIs in WireMock Cloud with a `[development]` suffix and generates a `wiremock-development.yaml` profile file that overlays your base `wiremock.yaml` configuration.

Note the base URLs from the output - you'll use these to test your recorded endpoints in WireMock Cloud.

### Set up staging environment

Create a staging environment that will serve as your pre-production testing ground:

```bash theme={null}
wiremock environments create --profile staging
```

This creates another set of mock APIs with a `[staging]` suffix and generates a `wiremock-staging.yaml` profile file. The staging environment will receive automated deployments from your CI/CD pipeline.

### Initialize git repository

If you haven't already, initialize Git in your project directory:

```bash theme={null}
cd kubernetes-runner-demo
git init
git add .
git commit -m "Initial commit: WireMock configuration"
```

Create a repository on GitHub and push your initial configuration:

```bash theme={null}
git remote add origin https://github.com/your-username/your-repo.git
git branch -M main
git push -u origin main
```

Your repository now contains:

* `.wiremock/wiremock.yaml` - Base configuration with production mock APIs
* `.wiremock/wiremock-development.yaml` - Development environment overrides
* `.wiremock/wiremock-staging.yaml` - Staging environment overrides
* `.wiremock/*/stub-mappings.yaml` - Stub mappings for each mock API

### Create GitHub Actions workflow

Create a GitHub Actions workflow that automatically pushes changes to staging when code is merged to the main branch.

Create the workflow file:

```bash theme={null}
mkdir -p .github/workflows
```

Create `.github/workflows/deploy-staging.yml`:

```yaml theme={null}
name: Deploy to Staging

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install WireMock CLI
        run: npm install -g @wiremock/cli

      - name: Configure WireMock CLI
        env:
          WIREMOCK_API_TOKEN: ${{ secrets.WIREMOCK_API_TOKEN }}
        run: |
          wiremock config set api_token $WIREMOCK_API_TOKEN

      - name: Push to staging environment
        run: |
          wiremock push mock-api --all --profile staging

      - name: Confirm deployment
        run: |
          echo "✅ Successfully deployed mock APIs to staging environment"
```

#### Configure GitHub secrets

Add your WireMock Cloud API token as a GitHub secret:

1. Go to your GitHub repository settings
2. Navigate to **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `WIREMOCK_API_TOKEN`
5. Value: Your WireMock Cloud API token (find it at [app.wiremock.cloud/account/security](https://app.wiremock.cloud/account/security))

Commit and push the workflow:

```bash theme={null}
git add .github/workflows/deploy-staging.yml
git commit -m "Add CI/CD workflow for staging deployment"
git push origin main
```

## Update APIs via the workflow

Now that your environments and CI/CD pipeline are configured, you can start making changes.

### Sync development with the source project

Run the following to push all the configuration to the development environment in WireMock Cloud:

```bash theme={null}
wiremock push mock-api --all --profile development
```

### Update APIs in development

Update the development APIs in Cloud via whatever means you wish e.g. manual editing in the UI, recording, scripting etc.

See the [recording on Kubernetes guide](/runner/recording-multiple-apis-on-kubernetes) for details on recording multiple APIs
simultaneously from within Kubernetes.

## Pull your changes from development

Pull the updated stub mappings from your development environment into your local project:

```bash theme={null}
wiremock pull mock-api --all --profile development
```

This downloads the stub mappings from your development environment and overwrites the local stub files in your `.wiremock` directory.

<Note>
  When pulling with a profile, only the stub mappings and API definition files are updated - the `wiremock.yaml` configuration remains unchanged.
</Note>

Review the changes to ensure they look correct:

```bash theme={null}
git diff .wiremock
```

## Create a pull request

Create a new branch for your changes:

```bash theme={null}
git checkout -b feature/add-github-org-endpoints
```

Commit your changes:

```bash theme={null}
git add .wiremock
git commit -m "Add GitHub organization and repository endpoints"
git push origin feature/add-github-org-endpoints
```

Create a pull request on GitHub:

1. Go to your repository on GitHub
2. Click **Pull requests** → **New pull request**
3. Select your feature branch
4. Add a description explaining the changes
5. Create the pull request

## Merge and Deploy

When the pull request is approved, merge it into the main branch:

1. Click **Merge pull request** on GitHub
2. Confirm the merge

GitHub Actions will automatically:

1. Detect the changes in the `.wiremock` directory
2. Run the deployment workflow
3. Push the updated mock APIs to the staging environment
4. Report the deployment status

### Verify the Deployment

Check the GitHub Actions workflow to ensure it completed successfully:

1. Go to the **Actions** tab in your repository
2. Click on the latest workflow run
3. Verify all steps completed successfully

Test the deployed endpoints in staging:

```bash theme={null}
curl https://your-staging-api.wiremock.cloud/a-new-endpoint
```

The staging environment now has the same stub mappings as your development environment.

## Troubleshooting

### Workflow Fails with Authentication Error

If the GitHub Actions workflow fails with an authentication error:

1. Verify the `WIREMOCK_API_TOKEN` secret is set correctly in GitHub
2. Check that your API token hasn't expired
3. Generate a new token at [app.wiremock.cloud/account/security](https://app.wiremock.cloud/account/security)

### Stub Mappings Not Updated After Push

If stub mappings don't appear in WireMock Cloud after pushing:

1. Check the workflow logs for errors
2. Verify the profile name matches your environment file
3. Ensure the `cloud_id` values in your profile file are correct

## Additional Resources

* Learn about [selective recording](/runner/record-many#choosing-which-services-to-record) to record only specific services
* Set up [branch-specific environments](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment) for feature branch testing


# Record Many Mode via the WireMock Runner
Source: https://docs.wiremock.io/runner/record-many

How to use Record Many Mode with the WireMock Runner

## Record Many Mode

One of the Runner's available modes is `record-many` mode.
The runner can be started in `record-many` mode by setting the `WMC_DEFAULT_MODE` environment variable to `record-many`,
or switched to this mode using the Runner's [switch endpoint](/runner/overview#switching-mode).
This mode starts a [multi-domain recording](/cli/multi-domain-recording) session that will continue to record until the
runner is stopped or its mode is switched.

### Record Many Configuration

The record many session started by the Runner can be configured via the same mechanism as the [`record-many` command](/cli/multi-domain-recording)
of the WireMock CLI - either [via a values file](/cli/overview#values-file) or [via environment variables](/cli/overview#environment-variables).
Additionally, configuration can be provided at switch time [via the HTTP request body](/runner/overview#mode-configuration).

All options available to the [`record-many` CLI command](/cli/multi-domain-recording) are also available to the Runner's `record-many` mode.
When specifying an option in the [`"config"` field of the HTTP switch request](/runner/overview#mode-configuration), remove the dash (`-`) prefix that would normally be used when provided on the command line.
For instance, the [`--include-services` option](/cli/multi-domain-recording#choosing-which-services-to-record) would become `"include-services"` in the request body, like so:

```json theme={null}
{
  "mode": "record-many",
  "config": {
    "include-services": "invoicing-api,payment-api"
  }
}
```

Just like the WireMock CLI, by default the Runner will expect a WireMock environment file in the `.wiremock` directory
in the current working directory of the container.

### Flushing Recordings

The `record-many` mode will honour the [batching configuration](/cli/recording#importing-recordings-as-you-go-along) you
have specified in your config file.  The Runner also defines an endpoint which can be used to flush the recorded requests
to WireMock Cloud independently of the batching configuration:

* `POST /v1/record-many/flush`

<Warning>
  When the Runner is stopped or switched out of record-many mode, recorded requests will not be flushed automatically.
  To ensure all your recordings are saved to WireMock Cloud, call [`POST
        /v1/record-many/flush`](/runner/record-many#flushing-recordings) before stopping the recording session.
</Warning>

### Starting the Runner In Record Many Mode

When starting the runner in `record-many` mode you will need to [publish the appropriate ports](https://docs.docker.com/reference/cli/docker/container/run/#publish)
for the services you are running along with the port you have configured for the Runner.

Here is a typical example on Linux or macOS when running the Runner on port `9999` and recording to two Mock APIs:

```shell theme={null}
docker run \
  -e WMC_DEFAULT_MODE='record-many' \
  -e WMC_ADMIN_PORT='9999' \
  -e WMC_API_TOKEN='<wmc-api-token>' \
  -v ./.wiremock/:/work/.wiremock/ \
  -p 9999:9999 \
  -p 8080:8080 \
  -p 8081:8081 \
  wiremock/wiremock-runner:latest
```


# Recording from Within Kubernetes
Source: https://docs.wiremock.io/runner/recording-multiple-apis-on-kubernetes

How to record new stub mappings using WireMock Runner deployed in Kubernetes

This guide shows you how to record additional API endpoints into your WireMock Cloud mock APIs using the WireMock Runner deployed in a Kubernetes cluster. You'll use the Runner's [Record Many Mode](/runner/record-many) to capture real HTTP traffic and automatically create stub mappings.

## Prerequisites

Before you begin, ensure you have:

* Completed the [Running on Kubernetes](/runner/running-on-kubernetes) guide
* WireMock Runner deployed and running in your Kubernetes cluster
* WireMock CLI installed and authenticated
* Access to the services you want to record (either real APIs or test environments)

## Set up a development environment

Next we'll set up a development environment in WireMock Cloud (an environment is a set of mock APIs intended to be used together).

### Initialise environment and profile

Run the following to create a new environment in WireMock Cloud and also create a new profile,
which will be defined in `wiremock-development.yaml` and maps the local services to the corresponding cloud IDs for the APIs we just created:

```bash theme={null}
wiremock environments create --profile development
```

Note the base URLs of the mock APIs from the output - you'll need these to test your recorded endpoints in WireMock Cloud.

### Push existing stubs

If you have existing stub mappings in your local `.wiremock` directory, push them to your development environment:

```bash theme={null}
wiremock push mock-api --all --profile development
```

This ensures your development environment starts with the same baseline as your production environment.

### Set the profile in the Runner

When the Runner starts we need to set it to use the profile we just created,
so add the following to the `wiremock-runner` container environment variables in the Kubernetes manifest in `wiremock-runner.yaml`:

```yaml theme={null}
- name: WMC_RUN_PROFILE
  value: "development"
- name: WMC_RECORD_MANY_PROFILE
  value: "development"
```

Apply the changes to the Kubernetes cluster:

```bash theme={null}
./install-wiremock.sh
```

## Start Recording

Switch the Runner to record-many mode using the Runner's admin API:

```bash theme={null}
curl -X PUT \
  -d '{ "mode": "record-many" }' \
  http://admin.local.wiremock.cloud/v1/mode
```

The Runner is now proxying requests to the real APIs defined in your `.wiremock/wiremock.yaml` file and recording the responses.

## Make requests to record

Make requests to the API endpoints you want to record. The Runner will forward these to the real API and capture both the request and response.

For example, to record a GitHub organizations endpoint:

```bash theme={null}
curl -v http://github.local.wiremock.cloud/organizations
```

You should see the real response from GitHub, and the Runner will automatically create a stub mapping for this endpoint.

Continue making requests to capture all the endpoints you need.

## Flush recorded stubs

Flush the recorded stubs to ensure they're saved to WireMock Cloud:

```bash theme={null}
curl -X POST http://admin.local.wiremock.cloud/v1/record-many/flush
```

<Warning>
  Always flush before stopping recording or switching modes. The Runner does not automatically flush when switching modes, so any unflushed recordings will be lost.
</Warning>

## Stop recording

Switch the Runner back to serve mode:

```bash theme={null}
curl -X PUT \
  -d '{ "mode": "serve" }' \
  http://admin.local.wiremock.cloud/v1/mode
```

## Test your recorded stubs

### Test in WireMock Cloud

Use the base URLs you noted earlier to test the recorded endpoints directly in WireMock Cloud:

```bash theme={null}
curl https://your-development-api.wiremock.cloud/organizations
```

You should see the recorded response without any request being made to the real GitHub API.

You should also see the recorded stubs in the WireMock Cloud UI under the Stubs tab for the GitHub API.

### Pull changes to your local environment

Pull the newly recorded stubs down into the local project:

```bash theme={null}
wiremock pull mock-api --all --profile development
```

This downloads the stub mappings and OpenAPI from the development instance of the GitHub API in Cloud to the local project.

Now redeploy to the local Kubernetes cluster:

```bash theme={null}
./install-wiremock.sh
```

### Test in Kubernetes

Test the recorded endpoints again to ensure they're working correctly:

```bash theme={null}
curl -v http://github.local.wiremock.cloud/organizations
```

You should see the recorded response without any request being made to the real GitHub API.

## Next steps

* Learn how to [promote your mock APIs between environments](/runner/promoting-apis-with-git-and-ci) using Git and CI/CD.

## Additional resources

* Explore [selective recording](/runner/record-many#choosing-which-services-to-record) to record only specific services
* Configure [batching options](/cli/recording#importing-recordings-as-you-go-along) to control when recordings are flushed


# Running the WireMock Runner on Kubernetes
Source: https://docs.wiremock.io/runner/running-on-kubernetes

How to deploy and run WireMock Runner in a Kubernetes cluster

This guide shows you how to deploy the WireMock Runner in a Kubernetes cluster, configured to serve mock APIs from WireMock Cloud.

## Prerequisites

Before you begin, ensure you have:

* A Kubernetes cluster (local or remote)
  * For local development, [KIND](https://kind.sigs.k8s.io/) is recommended
* `kubectl` CLI tool installed and configured
* WireMock CLI installed and configured
  * Install from the [WireMock CLI documentation](/cli/overview)
  * Authenticate with `wiremock login` or configure your API token with `wiremock config set api-token <your-token>`
* A WireMock Cloud account with one or more mock APIs created

## Clone the demo repository

The WireMock Kubernetes Runner demo repository contains all the necessary configuration files and scripts:

```bash theme={null}
git clone https://github.com/wiremock-inc/kubernetes-runner-demo.git
cd kubernetes-runner-demo
```

## Create a cluster

Run the following script:

```bash theme={null}
./create-cluster.sh
```

This will create a local KIND cluster using `kind.config.yaml` for configuration. Ingress will be configured to listen
on HTTP port 80 and HTTPS port 443.

If you're using a remote cluster, you can skip this step.

## Set up authentication

Create a Kubernetes secret with your WireMock Cloud API token:

```bash theme={null}
./set-secret.sh
```

This script retrieves your API token from the WireMock CLI configuration and creates a secret named `wiremock-cloud-token` that the WireMock Runner will use to authenticate with WireMock Cloud.

<Note>
  If you haven't logged in with the WireMock CLI, run `wiremock login` first. You can also find your API token in the [WireMock Cloud console](https://app.wiremock.cloud/account/security).
</Note>

## Deploy to Kubernetes

Run the installation script to deploy WireMock Runner:

```bash theme={null}
./install-wiremock.sh
```

This script will do the following by applying the manifest in `wiremock-runner.yaml`:

1. Create a Persistent Volume Claim (PVC) for storing WireMock configuration
2. Deploy the WireMock Runner service and deployment
3. Set up ingress rules for accessing the APIs

The demo project includes pre-recorded stub mappings under `.wiremock` directory for both the PayPal Invoicing and GitHub REST APIs, so you can test the deployment immediately without needing to create stubs first.

Verify the deployment:

```bash theme={null}
kubectl get pods -l app=wiremock-runner
```

You should see the WireMock Runner pod in a `Running` state.

## Monitor your deployment

### Check pod status

```bash theme={null}
kubectl get pods -l app=wiremock-runner
```

### View logs

```bash theme={null}
kubectl logs -l app=wiremock-runner -f
```

## Test the APIs

<Note>
  For local development, you may need to add these entries to your hosts file:

  ```
  127.0.0.1 admin.local.wiremock.cloud paypal.local.wiremock.cloud github.local.wiremock.cloud
  ```
</Note>

First, try fetching a list of PayPal invoices from the simulated PayPal Invoicing API:

```bash theme={null}
curl 'http://paypal.local.wiremock.cloud/v2/invoicing/invoices?page=1&page_size=10&total_required=true&fields=amount'
```

You should see a fairly large JSON response, containing invoice data.

Now try fetching a list of GitHub users from the simulated GitHub REST API:

```bash theme={null}
curl http://github.local.wiremock.cloud/users
```

Again, you should see a JSON response, containing a list of user profiles.

## Clean up

To remove the WireMock Runner deployment:

```bash theme={null}
./delete-wiremock.sh
```

To delete the KIND cluster (if using a local cluster):

```bash theme={null}
kind delete cluster --name wiremock-demo
```

## Next steps

* Learn how to [record multiple APIs simultaneously](/runner/recording-multiple-apis-on-kubernetes) from within Kubernetes
* Learn how to [promote your mock APIs between environments](/runner/promoting-apis-with-git-and-ci) using Git and CI/CD.

## Additional resources

* Learn more about [Serve Mode](/runner/serve) configuration options
* Explore the [Runner Overview](/runner/overview) for other modes


# Serve Mode via the WireMock Runner
Source: https://docs.wiremock.io/runner/serve

How to use Serve Mode with the WireMock Runner

## Serve Mode

One of the Runner's available modes is `serve` mode.
The runner can be started in `serve` mode by setting the `WMC_DEFAULT_MODE` environment variable to `serve`,
or switched to this mode using the Runner's [switch endpoint](/runner/overview#switching-mode).
This mode starts a [local playback](/cli/local-playback) session that will continue to serve your configured services
until the runner is stopped or its mode is switched.

### Serve Configuration

The serve session started by the Runner can be configured via the same mechanism as the [`run` command](/cli/local-playback)
of the WireMock CLI - either [via a values file](/cli/overview#values-file) or [via environment variables](/cli/overview#environment-variables).
Additionally, configuration can be provided at switch time [via the HTTP request body](/runner/overview#mode-configuration).

All options available to the [`run` CLI command](/cli/local-playback) are also available to the Runner's `serve` mode.
When specifying an option in the [`"config"` field of the HTTP switch request](/runner/overview#mode-configuration), remove the dash (`-`) prefix that would normally be used when provided on the command line.
For instance, the [`--profile` option](/cli/environments) would become `"profile"` in the request body, like so:

```json theme={null}
{
  "mode": "record-many",
  "config": {
    "profile": "staging"
  }
}
```

Just like the WireMock CLI, by default the Runner will expect a WireMock environment file in the `.wiremock` directory
in the current working directory of the container.

### Starting the Runner In Serve Mode

When starting the runner in `serve` mode you will need to [publish the appropriate ports](https://docs.docker.com/reference/cli/docker/container/run/#publish)
for the services you are running along with the port you have configured for the Runner.

Here is a typical example on Linux or macOS when running the Runner on port `9999` and serving two services:

```shell theme={null}
docker run \
  -e WMC_DEFAULT_MODE='serve' \
  -e WMC_ADMIN_PORT='9999' \
  -e WMC_API_TOKEN='<wmc-api-token>' \
  -v ./.wiremock/:/work/.wiremock/ \
  -p 9999:9999 \
  -p 8080:8080 \
  -p 8081:8081 \
  wiremock/wiremock-runner:latest
```

## Telemetry

The WireMock Runner's `serve` mode can be configured to export OpenTelemetry signals to a backend of your choice.
Configuration is done via environment variables, as specified by [the OpenTelemetry specification](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/).

For example, to emit logs to a backend that supports [OTLP](https://opentelemetry.io/docs/specs/otel/protocol/)
at the endpoint `https://my-telemetry-service:8080`, set the following environment variables:

* `OTEL_LOGS_EXPORTER=otlp`.
* `OTEL_EXPORTER_OTLP_ENDPOINT=https://my-telemetry-service:8080`.

Supported values for `OTEL_TRACES_EXPORTER`, `OTEL_METRICS_EXPORTER`, `OTEL_LOGS_EXPORTER` are:

* `otlp`: [OTLP](https://opentelemetry.io/docs/specs/otel/protocol/exporter/)
* `console`: [Standard Output](https://opentelemetry.io/docs/specs/otel/logs/sdk_exporters/stdout/)
* `none`: No automatically configured exporter.

If no OTEL environment variables are set, the specification defaults are obeyed, except `OTEL_TRACES_EXPORTER`,
`OTEL_METRICS_EXPORTER`, and `OTEL_LOGS_EXPORTER`, which are all set to `none` by default, rather than `otlp`.

These telemetry options also apply to [the `wiremock run` command](/cli/local-playback#telemetry).


# Automated Testing with Java
Source: https://docs.wiremock.io/samples/automated-testing-with-java

Creating automated tests in Java and WireMock Cloud

Everything that can be done with WireMock Cloud's web UI can also be done via its APIs. This can be useful when automating
testing, as it allows stubs to be configured and torn down on-demans by individual test cases rather than it being
necessary to configure an entire test suite's stubs manually up-front. Working this way can make your tests a lot more
readable as it makes their preconditions explicit.

WireMock Cloud's API is 100% compatible with [WireMock's](http://wiremock.org/docs/api/). This means that WireMock
can be used as a Java client for WireMock Cloud.

## Adding WireMock to your project

WireMock is distributed in two different types of JAR - a standard "thin" JAR, and a "fat" standalone JAR. The latter of these
contains all of WireMock's dependencies and repackages (shades) most of these. Either can be used as a dependency in your
project and which you choose depends primarily on whether you have dependencies already present that conflict with WireMock's.
Picking the standalone version generally avoids these problems but at the cost of a larger JAR download.

If you're using Gradle you can add WireMock to your build file's dependencies as follows. Choose one of:

```
testImplementation 'org.wiremock:wiremock:3.12.1' // thin JAR
testImplementation 'org.wiremock:wiremock-standalone:3.12.1' // standalone JAR
```

Or if you're using Maven, choose one of:

```xml theme={null}
<!-- Thin JAR -->
<dependency>
    <groupId>org.wiremock</groupId>
    <artifactId>wiremock</artifactId>
    <version>3.12.1</version>
    <scope>test</scope>
</dependency>

<!-- Standalone JAR -->
<dependency>
    <groupId>org.wiremock</groupId>
    <artifactId>wiremock-standalone</artifactId>
    <version>3.12.1</version>
    <scope>test</scope>
</dependency>
```

## Configuring your test

After you've created a mock API in the WireMock Cloud UI, setting up a WireMock client to it is a one-line task (you can copy-paste this from
your mock API's Settings page):

```java theme={null}
// If admin API security disabled
WireMock paymentGatewayMock = new WireMock("https", "payments-example.wiremockapi.cloud", 443);

// If admin API security enabled
WireMock paymentGatewayMock = new WireMockBuilder()
    .scheme("https")
    .host("payments-example.wiremockapi.cloud")
    .port(443)
    .authenticator(new ClientTokenAuthenticator("lksdr91283rsdjkfh981"))
    .build();
```

Then in your test cases you can create stubs as [documented on the WireMock site](http://wiremock.org/docs/stubbing/):

```java theme={null}
paymentGatewayMock.register(post("/send-payment").willReturn(created()));
```

And make assertions about received requests:

```java theme={null}
paymentGatewayMock.verifyThat(postRequestedFor(urlPathEqualTo("/send-payment")));
```

## Programmatic stub creation

The same approach can be taken if you want to create stubs in your API programmatically.
This can be useful when you require a large number of stubs and don't want to create
them all by hand.

The example in the previous section creates an ephemeral stub i.e. one that isn't
stored persistently and will be deleted when the API is reset. To ensure that stubs
created programmatically are saved, simply call `persistent()` during creation:

```java theme={null}
myMockApi.register(get(urlPathEqualTo("/persist-this"))
    .persistent()
    .willReturn(ok("Some body content"))
);
```

## Example project

For a complete, working example of a Java web project using WireMock Cloud with automated tests see [the WireMock Cloud demo app](https://github.com/wiremock/wiremock-cloud-demo-app).


# Exploratory Testing With Spring Boot
Source: https://docs.wiremock.io/samples/exploratory-testing-tutorial

Exploratory testing a Spring Boot app with WireMock Cloud

This tutorial demonstrates how WireMock Cloud can be used to perform a manual exploratory test of an application with an API back-end.

The app is a simple to-do list based on Java and Spring Boot, supporting listing of to-do items and posting new ones. Any version off Spring Boot, such as spring boot 3, will suffice for this tutorial.

## Mock API setup

If you haven't yet created a mock API in WireMock Cloud, start by doing this. See [Getting Started](/overview#getting-started) for how to do this.
Make a note of the base URL from the Settings page (any of them will do).

## App setup

Ensure that you have Java 8+ installed and the `java` executable on your shell's `PATH`.

Clone the WireMock Cloud demo project and change the working directory to the newly checked out project:

```bash theme={null}
git clone git@github.com:wiremock/wiremock-cloud-demo-app.git
cd wiremock-cloud-demo-app
```

Edit `src/main/resources/application.properties` changing the `todo-api.baseurl` value to your mock API's base URL noted earlier.

Run the app:

```bash theme={null}
./gradlew bootRun
```

This should start the app locally on port `9000`.

## Step 1 - show a list of to do items

Navigate to the Stubs page and create a new stub with method `GET`, URL `/todo-items`, response `Content-Type` header `application/json` and the following JSON in the response body:

```json theme={null}
{
  "items": [
    {
      "id": "1",
      "description": "First item"
    },
    {
      "id": "2",
      "description": "Item number two"
    },
    {
      "id": "3",
      "description": "Do that number three thing"
    },
    {
      "id": "4",
      "description": "Don't forget the fourth thing on the list"
    }
  ]
}
```

Your stub should look something like this:

<img title="To do list stub" />

Once you've saved the stub, point your browser to [http://localhost:9000](http://localhost:9000).
You should see the to-do items in your response body listed in the page:

<img title="To do list" />

What has happened here is that the Spring Boot app has made a REST request to WireMock Cloud, which was matched by the stub you just created.
The stub returned a JSON response which the app parsed and rendered into an HTML page.

Now try modifying one or more of the item descriptions in the stub response and saving it, then refreshing the page. You should
immediately see your new items in the to-to list.

## Step 2 - simulating the posting of a new item

Next we're going to simulate a new item being added to the list via a POST request.

For this you'll need another new stub, this time for `POST` to `/todo-items` , response `Content-Type` header `application/json` and the following JSON in the response body:

```json theme={null}
{ "message": "Successfully sent new item." }
```

Your stub should look like this:

<img title="To do list POST stub" />

Once that's saved, go to the to-do list page and add a new item by typing a description in the field and clicking the button:

<img title="New to-do item" />

You should now see the success message you put in the stub response:

<img title="Success message" />

You'll notice that the contents of the list hasn't changed. This is because WireMock Cloud stubs aren't stateful - the app will load whatever is in the `GET /todo-items` stub you created at the start until you change it. However, if you visit the request log in the WireMock Cloud UI you can confirm that the request you expected actually arrived:

<img title="To do post request log" />

## Step 3 - posting a new item fails

In this step we're going to deliberately return an error from the API in order to test that the app behaves appropriately.

Navigate to the `POST /todo-items` stub you created in the previous step and clone it (using the Clone button at the end of the form).

In the newly cloned stub, expand the Advanced section and give the stub a higher priority - 4 or less will work as the default is 5.
The reason we need to do this is to ensure that this and not the OK posting stub we cloned from is guaranteed to match an incoming `POST /todo-items`.

In the response section change the response code to 502 and the message in the JSON body to something suitable:

<img title="To do list stub" />

Now try adding a new to-do item as you did in Step 2. When after submitting it, you should see an error page like this:

<img title="To do error" />


# How to build a mock REST API [Tutorial]
Source: https://docs.wiremock.io/samples/mock-rest-api

How to build an online mock REST API in WireMock Cloud for functional, integration and performance testing

REST is the dominant style of API at present and it's common for web,
mobile and microservice developers to have to integrate with at least a few and
sometimes many REST APIs to the the job done.

Inevitably this means that teams are delayed shipping new features when APIs aren't
finished, sandbox environments are down or test scenarios can't be run, so being
able to quickly deploy a mock API is essential to keep things moving.

In this tutorial you'll build a mock REST API from a fictitious contact manager,
which is suitable for integration, functional and performance testing.
You'll also implement common REST patterns and see how to solve common problems.

## Prerequisites

In order to follow this tutorial you'll need:

* A basic working knowledge of HTTP and REST
* An HTTP client for testing, such as [Postman](https://www.postman.com/)
  or [Insomnia](https://insomnia.rest/)
* Basic familiarity with [Regular Expressions](https://www.regular-expressions.info/)
* Ideally, some familiarity with [JSONPath](https://goessner.net/articles/JsonPath/), but
  this is not essential as it'll be explained in the places it's used.

## Setting up

Firstly, you'll need to [sign up for a WireMock Cloud account](https://app.wiremock.cloud/login?for=signup) if you don't already have one.

Once you've signed up or logged back in, create a blank mock API in the app.

<div>
  <h3>tl;dr</h3>

  If you just want to take a look at the end result of this tutorial you can select
  the <strong>"rest-example"</strong> API template instead of "blank" when when creating a new mock API.

  <img alt="Example REST API template" />
</div>

After creating a new mock API you'll be taken to the Settings page where you can find
its base URLs (one for HTTP one for HTTPS):

<img alt="Base URL" />

You can check that your new API is live by copying the base URL by clicking the icon
to the right of the box and making a request from your HTTP client (e.g. Postman):

<img alt="Postman request to empty API" />

## Basic contact list

A contact manager application is likely to have the ability to list all stored contacts.
Let's assume our imaginary API responds to `GET /v1/contacts` with JSON like:

```json theme={null}
{
  "contacts": [
    {
      "id": "11111",
      "firstName": "Tom",
      "lastName": "Smith",
      "email": "tom.smith@example.com",
      "dateAdded": "2021-01-03",
      "companyId": "123"
    },
    {
      "id": "22222",
      "firstName": "Suki",
      "lastName": "Patel",
      "email": "spatel@example.com",
      "dateAdded": "2020-11-12",
      "companyId": "123"
    },
    {
      "id": "33333",
      "firstName": "Lexine",
      "lastName": "Barnfield",
      "email": "barnfield8@example.com",
      "dateAdded": "2021-01-03",
      "companyId": "234"
    }
  ]
}
```

We can simulate this by creating a basic stub, matched on a `GET` with the exact
URL path `/v1/contacts`. Go to the Stubs page under your new mock API and hit the
new stub button:
<img alt="Create new stub" />.

Then in the request section, set the method to `GET`, the URL to `/v1/contacts`
and the URL match type to `Path`:

<img alt="Contact list stub request" />

In the response section put the JSON in the body field, and for good measure
we'll also send a `Content-Type: application/json` header:

<img alt="Contact list stub response" />

After hitting Save, you can now test the stub using WireMock Cloud's Test Requester or
your preferred HTTP client:

<img alt="Contact list test request" />

## Filtering via query parameters

REST APIs often allow collection resources like the contact list to be filtered
using parameters in the request's query string.

For instance, so that we can find contacts for a specific company our contact
manager might support filtering by company ID. For instance `/v1/contacts?companyId=123`
would return:

```json theme={null}
{
  "contacts": [
    {
      "id": "11111",
      "firstName": "Tom",
      "lastName": "Smith",
      "email": "tom.smith@example.com",
      "dateAdded": "2021-01-03",
      "companyId": "123"
    },
    {
      "id": "22222",
      "firstName": "Suki",
      "lastName": "Patel",
      "email": "spatel@example.com",
      "dateAdded": "2020-11-12",
      "companyId": "123"
    }
  ]
}
```

We'll simulate this by creating a similar stub to the first one, but with a
query parameter match and the filtered JSON document in the response body. To save some time we can
clone the first stub rather than starting from scratch, which can be done by
clicking Clone Stub at the bottom of the stub form.

Then we add a query parameter match for `companyId` equalling `123`:

<img alt="Query parameter matching" />

And finally paste the filtered JSON in the body field:

<img alt="Query parameter matching" />

You can find more detail on [matching different parts of incoming requests here](/advanced-stubbing/#advanced-request-parameter-matching).

[See here for the full list of available request matchers](/request-matching/matcher-types/) (such as `equalTo` and `contains`).

## Getting an individual contact

It's also very common for REST APIs to support retrieval of individual items of
data specified by an identifier in the URL path, so in our case we might fetch an
individual contact via a `GET` to `/v1/contacts/22222`.

We can stub a single data item in a very similar manner to the contact list we
created first, relying on exact URL path equality to match the request:

<img alt="Single contact request" />

<img alt="Single contact response" />

## Using URL regex matching and response templating to simulate many data records

If you only need to be able to return a small number of individual contacts then the above
approach of creating a stub per contact will work OK.

However, you may need return many
unique contact records e.g. because you're performance testing and want to spread
the load across realistic data volumes. In this instance you can use URL regex
matching and response templating to simulate the presence of many data items.

Let's modify the single contact stub we've already created. First we'll switch to
a looser URL match using the `Path regex` URL match type with the regular expression `/v1/contacts/[0-9]{1,10}` as the value.
This will match any URL path starting with `/v1/contacts` and ending with any
numeric ID between 1 and 10 characters long:

<img alt="Templated contact request" />

Then we'll enable templating in the response by ticking "Enable templating" and
make the response body more dynamic by replacing some elements with template helpers, giving us:

```json theme={null}
{
  "contact": {
      "id": "{{{request.pathSegments.2}}}",
      "firstName": "{{{randomValue length=6 type='ALPHANUMERIC'}}}",
      "lastName": "{{{randomValue length=10 type='ALPHANUMERIC'}}}",
      "email": "{{{randomValue length=12 type='ALPHANUMERIC'}}}@example.com",
      "dateAdded": "{{{now offset='-3 months' format='yyyy-MM-dd'}}}",
      "companyId": "123"
    }
}
```

<img alt="Templated contact response" />

Now we can make a test request with any valid ID value (numeric, 1-10 characters)
and will receive a response with the ID field matching the value in the request URL
and some of the data randomised:

<img alt="Templated contact test request" />

Unpacking what we've done here:

* `id` is now set from the 3rd segment of the incoming request URL's path, so it will always be the same as the requested contact ID.
* `firstName`, `lastName` and `email` are now random alphanumeric text (with a fixed domain name in the case of `email`).
* `dateAdded` is set to 3 months before today's date.

You can [learn more about response templating here](../response-templating/basics/) and [more about URL matching here](../request-matching/url/).

## Creating a new contact

At some point our contact manager API will need to be able to accept new contacts
in addition to just returning them. Commonly, REST APIs support sending a `POST`
request to the URL for a collection resource as a means to add new data items.

So our contact manager might accept `POST /v1/contacts`, returning a
response with status code `201 Created` and an empty body:

<img alt="New contact POST" />

### More specific matching

In its current state, this stub will be matched regardless of the contents
of the request body, so a body with incorrectly structured JSON, XML or even no body
at all will still yield the `201` response.

If we want to ensure the stub is only matched when correctly structured JSON is
sent in the request but without requiring a set of exact values, we can add a body
matcher by clicking New body matcher and using JSONUnit as wildcards:

```json theme={null}
{
  "contact": {
      "id": "${json-unit.any-string}",
      "firstName": "${json-unit.any-string}",
      "lastName": "${json-unit.any-string}",
      "email": "${json-unit.regex}[a-z0-9+_.-]+@[^.]+\\.[^.]+$",
      "dateAdded": "${json-unit.regex}[0-9]{4}-[0-9]{2}-[0-9]{2}",
      "companyId": "${json-unit.any-string}"
    }
}
```

<img alt="New contact body pattern" />

Now if we make a request containing an incorrect JSON field (`name` instead of
`firstName` and `lastName`), we'll get a `404 Not Found` response
containing a diff report showing which part of the request didn't match:

<img alt="Contact POST mismatch" />

## Simulating state changes

When posting a new item of data to a real API we'd expect it to be
stored and therefore returned on a subsequent `GET` request for
the collection or the individual resource. However, mock APIs by default don't
store any state, so making a request to add a new contact will have no effect on
the data returned later.

For most testing scenarios this isn't an issue, but in cases where more realistic
behaviour is required WireMock Cloud supports the concept of "stateful scenarios" whereby
the state of a scenario can be used to determine which stub to match.

If we wanted to, for instance, create a test case in which posting a new company
results in it appearing in the companies collection we can achieve this by creating three
stubs, all associated with the same scenario.

Firstly, we'd stub the initial response for `GET /v1/companies` (in much the same manner as we did
for contacts), returning a single company in the collection:

```json theme={null}
{
  "companies": [
    {
      "id": 123,
      "name": "Boring Corp"
    }
  ]
}
```

This time we'd put the stub in a scenario called "Companies" (the name is not important)
and require that the scenario be in the "Started" state in order for the stub to match:

<img alt="Companies scenario 1" />

Next, we'd create a second `GET` stub cloned from the first but with a second
company added to the collection:

```json theme={null}
{
  "companies": [
    {
      "id": 123,
      "name": "Boring Corp"
    },
    {
      "id": 234,
      "name": "Az Tech"
    }
  ]
}
```

This stub would also be in the "Companies" scenario but this time with a different
required state:

<img alt="Companies scenario 2" />

Finally, we'd configure the stub that handles the `POST` to advance the state of the scenario
so that it appears to have the effect of storing the new company:

<img alt="Companies scenario 2" />

### Testing the scenario

The first time we make a request to `GET` our companies we should see a single item in the collection:

<img alt="Companies list in state 1" />

Then we `POST` a new company:

<img alt="New company POST with state change" />

Then when we fetch the companies list a second time we should see two companies
returned:

<img alt="Companies list in state 2" />

The scenario will now remain in state "2 companies" until it is manually reset,
which you can do by clicking Reset All Scenarios, which resets all scenarios to "Started".

You can [find out more about Scenarios here](../dynamic-state/stateful-scenarios/).

## Returning errors for specific requests

Sometimes we want to be able to support negative tests, for instance when the
API we're calling returns an error rather than the expected response. We can configure our mock API to return errors in response to specific requests
with the help of the priority stub parameter.

Let's suppose we want to test the case where our app tries to post a new contact
but the API returns a `503 Service Unavailable` response instead of the expected `201`.
If we configure a stub that expects specific data in the request body and give it
a higher priority than the existing `POST` stub that returns `201` then we can
send a request with appropriate data and see the error returned.

Start by cloning the existing `POST` stub for new contacts. Change the Priority value to a number
lower than `5` (`1` is highest).

<img alt="Raised stub priority" />

Then we'll modify the body matcher so that it'll only
match when a specific piece of data is sent. One option here would be to substitute
the placeholders in the `equalToJson` body match we already have and this would
work fine if we were confident our test could produce exactly the same values each time.
However, we can give ourselves a bit more flexibility by choosing one specific bit of
data and matching it using `matchesJsonPath`.

Let's say that if we receive a specific contact ID then we'll trigger the error.
To do this, change the body match type to `matchesJsonPath` and the expression to
`$.contact.id` `equalTo` `666`:

<img alt="Matching on JSONPath" />

Finally, change the response status code to `503`, and let's also add a plain text
error message supported by a `Content-Type: text/plain` header:

<img alt="Error 503 response" />

### Testing the error response

Now we can send a test request and see the error response returned:

<img alt="Error 503 response" />

<Note>The message in the red text in this case indicates that WireMock Cloud couldn't automatically generate a valid request body to match our JSONPath expression. This can be safely ignored as we've created our own request body.</Note>

### Other types of error

You can also simulate lower-level errors with WireMock Cloud such as dropped network
connections and delays. You can [learn more about faults here](../simulating-faults/).

## Conclusion

You've now built a mock of a REST API which can be used in a variety of testing scenarios,
and it hopefully it's possible to see how this approach could be applied to mocking
your own APIs or those of your suppliers and partners.

You could also try expanding the scope of the API by mocking more resources and test more
negative cases using faults, delays and other not-OK HTTP status codes.


# Key management
Source: https://docs.wiremock.io/security/key-management

Securing your mock API integrations.

When using external integrations with WireMock Cloud, the communication between WireMock Cloud and these integrated services
must be secured.

WireMock Cloud provides the means to generate, moderate and attach asymmetric keys to facilitate this secure communication.

## Usage

For a key to be of use it must be attached to something that requires secure authentication with a third party.
Currently, the only place in WireMock Cloud where a key can be attached is a mock API's [OpenAPI Git integration](/openAPI/openapi-git-integration).

Instructions for attaching a key to an OpenAPI Git integration can be found [here](/openAPI/openapi-git-integration#configuring-your-git-integration).

## Managing your keys

To view the keys you have access to, navigate to the security page in WireMock Cloud via your account avatar in the top
right and click on the `Keys` tab.

<img alt="Security page navigation" />

<img alt="Keys list page" />

From this page you can create new keys, page between existing keys, and delete keys, as well as search for specific
keys by name.

### Creating new keys

Clicking the `Create new key` button on the main keys page will take you to a new page containing a form to enter the
desired name of the new key.

<img alt="Creating a new key" />

Saving this new key will generate a secure key pair, and the public key for this key pair will be displayed.

<img alt="Viewing your new key" />

This key can then be [attached to other parts of WireMock Cloud](#usage).

The private key is stored in encrypted form and only decrypted briefly when in use via a secure decryption service.

### Moderating existing keys

To view and update a key, click on its name from the main key page.

<img alt="Navigating to a key" />

From here, a key's name can be updated, and the key can be shared with others in your organisation.

<img alt="Key share button" />

<img alt="Sharing a key" />


# The OAuth2 / OpenID Connect Mock
Source: https://docs.wiremock.io/security/oauth2-mock

Using the OAuth2 / OpenID Connect Mock

<img alt="OAuth2" />.    &#x20;

This is a simulation of an **OAuth2** / **OpenID Connect** login service that you can use as a **drop-in replacement** for the real thing during testing. It's free to use, and completely stateless so can accommodate virtually any number of concurrent clients (at least until the server runs out of breath!).

Currently the `authorization_code` (server-side web) OAuth2 flow is supported.

## Using with your app

Start by finding the OAuth2 configuration in your app's server-side component. Where this is located
varies from app to app - sometimes it can be found in a configuration file, other times it is set
directly in code. If you're using an SDK from your login service, you may need to override the defaults this provides.

Set the following values:

* Authorization URI: [`https://oauth.wiremockapi.cloud/oauth/authorize`](https://oauth.wiremockapi.cloud/oauth/authorize)

* Token URI: [`https://oauth.wiremockapi.cloud/oauth/token`](https://oauth.wiremockapi.cloud/oauth/token)

* User info URI: [`https://oauth.wiremockapi.cloud/userinfo`](https://oauth.wiremockapi.cloud/userinfo)

* JWKS URI: [`https://oauth.wiremockapi.cloud/.well-known/jwks.json`](https://oauth.wiremockapi.cloud/.well-known/jwks.json)

You can [see here](https://github.com/wiremock/wiremock-cloud-demo-app/blob/master/src/main/resources/application.yml#L8) how this is done in a Spring Boot application.

After that, when you start the login process from your app you should be sent to
a simulated login page, rather than the one belonging to your real provider. You
can log in with any email address and password you like, real or not.

<img alt="" />

## Questions and feedback

If you're not sure how something works or have a suggestion for improving this simulation, please get in touch with us
via [info@wiremock.io](mailto:info@wiremock.io) or the chat widget.


# The SAML Identity Provider Mock
Source: https://docs.wiremock.io/security/saml-idp-mock

How to mock a SAML Identity Provider

<img alt="SAML IDP" />

These instructions will help you set up a SAML Identity Provider Mock in your WireMock Cloud account.

The SAML IDP Mock is a template that simulates a SAML Identity Provider (IdP). It
generates signed SAML responses with configurable user attributes, making it suitable
for testing SAML-based SSO integrations without needing a real IdP.

Instructions are provided for using it as an Auth0 Enterprise Connection, but should be
broadly applicable to use with any other Service Provider (SP).

## Setting up the mock

To set up the SAML Identity Provider Mock in your WireMock Cloud account, follow these steps:

1. Log in to you [WireMock Cloud](https://app.wiremock.cloud/mock-apis) account.
2. Click **Create new mock API**.
3. On the `Choose protocol` screen, choose `Template library`.

<img alt="Choose Template" />

4. On the template library screen, search for `SAML` and click **Create Mock API** on the `SAML IDP` template.

<img alt="Search Templates" />

5. Give your mock API a name and click **Continue**.
6. This will create the mock API from the template in your WireMock Cloud account.

## How it works

The template provides an interactive web UI with a three-step flow:

1. **Instructions** (`/`) — Setup guide for connecting the mock IdP to your Service Provider (e.g. Auth0)
2. **Login** (`/login`) — A form to configure the post-back URL, email address, and optional extra SAML attributes
3. **Send Response** (`/send-response`) — Builds a signed SAML response and POSTs it back to your SP's ACS URL

The mock IdP also serves its X.509 signing certificate at `/certificate.pem`.

## SAML response structure

The response includes:

* **Issuer** — mock API's base URL
* **Subject** — NameID using email (format: `emailAddress`)
* **Conditions** — NotBefore (now - 1 min), NotOnOrAfter (now + 5 min), with audience from the SAML request
* **Attributes** — `email` attribute plus any extra `<saml:Attribute>` tags from the login form
* **AuthnStatement** — `PasswordProtectedTransport` context class
* **Signature** — SHA-256 digest, RSA-SHA256 signature, enveloped signature transform

## Setup

To set up the SAML Identity Provider Mock as an Enterprise Connection, copy the base URL
of the mock API and open it in your browser.  You should see a page with instructions for
setting up the connection.

<img alt="Copy Base URL" />

You will see the following instructions:

<img alt="Instructions" />

1. Download the signing certificate from `/certificate.pem`
2. In Auth0, navigate to **Authentication** > **Enterprise**, click **SAML** > **Create**
3. Set **Sign In URL** to `<mock api base url>/login`
4. Upload the certificate from step 1
5. Toggle off **Enable Sign Out** and **Sign Request**
6. Click **Create**

In the `Login Experience` tab you should specify your domain in the `Identity Provider domains` field
and remember to toggle on the applications you want to associate with this connection in the `Applications` tab.

## Using with your app

1. Login to your application using an account with an email address that matches the domain you specified in the connection setup.
2. This should recognize the connection associated with the domain and redirect you to the `/login` page of the mock IdP.
3. This will display the following form:

<img alt="Login Form" />

1. Fill out the post-back URL as defined by your IDP.  **This is a required field**. This is likely to be the same
   across all authentication requests for the same domain/connection.  If this is the case you could update the response template to
   hardcode this value.
2. Enter the email address of the user you want to authenticate. **This is a required field**.
3. The `Extra attribute(s)` allows you to send arbitrary extra `<saml:Attribute>` tags.
   It is important to remove all whitespace to ensure SAML hashing and signing work correctly.  For example

```xml theme={null}
<saml:Attribute Name="groups"><saml:AttributeValue>admins</saml:AttributeValue><saml:AttributeValue>developers</saml:AttributeValue><saml:AttributeValue>finance</saml:AttributeValue></saml:Attribute>
```

Once you have filled out the form, click on the `Build SAML Response` button. This will
take you to the `/send-response` page of the mock IdP, showing the SAML response that was built.

<img alt="SAML Response" />

This form shows you the SAML response that was built along with the parsed values for you to use for debugging if required.
Click on the `Send SAML Response to Service Provider` button to send the response back to your SP.

You should then be authenticated and redirected back to your application.

## Questions and feedback

If you're not sure how something works or have a suggestion for improving this simulation, please get in touch with us
via [info@wiremock.io](mailto:info@wiremock.io) or the chat widget.


# API Security Overview
Source: https://docs.wiremock.io/security/security

WireMock Cloud's simulation and admin API security and how to work with it

WireMock Cloud supports separately configurable authentication on the stub serving
and admin interface for each mock API.

## Admin API security

Every mock API created has its own admin API (think of it as a standalone WireMock server per API), which is used for stubbing, verification, reset and a few other things.
This has the same base URL as your mock API, with a base path of `/__admin` e.g. `https://example.wiremockapi.cloud/__admin`.

By default this is secured using the API token that can be found in [https://app.wiremock.cloud/account/security](https://app.wiremock.cloud/account/security).

The token can either be sent in an Authorization header e.g.

`Authorization:Token 1kj3h98f7sihjfsf`

or as a query parameter e.g.

`https://example.wiremockapi.cloud/__admin/mappings?apiToken=1kj3h98f7sihjfsf`.

It is recommended that you use the header approach where possible as this reduces the risk of the key appearing in log files an browser histories.

### Disabling admin security

Admin API security can be disabled from the Settings page for the API:

<img title="Security toggle" />

<Note>Admin API security will be disabled by default for APIs created prior to the security feature being released.</Note>

## Mock API security

Mock APIs can optionally be configured to authenticate callers. At present this can
be via HTTP Basic authentication (username + password) or an arbitrary header match,
as well as OpenID Connect authentication for [Enterprise plan users](https://www.wiremock.io/get-pricing).

### HTTP Basic authentication

<img title="HTTP Basic authentication" />

HTTP Basic is a widely supported part of the HTTP standard supporting username/password authentication.
An HTTP resource secured with HTTP Basic will result in a browser prompting the user
with a username/password dialogue box on their initial visit.

Alternatively, an API client can pre-emptively authenticate by sending a header of the form
`Authorization:Basic <base64 encoded username:password>`.

### Header match authentication

<img title="Header match authentication" />

WireMock Cloud can also authenticate requests based on a match expression against any header.
The match expression works in the same way as header matches in the stub creation form,
whereby you specify the header name, predicate and expected value.

### OpenID Connect authentication

<img title="OpenID Connect authentication" />

For [Enterprise plan users](https://www.wiremock.io/get-pricing), WireMock Cloud can authenticate requests via an
OpenID Connect authorization server.
Requests must contain an HTTP header whose value is a [JWT](https://jwt.io) generated by the configured authorization
server.
The value of the Authorization header field must be the name of the HTTP header that will contain the JWT (usually
`Authorization`, but any valid HTTP header name is allowed).
The value of the Issuer URL field must be the base URL of the authorization server.

The authorization server is expected to be configured as per
[the OpenID Connect specification](https://openid.net/specs/openid-connect-discovery-1_0.html).
Specifically `/.well-known/openid-configuration` contains the required configuration information, including the URL to
the JSON Web Key Set (JWKS) that contains the key(s) to verify the JWTs' signatures.

The value of the Audiences field can optionally be a set of required audiences.
If this field's value is non-empty, every JWT's
[`aud` claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3) must contain all of these audiences for the
JWT to be considered valid.


# Teams and Collaboration
Source: https://docs.wiremock.io/security/teams-and-collaboration

Working with teams & sharing Mock APIs in WireMock Cloud

The basic unit of ownership in WireMock Cloud is the Organisation. Mock APIs,
users and teams all belong to a single organisation. View your organisation by
clicking on the [Organisation page](https://app.wiremock.cloud/account/organisation) under your account.

Here you will see all the teams and users in your organisation:

<img title="Organisation details" />

There are two roles for users in an organisation: **Member** and **Admin**.

A **Member** can create and interact with mock APIs, API templates and teams.

In addition an **Admin** can:

* invite other users to the organisation
* remove users from the organisation (provided at least one Admin remains)
* change the role of any member of the organisation (provided at least one Admin
  remains)
* administer all mock APIs, teams and other resources belonging to the
  organisation

### Inviting users

An admin can enter the email address of a person not yet in the organisation,
and a role, to invite that person to join the organisation. They will then show
up in the "Pending Invites" section.

Organisation members and pending invitations count towards your subscription plan's total number
of seats. You can see your usage and limits on the [Usage page](https://app.wiremock.cloud/account/usage) under your account.

<img title="Subscription plan usage" />

## Teams

Any member of an organisation can create a team (provided the organisation is on
a plan which allows multiple members).

The person who creates the Team will automatically be given the Admin
role on that team. In addition all organisation admins can administer a team.

There are two roles for users in a team: **Member** and **Admin**.

A **Member** will inherit whatever permissions the team has been granted.

In addition an **Admin** can:

* add other members of the organisation to the team
* remove users from the team
* change the role of any member of the team

An organisation admin can enter the email address of a person not yet in the
organisation, and a role, to simultaneously invite that person to join the
organisation *and* add them to the team.

## Mock APIs

Any member of an organisation can create a mock API.

The person who creates the mock API will automatically be given the Admin
role on that mock API. In addition all organisation admins can administer a mock
API.

Mock APIs can be shared with other members of your organisation by clicking the
"Share" button on the API:

<img title="Share Mock API with others" />

Mock APIs can be shared with "All in organisation", any of the Teams
belonging to the same organisation as the mock API, and any individual members of the organisation.

When sharing a mock API, you can choose the role of the organisation, team or
person you are sharing the API with as one of **Admin**, **Write** or **Read**.

* **Read** allows: viewing the API, its stubs, and who else has permissions on it.

* **Write** also allows changing the settings of the API, and adding, changing or
  deleting the stubs on the API.

* **Admin** also allows deleting the mock API, and adding & removing people, teams & the organisation, or
  changing their roles, in the "Share" widget.

An organisation admin can enter the email address of a person not yet in the
organisation, and a role, to simultaneously invite that person to join the
organisation *and* give them that role on the mock API.

## Single Sign-on (SSO)

WireMock Cloud supports auto-provisioning and SSO for user management via any SAML 2.x capable IdP.


# Simulating Faults
Source: https://docs.wiremock.io/simulating-faults

Responding with network and HTTP faults

Real-world APIs and the networks used to communicate with them can fail in ways that can destabilise your application,
and are hard to test.

WireMock Cloud supports responding to requests with four different fault types:

* Server closes connection before response sent
* Corrupt data sent, then connection closed
* OK response sent, followed by corrupt data and connection close
* Peer connection reset - `SO_LINGER` is set to 0 causing a non-graceful TCP connection termination.

These are configured per stub, so it is possible to respond to specific requests with a fault.

## Usage

Faults are configured when creating or editing a stub by selecting the Fault tab in the response and choosing the fault type:

<img title="Fault response" />


# Simulating SOAP services
Source: https://docs.wiremock.io/soap-stubbing

Matching SOAP requests and sending SOAP responses

Stubbing a SOAP response is similar in most respects to stubbing a REST response. The main difference is that the HTTP method
and URL alone are not enough to differentiate requests since these are always the same for a given endpoint.

In addition, we need to match on the `SOAPAction` header and the request body XML.

## Using the SOAPAction header

SOAP APIs typically use the `SOAPAction` header to select the appropriate action for the call.
Although you can sometimes avoid this, it's usually a good idea to add a header match for `SOAPAction` as it's more
efficient and faster than relying exclusively on the XML body.

<img title="Matching the SOAPAction header" />

## Matching the request body with XML equality

When dealing with request bodies that are small and have no data of a transient nature (e.g. transaction IDs or today's date)
`equalToXml` is a straightforward way to specify a match.

For instance given a SOAP service for managing a to do list, you may wish to mock an interaction matching a specific request to add an item:

<img title="SOAP request" />

Which returns a success response:

<img title="SOAP response" />

Testing this returns the expected XML response:

```
$ curl -X POST -d '<?xml version="1.0"?>
<soap-env:Envelope xmlns:soap-env="http://www.w3.org/2001/12/soap-envelope" soap-env:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

   <soap-env:Body xmlns:m="http://example.company/todo" >
      <m:AddToDoItem>
         <m:ToDoItem>Have a wash</m:ToDoItem>
      </m:AddToDoItem>
   </soap-env:Body>

</soap-env:Envelope>' -H 'SOAPAction: "http://example.company/todo/AddToDoItem"' http://example.wiremockapi.cloud/soap-example -v

> POST /soap-example HTTP/1.1
> Host: example.wiremockapi.cloud
> User-Agent: curl/7.54.0
> Accept: */*
> SOAPAction: "http://example.company/todo/AddToDoItem"
> Content-Length: 355
> Content-Type: application/x-www-form-urlencoded
>
* upload completely sent off: 355 out of 355 bytes
< HTTP/1.1 200 OK
< Transfer-Encoding: chunked
<
<?xml version="1.0"?>
<soap-env:Envelope xmlns:soap-env="http://www.w3.org/2001/12/soap-envelope" soap-env:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

   <soap-env:Body xmlns:m="http://example.company/todo" >
      <m:AddToDoResult>Item "Have a wash" successfully added</m:AddToDoResult>
   </soap-env:Body>

</soap-env:Envelope>
```

### Using placeholders to ignore transient values

The above example works fine when the request body doesn't contain any transient data
such as transaction IDs or the current date. However, if data that changes on each
request is introduced it will be necessary allow a match to occur regardless of the
actual value received.

One way to do this is to use [placeholders](./advanced-stubbing/#xml-placeholders).
Let's assume the request body of our API now contains a `TransactionId` element, which
must be a unique value for each request e.g.:

```xml theme={null}
<?xml version="1.0"?>
<soap-env:Envelope xmlns:soap-env="http://www.w3.org/2001/12/soap-envelope"
  soap-env:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

   <soap-env:Body xmlns:m="http://example.company/todo">
      <m:TransactionId>1ea094dd-9548-4a79-a43c-b44670f955c6</m:TransactionId>
      <m:AddToDoItem>
         <m:ToDoItem>Have a wash</m:ToDoItem>
      </m:AddToDoItem>
   </soap-env:Body>

</soap-env:Envelope>
```

We can ignore this value by ticking the "Enable XMLUnit placeholders" box and
putting an ignore token into the expected XML in the form:

```xml theme={null}
<m:TransactionId>${xmlunit.ignore}</m:TransactionId>
```

<img title="SOAP request XML with placeholders" />

## Matching the request body with XPath

When working with large SOAP requests `equalToXml` can become quite slow as it must perform a comparison on every node in the XML document.

It's often faster to match specific elements within the document using the `matchesXPath` operator,
and since this is a much looser approach to matching it's another way to solve
the problem described above where frequently changing values are present.

When matching using XPath, your aim should be to target as few elements/attributes as possible while being able
to reliably distinguish between requests.

Given the same request body as in the previous section, we could use the following
XPath to match just on the value of the `m:ToDoItem` element:

```xpath theme={null}
//AddToDoItem/ToDoItem[text()='Have a wash']
```

<img title="Matching with XPath" />

### Using multiple XPath expressions

Sometimes you need to match on more than one XML element to be able to adequately
distinguish between requests. Although XPath supports multiple predicates with logical and/or,
often it can be easier to use multiple body matchers each targeting a single element.

Suppose we added a `UserId` field that we also wanted to target:

```xml theme={null}
<?xml version="1.0"?>
<soap-env:Envelope xmlns:soap-env="http://www.w3.org/2001/12/soap-envelope"
  soap-env:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

   <soap-env:Body xmlns:m="http://example.company/todo">
      <m:TransactionId>1ea094dd-9548-4a79-a43c-b44670f955c6</m:TransactionId>
      <m:UserId>abc123</m:UserId>
      <m:AddToDoItem>
         <m:ToDoItem>Have a wash</m:ToDoItem>
      </m:AddToDoItem>
   </soap-env:Body>

</soap-env:Envelope>
```

We could add one `matchesXPath` body pattern for each of the elements we
care about:

<img title="Matching with multiple XPaths" />

### A gotcha - the recursive selector: //

Given the above XML document, you might expect the following XPath expression to
produce a match:

```xpath theme={null}
//UserId[text()='abc123']
```

However, due to a quirk of how XML documents with namespaces are evaluated this won't work.
Ensuring that you select at least one node beneath the element searched for recursively
will fix this, so the above XPath can be corrected like this:

```xpath theme={null}
//UserId/text()[.='abc123']
```


# Stubbing Basics
Source: https://docs.wiremock.io/stubbing

Overview of WireMock Cloud's stubbing capabilities

WireMock Cloud at its core, like [WireMock](https://wiremock.org) which underpins it is an HTTP stubbing tool. This means that it can be configured to return specific canned responses depending on the request.

This can be a simple as just matching the URL, right up to a combination of URL, header and body matches using regexes, JSONPath, XPath and others.

## Creating a basic stub

Select the mock API you'd like to work in, then navigate to the Stubs page and hit the New Stub button. Change the URL field from thedefault value to whatever you'd like to match on e.g. `/hello-world`.

<img alt="basic-new-stub" title="New Stub Request" />

In the Response section, set HTTP status, headers and body text. Typically it is a good idea to send a `Content-Type` header in HTTP responses, so add one by clicking New Header and setting `Content-Type` to `application/json`.

<img alt="Basic response" />

Hit Save, then you're ready to test your stub. Point your browser to `http://<your-subdomain>.wiremockapi.cloud/hello-world`.
You should see the text that you entered into the body text box. You can find out what your
subdomain is on the Settings page for the mock API.

<img alt="Mock response served" />


# Managing Teams and Members
Source: https://docs.wiremock.io/teams-and-members

Creating, fetching and deleting teams and team members via the API

## Adding a member to a team

Follow these steps to find a specific user and team, then add the user to the team:

<Steps>
  <Step title="Get our organisation ID">
    Follow the steps in [finding your organisation ID](/organisation-info-and-members#finding-your-organisation-id) to retrieve
    your organisation's ID.
  </Step>

  <Step title="Find the ID of the team">
    List the organisations in your team by calling [get all teams in an organisation](/api-reference/teams/get-all-teams-in-an-organisation),
    then find the team you wish to use and read the `id` field.
  </Step>

  <Step title="Find the user">
    Find the user you wish to add to the team using [get users in an organisation](/api-reference/organisations/get-users-in-an-organisation).
    You can optionally pass the query parameter `q` which will filter the results to those whose username or email address
    at least partially matches the value.
  </Step>

  <Step title="Add the user to the team">
    Taking the data captured from the previous steps, call [add team member](/api-reference/teams/add-team-member).
  </Step>
</Steps>

## Removing a member from a team

A user can be removed from a team by first following the data collection steps described above, then calling
[delete a team member](/api-reference/teams/delete-a-team-member).


# Product Usage Data
Source: https://docs.wiremock.io/usage

Get data about your organisation's use of the product

<RequestExample>
  ```
  GET https://api.wiremock.cloud/v1/subscriptions/{subscriptionId}/usage
  Authorization: Token <api-key>
  Accept: application/json
  ```
</RequestExample>

<ResponseExample>
  ```json theme={null}
  {
    "usage": {
      "id": "kl1g9",
      "currentPeriodStart": "2024-08-01T13:50:48.988681Z",
      "currentPeriodEnd": "2025-08-01T13:50:48.988681Z",
      "stubCalledCount": 22309,
      "exportCalledCount": 30,
      "organisationMemberCount": 15,
      "invitationCount": 0,
      "seatLimit": null,
      "totalMockApiCount": 158,
      "totalDataSourceCount": 9,
      "ownMockApiCount": 0,
      "teamMockApiCount": 0,
      "collaboratorCount": 0,
      "totalSeatCount": 15,
      "teamMemberCount": 15,
      "totalTeamCount": 15
    }
  }
  ```
</ResponseExample>

You can use the API to retrieve various metrics about your organisation's use of the product. This corresponds to the data
you can see on the [usage page](https://app.wiremock.cloud/account/usage) in the app.

## Getting usage data

Usage data is associated with your organisation's subscription. Follow these steps to find the subscription ID and then use this
to retrive product usage data:

<Steps>
  <Step title="Get our user account">
    first getting our own user account by calling [get self](/api-reference/users/get-self), which will return
    a redirect to our user account resource. Follow this redirect to retrieve user account details and from here get the organisation ID.
  </Step>

  <Step title="Get the organisation">
    Using the organisation ID from the previous step call [get organisation](/api-reference/organisations/get-organisation-by-id)
    using the ID as the path parameter. This will return organisation information including the subscription ID, which we
    record for the next step.
  </Step>

  <Step title="Get product usage for the subscription">
    We can then use the subscription ID as the path parameter when calling [get usage](/api-reference/usage/get-usage) to get the actual usage data.
  </Step>
</Steps>


# User Info
Source: https://docs.wiremock.io/user-info

Getting and updating user account information

## Finding your own user details

You can find your own user account information by calling the [get self](/api-reference/users/get-self),
ensuring you follow the redirect.

## Finding users within your organisation

You can get all the users in your organisation or find a selection of these via their username or email address using
[get users in organisation](/api-reference/organisations/get-users-in-an-organisation).


# User Configurable Rate Limits
Source: https://docs.wiremock.io/user-rate-limits

Configuring your own rate limiters in order to simulate the real thing.

You can configure your own rate limiters and apply them to your stubs, allowing
you to simulate the real-world rate limiters protecting the APIs you're mocking.

## Add rate limits to a mock api

Rate limits are defined in your mock api settings page.

You can choose one of your rate limits to be the default rate limit for the mock API, which means it will apply to all stubs, unless a different rate limit is selected for a specific stub.

<img title="Rate limit settings" />

Once created rate limit names cannot be changed as then name is used as the unique identifier
when assigning to a stub.

If you would like to update the name please create a new rate limit
and attached to the new rate limit to your stub.

## Add rate limit to a stub

Rate limits can be applied to a stub in the "Response" section.

<img title="Rate limit settings" />

Stubs will by default have either no rate limit, or the default rate limit selected at the API level.

Even if the API has a default rate limit, you can selected another of your previously created rate limits to allow for any individual stub to perform with a rate limit other than the default.

## Creating a rate limiter via API

A rate limiter is defined by an object in your mock API's settings document. The
JSON attribute key is then used to apply the rate limiter to specific stub mappings.

A rate limiter has two mandatory parameters:

* `unit` - the time unit the rate is being expressed in e.g. `nanoseconds`, `seconds`, `minutes`
* `rate` - the number of requests per the time unit permitted e.g. `15`

You can also optionally allow bursting by setting:

* `burst` - the number of requests that can be made in a burst over the set rate limit

You set the rate limit by making a `PUT` request to `https://<your mock API>.wiremockapi.cloud/__admin/ext/settings/extended/rateLimits`
containing the JSON object configuring all of your rate limits e.g.

```json theme={null}
{
  "rateLimits": {
    "management": {
      "rate": 15,
      "unit": "seconds",
      "burst": 50
    },
    "authentication": {
      "rate": 100,
      "unit": "seconds"
    }
  }
}
```

If you've got admin API security turned on you'll need to supply your API key e.g.

```bash theme={null}
curl -H 'Authorization:Token <your API token>' \
  https://<your mock API>.wiremockapi.cloud/__admin/ext/settings/extended/rateLimits \
  -X PUT -d '{
 "rateLimits": {
   "management": {
     "rate": 15,
     "unit": "seconds",
     "burst": 50
   },
   "authentication": {
     "rate": 100,
     "unit": "seconds"
   }
  }
}'
```

## Applying to your stubs

To rate limit a particular stub according to one of your named configurations you
need to create or edit the stub via the API, so that you can enable the `rate-limit`
transformer and set the name of the rate limit to be used.

You do this by `POST`ing the JSON to `https://<your mock API>.wiremockapi.cloud/__admin/mappings`.

Taking the above example, if I wanted to use the "authentication" rate limit in my
login handler stub, I'd do as follows:

```json theme={null}
{
  "name": "Login handler",
  "request": {
    "urlPath": "/login",
    "method": "POST"
  },
  "response": {
    "status": 200,
    "body": "{ \"message\": \"Successfully logged in {{jsonPath request.body '$.username'}}\"",
    "transformers": [
      "response-template",
      "rate-limit"
    ],
    "transformerParameters": {
      "rateLimitName": "authentication"
    }
  },
  "persistent": true
}
```

The critical parts here are the `rate-limit` element in the `transformers` array,
and `"rateLimitName": "authentication"` under `transformerParameters`.

Once you've created a stub this way you will start to see 429 responses when the
request rate to **all stubs associated with the named rate limit** exceeds the limit.


# Versioning
Source: https://docs.wiremock.io/versioning/overview

Mock API Versioning Overview

WireMock Cloud supports versioning of your mock APIs.  This means that as you create and configure your mock APIs, a
version history is kept for each API.  This allows you to easily revert to a previous version of your API, or to
compare the differences between two versions.

## Usage

### Accessing your mock API version history

The version history for your mock API is available on the mock API menu bar.  Click on the `Version history` link to
access the version history.

<img alt="Versioning menu item" />

This will take you to the version history page for your mock API where you will be able to see a list of the most recent
commits.

<img alt="Versioning recent changes screen" />

### Commits

A commit is a collection of changes to your mock API and is created when you create, modify or delete assets
associated to your mock API - stubs, settings, GraphQL schemas, gRPC definition files, OpenAPI schemas, etc.

Each commit will have a timestamp of when commit was made to the API. If the commit is made by an authenticated user
(as opposed to the system), the user's username will be displayed alongside the commit.

### Changes

Changes are the individual changes that were made to your mock API. To view the changes associated with a commit, click
on the `View changes` link to the right of the commit.  This will display one or more changes highlighting what was
changed and how. For example, the following example shows a change for a stub creation in the Mock API:

<img alt="Versioning stub created change" />

### Viewing what actually changed

You can click on any of the changes in the list to view the actual changes that were made.  Where possible, this will
show you the diff highlighting what was added or removed.

<img alt="Versioning stub created change diff" />

In the above example, the left side of the diff shows the stub before the change was made (it didn't exist so this is
empty), and the right side shows the stub after the change was made. (All the stub is marked as 'green' because it was
created in this change)

The diff view is available where we have a text representation of the change.  For binary Mock API assets,
(like [gRPC](../grpc/overview) descriptor files) changes to those files are recorded but the diff view is not available.

### Restoring to a previous version

The buttons above the diff shows the restore actions you can take on either side of the diff.

<img alt="Versioning restore actions" />

In the example below, the right side of the diff has no action available because it shows the most recent
version of the stub.  The left side of the diff has an action available to restore the change.  Because this change
shows a stub creation, the 'restore' action is to delete this stub.

<img alt="Versioning stub created change diff" />

Clicking on the `Delete` button will display a confirmation dialog asking if you want to proceed with the deletion.

<img alt="Versioning stub delete confirmation" />

Clicking the `No` button will exit the confirmation dialog without deleting the stub.  Clicking the `Yes` button
will 'restore' the change and delete the stub.

Once you have deleted a stub, the stub will no longer be available in your mock API and a new commit will be created
with the stub deletion.  The diff will show the stub as being deleted:

<img alt="Versioning stub deleted change" />

You will see the button has now changed to `Restore` to allow you to restore the stub.  Clicking on the `Restore`
button will display a confirmation dialog asking if you want to proceed with the restore.

<img alt="Versioning stub restore confirmation" />

As before, clicking the `No` button will exit the dialog without restoring the stub.  Clicking `Yes` will restore the
stub and create a new commit with the stub creation.

The same applies to modifying - a new commit will be created with the change.  The diff will show the change from the
previous version to the new version:

<img alt="Versioning stub modified change - latest version" />

You will notice in the image above that no `Restore` button is available on the right hand side of the diff.  This is
because the right hand side of the diff shows the most recent version of the stub.  The left hand side of the diff has an
`Restore` button available to restore the change.  If the commit you were looking was not the most recent version of the
stub, you will see a `Restore` button on both sides of the diff allowing either side of the diff to be restored:

<img alt="Versioning stub modified change - previous version" />

Versioning is available for mock API stubs, settings, chaos, GraphQL schemas, gRPC definition files and OpenAPI schemas. Updating
any of these assets will create a new commit.  Some commits are created automatically for you.
For example, if you are working on a [REST mock API](../openAPI/openapi) and you have automatic generation of OpenAPI to
stubs enabled. Updating a stub will create a new commit for the change to the OpenAPI and a new commit for the change to
the stub.

### Importing

Importing into your mock API can generate multiple changes in the one commit.  For example, if you imported a file that
created multiple stubs, each of those stub creation changes will be recorded in a single commit.

<img alt="Versioning import changes" />

## Restoring a Mock API to a previous commit

When you click on the `View changes` link  for a commit, you will see the changes between the commit you have selected
and the previous commit.  This is great for when you want to cherry-pick specific changes and restore individual items
in your mock API.

However, if you want to restore the entire mock API to a previous version, you can do so by clicking on the `Compare with latest`
link next to a commit

<img alt="Versioning recent changes screen" />

This will show you all the changes between the current version of the mock API (the latest commit) and the commit you
have selected.  You can then click on the `Restore all changes` button next to the commit you want to restore to.

<img alt="Versioning stub created change" />

As with and restores, this will create a new commit with all the mock api changes from the selected commit. This will
include any changes to the mock API settings, stubs, chaos, GraphQL schemas, gRPC definition files and OpenAPI schemas.

When you click on the `Restore all changes` button, you will be prompted to confirm that you want to restore the entire
mock API to the selected commit.

<img alt="Versioning restore mock api confirmation" />

Clicking `Yes` will restore the entire mock API to the selected commit and clicking `No` will exit the confirmation dialog
without making any changes.

## Limits

You can read more about [plan limits here](./plan-limits/).

If you have feedback or questions on our Versioning functionality as it evolves, we'd love to hear from you.
Please [get in touch](mailto:support@wiremock.io).


# Versioning - Plan Limits
Source: https://docs.wiremock.io/versioning/plan-limits

Limitations of your versioning usage.

WireMock Cloud applies limits to versioning dependent upon the plan your organisation is subscribed to.

On the enterprise or enterprise trial plans, mock API versions will be kept for a period of 18 months.  There is no limit
to the number of changes that can be created in this time.  Accounts on the free plan are limited to 5 changes and
those changes will be kept for a period of 1 year.

If you are on the free plan and would like addition versioning capacity, [contact the WireMock team today](https://www.wiremock.io/contact-now)
to discuss an enterprise plan for your organisation.

## Downgrading to a lower plan

If an account/organisation is downgraded to a plan that causes their version changes to exceed the new plan's
limits, the exceeding changes will be deleted down to the limits of their new plan.


# How to Configure Webhooks and Callbacks
Source: https://docs.wiremock.io/webhooks

Triggering asynchronous outbound HTTP calls

WireMock Cloud offers the ability to make highly configurable asynchronous outbound HTTP calls triggered by inbound
requests.
This pattern is commonly referred to as webhooks or callbacks and is a common design in APIs that need to proactively
notify their clients of events or perform long-running processing asynchronously without blocking.

## Usage

Webhooks are triggered when a configured stub is matched.
Each stub may have any number of webhooks configured on it.
To add a webhook to a stub in WireMock Cloud, navigate to the stub you wish to configure, scroll down to the webhooks
section of the stub form, underneath the response section, and click "Add webhook".

<img alt="Stub form webhook section" />

Once you have added a webhook to your stub, you can configure each attribute of the request that will be sent when the
webhook is triggered, including the request method (e.g. `POST`, `GET`, `PUT`), URL, headers, and body.
A delay can also be set on the webhook, in the same fashion as [response delays](/delays), to stop the webhook's
requests from firing until some time after the triggering request is received.

<img alt="Webhook request form" />

### Templating

The request URL, header values and body attributes of a webhook can all be [templated](/response-templating), allowing
for request attributes to be set dynamically using the content of the triggering request, as well as other contexts like
[dynamic state](/dynamic-state) and [data sources](/data-sources).
All data and helpers that are available to the response body template are also available to the webhook request
attribute templates, **with the caveat that the triggering request is referenced by `originalRequest`, rather than
`request`.**

## Observing webhooks

All webhook request and responses are logged as events under the request that triggered them, and can be viewed in your
mock API's request log page.

<img alt="Webhook request log" />

## Asynchronous timing

Webhooks are fired asynchronously, outside the lifetime of the request that triggered them, so may not have completed by
the time the triggering request has completed.
There is also no guarantee of the order that webhooks will be fired if multiple webhooks are configured on a stub.


