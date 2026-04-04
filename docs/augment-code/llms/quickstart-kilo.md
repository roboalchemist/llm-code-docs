# Source: https://docs.augmentcode.com/context-services/mcp/quickstart-kilo.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart (Kilo)

> Get started with Augment Context Engine MCP in Kilo in minutes

## Quick Start with Kilo

### 1. Install Auggie CLI

```bash  theme={null}
npm install -g @augmentcode/auggie@latest
```

### 2. Sign in to Augment

```bash  theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in Kilo

* Click the MCP server icon
  <img src="https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-1.png?fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=db01b02e473bc0d81b0bbc0335d36540" alt="Click the MCP server icon" data-og-width="331" width="331" data-og-height="68" height="68" data-path="images/kilo-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-1.png?w=280&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=a5721959f3593f535eb72cd459cc00df 280w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-1.png?w=560&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=1669375a3e9019d91a9e5d0f334bb624 560w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-1.png?w=840&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=42f15ae3fd22ac1db0d2eb06a81e8f72 840w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-1.png?w=1100&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=335620c9e9dc22eb4da7e0dc0f80db2d 1100w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-1.png?w=1650&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=d154f74789ee07266522db3c9aeb3ab2 1650w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-1.png?w=2500&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=51f67b469aeeeb65d9894572289a66a0 2500w" />

* Click Edit Global MCP
  <img src="https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-2.png?fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=c7c319402a8842930e170de74aa27154" alt="Click Edit Global MCP" data-og-width="264" width="264" data-og-height="64" height="64" data-path="images/kilo-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-2.png?w=280&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=2f3f193380480e1c3528919c6c0ef094 280w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-2.png?w=560&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=c2a1916cce4ae369e82a92ec13d82777 560w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-2.png?w=840&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=2bebaf2f24a6d869d8e2b29d8fb573fc 840w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-2.png?w=1100&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=c1ac93df2e836a93db22d377f64fc881 1100w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-2.png?w=1650&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=baac6e102138b231fbc187b6dfc002e3 1650w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-2.png?w=2500&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=fd0d55715e4586ba29ee40cdfaf491a7 2500w" />

Paste this configuration:

```json  theme={null}
{
  "mcpServers": {
    "augment-context-engine": {
      "command": "auggie",
      "type": "stdio",
      "args": ["--mcp", "--mcp-auto-workspace"],
      "disabled": false,
      "alwaysAllow": ["codebase-retrieval"]
    }
  }
}
```

### 4. Test the integration

Prompt: "What is this project? Please use codebase retrieval tool to get the answer."

Kilo should confirm it has access to the `codebase-retrieval` tool.
<img src="https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-3.png?fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=643074aad72151ee9dffcb93459abb2c" alt="Kilo test" data-og-width="722" width="722" data-og-height="353" height="353" data-path="images/kilo-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-3.png?w=280&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=014bc1ed3f7acd980d6680e4afcd2bdb 280w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-3.png?w=560&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=a613929cf00eaa3aa0b653cc70291d6f 560w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-3.png?w=840&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=e1d8aead98c97fca4ec7f1052627794e 840w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-3.png?w=1100&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=1cf25dbca0ba9b86263d9c687e4313e1 1100w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-3.png?w=1650&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=762f4f2dbec4e2eaaecd9b45c924aa18 1650w, https://mintcdn.com/augment-mtje7p526w/rIravLuzI7-HsY1h/images/kilo-3.png?w=2500&fit=max&auto=format&n=rIravLuzI7-HsY1h&q=85&s=df1331ebf761134639118abe3736bd25 2500w" />
