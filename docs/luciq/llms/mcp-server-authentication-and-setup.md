# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/ai-features/luciq-mcp-server/mcp-server-authentication-and-setup.md

# MCP Server Authentication & Setup

### Overview

Luciq MCP uses **JSON-RPC 2.0** over HTTPS with **token-based authentication**. Once configured, your IDE can securely list applications, retrieve crash reports, and fetch stack traces all without leaving your development environment.

OAuth-based authentication is currently under development.

### Setup Instructions

Luciq MCP uses **JSON-RPC 2.0** over HTTPS. We provide **token-based authentication** requiring two mandatory headers:

* **Email:** Your registered Luciq account email
* **Token:** Your personal access token

#### How to Get Your Authentication Token

1. **Contact Luciq support team** to obtain your authentication token.
2. **Token is tied to your email address** and provides access to your applications.
3. **Token provides access control** - you can only access applications and data that your account has been granted permissions for.

#### Server Endpoint

```
https://api.instabug.com/api/mcp
```

***Note:** Clustered tenants may have different URLs. Contact Luciq Support for your endpoint.*

#### IDE Configuration

Below are step-by-step setup instructions for supported IDEs, along with example prompts to verify successful connection.

**Cursor**

**Step 1: Configure your MCP server**

1. Open Cursor IDE
2. Go to "Settings" => "Cursor Settings".
3. Select "Tools & Integrations" => "New MCP Server"
4. Create a `.cursor/mcp.json` file in your user directory (`~/.cursor/mcp.json`):

JSON

```json
{  
  "mcpServers": {  
    "luciq": {  
      "url": "https://api.instabug.com/api/mcp",  
      "headers": {  
        "Email": "your-email@company.com",  
        "Token": "your-authentication-token"  
      }  
    }  
  }  
}
```

> **Note:** The server URL will be different for different clusters (single tenants). Contact your Luciq support team to get the correct URL for your specific cluster.

**Step 2: Test Connection**

1. Open Cursor IDE.
2. Use the command palette (`Cmd/Ctrl + Shift + P`)
3. Search for "MCP" settings.
4. Test the connection to verify authentication.
5. Try listing available tools in the MCP server to validate the connection.

> **Note:** You might need to restart Cursor for the connection to work.

**Example Prompt:**

> “List my applications.”\
> “Show me recent crashes for luciqai.”

Cursor will display a structured list of apps or crash entries directly inside the IDE output panel.

***

### Security & Data Privacy

Luciq MCP is designed with **security and data isolation** as first principles.

#### Key Security Measures:

* **Token-Based Access:** Every request requires explicit authentication via your email and unique token.
* **Scoped Permissions:** Tokens are restricted to the apps and environments you’re authorized to access.
* **Encrypted Transport:** All communication occurs over HTTPS (TLS 1.2+).

#### Best Practices for Teams:

* Rotate tokens periodically or after role changes.
* Never share tokens in public repositories or internal code.
* Contact <support@luciq.ai> for enterprise security reviews or audits.

***

### Next Steps

Once you’ve confirmed your IDE connection:

* Explore the available MCP tools in [MCP Tools](https://luciq.gitbook.io/luciq-docs/ios/~/revisions/hhryA5Ra7vzsIzZmMnPr/product-guides/ai-features/luciq-mcp-server/mcp-tools-reference) .
* Try real-time prompts to analyze crash data or list applications.
* Report feedback or feature requests via <support@luciq.ai>
