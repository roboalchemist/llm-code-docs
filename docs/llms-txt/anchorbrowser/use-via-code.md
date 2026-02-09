# Source: https://docs.anchorbrowser.io/quickstart/use-via-code.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Code Quick Start

This page is a quick start using code. For a quick start using an Integration (Make, Langchain, CrewAI, etc.) [click here](/quickstart/use-via-api).

<Steps>
  <Step title="Fetch API Key">
    In [Anchor UI](https://app.anchorbrowser.io/api-keys), copy your API key
  </Step>

  <Step title="Install playwright">
    <CodeGroup>
      ```bash node.js theme={null}
      npm i playwright-core
      ```

      ```bash python theme={null}
      pip3 install playwright
      ```
    </CodeGroup>
  </Step>

  <Step title="Create a session via API">
    Also available by the [live playground](https://app.anchorbrowser.io/playground)

    <CodeGroup>
      ```javascript node.js theme={null}
      const axios = require("axios");

      (async () => {
          const session = await axios.post("https://api.anchorbrowser.io/v1/sessions", {}, {
              headers: {
                  "anchor-api-key": process.env.ANCHOR_API_KEY,
                  "Content-Type": "application/json"
              }
          });
          const cdp_url = session.data.data.cdp_url;
          console.log("Session's CDP_URL for later use\n", cdp_url);
      })().catch(console.error);
      ```

      ```python python theme={null}
      import requests
      import os

      url = "https://api.anchorbrowser.io/v1/sessions"
      headers = {
          "anchor-api-key": f"{os.getenv('ANCHOR_API_KEY')}",
          'Content-Type': 'application/json'
        }
      session = requests.post(url, headers=headers)

      cdp_url = session.json()['data']['cdp_url']
      print("Session's CDP_URL for later use\n", cdp_url)
      ```
    </CodeGroup>
  </Step>

  <Step title="Run sample code">
    <CodeGroup>
      ```javascript node.js theme={null}
      const { chromium } = require("playwright-core");

      (async () => {
          // Connect to the session
          const browser = await chromium.connectOverCDP(cdp_url);
          const page = await browser.newPage();

          // Navigate to Anchor Browser's website
          await page.goto("https://anchorbrowser.io");
          console.log("Page title:", await page.title());

          await browser.close();
      })().catch(console.error);
      ```

      ```python python theme={null}
      import os
      from playwright.sync_api import sync_playwright

      with sync_playwright() as p:
          browser = p.chromium.connect_over_cdp(cdp_url)
          page = browser.new_page()
          
          # Navigate to Anchor Browser's website
          page.goto("https://anchorbrowser.io")
          print("Page title:", page.title())
          
          browser.close()
      ```
    </CodeGroup>
  </Step>

  <Step title="Advanced browser configuration">
    Anchor Browser supports different configurations of the browser session (see [API reference](/api-reference/browser-sessions/start-browser-session) for all options).
    Some of the most common configurations are:

    * [Proxy Configuration](/advanced/proxy)
    * [Profiles to store Authenticated Sessions](/essentials/authentication-and-identity)
    * [Session Timeout](/advanced/session-timeout)

    To use a browser with a specific configuration, first create a browser session with the desired configuration.

    <CodeGroup>
      ```javascript node.js theme={null}
      const axios = require("axios");

      (async () => {
          const browserConfiguration = {
              session: {
                  "recording": { "active": false }, // Default is true
                  // Proxy configuration
                  proxy: {
                      active: true,
                      type: "anchor_residential",
                      country_code: "it"
                  },
                  // Session lifetime management
                  "timeout": {
                      "max_duration": 1, // 1 minute
                      "idle_timeout": 1   // 1 minute
                  }
              }
          };

          const response = await axios.post(
              "https://api.anchorbrowser.io/v1/sessions",
              browserConfiguration,
              { headers: {
                  "anchor-api-key": process.env.ANCHOR_API_KEY,
                  "Content-Type": "application/json",
              },
          });

          const session = response.data.data;
          console.log("Session created:", session.id); // Keep this ID for later use
      })().catch(console.error);
      ```

      ```python python theme={null}
      import os
      import requests # `pip3 install requests` if needed.

      browserConfiguration = {
          "session": {
              "recording": { "active": False }, # Default is True
              # Proxy configuration
              "proxy": {
                  "active": True,
                  "type": "anchor_residential",
                  "country_code": "it"
              },
              # Session lifetime management
              "timeout": {
                  "max_duration": 1, # 1 minute
                  "idle_timeout": 1   # 1 minute
              }
          },
      }

      response = requests.post(
          "https://api.anchorbrowser.io/v1/sessions",
          headers={
              "anchor-api-key": os.getenv("ANCHOR_API_KEY"),
              "Content-Type": "application/json",
          }, json=browserConfiguration
      )

      response.raise_for_status()
      session = response.json()["data"]
      print("Session created:", session["id"]) # Keep this ID for later use
      ```
    </CodeGroup>
  </Step>

  <Step title="Session reconnection">
    Reconnect to an existing session using the session CDP Url.

    <CodeGroup>
      ```javascript node.js theme={null}
      const { chromium } = require("playwright-core");
      const ANCHOR_API_KEY = process.env.ANCHOR_API_KEY;

      (async () => {
          const browser = await chromium.connectOverCDP(sessionCdpUrl);
          const page = await browser.newPage();

          // Check the IP address
          await page.goto("https://www.whatismyip.com/");
          await page.waitForTimeout(10000)
          console.log(await page.textContent('#region-state'))

          // Close browser but session remains active
          await browser.close();
      })().catch(console.error); 
      ```

      ```python python theme={null}
      import os
      from playwright.sync_api import sync_playwright

      ANCHOR_API_KEY = os.getenv("ANCHOR_API_KEY")

      # Connect to the session
      with sync_playwright() as p:
          browser = p.chromium.connect_over_cdp(
              f"wss://connect.anchorbrowser.io?apiKey={ANCHOR_API_KEY}&sessionId={session['id']}"
          )
          page = browser.new_page()
          
          # Check the IP address
          page.goto("https://www.whatismyip.com/")
          page.wait_for_timeout(10000)
          print(page.text_content('#region-state'))

          # Close browser but session remains active
          browser.close()

      ```
    </CodeGroup>
  </Step>
</Steps>
