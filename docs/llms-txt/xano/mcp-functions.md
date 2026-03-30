# Source: https://docs.xano.com/ai-tools/mcp-builder/mcp-functions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP Functions

## Run API Endpoint

Executes an API endpoint as part of an MCP Server Tool function stack

| Parameter | Purpose                                               |
| --------- | ----------------------------------------------------- |
| API Group | The API group that contains the API you'd like to run |
| Endpoint  | The API endpoint to run                               |
| Return as | The variable to store the output of the API call      |

## Note

When using the Run API Endpoint function, authentication tokens are not checked.

## Run Task

Executes a task as part of an MCP Server Tool function stack

| Parameter | Purpose         |
| --------- | --------------- |
| Task      | The task to run |

<Info>
  Tasks have no output.
</Info>

## MCP List Tools

Provides a list of available tools and their configurations from an MCP server

| Parameter    | Purpose                                                   |
| ------------ | --------------------------------------------------------- |
| url          | The URL to access the MCP server                          |
| bearer token | If required, an authentication token to access the server |

## MCP Call Tool

Executes a tool available on a remote MCP server

| Parameter    | Purpose                                                                        |
| ------------ | ------------------------------------------------------------------------------ |
| url          | The URL to access the MCP server                                               |
| bearer token | If required, an authentication token to access the server                      |
| tool name    | The name of the tool to call                                                   |
| args         | The data that the tool requires, if any. This should usually be a JSON object. |


Built with [Mintlify](https://mintlify.com).