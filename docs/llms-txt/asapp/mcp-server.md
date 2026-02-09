# Source: https://docs.asapp.com/generativeagent/configuring/connect-apis/mcp-server.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP Servers in API Connections

> Learn how to connect GenerativeAgent to an MCP server

MCP ([Model Context Protocol](https://modelcontextprotocol.io/)) servers provide a standardized way to expose tools and capabilities to LLMs. Unlike traditional APIs that implicitly require a developer to read docs, trial and error, and technical support to successfully use, MCP servers are designed with LLM use from the start, making them easier to integrate with GenerativeAgent.

## Use MCP Server

<Steps>
  <Step title="Create an MCP Server Source">
    1. Navigate to **API Integration Hub** > **API Connections**
    2. Click **Create Connection**
    3. Select **MCP Server** from the connection type list

       <Frame>
           <img src="https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/select-mcp.png?fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=c000de962af322db85d2952d1d383ae9" alt="Select Connection Type" data-og-width="1176" width="1176" data-og-height="545" height="545" data-path="images/generativeagent/connect-apis/mcp/select-mcp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/select-mcp.png?w=280&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=011fb950c208751245fca35cbf56b29a 280w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/select-mcp.png?w=560&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=4913b097af706984656089c92ea70e0d 560w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/select-mcp.png?w=840&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=bd6e7190e7d0b82a490555b234020851 840w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/select-mcp.png?w=1100&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=de5b4f17e751d43deab9a0bb0648e82b 1100w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/select-mcp.png?w=1650&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=c23d06f9aebf9ce4939f975468417ee4 1650w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/select-mcp.png?w=2500&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=b36ca547120076554fd6f9c5d8836604 2500w" />
       </Frame>
    4. Click **Add New** to create a new MCP server source

    <Frame>
            <img src="https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/add-new.png?fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=a175f8a9ff3144e4c98756d698ad0454" alt="Select MCP Server" data-og-width="969" width="969" data-og-height="170" height="170" data-path="images/generativeagent/connect-apis/mcp/add-new.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/add-new.png?w=280&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=9e2f6628df9024a4bbd17d0682dace84 280w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/add-new.png?w=560&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=8a49e49ad0d0a2919a3ed60012f57462 560w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/add-new.png?w=840&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=45168e903d2fa082106bb857cc3022c9 840w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/add-new.png?w=1100&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=36f2b4e6f9570c61207453acefe1f3a3 1100w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/add-new.png?w=1650&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=77d0f58b0f2f88e5bebdeca1951c5d74 1650w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/add-new.png?w=2500&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=72b6c4c285725750f4747d5f8e9ec384 2500w" />
    </Frame>

    <Note>
      You can create, edit, and delete sources from the **Sources** page in the **API Integration Hub**
    </Note>
  </Step>

  <Step title="Configure the MCP server">
    Configure the MCP server:

    * **URL**: Enter the URL of your MCP server
    * **Authentication Method**: Select or create an [authentication method](/generativeagent/configuring/connect-apis/authentication-methods) for the server

    <Frame>
            <img src="https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/specify-server-details.png?fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=e23d9d1c46d21ec6b43aed1dd5f27e03" alt="Configure MCP Server" data-og-width="1057" width="1057" data-og-height="491" height="491" data-path="images/generativeagent/connect-apis/mcp/specify-server-details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/specify-server-details.png?w=280&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=ef9e6cf8e9f0d6a5d31f64100f32751b 280w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/specify-server-details.png?w=560&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=852d57d134436bf13b6ec545b6dc595e 560w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/specify-server-details.png?w=840&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=dddaed8d4d8020a05c4c71b96c92b536 840w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/specify-server-details.png?w=1100&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=899525052a3ab850bf6fdc80e4a6e66f 1100w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/specify-server-details.png?w=1650&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=19f824874c03a70be7f100c9bc7ae8a2 1650w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/specify-server-details.png?w=2500&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=35bdc8d48704a60772d70b8585df1c2c 2500w" />
    </Frame>

    <Note>
      You can reuse MCP server sources across multiple API connections. Once created, they appear in the MCP server dropdown for future connections.
    </Note>
  </Step>

  <Step title="Select a Tool">
    After configuring the MCP server source, select the tool you want to use:

    1. Browse available tools from the MCP server
    2. Select the tool you want to connect
    3. The tool's name and purpose are automatically populated from the MCP server response

    <Frame>
            <img src="https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/select-tool.png?fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=abbddecfc747fa2b9bc3b36444a1976a" alt="Select MCP Tool" data-og-width="1553" width="1553" data-og-height="912" height="912" data-path="images/generativeagent/connect-apis/mcp/select-tool.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/select-tool.png?w=280&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=dd158a837764d096c5d75dd30b7755ba 280w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/select-tool.png?w=560&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=5be7d4a44f65af34bef521d801f6c11f 560w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/select-tool.png?w=840&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=430d75d7a37cd6acb0ffebb281b2e71e 840w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/select-tool.png?w=1100&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=90a4fe0f3745b84cd1e99c287a689d20 1100w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/select-tool.png?w=1650&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=dae9040e2ccfc6ba21d46695cfb01579 1650w, https://mintcdn.com/asapp/RpKmqzZWHqLiup9N/images/generativeagent/connect-apis/mcp/select-tool.png?w=2500&fit=max&auto=format&n=RpKmqzZWHqLiup9N&q=85&s=fcf77223e1b2e2c4c0183daee00c9594 2500w" />
    </Frame>

    <Note>
      MCP servers expose tools that are already designed for LLM use, so the request and response schemas are typically well-structured for GenerativeAgent. You may still configure [request and response transformations](/generativeagent/configuring/connect-apis#request-interface) if needed, but they're often unnecessary.
    </Note>
  </Step>

  <Step title="Link to Functions">
    Once your MCP server connection is configured, [reference it in a Function](/generativeagent/configuring#step-4-create-functions) to enable GenerativeAgent to use the MCP tool.
  </Step>
</Steps>

## Configure Request and Response Interfaces

Since MCP servers are designed for LLM interaction, transformations are often not needed. However, you can still configure:

* [Request Interface](/generativeagent/configuring/connect-apis#request-interface): Modify how GenerativeAgent sends data to the tool
* [Response Interface](/generativeagent/configuring/connect-apis#response-interface): Transform the tool's response format

<Tip>
  Start with the default schemas and transformations. Only customize if you need to adapt the tool's interface for your specific use case.
</Tip>

## MCP Server Schema Changes

MCP servers are unversioned. When you update the schema of your MCP tools, the existing MCP server source in your system continues to use the original schema.

To incorporate schema changes:

1. Create a new MCP server source with the same URL and authentication
2. The new source will fetch and use the updated schema from your MCP server
3. Update your API connections to reference the new MCP server source instead of the old one

## Authentication

MCP server connections in API Connection support the same [authentication methods](/generativeagent/configuring/connect-apis/authentication-methods) as standard API connections. They **do not** currently support MCP's authentication specification.

The [MCP authorization specification](https://modelcontextprotocol.io/docs/tutorials/security/authorization) is designed for uses cases where end users authorize bots to access their personal resources, such as internal productivity tools or chatGPT accessing resources on your behalf, such as your Google Drive.

This flow generally does not work for customer service communication where a user logins to your website or app and presumes any chat experience is already authenticated. The authentication methods of API Connection are designed around that user auth flow.

To use authentication for your MCP Server with API Connections, you need to use one of the [Authenticaiton Methods](/generativeagent/configuring/connect-apis/authentication-methods) we support.

<Warning>
  If your MCP server requires a unique authentication flow, contact your ASAPP account team to discuss your requirements. We'll work with you to build and implement the solution.
</Warning>

## Next Steps

<CardGroup>
  <Card title="Create Functions" href="/generativeagent/configuring#step-4-create-functions">
    Learn how to create functions that use your MCP server connection to enable GenerativeAgent to call MCP tools.
  </Card>

  <Card title="API Connections Overview" href="/generativeagent/configuring/connect-apis">
    Explore other API connection types and learn how to configure request and response transformations.
  </Card>
</CardGroup>
