# Source: https://docs.inkeep.com/guides/mcp-servers/gram

# Create an OpenAPI-based MCP server (/guides/mcp-servers/gram)

Generate an MCP server from an OpenAPI spec using Gram and connect it to your Inkeep agents.



## Overview

Gram by Speakeasy turns any OpenAPI specification into a production-ready MCP server. Upload your API spec, and Gram automatically generates tool definitions, handles hosting and authentication, and deploys your server- so you can focus on building powerful agents.

Visit [Gram's documentation](https://www.speakeasy.com/docs/gram/getting-started/openapi) for a complete guide.

<Tip>
  For custom MCP server logic, use [Gram Functions](https://www.speakeasy.com/docs/gram/getting-started/typescript), Gram's TypeScript framework with managed deployment and hosting.
</Tip>

### Step 1: Sign up for a Gram account

[Sign up](https://app.getgram.ai/login) for a free Gram account.

### Step 2: Upload your OpenAPI document

<Steps>
  <Step>
    Navigate to **Toolsets** in the Gram dashboard sidebar (under **Create**) and click **Get Started**
  </Step>

  <Step>
    Upload your OpenAPI document, provide a descriptive name, and click **Upload**
  </Step>
</Steps>

Gram extracts URL paths, HTTP methods, request schemas, and operation descriptions from your OpenAPI document to generate tool definitions.

<Note>
  Gram works with partial OpenAPI documents as long as key elements (paths, methods, schemas, descriptions) are present.
</Note>

### Step 3: Ship 🚢

Your MCP server is ready to ship! Open the MCP page, and open your MCP server by clicking it. Click Enable to allow the MCP server to handle requests.

### Step 4: Add authentication (optional)

To add authentication, set the appropriate environment variables. See [Step 3 in the Gram documentation](https://www.speakeasy.com/docs/gram/getting-started/openapi#step-3-set-environment-variables) for details.

<>
  ### Next steps

  Once you have your server, you can register it in one of:

  <Cards>
    <Card title="The TypeScript SDK" icon="LuCode" href="/typescript-sdk/tools/mcp-tools#step-2-register-the-mcp-server-as-a-tool-in-your-agent">
      Add your MCP server as a tool for your agents in the TypeScript SDK
    </Card>

    <Card title="The Visual Builder" icon="LuPalette" href="/visual-builder/tools/mcp-servers#register-an-mcp-server">
      Add your MCP server as a tool for your agents in the Visual Builder
    </Card>
  </Cards>
</>
