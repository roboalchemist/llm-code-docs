# Source: https://directus.io/docs/raw/guides/ai/mcp/local-mcp.md

# Installation

> The Directus Content MCP Server allows you to interact with your Directus data through AI tools using the Model Context Protocol.

The local MCP server is a standalone Node.js application that provides an alternative way to connect AI tools to your Directus instance using the Model Context Protocol.

<callout color="warning" icon="material-symbols:info">

**Remote vs Local MCP**: Directus v11.12+ now includes a [built-in remote MCP server](/guides/ai/mcp/) that's easier to set up and doesn't require Node.js. We highly recommend using the newer remote MCP server. The local MCP server remains available as an alternative for users who prefer a local setup or need specific Node.js-based functionality.

</callout>

## When to Use Local MCP

Consider using the local MCP server if you:

- Need to run MCP in local environments without internet access to your Directus instance
- Prefer Node.js-based tooling and local development workflows
- Want to customize or extend the MCP server functionality
- Are working with older Directus versions that don't support the remote MCP
- Need to run MCP operations through a proxy or custom network setup

## Comparison with Remote MCP

<table>
<thead>
  <tr>
    <th>
      Feature
    </th>
    
    <th>
      Remote MCP
    </th>
    
    <th>
      Local MCP
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <strong>
        Setup Complexity
      </strong>
    </td>
    
    <td>
      Simple (built into Directus)
    </td>
    
    <td>
      Requires Node.js installation
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Node.js Requirement
      </strong>
    </td>
    
    <td>
      None
    </td>
    
    <td>
      Node.js v22.12+
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Configuration
      </strong>
    </td>
    
    <td>
      UI-based settings
    </td>
    
    <td>
      Environment variables
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Updates
      </strong>
    </td>
    
    <td>
      Automatic with Directus
    </td>
    
    <td>
      Manual npm updates
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Customization
      </strong>
    </td>
    
    <td>
      Limited to settings
    </td>
    
    <td>
      Full source code access
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Network Requirements
      </strong>
    </td>
    
    <td>
      Direct Directus access
    </td>
    
    <td>
      Can work through proxies
    </td>
  </tr>
</tbody>
</table>

This guide will cover how to set up and use the local MCP server as an alternative to the built-in remote option.

<callout color="info" icon="material-symbols:code" to="https://github.com/directus/mcp">

View the local Directus Content MCP Server repository on GitHub.

</callout>

## Prerequisites

Before starting, ensure you have:

- Node.js v22.12 or newer installed on your computer
- An existing Directus project with access credentials
- One of the supported MCP clients: Claude Desktop, Cursor, or Raycast

If you don't have an existing Directus project, you can:

- Start a free trial on [Directus Cloud](https://directus.cloud/register)
- Create a local instance with `npx directus-template-cli@latest init`

## Get Directus Credentials

You'll need either a static token or your email and password to connect to your Directus instance:

To get a static access token:

1. Log in to your Directus instance.
2. Navigate to the User Directory and select your user profile.
3. Scroll down to the Token field.
4. Generate a token and copy it.
5. Save the user (do not forget this step).

## Installation

Choose your AI tool and follow the setup:

<accordion type="single">
<accordion-item icon="i-simple-icons-anthropic" label="Claude Desktop">
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; margin: 1rem 0;">
<iframe src="https://www.youtube.com/embed/mJiLiUGh9r8" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-radius: 12px;" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen="true">



</iframe>
</div>

1. Download [Claude Desktop](https://claude.ai/download)
2. Open **Settings → Developer → Edit Config**
3. Add this configuration:

```json
{
  "mcpServers": {
    "directus": {
      "command": "npx",
      "args": ["@directus/content-mcp@latest"],
      "env": {
        "DIRECTUS_URL": "https://your-directus-url.com",
        "DIRECTUS_TOKEN": "your-directus-token"
      }
    }
  }
}
```

1. Replace `your-directus-url.com` with your Directus URL
2. Replace `your-directus-token` with your user token
3. Restart Claude Desktop

</accordion-item>

<accordion-item icon="vscode-icons:file-type-cursorrules" label="Cursor">
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; margin: 1rem 0;">
<iframe src="https://www.youtube.com/embed/KmO09zRphnc" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-radius: 12px;" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen="true">



</iframe>
</div>

1. Download [Cursor](https://cursor.sh/)
2. Create `.cursor/mcp.json` in your project root:

```json
{
  "mcpServers": {
    "directus": {
      "command": "npx",
      "args": ["@directus/content-mcp@latest"],
      "env": {
        "DIRECTUS_URL": "https://your-directus-url.com",
        "DIRECTUS_TOKEN": "your-directus-token"
      }
    }
  }
}
```

1. Replace URLs and tokens
2. Verify connection in **Settings → MCP**

</accordion-item>

<accordion-item icon="i-simple-icons-raycast" label="Raycast">
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; margin: 1rem 0;">
<iframe src="https://www.youtube.com/embed/zeg7AWddcQs" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-radius: 12px;" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen="true">



</iframe>
</div>

1. Download [Raycast](https://raycast.com/)
2. Search "MCP Servers" → "Install Server"
3. Paste configuration:

```json
{
  "mcpServers": {
    "directus": {
      "command": "npx",
      "args": ["@directus/content-mcp@latest"],
      "env": {
        "DIRECTUS_URL": "https://your-directus-url.com",
        "DIRECTUS_TOKEN": "your-directus-token"
      }
    }
  }
}
```

1. Press **⌘ + Enter** to install
2. Use `@directus` to interact with your instance

**Tip**: Add custom instruction: "Make sure you always call the system prompt tool first."

</accordion-item>
</accordion>

### Using Email/Password Authentication

If you prefer using email and password instead of a token, use this configuration format for any of the platforms:

```json
{
    "mcpServers": {
        "directus": {
            "command": "npx",
            "args": ["@directus/content-mcp@latest"],
            "env": {
                "DIRECTUS_URL": "https://your-directus-url.com",
                "DIRECTUS_USER_EMAIL": "user@example.com",
                "DIRECTUS_USER_PASSWORD": "your_password"
            }
        }
    }
}
```

## Advanced Configuration

### System Prompt

The MCP server includes a default system prompt that helps guide the LLM's behavior. You can:

- Override it by setting the `MCP_SYSTEM_PROMPT` variable.
- Disable it by setting `MCP_SYSTEM_PROMPT_ENABLED` to `false`.

### Example: Advanced Configuration

```json
{
    "mcpServers": {
        "directus": {
            "command": "npx",
            "args": ["@directus/content-mcp@latest"],
            "env": {
                "DIRECTUS_URL": "https://your-directus-instance.com",
                "DIRECTUS_TOKEN": "your_directus_token",
                "DISABLE_TOOLS": ["delete-item", "update-field"],
                "MCP_SYSTEM_PROMPT_ENABLED": "true",
                "MCP_SYSTEM_PROMPT": "You are an assistant specialized in managing content for our marketing website.",
                "DIRECTUS_PROMPTS_COLLECTION_ENABLED": "true",
                "DIRECTUS_PROMPTS_COLLECTION": "ai_prompts",
                "DIRECTUS_PROMPTS_NAME_FIELD": "name",
                "DIRECTUS_PROMPTS_DESCRIPTION_FIELD": "description",
                "DIRECTUS_PROMPTS_SYSTEM_PROMPT_FIELD": "system_prompt",
                "DIRECTUS_PROMPTS_MESSAGES_FIELD": "messages"
            }
        }
    }
}
```
