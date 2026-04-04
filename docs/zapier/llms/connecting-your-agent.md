# Source: https://docs.zapier.com/powered-by-zapier/embedding-zapier-mcp/guides/connecting-your-agent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connecting Your Agent

> Learn how to connect your agent to Zapier MCP servers.

<Note>
  This is a very basic guide to get you started with connecting your agent to
  Zapier MCP servers. Please check out the official Model Context Protocol (MCP)
  [documentation](https://modelcontextprotocol.io/docs/develop/build-client) for
  more detailed information.
</Note>

# Connection examples

Below are examples of connecting to Zapier MCP from your MCP client using the server URL and secret.

## Installation

<CodeGroup>
  ```javascript TypeScript theme={null}
  npm install @modelcontextprotocol/sdk

  // or

  pnpm add @modelcontextprotocol/sdk
  ```

  ```python Python theme={null}
  pip install mcp

  # or

  uv pip install mcp
  ```
</CodeGroup>

## Usage

<CodeGroup>
  ```javascript TypeScript theme={null}
  import { Client } from "@modelcontextprotocol/sdk/client/index.js";
  import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

  /**
   * Connect to the Zapier MCP server
   *
   * @param serverUrl URL for the MCP server for a specific user
   * @param secret Your Zapier MCP embed secret
   * @returns MCP client
   */
  async function connectToZapierMcp(serverUrl: string, secret: string) {
    const transport = new StreamableHTTPClientTransport(new URL(serverUrl), {
      requestInit: {
        headers: {
          Authorization: `Bearer ${secret}`,
        },
      },
    });

    const client = new Client({
      name: "zapier-mcp",
      version: "1.0.0",
    });

    await client.connect(transport);

    return client;
  }

  async function main() {
    const client = await connectToZapierMcp(serverUrl, secret);

    const tools = await client.listTools();
    console.log("Available tools:", tools);

    await client.transport?.close();
    await client.close();
  }
  ```

  ```python Python theme={null}
  import asyncio

  from mcp import ClientSession
  from mcp.client.streamable_http import streamablehttp_client

  def connect_to_zapier_mcp(server_url: str, secret: str):
      """
      Connect to the Zapier MCP server

      Args:
          server_url: URL for the MCP server for a specific user
          secret: Your Zapier MCP embed secret
      """
      return streamablehttp_client(
          server_url,
          headers={
              "Authorization": f"Bearer {secret}",
          },
      )


  async def main():
      async with connect_to_zapier_mcp(server_url, secret) as (
          read_stream,
          write_stream,
          _,
      ):
          async with ClientSession(read_stream, write_stream) as session:
              await session.initialize()

              tools = await session.list_tools()
              print("Available tools:", tools)
  ```
</CodeGroup>
