# Source: https://docs.anchorbrowser.io/integrations/stagehand.md

# Stagehand

> Integrate Stagehand with Anchor Browser for AI-powered browser automation

## Basic Usage

<CodeGroup>
  ```python python theme={null}
  import os
  import asyncio
  import aiohttp
  import ssl
  from typing import Optional, Dict, Any
  from stagehand import Stagehand

  ssl._create_default_https_context = ssl._create_unverified_context

  API_KEY = os.environ.get("ANCHOR_API_KEY")
  if not API_KEY:
      raise ValueError("ANCHOR_API_KEY is not set")

  async def create_browser_session() -> Dict[str, Any]:
      async with aiohttp.ClientSession() as session:
          async with session.post(
              "https://api.anchorbrowser.io/v1/sessions",
              headers={
                  "anchor-api-key": API_KEY,
                  "Content-Type": "application/json",
              },
              json={
                  "session": {
                      "proxy": {"active": True}
                  },
                  "browser": {
                      "extra_stealth": {"active": True}
                  }
              },
              ssl=False
          ) as response:
              if not response.ok:
                  raise Exception(f"Failed to create session: {response.status}")
              return (await response.json())["data"]

  async def stop_browser_session(session_id: str):
      async with aiohttp.ClientSession() as session:
          async with session.delete(
              f"https://api.anchorbrowser.io/v1/sessions/{session_id}",
              headers={"anchor-api-key": API_KEY},
              ssl=False
          ) as response:
              if response.ok:
                  print(f"Session {session_id} stopped")

  async def run_stagehand():
      session_id: Optional[str] = None
      stagehand: Optional[Stagehand] = None
      
      try:
          session = await create_browser_session()
          session_id = session["id"]
          cdp_url = session["cdp_url"]
          
          # Check for GOOGLE_API_KEY
          google_api_key = os.environ.get("GOOGLE_API_KEY")
          if not google_api_key:
              raise ValueError("Either GOOGLE_API_KEY must be set")
          
          
          stagehand = Stagehand(
              verbose=1,
              log_level="info",
              dom_settle_timeout_ms=60000,
              model_name="google/gemini-2.5-pro",
              env="LOCAL",
              local_browser_launch_options={"cdp_url": cdp_url}
          )
          
          await stagehand.init()
          await stagehand.page.goto("https://example.com")
          await stagehand.page.act("Click on Learn more link")
          print(f"Current URL: {stagehand.page.url}")
      finally:
          if stagehand and not stagehand._closed:
              await stagehand.close()
          if session_id:
              await stop_browser_session(session_id)

  asyncio.run(run_stagehand())
  ```

  ```javascript node.js theme={null}
  import { Stagehand } from "@browserbasehq/stagehand";

  // Disable TLS certificate verification for local development
  process.env["NODE_TLS_REJECT_UNAUTHORIZED"] = "0";

  const API_KEY = process.env.ANCHOR_API_KEY || "";

  // Stagehand configuration factory
  const createStagehandConfig = () => {
    // Check for GOOGLE_API_KEY
    const googleApiKey = process.env.GOOGLE_API_KEY
    if (!googleApiKey) {
      throw new Error('Either GOOGLE_API_KEY must be set');
    }

    return {
      verbose: 1,
      disablePino: true,
      logger: console.log,
      domSettleTimeoutMs: 60_000,
      actionTimeoutMs: 10_000,
      navigationTimeoutMs: 15_000,
      model: "google/gemini-2.5-pro", // Use 'model' instead of 'modelName'
      // API key will auto-load from GOOGLE_API_KEY environment variable
      env: "LOCAL",
      localBrowserLaunchOptions: {
        headless: false,
        viewport: {
          width: 1288,
          height: 711,
        },
      },
    };
  };

  // Browser configuration for Anchor
  const browserConfiguration = {
    session: {
      proxy: {
        active: true,
      }
    },
    browser: {
      extra_stealth: {
        active: true
      }
    }
  };

  async function createBrowserSession() {
    console.log(`Creating browser session with Anchor API...`);
    const response = await fetch(`https://api.anchorbrowser.io/v1/sessions`, {
      method: "POST",
      headers: {
        "anchor-api-key": API_KEY,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(browserConfiguration),
    });

    if (!response.ok) {
      throw new Error(`Failed to create session: ${response.status} ${response.statusText}`);
    }

    const json = await response.json();
    console.log(`Session created:`, json);
    return json.data;
  }

  async function stopBrowserSession(sessionId) {
    console.log(`Stopping browser session ${sessionId}...`);
    const response = await fetch(`https://api.anchorbrowser.io/v1/sessions/${sessionId}`, {
      method: "DELETE",
      headers: {
        "anchor-api-key": API_KEY,
      },
    });

    if (response.ok) {
      console.log(`Session ${sessionId} stopped successfully`);
    } else {
      console.error(`Failed to stop session ${sessionId}:`, response.statusText);
    }
  }

  async function runStagehandTest() {
    let sessionId;
    let stagehand;

    try {
      // Create Anchor browser session
      const session = await createBrowserSession();
      sessionId = session.id;
      
      // Use CDP URL from Anchor Browser session response
      const cdpUrl = session.cdp_url;
      console.log(`CDP URL: ${cdpUrl}`);

      // Initialize Stagehand with Anchor browser
      stagehand = new Stagehand({
        ...createStagehandConfig(),
        env: "LOCAL",
        localBrowserLaunchOptions: {
          cdpUrl: cdpUrl,
        },
      });

      console.log("Stagehand initialized successfully");

      // Initialize Stagehand before using it
      console.log("Initializing Stagehand...");
      await stagehand.init();
      console.log("Stagehand initialization completed");

      // Get the Playwright page from the browser context
      const page = stagehand.ctx.pages()[0];
      if (!page) {
        throw new Error("No page available in browser context");
      }

      // Example test: Navigate to a page and perform some actions
      console.log("Navigating to test page...");
      await page.goto("https://example.com");
      
      console.log("Attempting to click on Learn more link...");
      try {
        // Use Stagehand's act method - it might be on the instance or via actHandler
        await stagehand.act("Click on Learn more link");
        console.log("Click action completed successfully");
      } catch (error) {
        console.log("Click action had timeout issues, but this is often expected for navigation:");
        console.log(error.message);
      }
      
      // Wait a bit for any navigation to complete
      console.log("Waiting for navigation to complete...");
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      console.log("Taking a screenshot...");
      const currentUrl = page.url();
      console.log(`Current URL: ${currentUrl}`);
      const screenshot = await page.screenshot();
      console.log(`Screenshot taken, size: ${screenshot.length} bytes`);
      
      console.log("Test completed successfully!");

    } catch (error) {
      console.error("Error during Stagehand test:", error);
    } finally {
      // Clean up
      if (stagehand) {
        try {
          // Only close if Stagehand was successfully initialized
          if (!stagehand.isClosed) {
            await stagehand.close();
            console.log("Stagehand closed");
          }
        } catch (error) {
          console.error("Error closing Stagehand:", error);
        }
      }
      
      if (sessionId) {
        await stopBrowserSession(sessionId);
      }
    }
  }

  // Run the test
  (async () => {
    console.log("Starting Stagehand sanity test with Anchor...");
    await runStagehandTest();
    console.log("Test completed");
  })();
  ```
</CodeGroup>

<Tip>
  Set `GOOGLE_API_KEY` (or your LLM API key) in your environment variables for Stagehand to function.
</Tip>
