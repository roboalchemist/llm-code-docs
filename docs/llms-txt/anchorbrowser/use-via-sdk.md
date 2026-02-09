# Source: https://docs.anchorbrowser.io/quickstart/use-via-sdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# SDK Quick Start

This page is a quick start using our official SDK.

For complete documentation and advanced usage examples, visit our package repositories:

* **Node.js**: [anchorbrowser on npm](https://www.npmjs.com/package/anchorbrowser)
* **Python**: [anchorbrowser on PyPI](https://pypi.org/project/anchorbrowser/)

<Steps>
  <Step title="Fetch API Key">
    In [Anchor UI](https://app.anchorbrowser.io/api-keys), copy your API key
  </Step>

  <Step title="Install the SDK">
    <CodeGroup>
      ```bash node.js theme={null}
      npm install anchorbrowser
      ```

      ```bash python theme={null}
      pip install anchorbrowser
      ```
    </CodeGroup>
  </Step>

  <Step title="Initialize the SDK">
    Set up the Anchor Browser client with your API key:

    <CodeGroup>
      ```javascript node.js theme={null}
      import AnchorClient from "anchorbrowser";

      const anchorClient = new AnchorClient({
        apiKey: process.env.ANCHOR_API_KEY,
      });
      ```

      ```python python theme={null}
      import os
      from anchorbrowser import Anchorbrowser

      anchor_client = Anchorbrowser(
          api_key=os.getenv("ANCHOR_API_KEY")
      )
      ```
    </CodeGroup>
  </Step>

  <Step title="AI Agent Browser Automation">
    Use AI agents to automate browser tasks with natural language commands:

    <CodeGroup>
      ```javascript node.js theme={null}
      (async () => {
        // Simple navigation task
        const result = await anchorClient.agent.task(
          "go to news.ycombinator.com and get the title of the first story"
        );
        console.log("Task result:", result);
        
        // Task with execution step monitoring
        const executionStepLogs = [];
        const navigationResult = await anchorClient.agent.task(
          "go to news.ycombinator.com and get the title of the first story",
          {
            taskOptions: {
              onAgentStep: (executionStep) => {
                console.log("Agent step:", executionStep);
                executionStepLogs.push(executionStep);
              },
            },
          }
        );
        console.log("Navigation result:", navigationResult)
        console.log("Execution step logs count:", executionStepLogs.length)
        })();
      ```

      ```python python theme={null}
      # Simple navigation task
      result = anchor_client.agent.task(
          "go to news.ycombinator.com and get the title of the first story"
      )
      print("Task result:", result)

      # Task with execution step monitoring
      execution_step_logs = []
      def on_agent_step(execution_step):
          print("Agent step:", execution_step)
          execution_step_logs.append(execution_step)

      navigation_result = anchor_client.agent.task(
          "go to news.ycombinator.com and get the title of the first story",
          task_options={
              "on_agent_step": on_agent_step
          }
      )
      print("Navigation result:", navigation_result)
      print("Execution step logs count:", len(execution_step_logs))
      ```
    </CodeGroup>
  </Step>
</Steps>

## Additional Usage

### Structured Data Extraction

Extract structured data from webpages using schemas:

<CodeGroup>
  ```javascript node.js theme={null}
  import { z } from "zod";

  (async () => {

    // Define your data schema
    const extractionSchema = z.object({
      title: z.string(),
      description: z.string(),
      price: z.string().optional(),
    });
    
    // Extract structured data from product page
    const structuredResult = await anchorClient.agent.task(
      "Extract the product title, description, and price from this Amazon product page",
      {
        taskOptions: {
          outputSchema: z.toJSONSchema(extractionSchema),
          url: "https://www.amazon.com/dp/B0D7D9N7X3",
        },
      }
    );
    
    // Validate the result
    const validatedData = extractionSchema.safeParse(structuredResult);
    if (validatedData.success) {
      console.log("Product title:", validatedData.data.title);
      console.log("Description:", validatedData.data.description);
      console.log("Price:", validatedData.data.price);
    } else {
      console.error("Validation failed:", validatedData.error);
    }
  })();
  ```

  ```python python theme={null}
  from pydantic import BaseModel
  from typing import Optional
  import ast

  # Define your data schema
  class ProductSchema(BaseModel):
      title: str
      description: str
      price: Optional[str] = None

  # Extract structured data from product page
  structured_result = anchor_client.agent.task(
      "Extract the product title, description, and price from this Amazon product page",
      task_options={
          "output_schema": ProductSchema.model_json_schema(),
          "url": "https://www.amazon.com/dp/B0D7D9N7X3"
      }
  )

  # Validate the result
  validated_data = ProductSchema.model_validate(ast.literal_eval(structured_result))   
  print("Product title:", validated_data.title)
  print("Description:", validated_data.description)
  print("Price:", validated_data.price)
  ```
</CodeGroup>

### Screenshots

Capture screenshots of your current session view.

<CodeGroup>
  ```javascript node.js theme={null}
  import fs from "fs/promises";

  (async () => {
    // Create a session for screenshot
    const screenshotSession = await anchorClient.sessions.create();
    const screenshotBrowser = await anchorClient.browser.connect(screenshotSession.data.id);
    const screenshotPage = screenshotBrowser.contexts()[0].pages()[0];
    await screenshotPage.goto("https://example.com");

    // Capture screenshot from the session
    const screenshot = await anchorClient.tools.screenshotWebpage({
      sessionId: screenshotSession.data.id,
    });

    // Get screenshot data
    const buffer = await screenshot.arrayBuffer();
    console.log("Screenshot captured, size:", buffer.byteLength);

    // Save screenshot to file
    await fs.writeFile("screenshot.png", Buffer.from(buffer));
    console.log("Screenshot saved as screenshot.png");
  })();
  ```

  ```python python theme={null}
  # Create a session for screenshot
  screenshot_session = anchor_client.sessions.create()
  with anchor_client.browser.connect(screenshot_session.data.id) as screenshot_browser:
      screenshot_page = screenshot_browser.contexts[0].pages[0]
      screenshot_page.goto("https://example.com")

  # Capture screenshot from the session
  screenshot = anchor_client.tools.screenshot_webpage(
      session_id=screenshot_session.data.id
  )

  # Get screenshot data
  screenshot_data = screenshot.read()
  print("Screenshot captured, size:", len(screenshot_data))

  # Save screenshot to file
  with open("screenshot.png", "wb") as f:
     f.write(screenshot_data)
     print("Screenshot saved as screenshot.png")
  ```
</CodeGroup>

### Advanced Configuration

Configure browser sessions with proxies, timeouts, and other options:

<CodeGroup>
  ```javascript node.js theme={null}
  // Create session with advanced configuration
  const sessionConfig = {
    session: {
      recording: {active: false}, // Disable session recording
      proxy: {
        active: true,
        type: "anchor_residential",
        country_code: "us",
      },
      timeout: {
        max_duration: 5, // 5 minutes
        idle_timeout: 1, // 1 minute
      }
    },
  };

  const configuredSession = await anchorClient.sessions.create(sessionConfig);
  const result = await anchorClient.agent.task(
    "What is my IP address and where am I?",
    {
    sessionId: configuredSession.data.id,
  });
  console.log(result);
  ```

  ```python python theme={null}
  # Create session with advanced configuration
  session_config = {
    "recording": {"active": False},  # Disable session recording
    "proxy": {
        "active": True,
        "type": "anchor_residential",
        "country_code": "us"
    },
    "timeout": {
        "max_duration": 5,
        "idle_timeout": 1
    }
  }

  configured_session = anchor_client.sessions.create(session=session_config)
  result = anchor_client.agent.task(
    session_options=configured_session,
    prompt="What is my IP address and where am I?"
    )
  print(result)
  ```
</CodeGroup>

## From SDK to Browser: Run Extra Playwright Code

### Standalone Browser Creation

Create a standalone browser instance:

<CodeGroup>
  ```javascript node.js theme={null}
  (async () => {
  // Create standalone browser
  const standaloneBrowser = await anchorClient.browser.create();
  const page = standaloneBrowser.contexts()[0].pages()[0];
  await page.goto("https://httpbin.org/ip");

  console.log("Current URL:", page.url());

  // Disconnect (session keeps running)
  standaloneBrowser.close();
  })();
  ```

  ```python python theme={null}
  # Create standalone browser
  with anchor_client.browser.create() as standalone_browser:
      page = standalone_browser.contexts[0].pages[0]
      page.goto("https://httpbin.org/ip")
      print("Current URL:", page.url)
  ```
</CodeGroup>

### Browser Task with Session Control

Use AI agents with direct browser control:

<CodeGroup>
  ```javascript node.js theme={null}
  // Browser task with session control
  const browserTask = await anchorClient.agent.browserTask(
    "go to github.com/trending and find the most popular JavaScript repository"
  );

  console.log("Session ID:", browserTask.sessionId);

  // Access the Playwright browser instance
  const playwrightBrowser = browserTask.playwrightBrowser;
  const page = playwrightBrowser.contexts()[0].pages()[0];

  // Direct Playwright manipulation
  await page.goto("https://stackoverflow.com/");
  console.log("Current URL:", page.url());

  // Wait for task completion
  const taskResult = await browserTask.taskResultPromise;
  console.log("Final result:", taskResult);

  browserTask.playwrightBrowser.close();
  ```

  ```python python theme={null}
  # Browser task with session control
  browser_task = anchor_client.agent.browser_task(
      "go to github.com/trending and find the most popular JavaScript repository"
  )

  print("Session ID:", browser_task["session_id"])

  # Access the Playwright browser instance
  playwright_browser = browser_task["playwright_browser"]
  with playwright_browser as browser:
      page = browser.contexts[0].pages[0]

      # Direct Playwright manipulation
      page.goto("https://stackoverflow.com/")
      print("Current URL:", page.url)

      # Wait for task completion
      task_result = browser_task["task_result_task"]
      print("Final result:", task_result)
  ```
</CodeGroup>

### Manual Session Management

Create and manage browser sessions manually:

<CodeGroup>
  ```javascript node.js theme={null}
  // Create session and connect it later
  const sessionResponse = await anchorClient.sessions.create();
  const sessionId = sessionResponse.data.id;

  const browser = await anchorClient.browser.connect(sessionId);
  const context = browser.contexts()[0];
  const page = context.pages()[0];
  await page.goto("https://reddit.com/r/programming");

  console.log("Current URL:", page.url());

  browser.close();
  ```

  ```python python theme={null}
  # Create session and connect it later
  session_response = anchor_client.sessions.create()
  session_id = session_response.data.id

  with anchor_client.browser.connect(session_id) as browser:
      context = browser.contexts[0]
      page = context.pages[0]
      page.goto("https://reddit.com/r/programming")
      print("Current URL:", page.url)
  ```
</CodeGroup>

## Key SDK Benefits

The Anchor Browser SDK provides several advantages over direct API usage:

* **AI Agent Integration**: Use natural language to automate complex browser tasks
* **Structured Data Extraction**: Define schemas and extract data in a predictable format
* **Seamless Playwright Integration**: Full access to Playwright's powerful browser automation capabilities
* **Session Management**: Easy creation and management of persistent browser sessions
* **Built-in Tools**: Screenshot capture, proxy management, and more
* **Type Safety**: Full TypeScript support with proper type definitions

## Next Steps

* Explore the [API Reference](/api-reference) for detailed documentation
* Learn about [Authentication and Identity](/essentials/authentication-and-identity) management
* Check out [Advanced Proxy Configuration](/advanced/proxy) for location-specific browsing
