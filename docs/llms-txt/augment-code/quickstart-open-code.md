# Source: https://docs.augmentcode.com/context-services/mcp/quickstart-open-code.md

# Quickstart (OpenCode)

> Get started with Augment Context Engine MCP in OpenCode in minutes

## Quick Start with OpenCode

### 1. Install Auggie CLI (Pre-release version)

```bash  theme={null}
npm install -g @augmentcode/auggie@prerelease
```

### 2. Sign in to Augment

```bash  theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in OpenCode

* Go to Folder: \~/.config/opencode/
* Create a file named: opencode.json

Paste this configuration:

```json  theme={null}
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "augment-context-engine": {
      "type": "local",
      "command": ["auggie", "--mcp"],
      "enabled": true
    }
  }
}
```

### 4. Test the integration

```
Prompt : "What is this project ? Please use codebase retrieval tool to get the answer."
```

OpenCode should confirm it has access to the `codebase-retrieval` tool.
<img src="https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/open-code-1.png?fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=81963a81b49d6c14ef9822004c1425f8" alt="OpenCode test" data-og-width="998" width="998" data-og-height="294" height="294" data-path="images/open-code-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/open-code-1.png?w=280&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=f4c3afd3d3b112f5027b13a6e1224eaa 280w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/open-code-1.png?w=560&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=33fd90209708e8af6c026b5ff89fbc00 560w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/open-code-1.png?w=840&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=90c381afc4b2ab500059f56ac5756d81 840w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/open-code-1.png?w=1100&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=366e22d5f2a1caa73343b63393d7d4ad 1100w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/open-code-1.png?w=1650&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=2f246c2d8110f1e7672f4a9821338e38 1650w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/open-code-1.png?w=2500&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=e3cbf2706b7434c8e795ad363a2da24f 2500w" />

## Advanced: Non-Interactive Setup

For non-interactive environments like CI/CD pipelines, GitHub Actions, or automated scripts where you cannot run `auggie login` interactively, you can configure authentication using environment variables.

### 1. Get your authentication token

```bash  theme={null}
auggie token print
```

This will output something like:

```
TOKEN={"accessToken":"your-access-token","tenantURL":"your-tenant-url","scopes":["read","write"]}
```

Copy the `accessToken` value (the long string after `"accessToken":"`) and the `tenantURL` value.

### 2. Configure with environment variables

Add the `env` section to your configuration:

```json  theme={null}
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "augment-context-engine": {
      "type": "local",
      "command": ["auggie", "--mcp"],
      "enabled": true,
      "env": {
        "AUGMENT_API_TOKEN": "your-access-token",
        "AUGMENT_API_URL": "your-tenant-url"
      }
    }
  }
}
```

Replace `your-access-token` and `your-tenant-url` with the values from step 1.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.augmentcode.com/llms.txt