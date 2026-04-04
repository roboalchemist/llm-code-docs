# Source: https://docs.xano.com/xanoscript/mcp-servers.md

# Source: https://docs.xano.com/building/logic/triggers/mcp-servers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP Server Triggers

<Steps>
  <Step title="Create a Trigger">
    MCP triggers can be created to run any time a client connects to the MCP server. This is useful for dynamic updating of server or tool instructions, as well as restricting tools based on the connecting user.

    Click the <span class="ui-bubble">⋮</span> icon in the top-right corner of your MCP server and select **Triggers**.

    Click <span class="ui-bubble">Add Trigger</span> to create a new MCP server trigger.

    <Tip>MCP servers currently only support one trigger per server.</Tip>
  </Step>

  <Step title="Trigger Information">
    Give your trigger a name, description, and tags to help you identify it later. When you're ready, click <span class="ui-bubble">Save</span>.

        <img src="https://mintcdn.com/xano-997cb9ee/KJsw8QUKy-ElkNLd/images/mcp-servers-20260107-104410.png?fit=max&auto=format&n=KJsw8QUKy-ElkNLd&q=85&s=d8a8aa48b2f147b3174927087088d57c" alt="mcp-servers-20260107-104410" width="687" height="593" data-path="images/mcp-servers-20260107-104410.png" />

    Select your newly created trigger to edit it.

        <img src="https://mintcdn.com/xano-997cb9ee/KJsw8QUKy-ElkNLd/images/mcp-servers-20260107-104447.png?fit=max&auto=format&n=KJsw8QUKy-ElkNLd&q=85&s=3ee3f5f0a8f364ba301c53e99306ad8b" alt="mcp-servers-20260107-104447" width="619" height="302" data-path="images/mcp-servers-20260107-104447.png" />
  </Step>

  <Step title="Trigger Inputs">
    MCP Server triggers offer the following inputs:
    `toolset`\
    Contains the server information, such as the name and instructions.

    ```json  theme={null}
    {
      "id": 1,
      "name": "Server Name",
      "instructions": "Server Instructions"
    }
    ```

    `tools[]`\
    An object array that contains each tool.

    ```json  theme={null}
    [
      {
        "id": 1,
        "name": "Tool Name",
        "instructions": "Tool Instructions"
      },
      {
        "id": 2,
        "name": "Another Tool",
        "instructions": "Another Tool Instructions"
      }
    ]
    ```

    You can modify the tools or toolset by building logic in the trigger to do so.
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).