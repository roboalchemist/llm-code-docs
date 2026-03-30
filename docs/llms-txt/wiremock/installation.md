# Source: https://docs.wiremock.io/ai-mcp/installation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Installing WireMock Cloud AI

> How to install the WireMock Cloud MCP server and integrate it with your AI tool

This guide walks you through configuring the MCP (Model Context Protocol) server necessary to natively use WireMock Cloud from an MCP-compatible AI tool such as Cursor or Claude Desktop.

This enables automatic API discovery, mocking and test abstraction from any codebase as part of prompt-driven development with your chosen AI tool.

Additionally, it enables you to skip the complexity of building out new services early on - which can hamper the rapid development by introducing more failure points - and instead use simulated APIs on WireMock to prototype new capabilities with less system overhead.

**Note** that while this article documents use with Cursor, Claude Desktop and VSCode specifically, WireMock Cloud’s MCP server will work with any AI-powered tool that supports MCP.

## Prerequisites

* Node.js 18+ (to install the CLI)
* An existing WireMock Cloud account (if you don’t have one, you can sign up during the login step)

## Step 1: Install the WireMock CLI

Install the CLI globally using npm:

```bash  theme={null}
npm i -g @wiremock/cli
```

## Step 2: Log in to WireMock Cloud

If you already have a WireMock Cloud account, simply log in. Otherwise, the login process will guide you through creating an account:

```bash  theme={null}
wiremock login
```

## Step 3: Configure your AI tool

<Tabs>
  <Tab title="Cursor">
    Click this button to install with Cursor:

    <a href="cursor://anysphere.cursor-deeplink/mcp/install?name=WireMock&config=eyJjb21tYW5kIjoid2lyZW1vY2sgbWNwIn0=">
      <img src="https://cursor.com/deeplink/mcp-install-light.png" alt="Add WireMock MCP server to Cursor" />
    </a>

    Or, follow these instructions:

    * Open Settings->Cursor settings.
    * Navigate to MCP.
    * Click Add new MCP server.
    * In the dialog, configure your server to run this command:

    ```bash  theme={null}
    wiremock mcp
    ```

    <img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/server-config.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=df6d4771527a298267fc9413414cab13" width="360" alt="Configure MCP server" data-og-width="1234" data-og-height="814" data-path="images/ai/server-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/server-config.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=f2695786e9fd5baf93a1e74143a085a4 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/server-config.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=589ffb1baaa89e8c30a94d9a7e48484f 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/server-config.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=e18ab15211475b13f81f1ac0555ea874 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/server-config.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=efb63e28380dcab136dd2f6bf2b0bdcc 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/server-config.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=70bb8d77bff3ed42cf6621f39ef7f264 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/server-config.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=347eaaa7731190f77a68a22699ef036c 2500w" />

    * Verify Installation by looking for the green status dot next to the MCP server and the list of tool names.

    <img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/enabled-server.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=e01a0c1bf07faca6c29affcb5b2827b0" alt="Verify the MCP server is active" data-og-width="1232" width="1232" data-og-height="258" height="258" data-path="images/ai/enabled-server.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/enabled-server.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=b77f7356b1b21d8976efbb19d5db8a34 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/enabled-server.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=f122b351ad1de3bedb06ec7e38753f99 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/enabled-server.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=10edfa97154b95335e4f63ded5489342 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/enabled-server.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=467eb1b70c888898631ea4818bafad8d 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/enabled-server.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=edba0075da48f02c96e47a49cc943a26 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/enabled-server.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=532f8915097aea75c1892687027eec16 2500w" />

    If you have an existing real API integration, you can replace it with a WireMock stub. Generate the mock from documentation, source code, or other external description formats. This enables you to test your app in isolation without depending on live services.

    ### Step 6: Confirm Your Setup

    To confirm everything is working correctly, check that you’re logged in to WireMock Cloud by running the following prompt:

    ```
    Am I logged into WireMock Cloud?
    ```

    If logged in, you’ll see your account details rather than being prompted to sign in.

    <img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/logged-in.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=ff1b697ef56c5ebd4bd829c14ad3c95e" width="550" alt="Confirm you are logged in via the CLI" data-og-width="1238" data-og-height="570" data-path="images/ai/logged-in.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/logged-in.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=3fb65c2628399c7a715ec435d0a5ac96 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/logged-in.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=72b167c86a61a09ea3aead12e8daf580 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/logged-in.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=457c452fa5c157278606bbb972ba94c4 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/logged-in.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=6555f17bcf4d50e31aa470086fd06aad 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/logged-in.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=d3eafd1705f170e179421b1110a7c8f0 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/logged-in.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=f28e9a2d0eb00d2daaa880fa9e684503 2500w" />
  </Tab>

  <Tab title="VSCode + GitHub Copilot">
    * In VSCode, open the `settings.json` file via Settings...->Settings then clicking the Open Settings (JSON) link in the top right.
    * Add the `mcp` element to the settings JSON:
      ```json  theme={null}
      {
        "mcp": {
                "servers": {
                    "WireMock": {
                        "type": "stdio",
                        "command": "wiremock",
                        "args": [
                            "mcp"
                        ]
                    }
                }
            }
      }
      ```
    * Restart VSCode

    ### Step 6: Confirm Your Setup

    Open the Copilot chat window and confirm that the tools icon is present with a number above zero:

    <img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/enabled-tools-icon.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=6f0b8e00143a232a25a3b7b7651630a4" width="50" alt="Copilot tools icon" data-og-width="94" data-og-height="54" data-path="images/ai/enabled-tools-icon.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/enabled-tools-icon.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=d67885533de168932b2c417d6afc81b4 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/enabled-tools-icon.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=a4425b18e6fb3a3a566966b899f20165 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/enabled-tools-icon.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=a2a7bf02971e07d1b18083164766aa31 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/enabled-tools-icon.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=8ee65894b9a13fd832fdfa75c34df219 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/enabled-tools-icon.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=a93d30d29397613e4c2410e063d55f8c 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/enabled-tools-icon.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=941387a7d776e88991073a399879cab0 2500w" />

    To confirm everything is working correctly, check that you’re logged in to WireMock Cloud by running the following prompt:

    ```
    Who am I logged into WireMock Cloud as?
    ```

    If logged in, you’ll see your account details rather than being prompted to sign in.

    <img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/vscode-whoami.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=fe98ecd08cfaefb62de44b1aa6cb6f04" width="550" alt="Confirm you are logged in via the CLI" data-og-width="1024" data-og-height="586" data-path="images/ai/vscode-whoami.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/vscode-whoami.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=e1bdb1c3dd518696f67d40effc03d53c 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/vscode-whoami.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=09662c10c2b8117362b7c3da1261d3a8 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/vscode-whoami.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=93c307b56272e39837df24f73069030a 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/vscode-whoami.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=ff79eb20b417f24b8fd1dcbcc89aa983 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/vscode-whoami.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=8438ccdfeb6253c6574e5ebd0df5725a 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/vscode-whoami.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=f09fba15b8af919d7756f3306ebe8db0 2500w" />
  </Tab>

  <Tab title="Claude Code">
    * Open your terminal or command prompt.
    * Add the WireMock MCP server using the Claude CLI:

    ```bash  theme={null}
    claude mcp add wiremock -- wiremock mcp
    ```

    * Verify the server was added successfully:

    ```bash  theme={null}
    claude mcp list
    ```

    <img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-code-mcp-install.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=0fb766fc40bfa3d99176a98123b81fd2" width="500" alt="Claude Code MCP install" data-og-width="932" data-og-height="410" data-path="images/ai/claude-code-mcp-install.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-code-mcp-install.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=fbc5c23de562331ff6ef7405f2b58b08 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-code-mcp-install.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=dcc9a6d08b9496f8adc52ea1c9a16a77 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-code-mcp-install.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=1312499c999b2bf45fcb7b1ff372b463 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-code-mcp-install.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=8753aa756e2373199d2bdd54f9e8f8c5 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-code-mcp-install.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=c20718eef406ef84dd93a01a37181d52 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-code-mcp-install.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=5bfe93e2a0a5c7042b286e868e0b1e2c 2500w" />

    * You should see "wiremock" in the list of configured MCP servers.

    ### Step 6: Confirm Your Setup

    To confirm everything is working correctly, check that you're logged in to WireMock Cloud by running the following prompt in Claude Code:

    ```
    Am I logged into WireMock Cloud?
    ```

    If logged in, you'll see your account details:

    <img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-code-success.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=8d289f3d8441ae39fd94a8f19f8c7f28" alt="Claude Code MCP success" data-og-width="1562" width="1562" data-og-height="904" height="904" data-path="images/ai/claude-code-success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-code-success.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=c0dc1509722ea35b215928944ca291da 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-code-success.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=04ac22c1197db6b9a1f7bccaa1f27332 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-code-success.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=fd102c1ffc5612a6ab94f032c3e90102 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-code-success.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=69623061890409fd3458dbac665c72bb 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-code-success.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=30495ddb92f30ab10c40762c8a735e32 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-code-success.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=c78cd33a057009939143631d3cb01d69 2500w" />
  </Tab>

  <Tab title="Claude Desktop">
    * Open Settings->Developer.
    * Click Edit Config and open the config file in your preferred editor.
    * Add the WireMock MCP server to the file. The whole file will look like this if this is the first MCP server installed:

    ```json  theme={null}
    {
        "mcpServers": {
        "wiremock": {
        "command": "wiremock",
        "args": [
        "mcp"
        ]
    }
    }
    }
    ```

    * Restart Claude Desktop.

    ### Step 6: Confirm Your Setup

    To confirm everything is working correctly, check that you’re logged in to WireMock Cloud by running the following prompt:

    ```
    Am I logged into WireMock Cloud?
    ```

    After confirming it is OK for Claude to use the tool, if logged in, you’ll see your account details rather than being prompted to sign in.

    <img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-whoami.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=3f560a3bbb9bc08e59f3bacde97a1edb" width="550" alt="Confirm you are logged in via the CLI" data-og-width="754" data-og-height="316" data-path="images/ai/claude-whoami.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-whoami.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=f0da4817a734be3c1c701fa6349736ee 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-whoami.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=4915a299a4dce12219917b658455d2ec 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-whoami.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=f86f0e1aa0ab6d05f24a6532bf87f461 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-whoami.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=053acc451925088a84eec45d62a071ed 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-whoami.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=c65fa1f8b8fa2c0a9c61764814689f5f 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/claude-whoami.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=f38a86974f197a44be6e7ebf0f938ba6 2500w" />
  </Tab>

  <Tab title="Windsurf">
    * Navigate to **Windsurf Settings** > **Cascade** > **Plugins**.
    * Click **Manage plugins** to access the raw configuration.
    * Click **View raw config** to edit the `mcp_config.json` file (located at `~/.codeium/windsurf/mcp_config.json`) and add:

      ```json  theme={null}
      {
        "mcpServers": {
          "wiremock": {
            "command": "wiremock",
            "args": ["mcp"]
          }
        }
      }
      ```

      * Save the configuration and press the refresh button in the Plugin Store.

      <img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/windsurf-manage-plugins.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=fd9589396496c688c448347826048af1" alt="Windsurf Manage Plugins" data-og-width="1590" width="1590" data-og-height="650" height="650" data-path="images/ai/windsurf-manage-plugins.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/windsurf-manage-plugins.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=d3b9b2620d91a83c29c7003fbc817002 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/windsurf-manage-plugins.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=406d2f543fb321141a321391a7580fe7 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/windsurf-manage-plugins.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=6ff1b3da8c05c893031a83d39714ff78 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/windsurf-manage-plugins.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=d5854286e620d20d31e16cedeb5fbbd2 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/windsurf-manage-plugins.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=51d96857c36bd93effb10b1a509c0f32 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/ai/windsurf-manage-plugins.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=abbd8aa667b2b8cb47c9de6ed5bd8842 2500w" />

      ### Step 6: Confirm Your Setup

      To confirm everything is working correctly, check that you're logged in to WireMock Cloud by running the following prompt in Cascade:

      ```
      Am I logged into WireMock Cloud?
      ```

      If logged in, you'll see your account details rather than being prompted to sign in.
  </Tab>
</Tabs>

## Next Steps

With WireMock MCP successfully installed, you can begin creating and using mocks in your development workflow:

### Generate a new feature and mock a new API

Develop a new feature in your application that calls a fresh API. Quickly generate a WireMock stub for this API, and then wire it up to your app while in development mode.

### Swap an existing API connection for a mock

If you have an existing real API integration, you can replace it with a WireMock Cloud mock. Generate the mock from documentation, source code, or other external description formats. This enables you to test your app in isolation without depending on live services.
