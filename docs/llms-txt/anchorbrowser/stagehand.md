# Source: https://docs.anchorbrowser.io/integrations/stagehand.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Stagehand

> Integrate Stagehand with Anchor Browser for AI-powered browser automation

## Basic Usage

This example demonstrates how to:

1. Create an AnchorBrowser session using the AnchorBrowser SDK
2. Get the CDP URL from the session
3. Connect Stagehand to the browser via CDP
4. Perform AI-powered browser automation

### Prerequisites

<CodeGroup>
  ```bash python theme={null}
  pip install stagehand anchorbrowser
  ```

  ```bash node.js theme={null}
  npm install @browserbasehq/stagehand anchorbrowser
  ```
</CodeGroup>

Set the following environment variables:

* `ANCHORBROWSER_API_KEY` - Your Anchorbrowser API key
* `MODEL_API_KEY`, `OPENAI_API_KEY`, or `GOOGLE_API_KEY` - Your LLM provider API key

<CodeGroup>
  ```python python theme={null}
  from __future__ import annotations

  import asyncio
  import os
  import sys
  from typing import Any, Optional

  from anchorbrowser import AsyncAnchorbrowser

  from stagehand import AsyncStagehand


  async def main() -> None:
      # 1. Check for required environment variables
      anchor_api_key = os.environ.get("ANCHORBROWSER_API_KEY")
      if not anchor_api_key:
          sys.exit(
              "❌ ANCHORBROWSER_API_KEY environment variable is required. "
              "Get your API key from https://anchorbrowser.io"
          )

      model_api_key = os.environ.get("MODEL_API_KEY") or os.environ.get("OPENAI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
      if not model_api_key:
          sys.exit("❌ MODEL_API_KEY, OPENAI_API_KEY, or GOOGLE_API_KEY environment variable is required.")

      # Detect model type from API key format
      if model_api_key.startswith("AIza"):
          model_name = "google/gemini-2.0-flash"
          print(f"   Detected Google API key, using model: {model_name}")
      else:
          model_name = "openai/gpt-4o-mini"
          print(f"   Detected OpenAI API key, using model: {model_name}")

      anchorbrowser_session_id: Optional[str] = None
      stagehand_session_id: Optional[str] = None

      # Initialize Anchorbrowser client
      anchor_client = AsyncAnchorbrowser(api_key=anchor_api_key)

      try:
          # 2. Create Anchorbrowser session using the SDK
          print("🌐 Creating Anchorbrowser session...")
          anchor_session = await anchor_client.sessions.create()
          
          if not anchor_session.data or not anchor_session.data.cdp_url:
              raise ValueError(f"Anchorbrowser session did not return a CDP URL. Response: {anchor_session}")
          
          anchorbrowser_session_id = anchor_session.data.id
          cdp_url = anchor_session.data.cdp_url
          
          print("✅ Anchorbrowser session created!")
          print(f"   Session ID: {anchorbrowser_session_id}")
          print(f"   CDP URL: {cdp_url}")

          # 3. Initialize Stagehand with the CDP URL
          print("\n🚀 Initializing Stagehand with CDP URL...")
          async with AsyncStagehand(
              server="local",
              model_api_key=model_api_key,
              local_openai_api_key=model_api_key,
              local_ready_timeout_s=30.0,
          ) as client:
              # Start session with CDP URL pointing to Anchorbrowser
              # Note: cdp_url must be inside launch_options for connecting to external browsers
              session_response = await client.sessions.start(
                  model_name=model_name,
                  browser={
                      "type": "local",
                      "launch_options": {
                          "cdp_url": cdp_url,
                      },
                  },
              )
              stagehand_session_id = session_response.data.session_id
              print("✅ Stagehand initialized successfully!")
              print(f"   Stagehand Session ID: {stagehand_session_id}")

              try:
                  # 4. Navigate to Hacker News
                  print("\n📍 Navigating to Hacker News...")
                  await client.sessions.navigate(
                      id=stagehand_session_id,
                      url="https://news.ycombinator.com",
                  )
                  print("✅ Navigation complete")

                  # 5. Use Stagehand's AI-powered extraction
                  print("\n🔍 Extracting top stories using AI...")
                  extract_response = await client.sessions.extract(
                      id=stagehand_session_id,
                      instruction="Extract the titles and URLs of the first 5 stories on the page",
                      schema={
                          "type": "object",
                          "properties": {
                              "stories": {
                                  "type": "array",
                                  "items": {
                                      "type": "object",
                                      "properties": {
                                          "title": {"type": "string"},
                                          "url": {"type": "string"},
                                      },
                                      "required": ["title"],
                                  },
                              },
                          },
                          "required": ["stories"],
                      },
                  )

                  print("\n📰 Extracted stories:")
                  result: Any = extract_response.data.result
                  if isinstance(result, dict) and "stories" in result:
                      stories = result["stories"]
                      if isinstance(stories, list):
                          for i, story in enumerate(stories, 1):
                              if isinstance(story, dict):
                                  title = story.get("title", "N/A")
                                  url = story.get("url")
                                  print(f"   {i}. {title}")
                                  if url:
                                      print(f"      URL: {url}")
                  else:
                      print(f"   Raw result: {result}")

                  # 6. Use Stagehand's observe to find clickable elements
                  print("\n👁️  Observing page for login link...")
                  observe_response = await client.sessions.observe(
                      id=stagehand_session_id,
                      instruction="find the login link",
                  )
                  actions = observe_response.data.result
                  print(f"   Found {len(actions)} possible actions")
                  if actions:
                      print(f"   First action: {actions[0].description}")

                  # 7. Use Stagehand's act to perform an action
                  print("\n🖱️  Clicking on the first story...")
                  act_response = await client.sessions.act(
                      id=stagehand_session_id,
                      input="click on the first story title",
                  )
                  print(f"   Act completed: {act_response.data.result.message}")

                  # Wait a moment for navigation
                  await asyncio.sleep(2)

                  print("\n✅ Test completed successfully!")

              finally:
                  # 8. End the Stagehand session
                  if stagehand_session_id:
                      print("\n🛑 Ending Stagehand session...")
                      await client.sessions.end(id=stagehand_session_id)
                      print("✅ Stagehand session ended")

      finally:
          # 9. Delete the Anchorbrowser session using the SDK
          if anchorbrowser_session_id:
              print("\n🧹 Deleting Anchorbrowser session...")
              try:
                  await anchor_client.sessions.delete(anchorbrowser_session_id)
                  print("✅ Anchorbrowser session deleted")
              except Exception as e:
                  print(f"⚠️  Failed to delete Anchorbrowser session: {e}")

          # Close the Anchorbrowser client
          await anchor_client.close()


  if __name__ == "__main__":
      asyncio.run(main())
  ```

  ```typescript node.js theme={null}
  import { Stagehand } from "@browserbasehq/stagehand";
  import Anchorbrowser from "anchorbrowser";
  import { z } from "zod";

  async function main(): Promise<void> {
    // 1. Check for required environment variables
    const anchorApiKey = process.env.ANCHORBROWSER_API_KEY;
    if (!anchorApiKey) {
      console.error(
        "❌ ANCHORBROWSER_API_KEY environment variable is required. " +
          "Get your API key from https://anchorbrowser.io"
      );
      process.exit(1);
    }

    const modelApiKey =
      process.env.MODEL_API_KEY ||
      process.env.OPENAI_API_KEY ||
      process.env.GOOGLE_API_KEY;
    if (!modelApiKey) {
      console.error(
        "❌ MODEL_API_KEY, OPENAI_API_KEY, or GOOGLE_API_KEY environment variable is required."
      );
      process.exit(1);
    }

    // Detect model type from API key format
    let modelName: string;
    if (modelApiKey.startsWith("AIza")) {
      modelName = "gemini-2.0-flash";
      console.log(`   Detected Google API key, using model: ${modelName}`);
    } else {
      modelName = "gpt-4o-mini";
      console.log(`   Detected OpenAI API key, using model: ${modelName}`);
    }

    let anchorbrowserSessionId: string | undefined;
    let stagehand: Stagehand | undefined;

    // Initialize Anchorbrowser client
    const anchorClient = new Anchorbrowser({
      apiKey: anchorApiKey,
    });

    try {
      // 2. Create Anchorbrowser session using the SDK
      console.log("🌐 Creating Anchorbrowser session...");
      const anchorSession = await anchorClient.sessions.create();

      if (!anchorSession.data?.cdp_url) {
        throw new Error(
          `Anchorbrowser session did not return a CDP URL. Response: ${JSON.stringify(anchorSession)}`
        );
      }

      anchorbrowserSessionId = anchorSession.data.id;
      const cdpUrl = anchorSession.data.cdp_url;

      console.log("✅ Anchorbrowser session created!");
      console.log(`   Session ID: ${anchorbrowserSessionId}`);
      console.log(`   CDP URL: ${cdpUrl}`);

      // 3. Initialize Stagehand V3 with the CDP URL
      console.log("\n🚀 Initializing Stagehand V3 with CDP URL...");
      stagehand = new Stagehand({
        env: "LOCAL",
        model: modelName,
        localBrowserLaunchOptions: {
          cdpUrl: cdpUrl,
        },
        verbose: 1,
      });

      await stagehand.init();
      console.log("✅ Stagehand V3 initialized successfully!");

      try {
        // Get the active page
        const page = stagehand.context.activePage();
        if (!page) {
          throw new Error("No active page found");
        }

        // 4. Navigate to Hacker News
        console.log("\n📍 Navigating to Hacker News...");
        await page.goto("https://news.ycombinator.com");
        console.log("✅ Navigation complete");

        // 5. Use Stagehand's AI-powered extraction
        console.log("\n🔍 Extracting top stories using AI...");
        const StoriesSchema = z.object({
          stories: z.array(
            z.object({
              title: z.string(),
              url: z.string().optional(),
            })
          ),
        });

        const extractResult = await stagehand.extract(
          "Extract the titles and URLs of the first 5 stories on the page",
          StoriesSchema
        );

        console.log("\n📰 Extracted stories:");
        if (extractResult.stories) {
          extractResult.stories.forEach((story, i) => {
            console.log(`   ${i + 1}. ${story.title}`);
            if (story.url) {
              console.log(`      URL: ${story.url}`);
            }
          });
        }

        // 6. Use Stagehand's observe to find clickable elements
        console.log("\n👁️  Observing page for login link...");
        const actions = await stagehand.observe("find the login link");
        console.log(`   Found ${actions.length} possible actions`);
        if (actions.length > 0) {
          console.log(`   First action: ${actions[0].description}`);
        }

        // 7. Use Stagehand's act to perform an action
        console.log("\n🖱️  Clicking on the first story...");
        const actResult = await stagehand.act("click on the first story title");
        console.log(`   Act completed: ${actResult.message}`);

        // Wait a moment for navigation
        await new Promise((resolve) => setTimeout(resolve, 2000));

        console.log("\n✅ Test completed successfully!");
      } finally {
        // 8. Close Stagehand
        if (stagehand) {
          console.log("\n🛑 Closing Stagehand...");
          await stagehand.close();
          console.log("✅ Stagehand closed");
        }
      }
    } finally {
      // 9. Delete the Anchorbrowser session using the SDK
      if (anchorbrowserSessionId) {
        console.log("\n🧹 Deleting Anchorbrowser session...");
        try {
          await anchorClient.sessions.delete(anchorbrowserSessionId);
          console.log("✅ Anchorbrowser session deleted");
        } catch (e) {
          console.log(`⚠️  Failed to delete Anchorbrowser session: ${e}`);
        }
      }
    }
  }

  main().catch((error) => {
    console.error("Fatal error:", error);
    process.exit(1);
  });
  ```
</CodeGroup>

<Tip>
  Set `ANCHOR_BROWSER_API_KEY` for AnchorBrowser authentication, and one of `MODEL_API_KEY`, `OPENAI_API_KEY`, or `GOOGLE_API_KEY` for your LLM provider.
</Tip>
