# Source: https://docs.augmentcode.com/context-services/mcp/quickstart-zed.md

# Quickstart (Zed)

> Get started with Augment Context Engine MCP in Zed in minutes

## Quick Start with Zed

### 1. Install Auggie CLI (Pre-release version)

```bash  theme={null}
npm install -g @augmentcode/auggie@prerelease
```

### 2. Sign in to Augment

```bash  theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Get your authentication token (Only if you set it up remotely, this is not mandatory locally.)

```bash  theme={null}
auggie token print
```

This will output something like:

```
TOKEN={"accessToken":"your-access-token","tenantURL":"your-tenant-url","scopes":["read","write"]}
```

Copy the `accessToken` value (the long string after `"accessToken":"`) and the `tenantURL` value for the next step.

### 4. Configure the MCP server in Zed

* Click the ... then **Add Custom Server**
  <img src="https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-1.png?fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=4f89d1d4023e5b63227eed394765069e" alt="Zed custom server" data-og-width="363" width="363" data-og-height="245" height="245" data-path="images/zed-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-1.png?w=280&fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=9d8e994b35e01cae82e8b2b64cb226d0 280w, https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-1.png?w=560&fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=b9d75f51f138b3a73bfb33ed0419b935 560w, https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-1.png?w=840&fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=db054992d6ef890ab339028b00e84783 840w, https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-1.png?w=1100&fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=c9d25b63ab249c3b1bf69095fb8153fe 1100w, https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-1.png?w=1650&fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=7c46a48837d9f4a99eabc0b474306660 1650w, https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-1.png?w=2500&fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=e16d766b76ecc38f5e5094d9cecbf942 2500w" />
* Paste the config and **Update the /path/to/your/project** this is mandatory in Zed for such MCP (easy copy paste is below the screenshot)
  <img src="https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-2.png?fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=1a602d03518a7382c58c4694b680ecfc" alt="Zed MCP" data-og-width="562" width="562" data-og-height="516" height="516" data-path="images/zed-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-2.png?w=280&fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=7e216eb394b4940e3e8c66b5ab1644ee 280w, https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-2.png?w=560&fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=ec0145778728dab305b7e190420203be 560w, https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-2.png?w=840&fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=b0ae228b6df1a3c435cd036547f69c0c 840w, https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-2.png?w=1100&fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=04796b3ef70c043eb6dcc052abed3412 1100w, https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-2.png?w=1650&fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=6aa97a3eb3cce4b9109c73ed340e6ddb 1650w, https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-2.png?w=2500&fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=1771c410e68f6919cd1c85b37cedd8f4 2500w" />

**Local Setup (MacOS or Linux)**\
On MacOS or Linux, use this config:

```
{
  "Augment-Context-Engine": {
    "enabled": true,
    "command": "bash",
    "args": [
      "-c",
      "auggie -m default --mcp -w $(pwd)"
    ],
    "env": {}
  }
}
```

On Windows, use the config below. Update the **/path/to/your/project**.

**Local Setup (Windows)**

```
{
  "Augment-Context-Engine": {
    "command": "auggie",
    "args": [
      "--mcp",
      "-m",
      "default",
      "-w",
      "/path/to/your/project"
    ],
    "env": {}
  }
}
```

### 5. Test the integration

Prompt : "What is this project ? Please use codebase retrieval tool to get the answer."\
Zed should confirm it has access to the `codebase-retrieval` tool.
<img src="https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-3.png?fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=5663fb0c0cc565f0b890f96e4f846eb8" alt="Zed test" data-og-width="813" width="813" data-og-height="161" height="161" data-path="images/zed-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-3.png?w=280&fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=16d46bb82b170feedf218d5a176fb29c 280w, https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-3.png?w=560&fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=800acc9486c9a0c106889250ce26f704 560w, https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-3.png?w=840&fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=2ec9e40b225b94635c948c07b0f4e458 840w, https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-3.png?w=1100&fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=c400e0ee8adad4c1900f19bb9b8c0add 1100w, https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-3.png?w=1650&fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=263b22ce78cc6bc7bc6b1ac67d17d5c5 1650w, https://mintcdn.com/augment-mtje7p526w/UAXlZ5LOydH6Jt19/images/zed-3.png?w=2500&fit=max&auto=format&n=UAXlZ5LOydH6Jt19&q=85&s=1426f8a7fb8ebdcf7f57ea96b0a6ed8f 2500w" />


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.augmentcode.com/llms.txt