# Source: https://docs.augmentcode.com/context-services/mcp/quickstart-anti-gravity.md

# Quickstart (AntiGravity)

> Get started with Augment Context Engine MCP in AntiGravity in minutes

## Quick Start with AntiGravity

### 1. Install Auggie CLI (Pre-release version)

```bash  theme={null}
npm install -g @augmentcode/auggie@prerelease
```

### 2. Sign in to Augment

```bash  theme={null}
auggie login
```

This will open a browser window for authentication.

### 3. Configure the MCP server in AntiGravity

* Click the MCP server icon
  <img src="https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-1.png?fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=0435ca2c51f4e1ba08dfb960e831d1b5" alt="MCP server icon" data-og-width="195" width="195" data-og-height="143" height="143" data-path="images/anti-gravity-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-1.png?w=280&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=e731d92de6eebfd9296d9b82effcdcb4 280w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-1.png?w=560&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=75dc03f70d8b3d0482619fc53c23022d 560w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-1.png?w=840&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=52e7d2b02f2683612fddbcc69e31013a 840w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-1.png?w=1100&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=15e9b13e2979e007ed235d0bcb5f7fd7 1100w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-1.png?w=1650&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=5114b30ce205bcf94349967d20856be4 1650w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-1.png?w=2500&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=89548a01f7e6a41c3c4c9788a3da00b4 2500w" />
* Click manage MCP server
  <img src="https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-2.png?fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=0ac8123bfce7dcbbc06cad295e83d5cd" alt="Manage MCP server" data-og-width="146" width="146" data-og-height="38" height="38" data-path="images/anti-gravity-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-2.png?w=280&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=bb1eac1b76c67f771c1c921b78ee06cd 280w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-2.png?w=560&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=8fc2cf758e8db4865d92a15b3073b735 560w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-2.png?w=840&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=7fc99fb6dd61afe0323522a071b62fb3 840w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-2.png?w=1100&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=a91b94c1fd06f9a40486bfa93db70e7c 1100w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-2.png?w=1650&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=906cf66a456a9dfb6ef4819e74f5ee31 1650w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-2.png?w=2500&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=ffb8e11df5b54bcb7adf6a606f4bc55c 2500w" />
* Click View raw config
  <img src="https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-3.png?fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=aba540233efbcb11816383c6c1cf2fe0" alt="View raw config" data-og-width="149" width="149" data-og-height="58" height="58" data-path="images/anti-gravity-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-3.png?w=280&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=4a241ea7b929fb79e70f40a841d60e15 280w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-3.png?w=560&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=185a5843d250e13e48b020e73bc9cb24 560w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-3.png?w=840&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=ff04fd53e99ecd54ecbe034b596a845b 840w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-3.png?w=1100&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=190ddc51a816d7a203697803dd11c7da 1100w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-3.png?w=1650&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=fa41a641184396ba37fc6b49fa558ede 1650w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-3.png?w=2500&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=bf0d291eb6a5f54f4d5d330613b16142 2500w" />

Paste this configuration. Update the **/path/to/your/project**.

```
{
  "mcpServers": {
    "augment-context-engine": {
      "command": "auggie",
      "args": [
        "--mcp",
        "-m",
        "default",
        "-w",
        "/path/to/your/project"
      ]
    }
  }
}
```

### 4. Test the integration

```
Prompt : "What is this project ? Please use codebase retrieval tool to get the answer."
```

AntiGravity should confirm it has access to the `codebase-retrieval` tool.
<img src="https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-4.png?fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=a047aed452e06af1c7d41e2c2461e731" alt="AntiGravity test" data-og-width="477" width="477" data-og-height="83" height="83" data-path="images/anti-gravity-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-4.png?w=280&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=95f51899bca5fbcf18eb44ef02a950f5 280w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-4.png?w=560&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=eb1cfdf6d7ce279dada9c084b399f409 560w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-4.png?w=840&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=2f4a62a806afc44e2faffe5ef3ba18aa 840w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-4.png?w=1100&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=b0127e4d82023981a71e3ff2413ac0b9 1100w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-4.png?w=1650&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=6a036d07f32b60722a8dd571def93756 1650w, https://mintcdn.com/augment-mtje7p526w/bPUsQPriBJwiNgJV/images/anti-gravity-4.png?w=2500&fit=max&auto=format&n=bPUsQPriBJwiNgJV&q=85&s=8bf4a626905bef9b009913a26c5c4352 2500w" />


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.augmentcode.com/llms.txt