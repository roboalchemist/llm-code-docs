# Source: https://docs.augmentcode.com/codereview/mcp-context.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding Context with MCP

> Connect Augment Code Review to external context sources through Model Context Protocol.

## Configuring Model Context Protocol (MCP) Servers

Administrators can connect Augment Code Review to external context sources through Model Context Protocol (MCP). MCP servers provide additional context to the code review agent, such as access to documentation, APIs, databases, or other external systems that can help improve review quality.

To configure MCP servers, visit [MCP for Code Review](https://app.augmentcode.com/settings/code-review/mcp).

### Types of MCP Servers

Augment Code Review supports both remote and local MCP servers:

* **Remote MCP servers** run remotely and are hosted by providers. Once you add a remote MCP server, you may need to complete an OAuth flow to authenticate before it can be used by the code review agent.
* **Local MCP servers** run in their own environment within the code review agent's workspace. You can specify environment variables for local servers when adding them. Environment variables are write-only and can only be overwritten or removed (not viewed) after the server has been added.

### Adding MCP Servers

There are three ways to add MCP servers to Code Review:

#### 1. Add Local MCP Server (+ MCP)

To add a local MCP server:

1. Navigate to [MCP for Code Review](https://app.augmentcode.com/settings/code-review/mcp)
2. Click **+ MCP** to add a local server
3. Enter the following information:
   * **Name**: A descriptive name for your MCP server
   * **Command**: The executable command to run the server
   * **Arguments**: Command-line arguments (optional)
4. Add environment variables if needed:
   * Click **+ Environment Variable**
   * Enter the variable name and value
   * Repeat for additional variables
5. Click **Add Server** to save
6. Add a review guideline telling Augment Code Review when to use the MCP server (see [Review Guidelines](/codereview/review-guidelines) for more information)

<Note>
  Environment variables for local MCP servers are stored securely and cannot be viewed after saving. You can only overwrite or remove them.
</Note>

#### 2. Add Remote MCP Server (+ Remote MCP)

To add a remote MCP server:

1. Navigate to [MCP for Code Review](https://app.augmentcode.com/settings/code-review/mcp)
2. Click **+ Remote MCP** to add a remote server
3. Enter the following information:
   * **Name**: A descriptive name for your MCP server
   * **URL**: The full URL of the remote MCP server (e.g., `https://mcp.example.com`)
4. Click **Add Server**
5. If the server requires OAuth authentication, you'll be redirected to complete the authentication flow
6. After successful authentication, you'll be redirected back to the settings page
7. Add a review guideline telling Augment Code Review when to use the MCP server (see [Review Guidelines](/codereview/review-guidelines) for more information)

Remote MCP servers that require authentication will show a status indicator:

* **Connected** (green): Server is authenticated and ready to use
* **Authenticate** (yellow): Server needs authentication or re-authentication

#### 3. Import from JSON

To import MCP server configurations from a JSON file:

1. Navigate to [MCP for Code Review](https://app.augmentcode.com/settings/code-review/mcp)
2. Click **Import from JSON**
3. Paste your JSON configuration in the format:
   ```json  theme={null}
   {
     "mcpServers": {
       "server-name": {
         "command": "npx",
         "args": ["-y", "@example/mcp-server"],
         "env": {
           "API_KEY": "your-api-key"
         }
       }
     }
   }
   ```
4. Click **Import** to add the servers
5. Add a review guideline telling Augment Code Review when to use the MCP server (see [Review Guidelines](/codereview/review-guidelines) for more information)

<Note>
  The JSON format matches the structure used in Augment's settings.json file, making it easy to share configurations across your team.
</Note>

### Managing MCP Servers

Once added, MCP servers appear in the "Configured MCP Servers" list. For each server, you can:

* **View status**: See if the server is connected or needs authentication
* **Re-authenticate**: Click the **Authenticate** button for remote servers that need re-authentication
* **Remove**: Click the trash icon to remove a server from Code Review

All configured MCP servers are available to the code review agent when analyzing pull requests.

### Example: Review Guideline for MCP Servers

After adding an MCP server, you should create a review guideline that tells Augment Code Review when and how to use it. Add guidelines to your `code_review_guidelines.yaml` file at `<repo-root>/.augment/code_review_guidelines.yaml`.

Here's an example guideline for using the Linear MCP server:

```yaml  theme={null}
areas:
  linear_ticket_verification:
    description: "Verify PRs implement their linked Linear tickets correctly"
    globs:
      - "**"
    rules:
      - id: "verify_linear_ticket_implementation"
        description: "If a Linear ticket is linked in the PR description, use the Linear MCP server to retrieve the ticket description and verify that the PR correctly implements the requirements specified in the ticket."
        severity: "high"
```

This guideline instructs the code review agent to:

1. Check if a Linear ticket is referenced in the PR description
2. Use the Linear MCP server to fetch the ticket details
3. Verify that the code changes align with the ticket requirements

For more information on writing review guidelines, see [Review Guidelines](/codereview/review-guidelines).
