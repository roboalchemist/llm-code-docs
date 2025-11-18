# Source: https://docs.anchorbrowser.io/advanced/mcp.md

# MCP - Hosted Version

> Use Anchor with Model Context Protocol (MCP) in your preferred agentic tools via our hosted service

<img src="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp_logo.png?fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=ec164cf1532c41350abe6f1dd8c52e73" alt="Model Context Protocol" style={{width: "200px", margin: "20px 0"}} data-og-width="485" width="485" data-og-height="514" height="514" data-path="images/mcp_logo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp_logo.png?w=280&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=a7afe80fed92f76a00fce74df69f33de 280w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp_logo.png?w=560&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=a7a9af2ab0e76f6de65611ff785bd01a 560w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp_logo.png?w=840&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=f954470c4999efd6b83502c4b5463626 840w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp_logo.png?w=1100&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=f288405c55b1fcb1c6d51ce232b468c2 1100w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp_logo.png?w=1650&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=54292ecf2eab83c5e92a2c9a65028bfb 1650w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp_logo.png?w=2500&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=e9432402a01b3bcf1a46bbfffcc5d4f9 2500w" />

## Overview

Anchor provides a **hosted** Model Context Protocol (MCP) integration, allowing you to use browser automation directly from your preferred AI tools without any local setup. Our hosted MCP server runs on our infrastructure and is available to all users with an Anchor API key.

This enables seamless browser control from Cursor, VS Code, Claude, ChatGPT, and other MCP-compatible tools without managing any local dependencies.

## What is MCP?

Model Context Protocol (MCP) is an open standard that allows AI assistants to interact with external tools and data sources.

In our case, it enables AI-powered tools to access and control our browser automation capabilities directly within your IDE, agent apps, or CI/CD pipelines.

## Hosted vs Self-Hosted

Our **hosted MCP service** provides:

* ✅ Zero setup - just add your API key
* ✅ Always up-to-date with latest features
* ✅ Managed infrastructure and updates
* ✅ Built-in scaling and reliability
* ✅ Direct integration with Anchor's cloud browsers

For advanced customization needs, see our [Open Source MCP Server](/advanced/mcp-open-source) documentation.

<Expandable title="Setup in Cursor">
  ## Setup in Cursor

  Other MCP-compatible tools follow about the same pattern.

  The MCP server runs on our servers ([https://api.anchorbrowser.io/mcp](https://api.anchorbrowser.io/mcp)), and is available to all users providing their Anchor API Key.

  ### Configure MCP in Cursor

  <Steps>
    <Step title="Open Command Palette">
      Press Command+Shift+P (Mac) or Ctrl+Shift+P (Linux/Windows) and select "Open MCP Configuration File"

      <img src="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-get-settings.png?fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=9f606f6e01b9349d29486f6aa07887c9" alt="Get Cursor MCP Settings" data-og-width="584" width="584" data-og-height="142" height="142" data-path="images/mcp-get-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-get-settings.png?w=280&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=e3a2038dbcf254fa9e7aa68ac0d3769a 280w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-get-settings.png?w=560&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=52d90c6964443d2251c86a5642411bc3 560w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-get-settings.png?w=840&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=e0e6dca0909fd24039a08d0e5a0646f3 840w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-get-settings.png?w=1100&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=e699101125102f5c00c26b065647503d 1100w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-get-settings.png?w=1650&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=209ce2728e69454757aa78a8ddc6bb86 1650w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-get-settings.png?w=2500&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=10a51f81358611b2addf885168c425f5 2500w" />
    </Step>

    <Step title="Open MCP Configurations">
      Click on "Add Custom MCP" or "New MCP Server" if you already have some pre-configured.

      <img src="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-add-custom.png?fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=f9c59aeb3f93c01d4a4f0dd8e27f182e" alt="Add Custom MCP Server" data-og-width="684" width="684" data-og-height="386" height="386" data-path="images/mcp-add-custom.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-add-custom.png?w=280&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=1c5cdfaca98a21287cb871c3d5489537 280w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-add-custom.png?w=560&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=19d6138b9456e0d7e4c4a8150792d2f2 560w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-add-custom.png?w=840&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=eba04cf29df505ad5e306cc2a0e16dab 840w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-add-custom.png?w=1100&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=1af12c87e58e90ab4463c325dea85ec3 1100w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-add-custom.png?w=1650&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=36fcb3e4e1526a4d95184e2ce697be8f 1650w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-add-custom.png?w=2500&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=b8e994dff3fd82848ac1ac8158699f36 2500w" />
    </Step>

    <Step title="Add MCP Server">
      Add inside the `mcpServers` object the following:

      ```json  theme={null}
      "Anchor Browser Agent": {
          "url": "https://api.anchorbrowser.io/mcp",
          "headers": {
              "anchor-api-key": "YOUR_ANCHOR_API_KEY"
          }
      }
      ```

      <Info>
        If you don't have your Anchor API key yet, you can get it from [Anchor UI](https://app.anchorbrowser.io/api-keys).
      </Info>

      You should now see Anchor MCP server in the list of MCP servers in Cursor. It should say '24 tools enabled'. If you don't see it, disable and re-enable Anchor MCP server, or wait a little longer.
    </Step>
  </Steps>
</Expandable>

<Expandable title="Setup in VS Code">
  ## Setup in VS Code

  <Steps>
    <Step title="Install MCP Extension">
      Install the MCP extension for VS Code from the marketplace.
    </Step>

    <Step title="Configure MCP Server">
      Add to your VS Code MCP configuration file:

      ```json  theme={null}
      {
        "mcpServers": {
          "anchor-browser": {
            "url": "https://api.anchorbrowser.io/mcp",
            "headers": {
              "anchor-api-key": "YOUR_ANCHOR_API_KEY"
            }
          }
        }
      }
      ```
    </Step>

    <Step title="Restart VS Code">
      Restart VS Code to load the new MCP server configuration.
    </Step>
  </Steps>
</Expandable>

<Expandable title="Setup in Claude Desktop">
  ## Setup in Claude Desktop

  <Steps>
    <Step title="Open Configuration">
      Open Claude Desktop's configuration file (`claude_desktop_config.json`).
    </Step>

    <Step title="Add Anchor MCP">
      Add the following to your configuration:

      ```json  theme={null}
      {
        "mcpServers": {
          "anchor-browser": {
            "url": "https://api.anchorbrowser.io/mcp",
            "headers": {
              "anchor-api-key": "YOUR_ANCHOR_API_KEY"
            }
          }
        }
      }
      ```
    </Step>

    <Step title="Restart Claude">
      Restart Claude Desktop to apply the configuration.
    </Step>
  </Steps>
</Expandable>

# Usage

Once configured, you can use Anchor Browser directly in your conversations with your AI assistant.

## Available Tools

The hosted MCP integration provides access to all main Anchor capabilities:

<img src="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-available-tools.png?fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=68a79a28abe6fb15867d9d7c4bb0ab01" alt="MCP Tools" data-og-width="661" width="661" data-og-height="251" height="251" data-path="images/mcp-available-tools.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-available-tools.png?w=280&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=8f3476ea57f00ada07f85918a746b6e1 280w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-available-tools.png?w=560&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=9f73492430d7ca1c0469f8dc113b89dc 560w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-available-tools.png?w=840&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=e87ee1f04a1cbf3b647fa0d482d8be4f 840w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-available-tools.png?w=1100&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=66a89d35761d5041c93d0bf50d70d69f 1100w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-available-tools.png?w=1650&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=44f22f895f9135bca3e4a3c8072bf11b 1650w, https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/mcp-available-tools.png?w=2500&fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=faacc3792e9a53842205f6738aa4245c 2500w" />

<Expandable title="Test Generator Example">
  ### Test Generator Example

  ```
  - You are a playwright test generator.
  - You are given a scenario and you need to generate a playwright test for it.
  - DO NOT generate test code based on the scenario alone. 
  - DO run steps one by one using the tools provided by the Anchor Browser Agent MCP.
  - Only after all steps are completed, emit a Playwright TypeScript test that uses @playwright/test based on message history
  - Save generated test file in the tests directory
  - Execute the test file and iterate until the test passes

  Generate a Playwright test for the following scenario:
  1. Navigate to https://www.imdb.com/
  2. search for 'Garfield'
  3. return the director of the last movie
  ```

  <video autoPlay muted loop playsInline src="https://mintcdn.com/anchor-b3ec2715/hJc2I0-WvjLCCXOl/images/garfield-test-generator.mp4?fit=max&auto=format&n=hJc2I0-WvjLCCXOl&q=85&s=9174bc30dd24beede6a343fb305f7b7b" alt="Test Generator" data-path="images/garfield-test-generator.mp4" />

  <Expandable title="garfield-test.spec.ts File">
    That is the generated test file:

    ```js  theme={null}
    import { test, expect } from '@playwright/test';

    test('Find director of the last Garfield movie', async ({ page }) => {
      // Step 1: Navigate to IMDB
      await page.goto('https://www.imdb.com/');
      
      // Verify we're on the IMDB homepage
      await expect(page).toHaveTitle(/IMDb/);
      
      // Step 2: Search for 'Garfield'
      // Click on the search box
      await page.getByTestId('suggestion-search').click();
      
      // Type 'Garfield' into the search box
      await page.getByTestId('suggestion-search').fill('Garfield');
      
      // Submit the search
      await page.getByRole('button', { name: 'Submit search' }).click();
      
      // Verify we're on the search results page
      await expect(page).toHaveURL(/\/find\/\?q=Garfield/);
      await expect(page).toHaveTitle(/Find - IMDb/);
      
      // Step 3: Click on the most recent Garfield movie (The Garfield Movie 2024)
      await page.getByRole('link', { name: 'The Garfield Movie' }).click();
      
      // Verify we're on the movie page
      await expect(page).toHaveURL(/\/title\/tt5779228/);
      await expect(page).toHaveTitle(/The Garfield Movie \(2024\)/);
      
      // Step 4: Extract the director information
      // The director information is displayed in the main content area
      const directorElement = page.locator('text=Director').locator('..').locator('a').first();
      
      // Verify the director is Mark Dindal
      await expect(directorElement).toHaveText('Mark Dindal');
      
      // Log the director name for verification
      const directorName = await directorElement.textContent();
      console.log(`Director of The Garfield Movie (2024): ${directorName}`);
      
      // Assert the expected result
      expect(directorName).toBe('Mark Dindal');
    });
    ```
  </Expandable>
</Expandable>

## Programmatic Usage (Python SDK)

You can also use the hosted MCP service programmatically in your Python applications using the MCP client library:

### Installation

```bash  theme={null}
pip install mcp
```

### Basic Example

```python  theme={null}
import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

async def list_tools():
    async with streamablehttp_client(
        url="https://api.anchorbrowser.io/mcp",
        headers={"anchor-api-key": "sk-your-key"}
    ) as (
        read_stream,
        write_stream,
        _,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            for tool in tools.tools:
                print(f"{tool.name}: {getattr(tool, 'description', '')}")

asyncio.run(list_tools()) 
```

## CI/CD Integration

The hosted MCP service works in CI/CD environments without requiring local browser installations:

```yaml  theme={null}
# GitHub Actions example
name: AI Browser Testing
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run AI tests
        env:
          ANCHOR_API_KEY: ${{ secrets.ANCHOR_API_KEY }}
        run: |
          python ai_test_runner.py
```

## Getting Help

If you encounter issues with the hosted MCP integration:

1. **Check API Key**: Ensure your API key is valid
2. **Restart MCP Client**: Disable and re-enable the MCP server in your client
3. **Contact Support**: Reach out at [support@anchorbrowser.io](mailto:support@anchorbrowser.io)

## Migration from Self-Hosted

Moving from a self-hosted MCP server to our hosted service:

1. **Update Configuration**: Change your MCP client to use `https://api.anchorbrowser.io/mcp`
2. **Add API Key**: Include your Anchor API key in the headers
3. **Remove Local Dependencies**: Uninstall local MCP server and dependencies
4. **Test Integration**: Verify all your existing MCP workflows still work
