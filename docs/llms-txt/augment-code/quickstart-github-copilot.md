# Source: https://docs.augmentcode.com/context-services/mcp/quickstart-github-copilot.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart (GitHub Copilot)

> Get started with Augment Context Engine MCP in GitHub Copilot in minutes

## Quick Start with GitHub Copilot

### 1. Install Auggie CLI

```bash  theme={null}
npm install -g @augmentcode/auggie@latest
```

### 2. Sign in to Augment

```bash  theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in GitHub Copilot

* Please create the following file **at the root** of your project: **.vscode/mcp.json**
* Paste this content inside and **Save**

```json  theme={null}
{
  "servers": {
    "augmentcode": {
      "type": "stdio",
      "command": "auggie",
      "args": ["--mcp", "--mcp-auto-workspace"]
    }
  },
  "inputs": []
}
```

### 4. Test the integration

Prompt this in **AGENT MODE**: "What is this project? Please use codebase retrieval tool to get the answer."

Copilot should confirm it has access to the `codebase-retrieval` tool.
<img src="https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/copilot-1.png?fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=fab7a23aa375687de73dc5e7ee9b8e2d" alt="Copilot test" data-og-width="761" width="761" data-og-height="235" height="235" data-path="images/copilot-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/copilot-1.png?w=280&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=376dfb2f44dd8a12f4db3a30ddc993b1 280w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/copilot-1.png?w=560&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=eda8c121965d1efb396cde98402b7e03 560w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/copilot-1.png?w=840&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=3ca6b5080cee12fc90fc25ad6482654a 840w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/copilot-1.png?w=1100&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=2126bdd6203acfa03e4f33622f073a91 1100w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/copilot-1.png?w=1650&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=61f7db485f2dd63381cf0f2710b5f6a4 1650w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/copilot-1.png?w=2500&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=2d1d197731c4c00c878fdd8ab24fa0c4 2500w" />
