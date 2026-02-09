# Source: https://docs.anchorbrowser.io/agent-frameworks/custom-agent-framework.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Integration

Anchor Browser enables integration with custom AI frameworks to empower agents with the ability to navigate and interact with the web effectively. You can leverage browser sessions within your own custom AI framework to automate workflows, explore the web, or interact with web content dynamically.

The integration methods for a custom AI framework include:

* **As a Flexible Browser Tool**: Utilize Anchor Browser as a general-purpose browser tool that allows your AI agent to freely explore the web and perform dynamic interactions.
* **As a Specific-Flow Tool Defined in Your Custom Framework**: Create reusable, custom tools in your AI framework to handle specific workflows or sequences of interactions.
* **As a Specific-Flow Tool Defined in Anchor Browser**: Define tools on the Anchor platform and invoke them using your custom AI framework through the Anchor API, allowing your agent to use predefined browser sessions and tools.

## Quick Start - Use Anchor Browser as a Flexible Browser Tool

Your custom AI framework can directly integrate with Anchor Browser, allowing your agent to interact with the web dynamically. Below is an example of how you can connect your custom AI framework to Anchor Browser, enabling the agent to perform various tasks.

<Accordion title="Code example - Use Anchor Browser as a flexible browser tool">
  <CodeGroup>
    ```python python theme={null}
    import requests
    from playwright.sync_api import sync_playwright

    ANCHOR_API_KEY = "YOUR_ANCHOR_API_KEY"  # Replace with your actual API key

    # Define a function to use Anchor Browser as a tool for web-based tasks
    def use_anchor_browser(command):
        with sync_playwright() as p:
            # Connect to Anchor Browser session
            browser = p.chromium.connect_over_cdp(
                f"wss://connect.anchorbrowser.io?apiKey={ANCHOR_API_KEY}"
            )
            page = browser.new_page()
            page.goto(command['url'])

            # Perform specific actions as needed
            if command.get('action') == 'search':
                page.fill(command['search_box'], command['search_text'])
                page.click(command['search_button'])

            # Extract and return data if needed
            result = page.content()

            browser.close()
            return result

    # Example usage in your custom AI framework
    command = {
        'url': 'https://example.com',
        'action': 'search',
        'search_box': 'input[name="q"]',
        'search_text': 'Anchor Browser',
        'search_button': 'button[type="submit"]'
    }

    result = use_anchor_browser(command)
    print(result)
    ```

    ```jsx node.js theme={null}
    import { chromium } from 'playwright-core';

    const ANCHOR_API_KEY = process.env.ANCHOR_API_KEY;  // Replace with your actual API key stored in environment variables

    // Define a function to use Anchor Browser as a tool for web-based tasks
    async function useAnchorBrowser(command) {
      // Connect to Anchor Browser session
      const browser = await chromium.connectOverCDP(
        `wss://connect.anchorbrowser.io?apiKey=${ANCHOR_API_KEY}`
      );

      const page = await browser.newPage();
      await page.goto(command.url);

      // Perform specific actions as needed
      if (command.action === 'search') {
        await page.fill(command.search_box, command.search_text);
        await page.click(command.search_button);
      }

      // Extract and return data if needed
      const result = await page.content();

      await browser.close();
      return result;
    }

    // Example usage in your custom AI framework
    const command = {
      url: 'https://example.com',
      action: 'search',
      search_box: 'input[name="q"]',
      search_text: 'Anchor Browser',
      search_button: 'button[type="submit"]'
    };

    const result = await useAnchorBrowser(command);
    console.log(result);
    ```
  </CodeGroup>
</Accordion>

## Use Anchor Browser as a Specific-Flow Tool Defined in a Custom Framework

Anchor Browser can also be integrated into your custom AI framework to create specific workflow tools. These tools can handle specialized tasks that your agent needs to perform repeatedly, providing consistency and reducing the need for writing duplicate code.

Here is an example of creating a specific tool using Anchor Browser that can be utilized by your custom AI framework for automating targeted tasks.

<Accordion title="Code example - Use Anchor Browser as a specific-flow tool in a custom AI framework">
  <CodeGroup>
    ```python python theme={null}
    import requests
    from playwright.sync_api import sync_playwright

    ANCHOR_API_KEY = "YOUR_ANCHOR_API_KEY"  # Replace with your actual API key

    # Define a custom tool for interacting with a specific web application
    def specific_anchor_tool(command):
        with sync_playwright() as p:
            # Connect to Anchor Browser session
            browser = p.chromium.connect_over_cdp(
                f"wss://connect.anchorbrowser.io?apiKey={ANCHOR_API_KEY}"
            )
            page = browser.new_page()
            page.goto(command['url'])

            # Perform specific actions based on the command
            if command.get('action') == 'extract':
                result = page.text_content(command['selector'])
                browser.close()
                return result

            browser.close()

    # Example usage in your custom AI framework
    command = {
        'url': 'https://example.com',
        'action': 'extract',
        'selector': '#data'
    }

    result = specific_anchor_tool(command)
    print(result)
    ```

    ```jsx node.js theme={null}
    import { chromium } from 'playwright-core';

    const ANCHOR_API_KEY = process.env.ANCHOR_API_KEY;  // Replace with your actual API key stored in environment variables

    // Define a custom specific-flow tool for interacting with a specific web application
    async function specificAnchorTool(command) {
      // Connect to Anchor Browser session
      const browser = await chromium.connectOverCDP(
        `wss://connect.anchorbrowser.io?apiKey=${ANCHOR_API_KEY}`
      );

      const page = await browser.newPage();
      await page.goto(command.url);

      // Perform specific actions based on the command
      if (command.action === 'extract') {
        const result = await page.textContent(command.selector);
        await browser.close();
        return result;
      }

      await browser.close();
    }

    // Example usage in your custom AI framework
    const command = {
      url: 'https://example.com',
      action: 'extract',
      selector: '#data'
    };

    const result = await specificAnchorTool(command);
    console.log(result);
    ```
  </CodeGroup>
</Accordion>
