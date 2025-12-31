# Source: https://docs.augmentcode.com/context-services/mcp/quickstart-cursor.md

# Quickstart (Cursor)

> Get started with Augment Context Engine MCP in Cursor in minutes

## Quick Start with Cursor

### 1. Install Auggie CLI (Pre-release version)

```bash  theme={null}
npm install -g @augmentcode/auggie@prerelease
```

### 2. Sign in to Augment

```bash  theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in Cursor

* Go in settings (top right)
  <img src="https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-1.png?fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=d1195573e43bb2307721f576674e5aae" alt="Cursor settings" data-og-width="136" width="136" data-og-height="37" height="37" data-path="images/cursor-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-1.png?w=280&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=030bf61c0df41a549ea26df3c8313264 280w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-1.png?w=560&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=aec3b625751690ed1d1967ab301b0f84 560w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-1.png?w=840&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=83516ca861e95aff1c6e1d3049f4c228 840w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-1.png?w=1100&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=0702a025bd84cc7f8b88a85c3059733b 1100w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-1.png?w=1650&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=d9c757f860ca6acdb44c015d0183ed5f 1650w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-1.png?w=2500&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=04bdd994a2e8c955fa90b542f689493b 2500w" />
* Click on Tools & MCP on the left menu then **New MCP Server**
  <img src="https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-2.png?fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=8db7b7e8d319f1cb1de18744f602a8bb" alt="Cursor MCP" data-og-width="942" width="942" data-og-height="418" height="418" data-path="images/cursor-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-2.png?w=280&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=698263a15b6f8f86a77878de95cf986c 280w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-2.png?w=560&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=4157e84545142dd3cb5618fea1b03916 560w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-2.png?w=840&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=f0f784f5df8db54e16e5b5b00880a756 840w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-2.png?w=1100&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=cf31313d0aee59b23ebccc3f29ff0a58 1100w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-2.png?w=1650&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=8f1180ae362efec69f7fa1801fdba372 1650w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-2.png?w=2500&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=ae54862781ed59aa648f12844b6088a1 2500w" />

**MacOS or Linux**

On MacOS or Linux, use this config:

```json  theme={null}
{
  "mcpServers": {
    "augment-context-engine": {
      "type": "local",
      "command": "bash",
      "args": [
        "-c",
        "auggie --mcp -m default -w \"${WORKSPACE_FOLDER_PATHS%%,*}\""
      ],
      "enabled": true
    }
  }
}
```

**Windows**

On Windows, use this config:

```json  theme={null}
{
  "mcpServers": {
    "augment-context-engine": {
      "type": "local",
      "command": "powershell",
      "args": [
        "-Command",
        "auggie --mcp -m default -w \"($env:WORKSPACE_FOLDER_PATHS -split ',')[0]\""
      ],
      "enabled": true
    }
  }
}
```

### 4. Test the integration

```
Prompt : "What is this project ? Please use codebase retrieval tool to get the answer."
```

Cursor should confirm it has access to the `codebase-retrieval` tool.
<img src="https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-3.png?fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=a33dfe584f3b9439ea2ba8e4ad485717" alt="Cursor test" data-og-width="418" width="418" data-og-height="149" height="149" data-path="images/cursor-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-3.png?w=280&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=514ef5df574a1af288e7549850bad320 280w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-3.png?w=560&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=ba4487e15fdc445099e5dc8749796431 560w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-3.png?w=840&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=742cc06afe8969489c665c7296f3106a 840w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-3.png?w=1100&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=099045bc704cd769b0145e44843c67cf 1100w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-3.png?w=1650&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=b540399d6842ddd88ec24786d88a8b55 1650w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/cursor-3.png?w=2500&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=bd758770ef9c2ffd8f71456ecc1d3397 2500w" />


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.augmentcode.com/llms.txt