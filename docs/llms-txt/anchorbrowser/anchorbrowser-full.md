# Anchorbrowser Documentation

Source: https://docs.anchorbrowser.io/llms-full.txt

---

# b0.dev - Deterministic Browser Tasks
Source: https://docs.anchorbrowser.io/B0

B0 makes browser automation easy. Just describe what you want to do, and B0 does it for you. No coding required.

B0 is the easiest way to automate anything on the web. Just tell B0 what you want to do in plain English, and it handles the rest.

<video />

## [Try it now!](https://b0.dev)

# How B0 Works

B0 takes your prompt and runs the following process:

<Steps>
  <Step title="Exploration">
    B0 passes the prompt to a dedicated exploration agent, which extracts the main goal of the task and break it down to different steps, as well as the expected output.
  </Step>

  <Step title="Session Recording">
    Whether "Demonstrate Manually" was chosen or not, B0 creates a cloud [Session](/quickstart/use-via-code) and Record the interactions with the browser for later usage.
  </Step>

  <Step title="Deterministic Code Generation">
    B0 uses the interaction recordings from last step, and use them to generate a deterministic code, creates a [Task](/advanced/tasks) with that code, and run it.
  </Step>

  <Step title="Evaluation">
    B0 compares between the results of the 2 execution and determines whether the results are equivalent and summarizes it to the user.
  </Step>
</Steps>

<Information>
  The task created in the process is available in the [Tasks Page](/advanced/tasks) and from the SDK.
</Information>

## Manual Demonstration

This feature allows you to show B0 the flow you want manually, while recording, B0 analyzes what's done and with the context of the prompt, it will generate the deterministic code as expected.

<img />

## Core Advantages

<CardGroup>
  <Card title="Reduced Costs" icon="dollar">
    Agent costs applied only on task creation. Any additional run doesn't require an agent involvement.
  </Card>

  <Card title="Works Every Time" icon="check-circle">
    B0 creates reliable automations that work consistently, for generating deterministic code.
  </Card>

  <Card title="Supported Authentication" icon="key">
    B0 is based on Anchor's SDK, which expose methods for [MFA handling](/advanced/mfa).
  </Card>
</CardGroup>

<Note>
  **Need help?** B0 works best when you describe exactly what you want to do. Be specific about which websites, what actions to take, and what results you expect. You can also show B0 how to do it by demonstrating the steps yourself.
</Note>


# Ad Blocker
Source: https://docs.anchorbrowser.io/advanced/adblocker

Block ads, trackers, and unwanted content in your browser sessions

Ad blocking is enabled by default in Anchor Browser. It blocks ads, trackers, and malicious content to improve page load times and create cleaner automation.

<Note>
  Ad blocking is enabled by default. Disable it only if you need to test ad-related functionality.
</Note>

## Quick Start

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  (async () => {
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    
    const session = await anchorClient.sessions.create({
      // Optional: ad blocking is enabled by default, so this configuration is not required
      browser: {
        adblock: {
          active: true  // Set to false to disable ad blocking
        }
      }
    });
    
    console.log("Session:", session.data.id);
  })().catch(console.error);
  ```

  ```python python theme={null}
  import os
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  session = anchor_client.sessions.create(
      # Optional: ad blocking is enabled by default, so this configuration is not required
      browser={
          "adblock": {
              "active": True  # Set to False to disable ad blocking
          }
      }
  )

  print("Session:", session.data.id)
  ```
</CodeGroup>

## Disabling Ad Blocker

To disable ad blocking for a session, set `active: false` in the adblock configuration:

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  (async () => {
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    
    const session = await anchorClient.sessions.create({
      browser: {
        adblock: {
          active: false  // Disables ad blocking for this session
        }
      }
    });
    
    console.log("Session:", session.data.id);
  })().catch(console.error);
  ```

  ```python python theme={null}
  import os
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  session = anchor_client.sessions.create(
      browser={
          "adblock": {
              "active": False  # Disables ad blocking for this session
          }
      }
  )

  print("Session:", session.data.id)
  ```
</CodeGroup>

## Related Features

* [Popup Blocker](/advanced/popup-blocker) - Block cookie banners and consent dialogs
* [Captcha Solving](/advanced/captcha-solving) - Solve CAPTCHAs that may appear when ad blocking is detected


# Batch Browser Sessions
Source: https://docs.anchorbrowser.io/advanced/batch-browser-sessions

Create and manage multiple browser sessions simultaneously for large-scale automation tasks

Create up to 5,000 browser sessions in a single API call for large-scale automation, web scraping, and load testing.

## Quick Start

### 1. Create a Batch

```javascript theme={null}
const response = await fetch('https://api.anchorbrowser.io/v1/batch-sessions', {
  method: 'POST',
  headers: {
    'anchor-api-key': process.env.ANCHOR_API_KEY,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    count: 10,
    configuration: {
      browser: {
        headless: { active: true },
        viewport: { width: 1440, height: 900 }
      },
      session: {
        timeout: { idle_timeout: 10, max_duration: 300 }
      }
    },
    metadata: {
      project: 'web-scraping'
    }
  })
});

const batch = await response.json();
const batchId = batch.data.batch_id;
console.log('Batch ID:', batchId);
```

### 2. Monitor Progress

```javascript theme={null}
const response = await fetch(`https://api.anchorbrowser.io/v1/batch-sessions/${batchId}`, {
  headers: { 'anchor-api-key': process.env.ANCHOR_API_KEY }
});

const status = await response.json();
console.log(`Progress: ${status.data.progress.percentage}%`);
console.log(`Completed: ${status.data.completed_requests}/${status.data.total_requests}`);
```

### 3. Use Sessions

```javascript theme={null}
import { chromium } from 'playwright';

const sessions = status.data.sessions.filter(s => s.status === 'completed');

for (const session of sessions) {
  const browser = await chromium.connectOverCDP(session.cdp_url);
  const page = await browser.contexts()[0].newPage();
  
  await page.goto('https://example.com');
  // ... your automation logic
  
  await browser.close();
}
```

## Polling Strategy

```javascript theme={null}
async function waitForBatchCompletion(batchId, maxWaitMinutes = 10) {
  const maxWaitMs = maxWaitMinutes * 60 * 1000;
  let checkInterval = 5000;
  const startTime = Date.now();
  
  while (Date.now() - startTime < maxWaitMs) {
    const response = await fetch(`https://api.anchorbrowser.io/v1/batch-sessions/${batchId}`, {
      headers: { 'anchor-api-key': process.env.ANCHOR_API_KEY }
    });
    
    const data = await response.json();
    
    if (data.data.status === 'completed') return data.data.sessions;
    if (data.data.status === 'failed') throw new Error(`Batch failed: ${data.data.error}`);
    
    await new Promise(resolve => setTimeout(resolve, checkInterval));
    checkInterval = Math.min(checkInterval * 1.5, 30000);
  }
  
  throw new Error(`Batch did not complete within ${maxWaitMinutes} minutes`);
}
```

## Parameters

<ResponseField name="count" type="number">
  Number of browser sessions to create (1-1000)
</ResponseField>

<ResponseField name="configuration" type="object">
  Session configuration that applies to all sessions in the batch
</ResponseField>

<ResponseField name="metadata" type="object">
  Optional key-value pairs for batch identification
</ResponseField>

## Status States

**Batch States**: `pending` → `processing` → `completed` / `failed`

**Session States**: `pending` → `processing` → `completed` / `failed`

## Available Endpoints

* `POST /v1/batch-sessions` - Create batch sessions
* `GET /v1/batch-sessions/{batch_id}` - Get batch status

<Note>
  Additional endpoints for listing, canceling, and retrying batches are planned for future releases.
</Note>

## Limits

* **Maximum batch size**: 1,000 sessions
* **Session lifetime**: Up to 24 hours
* Large batches may take several minutes to provision


# Embedded Browser Live UI
Source: https://docs.anchorbrowser.io/advanced/browser-live-view

Embed interactive browser sessions directly into your application

## Overview

Anchor Browser offers a live view feature that allows you to embed an interactive frame of a website as a web element. The `live_view_url` is received when creating a session.

## Headful Mode (Default)

Headful mode provides a single URL to view the full chrome view, including the address bar. This ensures the presented tab is always the active tab and provides the best user experience.

<img alt="Browser Live View in Headful Mode" />

To create a browser in headful mode, simply [create a session](/sdk-reference/browser-sessions/start-browser-session):

<CodeGroup>
  ```javascript node.js theme={null}
  import  AnchorBrowser from 'anchorbrowser';

  // Initialize the client
  const client = new AnchorBrowser({ apiKey: process.env.ANCHOR_API_KEY });

  // For explicit headfull session configuration (optional, default to false)
  const config = {
    browser: {
      headless: {
        active: false
      }
    }
  };

  const session = await client.sessions.create(config);
  const liveViewUrl = session.data.live_view_url;
  console.log(`Live view URL: ${liveViewUrl}`);
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  # Initialize the client
  client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  # For explicit headfull session configuration (optional, default to False)
  config = {
      "headless": {
        "active": False
      }
  }

  session = client.sessions.create(browser=config)
  print(f"Live view URL: {session.data.live_view_url}")
  ```
</CodeGroup>

Then, use the `live_view_url` from the response to embed the live view directly into an iframe:

```html theme={null}
<iframe 
  src="{{live_view_url}}" 
  sandbox="allow-same-origin allow-scripts" 
  allow="clipboard-read; clipboard-write" 
  style="border: 0px; display: block; width: 100%; height: 100%; position: absolute; top: 0px; left: 0px;">
</iframe>
```

## Advanced Embedding Configuration

### Embed in Fullscreen View (Hide Navigation Bar)

To use the fullscreen view, replace the live view URL with the following:

```html theme={null}
<iframe src="{{live_view_url}}" ...></iframe>
```

### Disable Browser Interactivity

To prevent the end user from interacting with the browser, add the `style="pointer-events: none;"` attribute to the iframe:

```html theme={null}
<iframe 
  src="{{live_view_url}}" 
  sandbox="allow-same-origin allow-scripts" 
  allow="clipboard-read; clipboard-write" 
  style="border: 0px; display: block; width: 100%; height: 100%; position: absolute; top: 0px; left: 0px; pointer-events: none;">
</iframe>
```

<Note>
  This feature is available for both headful and headless modes.
</Note>

## Headless Mode

To obtain the browser live session URL in headless mode, start by [creating a session](/api-reference/browser-sessions/start-browser-session):

<CodeGroup>
  ```javascript node.js theme={null}
  import  AnchorBrowser from 'anchorbrowser';

  // Initialize the client
  const client = new AnchorBrowser({ apiKey: process.env.ANCHOR_API_KEY });

  const config = {
    browser: {
      headless: {
        active: true
      }
    }
  };

  const session = await client.sessions.create(config);
  const liveViewUrl = session.data.live_view_url;
  console.log(`Live view URL: ${liveViewUrl}`);
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  # Initialize the client
  client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  config = {
      "headless": {
        "active": True
      }
  }

  session = client.sessions.create(browser=config)
  print(f"Live view URL: {session.data.live_view_url}")
  ```
</CodeGroup>

<img alt="Browser Live View in Headless Mode" />

<Warning>The live\_view\_url currently points to the browser default first page.</Warning>

Then, use the **create-session** response to embed the live view URL directly into an iframe:

```html theme={null}
<iframe src="{{live_view_url}}" sandbox="allow-same-origin allow-scripts" allow="clipboard-read; clipboard-write" style="border: 0px; display: block; width: 100%; height: 100%; position: absolute; top: 0px; left: 0px;"></iframe>
```


# Captcha Solving
Source: https://docs.anchorbrowser.io/advanced/captcha-solving



### Visual CAPTCHA solving

Anchor browser solves CAPTCHA challenges using a vision-based approach, along with extension-based fallbacks. The vision-based approach imitates human behavior to solve any CAPTCHA (including Cloudflare) without multiple challenges.

<Note> Proxy is required for CAPTCHA solving configuration.</Note>

For the full list of available options, view the [interactive api documentation](/api-reference)

### Enable CAPTCHA solving

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  (async () => {
    const anchorClient = new Anchorbrowser({apiKey: process.env.ANCHOR_API_KEY});
    
    const session = await anchorClient.sessions.create({
      browser: {
        captcha_solver: {
          active: true
        }
      },
      session: {
        proxy: {
          active: true  // Required
        }
      }
    });
    
    console.log("Session created with CAPTCHA solver:", session.data.id);
  })().catch(console.error);
  ```

  ```python python theme={null}
  import os
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  session = anchor_client.sessions.create(
      browser= {
        "captcha_solver": {
          "active": True
        }
      },
      session= {
        "proxy": {
          "active": true  # Required
        }
      }
  )

  print("Session created with CAPTCHA solver:", session.data.id)
  ```
</CodeGroup>

#### Configure Text-based CAPTCHA solving

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  (async () => {
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    
    const session = await anchorClient.sessions.create({
      browser: {
        captcha_solver: {
          active: true,
          image_selector: 'ol_capcha img',
          input_selector: 'ol-captcha input'
        }
      },
      session: {
        proxy: {
          active: true  // Required
        }
      }
    });
    
    console.log("Session created with text-based CAPTCHA solver:", session.data.id);
  })().catch(console.error);
  ```

  ```python python theme={null}
  import os
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  session = anchor_client.sessions.create(
      browser={
          "captcha_solver": {
              "active": True,
              "image_selector": 'ol_capcha img',
              "input_selector": 'ol-captcha input'
          }
      },
      session= {
        "proxy": {
          "active": true  # Required
        }
      }
  )

  print("Session created with text-based CAPTCHA solver:", session.data.id)
  ```
</CodeGroup>


# Cloudflare Web Bot Auth
Source: https://docs.anchorbrowser.io/advanced/cloudflare-web-bot-auth

Authenticate browser sessions with Cloudflare Web Bot Auth

Anchor Browser supports Cloudflare Web Bot Auth HTTP message signing for browser sessions. This allows you to identify as Anchor Browser to websites that require Cloudflare's web bot authentication, enabling access to protected content and avoiding bot detection.

<img alt="WebBotAuth.io Test" />

## How It Works

1. **Session Creation**: Create a browser session with web bot auth enabled
2. **HTTP Message Signing**: All HTTP requests are automatically signed as Anchor Browser
3. **Authentication**: Cloudflare validates the signatures
4. **Access Granted**: Successfully authenticated requests can access protected content

## Using Web Bot Auth

### How Authentication Works

When you enable web bot auth, Anchor Browser automatically identifies all HTTP requests to websites using our registered identity. This allows you to access protected content that requires Cloudflare's web bot authentication without any additional configuration.

### Browser Configuration

```typescript theme={null}
{
  "browser": {
    "web_bot_auth": {
      "active": boolean  // Enable/disable web bot auth (default: false)
    }
  }
}
```

### SDK Examples

Enable web bot auth by setting the `web_bot_auth.active` flag to `true` in your session configuration:

<CodeGroup>
  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  # Initialize the client
  client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  # Session configuration with web bot auth enabled
  config = {
      "web_bot_auth": {
        "active": True
      }
  }

  # Create session with web bot auth
  session = client.sessions.create(browser=config)
  print(f"Session created: {session.data.id}")
  print(f"CDP URL: {session.data.cdp_url}")
  print(f"Live view URL: {session.data.live_view_url}")
  ```

  ```javascript node.js theme={null}
  import  AnchorBrowser from 'anchorbrowser';

  // Initialize the client
  const client = new AnchorBrowser({ apiKey: process.env.ANCHOR_API_KEY });

  // Session configuration with web bot auth enabled
  const config = {
    browser: {
      web_bot_auth: {
        active: true
      }
    }
  };

  // Create session with web bot auth
  const session = await client.sessions.create(config);

  console.log('Session created:', session);
  ```
</CodeGroup>

## Testing

You can test your web bot auth configuration by visiting [https://webbotauth.io/test](https://webbotauth.io/test) in a browser session with web bot auth enabled. This site will show you whether your requests are being properly signed and authenticated.

## Read More

* [Cloudflare Verified Bots Blog](https://blog.cloudflare.com/verified-bots-with-cryptography/)
* [HTTP Message Signatures (RFC 9421)](https://datatracker.ietf.org/doc/html/rfc9421)
* [Web Bot Auth IETF Draft](https://datatracker.ietf.org/doc/html/draft-meunier-web-bot-auth-architecture)
* [WebBotAuth.io](https://webbotauth.io)


# Dedicated Sticky IP
Source: https://docs.anchorbrowser.io/advanced/dedicated-sticky-ip

Reserve a fixed IP address for a specific profile.

A **Dedicated Sticky IP** ensures that a specific profile uses by default the same IP address, reserved exclusively for that profile. This is helpful when IP consistency is required across sessions.

<Steps>
  <Step title="Enable sticky IP in profile creation">
    Use the [Create Profile API](https://docs.anchorbrowser.io/api-reference/profiles/create-profile?playground=open) to create a profile with a dedicated sticky IP by setting:

    ```json theme={null}
    {
      "dedicated_sticky_ip": true
    }
    ```

    This allocates a dedicated IP that is not shared with other profiles.
  </Step>

  <Step title="Start sessions with the reserved IP">
    Any browser session started using this profile will automatically use the reserved sticky IP.
  </Step>

  <Step title="Override the IP with a custom proxy (optional)">
    To override the default sticky IP, set the `proxy` field when using the [Start Browser Session API](https://docs.anchorbrowser.io/api-reference/browser-sessions/start-browser-session).
  </Step>
</Steps>


# Browser Extensions
Source: https://docs.anchorbrowser.io/advanced/extensions

Upload and use custom browser extensions in your sessions

Anchor allows you to upload and use Chrome extensions in your browser sessions. This lets you add ad blockers, privacy tools, or any other extension to enhance your browsing automation.

For uploading, listing, and managing extensions, see the [interactive API documentation](/api-reference/extensions).

## Getting Extensions from Chrome Web Store

To use extensions from the Chrome Web Store, you'll need to download and inspect their files:

### Download Extension Files

1. **Install CRX Extractor/Downloader** - Add this extension to your browser to download .zip files
2. **Navigate to the extension** you want on the Chrome Web Store
3. **Click the CRX Extractor icon** and download the .zip file
4. **Extract the ZIP** to inspect the contents

### Inspect Extension Contents

Once extracted, you'll see the extension's files:

* `manifest.json` - Contains extension metadata and permissions
* `background.js` or `service_worker.js` - Background scripts
* `content_scripts/` - Scripts that run on web pages
* `popup.html` - Extension popup interface
* `icons/` - Extension icons

### Repackage for Upload

After inspecting (and optionally modifying) the files:

1. **Select all files and folders** in the extracted directory
2. **Create a new ZIP file** containing all the extension files
3. **Upload this ZIP** to AnchorBrowser using the SDK

## Extension Requirements

Your extension ZIP file must contain a valid `manifest.json` with basic extension information like name and version.

### Example Manifest

```json theme={null}
{
  "manifest_version": 3,
  "name": "My Extension",
  "version": "1.0.0",
  "description": "Extension description",
  "permissions": ["activeTab", "storage"],
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [{
    "matches": ["<all_urls>"],
    "js": ["content.js"]
  }]
}
```

## Code Example

<CodeGroup>
  ```javascript node.js theme={null}
    import AnchorBrowser from 'anchorbrowser';
    import fs from 'fs';

    const anchor_client = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});

    const extension = await anchor_client.extensions.upload({
      file: fs.createReadStream('./my-extension.zip'),
      name: 'My Custom Extension'
    });
    const extensionId = extension.data.id;
    console.log("ExtensionId:", extensionId);

    const session = await anchor_client.sessions.create({
      browser: {
        extensions: [extensionId]
      }
    });
    console.log("Session:", session);
  ```

  ```python python theme={null}
    from anchorbrowser import Anchorbrowser
    import os

    anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

    with open('./my-extension.zip', 'rb') as file:
      extension = anchor_client.extensions.upload(file=file,name='My Custom Extension')
    extensionId = extension.data.id
    print("ExtensionId:", extensionId)

    session = anchor_client.sessions.create(browser={
        "extensions": [extensionId]
      })
    print("Session:", session)
  ```
</CodeGroup>

## Limitations

* Maximum extension size: 50MB per ZIP file
* Extensions must be valid Chrome extensions


# File Download
Source: https://docs.anchorbrowser.io/advanced/file-download



Anchor Browser supports two methods for downloading files during your browser sessions:

1. **Traditional Downloads**: Files are downloaded to the browser instance and then uploaded to S3 for retrieval

<Note>
  To download PDF files directly instead of viewing them in the browser, set `pdf_viewer` to `false` when creating your session.
</Note>

2. **P2P Downloads**: Files are captured directly in the browser using peer-to-peer technology, bypassing S3 storage

## Traditional File Downloads

The following examples demonstrate how to download a file using the traditional method and retrieve it from the browser session.

<Steps>
  <Step title="Create a browser session">
    Use the [create session](api-reference/browser-sessions/start-browser-session) API to create a new browser session.
    To enable automatic PDF downloads, include the following `browser` configuration:

    <CodeGroup>
      ```tsx node.js theme={null}
      browser: {
          pdf_viewer: {
              active: false
              }
          }
      ```

      ```python python theme={null}
      "browser": {
          "pdf_viewer": {
              "active": False
              }
          }
      ```
    </CodeGroup>
  </Step>

  <Step title="Browse and download a file">
    Use the following example to perform a file download

    <CodeGroup>
      ```tsx node.js theme={null}
      await page.goto("https://browser-tests-alpha.vercel.app/api/download-test");

      await Promise.all([page.waitForEvent("download"), page.locator("#download").click()]); // The download has completed
      ```

      ```python python theme={null}
      await page.goto("https://browser-tests-alpha.vercel.app/api/download-test")

      async with page.expect_download() as download_info:
          await page.locator("#download").click()

      download = await download_info.value
      ```
    </CodeGroup>
  </Step>

  <Step title="Fetch the file from the browser session">
    You can retrieve the downloaded file from the browser session using the [get session downloads](/api-reference/browser-sessions/list-session-downloads) API
  </Step>
</Steps>

## P2P Downloads

For enhanced performance and direct file capture without S3 storage, see our [P2P Download Guide](/advanced/p2p-downloads) which provides complete implementation examples and best practices.


# File Upload
Source: https://docs.anchorbrowser.io/advanced/file-upload



Anchor Browser allows you to upload files during your browser sessions, enabling you to interact with web applications/forms that require files as input.

The following examples demonstrate how to upload a file, either from your local development environment or one downloaded during the browser session.

## Using a local file

### Playwright example

<CodeGroup>
  ```tsx node.js theme={null}
  await page.goto('https://browser-tests-alpha.vercel.app/api/upload-test')

  const input = await page.$("#fileUpload")

  await input.setInputFiles('/tmp/my-files/google.png'); // Reference the local file path
  ```

  ```python python theme={null}
  page.goto('https://browser-tests-alpha.vercel.app/api/upload-test')

  input = page.locator("#fileUpload")

  input.set_input_files('/tmp/my-files/google.png') # Reference the local file path
  ```
</CodeGroup>


# MCP - Hosted Version
Source: https://docs.anchorbrowser.io/advanced/mcp

Use Anchor with Model Context Protocol (MCP) in your preferred agentic tools via our hosted service

<img alt="Model Context Protocol" />

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

      <img alt="Get Cursor MCP Settings" />
    </Step>

    <Step title="Open MCP Configurations">
      Click on "Add Custom MCP" or "New MCP Server" if you already have some pre-configured.

      <img alt="Add Custom MCP Server" />
    </Step>

    <Step title="Add MCP Server">
      Add inside the `mcpServers` object the following:

      ```json theme={null}
      "Anchor Browser Agent": {
          "url": "https://api.anchorbrowser.io/mcp",
          "headers": {
              "anchor-api-key": "YOUR_ANCHOR_API_KEY"
          }
      }
      ```

      <Note>
        If you don't have your Anchor API key yet, you can get it from [Anchor UI](https://app.anchorbrowser.io/api-keys).
      </Note>

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

      ```json theme={null}
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

      ```json theme={null}
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

<img alt="MCP Tools" />

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

  <video alt="Test Generator" />

  <Expandable title="garfield-test.spec.ts File">
    That is the generated test file:

    ```js theme={null}
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

```bash theme={null}
pip install mcp
```

### Basic Example

```python theme={null}
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

```yaml theme={null}
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


# MCP - Open Source
Source: https://docs.anchorbrowser.io/advanced/mcp-open-source

Self-host Anchor MCP server with customizable Playwright integration for your specific needs

# Anchor MCP Server (Open Source)

<img alt="Model Context Protocol" />

A Model Context Protocol (MCP) server that provides browser automation capabilities using [Anchor Browser](https://anchorbrowser.io)'s remote browser service with [Playwright](https://playwright.dev). This server enables LLMs to interact with web pages through Anchor's cloud-based browsers with built-in proxies, stealth features, and advanced capabilities.

This is based on the open source repository at [browsermcp-com/mcp](https://github.com/browsermcp-com/mcp), which extends Microsoft's Playwright MCP with Anchor Browser's cloud infrastructure.

<Note>
  Looking for our hosted MCP service? Check out [MCP - Hosted Version](/advanced/mcp) for zero-setup integration.
</Note>

## When to Use Open Source MCP

Choose the open source version when you need:

* **Custom tool modifications** - Modify browser automation tools for specific use cases
* **Advanced configuration** - Fine-tune browser settings and behaviors
* **Local development** - Test MCP integrations during development
* **Compliance requirements** - Run MCP server within your infrastructure
* **Integration with existing systems** - Connect MCP to your internal tools and workflows

## Key Features

* **Remote Browser Execution**: Uses Anchor Browser's cloud infrastructure instead of local browsers
* **Built-in Proxies**: Automatic residential proxy rotation and geo-targeting
* **Stealth & Anti-Detection**: Advanced browser fingerprinting and anti-bot detection
* **Fast and lightweight**: Uses Playwright's accessibility tree, not pixel-based input
* **LLM-friendly**: No vision models needed, operates purely on structured data
* **Deterministic tool application**: Avoids ambiguity common with screenshot-based approaches
* **Customizable**: Modify and extend tools for your specific needs

## Requirements

* Node.js 18 or newer
* **Anchor Browser API Key** ([Get one here](https://anchorbrowser.io))
* VS Code, Cursor, Windsurf, Claude Desktop, Goose or any other MCP client

## Getting Started

### 1. Clone and Build

Since this is a custom Anchor MCP server, you need to build it locally:

```bash theme={null}
# Clone the repository
git clone https://github.com/browsermcp-com/mcp.git
cd mcp

# Install dependencies and build
npm install
npm run build
```

### 2. Get Your Anchor API Key

1. Sign up at [anchorbrowser.io](https://anchorbrowser.io)
2. Get your API key from the dashboard
3. Copy your API key (starts with `sk-`)

### 3. Configure MCP Client

#### Cursor

Add to your `~/.cursor/mcp.json`:

```json theme={null}
{
  "mcpServers": {
    "anchor-browser": {
      "command": "node",
      "args": [
        "/path/to/mcp/cli.js"
      ],
      "env": {
        "ANCHOR_API_KEY": "sk-your-api-key-here"
      }
    }
  }
}
```

#### VS Code

Add to your MCP configuration:

```json theme={null}
{
  "mcpServers": {
    "anchor-browser": {
      "command": "node",
      "args": [
        "/path/to/mcp/cli.js"
      ],
      "env": {
        "ANCHOR_API_KEY": "sk-your-api-key-here"
      }
    }
  }
}
```

#### Claude Desktop

Add to your `claude_desktop_config.json`:

```json theme={null}
{
  "mcpServers": {
    "anchor-browser": {
      "command": "node",
      "args": [
        "/path/to/mcp/cli.js"
      ],
      "env": {
        "ANCHOR_API_KEY": "sk-your-api-key-here"
      }
    }
  }
}
```

### 4. Restart Your MCP Client

After updating the configuration, restart your MCP client (Cursor, VS Code, etc.) to load the new server.

## Configuration Options

The Anchor MCP server supports essential configuration options:

```bash theme={null}
node cli.js --help
```

### Available Options:

* `--host <host>` - Host to bind server to (default: localhost, use 0.0.0.0 for all interfaces)
* `--port <port>` - Port to listen on for HTTP transport (Docker/server mode)

### Example with Options:

```json theme={null}
{
  "mcpServers": {
    "anchor-browser": {
      "command": "node",
      "args": [
        "/path/to/mcp/cli.js"
      ],
      "env": {
        "ANCHOR_API_KEY": "sk-your-api-key-here"
      }
    }
  }
}
```

## How It Works

1. **Browser Session Creation**: When you use browser tools, the MCP server calls Anchor's API to create a remote browser session
2. **Remote Connection**: Connects to the remote browser via WebSocket using Chrome DevTools Protocol (CDP)
3. **Tool Execution**: All browser automation happens in Anchor's cloud infrastructure
4. **Proxy & Stealth**: Automatic residential proxy rotation and advanced anti-detection features
5. **Session Management**: Each session is isolated and can be viewed live via Anchor's dashboard

## Production & CI/CD Usage

### Self-Hosted in Production

The open source MCP server can be deployed in production environments:

* **Docker Containers** - Run in containerized environments
* **CI/CD Pipelines** - Integrate with Jenkins, GitHub Actions, GitLab CI
* **Serverless Functions** - Deploy as microservices or serverless functions
* **Kubernetes** - Scale horizontally in Kubernetes clusters

### CI/CD Integration Example

```yaml theme={null}
# GitHub Actions with self-hosted MCP
name: E2E Testing
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      anchor-mcp:
        image: your-registry/anchor-mcp:latest
        env:
          ANCHOR_API_KEY: ${{ secrets.ANCHOR_API_KEY }}
        ports:
          - 8931:8931
    steps:
      - uses: actions/checkout@v3
      - name: Run AI tests against MCP server
        run: |
          python ai_test_runner.py --mcp-url http://localhost:8931/mcp
```

## Benefits Over Local Browsers

### 🌐 **Global Proxy Network**

* Automatic residential proxy rotation
* Geo-targeting for different regions
* No proxy configuration needed

### 🛡️ **Advanced Stealth**

* Browser fingerprinting protection
* Anti-bot detection bypass
* Real browser environments

### ☁️ **Cloud Infrastructure**

* No local browser dependencies
* Consistent browser versions
* Scalable execution

### 📊 **Monitoring & Debugging**

* Live view of browser sessions
* Session recordings and traces
* Network request logging


# MFA
Source: https://docs.anchorbrowser.io/advanced/mfa

Real-time event signaling and coordination between external systems and browser instances

# Event Coordination

Event coordination allows you to send real-time messages between external systems and active browser instances. This is particularly useful for **multi-factor authentication (MFA)** where you need to inject authentication codes during browser automation.

## Overview

The system provides two operations:

* **Signal Event**: Send data to an event channel
* **Wait for Event**: Listen for data on an event channel with timeout

Events are user-scoped and work across multiple browser instances.

<Expandable title="API Endpoints">
  ## API Endpoints

  ### Signal an Event

  ```http theme={null}
  POST https://api.anchorbrowser.io/api/v1/events/{eventName}
  ```

  ### Wait for an Event

  ```http theme={null}
  POST https://api.anchorbrowser.io/api/v1/events/{eventName}/wait
  ```

  Both endpoints require `anchor-api-key` header and accept JSON payloads.

  ####
</Expandable>

## MFA Use Case

Handle MFA codes during automated login flows:

```javascript theme={null}
// In your browser automation script
async function handleMFAFlow() {
  await page.fill('#username', 'user@example.com');
  await page.fill('#password', 'password');
  await page.click('#login-button');
  
  // Wait for MFA code from external system
  const mfaEvent = await waitForEvent('mfa_code', 30000);
  
  if (mfaEvent?.data?.code) {
    await page.fill('#mfa-code', mfaEvent.data.code);
    await page.click('#verify-button');
  }
}
```

```javascript theme={null}
// In your external system (mobile app, webhook, etc.)
async function sendMFACode(code) {
  await signalEvent('mfa_code', { code });
}
```

## Implementation

### Helper Functions

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  const anchor_client = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});

  async function signalEvent(eventName, data) {
    try {
      const response = await anchor_client.events.signal(eventName, { data: data || {} });
      return response;
    } catch (error) {
      throw new Error(`Failed to signal event: ${error.message}`);
    }
  }

  async function waitForEvent(eventName, timeoutMs = 60000) {
    try {
      const response = await anchor_client.events.waitFor(eventName, { timeoutMs });
      return response;
    } catch (error) {
      if (error.message.includes("408")) return null; // Timeout
      throw new Error(`Failed to wait for event: ${error.message}`);
    }
  }
  ```

  ```python python theme={null}
  import os
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  def signal_event(event_name, data):
      try:
          response = anchor_client.events.signal(event_name, data=data or {})
          return response
      except Exception as error:
          raise Exception(f"Failed to signal event: {error}")

  def wait_for_event(event_name, timeout_ms=60000):
      try:
          response = anchor_client.events.wait_for(event_name, timeout_ms=timeout_ms)
          return response
      except Exception as error:
          if "408" in str(error):
              return None  # Timeout
          raise Exception(f"Failed to wait for event: {error}")
  ```
</CodeGroup>

## Event Flow Patterns

**Signal First, Wait Later** (immediate consumption):

```javascript theme={null}
await signalEvent("data", { value: "preloaded" });
const data = await waitForEvent("data", 1000); // Short timeout
```

**Wait First, Signal Later** (typical MFA flow):

```javascript theme={null}
const waitPromise = waitForEvent("mfa_code", 60000);
// ... other operations ...
const mfaData = await waitPromise;
```

## Best Practices

* Use descriptive event names: `mfa_code_login`, `mfa_code_transfer`
* Always set appropriate timeouts
* Validate received event data
* Handle timeout scenarios gracefully


# OS-Level Control
Source: https://docs.anchorbrowser.io/advanced/os-level-control

Direct operating system control for precise browser automation and AI agent interactions

# OS-Level Control

OS-level control provides direct access to operating system primitives like mouse movements, keyboard input, and screen interactions within your browser sessions. This approach offers more precise control than traditional web automation methods and is particularly powerful when combined with AI agents and vision-based models.

## Why OS-Level Control?

### Superior AI Agent Performance

**Vision-based AI models perform significantly better** when they can interact with the browser using the same primitives humans use:

* **OS-level UI elements**: Dropdowns, context menus, and system dialogs that aren't part of the webpage DOM.
* **Visual coordinate targeting**: AI agents can directly click on elements they see in screenshots
* **Keyboard shortcuts work naturally**: `Ctrl+F` for searching, `Ctrl+L` for browser navbar interaction, `Ctrl+T` for new tabs

<Expandable title="Key List for Keyboard Shortcuts">
  ## Supported Keys For Keyboard Shortcuts

  |         |            |      |       |            |             |           |   |
  | ------- | ---------- | ---- | ----- | ---------- | ----------- | --------- | - |
  | `A`-`Z` | `Up`       | `F1` | `F7`  | `Control`  | `Enter`     | `Command` |   |
  | `0`-`9` | `Down`     | `F2` | `F8`  | `Ctrl`     | `Return`    | `Cmd`     |   |
  | `Space` | `Left`     | `F3` | `F9`  | `Alt`      | `Backspace` | `Windows` |   |
  | `Home`  | `Right`    | `F4` | `F10` | `Shift`    | `Delete`    | `Win`     |   |
  | `End`   | `PageUp`   | `F5` | `F11` | `CapsLock` | `Escape`    | `Insert`  |   |
  | `Tab`   | `PageDown` | `F6` | `F12` | `NumLock`  | `Esc`       | `Ins`     |   |
</Expandable>

## Core Capabilities - Beyond Traditional Web Automation

Control mouse interactions with pixel-level precision:

### Basic Click

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';
  const anchor_client = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});

  const response = await anchor_client.sessions.mouse.click("Your Session ID", {
  // Single click at coordinates
      x: 100,
      y: 700,
  });
    console.log(response.data.status)
  ```

  ```python python theme={null}
    from anchorbrowser import Anchorbrowser
    import os

    client = Anchorbrowser(
        api_key = os.getenv("ANCHOR_API_KEY")
    )
    response = client.sessions.mouse.click(
        session_id = "Your Session ID",
      # Single click at coordinates
        x = 100,
        y = 700,
    )
    print(response.data['status'])
  ```
</CodeGroup>

### Advanced Mouse Control

<CodeGroup>
  ```javascript node.js theme={null}
    import AnchorBrowser from 'anchorbrowser';
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    const sessionId = "Your Session ID";

    // Double-click for text selection
    await anchorClient.sessions.mouse.doubleClick(sessionId, {
      x: 500, 
      y: 200
    });

    // Mouse down and up for custom gestures
    await anchorClient.sessions.mouse.down(sessionId, {
      x: 100, 
      y: 100, 
    });

    // Move while holding down (drag)
    await anchorClient.sessions.mouse.move(sessionId, {
      x: 300, 
      y: 300
    });

    // Release
    await anchorClient.sessions.mouse.up(sessionId, {
      x: 300, 
      y: 300
    });
  ```

  ```python python theme={null}
    from anchorbrowser import Anchorbrowser
    import os
    anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
    session_id = "Your Session ID"

    # Double-click for text selection
    anchor_client.sessions.mouse.double_click(session_id, x = 500, y = 200)

    # Mouse down and up for custom gestures
    anchor_client.sessions.mouse.down(session_id, x = 100, y = 100)

    # Move while holding down (drag)
    anchor_client.sessions.mouse.move(session_id, x = 300, y = 300)

    # Release
    anchor_client.sessions.mouse.up(session_id, x = 300, y = 300)
  ```
</CodeGroup>

### Drag and Drop

Perform complex drag and drop operations in a single command:

<CodeGroup>
  ```javascript node.js theme={null}
    import AnchorBrowser from 'anchorbrowser';
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    const sessionId = "Your Session ID";

    // Drag and Drop
    await anchorClient.sessions.dragAndDrop(sessionId, {
      startX: 200,
      startY: 150,
      endX: 600,
      endY: 400,
    });
  ```

  ```python python theme={null}
    from anchorbrowser import Anchorbrowser
    import os
    anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
    session_id = "Your Session ID"

    # Drag and Drop
    anchor_client.sessions.drag_and_drop(session_id,
      start_x = 200,
      start_y = 150,
      end_x = 600,
      end_y = 400
      )
  ```
</CodeGroup>

### Keyboard Input

Send text and keyboard shortcuts with human-like timing:

#### Text Input

<CodeGroup>
  ```javascript node.js theme={null}
    import AnchorBrowser from 'anchorbrowser';
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    const sessionId = "Your Session ID";

    // Type text with optional delay between keystrokes
    await anchorClient.sessions.keyboard.type(sessionId, {
      text: "Hello, world!",
      delay: 50 // milliseconds between keystrokes
    });
  ```

  ```python python theme={null}
    from anchorbrowser import Anchorbrowser
    import os
    anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
    session_id = "Your Session ID"

    # Type text with optional delay between keystrokes
    anchor_client.sessions.keyboard.type(session_id,
      text = "Hello, world!",
      delay = 50 # milliseconds between keystrokes
      )
  ```
</CodeGroup>

#### Keyboard Shortcuts

<CodeGroup>
  ```javascript node.js theme={null}
    import AnchorBrowser from 'anchorbrowser';
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    const sessionId = "Your Session ID";

    // Execute keyboard shortcuts
    anchorClient.sessions.keyboard.shortcut(sessionId, {
      keys: ['Ctrl', 'a'], // Select all
      holdTime: 100 // Hold keys for 100ms
    });

  // Common shortcuts
  const shortcuts = {
    selectAll: ['Ctrl', 'a'],
    copy: ['Ctrl', 'c'],
    paste: ['Ctrl', 'v'],
    undo: ['Ctrl', 'z'],
    newTab: ['Ctrl', 't'],
    closeTab: ['Ctrl', 'w'],
    focusAddressBar: ['Ctrl', 'l']
  };
  ```

  ```python python theme={null}
    from anchorbrowser import Anchorbrowser
    import os
    anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
    session_id = "Your Session ID"

    # Execute keyboard shortcuts
    anchor_client.sessions.keyboard.shortcut(session_id,
      keys = ['Ctrl', 'a'],
      hold_time = 100 # Hold keys for 100ms
      )

    # Common shortcuts
    shortcuts = {
      'select_all': ['Ctrl', 'a'],
      'copy': ['Ctrl', 'c'],
      'paste': ['Ctrl', 'v'],
      'undo': ['Ctrl', 'z'],
      'new_tab': ['Ctrl', 't'],
      'close_tab': ['Ctrl', 'w'],
      'focus_address_bar': ['Ctrl', 'l']
    }
  ```
</CodeGroup>

### Scrolling

Control page scrolling with precision:

```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';
  const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
  const sessionId = "Your Session ID";

  // Scroll at specific coordinates
  anchorClient.sessions.scroll(sessionId, {
    x: 400,           // Where to perform scroll (cursor position)
    y: 300,           // Where to perform scroll (cursor position)
    deltaX: 0,        // Horizontal scroll amount (does not correlate with pixels)
    deltaY: 200,      // Vertical scroll amount (does not correlate with pixels, positive = down)
    steps: 5          // Number of steps for smooth scrolling
  });
```

```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os
  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
  session_id = "Your Session ID"

  # Scroll at specific coordinates
  anchor_client.sessions.scroll(session_id,
    x = 400,           # Where to perform scroll (cursor position)
    y = 300,           # Where to perform scroll (cursor position)
    delta_x = 0,        # Horizontal scroll amount (does not correlate with pixels)
    delta_y = 200,      # Vertical scroll amount (does not correlate with pixels, positive = down)
    steps = 5          # Number of steps for smooth scrolling
    )
```

### Screenshots

Capture visual state for AI analysis:

<CodeGroup>
  ```javascript node.js theme={null}
    import AnchorBrowser from 'anchorbrowser';
    import { writeFile } from 'node:fs/promises';
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    const sessionId = "Your Session ID";

    // Take screenshot of current browser state
    const response = await anchorClient.sessions.retrieveScreenshot(sessionId);
    console.log(response);
    const imageBuffer = response.body;

    // Process screenshot with vision AI model (add code below)
    console.log(imageBuffer);

    // Or save screenshot to file
    const ab = await response.arrayBuffer();   // rs is a web ReadableStream
    await writeFile('image.png', Buffer.from(ab));
  ```

  ```python python theme={null}
    from anchorbrowser import Anchorbrowser
    import os
    anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
    session_id = "Your Session ID"

    # Take screenshot of current browser state
    response = anchor_client.sessions.retrieve_screenshot(session_id)
    print(response)

    # Save screenshot to file
    with open("image.png", "wb") as f:
        for chunk in response.iter_bytes(chunk_size=8192):
            f.write(chunk)

    # Process screenshot with vision AI model (add code below)
    print(f"Received {response}")
  ```
</CodeGroup>

### Clipboard Operations

Manage clipboard content programmatically:

#### Reading Clipboard

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';
  const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
  const sessionId = "Your Session ID";

  // Get current clipboard content
  const response = await anchorClient.sessions.clipboard.get(sessionId);
  console.log('Clipboard content:', response.data.text);
  ```

  ```python python theme={null}
    from anchorbrowser import Anchorbrowser
    import os
    anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
    session_id = "Your Session ID"

    # Get current clipboard content
    response = anchor_client.sessions.clipboard.get(session_id)
    print(response)
  ```
</CodeGroup>

#### Setting Clipboard

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';
  const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
  const sessionId = "Your Session ID";

  // Set clipboard content
  await anchorClient.sessions.clipboard.set(sessionId, {
    text: "Content to copy"
  });

  // Trigger copy operation (copies selected text)
  const copyResponse = await anchorClient.sessions.copy(sessionId);

  // Trigger paste operation
  await anchorClient.sessions.paste(sessionId, {
    text: "Text to paste"
  });
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os
  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
  session_id = "Your Session ID"

  # Set clipboard content
  anchor_client.sessions.clipboard.set(session_id, text="Content to copy")

  # Trigger copy operation (copies selected text)
  copy_response = anchor_client.sessions.copy(session_id)

  # Trigger paste operation
  anchor_client.sessions.paste(session_id, text="Text to paste")
  ```
</CodeGroup>

### Navigation

Direct URL navigation at the OS level on the currently selected tab:

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';
  const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
  const sessionId = "Your Session ID";

  // Navigate to a specific URL (completely OS-level, operates on selected tab)
  const response = await anchorClient.sessions.goto(sessionId, {
    url: "https://example.com"
  });
  console.log("Navigation response:", response);
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os
  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
  session_id = "Your Session ID"

  # Navigate to a specific URL (completely OS-level, operates on selected tab)
  response = anchor_client.sessions.goto(session_id, url="https://example.com")
  print("Navigation response:", response)
  ```
</CodeGroup>

## AI Agent Integration Patterns

### OpenAI Computer Use Integration

Anchor includes an integrated **OpenAI Computer Use agent** that leverages OS-level control for enhanced AI interactions. This agent can perform complex tasks by combining vision models with precise OS-level operations.

```python python theme={null}
class AnchorBrowser(BasePlaywrightComputer):
    """
    Computer implementation for Anchor browser (https://anchorbrowser.io)
    Uses OS-level control endpoints for browser automation within the container.

    IMPORTANT: The `goto` and navigation tools are already implemented and recommended
    when using the Anchor computer to help the agent navigate more effectively.
    """

    def __init__(self, width: int = 1024, height: int = 900, session_id: str = None):
        """Initialize the Anchor browser session"""
        super().__init__()
        self.dimensions = (width, height)
        self.session_id = session_id
        self.base_url = "http://localhost:8484/api/os-control"

    def screenshot(self) -> str:
        """
        Capture a screenshot using OS-level control API.
        
        Returns:
            str: A base64 encoded string of the screenshot for AI model consumption.
        """
        try:
            response = requests.get(f"{self.base_url}/screenshot")
            
            if not response.ok:
                print(f"OS-level screenshot failed, falling back to standard screenshot")
                return super().screenshot()
                
            # OS-level API returns binary PNG data, encoded for AI models
            return base64.b64encode(response.content).decode('utf-8')
            
        except Exception as error:
            print(f"OS-level screenshot failed, falling back: {error}")
            return super().screenshot()

    def click(self, x: int, y: int, button: str = "left") -> None:
        """
        Click at the specified coordinates using OS-level control.
        
        Args:
            x: The x-coordinate to click.
            y: The y-coordinate to click.
            button: The mouse button to use ('left', 'right').
        """
        try:
            response = requests.post(
                f"{self.base_url}/mouse/click",
                json={"x": x, "y": y, "button": button}
            )
            
            if not response.ok:
                print(f"OS-level click failed, falling back to standard click")
                super().click(x, y, button)
                
        except Exception as error:
            print(f"OS-level click failed, falling back: {error}")
            super().click(x, y, button)

    def type(self, text: str) -> None:
        """
        Type text using OS-level control with realistic delays.
        """
        try:
            response = requests.post(
                f"{self.base_url}/keyboard/type",
                json={"text": text, "delay": 30}
            )
            
            if not response.ok:
                print(f"OS-level type failed, falling back to standard type")
                super().type(text)
                
        except Exception as error:
            print(f"OS-level type failed, falling back: {error}")
            super().type(text)

    def keypress(self, keys: List[str]) -> None:
        """
        Press keyboard shortcut using OS-level control.
        
        Args:
            keys: List of keys to press simultaneously (e.g., ['Ctrl', 'c']).
        """
        try:
            response = requests.post(
                f"{self.base_url}/keyboard/shortcut",
                json={"keys": keys, "holdTime": 100}
            )
            
            if not response.ok:
                print(f"OS-level keyboard shortcut failed, falling back")
                # Fallback to standard implementation
                for key in keys:
                    self._page.keyboard.down(key)
                for key in reversed(keys):
                    self._page.keyboard.up(key)
                
        except Exception as error:
            print(f"OS-level keyboard shortcut failed: {error}")
```

### Usage with OpenAI Models

The integrated computer use agent works seamlessly with OpenAI's vision models:

```python theme={null}
# Initialize the agent with your session
agent = AnchorBrowser(width=1440, height=900, session_id="your-session-id")

# The agent can now:
# 1. Take screenshots for AI analysis
screenshot = agent.screenshot()

# 2. Perform precise clicks based on AI vision
agent.click(x=400, y=300)

# 3. Type text naturally
agent.type("Hello from AI agent!")

# 4. Execute keyboard shortcuts
agent.keypress(['Ctrl', 'l'])  # Focus address bar
agent.keypress(['Ctrl', 'f'])  # Open search
```

The computer use integration provides **automatic fallbacks** to standard browser automation if OS-level operations aren't available, ensuring reliability across different environments.

## Limitations and Considerations

### Session Requirements

* **Headful Sessions Only**: OS-level control requires a visible desktop environment
* **Performance Impact**: Screenshots and precise positioning may be slower than DOM-based automation

***

OS-level control opens up powerful possibilities for AI-driven browser automation, enabling more natural and effective interactions that mirror human behavior while providing the precision needed for reliable automation workflows.


# P2P Download
Source: https://docs.anchorbrowser.io/advanced/p2p-downloads

Capture files directly in the browser without cloud storage

## What is P2P Download?

P2P (Peer-to-Peer) downloads capture files directly in the browser memory without ever uploading them to cloud storage. When a user downloads a file in your browser session, instead of the file going to Anchor's servers, it's intercepted and made available to you immediately through browser hooks.

## How It Works

Traditional downloads follow this path:

* User clicks download → File goes to browser → File uploads to Anchor's servers → You fetch from Anchor's servers

P2P downloads work differently:

* User clicks download → File captured in browser memory → You fetch from the browser

The browser intercept download events, allowing you to extract the file data directly without any cloud storage involved.

## Implementation Example

<CodeGroup>
  ```tsx node.js theme={null}
  import { promises as fs, existsSync } from "node:fs";
  import { chromium } from "playwright";
  import AnchorBrowser from 'anchorbrowser';

  const { ANCHOR_API_KEY } = process.env;

  /**
   * Save a download to disk.
   * Handles three possible formats:
   *   1. Playwright Download object
   *   2. Base‑64 string
   *   3. Fallback text scraped from the page
   */
  async function saveDownload(download, filePath, page) {
    // 1. Playwright Download object
    if (download && typeof download.path === "function") {
      try {
        const tmpPath = await download.path();
        if (tmpPath && existsSync(tmpPath)) {
          await download.saveAs(filePath);
          return filePath;
        }
      } catch {
        /* ignore and fall through */
      }
    }

    // 2. Raw base64 string
    if (typeof download === "string") {
      try {
        await fs.writeFile(filePath, Buffer.from(download, "base64"));
        return filePath;
      } catch {
        /* ignore and fall through */
      }
    }

    // 3. Fallback – ask the page for data or capture visible text
    if (page) {
      try {
        const blob = await page.evaluate(() => window._anchorExtractDownloadData());
        return saveDownload(blob, filePath);
      } catch {
        /* ignore and fall through */
      }

      const fallbackText = await page.evaluate(() => {
        const el = document.querySelector("main") || document.body;
        return el.innerText || "";
      });
      await fs.writeFile(filePath, fallbackText, "utf8");
      return filePath;
    }
    throw new Error("Failed to save download");
  }

  const downloadHandler = (filePath) => async (page, info) => {
    if (info?.value) {
      try {
        return await saveDownload(info.value, filePath);
      } catch {
        /* ignore and fall through */
      }
    }
    return saveDownload(null, filePath, page);
  };

  async function createSession() {
    const anchor_client = new AnchorBrowser({apiKey: ANCHOR_API_KEY});
    const session = await anchor_client.sessions.create({
      browser: { p2p_download: { active: true } }
    });
    return session.data;
  }

  (async () => {
    const session = await createSession();
    if (!session?.cdp_url) throw new Error("No CDP URL in session");

    const browser = await chromium.connectOverCDP(session.cdp_url);
    const context = browser.contexts()[0];
    const page = context.pages()[0];

    await page.goto("https://v0-download-and-upload-text.vercel.app/");
    await page.waitForSelector("button");

    const [download] = await Promise.all([
      page.waitForEvent("download", { timeout: 5000 }),
      page.click("button"),
      page.waitForTimeout(500), // allow JS to finish
    ]);

    const filename = download.suggestedFilename();
    await downloadHandler(filename)(page, { value: download });

    const content = await fs.readFile(filename, "utf8");
    console.log(`Downloaded '${filename}', content:\n${content}`);

    await browser.close();
  })();

  ```

  ```python python theme={null}
  import os, base64, json
  from playwright.sync_api import sync_playwright
  from anchorbrowser import Anchorbrowser

  ANCHOR_API_KEY = os.getenv("ANCHOR_API_KEY")

  def save_download(src, path, page=None):
      """Persist a Playwright Download object or base‑64 string to *path*.
      Falls back to blob extraction or page text when needed.
      """
      if hasattr(src, "path"):
          try:
              tmp = src.path()
              if tmp and os.path.exists(tmp):
                  src.save_as(path)
                  return path
          except Exception:
              pass

      if isinstance(src, str):
          try:
              with open(path, "wb") as f:
                  f.write(base64.b64decode(src))
              return path
          except Exception:
              pass

      if page:
          try:
              blob = page.evaluate("() => window._anchorExtractDownloadData()")
              return save_download(blob, path)
          except Exception:
              # As a last resort, dump visible page text
              text = page.evaluate(
                  "() => (document.querySelector('main')||document.body).innerText"
              )
              with open(path, "w") as f:
                  f.write(text)
              return path

      raise RuntimeError("Failed to save download")

  def download_handler(path):
      """Return a function (page, download_info) that writes to *path*."""
      def _handle(page, info=None):
          if info and hasattr(info, "value"):
              try:
                  return save_download(info.value, path)
              except Exception:
                  pass
          # Fallback to blob extraction
          return save_download(None, path, page)
      return _handle

  def create_session():
      anchor_client = Anchorbrowser(api_key=ANCHOR_API_KEY)
      session = anchor_client.sessions.create({
          "browser": {
              "p2p_download": {
                  "active": True
              }
          }
      })
      return session.data

  with sync_playwright() as p:
      session = create_session()
      if not session or "cdp_url" not in session:
          print("Could not obtain a valid browser session – exiting.")
          raise SystemExit(1)

      browser = p.chromium.connect_over_cdp(session["cdp_url"])
      page = browser.contexts[0].pages[0]

      page.goto("https://v0-download-and-upload-text.vercel.app/")
      page.wait_for_selector("button", state="visible")

      with page.expect_download(timeout=5000) as dl:
          page.click("button")
          page.wait_for_timeout(500)  # allow JS to finish

      filename = dl.value.suggested_filename
      handler = download_handler(filename)
      handler(page, dl)

      with open(filename) as f:
          snippet = f.read()
      print(f"Downloaded '{filename}', content:\n{snippet}")
  ```
</CodeGroup>


# Popup Blocker
Source: https://docs.anchorbrowser.io/advanced/popup-blocker

Block cookie banners and consent dialogs in your browser sessions

Popup blocking is enabled by default in Anchor Browser. It blocks cookie banners and consent dialogs to create cleaner automation experiences.

<Note>
  Popup blocking is enabled by default. Disable it only if you need to test popup-related functionality.
</Note>

## Quick Start

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  (async () => {
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    
    const session = await anchorClient.sessions.create({
      // Optional: Enabled by default (both), so this configuration is not required
      browser: {
        adblock: {
          active: true  // Required for popup blocking
        },
        popup_blocker: {
          active: true  // Blocks cookie banners and consent dialogs
        }
      }
    });
    
    console.log("Session:", session.data.id);
  })().catch(console.error);
  ```

  ```python python theme={null}
  import os
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  session = anchor_client.sessions.create(
      # Optional: Enabled by default (both), so this configuration is not required
      browser={
          "adblock": {
              "active": True  # Required for popup blocking
          },
          "popup_blocker": {
              "active": True  # Blocks cookie banners and consent dialogs
          }
      }
  )

  print("Session:", session.data.id)
  ```
</CodeGroup>

<Warning>
  Popup blocking requires ad blocking to be active. Disabling ad blocking will result an error.
</Warning>

## Disabling Popup Blocker

To disable popup blocking for a session, set `active: false` in the popup\_blocker configuration:

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  (async () => {
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    
    const session = await anchorClient.sessions.create({
      browser: {
        // Optional: ad blocking is enabled by default, so this configuration is not required
        adblock: {
          active: true  // Ad blocking must remain active
        },
        // Required to disable popup_blocker
        popup_blocker: {
          active: false  // Disables popup blocking for this session
        }
      }
    });
    
    console.log("Session:", session.data.id);
  })().catch(console.error);
  ```

  ```python python theme={null}
  import os
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  session = anchor_client.sessions.create(
      browser={
          # Optional: ad blocking is enabled by default, so this configuration is not required
          "adblock": {
              "active": True  # Ad blocking must remain active
          },
          # Required to disable popup_blocker
          "popup_blocker": {
              "active": False  # Disables popup blocking for this session
          }
      }
  )

  print("Session:", session.data.id)
  ```
</CodeGroup>

## Related Features

* [Ad Blocker](/advanced/adblocker) - Block ads, trackers, and malicious content (required for popup blocking)
* [Captcha Solving](/advanced/captcha-solving) - Solve CAPTCHAs that may appear when ad blocking is detected


# Proxy
Source: https://docs.anchorbrowser.io/advanced/proxy



Anchor provides proxy configurations to access websites from different geographic locations, configurable down to the **city level.** Use custom proxies or Anchor's built-in proxy for localization.

<Warning>
  Anchor Browser infrastructure is fully hosted in the US. For GDPR compliance, upgrade to the [Growth tier](https://app.anchorbrowser.io/billing) or [contact support](https://mail.google.com/mail/?view=cm\&fs=1\&to=support@anchorbrowser.io\&su=Full%20GDPR%20Compatibility%20Request).
</Warning>

#### Quick Start Example

Here's a simple example of how to use Anchor's built-in proxy:

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  const anchor_client = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});

  const session = await anchor_client.sessions.create({
      session: {
        proxy: {
          active: true,
          country_code: 'gb',
        }
      }
  });

  console.log("Session created:", session.data);
  ```

  ```python python theme={null}
  import os
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  session = anchor_client.sessions.create(
    session={
      'proxy': {
          'active': True,
          'country_code': 'gb',
      }
    }
  )
  print("Session created:", session.data)
  ```
</CodeGroup>

This creates a browser session using Anchor's US proxy. You can change `country_code` to any supported country (e.g., 'gb', 'de', 'jp').

To experiment with different proxy configurations, visit our [Interactive API Reference](/api-reference/browser-sessions/start-browser-session)

## Custom Proxy

Anchor Browser allows you to use your own proxy servers, giving you complete control over your proxy infrastructure. This is particularly useful when you have existing proxy solutions or need to comply with specific network policies.

### Custom Proxy Configuration

To use a custom proxy, you need to provide the following information:

* **`active`**: Set to `true` to enable the proxy
* **`type`**: Set to `"custom"` to indicate you're using your own proxy
* **`server`**: The hostname or IP address of your proxy server, appended by the port (SERVER:PORT)
* **`username`**: Your proxy authentication username (if required)
* **`password`**: Your proxy authentication password (if required)

### Supported Proxy Protocols

Anchor Browser supports the following proxy protocols:

* **HTTP Proxy**: Standard HTTP proxy with optional authentication
* **HTTPS Proxy**: Secure HTTPS proxy connections
* **SOCKS5 Proxy**: SOCKS5 proxy for enhanced privacy and flexibility

### Example Configurations

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});

  const response = await anchorClient.sessions.create({
    session: {
      proxy: {
        active: true
        type: 'custom',
        server: 'proxy.example.com:port',
        username: 'myUser',
        password: 'myPassword',
      }
    }
  });
    
  console.log('Session created:', response.data);
  ```

  ```python python theme={null}
  import os
  import json
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv('ANCHOR_API_KEY'))

  response = anchor_client.sessions.create(
    session={
      'proxy': {
          'active': True
          'type': 'custom',
          'server': 'proxy.example.com:port',
          'username': 'myUser',
          'password': 'myPassword',
      }
    }
  )

  print('Session created:')
  print(response.data)
  ```
</CodeGroup>

## Localization

You can specify a country code for your proxy to route traffic through a specific geographic location. This is useful for accessing region-specific content or testing localized experiences.

The `country_code` parameter accepts country codes in lowercase. See the [complete list of supported countries](#supported-countries-with-their-country-codes) below for all available options.

### Region and City-Based Targeting

For even more precise geographic targeting, you can specify both `region` and `city` parameters. This is only supported for the default proxy type (`anchor_proxy`).

**Important Notes:**

* The `city` parameter can only be used when `region` is also provided
* If you specify a city without a region, the city parameter will be ignored
* City names: use English, case-insensitive. Both "Los Angeles" and "los-angeles" work.

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});

  const response = await anchorClient.sessions.create({
    session: {
      proxy: {
        active: true,
        country_code: 'us',
        region: 'ca',
        city: 'los-angeles'
      }
    }
  });
    
  console.log('Session created:', response.data);
  ```

  ```python python theme={null}
  import os
  import json
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv('ANCHOR_API_KEY'))

  response = anchor_client.sessions.create(
      session={
          'proxy': {
              'active': True,
              'country_code': 'us',
              'region': 'ca',
              'city': 'los-angeles'
          }
      }
  )

  print('Session created:')
  print(response.data)
  ```
</CodeGroup>

### Supported Countries with their Country Codes

<Tabs>
  <Tab title="Anchor Proxy">
    |                        |    |                  |    |                          |    |
    | ---------------------- | -- | ---------------- | -- | ------------------------ | -- |
    | Afghanistan            | af | France           | fr | Netherlands              | nl |
    | Albania                | al | French Guiana    | gf | New Zealand              | nz |
    | Algeria                | dz | French Polynesia | pf | Nicaragua                | ni |
    | Andorra                | ad | Gabon            | ga | Nigeria                  | ng |
    | Angola                 | ao | Gambia           | gm | Norway                   | no |
    | American Samoa         | as | Georgia          | ge | Pakistan                 | pk |
    | Antigua and Barbuda    | ag | Germany          | de | Panama                   | pa |
    | Argentina              | ar | Ghana            | gh | Paraguay                 | py |
    | Armenia                | am | Gibraltar        | gi | Peru                     | pe |
    | Aruba                  | aw | Greece           | gr | Philippines              | ph |
    | Australia              | au | Grenada          | gd | Poland                   | pl |
    | Austria                | at | Guadeloupe       | gp | Portugal                 | pt |
    | Azerbaijan             | az | Guatemala        | gt | Puerto Rico              | pr |
    | Bahamas                | bs | Guernsey         | gg | Qatar                    | qa |
    | Bahrain                | bh | Guinea           | gn | Romania                  | ro |
    | Barbados               | bb | Guinea-Bissau    | gw | Saint Lucia              | lc |
    | Belarus                | by | Guyana           | gy | San Marino               | sm |
    | Belgium                | be | Haiti            | ht | Saudi Arabia             | sa |
    | Belize                 | bz | Honduras         | hn | Senegal                  | sn |
    | Benin                  | bj | Hungary          | hu | Serbia                   | rs |
    | Bermuda                | bm | Iceland          | is | Seychelles               | sc |
    | Bolivia                | bo | India            | in | Sierra Leone             | sl |
    | Bosnia and Herzegovina | ba | Iran             | ir | Slovakia                 | sk |
    | Brazil                 | br | Iraq             | iq | Slovenia                 | si |
    | Bulgaria               | bg | Ireland          | ie | Somalia                  | so |
    | Burkina Faso           | bf | Israel           | il | South Africa             | za |
    | Cameroon               | cm | Italy            | it | South Korea              | kr |
    | Canada                 | ca | Jamaica          | jm | Spain                    | es |
    | Cape Verde             | cv | Japan            | jp | Suriname                 | sr |
    | Chad                   | td | Jordan           | jo | Sweden                   | se |
    | Chile                  | cl | Kazakhstan       | kz | Switzerland              | ch |
    | Colombia               | co | Kuwait           | kw | Syria                    | sy |
    | Congo                  | cg | Kyrgyzstan       | kg | São Tomé and Príncipe    | st |
    | Costa Rica             | cr | Latvia           | lv | Taiwan                   | tw |
    | Côte d’Ivoire          | ci | Lebanon          | lb | Tajikistan               | tj |
    | Croatia                | hr | Libya            | ly | Togo                     | tg |
    | Cuba                   | cu | Liechtenstein    | li | Trinidad and Tobago      | tt |
    | Cyprus                 | cy | Lithuania        | lt | Tunisia                  | tn |
    | Czech Republic         | cz | Luxembourg       | lu | Turkey                   | tr |
    | Denmark                | dk | Macedonia        | mk | Turks and Caicos Islands | tc |
    | Dominica               | dm | Mali             | ml | Ukraine                  | ua |
    | Dominican Republic     | do | Malta            | mt | United Arab Emirates     | ae |
    | Ecuador                | ec | Martinique       | mq | United Kingdom           | gb |
    | Egypt                  | eg | Mauritania       | mr | United States            | us |
    | El Salvador            | sv | Mexico           | mx | Uruguay                  | uy |
    | Estonia                | ee | Moldova          | md | Uzbekistan               | uz |
    | Ethiopia               | et | Monaco           | mc | Venezuela                | ve |
    | Faroe Islands          | fo | Montenegro       | me | Yemen                    | ye |
    | Finland                | fi | Morocco          | ma |                          |    |
  </Tab>
</Tabs>


# Session Timeout
Source: https://docs.anchorbrowser.io/advanced/session-timeout



### Managing Browser Session Lifetime

Anchor provides multiple ways to control and terminate browser sessions. In addition to manually stopping sessions via the [stop session API](/api-reference/browser-sessions/end-browser-session), you can configure two types of automatic timeout mechanisms to manage session lifetime effectively.

For the full list of available options, view the [interactive api documentation](/api-reference/browser-sessions).

### Timeout Configuration Options

The API offers two distinct timeout parameters through the `session.timeout` object to automatically manage browser session termination.

#### Idle Timeout

The `idle_timeout` parameter automatically terminates sessions after a period of inactivity. This timer starts after the last connection to the browser has disconnected, and any new connection will restart the timer. This includes live view sessions, CDP (Chrome DevTools Protocol) connections, and OS-level control connections.

The idle timeout is particularly useful for sessions with unknown length, allowing users to interact with browsers for as long as they need without keeping stale browsers alive unnecessarily. When set to `3` minutes for example, the session will terminate after 3 minutes with no active connections. The default value is `5` minutes, and you can disable automatic termination for idle sessions by setting it to `-1`.

#### Maximum Duration

The `max_duration` parameter sets a hard limit on total session lifetime. Unlike the idle timeout, this will automatically terminate the session after the specified duration regardless of activity level. This acts as a safety mechanism to ensure sessions don't run indefinitely.

The default maximum duration is `180` minutes (3 hours), but you can adjust this based on your needs. Setting `max_duration` to `10` will terminate the session after exactly 10 minutes, whether the browser is actively being used or not. There is no upper limit on how long you can set the maximum duration.

### Implementation Example

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';

  (async () => {
    const anchor_client = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    
    const session = await anchor_client.sessions.create({
      session: {
        timeout: {
          max_duration: 10,  // 10 minutes hard limit
          idle_timeout: 3    // 3 minutes of inactivity
        }
      }
    });
    
    console.log("Session created with timeout configuration:", session.data.id);
  })().catch(console.error);
  ```

  ```python python theme={null}
  import os
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  session = anchor_client.sessions.create(
      session={
          "timeout": {
              "max_duration": 10,  # 10 minutes hard limit
              "idle_timeout": 3    # 3 minutes of inactivity
          }
      }
  )

  print("Session created with timeout configuration:", session.data.id)
  ```
</CodeGroup>

In this example, replace `"your_api_key_here"` with your actual API key. The configuration sets a 10-minute hard session limit with `max_duration`, while `idle_timeout` ensures the session terminates after 3 minutes of no active connections. These two timeout mechanisms work independently, so the session will end when whichever condition is met first.


# Automation Tasks
Source: https://docs.anchorbrowser.io/advanced/tasks

Create, manage, and execute reusable browser automation tasks

## Overview

The Tasks API enables you to **create, version, and execute reusable browser automation code** in your Anchor Browser sessions. Tasks allow you to:

<img alt="Tasks dashboard showing task management interface" />

<Note>
  Tasks are executed in a secure sandbox environment and can access the full Anchor Browser API for automation capabilities.
</Note>

## Creating Your First Task

## Writing Task Code

For reliable execution, **follow these guidelines:**

* Write your **code in TypeScript.**
* **Export** a single **default async function.**
* In that function, **return** whatever your workflow requires as **output** (e.g., status, messages, domain data).

<Note>
  Tasks can receive values as inputs. **All input names must be prefixed with `ANCHOR_`**
</Note>

### Basic Task Example

<CodeGroup>
  ```typescript typescript theme={null}
  import AnchorClient from 'anchorbrowser';

  // Initialize the Anchor client with your API key
  const anchorClient = new AnchorClient({
      apiKey: process.env.ANCHOR_API_KEY,
  });

  // Export the main function as the default export
  export default async function run() {

      // Create a new browser instance
      const browser = await anchorClient.browser.create();
      const page = browser.contexts()[0].pages()[0];

      // Access input values
      const targetUrl = process.env.ANCHOR_TARGET_URL;
      const maxPages = parseInt(process.env.ANCHOR_MAX_PAGES || '10');

      // Implement your automation logic
      await page.goto(targetUrl);
      console.log(`Scraping up to ${maxPages} pages from ${targetUrl}`);

      // Always close the browser when done
      await browser.close();

      // Return a result object with success status and message
      return {
          success: true,
          message: 'Task completed successfully'
      };
  }
  ```
</CodeGroup>

### Using the SDK

Create your task in Anchor:

<Steps>
  <Step title="Save your typescript code as a .ts file">
    <Warning>
      Make sure it follows the guidelines from above.
    </Warning>
  </Step>

  <Step title="Get the base64 version of the file">
    Run the script to show your base64 file version

    ```bash terminal theme={null}
    # Convert your TypeScript file to base64
    base64 -i your-task.ts
    ```

    Copy the output for later.
  </Step>

  <Step title="Create your Task in Anchor">
    <CodeGroup>
      ```typescript node.js theme={null}
      import Anchorbrowser from 'anchorbrowser';

      const client = new Anchorbrowser({
        apiKey: process.env.ANCHORBROWSER_API_KEY,
      });

      // Create a new task
      const task = await client.task.create({
        name: 'example-task',
        language: 'typescript',
        description: 'A task to scrape product information from e-commerce sites',
        code: "<base64-string>" // Replace with the output of the last step.
      });

      const taskId = task.data.id
      console.log('Task created:', taskId);
      ```

      ```python python theme={null}
      import os
      from anchorbrowser import Anchorbrowser

      client = Anchorbrowser(
          api_key=os.environ.get("ANCHORBROWSER_API_KEY")
      )

      # Create a new task
      task = client.task.create(
          name="example-task",
          language="typescript",
          description="A task to scrape product information from e-commerce sites",
          code="<base64-string>" # Replace with the output of the last step.
      )

      # Save the id for later
      task_id = task.data.id
      print(f"Task created: {task_id}")
      ```
    </CodeGroup>
  </Step>

  <Step title="Running Tasks">
    <CodeGroup>
      ```typescript node.js theme={null}
      // Run the task with inputs
      const execution = await client.task.run({
        taskId: taskId,
        version: 'draft',
        inputs: {
          ANCHOR_TARGET_URL: 'https://example.com',
          ANCHOR_MAX_PAGES: '10'
        }
      });

      console.log('Task execution started:', execution.data);
      ```

      ```python python theme={null}
      # Run the task with inputs
      execution = client.task.run(
          task_id=task_id,
          version="draft",
          inputs={
              "ANCHOR_TARGET_URL": "https://example.com",
              "ANCHOR_MAX_PAGES": "10"
          }
      )

      print(f"Task execution started: {execution.data}")
      ```
    </CodeGroup>

    <Note>
      By default, the browser session is automatically closed when the task ends. Set `cleanupSessions: false` to keep the session open after task execution.
    </Note>

    <img alt="Running a task with inputs" />
  </Step>

  <Step title="Deploy Task">
    <CodeGroup>
      ```typescript node.js theme={null}
      // Deploy the task to make it available for production use
      const deployment = await client.task.deploy({
        taskId: taskId,
        code: "<base64-string>", // Replace with the base64 encoded code
        language: 'typescript',
        description: 'Optional description for this version'
      });

      console.log('Task deployed:', deployment.data);
      ```

      ```python python theme={null}
      # Deploy the task to make it available for production use
      deployment = client.task.deploy(
          task_id=task_id,
          code="<base64-string>",  # Replace with the base64 encoded code
          language="typescript",
          description="Optional description for this version"
      )

      print(f"Task deployed: {deployment.data}")
      ```
    </CodeGroup>
  </Step>
</Steps>

## Async Task

By default, task execution is **synchronous** - the API call waits for the task to complete before returning results. For long-running tasks, you can use **asynchronous execution** to start the task and check results later.

### Running Tasks Asynchronously

When you set `async: true`, the API returns immediately with a confirmation that the task has started. You can then poll for execution results using the task execution history endpoint.

<CodeGroup>
  ```typescript node.js theme={null}
  // Run the task asynchronously
  const execution = await client.task.run({
    taskId: taskId,
    version: '1',
    async: true, // Enable async execution
    inputs: {
      ANCHOR_TARGET_URL: 'https://example.com',
      ANCHOR_MAX_PAGES: '10'
    }
  });

  console.log('Task execution started:', execution.data);
  // Response: { async: true, success: true, message: 'Task execution started', taskId: '...' }
  ```

  ```python python theme={null}
  # Run the task asynchronously
  execution = client.task.run(
      task_id=task_id,
      version="1",
      async_=True,  # Enable async execution
      inputs={
          "ANCHOR_TARGET_URL": "https://example.com",
          "ANCHOR_MAX_PAGES": "10"
      }
  )

  print(f"Task execution started: {execution.data}")
  # Response: {'async': True, 'success': True, 'message': 'Task execution started', 'taskId': '...'}
  ```
</CodeGroup>

### Checking Execution Results

After starting an async task, you can check its execution status and results by querying the task's execution history endpoint:

<CodeGroup>
  ```typescript node.js theme={null}
  // Get execution results
  const response = await fetch(`https://api.anchorbrowser.io/v1/task/${taskId}/executions?page=1&limit=1&version=1`, {
    headers: {
      'anchor-api-key': process.env.ANCHORBROWSER_API_KEY,
      'Content-Type': 'application/json'
    }
  });

  const results = await response.json();
  console.log('Execution results:', results.data);
  ```

  ```python python theme={null}
  import os
  import requests

  # Get execution results
  response = requests.get(
      f"https://api.anchorbrowser.io/v1/task/{task_id}/executions",
      params={
    #     "status": "success",  #Optional: filter by status (success, failure, timeout, cancelled)
          "page": 1,
          "limit": 1,
          "version": "1"    # Optional: filter by version
      },
      headers={
          "anchor-api-key": os.environ.get("ANCHORBROWSER_API_KEY"),
          "Content-Type": "application/json"
      }
  )

  results = response.json()
  print(f"Execution results: {results['data']}")
  ```
</CodeGroup>

**Example response:**

```json theme={null}
{
  "data": {
    "results": [
      {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "status": "success",
        "executionTime": 5234,
        "output": "{\"success\": true, \"message\": \"Task completed successfully\"}",
        "errorMessage": null,
        "startTime": "2024-01-15T10:30:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 1,
      "total": 1,
      "totalPages": 1
    }
  }
}
```

<Warning>
  Async task executions have a maximum duration of **3 hours**. Tasks that exceed this limit will be automatically cancelled.

  **Note:** Tasks must be deployed (not just in draft) to appear in the execution results list.
</Warning>

### Polling for Results

For async tasks, you can implement polling to wait for completion:

<CodeGroup>
  ```typescript node.js theme={null}
  // Poll for task completion
  async function waitForTaskCompletion(taskId: string, maxAttempts: number = 60) {
    for (let i = 0; i < maxAttempts; i++) {
      const response = await fetch(`https://api.anchorbrowser.io/v1/task/${taskId}/executions?page=1&limit=1`, {
        headers: {
          'anchor-api-key': process.env.ANCHORBROWSER_API_KEY,
          'Content-Type': 'application/json'
        }
      });
      
      const results = await response.json();
      const latestResult = results.data?.results?.[0];
      if (latestResult) {
        if (latestResult.status === 'success' || latestResult.status === 'failure') {
          return latestResult;
        }
      }
      
      // Wait 2 seconds before next poll
      await new Promise(resolve => setTimeout(resolve, 2000));
    }
    
    throw new Error('Task execution timeout');
  }

  // Usage
  const execution = await client.task.run({
    taskId: taskId,
    version: '1',
    async: true,
    inputs: { ANCHOR_TARGET_URL: 'https://example.com' }
  });

  const result = await waitForTaskCompletion(taskId);
  console.log('Task completed:', result);
  ```

  ```python python theme={null}
  import os
  import time
  import requests

  # Poll for task completion
  def wait_for_task_completion(task_id: str, max_attempts: int = 60):
      for _ in range(max_attempts):
          response = requests.get(
              f"https://api.anchorbrowser.io/v1/task/{task_id}/executions",
              params={"page": 1, "limit": 1},
              headers={
                  "anchor-api-key": os.environ.get("ANCHORBROWSER_API_KEY"),
                  "Content-Type": "application/json"
              }
          )
          
          results = response.json()
          latest_result = results['data']['results'][0] if results['data']['results'] else None
          if latest_result:
              if latest_result['status'] in ['success', 'failure']:
                  return latest_result
          
          # Wait 2 seconds before next poll
          time.sleep(2)
      
      raise Exception('Task execution timeout')

  # Usage
  execution = client.task.run(
      task_id=task_id,
      version="1",
      async_=True,
      inputs={"ANCHOR_TARGET_URL": "https://example.com"}
  )

  result = wait_for_task_completion(task_id)
  print(f"Task completed: {result}")
  ```
</CodeGroup>

## Support

For additional help with the Tasks API:

* Check the [API Reference](/api-reference/browser-sessions/start-browser-session/) for detailed tasks endpoint documentation
* Contact Anchor Browser support at [support@anchorbrowser.io](mailto:support@anchorbrowser.io)


# CrewAI
Source: https://docs.anchorbrowser.io/agent-frameworks/crewai



AI agents can leverage browser sessions to complete tasks in the web. The ways to use the browser in CrewAI agent platform are:

* **As a Flexible Browser Tool**: Enable the CrewAI agent to explore the web freely using a general-purpose browser tool.
* **As a Specific-Flow Tool Defined in CrewAI**: Create custom tools by writing CrewAI code to define specific workflows tailored to your needs.
* **As a Specific-Flow Tool Defined in Anchor Browser**: Define tools using the Anchor platform, which CrewAI agents can then use through the Official Anchor Tool.

## Quick start - Use Anchor Browser as a flexible browser tool

You can connect your CrewAI agent directly to Anchor Browser, allowing it to use browser sessions for various tasks, leveraging the power of browser automation without the need for complex integration code. Below is a quick guide to setting up and using Anchor Browser as a tool for your CrewAI agent.

<Accordion title="Code example - Use Anchor Browser as a flexible browser tool">
  <CodeGroup>
    ```python python theme={null}
    import os
    from anchorbrowser import Anchorbrowser
    from crewai import Agent, Task, Crew

    ANCHOR_API_KEY = os.getenv("ANCHOR_API_KEY")

    # Create an Anchor Browser tool for CrewAI
    class AnchorBrowserTool:
        def __init__(self):
            self.anchor_client = Anchorbrowser(api_key=ANCHOR_API_KEY)
        
        def browse_and_extract(self, url, task_description):
            # Create a browser session
            session = self.anchor_client.sessions.create(
                session={
                    "max_duration": 30,
                    "idle_timeout": 10
                }
            )
            
            try:
                # Use the agent to perform the task
                result = self.anchor_client.agent.task(
                    task_description,
                    task_options={
                        "url": url,
                        "session_id": session.id
                    }
                )
                return result
            finally:
                # Clean up
                self.anchor_client.sessions.terminate(session.id)

    # Initialize the tool
    browser_tool = AnchorBrowserTool()

    # Create a CrewAI agent that uses Anchor Browser
    researcher = Agent(
        role='Web Researcher',
        goal='Research and extract information from websites',
        backstory='Expert at gathering information from web sources',
        tools=[browser_tool.browse_and_extract],
        verbose=True
    )

    # Create a task
    research_task = Task(
        description='Go to news.ycombinator.com and extract the title of the first story',
        agent=researcher
    )

    # Create and run the crew
    crew = Crew(
        agents=[researcher],
        tasks=[research_task],
        verbose=True
    )

    result = crew.kickoff()
    print(result)
    ```

    ```javascript node.js theme={null}
    const { AnchorClient } = require("anchorbrowser");
    const { Agent, Task, Crew } = require("crewai");

    class AnchorBrowserTool {
        constructor() {
            this.anchorClient = new AnchorClient({
                apiKey: process.env.ANCHOR_API_KEY,
            });
        }
        
        async browseAndExtract(url, taskDescription) {
            // Create a browser session
            const session = await this.anchorClient.sessions.create({
                session: {
                    max_duration: 30,
                    idle_timeout: 10
                }
            });
            
            try {
                // Use the agent to perform the task
                const result = await this.anchorClient.agent.task(
                    taskDescription,
                    { sessionId: session.id }
                );
                return result;
            } finally {
                // Clean up
                await this.anchorClient.sessions.terminate(session.id);
            }
        }
    }

    // Initialize the tool
    const browserTool = new AnchorBrowserTool();

    // Create a CrewAI agent that uses Anchor Browser
    const researcher = new Agent({
        role: 'Web Researcher',
        goal: 'Research and extract information from websites',
        backstory: 'Expert at gathering information from web sources',
        tools: [browserTool.browseAndExtract.bind(browserTool)],
        verbose: true
    });

    // Create a task
    const researchTask = new Task({
        description: 'Go to news.ycombinator.com and extract the title of the first story',
        agent: researcher
    });

    // Create and run the crew
    const crew = new Crew({
        agents: [researcher],
        tasks: [researchTask],
        verbose: true
    });

    const result = await crew.kickoff();
    console.log(result);
    ```
  </CodeGroup>
</Accordion>

## Use Anchor Browser as a specific-flow tool defined in CrewAI

CrewAI can integrate closely with Anchor Browser to define tools for particular workflows. For example, if you need a customized process to interact with an authenticated application, you can create that flow as a reusable tool that CrewAI agents can use for automation.

Here is an example of creating a specific workflow tool using Anchor Browser that can be utilized by CrewAI to automate targeted tasks.

<Accordion title="Code example - Use Anchor Browser as a specific-flow tool defined in CrewAI">
  <CodeGroup>
    ```python python theme={null}

    import crewai
    from playwright.sync_api import sync_playwright

    ANCHOR_API_KEY = "YOUR_ANCHOR_API_KEY"  # Replace with your actual API key

    # Register Anchor Browser as a specific application tool in CrewAI
    class AnchorSpecificTool(crewai.Tool):
        name = "SpecificAnchorTool"
        description = "Custom tool for interacting with a specific application."

        def __init__(self):
            super().__init__()

            anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
            with sync_playwright() as p:
                # Create a browser session
                session = anchor_client.sessions.create()
                cdp_url = session.data.cdp_url
            
                # Connect to Anchor Browser session
                browser = p.chromium.connect_over_cdp(cdp_url)
                page = browser.new_page()
                page.goto(command['url'])

                # Perform specific actions based on command
                if command.get('action') == 'extract':
                    result = page.text_content(command['selector'])
                    browser.close()
                    return result

                browser.close()

    # Add custom AnchorBrowserTool to CrewAI agent
    my_agent = crewai.Agent(name="Web Automation Agent")
    my_agent.add_tool(AnchorSpecificTool())

    # Use the agent to perform a specific task
    result = my_agent.act({
        'tool': 'SpecificAnchorTool',
        'command': {
            'url': 'https://example.com',
            'action': 'extract',
            'selector': 'body'
        }
    })

    print(result)
    ```

    ```jsx node.js theme={null}
    const { chromium } = require('playwright-core');
    const AnchorClient = require('anchorbrowser');
    const crewai = require('crewai');

    // Define a custom specific-flow tool in CrewAI that uses Anchor Browser
    class AnchorSpecificTool {
      name = "SpecificAnchorTool";
      description = "Custom tool for interacting with a specific application.";

      async run(command) {
        const anchorClient = new AnchorClient({
            apiKey: process.env.ANCHOR_API_KEY,
        });

        // Create a browser session
        const session = await anchorClient.sessions.create();
        const cdp_url = session.data.cdp_url;

        // Connect to Anchor Browser session
        const browser = await chromium.connectOverCDP(cdp_url);

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
    }

    // Create a CrewAI agent and add the custom specific-flow Anchor Browser tool
    const agent = new crewai.Agent({ name: "Web Automation Agent" });
    const anchorSpecificTool = new AnchorSpecificTool();
    agent.addTool(anchorSpecificTool);

    // Use the tool through the CrewAI agent
    const result = await agent.act({
      tool: 'SpecificAnchorTool',
      command: {
        url: 'https://example.com',
        action: 'extract',
        selector: 'body'
      }
    });

    console.log(result);
    ```
  </CodeGroup>
</Accordion>


# Custom Integration
Source: https://docs.anchorbrowser.io/agent-frameworks/custom-agent-framework



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


# LangChain
Source: https://docs.anchorbrowser.io/agent-frameworks/langchain



AI agents can leverage browser sessions to complete tasks on the web using LangChain, a framework that provides easy integration for AI-driven workflows.

Anchor provides [LangChain tools](https://python.langchain.com/docs/integrations/tools/anchor_browser/) that allows you to use Anchor Browser as a tool in your LangChain workflows.
The package contains the following tools:

* `AnchorContentTool`: Get the content of a web page in markdown format.
* `AnchorScreenshotTool`: Take a screenshot of a web page.
* `AnchorWebTaskTools`: Perform intelligent web tasks using AI:
  * Simple - `SimpleAnchorWebTaskTool`
  * Advanced - `AdvancedAnchorWebTaskTool`

See Anchor Browser package for LangChain on [PyPi](https://pypi.org/project/langchain-anchorbrowser/) for more information.

## Quickstart

### Installation

Install the `langchain-anchorbrowser` package:

```bash theme={null}
pip install langchain-anchorbrowser
```

### Usage

Import and utilize your intended tool. The full list of Anchor Browser available tools see **Tool Features** table in [Anchor Browser tool page](/docs/integrations/tools/anchor_browser)

```python theme={null}
from langchain_anchorbrowser import AnchorContentTool

# Get Markdown Content for https://www.anchorbrowser.io
AnchorContentTool().invoke(
    {"url": "https://www.anchorbrowser.io", "format": "markdown"}
)
```

## Additional Resources

* [PyPi](https://pypi.org/project/langchain-anchorbrowser)
* [Github](https://github.com/anchorbrowser/langchain-anchorbrowser)
* [Anchor Browser Docs on LangChain](https://python.langchain.com/docs/integrations/tools/anchor_browser/)


# Agentic File Usage
Source: https://docs.anchorbrowser.io/agentic-browser-control/agentic-file-usage

Upload ZIP files to browser sessions for AI agents to use

<Warning>
  **Compatibility Note**: Only works with the `browser-use` agent. Not supported with `openai-cua`, `gemini-computer-use`, and `anthropic-cua`.
</Warning>

## Quick Start

Upload a ZIP file containing resources that your AI agent can use to complete tasks. The ZIP file is automatically extracted and made available to the agent.

## Example: Upload ZIP File

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';
  import JSZip from 'jszip';

  const ANCHOR_API_KEY = process.env.ANCHOR_API_KEY;

  // Initialize Anchor client
  const anchorClient = new Anchorbrowser({
    apiKey: ANCHOR_API_KEY,
  });

  // Create a new session
  const session = await anchorClient.sessions.create();
  console.log('session live view url:', session.data?.live_view_url);
  const sessionId = session.data?.id;

  // 1. Create a test ZIP file with content
  const zip = new JSZip();
  zip.file('test.txt', 'Hello from Anchor!\nThis is a test file for the agent.');
  const zipBlob = await zip.generateAsync({ type: 'blob' });
  const zipFile = new File([zipBlob], 'test-data.zip', { type: 'application/zip' });

  console.log(`Uploading file to session...`);
  // 2. Upload to browser session
  const fileUploadResult = await anchorClient.sessions.agent.files.upload(sessionId!, {
    file: zipFile
  });
  console.log('Upload result:', fileUploadResult);

  // 3. Use uploaded files with AI agent
  const result = await anchorClient.agent.task('upload a file to the server', {
    taskOptions: {
        url: 'https://v0-download-and-upload-text.vercel.app/',
      },
    sessionId: sessionId
    });
  console.log('AI agent result:', result);
  ```

  ```python python theme={null}
  import os
  import zipfile
  import tempfile
  from anchorbrowser import Anchorbrowser

  ANCHOR_API_KEY = os.getenv("ANCHOR_API_KEY")

  # Initialize Anchor client
  anchor_client = Anchorbrowser(api_key=ANCHOR_API_KEY)

  # Create a new session
  session = anchor_client.sessions.create()
  print('session live view url:', session.data.live_view_url)
  session_id = session.data.id

  # 1. Create a test ZIP file with content
  with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as temp_zip:
      with zipfile.ZipFile(temp_zip.name, 'w') as zip_file:
          zip_file.writestr('test.txt', 'Hello from Anchor!\nThis is a test file for the agent.')
      
      # 2. Upload to browser session
      with open(temp_zip.name, 'rb') as zip_file:
          result = anchor_client.sessions.agent.files.upload(
              session_id=session_id,
              file=zip_file
          )
      
      # Clean up temporary file
      os.unlink(temp_zip.name)

  print('Upload result:', result)

  # 3. Use uploaded files with AI agent
  result = anchor_client.agent.task('upload a file to the server',
      task_options={
          "url": 'https://v0-download-and-upload-text.vercel.app/',
        },
        session_id=session_id,
      )
  print('AI agent result:', result)
  ```
</CodeGroup>

That's it! The agent can now access all uploaded files and use them to complete web tasks.


# AI Task Completion
Source: https://docs.anchorbrowser.io/agentic-browser-control/ai-task-completion



Anchor Browser delivers a state-of-the-art 89% Score on the industry-standard benchmark WebVoyager, leveraging browser-use as a core component of the automation capability.

<video />

## The agent task method

Anchor Browser provides within its SDK the `agent.task` method that enables natural language control over web browsing sessions. This capability allows you to **automate complex web tasks without coding the whole flow.**

<Note>
  Looking for Tasks? Visit the [Tasks Page](/advanced/tasks).
</Note>

### Code Example

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  const anchorClient = new Anchorbrowser({
    apiKey: process.env.ANCHORBROWSER_API_KEY
  });

  const response = await anchorClient.agent.task(
    'Extract the main heading',                     // Required
    {
      taskOptions: {
        url: 'https://example.com',                 // Either sessionId or url is required
        humanIntervention: false,                   // Disable human intervention during task execution (disabled by default)
        detectElements: true,                       // Improves the agent's ability to identify and interact with UI elements
        maxSteps: 40,                               // Maximum number of steps the agent can take
        agent: 'browser-use',                       // browser-use (default), openai-cua, or gemini-computer-use
        provider: 'openai',                         // For browser-use agent only, openai, gemini, groq, azure, xai
        model: 'gpt-5',                             // For browser-use agent only, see model list below
        extendedSystemMessage: 'Focus on extracting the main heading from the page',
        secretValues: {                             // Secret values to pass to the agent for secure credential handling
          API_KEY: 'your-secret-key'
        }
      }
    }
  );

  console.log(response);
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchor_client = Anchorbrowser(api_key=os.environ.get("ANCHORBROWSER_API_KEY"))

  response = anchor_client.agent.task(
      'Extract the main heading',                    # Required
      task_options={
          url='https://example.com',                 # Either session_id or url is required
          human_intervention=False,                  # Disable human intervention during task execution (disabled by default)
          detect_elements=True,                      # Improves the agent's ability to identify and interact with UI elements
          max_steps=40,                              # Maximum number of steps the agent can take
          agent='browser-use',                       # browser-use (default), openai-cua, or gemini-computer-use
          provider='openai',                           # For browser-use agent only, openai, gemini, groq, azure, xai
          model='gpt-5',               # For browser-use agent only, see model list below
          extended_system_message='Focus on extracting the main heading from the page',
          secret_values={                            # Secret values to pass to the agent for secure credential handling
              'API_KEY': 'your-secret-key'
          }
      }
  )

  print(response)
  ```
</CodeGroup>

## Structured Output

The AI object can also be used to extract structured data from the browser. This is done by providing a **JSON schema** to the AI object, which will then return the structured data.
The following demonstrates using **Zod** and **Pydantic** to utilize the structured output capability.

<CodeGroup>
  ```javascript node.js theme={null}
  import { z } from 'zod';
  import { zodToJsonSchema } from 'zod-to-json-schema';

  const anchorClient = new Anchorbrowser()

  // Define the expected output structure using Zod schema
  const outputSchema = z.object({
    nodes_cpu_usage: z.array(
      z.object({
        node: z.string(),                 // Node name
        cluster: z.string(),              // Cluster identifier
        cpu_avg_percentage: z.number(),   // CPU usage percentage
      })
    )
  });

  // Execute the AI task with structured output
  const result = await anchorClient.agent.task('Collect the node names and their CPU average %', {
    taskOptions: {
      outputSchema: zodToJsonSchema(outputSchema), // Convert to JSON Schema
      url: 'https://play.grafana.org/a/grafana-k8s-app/navigation/nodes?from=now-1h&to=now&refresh=1m',
    }
  });
  console.info(result);
  ```

  ```python python theme={null}
  # Define data models using Pydantic for structured output
  class NodeCpuUsage(BaseModel):
      node: str                    # Node name
      cluster: str                 # Cluster identifier
      cpu_avg_percentage: float    # CPU usage percentage

  class OutputSchema(BaseModel):
      nodes_cpu_usage: List[NodeCpuUsage]  # List of node CPU usage data

  # Create task payload with structured output schema
  task_payload = {
      'prompt': 'Collect the node names and their CPU average %',
      'output_schema': OutputSchema.model_json_schema()  # Convert to JSON Schema
  }

  result = anchor_client.agent.task('Collect the node names and their CPU average %',
      task_options={
          'output_schema': OutputSchema.model_json_schema(),
          'url': 'https://play.grafana.org/a/grafana-k8s-app/navigation/nodes?from=now-1h&to=now&refresh=1m',
      }
  )
  print(result)
  ```
</CodeGroup>

<Expandable title="Configuration Options">
  ## Configuration Options

  The AI agent can be configured with the following parameters:

  <Note>
    Parameter names use `snake_case` in Python and `camelCase` in JavaScript/TypeScript (e.g., `max_steps` vs `maxSteps`).
  </Note>

  * **agent** (string): AI agent to use (`browser-use`, `openai-cua`, `gemini-computer-use`). Defaults to `browser-use`.
  * **secret\_values** | **secretValues** (object): Secret values to pass to the agent for secure credential handling.
  * **human\_intervention** | **humanIntervention** (boolean): Allow human intervention during task execution.
  * **provider** (string): AI provider to use (`openai`, `gemini`, `groq`, `azure`, `xai`).
  * **model** (string): Specific model to use (see [Available Models](#available-models) below).
  * **url** (string): Target URL to navigate to before executing the task.
  * **output\_schema** | **outputSchema** (object): JSON Schema defining the expected structure of the output data.
  * **max\_steps** | **maxSteps** (integer): Maximum number of steps the agent can take (default: 40).
  * **detect\_elements** | **detectElements** (boolean): Enable element detection for better interaction accuracy.
  * **extended\_system\_message** | **extendedSystemMessage** (string): Custom system message to provide additional context or instructions to the agent.
  * **use\_vision** | **useVision** (boolean): Enable vision capabilities for enhanced visual understanding.
</Expandable>

## Secret Values

<p>Securely pass credentials and sensitive data to AI agents during task execution. Secret values are not logged and automatically cleaned up after completion.</p>
<p><a href="/agentic-browser-control/secret-values">Learn more about Secret Values →</a></p>

## Available Models For Browser-Use

<Expandable title="Available Models">
  <Tabs>
    <Tab title="OpenAI">
      <div>
        <div>gpt-5.2</div>
        <div>gpt-5</div>
        <div>gpt-5-mini</div>
        <div>gpt-5-nano</div>
        <div>gpt-4o</div>
        <div>gpt-4o-mini</div>
        <div>gpt-4.1</div>
        <div>gpt-4.1-mini</div>
      </div>
    </Tab>

    <Tab title="Gemini">
      <div>
        <div>gemini-3-flash-preview</div>
        <div>gemini-3-pro-preview</div>
        <div>gemini-2.5-flash</div>
        <div>gemini-2.5-flash-lite</div>
        <div>gemini-2.5-pro</div>
        <div>gemini-2.0-flash</div>
        <div>gemini-2.0-flash-exp</div>
        <div>gemini-2.0-flash-lite</div>
      </div>
    </Tab>

    <Tab title="Groq">
      <div>
        <div>openai/gpt-oss-120b</div>
        <div>meta-llama/llama-4-maverick-17b-128e-instruct</div>
        <div>meta-llama/llama-4-scout-17b-16e-instruct</div>
        <div>moonshotai/kimi-k2-instruct</div>
      </div>
    </Tab>

    <Tab title="Azure">
      <div>
        <div>o4-mini</div>
        <div>o3</div>
        <div>o3-mini</div>
        <div>o1</div>
      </div>
    </Tab>
  </Tabs>
</Expandable>


# Async Perform Web Task
Source: https://docs.anchorbrowser.io/agentic-browser-control/async-perform-web-task

Run perform-web-task asynchronously and poll for results

## Basic Usage

To run `perform-web-task` asynchronously, set the `async` parameter to `true` in your request. The API will return immediately with a `workflow_id` that you can use to poll for results.

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  const anchorClient = new Anchorbrowser({
  apiKey: process.env.ANCHORBROWSER_API_KEY
  });

  // Start async task
  const response = await anchorClient.tools.performWebTask({
  prompt: 'Extract the main heading and first paragraph from the page',
  url: 'https://docs.anchorbrowser.io',
  async: true
  });

  console.log('Workflow ID:', response.data.workflow_id);
  console.log('Status:', response.data.status);
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchor_client = Anchorbrowser(api_key=os.environ.get("ANCHORBROWSER_API_KEY"))

  # Start async task
  response = anchor_client.tools.perform_web_task(
      prompt='Extract the main heading and first paragraph from the page',
      url='https://docs.anchorbrowser.io',
      async_=True
  )

  print('Workflow ID:', response.data.workflow_id)
  print('Status:', response.data.status)
  ```
</CodeGroup>

<Expandable title="Parameters">
  ## Parameters

  The async `perform-web-task` accepts the following parameters:

  | Parameter            | Type    | Required | Description                                                                                                                                                     |
  | -------------------- | ------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `prompt`             | string  | Yes      | The task to be autonomously completed                                                                                                                           |
  | `url`                | string  | No       | The URL of the webpage. If not provided, the tool will use the current page in the session                                                                      |
  | `sessionId`          | string  | No       | An optional browser session identifier to reference an existing running browser session. When passed, the tool will be executed on the provided browser session |
  | `async`              | boolean | No       | Whether to run the task asynchronously. If `true`, the task will be run asynchronously and the response will include a workflow ID. Defaults to `false`         |
  | `agent`              | string  | No       | The AI agent to use for task completion. Options: `browser-use` (default), `openai-cua`, `gemini-computer-use`, `anthropic-cua`                                 |
  | `provider`           | string  | No       | The AI provider to use for task completion. Options: `openai`, `gemini`, `groq`, `azure`, `xai`                                                                 |
  | `model`              | string  | No       | The specific model to use for task completion. See [Available Models](/agentic-browser-control/ai-task-completion#available-models) for more information        |
  | `detect_elements`    | boolean | No       | Enable element detection for better interaction accuracy. Improves the agent's ability to identify and interact with UI elements                                |
  | `human_intervention` | boolean | No       | Allow human intervention during task execution. When enabled, the agent can request human input for ambiguous situations                                        |
  | `max_steps`          | integer | No       | Maximum number of steps the agent can take to complete the task. Defaults to `200`                                                                              |
  | `secret_values`      | object  | No       | Secret values to pass to the agent for secure credential handling. Keys and values are passed as environment variables to the agent                             |
  | `highlight_elements` | boolean | No       | Whether to highlight elements during task execution for better visibility                                                                                       |
  | `output_schema`      | object  | No       | JSON Schema defining the expected structure of the output data                                                                                                  |
</Expandable>

## Polling for Results

After starting an async task, you'll receive a `workflow_id` in the response. Use this ID to poll the status endpoint until the task completes.

### Status Endpoint

<CodeGroup>
  ```javascript node.js theme={null}
  const statusResponse = await anchorClient.tools.getPerformWebTaskStatus(workflowId);

  // Status can be: 'RUNNING', 'COMPLETED', or 'FAILED'
  if (statusResponse.data.status === 'RUNNING') {
      console.log('Still running...');
  } else if (statusResponse.data.status === 'COMPLETED') {
      console.log('Result:', statusResponse.data.result);
  } else if (statusResponse.data.status === 'FAILED') {
      console.error('Error:', statusResponse.data.error);
  }
  ```

  ```python python theme={null}
  status_response = anchor_client.tools.get_perform_web_task_status(workflow_id)

  # Status can be: 'RUNNING', 'COMPLETED', or 'FAILED'
  if status_response['data']['status'] == 'RUNNING':
      print('Still running...')
  elif status_response['data']['status'] == 'COMPLETED':
      print('Result:', status_response['data']['result'])
  elif status_response['data']['status'] == 'FAILED':
      print('Error:', status_response['data']['error'])
  ```
</CodeGroup>

### Response Statuses

* **`RUNNING`**: The workflow is currently executing
* **`COMPLETED`**: The workflow has completed. The `result` field contains the task output as a string.

<Note>
  The status will be `COMPLETED` even if the agent fails to complete the task, since the workflow execution itself succeeded. Always check the `result` field to verify whether the agent completed the task successfully or encountered an error.
</Note>

* **`FAILED`**: The workflow has failed. The `error` field contains the error message

## Complete Example

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  (async () => {
    const anchorClient = new Anchorbrowser({
      apiKey: process.env.ANCHORBROWSER_API_KEY
    });

    // Start multiple async tasks in parallel
    const responses = await Promise.all([
      anchorClient.tools.performWebTask({
        prompt: 'Extract the main heading',
        url: 'https://docs.anchorbrowser.io',
        async: true
      }),
      anchorClient.tools.performWebTask({
        prompt: 'Get the first paragraph',
        url: 'https://example.com',
        async: true
      })
    ]);

    const workflowIds = responses.map(response => response.data.workflow_id);
    console.log('Started', workflowIds.length, 'tasks');

    // Poll all tasks
    const results = await Promise.all(
      workflowIds.map(async (wokflowId) => {
        let status = 'RUNNING';
        while (status === 'RUNNING') {
          await new Promise(resolve => setTimeout(resolve, 2000));
          const statusResponse = await anchorClient.tools.getPerformWebTaskStatus(wokflowId);
          status = statusResponse.data.status;

          if (status === 'COMPLETED') {
            return statusResponse.data.result;
          } else if (status === 'FAILED') {
            throw new Error(statusResponse.data.error);
          }
        }
      })
    );

    console.log('All tasks completed:', results);
  })();
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os
  import time
  import requests

  anchor_client = Anchorbrowser(api_key=os.environ.get("ANCHORBROWSER_API_KEY"))

  # Start multiple async tasks in parallel
  responses = [
      anchor_client.tools.perform_web_task(
          prompt='Extract the main heading',
          url='https://docs.anchorbrowser.io',
          async_=True
      ),
      anchor_client.tools.perform_web_task(
          prompt='Get the first paragraph',
          url='https://example.com',
          async_=True
      )
  ]

  workflow_ids = [response.data.workflow_id for response in responses]
  print('Started', len(workflow_ids), 'tasks')

  # Poll all tasks
  results = []
  for workflow_id in workflow_ids:
      status = 'RUNNING'
      while status == 'RUNNING':
          time.sleep(2)

          status_response = anchor_client.tools.get_perform_web_task_status(workflow_id)
          status = status_response['data']['status']

          if status == 'COMPLETED':
              results.append(status_response['data']['result'])
              break
          elif status == 'FAILED':
              raise Exception(status_response['data']['error'])

  print('All tasks completed:', results)
  ```
</CodeGroup>


# Anthropic Computer Use
Source: https://docs.anchorbrowser.io/agentic-browser-control/computer-use-agents/anthropic

Use Claude models with native computer use capabilities for browser automation

Anthropic's Claude models with Computer Use capabilities enable AI agents to interact with web browsers through screenshots and native computer control actions.

## Overview

Anthropic Computer Use (`anthropic-cua`) leverages Claude's vision and reasoning capabilities to:

* Analyze screenshots of web pages
* Identify interactive elements
* Execute precise mouse and keyboard actions
* Complete complex multi-step workflows

## Supported Models

| Model             | Model ID                     | Best For                                                 |
| ----------------- | ---------------------------- | -------------------------------------------------------- |
| Claude Opus 4.5   | `claude-opus-4-5-20251101`   | Most advanced reasoning, complex workflows **(default)** |
| Claude Sonnet 4.5 | `claude-sonnet-4-5-20250929` | Balanced performance, general automation                 |
| Claude Opus 4     | `claude-opus-4-20250514`     | Advanced coding and agentic tasks                        |
| Claude Sonnet 4   | `claude-sonnet-4-20250514`   | Fast, reliable automation                                |

## Code Example

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  const anchorClient = new Anchorbrowser({
    apiKey: process.env.ANCHORBROWSER_API_KEY
  });

  const response = await anchorClient.agent.task(
    'Navigate to GitHub and find the anchorbrowser repository',
    {
      taskOptions: {
        url: 'https://github.com',
        agent: 'anthropic-cua',
        // model: 'claude-opus-4-5-20251101',  // Default model
        maxSteps: 30
      }
    }
  );

  console.log(response);
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchor_client = Anchorbrowser(api_key=os.environ.get("ANCHORBROWSER_API_KEY"))

  response = anchor_client.agent.task(
      'Navigate to GitHub and find the anchorbrowser repository',
      task_options={
          'url': 'https://github.com',
          'agent': 'anthropic-cua',
          # 'model': 'claude-opus-4-5-20251101',  # Default model
          'max_steps': 30
      }
  )

  print(response)
  ```
</CodeGroup>

## Configuration Options

| Parameter       | Type    | Description                                                                      |
| --------------- | ------- | -------------------------------------------------------------------------------- |
| `agent`         | string  | Must be `anthropic-cua`                                                          |
| `model`         | string  | Claude model to use (default: `claude-opus-4-5-20251101`)                        |
| `url`           | string  | Starting URL for the task                                                        |
| `max_steps`     | integer | Maximum actions the agent can take                                               |
| `output_schema` | object  | JSON Schema for structured output                                                |
| `secret_values` | object  | Secure credentials (see [Secret Values](/agentic-browser-control/secret-values)) |

## Secure Credentials with Secret Values

Anthropic CUA fully supports secret values for secure credential handling. Secrets are never exposed to the AI model.

<CodeGroup>
  ```javascript node.js theme={null}
  const response = await anchorClient.agent.task(
    'Login to the dashboard and download my latest report',
    {
      taskOptions: {
        url: 'https://app.example.com/login',
        agent: 'anthropic-cua',
        secretValues: {
          EMAIL: process.env.APP_EMAIL,
          PASSWORD: process.env.APP_PASSWORD
        }
      }
    }
  );
  ```

  ```python python theme={null}
  response = anchor_client.agent.task(
      'Login to the dashboard and download my latest report',
      task_options={
          'url': 'https://app.example.com/login',
          'agent': 'anthropic-cua',
          'secret_values': {
              'EMAIL': os.environ.get('APP_EMAIL'),
              'PASSWORD': os.environ.get('APP_PASSWORD')
          }
      }
  )
  ```
</CodeGroup>

Learn more about [domain-scoped secrets and TOTP support](/agentic-browser-control/secret-values).

## Best Practices

* **Opus 4.5 is the default** - most capable model for complex workflows
* **Use Sonnet 4.5** for faster automation when speed is important
* **Provide clear, specific prompts** describing the exact task to complete


# Gemini Computer Use
Source: https://docs.anchorbrowser.io/agentic-browser-control/computer-use-agents/gemini

Use Google Gemini models for screenshot-based browser automation

Google's Gemini Computer Use agent (`gemini-computer-use`) enables AI-powered browser automation through visual understanding and multi-turn interactions.

## Overview

Gemini Computer Use leverages Google's multimodal AI capabilities to:

* Process and understand web page screenshots
* Plan and execute multi-step browser interactions
* Handle complex visual layouts and dynamic content
* Integrate with Google's AI ecosystem

## Supported Models

| Model                   | Model ID                                  | Best For                                  |
| ----------------------- | ----------------------------------------- | ----------------------------------------- |
| Gemini 2.5 Computer Use | `gemini-2.5-computer-use-preview-10-2025` | Screenshot-based automation **(default)** |

## Code Example

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  const anchorClient = new Anchorbrowser({
    apiKey: process.env.ANCHORBROWSER_API_KEY
  });

  const response = await anchorClient.agent.task(
    'Search for the latest AI news and summarize the top 3 articles',
    {
      taskOptions: {
        url: 'https://news.google.com',
        agent: 'gemini-computer-use',
        // model: 'gemini-2.5-computer-use-preview-10-2025',  // Default model
        maxSteps: 25,
        outputSchema: {
          type: 'object',
          properties: {
            articles: {
              type: 'array',
              items: {
                type: 'object',
                properties: {
                  title: { type: 'string' },
                  summary: { type: 'string' },
                  source: { type: 'string' }
                }
              }
            }
          }
        }
      }
    }
  );

  console.log(response);
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchor_client = Anchorbrowser(api_key=os.environ.get("ANCHORBROWSER_API_KEY"))

  response = anchor_client.agent.task(
      'Search for the latest AI news and summarize the top 3 articles',
      task_options={
          'url': 'https://news.google.com',
          'agent': 'gemini-computer-use',
          # 'model': 'gemini-2.5-computer-use-preview-10-2025',  # Default model
          'max_steps': 25,
          'output_schema': {
              'type': 'object',
              'properties': {
                  'articles': {
                      'type': 'array',
                      'items': {
                          'type': 'object',
                          'properties': {
                              'title': {'type': 'string'},
                              'summary': {'type': 'string'},
                              'source': {'type': 'string'}
                          }
                      }
                  }
              }
          }
      }
  )

  print(response)
  ```
</CodeGroup>

## Configuration Options

| Parameter       | Type    | Description                                                                      |
| --------------- | ------- | -------------------------------------------------------------------------------- |
| `agent`         | string  | Must be `gemini-computer-use`                                                    |
| `model`         | string  | Gemini model to use (default: `gemini-2.5-computer-use-preview-10-2025`)         |
| `url`           | string  | Starting URL for the task                                                        |
| `max_steps`     | integer | Maximum actions the agent can take                                               |
| `output_schema` | object  | JSON Schema for structured output                                                |
| `secret_values` | object  | Secure credentials (see [Secret Values](/agentic-browser-control/secret-values)) |

## Secure Credentials with Secret Values

Gemini Computer Use fully supports secret values for secure credential handling. Secrets are never exposed to the AI model.

<CodeGroup>
  ```javascript node.js theme={null}
  const response = await anchorClient.agent.task(
    'Login to the dashboard and download my latest report',
    {
      taskOptions: {
        url: 'https://app.example.com/login',
        agent: 'gemini-computer-use',
        secretValues: {
          EMAIL: process.env.APP_EMAIL,
          PASSWORD: process.env.APP_PASSWORD
        }
      }
    }
  );
  ```

  ```python python theme={null}
  response = anchor_client.agent.task(
      'Login to the dashboard and download my latest report',
      task_options={
          'url': 'https://app.example.com/login',
          'agent': 'gemini-computer-use',
          'secret_values': {
              'EMAIL': os.environ.get('APP_EMAIL'),
              'PASSWORD': os.environ.get('APP_PASSWORD')
          }
      }
  )
  ```
</CodeGroup>

Learn more about [domain-scoped secrets and TOTP support](/agentic-browser-control/secret-values).

## Best Practices

* **gemini-2.5-computer-use-preview is the default** - optimized for screenshot-based automation
* **Leverage structured output** with `output_schema` for reliable data extraction
* **Provide clear, specific prompts** describing the exact task to complete


# OpenAI Computer Use
Source: https://docs.anchorbrowser.io/agentic-browser-control/computer-use-agents/openai

Use OpenAI models with computer use capabilities for browser automation

OpenAI's Computer Use Agent (`openai-cua`) leverages GPT models with vision and reasoning capabilities for screenshot-based browser automation.

## Overview

OpenAI Computer Use provides:

* **Screenshot-based interactions** for visual understanding of web pages
* **Advanced reasoning** powered by GPT models
* **High accuracy** for complex web interactions
* **Structured outputs** for reliable data extraction

## Supported Models

| Model                | Model ID               | Best For                                  |
| -------------------- | ---------------------- | ----------------------------------------- |
| Computer Use Preview | `computer-use-preview` | Screenshot-based automation **(default)** |

## Code Example

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  const anchorClient = new Anchorbrowser({
    apiKey: process.env.ANCHORBROWSER_API_KEY
  });

  const response = await anchorClient.agent.task(
    'Find the pricing information and extract the plan details',
    {
      taskOptions: {
        url: 'https://example.com/pricing',
        agent: 'openai-cua',
        // model: 'computer-use-preview',  // Default model
        maxSteps: 25,
        outputSchema: {
          type: 'object',
          properties: {
            plans: {
              type: 'array',
              items: {
                type: 'object',
                properties: {
                  name: { type: 'string' },
                  price: { type: 'string' },
                  features: { type: 'array', items: { type: 'string' } }
                }
              }
            }
          }
        }
      }
    }
  );

  console.log(response);
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchor_client = Anchorbrowser(api_key=os.environ.get("ANCHORBROWSER_API_KEY"))

  response = anchor_client.agent.task(
      'Find the pricing information and extract the plan details',
      task_options={
          'url': 'https://example.com/pricing',
          'agent': 'openai-cua',
          # 'model': 'computer-use-preview',  # Default model
          'max_steps': 25,
          'output_schema': {
              'type': 'object',
              'properties': {
                  'plans': {
                      'type': 'array',
                      'items': {
                          'type': 'object',
                          'properties': {
                              'name': {'type': 'string'},
                              'price': {'type': 'string'},
                              'features': {'type': 'array', 'items': {'type': 'string'}}
                          }
                      }
                  }
              }
          }
      }
  )

  print(response)
  ```
</CodeGroup>

## Configuration Options

| Parameter       | Type    | Description                                                                      |
| --------------- | ------- | -------------------------------------------------------------------------------- |
| `agent`         | string  | Must be `openai-cua`                                                             |
| `model`         | string  | OpenAI model to use (default: `computer-use-preview`)                            |
| `url`           | string  | Starting URL for the task                                                        |
| `max_steps`     | integer | Maximum actions the agent can take                                               |
| `output_schema` | object  | JSON Schema for structured output                                                |
| `secret_values` | object  | Secure credentials (see [Secret Values](/agentic-browser-control/secret-values)) |

## Secure Credentials with Secret Values

OpenAI CUA fully supports secret values for secure credential handling. Secrets are never exposed to the AI model.

<CodeGroup>
  ```javascript node.js theme={null}
  const response = await anchorClient.agent.task(
    'Login to the dashboard and download my latest report',
    {
      taskOptions: {
        url: 'https://app.example.com/login',
        agent: 'openai-cua',
        secretValues: {
          EMAIL: process.env.APP_EMAIL,
          PASSWORD: process.env.APP_PASSWORD
        }
      }
    }
  );
  ```

  ```python python theme={null}
  response = anchor_client.agent.task(
      'Login to the dashboard and download my latest report',
      task_options={
          'url': 'https://app.example.com/login',
          'agent': 'openai-cua',
          'secret_values': {
              'EMAIL': os.environ.get('APP_EMAIL'),
              'PASSWORD': os.environ.get('APP_PASSWORD')
          }
      }
  )
  ```
</CodeGroup>

Learn more about [domain-scoped secrets and TOTP support](/agentic-browser-control/secret-values).


# Human-in-the-Loop
Source: https://docs.anchorbrowser.io/agentic-browser-control/human-in-the-loop

Enable human intervention during AI agent task execution

Enabling Human-in-the-loop (HITL) allows the AI agent to pause execution and request human intervention when needed. This feature is essential for tasks that require human judgment, approval, or handling of unexpected situations.

## Basic Usage

### How It Works

When HITL is enabled, the agent sends its intervention requests to a session-specific queue. The agent then continues execution based on your instructions.

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  (async () => {
    const anchorClient = new Anchorbrowser({
      apiKey: process.env.ANCHOR_API_KEY
    });

    const response = await anchorClient.agent.task(
      'Research information about Python programming on Wikipedia and create a summary. Ask for human verification if you find any controversial or disputed information.',
      {
        taskOptions: {
          url: 'https://en.wikipedia.org/wiki/Python_(programming_language)',
          humanIntervention: true,
          extendedSystemMessage: 'Request human intervention when you encounter disputed or controversial claims about Python'
        }
      }
    );

    console.log(response);
  })();
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchor_client = Anchorbrowser(api_key=os.environ.get("ANCHOR_API_KEY"))

  response = anchor_client.agent.task(
      'Research information about Python programming on Wikipedia and create a summary. Ask for human verification if you find any controversial or disputed information.',
      task_options={
          'url': 'https://en.wikipedia.org/wiki/Python_(programming_language)',
          'human_intervention': True,
          'extended_system_message': 'Request human intervention when you encounter disputed or controversial claims about Python'
      }
  )

  print(response)
  ```
</CodeGroup>

<Tip>
  Human-in-the-loop is most effective when combined with clear system messages that define specific intervention triggers and provide context for decision-making.
</Tip>

## Get Pending Requests

To retrieve pending human intervention requests from the agent, use the GET endpoint:

<CodeGroup>
  ```javascript node.js theme={null}
  (async () => {
    const response = await fetch(`https://api.anchorbrowser.io/v1/sessions/${sessionId}/agent/requested-human-intervention`, {
      method: 'GET',
      headers: {
        'anchor-api-key': process.env.ANCHOR_API_KEY
      }
    });

    const data = await response.json();
    console.log('Intervention requests:', data.data.requests);
  })();
  ```

  ```python python theme={null}
  import requests
  import os

  response = requests.get(
      f'https://api.anchorbrowser.io/v1/sessions/{session_id}/agent/requested-human-intervention',
      headers={
          'anchor-api-key': os.getenv('ANCHOR_API_KEY')
      }
  )

  data = response.json()
  print('Intervention requests:', data['data']['requests'])
  ```
</CodeGroup>

## Send Intervention Response

To send a response to a pending human intervention request, use the POST endpoint:

<CodeGroup>
  ```javascript node.js theme={null}
  (async () => {
    const response = await fetch(`https://api.anchorbrowser.io/v1/sessions/${sessionId}/agent/respond-to-human-intervention`, {
      method: 'POST',
      headers: {
        'anchor-api-key': process.env.ANCHOR_API_KEY,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        requestId: 'request-id-from-intervention-request',
        response: 'Your response to the agent\'s request'
      })
    });

    const data = await response.json();
    console.log('Response:', data);
  })();
  ```

  ```python python theme={null}
  import requests
  import os

  response = requests.post(
      f'https://api.anchorbrowser.io/v1/sessions/{session_id}/agent/respond-to-human-intervention',
      headers={
          'anchor-api-key': os.getenv('ANCHOR_API_KEY'),
          'Content-Type': 'application/json'
      },
      json={
          'requestId': 'request-id-from-intervention-request',
          'response': 'Your response to the agent\'s request'
      }
  )

  data = response.json()
  print('Response:', data)
  ```
</CodeGroup>


# Secret Values
Source: https://docs.anchorbrowser.io/agentic-browser-control/secret-values

Securely pass credentials and sensitive data to AI agents

Secret values allow you to securely pass credentials, API keys, and other sensitive data to AI agents during task execution. These values are automatically handled at type-time, never logged, and never exposed to the AI model.

Secret values work with all agent types: `browser-use`, `openai-cua`, `anthropic-cua`, and `gemini-computer-use`.

## Basic Usage

Pass credentials as key-value pairs in `secretValues`. The agent will securely use these values when logging into websites or filling forms.

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  const anchorClient = new Anchorbrowser({
    apiKey: process.env.ANCHORBROWSER_API_KEY
  });

  const response = await anchorClient.agent.task(
    'Login to LinkedIn and send a connection request to the Anchorbrowser team',
    {
      taskOptions: {
        url: 'https://linkedin.com',
        secretValues: {
          LINKEDIN_EMAIL: process.env.LINKEDIN_EMAIL,
          LINKEDIN_PASSWORD: process.env.LINKEDIN_PASSWORD
        }
      }
    }
  );

  console.log(response);
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchor_client = Anchorbrowser(api_key=os.environ.get("ANCHORBROWSER_API_KEY"))

  response = anchor_client.agent.task(
      'Login to LinkedIn and send a connection request to the Anchorbrowser team',
      task_options={
          'url': 'https://linkedin.com',
          'secret_values': {
              'LINKEDIN_EMAIL': os.environ.get('LINKEDIN_EMAIL'),
              'LINKEDIN_PASSWORD': os.environ.get('LINKEDIN_PASSWORD')
          }
      }
  )

  print(response)
  ```
</CodeGroup>

<Tip>
  Secret values are the recommended way to handle any sensitive data in AI agent tasks. Never include credentials directly in prompts.
</Tip>

## Domain-Scoped Secrets

For enhanced security, you can scope secrets to specific domains. Secrets will only be available when the browser is on a matching domain - preventing credential exposure on the wrong site.

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  const anchorClient = new Anchorbrowser({
    apiKey: process.env.ANCHORBROWSER_API_KEY
  });

  const response = await anchorClient.agent.task(
    'Login to LinkedIn, then login to Gmail and check my inbox',
    {
      taskOptions: {
        url: 'https://linkedin.com',
        agent: 'anthropic-cua',
        secretValues: {
          // Only available on linkedin.com
          '*.linkedin.com': {
            LINKEDIN_EMAIL: process.env.LINKEDIN_EMAIL,
            LINKEDIN_PASSWORD: process.env.LINKEDIN_PASSWORD
          },
          // Only available on google.com
          '*.google.com': {
            GOOGLE_EMAIL: process.env.GOOGLE_EMAIL,
            GOOGLE_PASSWORD: process.env.GOOGLE_PASSWORD
          }
        }
      }
    }
  );

  console.log(response);
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchor_client = Anchorbrowser(api_key=os.environ.get("ANCHORBROWSER_API_KEY"))

  response = anchor_client.agent.task(
      'Login to LinkedIn, then login to Gmail and check my inbox',
      task_options={
          'url': 'https://linkedin.com',
          'agent': 'anthropic-cua',
          'secret_values': {
              # Only available on linkedin.com
              '*.linkedin.com': {
                  'LINKEDIN_EMAIL': os.environ.get('LINKEDIN_EMAIL'),
                  'LINKEDIN_PASSWORD': os.environ.get('LINKEDIN_PASSWORD')
              },
              # Only available on google.com
              '*.google.com': {
                  'GOOGLE_EMAIL': os.environ.get('GOOGLE_EMAIL'),
                  'GOOGLE_PASSWORD': os.environ.get('GOOGLE_PASSWORD')
              }
          }
      }
  )

  print(response)
  ```
</CodeGroup>

### Domain Pattern Examples

| Pattern                | Matches                                  |
| ---------------------- | ---------------------------------------- |
| `*.linkedin.com`       | `www.linkedin.com`, `login.linkedin.com` |
| `linkedin.com`         | `linkedin.com`, `www.linkedin.com`       |
| `https://*.google.com` | Only HTTPS Google subdomains             |
| `*`                    | All domains (use sparingly)              |

<Warning>
  Domain-scoped secrets are only available when the browser URL matches the pattern. If the agent navigates to a different domain, those secrets won't be accessible.
</Warning>

## TOTP / Two-Factor Authentication

Secret values support automatic TOTP code generation for 2FA. Use the `bu_2fa_code` suffix for your TOTP secret key:

<CodeGroup>
  ```javascript node.js theme={null}
  const response = await anchorClient.agent.task(
    'Login to the app and complete 2FA verification',
    {
      taskOptions: {
        url: 'https://secure-app.example.com/login',
        secretValues: {
          EMAIL: process.env.APP_EMAIL,
          PASSWORD: process.env.APP_PASSWORD,
          // TOTP secret - generates a fresh 6-digit code automatically
          APP_2FA_bu_2fa_code: process.env.APP_TOTP_SECRET
        }
      }
    }
  );
  ```

  ```python python theme={null}
  response = anchor_client.agent.task(
      'Login to the app and complete 2FA verification',
      task_options={
          'url': 'https://secure-app.example.com/login',
          'secret_values': {
              'EMAIL': os.environ.get('APP_EMAIL'),
              'PASSWORD': os.environ.get('APP_PASSWORD'),
              # TOTP secret - generates a fresh 6-digit code automatically
              'APP_2FA_bu_2fa_code': os.environ.get('APP_TOTP_SECRET')
          }
      }
  )
  ```
</CodeGroup>

## Best Practices

<CardGroup>
  <Card title="Use Environment Variables" icon="leaf">
    Never hardcode secrets in your code. Always load from environment variables or a secrets manager.
  </Card>

  <Card title="Scope to Domains" icon="lock">
    Use domain-scoped secrets for multi-site tasks to prevent credential leakage.
  </Card>

  <Card title="Meaningful Key Names" icon="tag">
    Use clear, descriptive key names like `LINKEDIN_PASSWORD` instead of `PASS1`.
  </Card>

  <Card title="Minimal Exposure" icon="eye-slash">
    Only include secrets that the task actually needs.
  </Card>
</CardGroup>

## Security Guarantees

| Guarantee                 | Description                                               |
| ------------------------- | --------------------------------------------------------- |
| **Never logged**          | Secret values are excluded from all logs and telemetry    |
| **Never sent to AI**      | Real values are never visible to the AI model             |
| **Type-time replacement** | Secrets are only used at the moment of typing             |
| **Domain isolation**      | Domain-scoped secrets are only available on matching URLs |
| **No storage**            | Secrets are processed in-memory and never persisted       |


# Authenticated Applications (Early Availability)
Source: https://docs.anchorbrowser.io/essentials/authenticated-applications

Define target websites, configure supported login methods (auth flows), let end-users authenticate via an [Embeddable UI](/essentials/embedding-identity-ui), and create pre-authenticated browser sessions to those websites.

<Warning>
  This feature is currently in **Early Availability**. Contact [**support**](mailto:support@anchorbrowser.io) to enable this feature.
</Warning>

<Steps>
  <Step title="Create an Application">
    <CodeGroup>
      ```javascript node.js theme={null}
      import Anchorbrowser from 'anchorbrowser';

      const anchorClient = new Anchorbrowser();

      // Create an application for a target website
      const app = await anchorClient.applications.create({
        name: 'My LinkedIn User',
        source: 'linkedin.com'
      });

      console.log(app.id);
      ```

      ```python python theme={null}
      from anchorbrowser import Anchorbrowser

      anchor_client = Anchorbrowser()

      # Create an application for a target website
      app = anchor_client.applications.create(
          name="My LinkedIn User",
          source="linkedin.com"
      )

      print(app.id)
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.anchorbrowser.io/v1/applications" \
        -H "anchor-api-key: YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{"name": "My LinkedIn User", "source": "linkedin.com"}'
      ```
    </CodeGroup>
  </Step>

  <Step title="Configure Auth Flow for the Application">
    Applications support multiple authentication flows: `username_password`, `authenticator`, and `custom`.

    <CodeGroup>
      ```javascript node.js theme={null}
      await anchorClient.applications.authFlows.create(app.id, {
        name: 'Email Login with authenticator',
        methods: ['username_password', 'authenticator']
      });
      ```

      ```python python theme={null}
      anchor_client.applications.auth_flows.create(
          application_id=app.id,
          name="Email Login with authenticator",
          methods=["username_password", "authenticator"]
      )
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.anchorbrowser.io/v1/applications/{app_id}/auth-flows" \
        -H "anchor-api-key: YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{"name": "Email Login with authenticator", "methods": ["username_password", "authenticator"]}'
      ```
    </CodeGroup>
  </Step>

  <Step title="Create Identity">
    Create an identity with credentials for the application.

    <CodeGroup>
      ```javascript node.js theme={null}
      const identity = await anchorClient.identities.create({
        source: 'https://linkedin.com',
        name: 'John Doe',
        credentials: [{
          type: 'username_password',
          username: 'john@example.com',
          password: 'secret'
        }]
      });

      console.log(identity.id);
      ```

      ```python python theme={null}
      identity = anchor_client.identities.create(
          source="https://linkedin.com",
          name="John Doe",
          credentials=[{
              "type": "username_password",
              "username": "john@example.com",
              "password": "secret"
          }]
      )

      print(identity.id)
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.anchorbrowser.io/v1/identities" \
        -H "anchor-api-key: YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "source": "https://linkedin.com",
          "name": "John Doe",
          "credentials": [{
            "type": "username_password",
            "username": "john@example.com",
            "password": "secret"
          }]
        }'
      ```
    </CodeGroup>

    <Tip>
      For end-user self-service authentication, use the [Embeddable Identity UI](/essentials/embedding-identity-ui).
    </Tip>
  </Step>

  <Step title="Create Authenticated Sessions">
    Use the identity ID to create an authenticated browser session.

    <CodeGroup>
      ```javascript node.js theme={null}
      import Anchorbrowser from 'anchorbrowser';

      const anchorClient = new Anchorbrowser();
      const identityId = "your-identity-id";
      const session = await anchorClient.sessions.create({
          // Recommended settings for authenticated sessions.
          session: {
              proxy: {
                  active: true,
              }
          },
          browser: {
              captcha_solver: {
                  active: true,
              },
              extra_stealth: {
                  active: true,
              }
          },

          // Identity to authenticate with.
          identities: [{ id: identityId }]
      });

      console.log(session.data.id);
      ```

      ```python python theme={null}
      from anchorbrowser import Anchorbrowser

      anchor_client = Anchorbrowser()
      identity_id = "your-identity-id"
      session = anchor_client.sessions.create(
          # Recommended settings for authenticated sessions.
          session={
              "proxy": {
                  "active": True,
              }
          },
          browser={
              "captcha_solver": {
                  "active": True,
              },
              "extra_stealth": {
                  "active": True,
              }
          },

          # Identity to authenticate with.
          identities=[{"id": identity_id}]
      )

      print(session.data.id)
      ```
    </CodeGroup>
  </Step>
</Steps>

## Related

<CardGroup>
  <Card title="Embedding End-User Authentication UI" icon="window" href="/essentials/embedding-identity-ui">
    Embed the authentication flow in your app
  </Card>

  <Card title="Browser Profiles" icon="fingerprint" href="/essentials/authentication-and-identity">
    Alternative approach using browser profiles
  </Card>

  <Card title="API Reference" icon="code" href="/api-reference/applications-early-availability/">
    Applications and Identities endpoints
  </Card>
</CardGroup>


# Browser Profiles (Authenticated sessions)
Source: https://docs.anchorbrowser.io/essentials/authentication-and-identity



Anchor allows you to save an existing browser state as "profiles" for use in future browser sessions. This feature enables users to:

* Store authenticated sessions and identities, allowing to stay logged in to websites
* Improve overall speed and performance

The following guide explains how to create and use Identity Profiles in Anchor Browser.

## Quick start - Create and use a profile

<Expandable title="Via SDK">
  <Steps>
    <Step title="Start a session with a new profile">
      Create a session via SDK, Make sure to configure the new profile to persist.

      <CodeGroup>
        ```JavaScript node.js theme={null}
        import Anchorbrowser from "anchorbrowser";

        (async () => {
         const anchorClient = new Anchorbrowser()
         const session = await anchorClient.sessions.create({
            browser: {
                profile: {
                    name: 'new-profile',
                    persist: true
                    }
                }
            })
         console.log(session)
        })();
        ```

        ```python python theme={null}
        from anchorbrowser import Anchorbrowser
        import os

        anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
        session = anchor_client.sessions.create(browser={
            "profile": {
                "name": "new-profile",
                "persist": True
            }
        })
        print(session)
        ```
      </CodeGroup>
    </Step>

    <Step title="Authenticate Once">
      Authenticate to the target service and create a browser context with the required cookies and session data.

      <CodeGroup>
        ```JavaScript node.js theme={null}
        import Anchorbrowser from "anchorbrowser";

        (async () => {
         const anchorClient = new Anchorbrowser()
         const session = await anchorClient.sessions.create({
            browser: {
                profile: {
                    name: 'new-profile',
                    persist: true
                    }
                }
            })

         const sessionId = session.data.id;

         // Navigate to the login page
         await anchorClient.sessions.goto(sessionId, {
            url: 'https://example.com/login'
         })

         // Fill in your login credentials
         await anchorClient.sessions.mouse.click(sessionId, { x: 100, y: 200 })
         await anchorClient.sessions.keyboard.type(sessionId, { text: 'your-username' })

         await anchorClient.sessions.mouse.click(sessionId, { x: 100, y: 250 })
         await anchorClient.sessions.keyboard.type(sessionId, { text: 'your-password' })

         // Submit the login form
         await anchorClient.sessions.mouse.click(sessionId, { x: 100, y: 300 })

         console.log('Authentication completed. Profile will be saved when session ends.')
        })();
        ```

        ```python python theme={null}
        from anchorbrowser import Anchorbrowser
        import os

        anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
        session = anchor_client.sessions.create(browser={
            "profile": {
                "name": "new-profile",
                "persist": True
            }
        })

        session_id = session["data"]["id"]

        # Navigate to the login page
        anchor_client.sessions.goto(session_id, url="https://example.com/login")

        # Fill in your login credentials
        anchor_client.sessions.mouse.click(session_id, x=100, y=200)
        anchor_client.sessions.keyboard.type(session_id, text="your-username")

        anchor_client.sessions.mouse.click(session_id, x=100, y=250)
        anchor_client.sessions.keyboard.type(session_id, text="your-password")

        # Submit the login form
        anchor_client.sessions.mouse.click(session_id, x=100, y=300)

        print("Authentication completed. Profile will be saved when session ends.")
        ```
      </CodeGroup>
    </Step>

    <Step title="Save Profile">
      End the session. The profile will be automatically saved since you set `persist: true` when creating the session.

      <CodeGroup>
        ```JavaScript node.js theme={null}
        import Anchorbrowser from "anchorbrowser";

        (async () => {
         const anchorClient = new Anchorbrowser()

         // After completing authentication, end the session to save the profile
         await anchorClient.sessions.delete(sessionId)

         console.log('Session ended. Profile "new-profile" has been saved.')
        })();
        ```

        ```python python theme={null}
        from anchorbrowser import Anchorbrowser
        import os

        anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

        # After completing authentication, end the session to save the profile
        anchor_client.sessions.delete(session_id)

        print('Session ended. Profile "new-profile" has been saved.')
        ```
      </CodeGroup>
    </Step>

    <Step title="Use the profile in other sessions">
      Now, when creating a new session pass the `profile` parameter with the name of the profile you created to load the saved browser context.

      <CodeGroup>
        ```JavaScript node.js theme={null}
        import Anchorbrowser from "anchorbrowser";

        (async () => {
         const anchorClient = new Anchorbrowser()
         const session = await anchorClient.sessions.create({
            browser: {
                profile: {
                    name: 'new-profile'
                }
            }
            })
         console.log(session)
        })();
        ```

        ```python python theme={null}
        from anchorbrowser import Anchorbrowser
        import os

        anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
        session = anchor_client.sessions.create(browser={
            "profile": {
                "name": "new-profile"
            }
        })
        print(session)
        ```
      </CodeGroup>
    </Step>
  </Steps>
</Expandable>

<Expandable title="Via UI">
  <Steps>
    <Step title="Start a session with a new profile">
      Through the Anchor playground, create a profile on the configuration area. Then, click to start a session.

      <img alt="Create profile in playground" />
    </Step>

    <Step title="Authenticate Once">
      Authenticate to the target service using the playground to create a browser context with the required cookies and session data.
    </Step>

    <Step title="Save Profile">
      Save the profile using the 'Save Profile' button in the Anchor Browser Playground.
      <Note>This operation will end the current playground browser session</Note>

      <img alt="Save profile in playground" />

      Then approve it in the popup window 'Yes, Save and Terminate'

      <img alt="Confirm profile save" />
    </Step>

    <Step title="Use the profile in other sessions">
      Select the saved profile from the dropdown in the playground configuration area when starting a new session.

      <img alt="Reuse saved profile" />
    </Step>
  </Steps>
</Expandable>


# Embedding End-User Authentication UI (Early Availability)
Source: https://docs.anchorbrowser.io/essentials/embedding-identity-ui

Anchor provides an embeddable identity creation flow that allows end-users to authenticate to third-party websites directly from your application, enabling [authenticated browser sessions](/essentials/authenticated-applications).

<Warning>
  This feature is currently in **Early Availability**. Contact [**support**](mailto:support@anchorbrowser.io) to enable this feature.
</Warning>

## Prerequisites

Before integrating the embedded identity flow, ensure the following are configured:

1. **[Create an Application](/essentials/authenticated-applications)** - Define the target website users will authenticate to via the Anchor Dashboard or API
2. **[Configure Authentication Flows](/essentials/authenticated-applications#configure-auth-flow-for-the-application)** - Set up the supported login methods.

## Overview

<Steps>
  <Step title="Generate a Token">
    Create a one-time token that authorizes the identity creation flow.

    <CodeGroup>
      ```javascript node.js theme={null}
      import Anchorbrowser from 'anchorbrowser';

      const anchorClient = new Anchorbrowser();

      // Generate a token for identity creation
      const tokenResponse = await anchorClient.applications.createIdentityToken(
          'your-application-id',
          { callbackUrl: 'https://your-app.com/identity-callback' }
      );

      console.log(tokenResponse.token);
      // Use this token to redirect the user
      ```

      ```python python theme={null}
      from anchorbrowser import Anchorbrowser

      anchor_client = Anchorbrowser()

      # Generate a token for identity creation
      token_response = anchor_client.applications.create_identity_token(
          application_id="your-application-id",
          callback_url="https://your-app.com/identity-callback"
      )

      print(token_response.token)
      # Use this token to redirect the user
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.anchorbrowser.io/v1/applications/{application_id}/tokens" \
        -H "anchor-api-key: YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "callbackUrl": "https://your-app.com/identity-callback"
        }'
      ```
    </CodeGroup>

    <Warning>
      The `callbackUrl` must use HTTPS. Store the token securely and use it immediately - tokens are single-use and expire
      after 15 minutes.
    </Warning>
  </Step>

  <Step title="Redirect User to Identity Creation">
    Redirect the user to the Anchor identity creation page with the generated token:

    ```
    https://app.anchorbrowser.io/identity/create?token={token}
    ```

    <CodeGroup>
      ```javascript Frontend (React) theme={null}
      function CreateIdentityButton({ token }) {
        const handleClick = () => {
          window.location.href = `https://app.anchorbrowser.io/identity/create?token=${token}`;
        };

        return <button onClick={handleClick}>Connect Your Account</button>;
      }
      ```
    </CodeGroup>

    The user will be guided through the authentication process for the target website configured in the application.
  </Step>

  <Step title="Handle the Callback">
    After the user successfully creates an identity, Anchor redirects them to the `callbackUrl` with the identity ID:

    ```
    https://your-app.com/identity-callback?identityId={identity_id}
    ```

    <CodeGroup>
      ```javascript Express.js theme={null}
      app.get('/identity-callback', async (req, res) => {
        const { identityId } = req.query;

        if (!identityId) {
          return res.status(400).send('Missing identity ID');
        }

        // Store the mapping between the user and the Anchor identity
        await saveUserIdentityMapping(req.user.id, identityId);

        // Optionally, update the identity with an external user ID

        res.redirect('/dashboard?connected=true');
      });
      ```

      ```python Flask theme={null}
      @app.route('/identity-callback')
      def identity_callback():
          identity_id = request.args.get('identityId')

          if not identity_id:
              return 'Missing identity ID', 400

          # Store the mapping between the user and the Anchor identity
          save_user_identity_mapping(current_user.id, identity_id)

          # Optionally, update the identity with an external user ID (See next step)

          return redirect('/dashboard?connected=true')
      ```
    </CodeGroup>
  </Step>

  <Step title="Update Identity Metadata (Optional)">
    Update the identity with additional metadata to maintain a mapping between users and their Anchor identities:

    <CodeGroup>
      ```javascript node.js theme={null}
      import Anchorbrowser from 'anchorbrowser';

      const anchorClient = new Anchorbrowser();

      // Update identity with external user ID
      const updatedIdentity = await anchorClient.identities.update('your-identity-id', {
        name: 'User Display Name',
        metadata: {
          externalUserId: 'your-user-id-123',
          plan: 'premium',
          connectedAt: new Date().toISOString(),
        },
      });
      ```

      ```python python theme={null}
      from anchorbrowser import Anchorbrowser

      anchor_client = Anchorbrowser()

      # Update identity with external user ID
      updated_identity = anchor_client.identities.update(
          identity_id='your-identity-id',
          name="User Display Name",
          metadata={
              "externalUserId": "your-user-id-123",
              "plan": "premium",
              "connectedAt": datetime.now().isoformat()
          }
      )
      ```

      ```bash cURL theme={null}
      curl -X PUT "https://api.anchorbrowser.io/v1/identities/{identity_id}" \
        -H "anchor-api-key: YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "name": "User Display Name",
          "metadata": {
            "externalUserId": "your-user-id-123",
            "plan": "premium"
          }
        }'
      ```
    </CodeGroup>
  </Step>

  <Step title="Create Authenticated Sessions">
    Once an identity ID is available, use it to create authenticated browser sessions:

    <CodeGroup>
      ```javascript node.js theme={null}
      import Anchorbrowser from 'anchorbrowser';

      const anchorClient = new Anchorbrowser();
      const identityId = "your-identity-id";
      const session = await anchorClient.sessions.create({
          // Recommended settings for authenticated sessions.
          session: {
              proxy: {
                  active: true,
              }
          },
          browser: {
              captcha_solver: {
                  active: true,
              },
              extra_stealth: {
                  active: true,
              }
          },

          // Identity to authenticate with.
          identities: [{ id: identityId }]
      });

      console.log(session.data.id);
      ```

      ```python python theme={null}
      from anchorbrowser import Anchorbrowser

      anchor_client = Anchorbrowser()
      identity_id = "your-identity-id"
      session = anchor_client.sessions.create(
          # Recommended settings for authenticated sessions.
          session={
              "proxy": {
                  "active": True,
              }
          },
          browser={
              "captcha_solver": {
                  "active": True,
              },
              "extra_stealth": {
                  "active": True,
              }
          },

          # Identity to authenticate with.
          identities=[{"id": identity_id}]
      )

      print(session.data.id)
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.anchorbrowser.io/v1/sessions" \
        -H "anchor-api-key: YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
        "browser": {
          "captcha_solver": {
            "active": true
          },
          "extra_stealth": {
            "active": true
          }
        },
        "session": {
          "proxy": {
            "active": true
          }
        },
        "identities": [
          {
            "id": "your-identity-id"
          }
        ]
      }'
      ```
    </CodeGroup>

    The browser session will automatically be authenticated to the target website using the stored identity.
  </Step>
</Steps>

## Complete Integration Example

Here's a complete example showing the full flow:

<CodeGroup>
  ```javascript node.js (Express) theme={null}
  import express from 'express';
  import Anchorbrowser from 'anchorbrowser';

  const app = express();
  const anchorClient = new Anchorbrowser();

  const APPLICATION_ID = 'your-application-id';

  // Step 1: Initiate identity creation
  app.post('/api/connect-account', async (req, res) => {
    const userId = req.user.id;

    // Generate token with callback URL
    const tokenResponse = await anchorClient.applications.createIdentityToken(APPLICATION_ID, {
      callbackUrl: `https://your-app.com/api/identity-callback`,
    });

    // Store token-to-user mapping for callback verification
    await storeTokenMapping(tokenResponse.tokenHash, userId);

    // Return redirect URL to frontend
    res.json({
      redirectUrl: `https://app.anchorbrowser.io/identity/create?token=${tokenResponse.token}`,
    });
  });

  // Step 2: Handle callback after identity creation
  app.get('/api/identity-callback', async (req, res) => {
    const { identityId } = req.query;

    // Save identity mapping
    await saveIdentityMapping(req.user.id, identityId);

    // Update identity with external reference
    await anchorClient.identities.update(identityId, {
      metadata: { externalUserId: req.user.id },
    });

    res.redirect('/dashboard?connected=true');
  });

  // Step 3: Use identity in browser sessions
  app.post('/api/run-automation', async (req, res) => {
    const identityId = await getUserIdentity(req.user.id);

    const session = await anchorClient.sessions.create({
      browser: {
        identities: [{ id: identityId }],
      },
    });

    // Run your automation with the authenticated session
    // ...

    res.json({ sessionId: session.id });
  });
  ```

  ```python python (Flask) theme={null}
  from flask import Flask, request, redirect, jsonify
  from anchorbrowser import Anchorbrowser

  app = Flask(__name__)
  anchor_client = Anchorbrowser()

  APPLICATION_ID = "your-application-id"

  # Step 1: Initiate identity creation
  @app.route("/api/connect-account", methods=["POST"])
  def connect_account():
      user_id = request.user.id

      # Generate token with callback URL
      token_response = anchor_client.applications.identities.tokens.create(
          application_id=APPLICATION_ID,
          callback_url="https://your-app.com/api/identity-callback"
      )

      # Store token-to-user mapping for callback verification
      store_token_mapping(token_response.token_hash, user_id)

      # Return redirect URL to frontend
      return jsonify({
          "redirectUrl": f"https://app.anchorbrowser.io/identity/create?token={token_response.token}"
      })

  # Step 2: Handle callback after identity creation
  @app.route("/api/identity-callback")
  def identity_callback():
      identity_id = request.args.get("identityId")

      # Save identity mapping
      save_identity_mapping(request.user.id, identity_id)

      # Update identity with external reference
      anchor_client.identities.update(
          identity_id=identity_id,
          metadata={"externalUserId": request.user.id}
      )

      return redirect("/dashboard?connected=true")

  # Step 3: Use identity in browser sessions
  @app.route("/api/run-automation", methods=["POST"])
  def run_automation():
      identity_id = get_user_identity(request.user.id)

      session = anchor_client.sessions.create(
          # Recommended settings for authenticated sessions.
          session={
              "proxy": {
                  "active": True,
              }
          },
          browser={
              "captcha_solver": {
                  "active": True,
              },
              "extra_stealth": {
                  "active": True,
              }
          },

          # Identity to authenticate with.
          identities=[{"id": identity_id}]
      )

      # Run your automation with the authenticated session
      # ...

      return jsonify({"sessionId": session.id})
  ```
</CodeGroup>

## Best Practices

<CardGroup>
  <Card title="Secure Token Handling" icon="lock">
    Generate tokens server-side and never expose your API key to the frontend. Tokens are single-use and should be used immediately.
  </Card>

  <Card title="Store Identity Mappings" icon="database">
    Maintain a mapping between your users and their Anchor identity IDs in your database for future session creation.
  </Card>

  <Card title="Use Metadata" icon="tags">
    Store your external user ID in the identity metadata to easily correlate identities with your users.
  </Card>

  <Card title="Handle Errors" icon="triangle-exclamation">
    Implement proper error handling for cases where identity creation fails or the user cancels the flow.
  </Card>
</CardGroup>

## Related Resources

* [Authenticated Applications](/essentials/authenticated-applications) - Define target websites, authentication flows, and create pre-authenticated browser sessions
* [Browser Profiles](/essentials/authentication-and-identity) - Alternative approach using browser profiles


# Session Recording
Source: https://docs.anchorbrowser.io/essentials/recording

Record browser sessions for debugging, analysis, and documentation

## Overview

Anchor Browser provides built-in session recording that allows you to capture and review browser sessions. This feature is invaluable for debugging automation workflows, analyzing user behavior, and creating documentation.

## How It Works

Anchor Browser automatically records browser sessions and creates an MP4 video file that captures the complete visual experience.
Recordings are accessible both through our API and the web UI (see below).

<Expandable title="SDK Usage">
  # SDK Usage

  ## Record a Session

  Recording is enabled by default when creating a session.
  Start a session using the [SDK](/quickstart/use-via-sdk), you can enable recording by setting:
  `recording` -> `active` -> `true` in the request body.

  <CodeGroup>
    ```javascript node.js theme={null}
    import AnchorBrowser from 'anchorbrowser';

    (async () => {
      const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
      
      const response = await anchorClient.sessions.create({
        session: {
          recording: {
            active: true   // Enable recording (default)
          }
        }
      });
      
      const sessionId = response.data.id
      console.log("Session created:", response.data);
    })().catch(console.error);
    ```

    ```python python theme={null}
    import os
    from anchorbrowser import Anchorbrowser

    anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

    response = anchor_client.sessions.create(
        session={
            "recording": {
                "active": True  # Enable recording (default)
            }
        }
    )

    session_id = response.data.id
    print("Session created:", session_id)
    ```
  </CodeGroup>

  ## Get Session Recordings

  Retrieve recordings for a specific session:

  <CodeGroup>
    ```javascript node.js theme={null}
    import AnchorBrowser from 'anchorbrowser';

    (async () => {
      const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
      
      const recordings = await anchorClient.sessions.recordings.list(sessionId);
      console.log("Recordings:", recordings.data);
    })().catch(console.error);
    ```

    ```python python theme={null}
    import os
    from anchorbrowser import Anchorbrowser

    anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

    recordings = anchor_client.sessions.recordings.list(session_id)
    print("Recordings:", recordings.data)
    ```
  </CodeGroup>

  ## Download Recording

  Download a specific recording file:

  <CodeGroup>
    ```javascript node.js theme={null}
      import AnchorBrowser from 'anchorbrowser';
      import { writeFile } from 'node:fs/promises';
      
      (async () => {
        const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
        // const sessionId = 'your-session-id'; // Replace with actual session ID
        
        const recording = await anchorClient.sessions.recordings.primary.get(sessionId);
        
        // Save to file
        const buffer = await recording.arrayBuffer();
        await writeFile(`recording-${sessionId}.mp4`, Buffer.from(buffer));
        
        console.log(`Recording saved as recording-${sessionId}.mp4`);
      })().catch(console.error);
    ```

    ```python python theme={null}
      import os
      from anchorbrowser import Anchorbrowser

      anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
      session_id = "your-session-id"  # Replace with actual session ID

      recording = anchor_client.sessions.recordings.primary.get(session_id)

      # Save to file
      with open(f"recording-{session_id}.mp4", "wb") as f:
          for chunk in recording.iter_bytes(chunk_size=8192):
              f.write(chunk)

      print(f"Recording saved as recording-{session_id}.mp4")
    ```
  </CodeGroup>
</Expandable>

<Expandable title="Web UI Usage">
  # Web UI Usage

  ## Create a Session

  In order to create a session through the UI with recording enabled use the [playground](https://app.anchorbrowser.io/playground), it will be recorded by default.

  <img alt="Starting a session to be recorded in the playground" />

  ## Session Recordings

  The Session History dashboard shows all sessions. Each session has a link to its recording.

  <Warning>
    If a session is still running, the link in the session history page will take you to the session's live view instead of the recording. Once the session ends, the link will point to the recording.
  </Warning>

  <img alt="Session history dashboard showing list of sessions" />

  ## Recording Playback

  When you click on a session recording, the playback interface will be opened.
  You can use it to view the recording, navigate through it, and download it as MP4 file.

  <img alt="Recording playback interface with video controls" />
</Expandable>


# Extra Stealth Mode
Source: https://docs.anchorbrowser.io/essentials/stealth

Advanced anti-detection and browser fingerprinting protection for automated browsing

<Note>
  Extra Stealth is available on our **Growth tier**.

  [Upgrade Now](https://app.anchorbrowser.io/billing)
</Note>

Anchor Browser provides built-in stealth capabilities that help avoid detection by anti-bot systems and website fingerprinting. These features enable automated browsing that mimics human behavior and bypasses common detection mechanisms.

## What is Extra Stealth Mode?

Extra Stealth Mode leverages a specialized Chrome browser environment that provides:

* 🔒 **Advanced Anti-Detection** - Bypass sophisticated bot detection systems and CAPTCHAs
* 🛡️ **Automation Consistency** - Maintain consistent access without getting blocked
* 👤 **Human-Like Behavior** - Mimic real user patterns to avoid suspicion

<Note>
  Alternative Cloudflare-verified access to webpages is available through our [Cloudflare Web Bot Auth Integration](/advanced/cloudflare-web-bot-auth).
</Note>

## Quick start - Enable stealth features

<Steps>
  <Step title="Create a session with extra stealth enabled">
    Create a browser session with extra stealth features enabled using the SDK:

    <Warning>
      Extra stealth mode requires proxy configuration to be active. **If proxy is disabled, extra stealth will be automatically disabled** by the system.

      Read more about [Proxy Configuration](/advanced/proxy)
    </Warning>

    <CodeGroup>
      ```JavaScript node.js theme={null}
      import Anchorbrowser from "anchorbrowser";

      const anchorClient = new Anchorbrowser()
      const session = await anchorClient.sessions.create({
          browser: {
              extra_stealth: {
                  active: true
              }
          },
          session: {
              proxy: {
                  active: true
              }
          }
      });

      console.log(session);
      ```

      ```python python theme={null}
      from anchorbrowser import Anchorbrowser
      import os

      anchorClient = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
      session = anchorClient.sessions.create(
          browser={
              "extra_stealth": {
                  "active": True
              }
          },
          session={
              "proxy": {
                  "active": True
              }
          }
      )
      print(session)
      ```
    </CodeGroup>
  </Step>

  <Step title="Use the session for automated browsing">
    Once your stealth session is created, you can use it for automated browsing that bypasses common detection mechanisms:

    <CodeGroup>
      ```JavaScript node.js theme={null}
      import Anchorbrowser from "anchorbrowser";

      const anchorClient = new Anchorbrowser()
       
      // Create stealth session
      const session = await anchorClient.sessions.create({
          browser: {
              extra_stealth: {
                  active: true
              }
          },
          session: {
              proxy: {
                  active: true
              }
          }
       })

      // Use the session for automated tasks
      const result = await anchorClient.agent.task(
          "Navigate to a website and check if I'm detected as a bot",
          {
              sessionId: session.data.id
          }
      );

      console.log(result);
      ```

      ```python python theme={null}
      from anchorbrowser import Anchorbrowser
      import os

      anchorClient = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

      # Create stealth session
      session = anchorClient.sessions.create(
          browser={
              "extra_stealth": {
                  "active": True
              }
          },
          session={
              "proxy": {
                  "active": True
              }
          }
      )

      # Use the session for automated tasks
      result = anchorClient.agent.task(
          session_options=session,
          prompt="Navigate to a website and check if I'm detected as a bot"
      )

      print(result)
      ```
    </CodeGroup>
  </Step>
</Steps>

## Usage with Profiles

Use stealth mode with saved browser profiles for persistent authenticated sessions:

<CodeGroup>
  ```JavaScript node.js theme={null}
  import Anchorbrowser from "anchorbrowser";

  const anchorClient = new Anchorbrowser()
  const session = await anchorClient.sessions.create({
      browser: {
          extra_stealth: {
              active: true
          },
          profile: {
              name: 'stealth-profile',
              persist: true   // Only on Profile Creation
          }
      },
      session: {
          proxy: {
              active: true
          }
      }
  })
  console.log(session)

  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchorClient = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
  session = anchorClient.sessions.create(
      browser={
          "extra_stealth": {
              "active": True
          },
          "profile": {
              "name": "stealth-profile",
              "persist": true   # Only on Profile Creation
          }
      },
      session={
          "proxy": {
              "active": True
          }
      }
  )
  print(session)
  ```
</CodeGroup>

## Enabling Console Logs

<Warning>
  When extra stealth mode is enabled, `page.on('console')` events are **disabled by default** to prevent detection. If you need to capture console output, you must explicitly enable it.
</Warning>

To receive console log events while using extra stealth, enable `console_logs` in your session configuration:

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from "anchorbrowser";

  const anchorClient = new Anchorbrowser();

  const session = await anchorClient.sessions.create({
    browser: {
      extra_stealth: { active: true },
      console_logs: { active: true }
    },
    session: {
      proxy: { active: true }
    }
  });

  // Connect to the browser
  const browser = await anchorClient.browser.connect(session.data.id);
  const context = browser.contexts()[0];
  const page = context.pages()[0];

  // Now page.on('console') will work
  page.on('console', (msg) => {
    console.log(`[${msg.type()}] ${msg.text()}`);
  });

  await page.goto("https://example.com");
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  session = anchor_client.sessions.create(
      browser={
          "extra_stealth": {"active": True},
          "console_logs": {"active": True}
      },
      session={
          "proxy": {"active": True}
      }
  )

  # Connect to the browser
  with anchor_client.browser.connect(session.data.id) as browser:
      context = browser.contexts[0]
      page = context.pages[0]

      # Now page.on('console') will work
      def handle_console(msg):
          print(f"[{msg.type}] {msg.text}")

      page.on("console", handle_console)

      page.goto("https://example.com")
  ```
</CodeGroup>

## Catching Captcha Events

When using stealth mode with captcha solving enabled, you can listen to captcha lifecycle events via CDP (Chrome DevTools Protocol). This allows you to track when captchas are detected, solved, or failed.

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from "anchorbrowser";

  const anchorClient = new Anchorbrowser();

  // Create a session with extra stealth and captcha solving enabled
  const session = await anchorClient.sessions.create({
    browser: {
      extra_stealth: { active: true },
      captcha_solver: { active: true }
    },
    session: {
      proxy: { active: true }
    }
  });

  // Connect to the browser
  const browser = await anchorClient.browser.connect(session.data.id);
  const context = browser.contexts()[0];
  const page = context.pages()[0];

  // Create CDP session and listen to captcha events
  const client = await context.newCDPSession(page);

  client.on('Captcha.lifecycle', (event) => {
    if (event.name === 'detected') {
      console.log(`${event.captchaType} captcha detected on ${event.url}`);
    }
    
    if (event.name === 'solved') {
      console.log(`Captcha solved in ${event.timeToSolve}ms`);
    }

    if (event.name === 'failed') {
      console.log(`Captcha failed: ${event.error}`);
    }
  });

  // Navigate to a page with captcha
  await page.goto("https://example.com");
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

  # Create a session with extra stealth and captcha solving enabled
  session = anchor_client.sessions.create(
      browser={
          "extra_stealth": {"active": True},
          "captcha_solver": {"active": True}
      },
      session={
          "proxy": {"active": True}
      }
  )

  # Connect to the browser
  with anchor_client.browser.connect(session.data.id) as browser:
      context = browser.contexts[0]
      page = context.pages[0]

      # Create CDP session and listen to captcha events
      client = context.new_cdp_session(page)

      def handle_captcha_event(event):
          if event["name"] == "detected":
              print(f"{event['captchaType']} captcha detected on {event['url']}")
          
          if event["name"] == "solved":
              print(f"Captcha solved in {event['timeToSolve']}ms")
          
          if event["name"] == "failed":
              print(f"Captcha failed: {event['error']}")

      client.on("Captcha.lifecycle", handle_captcha_event)

      # Navigate to a page with captcha
      page.goto("https://example.com")
  ```
</CodeGroup>

### Event Types

| Event Name | Description                                   | Properties                      |
| ---------- | --------------------------------------------- | ------------------------------- |
| `detected` | Fired when a captcha is detected on the page  | `captchaType`, `url`            |
| `solved`   | Fired when the captcha is successfully solved | `timeToSolve` (in milliseconds) |
| `failed`   | Fired when captcha solving fails              | `error`                         |


# Tools - Browser Control API
Source: https://docs.anchorbrowser.io/essentials/tool-building



Anchor Browser offers API endpoints (also known as "agentic tools") to simplify the usage of the browser, and enable browser utilization *without any coding*

### Featured tools

* **[Screenshot webpage](/api-reference/tools/screenshot-webpage)**: Get a fully javascript-rendered screenshot of a given webpage.
* **[Get webpage content](/api-reference/tools/get-webpage-content)**: Get an LLM ready, Markdown version of a given webpage.

### Featured AI based tools

* **[Perform task](/api-reference/ai-tools/perform-web-task)**: Use natural language to have the browser autonomously act and perform a task.


# Buyer Intent Discovery
Source: https://docs.anchorbrowser.io/examples/buyer-intent



The following example use-case shows how to find buyer-intent data based on Github stargazers of a Github project named 'Airflow'. A star from a person that works for a significant corporation can be a hint of buying intent in the data pipelines space.

<CodeGroup>
  ```tsx node.js theme={null}
  const result = await anchorClient.agent.task(
    `On the current stargazers list, return the GitHub profile URLs of all users
    that are a part of a well-known company. Then, do this for the first 3 pages
    using the "page" query parameter.
    Return a JSON array result: ["url1", "url2", ...].`,
    {
      taskOptions: {
        url: 'https://github.com/apache/airflow/stargazers?page=1',
      }
    }
  )
  console.log(result);
  ```

  ```python python theme={null}
  result = anchor_client.agent.task(
    '''On the current stargazers list, return the GitHub profile URLs of all users
    that are a part of a well-known company. Then, do this for the first 3 pages
    using the "page" query parameter.
    Return a JSON array result: ["url1", "url2", ...].''',
    task_options={
      'url': 'https://github.com/apache/airflow/stargazers?page=1',
    }
  )
  print(result)
  ```
</CodeGroup>


# Configuration Collection
Source: https://docs.anchorbrowser.io/examples/configuration-collection



The following example shows how to collect configuration data that is not exposed through an API from a SaaS service (Grafana) configuration page.

<CodeGroup>
  ```tsx node.js theme={null}
  const result = await anchorClient.agent.task(
    'Collect the node names and their CPU average %, return in JSON array',
    {
      taskOptions: {
        url: 'https://play.grafana.org/a/grafana-k8s-app/navigation/nodes',
      }
    }
  )
  console.log(result);
  ```

  ```python python theme={null}
  result = anchor_client.agent.task(
    'Collect the node names and their CPU average %, return in JSON array',
    task_options={
      'url': 'https://play.grafana.org/a/grafana-k8s-app/navigation/nodes',
    }
  )
  print(result)
  ```
</CodeGroup>


# Form Filling Automation
Source: https://docs.anchorbrowser.io/examples/form-filling



The following example shows form filling, including the ability to self-complete missing data in the form filling process.

<CodeGroup>
  ```tsx node.js theme={null}
  const result = await anchorClient.agent.task(
    `Go to https://www.wix.com/demone2/nicol-rider, read the resume,
    understand the details, and complete the form at
    https://formspree.io/library/donation/charity-donation-form/preview.html
    as if you were her. Limit the donation to $10.`
  )
  console.log(result);
  ```

  ```python python theme={null}
  result = anchor_client.agent.task(
    '''Go to https://www.wix.com/demone2/nicol-rider, read the resume,
    understand the details, and complete the form at
    https://formspree.io/library/donation/charity-donation-form/preview.html
    as if you were her. Limit the donation to $10.'''
  )
  print(result)
  ```
</CodeGroup>


# Deep Research
Source: https://docs.anchorbrowser.io/examples/research-task



The following example demonstrates how to use Anchor Browser to perform web research tasks.

<CodeGroup>
  ```tsx node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  const anchorClient = new Anchorbrowser()
  const session = await anchorClient.sessions.create()
  const sessionId = session.data?.id

  const result = await anchorClient.agent.task(
    `Find the most recent NBA game played by the Milwaukee Bucks
     and provide the result.`,
    {
      taskOptions: {
        url: 'https://nba.com/',
      },
      sessionId: sessionId,
    }
  )
  console.log(result)

  const author = await anchorClient.agent.task(
    `Find an article discussing the game and provide the author's name.`,
    {
      sessionId: sessionId,
    }
  )
  console.log(author)
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser

  anchor_client = Anchorbrowser()
  session = anchor_client.sessions.create()
  session_id = session.data.id

  result = anchor_client.agent.task(
    '''Find the most recent NBA game played by the Milwaukee Bucks
       and provide the result.''',
    task_options={
      'url': 'https://nba.com/',
    },
    session_id=session_id,
  )
  print(result)

  author = anchor_client.agent.task(
    'Find an article discussing the game and provide the author\'s name.',
    session_id=session_id,
  )
  print(author)
  ```
</CodeGroup>


# 1Password
Source: https://docs.anchorbrowser.io/integrations/1password

Securely inject 1Password secrets into your browser sessions

## Overview

The 1Password integration **enables your AI agent to securely authenticate with services** during browser automation by injecting secrets, credentials, and other sensitive data from your 1Password vaults directly into your Anchor Browser sessions. This gives your AI agent the ability to log into websites, access APIs, and perform authenticated actions **without you needing to hardcode credentials** in your automation scripts.

<Note>
  The actual secret values are **never exposed** to the AI agent, logs, API responses, or any other output
</Note>

## Prerequisites

Before you can use the 1Password integration, you need:

1. **1Password Account**: An active 1Password account with access to the secrets you want to use  in a vault different than “Personal”.
2. **Anchor Browser API Key**: Your Anchor Browser API key for authentication

## Getting a 1Password Service Account Token

1. Log in to your [1Password account](https://my.1password.com/)
2. Navigate to **Developer** → **Directory** → **Service Accounts**
3. Click **Create Service Account**
4. Give your service account a descriptive name (e.g., "Anchor Browser Automation")
5. Grant the service account access to the vaults containing the secrets you need
6. Copy the service account token (starts with `ops_`) - you'll need this for the integration setup

<Warning>
  Store your service account token securely. It provides access to your
  1Password secrets and should be treated like a password.
</Warning>

## Creating a 1Password Integration

### Using the API

Create a 1Password integration using the AnchorBrowser API:

```bash theme={null}
curl -X POST https://api.anchorbrowser.io/v1/integrations \
  -H "anchor-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My 1Password Integration",
    "type": "1PASSWORD",
    "credentials": {
      "type": "serviceAccount",
      "data": {
        "serviceAccount": "ops_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
      }
    }
  }'
```

**Response:**

```json theme={null}
{
  "data": {
    "integration": {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "name": "My 1Password Integration",
      "type": "1PASSWORD",
      "path": "integrations/team-id/550e8400-e29b-41d4-a716-446655440000",
      "createdAt": "2024-01-01T00:00:00.000Z"
    }
  }
}
```

Save the `id` from the response - you'll need it to use the integration in browser sessions.

## Using 1Password Integration in Browser Sessions

Once you've created a 1Password integration, you can use it in your browser sessions to automatically load secrets.

### Load All Secrets

Load all secrets from your 1Password vaults:

```bash theme={null}
curl -X POST https://api.anchorbrowser.io/v1/sessions \
  -H "anchor-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "integrations": [
      {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "type": "1PASSWORD",
        "configuration": {
          "load_mode": "all"
        }
      }
    ]
  }'
```

### Load Specific Secrets

Load only specific secrets using 1Password secret references:

```bash theme={null}
curl -X POST https://api.anchorbrowser.io/v1/sessions \
  -H "anchor-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "integrations": [
      {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "type": "1PASSWORD",
        "configuration": {
          "load_mode": "specific",
          "secrets": [
            "op://Production/Database/username",
            "op://Production/Database/password",
            "op://Production/API Keys/stripe_key"
          ]
        }
      }
    ]
  }'
```

## 1Password Secret Reference Format

1Password uses a specific format for secret references:

```
op://[vault]/[item]/[field]
```

* **vault**: The name of your 1Password vault
* **item**: The name of the item in the vault
* **field**: The specific field within the item

### Examples

```
op://Production/AWS Credentials/access_key_id
op://Development/GitHub/personal_access_token
op://Shared/Stripe/api_key
```

## Accessing Secrets in Your Browser Session

Once loaded, secrets are available as environment variables in your browser session. The environment variable name is derived from the secret reference:

* Secret reference: `op://Production/Database/username`
* Environment variable: `OP_PRODUCTION_DATABASE_USERNAME`

The conversion follows these rules:

1. Remove the `op://` prefix
2. Replace `/` with `_`
3. Convert to uppercase
4. Prefix with `OP_`

<Note>
  **AI Agent Security**: When your AI agent accesses these environment variables, it can use them for authentication with external services, but the actual credential values are never visible in the agent's output, logs, or responses. The credentials are used transparently by the browser environment for authentication purposes only.
</Note>

### Example: Using Secrets in Automation

<CodeGroup>
  ```javascript node.js theme={null}
  (async () => {
    // Create a session with 1Password integration
    const response = await fetch('https://api.anchorbrowser.io/v1/sessions', {
      method: 'POST',
      headers: {
        'anchor-api-key': process.env.ANCHOR_API_KEY,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        integrations: [
          {
            id: integrationId,
            type: '1PASSWORD',
            configuration: {
              load_mode: 'specific',
              secrets: [
                'op://Production/Database/username',
                'op://Production/Database/password'
              ]
            }
          }
        ]
      })
    });


    const sessionData = await response.json();
    console.log(sessionData)

    // Access the secrets in your automation code
    // The secrets are automatically available as environment variables
    // OP_PRODUCTION_DATABASE_USERNAME and OP_PRODUCTION_DATABASE_PASSWORD
    // Your AI agent can use these for authentication without exposing the actual values
  })();
  ```

  ```python python theme={null}
  import os
  import requests

  # Create a session with 1Password integration
  response = requests.post(
      "https://api.anchorbrowser.io/v1/sessions",
      headers={
          "anchor-api-key": os.getenv("ANCHOR_API_KEY"),
          "Content-Type": "application/json"
      },
      json={
          "integrations": [
              {
                  "id": integration_id,
                  "type": "1PASSWORD",
                  "configuration": {
                      "load_mode": "specific",
                      "secrets": [
                          "op://Production/Database/username",
                          "op://Production/Database/password"
                      ]
                  }
              }
          ]
      }
  )

  session_data = response.json()
  print(session_data)
  # Access the secrets in your automation code
  # The secrets are automatically available as environment variables
  # OP_PRODUCTION_DATABASE_USERNAME and OP_PRODUCTION_DATABASE_PASSWORD
  # Your AI agent can use these for authentication without exposing the actual values
  ```
</CodeGroup>

## Managing Integrations

### List All Integrations

```bash theme={null}
curl -X GET https://api.anchorbrowser.io/v1/integrations \
  -H "anchor-api-key: YOUR_API_KEY"
```

**Response:**

```json theme={null}
{
  "data": {
    "integrations": [
      {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "name": "My 1Password Integration",
        "type": "1PASSWORD",
        "createdAt": "2024-01-01T00:00:00.000Z"
      }
    ]
  }
}
```

### Delete an Integration

```bash theme={null}
curl -X DELETE https://api.anchorbrowser.io/v1/integrations/550e8400-e29b-41d4-a716-446655440000 \
  -H "anchor-api-key: YOUR_API_KEY"
```

**Response:**

```json theme={null}
{
  "data": {
    "integration": {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "deleted": true,
      "path": "integrations/team-id/550e8400-e29b-41d4-a716-446655440000"
    }
  }
}
```

<Warning>
  Deleting an integration will remove the stored service account token. Any
  browser sessions using this integration will fail to load secrets.
</Warning>

## Troubleshooting

### Integration Creation Fails

* **Invalid Service Account Token**: Verify your token starts with `ops_` and is valid
* **Insufficient Permissions**: Ensure the service account has access to the required vaults

### Secrets Not Loading

* **Invalid Secret Reference**: Check the format of your secret references (`op://vault/item/field`)
* **Service Account Access**: Verify the service account has access to the specified vaults and items
* **Item or Field Not Found**: Ensure the vault, item, and field names are correct and exist

### Environment Variables Not Available

* **Check Secret Reference Format**: Ensure your secret references follow the correct format
* **Verify Integration ID**: Make sure you're using the correct integration ID in your session configuration

## Support

For additional help with 1Password integration:

* [1Password Service Accounts Documentation](https://developer.1password.com/docs/service-accounts/)
* Contact Anchor Browser support at [support@anchorbrowser.io](mailto:support@anchorbrowser.io)


# Browser-use
Source: https://docs.anchorbrowser.io/integrations/browseruse-deployment



<Note>This guide is dedicated to running your own browser-use agent while connecting to an Anchor browser. To use the embedded browser use capability, refer to [AI task completion](/agentic-browser-control/ai-task-completion)</Note>

<Steps>
  <Step title="Step one - Create an Anchor Browser session">
    ```python python theme={null}
    from anchorbrowser import Anchorbrowser
    import os

    anchor_client = Anchorbrowser(
        api_key=os.getenv("ANCHOR_API_KEY")
    )

    session = anchor_client.sessions.create()
    cdp_url = session.data.cdp_url
    print("Session's CDP_URL for later use\n", cdp_url)
    ```
  </Step>

  <Step title="Initialize browser-use with Anchor browser">
    ```python python theme={null}
    from browser_use import Agent, Controller
    from browser_use.browser import BrowserProfile, BrowserSession
    from browser_use.llm import ChatOpenAI
    import os

    # Configure your LLM (example with OpenAI)
    llm = ChatOpenAI(
        model='gpt-4o',
        api_key=os.getenv('OPENAI_API_KEY'),
    )

    # Initialize browser session with Anchor
    profile = BrowserProfile(keep_alive=True)
    browser_session = BrowserSession(
        headless=False, 
        cdp_url=cdp_url, 
        browser_profile=profile
    )

    # Create controller and agent
    controller = Controller()
    agent = Agent(
        task="Your task description here",
        llm=llm,
        enable_memory=False,
        use_vision=False,
        controller=controller,
        browser_session=browser_session,
    )

    # Run the agent
    result = await agent.run(max_steps=40)
    ```
  </Step>

  <Step title="Optional - Live view the browser">
    Use the `live_view_url` returned on the first step to view the browser session in real-time, or to embed it as a UI component

    ```html theme={null}
    <!-- Make sure to replace <session_id> with the 
        actual session ID from the first step -->
    <iframe src="https://live.anchorbrowser.io?sessionId=<session_id>" 
        sandbox="allow-same-origin allow-scripts" 
        allow="clipboard-read; clipboard-write" 
        style="border: 0px; display: block; width: 100%; height: 100%;
        position: absolute; top: 0px; left: 0px;">
    </iframe>
    ```
  </Step>
</Steps>


# Groq GPT-OSS
Source: https://docs.anchorbrowser.io/integrations/groq

Blazing Fast, Accurate Browser Agents

# Anchor Browser + Groq: Blazing, Accurate Fast Browser Agents

[Groq](https://groq.com/) is the fast inference platform, providing llm APIs with low time-to-first-token and time-to-response

## Python Quickstart (2 minutes to hello world)

<img alt="AI Form Filling with Groq on Anchor Browser" />

### Prerequisites

* Python 3.8 or higher installed.

### Setup

1. **Get your API keys:**
   * Go to [Anchor Browser API Key](https://app.anchorbrowser.io/api-keys?utm_source=groq)

2. **Install dependencies:**
   Install the [Anchor Browser Python SDK](https://docs.anchorbrowser.io/quickstart/use-via-sdk?utm_source=groq). ([Typescript SDK](https://docs.anchorbrowser.io/quickstart/use-via-sdk?utm_source=groq) is also available).

```bash theme={null}
pip install anchorbrowser pydantic
```

## Quick Example: Extract Latest AI News

```python python theme={null}
import os
from anchorbrowser import Anchorbrowser

# Initialize the Anchor Browser Client
client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))

# Collect the newest from AI News website
task_result = client.agent.task(
    "Extract the latest news title from this AI News website",
    task_options={
        "url": "https://www.artificialintelligence-news.com/",
        "provider": "groq",
        "model": "openai/gpt-oss-120b",
    }
)

print("Latest news title:", task_result)

```

## Advanced Session Configuration

Create a session using advanced configuration (see Anchor [API reference](https://docs.anchorbrowser.io/api-reference/browser-sessions/start-browser-session?utm_source=groq)).

```python python theme={null}
import os
from anchorbrowser import Anchorbrowser

# configuration example, can be ommited for default values.
session_config = {
    "session": {
        "recording": False,  # Disable session recording
        "proxy": {
            "active": True,
            "type": "anchor_residential",
            "country_code": "us"
        },
        "max_duration": 5,  # 5 minutes
        "idle_timeout": 1    # 1 minute
    }
}

client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
configured_session = client.sessions.create(browser=session_config)

# Get the session_id to run automation workflows to the same running session.
session_id = configured_session.data.id

# Get the live view url to browse the browser in action (it's interactive!).
live_view_url = configured_session.data.live_view_url

print('session_id:', session_id, '\nlive_view_url:', live_view_url)
```

## Next Steps

* Explore the [API Reference](https://docs.anchorbrowser.io/api-reference?utm_source=groq) for detailed documentation
* Learn about [Authentication and Identity management](https://docs.anchorbrowser.io/essentials/authentication-and-identity?utm_source=groq)
* Check out [Advanced Proxy Configuration](https://docs.anchorbrowser.io/advanced/proxy?utm_source=groq) for location-specific browsing
* Use more [Agentic tools](https://docs.anchorbrowser.io/agentic-browser-control?utm_source=groq)


# Make
Source: https://docs.anchorbrowser.io/integrations/make

Integrate Anchor Browser with Make (formerly Integromat) for no-code automation workflows

## About Make

[Make](https://www.make.com/) is a no-code automation platform that lets you connect apps and services together to build powerful workflows — without writing code.

## Quick Start

Use our modules to enhance your automation workflows with Anchor Browser powerful tools.

### Module Selection

<img alt="Our Modules when creating a new scenario" />

Use our [AI Task Completion](/agentic-browser-control/ai-task-completion) module to perform various tasks in a single module.

<img alt="Our AI Web Task module" />

### Basic Workflow

Here is a basic workflow that uses our modules to perform a task, capture a screenshot and save it to a file both in google drive and slack.

<img alt="Basic Anchor Browser workflow" />

***

## Getting Help

If you experience any issues with Anchor Browser Make modules, please contact our support team at [support@anchorbrowser.io](mailto:support@anchorbrowser.io).


# n8n
Source: https://docs.anchorbrowser.io/integrations/n8n

Integrate Anchor Browser with n8n for no-code automation workflows

## About n8n

[n8n](https://n8n.io/) is an open-source workflow automation platform that lets you connect apps and services together to build powerful workflows — without writing code.

## Quick Start

Use our node to enhance your automation workflows with Anchor Browser powerful tools.

### Node Installation

Install the Anchor Browser node from the n8n community nodes:

```bash theme={null}
npm install n8n-nodes-anchorbrowser
```

<img alt="Installing the Anchor Browser node" />

### Credentials Setup

Set up your Anchor Browser API credentials:

<img alt="Credentials configuration" />

Make sure after saving that the connection is tested successfully.

<img alt="Credentials tested successfully" />

### Node Selection

<img alt="Our Node when creating a new workflow" />

<img alt="Basic Anchor Browser workflow" />

Use our [AI Task Completion](/agentic-browser-control/ai-task-completion) node to perform various tasks in a single operation.

### Node Configuration

Configure your Anchor Browser node with the necessary settings, and then Execute step.

<img alt="Node configuration settings" />

### Task Configuration

Configure your browser automation task:

<img alt="Task configuration settings" />

<img alt="Task prompt configuration" />

***

## Getting Help

If you experience any issues with Anchor Browser n8n node, please contact our support team at [support@anchorbrowser.io](mailto:support@anchorbrowser.io).


# Airtable
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/airtable

Automate Airtable database workflows with Playwright when APIs aren't available.

# How to Automate Airtable with Playwright

Automate critical Airtable database workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual data entry and reduce record management errors by automating repetitive database management processes. Use Playwright to interact with Airtable's web interface programmatically.

[View Airtable's API documentation](https://airtable.com/developers/web/api/introduction) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Airtable tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Airtable
await page.goto('https://airtable.com/login');
await page.fill('[data-testid="email-input"]', process.env.AIRTABLE_EMAIL);
await page.fill('[data-testid="password-input"]', process.env.AIRTABLE_PASSWORD);
await page.click('[data-testid="submit-button"]');

// Navigate to workspace and base
await page.click('[data-testid="workspace-switcher"]');
await page.click('text=Marketing Team');
await page.click('text=Campaign Tracker');

// Add new record to table
await page.click('[data-testid="add-record-button"]');
await page.fill('[data-testid="field-Campaign Name"]', 'Q1 Product Launch');
await page.selectOption('[data-testid="field-Status"]', 'In Progress');
await page.fill('[data-testid="field-Budget"]', '50000');
await page.fill('[data-testid="field-Start Date"]', '2024-01-15');
await page.click('[data-testid="save-record"]');

// Create filtered view
await page.click('[data-testid="view-switcher"]');
await page.click('[data-testid="create-view"]');
await page.fill('[data-testid="view-name"]', 'Active Campaigns');
await page.click('[data-testid="add-filter"]');
await page.selectOption('[data-testid="filter-field"]', 'Status');
await page.selectOption('[data-testid="filter-condition"]', 'is');
await page.selectOption('[data-testid="filter-value"]', 'In Progress');
await page.click('[data-testid="save-view"]');

await browser.close();
```

Playwright handles field validation, view creation, and record linking automatically. You can automate data imports, report generation, and workflow automation processes.

## Scale your Airtable automation with Anchor Browser

Run your Playwright Airtable automations on cloud browsers with enterprise-grade reliability and persistent Airtable sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Attio
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/attio

Automate Attio CRM workflows with Playwright when APIs aren't available.

# How to Automate Attio with Playwright

Automate critical Attio CRM workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual contact management and reduce data entry errors by automating repetitive customer relationship processes. Use Playwright to interact with Attio's web interface programmatically.

[View Attio's API documentation](https://docs.attio.com/) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Attio tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Attio
await page.goto('https://app.attio.com/login');
await page.fill('[data-testid="email-input"]', process.env.ATTIO_EMAIL);
await page.fill('[data-testid="password-input"]', process.env.ATTIO_PASSWORD);
await page.click('[data-testid="login-button"]');

// Navigate to contacts
await page.click('[data-testid="nav-people"]');
await page.click('[data-testid="add-person-button"]');

// Create new contact
await page.fill('[data-testid="first-name"]', 'Sarah');
await page.fill('[data-testid="last-name"]', 'Johnson');
await page.fill('[data-testid="email-field"]', 'sarah.johnson@company.com');
await page.fill('[data-testid="company-field"]', 'Tech Innovations Inc');
await page.selectOption('[data-testid="status-select"]', 'qualified-lead');

// Add deal to pipeline
await page.click('[data-testid="deals-tab"]');
await page.click('[data-testid="add-deal-button"]');
await page.fill('[data-testid="deal-name"]', 'Enterprise Software License');
await page.fill('[data-testid="deal-value"]', '25000');
await page.click('[data-testid="save-contact"]');

await browser.close();
```

Playwright handles dynamic form fields, relationship linking, and pipeline updates automatically. You can automate lead qualification, deal progression, and contact enrichment workflows.

## Scale your Attio automation with Anchor Browser

Run your Playwright Attio automations on cloud browsers with enterprise-grade reliability and persistent Attio sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Bill.com
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/bill

Automate Bill.com accounts payable workflows with Playwright when APIs aren't available.

# How to Automate Bill.com with Playwright

Automate critical Bill.com accounts payable workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual invoice processing and reduce payment errors by automating repetitive financial management processes. Use Playwright to interact with Bill.com's web interface programmatically.

[View Bill.com's API documentation](https://developer.bill.com/hc/en-us) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Bill.com tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Bill.com
await page.goto('https://app.bill.com/login');
await page.fill('[data-testid="email-input"]', process.env.BILL_EMAIL);
await page.fill('[data-testid="password-input"]', process.env.BILL_PASSWORD);
await page.click('[data-testid="login-button"]');

// Navigate to bills section
await page.click('[data-testid="nav-bills"]');
await page.click('[data-testid="create-bill-button"]');

// Create new bill
await page.fill('[data-testid="vendor-search"]', 'Office Supply Co');
await page.click('[data-testid="vendor-select"]');
await page.fill('[data-testid="invoice-number"]', 'INV-2024-001');
await page.fill('[data-testid="invoice-date"]', '01/15/2024');
await page.fill('[data-testid="due-date"]', '02/15/2024');
await page.fill('[data-testid="amount"]', '1250.00');

// Add line item details
await page.click('[data-testid="add-line-item"]');
await page.fill('[data-testid="description"]', 'Office supplies - January');
await page.selectOption('[data-testid="expense-account"]', 'Office Expenses');
await page.click('[data-testid="save-bill"]');

// Approve and schedule payment
await page.click('[data-testid="approve-button"]');
await page.click('[data-testid="schedule-payment"]');
await page.selectOption('[data-testid="payment-date"]', '02/10/2024');
await page.click('[data-testid="confirm-payment"]');

await browser.close();
```

Playwright handles vendor lookups, approval workflows, and payment scheduling automatically. You can automate invoice processing, expense categorization, and cash flow management workflows.

## Scale your Bill.com automation with Anchor Browser

Run your Playwright Bill.com automations on cloud browsers with enterprise-grade reliability and persistent Bill.com sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Clickup
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/clickup

Automate ClickUp project management workflows with Playwright when APIs aren't available.

# How to Automate ClickUp with Playwright

Automate critical ClickUp project management workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual task creation and reduce project tracking errors by automating repetitive productivity processes. Use Playwright to interact with ClickUp's web interface programmatically.

[View ClickUp's API documentation](https://clickup.com/api/) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common ClickUp tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to ClickUp
await page.goto('https://app.clickup.com/login');
await page.fill('[data-test="login-email-input"]', process.env.CLICKUP_EMAIL);
await page.fill('[data-test="login-password-input"]', process.env.CLICKUP_PASSWORD);
await page.click('[data-test="login-submit"]');

// Navigate to workspace
await page.click('[data-test="sidebar-workspace"]');
await page.click('text=Development Team');

// Create new task
await page.click('[data-test="new-task-button"]');
await page.fill('[data-test="draft-view__title"]', 'Implement user dashboard');
await page.fill('[data-test="description-input"]', 'Create responsive dashboard with analytics widgets');
await page.selectOption('[data-test="priority-select"]', 'high');
await page.click('[data-test="assignee-dropdown"]');
await page.click('text=John Developer');

// Set due date and create task
await page.click('[data-test="due-date-picker"]');
await page.click('[data-test="date-next-week"]');
await page.click('[data-test="save-task"]');

// Update task status
await page.click('[data-test="status-dropdown"]');
await page.click('text=In Progress');

await browser.close();
```

Playwright handles task creation, status updates, and team assignments automatically. You can automate sprint planning, time tracking, and project reporting workflows.

## Scale your Clickup automation with Anchor Browser

Run your Playwright Clickup automations on cloud browsers with enterprise-grade reliability and persistent Clickup sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# CrowdStrike
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/crowdstrike

Automate CrowdStrike security workflows with Playwright when APIs aren't available.

# How to Automate CrowdStrike with Playwright

Automate critical CrowdStrike security workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual threat investigation and reduce incident response time by automating repetitive cybersecurity processes. Use Playwright to interact with CrowdStrike's web interface programmatically.

[View CrowdStrike's API documentation](https://developer.crowdstrike.com/) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common CrowdStrike tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to CrowdStrike Falcon
await page.goto('https://falcon.crowdstrike.com/');
await page.fill('[data-testid="username"]', process.env.CROWDSTRIKE_USERNAME);
await page.fill('[data-testid="password"]', process.env.CROWDSTRIKE_PASSWORD);
await page.click('[data-testid="login-button"]');

// Navigate to Incident Workbench
await page.click('[data-testid="nav-incident-workbench"]');
await page.click('[data-testid="view-all-incidents"]');

// Create new incident investigation
await page.click('[data-testid="create-incident"]');
await page.fill('[data-testid="incident-name"]', 'Suspicious Network Activity Investigation');
await page.selectOption('[data-testid="severity-level"]', 'Medium');
await page.fill('[data-testid="description"]', 'Unusual outbound traffic detected from workstation');

// Assign to security team
await page.click('[data-testid="assignee-dropdown"]');
await page.click('text=SOC Team Alpha');
await page.selectOption('[data-testid="priority"]', 'High');

// Add affected hosts
await page.click('[data-testid="add-hosts-tab"]');
await page.fill('[data-testid="hostname-search"]', 'DESKTOP-001');
await page.click('[data-testid="add-host"]');

// Generate investigation report
await page.click('[data-testid="generate-report"]');
await page.selectOption('[data-testid="report-format"]', 'PDF');
await page.click('[data-testid="download-report"]');

await browser.close();
```

Playwright handles threat detection workflows, incident management, and security reporting automatically. You can automate host isolation, malware analysis, and compliance reporting workflows.

## Scale your CrowdStrike automation with Anchor Browser

Run your Playwright CrowdStrike automations on cloud browsers with enterprise-grade reliability and persistent CrowdStrike sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# DocuSign
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/docusign

Automate DocuSign electronic signature workflows with Playwright when APIs aren't available.

# How to Automate DocuSign with Playwright

Automate critical DocuSign electronic signature workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual document sending and reduce signature processing errors by automating repetitive contract management processes. Use Playwright to interact with DocuSign's web interface programmatically.

[View DocuSign's API documentation](https://developers.docusign.com/) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common DocuSign tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to DocuSign
await page.goto('https://account.docusign.com/');
await page.fill('[data-qa="Username"]', process.env.DOCUSIGN_EMAIL);
await page.fill('[data-qa="Password"]', process.env.DOCUSIGN_PASSWORD);
await page.click('[data-qa="Log In"]');

// Navigate to envelope creation
await page.click('[data-qa="nav-send"]');
await page.click('[data-qa="start-sending"]');

// Upload document
await page.click('[data-qa="upload-document"]');
const fileInput = await page.locator('input[type="file"]');
await fileInput.setInputFiles('./contracts/employment-agreement.pdf');

// Add recipients
await page.click('[data-qa="add-recipient"]');
await page.fill('[data-qa="recipient-name"]', 'John Smith');
await page.fill('[data-qa="recipient-email"]', 'john.smith@company.com');
await page.selectOption('[data-qa="recipient-role"]', 'signer');

// Position signature fields
await page.click('[data-qa="tag-document"]');
await page.click('[data-qa="signature-tab"]');
await page.click('[data-qa="signature-placement"]', { position: { x: 200, y: 400 } });

// Send envelope
await page.click('[data-qa="send-envelope"]');

await browser.close();
```

Playwright handles document uploads, recipient management, and signature field positioning automatically. You can automate contract distribution, template creation, and signing ceremony workflows.

## Scale your DocuSign automation with Anchor Browser

Run your Playwright DocuSign automations on cloud browsers with enterprise-grade reliability and persistent DocuSign sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Dropbox
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/dropbox

Automate Dropbox file management workflows with Playwright when APIs aren't available.

# How to Automate Dropbox with Playwright

Automate critical Dropbox file management workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual file organization and reduce sharing errors by automating repetitive document management processes. Use Playwright to interact with Dropbox's web interface programmatically.

[View Dropbox's API documentation](https://www.dropbox.com/developers/documentation) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Dropbox tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Dropbox
await page.goto('https://www.dropbox.com/login');
await page.fill('[name="login_email"]', process.env.DROPBOX_EMAIL);
await page.fill('[name="login_password"]', process.env.DROPBOX_PASSWORD);
await page.click('[data-testid="real-login-button"]');

// Navigate to team folder
await page.click('[data-testid="browse-folders"]');
await page.click('text=Team Shared');

// Create new folder structure
await page.click('[data-testid="new-folder-button"]');
await page.fill('[data-testid="folder-name-input"]', 'Q1 Reports');
await page.click('[data-testid="create-folder"]');

// Upload files to folder
await page.click('text=Q1 Reports');
await page.click('[data-testid="upload-button"]');
const fileInput = await page.locator('input[type="file"]');
await fileInput.setInputFiles(['./reports/january.pdf', './reports/february.pdf']);

// Share folder with team
await page.click('[data-testid="share-button"]');
await page.fill('[data-testid="share-email"]', 'team@company.com');
await page.selectOption('[data-testid="permission-level"]', 'edit');
await page.click('[data-testid="send-invitation"]');

await browser.close();
```

Playwright handles file uploads, folder permissions, and sharing workflows automatically. You can automate document organization, team collaboration setup, and backup processes.

## Scale your Dropbox automation with Anchor Browser

Run your Playwright Dropbox automations on cloud browsers with enterprise-grade reliability and persistent Dropbox sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Figma
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/figma

Automate Figma design workflows with Playwright when APIs aren't available.

# How to Automate Figma with Playwright

Automate critical Figma design workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual design handoffs and reduce version control errors by automating repetitive design collaboration processes. Use Playwright to interact with Figma's web interface programmatically.

[View Figma's API documentation](https://www.figma.com/developers/api) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Figma actions:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Figma
await page.goto('https://www.figma.com/login');
await page.fill('[data-testid="email"]', process.env.FIGMA_EMAIL);
await page.fill('[data-testid="password"]', process.env.FIGMA_PASSWORD);
await page.click('[data-testid="submit"]');

// Navigate to team files
await page.click('[data-testid="dashboard-team-switcher"]');
await page.click('text=Design Team');
await page.click('text=Mobile App Redesign');

// Create new frame
await page.click('[data-testid="toolbar-frame-tool"]');
await page.click('[data-testid="canvas"]');
await page.selectOption('[data-testid="frame-preset"]', 'iPhone 14');

// Add components and export
await page.click('[data-testid="assets-panel"]');
await page.dragAndDrop('[data-testid="button-component"]', '[data-testid="canvas-frame"]');
await page.fill('[data-testid="text-input"]', 'Get Started');

// Export assets
await page.click('[data-testid="export-button"]');
await page.selectOption('[data-testid="export-format"]', 'PNG');
await page.selectOption('[data-testid="export-scale"]', '2x');
await page.click('[data-testid="export-download"]');

// Share with developer
await page.click('[data-testid="share-button"]');
await page.fill('[data-testid="share-email"]', 'developer@company.com');
await page.selectOption('[data-testid="permission-level"]', 'can view');
await page.click('[data-testid="send-invite"]');

await browser.close();
```

Playwright handles component manipulation, export processes, and collaboration workflows automatically. You can automate design system updates, asset generation, and developer handoff processes.

## Scale your Figma automation with Anchor Browser

Run your Playwright Figma automations on cloud browsers with enterprise-grade reliability and persistent Figma sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# HubSpot
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/hubspot

Automate HubSpot CRM workflows with Playwright when APIs aren't available.

# How to Automate HubSpot with Playwright

Automate critical HubSpot CRM workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual lead processing and reduce sales pipeline errors by automating repetitive marketing and sales processes. Use Playwright to interact with HubSpot's web interface programmatically.

[View HubSpot's API documentation](https://developers.hubspot.com/docs/api/overview) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common HubSpot tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to HubSpot
await page.goto('https://app.hubspot.com/login');
await page.fill('#username', process.env.HUBSPOT_EMAIL);
await page.fill('#password', process.env.HUBSPOT_PASSWORD);
await page.click('#loginBtn');

// Navigate to contacts
await page.click('[data-selenium-test="nav-primary-contacts-contacts"]');
await page.click('[data-selenium-test="create-contact-button"]');

// Create new contact
await page.fill('[data-field="firstname"]', 'Michael');
await page.fill('[data-field="lastname"]', 'Chen');
await page.fill('[data-field="email"]', 'michael.chen@techcorp.com');
await page.fill('[data-field="company"]', 'TechCorp Solutions');
await page.selectOption('[data-field="lifecyclestage"]', 'marketingqualifiedlead');

// Create associated deal
await page.click('[data-selenium-test="associations-tab"]');
await page.click('[data-selenium-test="create-deal-button"]');
await page.fill('[data-field="dealname"]', 'TechCorp Enterprise Package');
await page.fill('[data-field="amount"]', '75000');
await page.selectOption('[data-field="dealstage"]', 'qualifiedtobuy');
await page.click('[data-selenium-test="save-contact"]');

await browser.close();
```

Playwright handles form validations, association creation, and pipeline updates automatically. You can automate lead scoring, email campaign management, and sales forecasting workflows.

## Scale your HubSpot automation with Anchor Browser

Run your Playwright HubSpot automations on cloud browsers with enterprise-grade reliability and persistent HubSpot CRM sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Jira
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/jira

Automate Jira project management workflows with Playwright when APIs aren't available.

# How to Automate Jira with Playwright

Automate critical Jira project management workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual ticket creation and reduce project tracking errors by automating repetitive development processes. Use Playwright to interact with Jira's web interface programmatically.

[View Jira's REST API documentation](https://developer.atlassian.com/server/jira/platform/rest/v11000/intro/#gettingstarted) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Jira tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Jira
await page.goto('https://your-company.atlassian.net/');
await page.fill('#username', process.env.JIRA_USERNAME);
await page.click('#login-submit');
await page.fill('#password', process.env.JIRA_PASSWORD);
await page.click('#login-submit');

// Navigate to project
await page.click('[data-testid="global-pages.directories.projects-directory-v2"]');
await page.click('text=Development Project');

// Create new issue
await page.click('[data-testid="project-sidebar.create-issue-button"]');
await page.selectOption('[data-testid="issue-type-select"]', 'Story');
await page.fill('[data-testid="issue-summary-field"]', 'Implement user authentication');
await page.fill('[data-testid="issue-description-field"]', 'Add OAuth login functionality');
await page.selectOption('[data-testid="assignee-select"]', 'john.doe');
await page.click('[data-testid="issue-create-submit"]');

// Update issue status
await page.click('text=DEV-123');
await page.click('[data-testid="issue-workflow-transition"]');
await page.click('text=In Progress');

await browser.close();
```

Playwright handles issue creation, workflow transitions, and field updates automatically. You can automate sprint planning, bulk status updates, and project reporting workflows.

## Scale your Jira automation with Anchor Browser

Run your Playwright Jira automations on cloud browsers with enterprise-grade reliability and persistent Jira sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Miro
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/miro

Automate Miro collaboration workflows with Playwright when APIs aren't available.

# How to Automate Miro with Playwright

Automate critical Miro collaboration workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual board setup and reduce brainstorming session errors by automating repetitive visual collaboration processes. Use Playwright to interact with Miro's web interface programmatically.

[View Miro's API documentation](https://developers.miro.com/docs) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Miro actions:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Miro
await page.goto('https://miro.com/login/');
await page.fill('[data-testid="mr-form-login-btn-start-1"]', process.env.MIRO_EMAIL);
await page.click('[data-testid="mr-form-login-btn-start-1"]');
await page.fill('[data-testid="password"]', process.env.MIRO_PASSWORD);
await page.click('[data-testid="mr-form-login-btn-signin-1"]');

// Create new board
await page.click('[data-testid="create-board-button"]');
await page.fill('[data-testid="board-title-input"]', 'Sprint Planning Session');
await page.selectOption('[data-testid="template-select"]', 'Agile Planning');
await page.click('[data-testid="create-button"]');

// Add sticky notes for user stories
await page.click('[data-testid="toolbar-sticky-note"]');
await page.click('[data-testid="canvas"]', { position: { x: 200, y: 200 } });
await page.fill('[data-testid="sticky-note-text"]', 'As a user, I want to login easily');
await page.press('[data-testid="sticky-note-text"]', 'Escape');

// Create swimlanes
await page.click('[data-testid="toolbar-shapes"]');
await page.click('[data-testid="rectangle-shape"]');
await page.dragAndDrop('[data-testid="canvas"]', '[data-testid="canvas"]', {
  sourcePosition: { x: 100, y: 100 },
  targetPosition: { x: 800, y: 150 }
});

// Share board with team
await page.click('[data-testid="share-board-button"]');
await page.fill('[data-testid="invite-email"]', 'team@company.com');
await page.selectOption('[data-testid="permission-level"]', 'can edit');
await page.click('[data-testid="send-invitation"]');

await browser.close();
```

Playwright handles canvas interactions, shape creation, and collaboration features automatically. You can automate template setup, workshop facilitation, and board organization workflows.

## Scale your Miro automation with Anchor Browser

Run your Playwright Miro automations on cloud browsers with enterprise-grade reliability and persistent Miro sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Monday
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/monday

Automate Monday.com project management workflows with Playwright when APIs aren't available.

# How to Automate Monday with Playwright

Automate critical Monday.com project management workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual board setup and reduce task tracking errors by automating repetitive project management processes. Use Playwright to interact with Monday.com's web interface programmatically.

[View Monday.com's API documentation](https://developer.monday.com/api-reference/docs) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Monday.com tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Monday.com
await page.goto('https://auth.monday.com/login');
await page.fill('[data-testid="email-field"]', process.env.MONDAY_EMAIL);
await page.fill('[data-testid="password-field"]', process.env.MONDAY_PASSWORD);
await page.click('[data-testid="login-button"]');

// Create new board
await page.click('[data-testid="create-board-button"]');
await page.fill('[data-testid="board-name-input"]', 'Product Launch Campaign');
await page.selectOption('[data-testid="board-template"]', 'Marketing Campaign');
await page.click('[data-testid="create-board-confirm"]');

// Add new item to board
await page.click('[data-testid="add-item-button"]');
await page.fill('[data-testid="item-name"]', 'Website Landing Page');
await page.selectOption('[data-testid="status-column"]', 'Working on it');
await page.fill('[data-testid="person-column"]', 'Sarah Marketing');
await page.click('[data-testid="date-column"]');
await page.fill('[data-testid="due-date"]', '2024-03-15');

// Update item progress
await page.click('[data-testid="timeline-column"]');
await page.dragAndDrop('[data-testid="timeline-bar"]', '[data-testid="timeline-bar"]', {
  sourcePosition: { x: 0, y: 0 },
  targetPosition: { x: 100, y: 0 }
});

// Add automation
await page.click('[data-testid="board-menu"]');
await page.click('[data-testid="automations-tab"]');
await page.click('[data-testid="add-automation"]');
await page.selectOption('[data-testid="automation-trigger"]', 'when status changes to Done');
await page.selectOption('[data-testid="automation-action"]', 'notify person');
await page.click('[data-testid="save-automation"]');

await browser.close();
```

Playwright handles board creation, item management, and automation setup automatically. You can automate project tracking, team notifications, and reporting workflows.

## Scale your Monday.com automation with Anchor Browser

Run your Playwright Monday automations on cloud browsers with enterprise-grade reliability and persistent Monday sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# NetSuite
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/netsuite

Automate NetSuite business workflows with Playwright when APIs aren't available.

# How to Automate NetSuite with Playwright

Automate critical NetSuite workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual data entry and reduce errors by automating repetitive business processes. Use Playwright to interact with NetSuite's web interface programmatically.

[View NetSuite's SuiteScript documentation](https://system.netsuite.com/help/helpcenter/en_US/APIs/REST_API_Browser/record/v1/2023.1/index.html) for API alternatives when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common NetSuite tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to NetSuite
await page.goto('https://system.netsuite.com/pages/customerlogin.jsp');
await page.fill('#email', process.env.NETSUITE_EMAIL);
await page.fill('#password', process.env.NETSUITE_PASSWORD);
await page.click('#login-submit');

// Navigate to customer records
await page.click('text=Lists');
await page.click('text=Customers');

// Create new customer record
await page.click('text=New');
await page.fill('#companyname', 'Acme Corporation');
await page.fill('#email', 'contact@acme.com');
await page.click('#btn_multibutton_submitter');

await browser.close();
```

Playwright handles dynamic loading, form submissions, and navigation automatically. You can automate financial reporting, customer management, and inventory updates.

## Scale your NetSuite automation with Anchor Browser

Run your Playwright NetSuite automations on cloud browsers with enterprise-grade reliability and session persistence. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Notion
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/notion

Automate Notion workspace workflows with Playwright when APIs aren't available.

# How to Automate Notion with Playwright

Automate critical Notion workspace workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual page creation and reduce content management errors by automating repetitive documentation processes. Use Playwright to interact with Notion's web interface programmatically.

[View Notion's API documentation](https://developers.notion.com/) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Notion tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Notion
await page.goto('https://www.notion.so/login');
await page.fill('[data-testid="login-email"]', process.env.NOTION_EMAIL);
await page.fill('[data-testid="login-password"]', process.env.NOTION_PASSWORD);
await page.click('[data-testid="login-submit"]');

// Navigate to workspace
await page.click('[data-testid="workspace-switcher"]');
await page.click('text=Team Workspace');

// Create new page
await page.click('text=+ New page');
await page.fill('[placeholder="Untitled"]', 'Weekly Status Report');
await page.click('[data-testid="template-button"]');
await page.click('text=Meeting notes');

// Add content to database
await page.click('text=Projects Database');
await page.click('text=+ New');
await page.fill('[data-testid="title-input"]', 'Q1 Marketing Campaign');
await page.selectOption('[data-testid="status-select"]', 'In Progress');
await page.click('[data-testid="save-button"]');

await browser.close();
```

Playwright handles page loading, template selection, and database updates automatically. You can automate content publishing, team collaboration workflows, and project tracking processes.

## Scale your Notion automation with Anchor Browser

Run your Playwright Notion automations on cloud browsers with enterprise-grade reliability and persistent Notion sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Pipedrive
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/pipedrive

Automate Pipedrive CRM workflows with Playwright when APIs aren't available.

# How to Automate Pipedrive with Playwright

Automate critical Pipedrive CRM workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual deal tracking and reduce sales pipeline errors by automating repetitive sales processes. Use Playwright to interact with Pipedrive's web interface programmatically.

[View Pipedrive's API documentation](https://developers.pipedrive.com/docs/api/v1) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Pipedrive tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Pipedrive
await page.goto('https://your-company.pipedrive.com/');
await page.fill('[data-testid="login-email"]', process.env.PIPEDRIVE_EMAIL);
await page.fill('[data-testid="login-password"]', process.env.PIPEDRIVE_PASSWORD);
await page.click('[data-testid="login-button"]');

// Navigate to deals pipeline
await page.click('[data-testid="menu-deals"]');
await page.click('[data-testid="add-deal-button"]');

// Create new deal
await page.fill('[data-testid="deal-title"]', 'Enterprise Software License');
await page.fill('[data-testid="deal-value"]', '45000');
await page.selectOption('[data-testid="deal-stage"]', 'qualified-to-buy');
await page.fill('[data-testid="person-name"]', 'Lisa Rodriguez');
await page.fill('[data-testid="organization-name"]', 'Global Tech Solutions');

// Set follow-up activity
await page.click('[data-testid="add-activity-button"]');
await page.selectOption('[data-testid="activity-type"]', 'call');
await page.fill('[data-testid="activity-subject"]', 'Follow-up demo call');
await page.click('[data-testid="save-deal"]');

await browser.close();
```

Playwright handles pipeline navigation, deal progression, and activity scheduling automatically. You can automate lead qualification, sales forecasting, and customer follow-up workflows.

## Scale your Pipedrive automation with Anchor Browser

Run your Playwright Pipedrive automations on cloud browsers with enterprise-grade reliability and persistent Pipedrive sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Sage Intact
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/sage-intact

Automate Sage Intacct financial workflows with Playwright when APIs aren't available.

# How to Automate Sage Intacct with Playwright

Automate critical Sage Intacct financial workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual accounting tasks and reduce processing errors by automating repetitive financial processes. Use Playwright to interact with Intacct's web interface programmatically.

[View Sage Intacct's API documentation](https://developer.intacct.com/api/) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Intacct tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Sage Intacct
await page.goto('https://www.intacct.com/ia/acct/login.phtml');
await page.fill('#userid', process.env.INTACCT_USERNAME);
await page.fill('#companyid', process.env.INTACCT_COMPANY);
await page.fill('#password', process.env.INTACCT_PASSWORD);
await page.click('#loginButton');

// Navigate to General Ledger
await page.click('text=General Ledger');
await page.click('text=Journal Entry');

// Create new journal entry
await page.click('text=+');
await page.fill('[name="description"]', 'Monthly Accrual Entry');
await page.selectOption('[name="account"]', '1200');
await page.fill('[name="debit"]', '5000.00');
await page.click('#post');

await browser.close();
```

Playwright handles dynamic forms, account lookups, and validation automatically. You can automate journal entries, invoice processing, and financial reporting workflows.

## Scale your Sage Intacct automation with Anchor Browser

Run your Playwright Intacct automations on cloud browsers with enterprise-grade reliability and persistent financial sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Salesforce
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/salesforce

Automate Salesforce CRM workflows with Playwright when APIs aren't available.

# How to Automate Salesforce with Playwright

Automate critical Salesforce CRM workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual data entry and reduce lead processing errors by automating repetitive sales processes. Use Playwright to interact with Salesforce's web interface programmatically.

[View Salesforce's REST API documentation](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

### Authentication Options

**Option 1: Direct Login (Basic)**
Store credentials securely using environment variables:

```JavaScript theme={null}
// Use environment variables for security
const SALESFORCE_USERNAME = process.env.SALESFORCE_USERNAME;
const SALESFORCE_PASSWORD = process.env.SALESFORCE_PASSWORD;
```

**Option 2: OAuth2 Integration**
For production environments, implement OAuth2 flow:

```
import { chromium } from 'playwright';

// OAuth2 flow for secure authentication
const page = await browser.newPage();
await page.goto('https://login.salesforce.com/services/oauth2/authorize?...');
// Handle OAuth callback and token exchange
const accessToken = await handleOAuthCallback(page);
```

## Automate Workflows

Create scripts for common Salesforce tasks:

```
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Salesforce
await page.goto('https://login.salesforce.com/');
await page.fill('#username', process.env.SALESFORCE_USERNAME);
await page.fill('#password', process.env.SALESFORCE_PASSWORD);
await page.click('#Login');

// Navigate to Leads
await page.click('[title="App Launcher"]');
await page.fill('input[placeholder="Search apps and items..."]', 'Leads');
await page.click('text=Leads');

// Create new lead
await page.click('text=New');
await page.fill('[name="firstName"]', 'John');
await page.fill('[name="lastName"]', 'Doe');
await page.fill('[name="Company"]', 'Acme Corporation');
await page.fill('[name="Email"]', 'john.doe@acme.com');
await page.selectOption('[name="LeadSource"]', 'Website');
await page.click('button[name="SaveEdit"]');

await browser.close();
```

Playwright handles dynamic Lightning components, field validations, and record saves automatically. You can automate lead conversion, opportunity updates, and account management workflows.

## Scale your Salesforce automation with Anchor Browser

Run your Playwright Salesforce automations on cloud browsers with enterprise-grade reliability and persistent Salesforce sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# SAP S/4HANA
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/sap-s4-hana

Automate SAP S/4HANA business workflows with Playwright when APIs aren't available.

# How to Automate SAP S/4HANA with Playwright

Automate critical SAP S/4HANA workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual ERP tasks and reduce processing errors by automating repetitive business processes. Use Playwright to interact with SAP's web interface programmatically.

[View SAP's API documentation](https://api.sap.com/products/SAPS4HANA/apis/REST) for programmatic connections when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common SAP tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to SAP S/4HANA
await page.goto('https://your-sap-system.com:8000/sap/bc/gui/sap/its/webgui');
await page.fill('#sap-user', process.env.SAP_USERNAME);
await page.fill('#sap-password', process.env.SAP_PASSWORD);
await page.click('#LOGON_BUTTON');

// Navigate to purchase orders
await page.fill('#RSWPSearchTextField', 'ME21N');
await page.press('#RSWPSearchTextField', 'Enter');

// Create new purchase order
await page.fill('[title="Vendor"]', '100001');
await page.fill('[title="Purchase Organization"]', '1000');
await page.fill('[title="Material"]', 'MAT-001');
await page.fill('[title="Quantity"]', '10');
await page.click('#toolbar_save');

await browser.close();
```

Playwright handles SAP GUI navigation, transaction codes, and form submissions automatically. You can automate procurement, financial postings, and material movements.

## Scale your SAP S/4HANA automation with Anchor Browser

Run your Playwright SAP automations on cloud browsers with enterprise-grade reliability and persistent SAP sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# ServiceNow
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/servicenow

Automate ServiceNow IT service management workflows with Playwright when APIs aren't available.

# How to Automate ServiceNow with Playwright

Automate critical ServiceNow IT service management workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual ticket processing and reduce service delivery errors by automating repetitive ITSM processes. Use Playwright to interact with ServiceNow's web interface programmatically.

[View ServiceNow's API documentation](https://docs.servicenow.com/csh?topicname=c_RESTAPI.html) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common ServiceNow tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to ServiceNow
await page.goto('https://your-instance.service-now.com/');
await page.fill('[name="user_name"]', process.env.SERVICENOW_USERNAME);
await page.fill('[name="user_password"]', process.env.SERVICENOW_PASSWORD);
await page.click('[name="not_important"]');

// Navigate to Incident Management
await page.click('[data-testid="nav-incident-management"]');
await page.click('[data-testid="create-new-incident"]');

// Create new incident
await page.fill('[data-testid="caller-field"]', 'John Smith');
await page.selectOption('[data-testid="category-select"]', 'Hardware');
await page.selectOption('[data-testid="subcategory-select"]', 'Monitor');
await page.fill('[data-testid="short-description"]', 'Monitor display issues');
await page.fill('[data-testid="description"]', 'User reports flickering and color distortion on primary monitor');
await page.selectOption('[data-testid="priority-select"]', '3 - Moderate');
await page.selectOption('[data-testid="assignment-group"]', 'Desktop Support');

// Add work notes and resolve
await page.fill('[data-testid="work-notes"]', 'Replaced monitor cable. Issue resolved.');
await page.selectOption('[data-testid="incident-state"]', 'Resolved');
await page.selectOption('[data-testid="resolution-code"]', 'Solved (Permanently)');
await page.click('[data-testid="update-incident"]');

// Create change request
await page.click('[data-testid="change-management"]');
await page.click('[data-testid="create-change-request"]');
await page.fill('[data-testid="change-short-description"]', 'Server memory upgrade');
await page.selectOption('[data-testid="change-type"]', 'Standard');
await page.selectOption('[data-testid="risk-level"]', 'Low');
await page.click('[data-testid="submit-change"]');

await browser.close();
```

Playwright handles form navigation, dropdown selections, and workflow transitions automatically. You can automate incident resolution, change approvals, and asset management workflows.

## Scale your ServiceNow automation with Anchor Browser

Run your Playwright ServiceNow automations on cloud browsers with enterprise-grade reliability and persistent ServiceNow sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Tableau
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/tableau

Automate Tableau dashboard workflows with Playwright when APIs aren't available.

# How to Automate Tableau with Playwright

Automate critical Tableau dashboard workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual reporting tasks and reduce data processing errors by automating repetitive visualization processes. Use Playwright to interact with Tableau's web interface programmatically.

[View Tableau's REST API documentation](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright

```

## Automate Workflows

Create scripts for common Tableau tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Tableau Server
await page.goto('https://your-tableau-server.com');
await page.fill('[name="username"]', process.env.TABLEAU_USERNAME);
await page.fill('[name="password"]', process.env.TABLEAU_PASSWORD);
await page.click('[type="submit"]');

// Navigate to workbooks
await page.click('text=Explore');
await page.click('text=All Workbooks');

// Refresh data source
await page.click('text=Sales Dashboard');
await page.click('[data-test-id="refresh-button"]');
await page.waitForSelector('.refresh-complete');

// Export dashboard as PDF
await page.click('[data-test-id="share-button"]');
await page.click('text=Download');
await page.selectOption('[name="format"]', 'pdf');
await page.click('#download-button');

await browser.close();
```

Playwright handles dashboard loading, data refresh cycles, and export processes automatically. You can automate report generation, data source updates, and user permission management.

## Scale your Tableau automation with Anchor Browser

Run your Playwright Tableau automations on cloud browsers with enterprise-grade reliability and persistent Tableau sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# UiPath
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/uipath

Automate UiPath RPA management workflows with Playwright when APIs aren't available.

# How to Automate UiPath with Playwright

Automate critical UiPath RPA management workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual bot deployment and reduce automation management errors by automating repetitive RPA administration processes. Use Playwright to interact with UiPath's web interface programmatically.

[View UiPath's API documentation](https://docs.uipath.com/orchestrator/reference) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common UiPath tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to UiPath Orchestrator
await page.goto('https://your-tenant.uipath.com/');
await page.fill('[data-testid="email"]', process.env.UIPATH_EMAIL);
await page.fill('[data-testid="password"]', process.env.UIPATH_PASSWORD);
await page.click('[data-testid="login-button"]');

// Navigate to Automation Cloud
await page.click('[data-testid="orchestrator-tile"]');
await page.click('[data-testid="processes-menu"]');

// Deploy new process
await page.click('[data-testid="add-process-button"]');
await page.fill('[data-testid="process-name"]', 'Invoice Processing Bot');
await page.selectOption('[data-testid="package-select"]', 'InvoiceBot_v1.2');
await page.selectOption('[data-testid="environment-select"]', 'Production');
await page.click('[data-testid="deploy-process"]');

// Schedule automation job
await page.click('[data-testid="jobs-menu"]');
await page.click('[data-testid="create-job-button"]');
await page.selectOption('[data-testid="process-dropdown"]', 'Invoice Processing Bot');
await page.selectOption('[data-testid="robot-select"]', 'Robot-01');
await page.fill('[data-testid="job-priority"]', 'High');
await page.click('[data-testid="start-job"]');

// Monitor job status
await page.click('[data-testid="monitoring-tab"]');
await expect(page.locator('[data-testid="job-status"]')).toContainText('Running');

await browser.close();
```

Playwright handles process deployment, job scheduling, and monitoring workflows automatically. You can automate bot management, queue processing, and performance reporting workflows.

## Scale your UiPath automation with Anchor Browser

Run your Playwright UiPath automations on cloud browsers with enterprise-grade reliability and persistent UiPath sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Wrike
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/wrike

Automate Wrike project management workflows with Playwright when APIs aren't available.

# How to Automate Wrike with Playwright

Automate critical Wrike project management workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual project setup and reduce task management errors by automating repetitive work management processes. Use Playwright to interact with Wrike's web interface programmatically.

[View Wrike's API documentation](https://developers.wrike.com/) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Wrike tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Wrike
await page.goto('https://www.wrike.com/login/');
await page.fill('[data-testid="email-input"]', process.env.WRIKE_EMAIL);
await page.fill('[data-testid="password-input"]', process.env.WRIKE_PASSWORD);
await page.click('[data-testid="login-button"]');

// Create new project
await page.click('[data-testid="create-project-button"]');
await page.fill('[data-testid="project-title"]', 'Website Redesign Project');
await page.selectOption('[data-testid="project-template"]', 'Marketing Project');
await page.click('[data-testid="create-project-confirm"]');

// Add new task
await page.click('[data-testid="add-task-button"]');
await page.fill('[data-testid="task-title"]', 'Design homepage mockup');
await page.fill('[data-testid="task-description"]', 'Create responsive design mockups for new homepage');
await page.selectOption('[data-testid="task-status"]', 'In Progress');
await page.click('[data-testid="assignee-dropdown"]');
await page.click('text=Design Team');

// Set task dates and priority
await page.click('[data-testid="start-date-picker"]');
await page.click('[data-testid="today-button"]');
await page.click('[data-testid="due-date-picker"]');
await page.click('[data-testid="next-week-button"]');
await page.selectOption('[data-testid="priority-select"]', 'High');
await page.click('[data-testid="save-task"]');

// Create custom dashboard
await page.click('[data-testid="dashboards-menu"]');
await page.click('[data-testid="create-dashboard"]');
await page.fill('[data-testid="dashboard-name"]', 'Project Overview');
await page.click('[data-testid="add-widget"]');
await page.selectOption('[data-testid="widget-type"]', 'Tasks by Status');
await page.click('[data-testid="save-dashboard"]');

await browser.close();
```

Playwright handles project creation, task assignment, and dashboard customization automatically. You can automate time tracking, resource allocation, and progress reporting workflows.

## Scale your Wrike automation with Anchor Browser

Run your Playwright Wrike automations on cloud browsers with enterprise-grade reliability and persistent Wrike sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Zendesk
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/business-applications/zendesk

Automate Zendesk customer service workflows with Playwright when APIs aren't available.

# How to Automate Zendesk with Playwright

Automate critical Zendesk customer service workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual ticket processing and reduce response time errors by automating repetitive support processes. Use Playwright to interact with Zendesk's web interface programmatically.

[View Zendesk's API documentation](https://developer.zendesk.com/api-reference/) for integration services when available.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common Zendesk tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Login to Zendesk
await page.goto('https://your-company.zendesk.com/agent/');
await page.fill('[name="user[email]"]', process.env.ZENDESK_EMAIL);
await page.fill('[name="user[password]"]', process.env.ZENDESK_PASSWORD);
await page.click('[type="submit"]');

// Navigate to tickets
await page.click('[data-test-id="views_views-list_row-item"]');
await page.click('text=Open tickets');

// Update ticket priority
await page.click('.ticket-row:first-child');
await page.click('[data-test-id="priority-field"]');
await page.selectOption('[data-test-id="priority-field"]', 'high');

// Add internal note
await page.fill('[data-test-id="omni-composer-rich-text"]', 'Customer escalation processed - priority updated');
await page.click('[data-test-id="submit-button"]');

await browser.close();

```

Playwright handles ticket loading, field updates, and comment submissions automatically. You can automate ticket routing, bulk status updates, and customer communication workflows.

## Scale your Zendesk automation with Anchor Browser

Run your Playwright Zendesk automations on cloud browsers with enterprise-grade reliability and persistent Zendesk sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Apache Superset
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/e2e-testing/apache-superset

Test Apache Superset dashboards and data visualization workflows with Playwright's end-to-end testing framework.

# How to Test Apache Superset with Playwright

Test your Apache Superset dashboards and data exploration workflows with Playwright's end-to-end testing framework. You'll catch visualization errors and ensure data accuracy by testing charts and filters in a real browser environment. Use Playwright to automate dashboard interactions and validate SQL queries.

[View Superset's Playwright configuration](https://github.com/apache/superset/blob/master/superset-frontend/playwright.config.ts) from the official repository.

## Setup

Install Playwright and configure for Superset testing:

```bash theme={null}
npm install playwright
```

## Write Tests

Create tests for dashboard and chart functionality:

```JavaScript theme={null}
import { test, expect } from '@playwright/test';

test('dashboard loads with correct charts', async ({ page }) => {
  await page.goto('http://localhost:8088/superset/dashboard/1/');
  
  // Login if required
  await page.fill('[name="username"]', 'admin');
  await page.fill('[name="password"]', 'admin');
  await page.click('[type="submit"]');
  
  // Verify dashboard elements
  await expect(page.locator('.dashboard-header')).toBeVisible();
  await expect(page.locator('.chart-container')).toHaveCount(4);
});

test('chart filters update data correctly', async ({ page }) => {
  await page.goto('http://localhost:8088/explore/');
  
  // Apply filter
  await page.click('[data-test="adhoc-filter-edit"]');
  await page.selectOption('[data-test="select-column"]', 'category');
  await page.fill('[data-test="filter-value"]', 'Technology');
  await page.click('[data-test="run-query"]');
  
  // Verify filtered results
  await expect(page.locator('.slice_container')).toContainText('Technology');
});
```

Playwright handles chart rendering, filter interactions, and SQL query execution automatically. You can test custom visualizations, dashboard permissions, and data source connections.

## Scale your Apache Superset testing with Anchor Browser

Run your Playwright Superset tests on cloud browsers with enterprise-grade reliability and persistent database connections. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Grafana
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/e2e-testing/grafana

Test Grafana dashboards and monitoring workflows with Playwright's end-to-end testing framework.

# How to Test Grafana with Playwright

Test your Grafana dashboards and monitoring workflows with Playwright's end-to-end testing framework. You'll catch visualization bugs and ensure critical alerts work correctly by testing in a real browser environment. Use Playwright to automate dashboard interactions and validate data accuracy.

[View Grafana's Playwright configuration](https://github.com/grafana/grafana/blob/main/playwright.config.ts) from the official repository.

## Setup

Install Playwright and configure for Grafana testing:

```bash theme={null}
npm install playwright
```

## Write Tests

Create tests for dashboard functionality:

```JavaScript theme={null}
import { test, expect } from '@playwright/test';

test('dashboard loads with correct panels', async ({ page }) => {
  await page.goto('http://localhost:3000/d/dashboard-id');
  
  // Login if required
  await page.fill('[name="user"]', 'admin');
  await page.fill('[name="password"]', 'admin');
  await page.click('[type="submit"]');
  
  // Verify dashboard elements
  await expect(page.locator('.panel-title')).toContainText('CPU Usage');
  await expect(page.locator('.graph-panel')).toBeVisible();
});

test('alert rule triggers correctly', async ({ page }) => {
  await page.goto('http://localhost:3000/alerting/list');
  
  // Check alert status
  await expect(page.locator('[data-testid="alert-rule"]')).toBeVisible();
  await expect(page.locator('.alert-state-ok')).toContainText('OK');
});
```

Playwright handles dashboard loading, data refresh cycles, and alert state changes automatically. You can test panel configurations, data source connections, and user permissions.

## Scale your Grafana testing with Anchor Browser

Run your Playwright Grafana tests on cloud browsers with enterprise-grade reliability and persistent authentication sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# OpenHands
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/e2e-testing/openhands

Test OpenHands' AI-driven software development workflows with Playwright's end-to-end testing framework.

# How to Test OpenHands with Playwright

Test your OpenHands AI development workflows with Playwright's end-to-end testing framework. You'll catch UI bugs and ensure agent interactions work correctly by testing in a real browser environment. Use Playwright to automate chat interactions and validate code generation features.

[View OpenHands' Playwright configuration](https://github.com/All-Hands-AI/OpenHands/blob/main/frontend/playwright.config.ts) from the official repository.

## Setup

Install Playwright and configure for OpenHands testing:

```bash theme={null}
npm install playwright
```

## Write Tests

Create tests for AI agent functionality:

```JavaScript theme={null}
import { test, expect } from '@playwright/test';

test('chat interface loads and responds', async ({ page }) => {
  await page.goto('http://localhost:3000');
  
  // Verify chat interface is ready
  await expect(page.locator('[data-testid="chat-input"]')).toBeVisible();
  await expect(page.locator('[data-testid="send-button"]')).toBeEnabled();
  
  // Send a message to the agent
  await page.fill('[data-testid="chat-input"]', 'Create a simple Python function');
  await page.click('[data-testid="send-button"]');
  
  // Verify agent response appears
  await expect(page.locator('.agent-response')).toBeVisible();
  await expect(page.locator('.code-block')).toContainText('def');
});

test('file explorer functionality works', async ({ page }) => {
  await page.goto('http://localhost:3000');
  
  // Test file tree navigation
  await page.click('[data-testid="file-explorer"]');
  await expect(page.locator('.file-tree')).toBeVisible();
  
  // Create new file through UI
  await page.click('[data-testid="new-file-button"]');
  await page.fill('[data-testid="file-name-input"]', 'test.py');
  await page.click('[data-testid="confirm-button"]');
  
  // Verify file appears in explorer
  await expect(page.locator('text=test.py')).toBeVisible();
});
```

Playwright handles agent response timing, code syntax highlighting, and file system interactions automatically. You can test multi-step workflows, error handling, and agent memory persistence.

## Scale your OpenHands testing with Anchor Browser

Run your Playwright OpenHands tests on cloud browsers with enterprise-grade reliability and persistent authentication sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Storybook
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/e2e-testing/storybook

Test Storybook components with Playwright's component testing framework.

# How to Test Storybook with Playwright

Test your Storybook components directly with Playwright's component testing framework. You'll catch UI bugs early by testing components in a real browser environment. Use Storybook's experimental Playwright integration to mount and interact with your stories.

[View the complete example](https://github.com/storybookjs/storybook/blob/795e05c3e6a72d7de10fbb2f4cb309e4dd333f46/docs/_snippets/portable-stories-playwright-ct.md) from the Storybook project.

## Setup

Install the required packages:

```bash theme={null}
npm install @storybook/react/experimental-playwright @playwright/experimental-ct-react
```

## Write Tests

Create tests that mount your stories:

```JavaScript theme={null}
import { createTest } from '@storybook/react/experimental-playwright';
import { test as base } from '@playwright/experimental-ct-react';
import stories from './Button.stories.portable';

const test = createTest(base);

test('renders primary button', async ({ mount }) => {
  await mount(<stories.Primary />);
});

test('renders with custom props', async ({ mount }) => {
  const component = await mount(<stories.Primary label="custom label" />);
  await expect(component).toContainText('custom label');
});

```

The `mount` function executes your story's loaders, render, and play functions automatically. You can override props and test different component states.

## Scale your Storybook testing with Anchor Browser

Run your Playwright component tests on cloud browsers with enterprise-grade reliability and performance. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Twenty
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/e2e-testing/twenty

Test Twenty CRM workflows with Playwright's end-to-end testing framework.

# How to Test Twenty with Playwright

Test your Twenty CRM workflows with Playwright's end-to-end testing framework. You'll catch UI bugs and ensure contact management works correctly by testing in a real browser environment. Use Playwright to automate lead creation, pipeline management, and data validation features.

[View Twenty's Playwright configuration](https://github.com/twentyhq/twenty/blob/main/packages/twenty-e2e-testing/playwright.config.ts) from the official repository.

## Setup

Install Playwright and configure for Twenty testing:

```bash theme={null}
npm install playwright
```

## Write Tests

Create tests for CRM functionality:

```JavaScript theme={null}
import { test, expect } from '@playwright/test';

test('creates new contact successfully', async ({ page }) => {
  await page.goto('http://localhost:3000');
  
  // Navigate to contacts
  await page.click('[data-testid="nav-contacts"]');
  await expect(page.locator('[data-testid="contacts-table"]')).toBeVisible();
  
  // Create new contact
  await page.click('[data-testid="add-contact-button"]');
  await page.fill('[data-testid="contact-first-name"]', 'John');
  await page.fill('[data-testid="contact-last-name"]', 'Doe');
  await page.fill('[data-testid="contact-email"]', 'john.doe@example.com');
  await page.click('[data-testid="save-contact"]');
  
  // Verify contact appears in list
  await expect(page.locator('text=John Doe')).toBeVisible();
});

test('manages sales pipeline correctly', async ({ page }) => {
  await page.goto('http://localhost:3000/opportunities');
  
  // Create new opportunity
  await page.click('[data-testid="add-opportunity"]');
  await page.fill('[data-testid="opportunity-name"]', 'Enterprise Deal');
  await page.fill('[data-testid="opportunity-amount"]', '50000');
  await page.selectOption('[data-testid="opportunity-stage"]', 'qualification');
  await page.click('[data-testid="save-opportunity"]');
  
  // Verify opportunity in pipeline
  await expect(page.locator('.pipeline-stage')).toContainText('Enterprise Deal');
});
```

Playwright handles dynamic loading, form validations, and state updates automatically. You can test contact imports, task management, and custom field configurations.

## Scale your Twenty testing with Anchor Browser

Run your Playwright Twenty tests on cloud browsers with enterprise-grade reliability and persistent authentication sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# BLM Form 3510
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/blm-3510

Automate BLM mineral operations reporting workflows with Playwright when APIs aren't available.

# How to Automate BLM Form 3510 with Playwright

Automate critical BLM mineral operations reporting workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual lease documentation and reduce compliance errors by automating repetitive mineral rights declaration processes. Use Playwright to interact with BLM's minerals management system programmatically.

[View BLM's developer resources](https://www.blm.gov/) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [BLM Form 3510](https://www.blm.gov/sites/blm.gov/files/uploads/Services_National-Operations-Center_Eforms_Fluid-and-Solid-Minerals_3510-001.pdf) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to BLM minerals system
await page.goto('https://www.blm.gov/services/electronic-forms');

// Start new mineral operations report
await page.click('[data-testid="new-form-3510"]');
await page.selectOption('[name="report_type"]', 'drilling_operations');

// Lease information
await page.fill('[name="lease_serial_number"]', 'NM-12345-67890');
await page.fill('[name="operator_number"]', 'OP-98765');
await page.selectOption('[name="state"]', 'NM');
await page.fill('[name="county"]', 'Eddy');

// Operator information
await page.fill('[name="operator_name"]', 'Southwest Energy Resources LLC');
await page.fill('[name="operator_address"]', '456 Oil Field Road');
await page.fill('[name="operator_city"]', 'Carlsbad');
await page.selectOption('[name="operator_state"]', 'NM');
await page.fill('[name="operator_zip"]', '88220');

// Well information
await page.fill('[name="well_name"]', 'Federal Well #1');
await page.fill('[name="api_number"]', '30-015-12345');
await page.selectOption('[name="well_type"]', 'oil');
await page.fill('[name="spud_date"]', '10/01/2024');
await page.fill('[name="total_depth"]', '8500');

// Production data
await page.fill('[name="oil_production_bbls"]', '1250');
await page.fill('[name="gas_production_mcf"]', '5600');
await page.fill('[name="water_production_bbls"]', '450');
await page.selectOption('[name="reporting_month"]', '11');
await page.fill('[name="reporting_year"]', '2024');

// Surface operations
await page.fill('[name="surface_disturbance_acres"]', '5.2');
await page.check('[name="reclamation_required"]');
await page.fill('[name="reclamation_bond_amount"]', '50000');

// Certification and submission
await page.check('[name="certify_accuracy"]');
await page.fill('[name="certifier_name"]', 'Robert Operations Manager');
await page.fill('[name="certifier_title"]', 'Operations Manager');
await page.click('[data-testid="submit-report"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles lease validation, production calculations, and BLM submission processes automatically. You can automate monthly reporting, lease modifications, and environmental compliance workflows.

## Scale your BLM Form 3510 automation with Anchor Browser

Run your Playwright BLM automations on cloud browsers with enterprise-grade reliability and persistent minerals management sessions. Learn more and get started for free: Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# BOP Form BP-S0243
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/bop-s243

Automate Bureau of Prisons inmate request workflows with Playwright when APIs aren't available.

# How to Automate BOP Form BP-S0243 with Playwright

Automate Bureau of Prisons administrative request workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual inmate records processing and reduce administrative delays by automating repetitive BOP filing processes. Use Playwright to interact with BOP's TRULINCS system programmatically.

[View BOP's developer resources](https://www.bop.gov/resources/) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [BOP Form BP-S0243](https://www.bop.gov/policy/forms/BP_A0243.pdf) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to Bureau of Prisons website
await page.goto('https://www.bop.gov/mobile/policy/forms.jsp');

// Start new BP-S0243 request
await page.click('[data-testid="new-form-s0243"]');
await page.selectOption('[name="request_type"]', 'administrative_remedy');

// Inmate information
await page.fill('[name="register_number"]', '12345-678');
await page.fill('[name="inmate_name"]', 'Smith, John Michael');
await page.fill('[name="date_of_birth"]', '06/20/1980');
await page.selectOption('[name="facility"]', 'FCI_TERMINAL_ISLAND');
await page.fill('[name="unit"]', 'B-2');
await page.fill('[name="cell_number"]', '215');

// Request details
await page.selectOption('[name="subject_category"]', 'medical_services');
await page.fill('[name="request_title"]', 'Request for Specialist Consultation');
await page.fill('[name="request_date"]', '01/15/2025');

// Statement of facts
await page.fill('[name="statement_of_facts"]', 'Requested medical consultation with orthopedic specialist on 12/01/2024. No appointment scheduled after 45 days. Medical staff acknowledged request but provided no timeline.');

// Relief requested
await page.fill('[name="relief_sought"]', 'Schedule consultation with orthopedic specialist within 30 days to address ongoing knee injury documented in medical records.');

// Supporting documentation
await page.check('[name="attachments_included"]');
await page.click('[data-testid="upload-supporting-docs"]');
await page.setInputFiles('[name="supporting_documents"]', './documents/medical_request_form.pdf');

// Previous attempts to resolve
await page.selectOption('[name="informal_resolution_attempted"]', 'yes');
await page.fill('[name="informal_resolution_date"]', '12/15/2024');
await page.fill('[name="staff_contacted"]', 'Medical Unit Manager Thompson');
await page.fill('[name="resolution_outcome"]', 'No resolution provided. Staff stated request was pending review.');

// Witness information (if applicable)
await page.fill('[name="witness_name"]', 'Johnson, Robert');
await page.fill('[name="witness_register"]', '98765-432');
await page.fill('[name="witness_unit"]', 'B-2');

// Emergency request designation
await page.check('[name="expedited_review"]');
await page.fill('[name="expedited_justification"]', 'Ongoing pain affecting daily activities and work assignment performance.');

// Signature and certification
await page.check('[name="certify_accuracy"]');
await page.fill('[name="signature_name"]', 'John Michael Smith');
await page.fill('[name="signature_date"]', '01/15/2025');
await page.fill('[name="register_number_confirm"]', '12345-678');
await page.click('[data-testid="submit-request"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles request categorization, documentation attachment, and BOP submission processes automatically. You can automate remedy requests, appeal filings, and administrative tracking workflows.

## Scale your BOP Form BP-S0243 automation with Anchor Browser

Run your Playwright BOP automations on cloud browsers with enterprise-grade reliability and persistent federal corrections system sessions.

Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# CBP Form 7501
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/cbp-7501

Automate CBP Form 7501 entry documentation workflows with Playwright when APIs aren't available.

# How to Automate CBP Form 7501 with Playwright

Automate critical CBP Form 7501 entry documentation workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual customs entry processing and reduce import clearance delays by automating repetitive trade compliance processes. Use Playwright to interact with CBP's entry system programmatically.

[View CBP's developer resources](https://www.cbp.gov/trade/automated/getting-started) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [CBP Form 7501](https://www.cbp.gov/sites/default/files/2025-07/CBP_Form_7501.pdf) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to CBP website
await page.goto('https://www.cbp.gov/document/forms/form-7501-entry-summary-continuation-sheets');

// Start new entry filing
await page.click('[data-testid="new-entry"]');
await page.selectOption('[name="entry_type"]', 'consumption');

// Entry summary information
await page.fill('[name="entry_number"]', '12345678901');
await page.selectOption('[name="port_of_entry"]', '2704'); // Port of Los Angeles
await page.fill('[name="entry_date"]', '12/15/2024');
await page.fill('[name="import_date"]', '12/14/2024');

// Importer information
await page.fill('[name="importer_name"]', 'Global Trade Solutions Inc');
await page.fill('[name="importer_address"]', '456 Commerce St');
await page.fill('[name="importer_city"]', 'Los Angeles');
await page.selectOption('[name="importer_state"]', 'CA');
await page.fill('[name="importer_zip"]', '90210');
await page.fill('[name="importer_ein"]', '12-3456789');

// Transportation details
await page.fill('[name="vessel_name"]', 'MSC MAYA');
await page.fill('[name="voyage_number"]', '024W');
await page.fill('[name="bill_of_lading"]', 'MSCU1234567890');
await page.selectOption('[name="country_of_origin"]', 'CN');

// Merchandise line items
await page.click('[data-testid="add-line-item"]');
await page.fill('[name="line_number"]', '1');
await page.fill('[name="hts_number"]', '6204.62.4040');
await page.fill('[name="merchandise_description"]', 'Women cotton trousers');
await page.fill('[name="quantity"]', '500');
await page.selectOption('[name="unit_of_measure"]', 'DZ'); // Dozen
await page.fill('[name="entered_value"]', '12500.00');

// Duty and fee calculations
await page.fill('[name="duty_rate"]', '16.6');
await page.click('[data-testid="calculate-duties"]');
await page.waitForSelector('[data-testid="duty-amount"]');

// Broker certification
await page.fill('[name="broker_name"]', 'ABC Customs Brokerage');
await page.fill('[name="broker_license"]', '12345');
await page.check('[name="certify_accuracy"]');

// Submit entry
await page.click('[data-testid="submit-entry"]');
await page.waitForSelector('[data-testid="entry-confirmation"]');

// Download entry summary
await page.click('[data-testid="download-summary"]');

await browser.close();
```

Playwright handles HTS code validation, duty calculations, and customs submission processes automatically. You can automate entry modifications, drawback claims, and trade compliance reporting workflows.

## Scale your CBP Form 7501 automation with Anchor Browser

Run your Playwright EPA automations on cloud browsers with enterprise-grade reliability and persistent environmental compliance sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# CCC Form 941
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/ccc-941

Automate USDA farm program income certification workflows with Playwright when APIs aren't available.

# How to Automate CCC Form 941 with Playwright

Automate USDA average adjusted gross income (AGI) certification workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual farm program eligibility documentation and reduce compliance errors by automating repetitive income certification processes. Use Playwright to interact with USDA's farmers.gov system programmatically.

[View USDA's developer resources](https://www.farmers.gov/#tools) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [CCC Form 941](https://www.farmers.gov/sites/default/files/documents/form-ccc-941.pdf) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to farmers.gov system
await page.goto('https://www.farmers.gov/working-with-us/common-forms');

// Start new CCC-941 certification
await page.click('[data-testid="new-form-941"]');
await page.selectOption('[name="certification_year"]', '2024');

// Producer information
await page.fill('[name="producer_name"]', 'Johnson Family Farms LLC');
await page.fill('[name="tax_id"]', '12-3456789');
await page.fill('[name="farm_number"]', 'IA-045-678');
await page.fill('[name="tract_number"]', '1234');

// Contact information
await page.fill('[name="address"]', '789 County Road 45');
await page.fill('[name="city"]', 'Des Moines');
await page.selectOption('[name="state"]', 'IA');
await page.fill('[name="zip"]', '50310');
await page.fill('[name="phone"]', '515-555-0123');
await page.fill('[name="email"]', 'operations@johnsonfarms.com');

// AGI certification - three-year average
await page.fill('[name="agi_year_1"]', '2021');
await page.fill('[name="agi_amount_1"]', '675000');
await page.fill('[name="agi_year_2"]', '2022');
await page.fill('[name="agi_amount_2"]', '720000');
await page.fill('[name="agi_year_3"]', '2023');
await page.fill('[name="agi_amount_3"]', '695000');

// Certification statement
await page.check('[name="certify_below_900k"]');
await page.fill('[name="average_agi"]', '696667');

// Farm income breakdown
await page.fill('[name="farm_income_percentage"]', '85');
await page.fill('[name="non_farm_income_percentage"]', '15');

// Program eligibility
await page.check('[name="arc_plc_eligible"]');
await page.check('[name="conservation_eligible"]');
await page.check('[name="disaster_eligible"]');

// Spouse information (if applicable)
await page.check('[name="spouse_separate_filing"]');
await page.fill('[name="spouse_name"]', 'Mary Johnson');
await page.fill('[name="spouse_tax_id"]', '98-7654321');

// Signature and certification
await page.check('[name="certify_accuracy"]');
await page.fill('[name="signature_name"]', 'Robert Johnson');
await page.fill('[name="signature_title"]', 'Managing Partner');
await page.fill('[name="signature_date"]', '12/15/2024');
await page.click('[data-testid="submit-certification"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles AGI calculations, eligibility verification, and USDA submission processes automatically. You can automate annual certifications, multi-entity filings, and program payment tracking workflows.

## Scale your CCC Form 941 automation with Anchor Browser

Run your Playwright USDA automations on cloud browsers with enterprise-grade reliability and persistent farm program sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# CMS Form 10069
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/cms-10069

Automate Medicare provider enrollment and certification workflows with Playwright when APIs aren't available.

# How to Automate CMS Form 10069 with Playwright

Automate CMS Medicare provider enrollment and certification workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual credentialing processes and reduce enrollment delays by automating repetitive Medicare provider application workflows. Use Playwright to interact with CMS's Provider Enrollment, Chain, and Ownership System (PECOS) programmatically.

[View CMS developer resources](https://data.cms.gov/provider-data/) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [CMS Form 10069](https://www.cms.gov/medicare/cms-forms/cms-forms/downloads/cms10069.pdf) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to CMS PECOS system
await page.goto('https://www.cms.gov/medicare/forms-notices/cms-forms-list');

// Start new provider enrollment application
await page.click('[data-testid="new-enrollment"]');
await page.selectOption('[name="provider_type"]', 'physician');

// Provider information
await page.fill('[name="npi_number"]', '1234567890');
await page.fill('[name="first_name"]', 'Sarah');
await page.fill('[name="middle_name"]', 'Elizabeth');
await page.fill('[name="last_name"]', 'Williams');
await page.fill('[name="ssn"]', '123-45-6789');
await page.fill('[name="date_of_birth"]', '04/12/1978');

// Contact information
await page.fill('[name="practice_address"]', '456 Medical Plaza, Suite 200');
await page.fill('[name="city"]', 'Houston');
await page.selectOption('[name="state"]', 'TX');
await page.fill('[name="zip"]', '77002');
await page.fill('[name="phone"]', '713-555-0147');
await page.fill('[name="fax"]', '713-555-0148');
await page.fill('[name="email"]', 'swilliams@houstonmedical.com');

// Practice information
await page.fill('[name="practice_name"]', 'Houston Medical Associates');
await page.fill('[name="tax_id"]', '12-3456789');
await page.selectOption('[name="organization_type"]', 'professional_corporation');
await page.fill('[name="group_npi"]', '9876543210');

// Specialty and certification
await page.selectOption('[name="primary_specialty"]', 'internal_medicine');
await page.selectOption('[name="board_certification"]', 'abim');
await page.fill('[name="certification_date"]', '06/15/2005');
await page.fill('[name="certification_expiration"]', '06/15/2025');

// Medical education
await page.fill('[name="medical_school"]', 'Baylor College of Medicine');
await page.fill('[name="graduation_year"]', '2002');
await page.fill('[name="residency_program"]', 'Massachusetts General Hospital');
await page.fill('[name="residency_completion"]', '2005');

// License information
await page.fill('[name="license_number"]', 'TX-M12345');
await page.selectOption('[name="license_state"]', 'TX');
await page.fill('[name="license_issue_date"]', '07/01/2005');
await page.fill('[name="license_expiration"]', '07/01/2026');
await page.check('[name="license_active_status"]');

// Medicare enrollment
await page.selectOption('[name="enrollment_type"]', 'initial');
await page.fill('[name="effective_date"]', '02/01/2025');
await page.check('[name="opt_in_assignment"]');

// Practice locations
await page.click('[data-testid="add-practice-location"]');
await page.fill('[name="location_address"]', '789 Community Health Center');
await page.fill('[name="location_city"]', 'Katy');
await page.selectOption('[name="location_state"]', 'TX');
await page.fill('[name="location_zip"]', '77494');
await page.fill('[name="location_phone"]', '281-555-0199');

// Hospital affiliations
await page.fill('[name="hospital_name"]', 'Memorial Hermann Hospital');
await page.fill('[name="hospital_npi"]', '5555555555');
await page.selectOption('[name="admitting_privileges"]', 'active');

// Malpractice insurance
await page.fill('[name="insurance_carrier"]', 'Texas Medical Liability Trust');
await page.fill('[name="policy_number"]', 'TMLT-2024-789456');
await page.fill('[name="coverage_amount"]', '1000000');
await page.fill('[name="policy_effective']', '01/01/2024');
await page.fill('[name="policy_expiration"]', '12/31/2024');

// Background information
await page.selectOption('[name="felony_conviction"]', 'no');
await page.selectOption('[name="license_revocation"]', 'no');
await page.selectOption('[name="medicare_sanctions"]', 'no');
await page.selectOption('[name="medicaid_exclusion"]', 'no');

// Banking information for EFT
await page.fill('[name="bank_name"]', 'Wells Fargo Bank');
await page.fill('[name="routing_number"]', '111000025');
await page.fill('[name="account_number"]', '1234567890123');
await page.selectOption('[name="account_type"]', 'checking');

// Supporting documentation
await page.click('[data-testid="upload-medical-license"]');
await page.setInputFiles('[name="license_document"]', './documents/tx_medical_license.pdf');
await page.click('[data-testid="upload-board-certification"]');
await page.setInputFiles('[name="certification_document"]', './documents/abim_certificate.pdf');
await page.click('[data-testid="upload-malpractice-insurance"]');
await page.setInputFiles('[name="insurance_document"]', './documents/malpractice_policy.pdf');

// Signature and certification
await page.check('[name="certify_accuracy"]');
await page.check('[name="agree_to_terms"]');
await page.fill('[name="signature_name"]', 'Sarah Elizabeth Williams MD');
await page.fill('[name="signature_title"]', 'Physician');
await page.fill('[name="signature_date"]', '01/20/2025');
await page.click('[data-testid="submit-enrollment"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles credential verification, documentation upload, and CMS submission processes automatically. You can automate provider enrollments, revalidation filings, and practice location updates workflows.

## Scale your CMS Form 10069 automation with Anchor Browser

Run your Playwright CMS automations on cloud browsers with enterprise-grade reliability and persistent Medicare enrollment sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# DOE Form 1845-0031
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/doe-1845-0031

Automate federal student loan forbearance request workflows with Playwright when APIs aren't available.

# How to Automate DOE Form 1845-0031 with Playwright

Automate federal student loan general forbearance request workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual forbearance application processing and reduce approval delays by automating repetitive student loan relief processes. Use Playwright to interact with Federal Student Aid systems programmatically.

[View Federal Student Aid developer resources](https://studentaid.gov/data-center/) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [DOE Form 1845-0031](https://studentaid.gov/sites/default/files/GeneralForbearance.pdf) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to Department of Education website
await page.goto('https://www.ed.gov/grants-and-programs/apply-grant/grant-application-and-other-forms');

// Start new forbearance request
await page.click('[data-testid="manage-loans"]');
await page.click('[data-testid="request-forbearance"]');
await page.selectOption('[name="forbearance_type"]', 'general_discretionary');

// Borrower information
await page.fill('[name="first_name"]', 'Jennifer');
await page.fill('[name="middle_initial"]', 'L');
await page.fill('[name="last_name"]', 'Martinez');
await page.fill('[name="ssn"]', '987-65-4321');
await page.fill('[name="date_of_birth"]', '08/25/1995');

// Contact information
await page.fill('[name="address"]', '234 University Avenue, Apt 5C');
await page.fill('[name="city"]', 'Austin');
await page.selectOption('[name="state"]', 'TX');
await page.fill('[name="zip"]', '78705');
await page.fill('[name="phone"]', '512-555-0176');
await page.fill('[name="email"]', 'j.martinez@email.com');

// Loan servicer information
await page.selectOption('[name="loan_servicer"]', 'nelnet');
await page.fill('[name="servicer_account_number"]', '1234567890');

// Forbearance request details
await page.selectOption('[name="reason"]', 'financial_hardship');
await page.fill('[name="requested_start_date"]', '02/01/2025');
await page.selectOption('[name="requested_duration"]', '12_months');

// Financial hardship details
await page.fill('[name="monthly_income"]', '2400');
await page.fill('[name="monthly_expenses"]', '2650');
await page.fill('[name="total_loan_balance"]', '45000');
await page.fill('[name="monthly_loan_payment"]', '485');

// Employment status
await page.selectOption('[name="employment_status"]', 'employed_part_time');
await page.fill('[name="employer_name"]', 'Downtown Coffee Shop');
await page.fill('[name="hours_per_week"]', '25');
await page.fill('[name="employment_start_date"]', '11/15/2024');

// Hardship explanation
await page.fill('[name="hardship_explanation"]', 'Reduced work hours due to business downsizing. Currently seeking full-time employment while maintaining part-time position. Unable to meet loan payment obligations without forbearance.');

// Loan types to include
await page.check('[name="include_direct_loans"]');
await page.check('[name="include_ffel_loans"]');
await page.check('[name="subsidized_loans"]');
await page.check('[name="unsubsidized_loans"]');

// Interest capitalization acknowledgment
await page.check('[name="understand_interest_accrual"]');
await page.check('[name="understand_capitalization"]');
await page.check('[name="acknowledge_payment_increase"]');

// Alternative options reviewed
await page.check('[name="reviewed_income_driven"]');
await page.check('[name="reviewed_deferment"]');
await page.check('[name="reviewed_consolidation"]');

// Supporting documentation
await page.click('[data-testid="upload-income-docs"]');
await page.setInputFiles('[name="income_verification"]', './documents/paystubs_recent.pdf');
await page.click('[data-testid="upload-expense-docs"]');
await page.setInputFiles('[name="expense_documentation"]', './documents/monthly_bills.pdf');

// Notification preferences
await page.check('[name="email_notifications"]');
await page.check('[name="sms_notifications"]');
await page.fill('[name="mobile_number"]', '512-555-0176');

// Signature and certification
await page.check('[name="certify_accuracy"]');
await page.check('[name="authorize_credit_check"]');
await page.fill('[name="signature_name"]', 'Jennifer L Martinez');
await page.fill('[name="signature_date"]', '01/25/2025');
await page.click('[data-testid="submit-request"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles eligibility verification, documentation upload, and Federal Student Aid submission processes automatically. You can automate forbearance renewals, servicer communications, and repayment plan transitions workflows.

## Scale your DOE Form 1845-0031 automation with Anchor Browser

Run your Playwright Federal Student Aid automations on cloud browsers with enterprise-grade reliability and persistent loan servicing sessions. [https://anchorbrowser.io](https://anchorbrowser.io)


# DOJ Form 361
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/doj-361

Automate Department of Justice identity certification workflows with Playwright when APIs aren't available.

# How to Automate DOJ Form 361 with Playwright

Automate Department of Justice identity certification workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual FOIA and Privacy Act request processing and reduce verification delays by automating repetitive identity certification processes. Use Playwright to interact with DOJ records request systems programmatically.

[View Department of Justice developer resources](https://www.justice.gov/developer) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [DOJ Form 361](https://www.justice.gov/ust/file/doj361_form.pdf/dl?inline) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to Department of Justice website
await page.goto('https://www.justice.gov/forms');

// Start new identity certification
await page.click('[data-testid="new-request"]');
await page.click('[data-testid="form-361"]');
await page.selectOption('[name="request_type"]', 'privacy_act_request');

// Full name of requester
await page.fill('[name="requester_last_name"]', 'Thompson');
await page.fill('[name="requester_first_name"]', 'Rebecca');
await page.fill('[name="requester_middle_name"]', 'Anne');
await page.fill('[name="requester_suffix"]', '');

// Citizenship status
await page.selectOption('[name="citizenship_status"]', 'us_citizen');

// Social Security Number (optional but recommended)
await page.fill('[name="ssn"]', '123-45-6789');

// Current address
await page.fill('[name="address_line_1"]', '456 Constitution Avenue');
await page.fill('[name="address_line_2"]', 'Apt 12B');
await page.fill('[name="city"]', 'Washington');
await page.selectOption('[name="state"]', 'DC');
await page.fill('[name="zip"]', '20001');

// Date of birth
await page.fill('[name="date_of_birth"]', '06/14/1982');

// Place of birth
await page.fill('[name="place_of_birth_city"]', 'Philadelphia');
await page.selectOption('[name="place_of_birth_state"]', 'PA');
await page.selectOption('[name="place_of_birth_country"]', 'USA');

// Contact information
await page.fill('[name="phone"]', '202-555-0156');
await page.fill('[name="email"]', 'rthompson@email.com');

// Records being requested
await page.fill('[name="records_description"]', 'All records relating to employment with the Federal Bureau of Investigation from 2005 to 2015, including personnel files, training records, and performance evaluations.');

// Time period for records
await page.fill('[name="date_range_start"]', '01/01/2005');
await page.fill('[name="date_range_end"]', '12/31/2015');

// DOJ component
await page.selectOption('[name="doj_component"]', 'fbi');

// Optional: Authorization to release information to another person
await page.check('[name="authorize_release_to_another"]');

// Authorized person information
await page.fill('[name="authorized_person_name"]', 'David Thompson');
await page.fill('[name="authorized_relationship"]', 'Spouse');
await page.fill('[name="authorized_address"]', '456 Constitution Avenue, Apt 12B');
await page.fill('[name="authorized_city"]', 'Washington');
await page.selectOption('[name="authorized_state"]', 'DC');
await page.fill('[name="authorized_zip"]', '20001');
await page.fill('[name="authorized_phone"]', '202-555-0157');
await page.fill('[name="authorized_email"]', 'dthompson@email.com');

// Purpose of authorization
await page.fill('[name="authorization_purpose"]', 'Authorized to receive and review records on my behalf for legal proceedings.');

// Previous names (if applicable)
await page.check('[name="has_previous_names"]');
await page.fill('[name="previous_name"]', 'Rebecca Miller');
await page.fill('[name="name_change_date"]', '08/2010');

// Previous addresses (if relevant to records)
await page.check('[name="has_previous_addresses"]');
await page.fill('[name="previous_address"]', '789 Market Street, Philadelphia, PA 19107');
await page.fill('[name="previous_address_dates"]', '2005-2010');

// Employment information (if relevant)
await page.fill('[name="employer_during_period"]', 'Federal Bureau of Investigation');
await page.fill('[name="job_title"]', 'Special Agent');
await page.fill('[name="employee_id"]', 'FBI-SA-12345');
await page.fill('[name="employment_dates"]', '2005-2015');

// Identity verification documents
await page.click('[data-testid="upload-id-front"]');
await page.setInputFiles('[name="identification_front"]', './documents/drivers_license_front.pdf');
await page.click('[data-testid="upload-id-back"]');
await page.setInputFiles('[name="identification_back"]', './documents/drivers_license_back.pdf');

// Supporting documentation
await page.click('[data-testid="upload-supporting-docs"]');
await page.setInputFiles('[name="supporting_documents"]', './documents/birth_certificate.pdf');

// Notarization (if required)
await page.check('[name="notarized"]');
await page.fill('[name="notary_name"]', 'John Notary Public');
await page.fill('[name="notary_commission_number"]', 'DC-12345');
await page.fill('[name="notary_expiration"]', '12/31/2026');
await page.fill('[name="notarization_date"]', '03/15/2025');

// Fee waiver request (if applicable)
await page.selectOption('[name="fee_waiver_requested"]', 'no');

// Expedited processing request
await page.selectOption('[name="expedited_processing"]', 'yes');
await page.fill('[name="expedited_justification"]', 'Records needed for pending litigation with court-imposed deadline.');

// Certification under penalty of perjury
await page.check('[name="certify_true_and_correct"]');
await page.check('[name="certify_identity"]');
await page.check('[name="understand_penalties_false_statement"]');
await page.check('[name="understand_penalties_false_pretenses"]');

// Privacy Act acknowledgment
await page.check('[name="acknowledge_privacy_act"]');
await page.check('[name="consent_to_disclosure"]');

// Request delivery preference
await page.selectOption('[name="delivery_method"]', 'electronic');
await page.check('[name="email_notification"]');

// Declaration statement
await page.fill('[name="declaration_text"]', 'I declare under penalty of perjury under the laws of the United States of America that the foregoing is true and correct, and that I am the person named above.');

// Signature
await page.fill('[name="signature_name"]', 'Rebecca Anne Thompson');
await page.fill('[name="signature_date"]', '03/15/2025');

// Digital signature or attestation
await page.check('[name="electronic_signature_consent"]');
await page.fill('[name="electronic_signature']', 'Rebecca Anne Thompson');

// Authorized representative signature (if applicable)
await page.fill('[name="authorized_signature"]', 'David Thompson');
await page.fill('[name="authorized_signature_date"]', '03/15/2025');

// Request tracking preferences
await page.check('[name="track_request_online"]');
await page.check('[name="sms_notifications"]');
await page.fill('[name="mobile_number"]', '202-555-0156');

await page.click('[data-testid="submit-certification"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles identity verification, authorization processing, and DOJ submission processes automatically. You can automate FOIA requests, Privacy Act requests, and identity certification workflows.

## Scale your DOJ Form 361 automation with Anchor Browser

Run your Playwright DOJ automations on cloud browsers with enterprise-grade reliability and persistent PACER sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# EPA Form 8700-22
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/epa-8200

Automate EPA hazardous waste notification workflows with Playwright when APIs aren't available.

# How to Automate EPA Form 8700-22 with Playwright

Automate critical EPA hazardous waste notification workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual compliance reporting and reduce environmental violation risks by automating repetitive hazardous waste declaration processes. Use Playwright to interact with EPA's notification system programmatically.

[View EPA's developer resources](https://www.epa.gov/enviro/web-services) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [EPA Form 8700-22](https://www.epa.gov/sites/default/files/2018-05/documents/uniform_hazardous_waste_manifest.pdf) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to EPA RCRAInfo system
await page.goto('https://www.epa.gov/hwgenerators/uniform-hazardous-waste-manifest-instructions-sample-form-and-continuation-sheet');

// Start new hazardous waste notification
await page.click('[data-testid="new-notification"]');
await page.selectOption('[name="notification_type"]', 'initial');

// Facility information
await page.fill('[name="facility_name"]', 'ABC Manufacturing Plant');
await page.fill('[name="facility_address"]', '123 Industrial Blvd');
await page.fill('[name="city"]', 'Detroit');
await page.selectOption('[name="state"]', 'MI');
await page.fill('[name="zip_code"]', '48201');
await page.fill('[name="epa_id_number"]', 'MID987654321');

// Handler classification
await page.check('[name="generator"]');
await page.check('[name="transporter"]');
await page.fill('[name="estimated_annual_quantity"]', '2500');
await page.selectOption('[name="quantity_units"]', 'tons');

// Waste stream information
await page.click('[data-testid="add-waste-stream"]');
await page.selectOption('[name="waste_code"]', 'D001');
await page.fill('[name="waste_description"]', 'Ignitable waste solvents');
await page.selectOption('[name="physical_form"]', 'liquid');
await page.fill('[name="annual_quantity"]', '500');

// Contact person details
await page.fill('[name="contact_first_name"]', 'Sarah');
await page.fill('[name="contact_last_name']', 'Johnson');
await page.fill('[name="contact_title"]', 'Environmental Manager');
await page.fill('[name="contact_phone"]', '555-123-4567');
await page.fill('[name="contact_email"]', 'sarah.johnson@abcmfg.com');

// Certification and submission
await page.check('[name="certify_accuracy"]');
await page.fill('[name="certifier_name"]', 'Sarah Johnson');
await page.fill('[name="certifier_title"]', 'Environmental Manager');
await page.click('[data-testid="submit-notification"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles waste code validation, quantity calculations, and regulatory submission processes automatically. You can automate facility updates, annual reporting, and compliance tracking workflows.

## Scale your EPA Form 8700-22 automation with Anchor Browser

Run your Playwright EPA automations on cloud browsers with enterprise-grade reliability and persistent environmental compliance sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# FDA Form 2579
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/fda-2579

Automate FDA food facility registration workflows with Playwright when APIs aren't available.

# How to Automate FDA Form 2579 with Playwright

Automate critical FDA food facility registration workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual compliance paperwork and reduce food safety violation risks by automating repetitive facility registration processes. Use Playwright to interact with FDA's registration system programmatically.

[View FDA's developer resources](https://www.fda.gov/food/guidance-regulation-food-and-dietary-supplements/registration-food-facilities-and-other-submissions) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [FDA Form 2579](https://www.fda.gov/media/144454/download) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to FDA Food forms
await page.goto('https://www.fda.gov/about-fda/reports-manuals-forms/forms');

// Start new facility registration
await page.click('[data-testid="new-registration"]');
await page.selectOption('[name="registration_type"]', 'initial');

// Facility information
await page.fill('[name="facility_name"]', 'Fresh Valley Food Processing LLC');
await page.fill('[name="facility_address"]', '123 Processing Plant Road');
await page.fill('[name="city"]', 'Fresno');
await page.selectOption('[name="state"]', 'CA');
await page.fill('[name="zip_code"]', '93701');
await page.selectOption('[name="country"]', 'United States');

// Business operations
await page.check('[name="food_manufacturing"]');
await page.check('[name="food_processing"]');
await page.check('[name="food_packing"]');
await page.fill('[name="duns_number"]', '123456789');

// Food categories and processes
await page.click('[data-testid="add-food-category"]');
await page.selectOption('[name="food_category"]', 'fruits_vegetables');
await page.fill('[name="food_description"]', 'Fresh cut vegetables and salad mixes');
await page.selectOption('[name="process_type"]', 'processing_packing');

// Contact information
await page.fill('[name="contact_first_name"]', 'Maria');
await page.fill('[name="contact_last_name']', 'Rodriguez');
await page.fill('[name="contact_title']', 'Quality Assurance Manager');
await page.fill('[name="contact_phone"]', '559-123-4567');
await page.fill('[name="contact_email"]', 'maria.rodriguez@freshvalley.com');

// Emergency contact
await page.fill('[name="emergency_contact_name"]', 'David Chen');
await page.fill('[name="emergency_contact_phone"]', '559-123-4568');
await page.fill('[name="emergency_contact_email"]', 'david.chen@freshvalley.com');

// Certification and submission
await page.check('[name="certify_accuracy"]');
await page.fill('[name="certifier_name"]', 'Maria Rodriguez');
await page.fill('[name="certifier_title']', 'Quality Assurance Manager');
await page.click('[data-testid="submit-registration"]');

// Download registration confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles food category validation, contact verification, and FDA submission processes automatically. You can automate registration renewals, facility updates, and compliance tracking workflows.

## Scale your FDA Form 2579 automation with Anchor Browser

Run your Playwright FDA automations on cloud browsers with enterprise-grade reliability and persistent food safety compliance sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# FinCEN 105 (CMIR)
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/fincen-105

Automate FinCEN 105 currency reporting workflows with Playwright when APIs aren't available.

# How to Automate FinCEN 105 with Playwright

Automate critical FinCEN 105 Currency and Monetary Instrument Report workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual form completion and reduce customs reporting errors by automating repetitive currency declaration processes. Use Playwright to interact with the FinCEN 105 web interface programmatically.

[View more about FinCEN 105](https://fincen105.cbp.dhs.gov/) for available web forms when applicable.

## Setup

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [FinCEN 105](https://www.fincen.gov/system/files/shared/fin105_cmir.pdf) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to FinCEN 105 portal
await page.goto('https://www.fincen.gov/resources/filing-information');

// Start new CMIR filing
await page.click('[data-testid="new-filing-button"]');
await page.selectOption('[name="report_type"]', 'import');

// Fill traveler information
await page.fill('[name="first_name"]', 'John');
await page.fill('[name="last_name"]', 'Smith');
await page.fill('[name="date_of_birth"]', '01/15/1980');
await page.fill('[name="passport_number"]', 'A12345678');
await page.selectOption('[name="country_of_citizenship"]', 'Canada');

// Transportation details
await page.fill('[name="flight_number"]', 'AC123');
await page.fill('[name="arrival_date"]', '12/15/2024');
await page.selectOption('[name="port_of_entry"]', 'JFK');
await page.fill('[name="departure_city"]', 'Toronto, ON');

// Currency information
await page.selectOption('[name="currency_type"]', 'cash');
await page.fill('[name="currency_amount"]', '15000');
await page.selectOption('[name="currency_denomination"]', 'USD');
await page.fill('[name="source_of_funds"]', 'Business proceeds from sale');

// Submit declaration
await page.click('[name="certify_accuracy"]');
await page.fill('[name="electronic_signature"]', 'John Smith');
await page.click('[data-testid="submit-declaration"]');

// Download confirmation receipt
await page.click('[data-testid="download-receipt"]');

await browser.close();
```

Playwright handles form validation, currency calculations, and submission processes automatically. You can automate bulk filings, compliance reporting, and traveler declaration workflows.

## Scale your FinCEN 105 automation with Anchor Browser

Run your Playwright FinCEN 105 automations on cloud browsers with enterprise-grade reliability and persistent customs sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# FMCSA Form BMC-40
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/fmcsa-bmc-40

Automate motor carrier surety bond and trust fund filing workflows with Playwright when APIs aren't available.

# How to Automate FMCSA Form BMC-40 with Playwright

Automate FMCSA motor carrier surety bond and trust fund filing workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual bond filing processes and reduce operating authority delays by automating repetitive FMCSA compliance workflows. Use Playwright to interact with FMCSA's registration systems programmatically.

[View FMCSA developer resources](https://mobile.fmcsa.dot.gov/QCDevsite/docs/apiAccess) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [FMCSA Form BMC-40](https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/2025-09/BMC-40%20Form.pdf) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to FMCSA registration system
await page.goto('https://www.fmcsa.dot.gov/registration/registration-forms');

// Start new BMC-40 filing
await page.click('[data-testid="insurance-filing"]');
await page.click('[data-testid="form-bmc-40"]');
await page.selectOption('[name="filing_type"]', 'surety_bond');

// Motor carrier information
await page.fill('[name="legal_name"]', 'Midwest Transport Solutions LLC');
await page.fill('[name="dba_name"]', 'Midwest Express Freight');
await page.fill('[name="usdot_number"]', '3456789');
await page.fill('[name="mc_number"]', 'MC-987654');
await page.fill('[name="federal_ein"]', '45-6789012');

// Principal address
await page.fill('[name="address"]', '1200 Industrial Parkway');
await page.fill('[name="city"]', 'Indianapolis');
await page.selectOption('[name="state"]', 'IN');
await page.fill('[name="zip"]', '46204');
await page.fill('[name="phone"]', '317-555-0187');
await page.fill('[name="email"]', 'compliance@midwesttransport.com');

// Operating authority
await page.selectOption('[name="authority_type"]', 'property_carrier');
await page.check('[name="interstate_authority"]');
await page.fill('[name="effective_date"]', '03/01/2025');

// Surety company information
await page.fill('[name="surety_company"]', 'National Surety Corporation');
await page.fill('[name="surety_code"]', '12345');
await page.fill('[name="surety_address"]', '500 Insurance Plaza');
await page.fill('[name="surety_city"]', 'Chicago');
await page.selectOption('[name="surety_state"]', 'IL');
await page.fill('[name="surety_zip"]', '60601');
await page.fill('[name="surety_phone"]', '312-555-0145');

// Bond details
await page.fill('[name="bond_number"]', 'SB-2025-789456');
await page.fill('[name="bond_amount"]', '75000');
await page.fill('[name="bond_effective_date"]', '03/01/2025');
await page.selectOption('[name="bond_type"]', 'continuous');

// Coverage information
await page.check('[name="cargo_liability"]');
await page.check('[name="auto_liability"]');
await page.fill('[name="cargo_limit"]', '100000');
await page.fill('[name="auto_limit"]', '750000');

// Agent for service of process
await page.fill('[name="agent_name"]', 'Corporate Agents Inc');
await page.fill('[name="agent_address"]', '789 State Street');
await page.fill('[name="agent_city"]', 'Indianapolis');
await page.selectOption('[name="agent_state"]', 'IN');
await page.fill('[name="agent_zip"]', '46201');
await page.fill('[name="agent_phone"]', '317-555-0166');

// Power of attorney information
await page.fill('[name="attorney_in_fact']', 'Robert J. Anderson');
await page.fill('[name="attorney_title"]', 'Authorized Representative');
await page.fill('[name="power_of_attorney_number"]', 'POA-456789');

// Cancellation provisions
await page.selectOption('[name="cancellation_notice_days"]', '30');
await page.check('[name="continuous_until_cancelled"]');

// Claims contact information
await page.fill('[name="claims_contact_name"]', 'Jennifer Claims Manager');
await page.fill('[name="claims_phone"]', '312-555-0199');
await page.fill('[name="claims_email"]', 'claims@nationalsurety.com');
await page.fill('[name="claims_fax"]', '312-555-0200');

// Additional insured parties (if applicable)
await page.click('[data-testid="add-additional-insured"]');
await page.fill('[name="additional_insured_name"]', 'ABC Logistics Partners');
await page.fill('[name="additional_insured_address"]', '234 Commerce Drive');
await page.fill('[name="additional_insured_city"]', 'Fort Wayne');
await page.selectOption('[name="additional_insured_state"]', 'IN');
await page.fill('[name="additional_insured_zip"]', '46802');

// Filing reason
await page.selectOption('[name="filing_reason"]', 'new_authority');
await page.fill('[name="previous_bond_number"]', 'N/A');

// Broker authority (if applicable)
await page.check('[name="broker_authority"]');
await page.fill('[name="broker_bond_amount"]', '75000');
await page.fill('[name="broker_bond_number"]', 'BB-2025-789457');

// Supporting documentation
await page.click('[data-testid="upload-bond-document"]');
await page.setInputFiles('[name="bond_document"]', './documents/surety_bond_original.pdf');
await page.click('[data-testid="upload-power-of-attorney"]');
await page.setInputFiles('[name="poa_document"]', './documents/power_of_attorney.pdf');
await page.click('[data-testid="upload-certificate"]');
await page.setInputFiles('[name="certificate_document"]', './documents/insurance_certificate.pdf');

// Carrier certification
await page.check('[name="certify_financial_responsibility"]');
await page.check('[name="certify_continuous_coverage"]');
await page.check('[name="acknowledge_cancellation_terms"]');
await page.check('[name="certify_accuracy"]');

// Carrier signature
await page.fill('[name="carrier_signature_name"]', 'David Transport Owner');
await page.fill('[name="carrier_signature_title"]', 'President');
await page.fill('[name="carrier_signature_date"]', '02/01/2025');

// Surety company certification
await page.fill('[name="surety_signature_name"]', 'Robert J. Anderson');
await page.fill('[name="surety_signature_title"]', 'Authorized Representative');
await page.fill('[name="surety_signature_date"]', '02/01/2025');
await page.click('[data-testid="submit-filing"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles bond validation, surety verification, and FMCSA submission processes automatically. You can automate new authority filings, bond renewals, and coverage modification workflows.

## Scale your FMCSA Form BMC-40 automation with Anchor Browser

Run your Playwright FMCSA automations on cloud browsers with enterprise-grade reliability and persistent motor carrier registration sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# FMCSA Form OP-1
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/fmcsa-op-1

Automate motor carrier operating authority application workflows with Playwright when APIs aren't available.

# How to Automate FMCSA Form OP-1 with Playwright

Automate FMCSA motor carrier operating authority application workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual registration processes and reduce authority approval delays by automating repetitive FMCSA application workflows. Use Playwright to interact with FMCSA's Unified Registration System programmatically.

[View FMCSA developer resources](https://mobile.fmcsa.dot.gov/QCDevsite/docs/apiAccess) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [FMCSA Form OP-1](https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/2025-09/OP-1%20Form.pdf) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to FMCSA registration system
await page.goto('https://www.fmcsa.dot.gov/registration/registration-forms');

// Start new OP-1 application
await page.click('[data-testid="new-application"]');
await page.selectOption('[name="application_type"]', 'motor_carrier_authority');
await page.selectOption('[name="operation_classification"]', 'passenger_carrier');

// Legal business name
await page.fill('[name="legal_name"]', 'Premier Charter Bus Services Inc');
await page.fill('[name="dba_name"]', 'Premier Coaches');
await page.selectOption('[name="entity_type"]', 'corporation');
await page.fill('[name="state_of_incorporation"]', 'FL');
await page.fill('[name="date_of_incorporation"]', '03/20/2023');

// Tax identification
await page.fill('[name="federal_ein"]', '65-4321987');
await page.selectOption('[name="tax_status"]', 'corporation');

// Principal place of business
await page.fill('[name="business_address"]', '3400 Transportation Boulevard');
await page.fill('[name="business_suite"]', '');
await page.fill('[name="business_city"]', 'Orlando');
await page.selectOption('[name="business_state"]', 'FL');
await page.fill('[name="business_zip"]', '32801');
await page.fill('[name="business_phone"]', '407-555-0164');
await page.fill('[name="business_fax"]', '407-555-0165');
await page.fill('[name="business_email"]', 'info@premiercoaches.com');

// Mailing address
await page.check('[name="mailing_same_as_business"]');

// Ownership information
await page.click('[data-testid="add-officer"]');
await page.fill('[name="officer_name"]', 'Elizabeth Martinez');
await page.fill('[name="officer_title"]', 'President/CEO');
await page.fill('[name="officer_ownership"]', '55');
await page.fill('[name="officer_ssn"]', '456-78-9012');
await page.fill('[name="officer_address"]', '1200 Executive Circle');
await page.fill('[name="officer_city"]', 'Winter Park');
await page.selectOption('[name="officer_state"]', 'FL');
await page.fill('[name="officer_zip"]', '32789');

// Add additional officer
await page.click('[data-testid="add-officer"]');
await page.fill('[name="officer_name_2"]', 'James Rodriguez');
await page.fill('[name="officer_title_2"]', 'Vice President/CFO');
await page.fill('[name="officer_ownership_2"]', '45');
await page.fill('[name="officer_ssn_2"]', '567-89-0123');

// Operating authority requested
await page.check('[name="interstate_authority"]');
await page.selectOption('[name="carrier_type"]', 'passenger');
await page.check('[name="charter_service"]');
await page.check('[name="tour_service"]');
await page.check('[name="special_operations"]');

// Passenger service details
await page.selectOption('[name="service_type"]', 'charter_tour');
await page.fill('[name="passenger_capacity"]', '450');
await page.check('[name="wheelchair_accessible"]');
await page.fill('[name="accessible_vehicles"]', '8');

// Geographic scope
await page.check('[name="48_states"]');
await page.check('[name="canada"]');
await page.selectOption('[name="primary_service_area"]', 'southeast');

// Type of operation
await page.selectOption('[name="operating_status"]', 'new_entrant');
await page.fill('[name="operations_begin_date"]', '05/01/2025');
await page.fill('[name="estimated_annual_mileage"]', '350000');

// Fleet information
await page.fill('[name="motorcoaches_owned"]', '10');
await page.fill('[name="motorcoaches_leased"]', '2');
await page.fill('[name="minibuses_owned"]', '3');
await page.fill('[name="vans_owned"]', '5');
await page.fill('[name="total_seating_capacity"]', '450');
await page.fill('[name="drivers_employed"]', '15');

// Vehicle specifications
await page.fill('[name="average_vehicle_age"]', '3');
await page.fill('[name="newest_vehicle_year"]', '2024');
await page.fill('[name="oldest_vehicle_year"]', '2019');

// MCS-150 mileage information
await page.fill('[name="total_annual_mileage"]', '350000');
await page.fill('[name="vehicle_miles_us"]', '330000');
await page.fill('[name="vehicle_miles_canada"]', '20000');
await page.fill('[name="vehicle_miles_mexico"]', '0');

// Safety management information
await page.fill('[name="safety_director_name"]', 'Michael Safety Director');
await page.fill('[name="safety_director_phone"]', '407-555-0170');
await page.fill('[name="safety_director_email"]', 'safety@premiercoaches.com');
await page.check('[name="drug_testing_program"]');
await page.check('[name="alcohol_testing_program"]');

// Driver qualification files
await page.check('[name="maintains_driver_files"]');
await page.fill('[name="driver_file_location"]', '3400 Transportation Boulevard, Orlando FL 32801');

// Process agent designation
await page.fill('[name="process_agent_name"]', 'Florida Registered Agents LLC');
await page.fill('[name="process_agent_address"]', '678 Legal Plaza');
await page.fill('[name="process_agent_city"]', 'Tallahassee');
await page.selectOption('[name="process_agent_state"]', 'FL');
await page.fill('[name="process_agent_zip"]', '32301');
await page.fill('[name="process_agent_phone"]', '850-555-0188');

// Unified Carrier Registration
await page.check('[name="ucr_participation"]');
await page.selectOption('[name="ucr_tier"]', 'tier_2');
await page.fill('[name="ucr_year"]', '2025');

// Liability insurance
await page.fill('[name="insurance_carrier"]', 'National Transit Insurance Company');
await page.fill('[name="insurance_policy"]', 'NTIC-2025-PC-789456');
await page.fill('[name="liability_coverage"]', '5000000');
await page.fill('[name="insurance_effective_date"]', '05/01/2025');
await page.fill('[name="insurance_agent_name"]', 'Sarah Insurance Agent');
await page.fill('[name="insurance_agent_phone"]', '407-555-0199');

// Additional insurance coverage
await page.check('[name="physical_damage_coverage"]');
await page.fill('[name="physical_damage_amount"]', '2500000');
await page.check('[name="medical_payments"]');
await page.fill('[name="medical_payments_limit"]', '5000');

// USDOT PIN creation
await page.fill('[name="pin_password"]', process.env.USDOT_PIN);
await page.fill('[name="pin_confirm"]', process.env.USDOT_PIN);
await page.fill('[name="security_question_1"]', 'What city were you born in?');
await page.fill('[name="security_answer_1"]', process.env.SECURITY_ANSWER_1);
await page.fill('[name="security_question_2"]', 'What was your first pet\'s name?');
await page.fill('[name="security_answer_2"]', process.env.SECURITY_ANSWER_2);

// Background information
await page.selectOption('[name="prior_authority"]', 'no');
await page.selectOption('[name="revoked_authority"]', 'no');
await page.selectOption('[name="safety_rating"]', 'none');
await page.selectOption('[name="out_of_service"]', 'no');
await page.selectOption('[name="bankruptcy_proceedings"]', 'no');

// Criminal history disclosure
await page.selectOption('[name="felony_convictions"]', 'no');
await page.selectOption('[name="officer_convictions"]', 'no');

// State operating authority
await page.check('[name="state_authority_florida"]');
await page.fill('[name="fl_permit_number"]', 'FL-PC-456789');
await page.check('[name="additional_state_authority"]');
await page.fill('[name="states_authorized"]', 'GA, AL, SC, NC, TN');

// Contact person for application
await page.fill('[name="contact_name"]', 'Elizabeth Martinez');
await page.fill('[name="contact_title"]', 'President/CEO');
await page.fill('[name="contact_phone"]', '407-555-0164');
await page.fill('[name="contact_email"]', 'emartinez@premiercoaches.com');

// Supporting documentation
await page.click('[data-testid="upload-articles-incorporation"]');
await page.setInputFiles('[name="incorporation_documents"]', './documents/articles_of_incorporation.pdf');
await page.click('[data-testid="upload-ein-letter"]');
await page.setInputFiles('[name="ein_verification"]', './documents/irs_ein_letter.pdf');
await page.click('[data-testid="upload-vehicle-list"]');
await page.setInputFiles('[name="fleet_roster"]', './documents/vehicle_inventory.pdf');
await page.click('[data-testid="upload-lease-agreements"]');
await page.setInputFiles('[name="equipment_leases"]', './documents/coach_leases.pdf');

// Certification and signature
await page.check('[name="certify_accuracy"]');
await page.check('[name="certify_authority_to_sign"]');
await page.check('[name="acknowledge_penalties"]');
await page.check('[name="agree_to_fmcsa_regulations"]');
await page.check('[name="acknowledge_safety_fitness"]');
await page.fill('[name="signature_name"]', 'Elizabeth Martinez');
await page.fill('[name="signature_title"]', 'President/CEO');
await page.fill('[name="signature_date"]', '02/10/2025');

// Payment information
await page.selectOption('[name="payment_method"]', 'credit_card');
await page.fill('[name="card_number"]', process.env.PAYMENT_CARD);
await page.fill('[name="card_expiry"]', '11/28');
await page.fill('[name="card_cvv"]', process.env.CARD_CVV);
await page.fill('[name="cardholder_name"]', 'Elizabeth Martinez');
await page.fill('[name="billing_zip"]', '32801');
await page.fill('[name="registration_fee"]', '300');

await page.click('[data-testid="submit-application"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles fleet validation, insurance verification, and FMCSA submission processes automatically. You can automate new authority applications, passenger carrier registrations, and biennial updates workflows.

## Scale your FMCSA Form OP-1 automation with Anchor Browser

Run your Playwright FMCSA automations on cloud browsers with enterprise-grade reliability and persistent carrier registration sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# FMCSA Form OP-1(P)
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/fmcsa-op-1-p

Automate motor carrier passenger operating authority application workflows with Playwright when APIs aren't available.

# How to Automate FMCSA Form OP-1(P) with Playwright

Automate FMCSA passenger carrier operating authority application workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual registration processes and reduce authority approval delays by automating repetitive FMCSA application workflows. Use Playwright to interact with FMCSA's Unified Registration System programmatically.

[View FMCSA developer resources](https://mobile.fmcsa.dot.gov/QCDevsite/docs/apiAccess) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [FMCSA Form OP-1(P)](https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/2025-09/OP-1%28P%29%20Form.pdf) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to FMCSA registration system
await page.goto('https://www.fmcsa.dot.gov/registration/registration-forms');

// Start new OP-1(P) application
await page.click('[data-testid="new-application"]');
await page.selectOption('[name="application_type"]', 'passenger_carrier_authority');
await page.selectOption('[name="operation_classification"]', 'for_hire');

// Legal business name
await page.fill('[name="legal_name"]', 'Gateway Freight Systems LLC');
await page.fill('[name="dba_name"]', 'Gateway Express');
await page.selectOption('[name="entity_type"]', 'limited_liability_company');
await page.fill('[name="state_of_formation"]', 'GA');
await page.fill('[name="date_of_formation"]', '01/15/2024');

// Tax identification
await page.fill('[name="federal_ein"]', '58-9876543');
await page.selectOption('[name="tax_status"]', 'corporation');

// Principal place of business
await page.fill('[name="business_address"]', '2500 Commerce Parkway');
await page.fill('[name="business_suite"]', 'Suite 300');
await page.fill('[name="business_city"]', 'Atlanta');
await page.selectOption('[name="business_state"]', 'GA');
await page.fill('[name="business_zip"]', '30339');
await page.fill('[name="business_phone"]', '404-555-0192');
await page.fill('[name="business_fax"]', '404-555-0193');
await page.fill('[name="business_email"]', 'operations@gatewayfreight.com');

// Mailing address (if different)
await page.check('[name="mailing_same_as_business"]');

// Ownership information
await page.click('[data-testid="add-owner"]');
await page.fill('[name="owner_name"]', 'Thomas Anderson');
await page.fill('[name="owner_title"]', 'Managing Member');
await page.fill('[name="owner_percentage"]', '60');
await page.fill('[name="owner_ssn"]', '234-56-7890');
await page.fill('[name="owner_address"]', '789 Executive Drive');
await page.fill('[name="owner_city"]', 'Alpharetta');
await page.selectOption('[name="owner_state"]', 'GA');
await page.fill('[name="owner_zip"]', '30022');

// Add second owner
await page.click('[data-testid="add-owner"]');
await page.fill('[name="owner_name_2"]', 'Patricia Wilson');
await page.fill('[name="owner_title_2"]', 'Member');
await page.fill('[name="owner_percentage_2"]', '40');
await page.fill('[name="owner_ssn_2"]', '345-67-8901');

// Operating authority requested
await page.check('[name="interstate_authority"]');
await page.selectOption('[name="passenger_type"]', 'bus');

// Geographic scope
await page.check('[name="48_states"]');
await page.check('[name="mexico"]');
await page.check('[name="canada"]');

// Cargo carried
await page.check('[name="general_commodities"]');
await page.check('[name="household_goods_carrier"]');
await page.fill('[name="commodity_description"]', 'General freight including consumer goods, electronics, and refrigerated products');

// Type of operation
await page.selectOption('[name="operating_status"]', 'new_entrant');
await page.fill('[name="operations_begin_date"]', '04/01/2025');
await page.fill('[name="estimated_mileage"]', '500000');

// Fleet information
await page.fill('[name="power_units_owned"]', '12');
await page.fill('[name="power_units_term_leased"]', '3');
await page.fill('[name="power_units_trip_leased"]', '0');
await page.fill('[name="trailers_owned"]', '25');
await page.fill('[name="trailers_leased"]', '5');
await page.fill('[name="drivers_employed"]', '18');

// MCS-150 mileage information
await page.fill('[name="total_annual_mileage"]', '500000');
await page.fill('[name="vehicle_miles_us"]', '450000');
await page.fill('[name="vehicle_miles_canada"]', '30000');
await page.fill('[name="vehicle_miles_mexico"]', '20000');

// Safety management information
await page.fill('[name="safety_director_name"]', 'Karen Transportation Manager');
await page.fill('[name="safety_director_phone"]', '404-555-0198');
await page.fill('[name="safety_director_email"]', 'safety@gatewayfreight.com');

// Process agent designation
await page.fill('[name="process_agent_name"]', 'National Registered Agents Inc');
await page.fill('[name="process_agent_address"]', '456 Legal Services Blvd');
await page.fill('[name="process_agent_city"]', 'Atlanta');
await page.selectOption('[name="process_agent_state"]', 'GA');
await page.fill('[name="process_agent_zip"]', '30303');
await page.fill('[name="process_agent_phone"]', '404-555-0177');

// Unified Carrier Registration
await page.check('[name="ucr_participation"]');
await page.selectOption('[name="ucr_tier"]', 'tier_3');
await page.fill('[name="ucr_year"]', '2025');

// Insurance information
await page.fill('[name="insurance_carrier"]', 'Continental Insurance Group');
await page.fill('[name="insurance_policy"]', 'CIG-2025-789123');
await page.fill('[name="insurance_coverage_amount"]', '1000000');
await page.fill('[name="insurance_effective_date"]', '04/01/2025');

// Cargo insurance
await page.fill('[name="cargo_insurance_carrier"]', 'Transport Insurance Services');
await page.fill('[name="cargo_policy_number"]', 'TIS-2025-456789');
await page.fill('[name="cargo_coverage"]', '100000');

// USDOT PIN creation
await page.fill('[name="pin_password"]', process.env.USDOT_PIN);
await page.fill('[name="pin_confirm"]', process.env.USDOT_PIN);
await page.fill('[name="security_question_1"]', 'What is your mother\'s maiden name?');
await page.fill('[name="security_answer_1"]', process.env.SECURITY_ANSWER_1);

// Background information
await page.selectOption('[name="prior_authority"]', 'no');
await page.selectOption('[name="safety_rating"]', 'none');
await page.selectOption('[name="suspended_authority"]', 'no');
await page.selectOption('[name="bankruptcy_proceedings"]', 'no');

// Felony conviction disclosure
await page.selectOption('[name="felony_convictions"]', 'no');

// Contact person for application
await page.fill('[name="contact_name"]', 'Thomas Anderson');
await page.fill('[name="contact_title"]', 'Managing Member');
await page.fill('[name="contact_phone"]', '404-555-0192');
await page.fill('[name="contact_email"]', 'tanderson@gatewayfreight.com');

// Supporting documentation
await page.click('[data-testid="upload-articles-of-organization"]');
await page.setInputFiles('[name="formation_documents"]', './documents/llc_articles.pdf');
await page.click('[data-testid="upload-ein-letter"]');
await page.setInputFiles('[name="ein_verification"]', './documents/irs_ein_letter.pdf');
await page.click('[data-testid="upload-lease-agreements"]');
await page.setInputFiles('[name="equipment_leases"]', './documents/truck_leases.pdf');

// Certification and signature
await page.check('[name="certify_truth"]');
await page.check('[name="certify_authority"]');
await page.check('[name="acknowledge_penalties"]');
await page.check('[name="agree_to_regulations"]');
await page.fill('[name="signature_name"]', 'Thomas Anderson');
await page.fill('[name="signature_title"]', 'Managing Member');
await page.fill('[name="signature_date"]', '02/05/2025');

// Payment information
await page.selectOption('[name="payment_method"]', 'credit_card');
await page.fill('[name="card_number"]', process.env.PAYMENT_CARD);
await page.fill('[name="card_expiry"]', '12/27');
await page.fill('[name="card_cvv"]', process.env.CARD_CVV);
await page.fill('[name="billing_zip"]', '30339');
await page.fill('[name="registration_fee"]', '300');

await page.click('[data-testid="submit-application"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles fleet validation, insurance verification, and FMCSA submission processes automatically. You can automate new authority applications, operating authority amendments, and biennial updates workflows.

## Scale your FMCSA Form OP-1(P) automation with Anchor Browser

Run your Playwright FMCSA automations on cloud browsers with enterprise-grade reliability and persistent carrier registration sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Form 122A-1
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/form-122a-1

Automate Chapter 7 bankruptcy means test and income statement workflows with Playwright when APIs aren't available.

# How to Automate Form 122A-1 with Playwright

Automate Chapter 7 bankruptcy means test and current monthly income statement workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual income calculation errors and reduce case filing delays by automating repetitive bankruptcy documentation processes. Use Playwright to interact with PACER and bankruptcy court systems programmatically.

[View PACER developer resources](https://pacer.uscourts.gov/file-case/developer-resources) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [Form 122A-1](https://www.uscourts.gov/file/26712/download) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to US Federal Courts system
await page.goto('https://www.uscourts.gov/forms-rules/forms');

// Start new Form 122A-1
await page.click('[data-testid="bankruptcy-filing"]');
await page.click('[data-testid="form-122a-1"]');
await page.selectOption('[name="case_chapter"]', 'chapter_7');

// Debtor information
await page.fill('[name="debtor_first_name"]', 'Christopher');
await page.fill('[name="debtor_middle_name"]', 'Daniel');
await page.fill('[name="debtor_last_name"]', 'Peterson');
await page.fill('[name="ssn_last_4"]', '6789');
await page.fill('[name="case_number"]', '25-10234');

// Court information
await page.selectOption('[name="district"]', 'eastern_michigan');
await page.selectOption('[name="division"]', 'detroit');

// Joint debtor (if applicable)
await page.check('[name="joint_case"]');
await page.fill('[name="joint_first_name"]', 'Amanda');
await page.fill('[name="joint_middle_name"]', 'Lynn');
await page.fill('[name="joint_last_name"]', 'Peterson');
await page.fill('[name="joint_ssn_last_4"]', '4321');

// Marital and household status
await page.selectOption('[name="marital_status"]', 'married');
await page.fill('[name="household_size"]', '4');
await page.fill('[name="dependents"]', '2');
await page.fill('[name="dependent_ages"]', '8, 12');

// Employment status - Debtor
await page.selectOption('[name="debtor_employment"]', 'employed');
await page.fill('[name="debtor_employer"]', 'Metro Manufacturing Inc');
await page.fill('[name="debtor_occupation"]', 'Production Supervisor');
await page.fill('[name="debtor_employment_start"]', '03/2019');

// Employment status - Spouse
await page.selectOption('[name="spouse_employment"]', 'employed');
await page.fill('[name="spouse_employer"]', 'Community Hospital');
await page.fill('[name="spouse_occupation"]', 'Registered Nurse');
await page.fill('[name="spouse_employment_start"]', '06/2018');

// Part 1: Calculate Your Current Monthly Income
// Income from employment (6-month average)
await page.fill('[name="debtor_gross_month_1"]', '4200');
await page.fill('[name="debtor_gross_month_2"]', '4200');
await page.fill('[name="debtor_gross_month_3"]', '4200');
await page.fill('[name="debtor_gross_month_4"]', '4350');
await page.fill('[name="debtor_gross_month_5"]', '4200');
await page.fill('[name="debtor_gross_month_6"]', '4200');

await page.fill('[name="spouse_gross_month_1"]', '5100');
await page.fill('[name="spouse_gross_month_2"]', '5400');
await page.fill('[name="spouse_gross_month_3"]', '5100');
await page.fill('[name="spouse_gross_month_4"]', '5100');
await page.fill('[name="spouse_gross_month_5"]', '5250');
await page.fill('[name="spouse_gross_month_6"]', '5100');

// Business income (if applicable)
await page.selectOption('[name="operates_business"]', 'no');
await page.fill('[name="business_gross_income"]', '0');
await page.fill('[name="business_expenses"]', '0');

// Rental and real property income
await page.check('[name="rental_income_exists"]');
await page.fill('[name="rental_gross_receipts"]', '1200');
await page.fill('[name="rental_ordinary_expenses"]', '850');
await page.fill('[name="rental_net_income"]', '350');

// Interest, dividends, and royalties
await page.fill('[name="interest_income"]', '15');
await page.fill('[name="dividend_income"]', '0');
await page.fill('[name="royalty_income"]', '0');

// Pension and retirement income
await page.fill('[name="pension_income"]', '0');
await page.fill('[name="401k_withdrawals"]', '0');
await page.fill('[name="social_security"]', '0');

// Other monthly income
await page.fill('[name="unemployment_compensation"]', '0');
await page.fill('[name="workers_compensation"]', '0');
await page.fill('[name="child_support_received"]', '0');
await page.fill('[name="alimony_received"]', '0');
await page.fill('[name="other_income"]', '0');

// Income from all sources (calculated automatically)
await page.fill('[name="total_monthly_income"]', '9630');
await page.fill('[name="annual_income']', '115560');

// Part 2: Determine Whether the Presumption of Abuse Applies
// Median family income comparison
await page.selectOption('[name="state_of_residence"]', 'MI');
await page.fill('[name="household_size_means_test"]', '4');
await page.fill('[name="applicable_median_income"]', '106847');

// Marital adjustment deductions
await page.check('[name="non_filing_spouse_income"]');
await page.fill('[name="spouse_income_not_contributed"]', '850');
await page.fill('[name="spouse_separate_debt_payments"]', '0');

// Calculate current monthly income for means test
await page.fill('[name="cmi_total"]', '8780');
await page.fill('[name="annualized_cmi"]', '105360');

// Compare to median income
await page.check('[name="income_below_median"]');

// Presumption determination
await page.selectOption('[name="presumption_result"]', 'does_not_arise');

// Additional information
await page.fill('[name="calculation_period_start"]', '08/01/2024');
await page.fill('[name="calculation_period_end"]', '01/31/2025');

// Income fluctuation explanation
await page.fill('[name="income_changes_explanation"]', 'Spouse received overtime pay in December 2024 for holiday coverage. Rental property tenant moved in during calculation period.');

// Excluded income (if applicable)
await page.selectOption('[name="excluded_income_exists"]', 'yes');
await page.fill('[name="excluded_income_type"]', 'Social Security benefits for minor child');
await page.fill('[name="excluded_income_amount"]', '685');

// Non-filing spouse contribution
await page.fill('[name="spouse_household_contribution"]', '4250');
await page.fill('[name="spouse_separate_household_expenses"]', '850');

// Special circumstances (if any)
await page.selectOption('[name="special_circumstances"]', 'no');

// Attorney information
await page.check('[name="represented_by_attorney"]');
await page.fill('[name="attorney_name"]', 'Patricia Morrison');
await page.fill('[name="attorney_bar_number"]', 'MI-P67890');
await page.fill('[name="attorney_firm"]', 'Morrison Bankruptcy Law PLLC');
await page.fill('[name="attorney_address"]', '1500 Woodward Avenue, Suite 800');
await page.fill('[name="attorney_city"]', 'Detroit');
await page.selectOption('[name="attorney_state"]', 'MI');
await page.fill('[name="attorney_zip"]', '48226');
await page.fill('[name="attorney_phone"]', '313-555-0145');

// Supporting documentation
await page.click('[data-testid="upload-pay-stubs"]');
await page.setInputFiles('[name="income_verification"]', './documents/paystubs_6months.pdf');
await page.click('[data-testid="upload-tax-returns"]');
await page.setInputFiles('[name="tax_documents"]', './documents/2024_tax_return.pdf');
await page.click('[data-testid="upload-rental-statements"]');
await page.setInputFiles('[name="rental_documentation"]', './documents/rental_income_statements.pdf');

// Certification under penalty of perjury
await page.check('[name="certify_accuracy"]');
await page.check('[name="certify_complete"]');
await page.check('[name="understand_penalties"]');

// Debtor signature
await page.fill('[name="debtor_signature"]', 'Christopher Daniel Peterson');
await page.fill('[name="debtor_signature_date"]', '02/15/2025');

// Joint debtor signature
await page.fill('[name="joint_debtor_signature"]', 'Amanda Lynn Peterson');
await page.fill('[name="joint_debtor_signature_date"]', '02/15/2025');

// Attorney certification
await page.fill('[name="attorney_signature"]', 'Patricia Morrison');
await page.fill('[name="attorney_signature_date"]', '02/15/2025');
await page.click('[data-testid="submit-form"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles income calculations, median income comparisons, and bankruptcy court submission processes automatically. You can automate means test filings, income statement updates, and case documentation workflows.

## Scale your Form 122A-1 automation with Anchor Browser

Run your Playwright bankruptcy court automations on cloud browsers with enterprise-grade reliability and persistent PACER sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# FS Form 5444
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/fs-5444

Automate TreasuryDirect account authorization workflows with Playwright when APIs aren't available.

# How to Automate FS Form 5444 with Playwright

Automate TreasuryDirect account authorization workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual authorization processing and reduce account access delays by automating repetitive TreasuryDirect delegation processes. Use Playwright to interact with TreasuryDirect systems programmatically.

[View TreasuryDirect developer resources](https://www.treasurydirect.gov/help-center/) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [FS Form 5444](https://www.treasurydirect.gov/forms/acctauth.pdf) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to TreasuryDirect system
await page.goto('https://treasurydirect.gov/forms/');

// Start new account authorization form
await page.click('[data-testid="manage-account"]');
await page.click('[data-testid="account-authorization"]');
await page.selectOption('[name="form_type"]', 'fs_5444');

// Account holder information
await page.fill('[name="account_holder_name"]', 'Margaret Elizabeth Wilson');
await page.fill('[name="ssn"]', '123-45-6789');
await page.fill('[name="account_number"]', 'TD-987654321');
await page.fill('[name="date_of_birth"]', '06/12/1968');

// Contact information
await page.fill('[name="address"]', '456 Financial Plaza, Suite 200');
await page.fill('[name="city"]', 'Charlotte');
await page.selectOption('[name="state"]', 'NC');
await page.fill('[name="zip"]', '28202');
await page.fill('[name="phone"]', '704-555-0156');
await page.fill('[name="email"]', 'mwilson@email.com');

// Type of authorization
await page.selectOption('[name="authorization_type"]', 'account_manager');
await page.check('[name="full_transaction_authority"]');

// Authorized individual information
await page.fill('[name="authorized_name"]', 'Robert James Wilson');
await page.fill('[name="authorized_ssn"]', '987-65-4321');
await page.fill('[name="authorized_relationship"]', 'Spouse');
await page.fill('[name="authorized_date_of_birth"]', '03/18/1965');

// Authorized person contact information
await page.fill('[name="authorized_address"]', '456 Financial Plaza, Suite 200');
await page.fill('[name="authorized_city"]', 'Charlotte');
await page.selectOption('[name="authorized_state"]', 'NC');
await page.fill('[name="authorized_zip"]', '28202');
await page.fill('[name="authorized_phone"]', '704-555-0157');
await page.fill('[name="authorized_email"]', 'rwilson@email.com');

// Authorization scope
await page.check('[name="purchase_securities"]');
await page.check('[name="redeem_securities"]');
await page.check('[name="reinvest_securities"]');
await page.check('[name="change_registration"]');
await page.check('[name="view_account_information"]');
await page.check('[name="update_banking_information"]');

// Securities types covered
await page.check('[name="savings_bonds"]');
await page.check('[name="treasury_bills"]');
await page.check('[name="treasury_notes"]');
await page.check('[name="treasury_bonds"]');
await page.check('[name="tips"]');

// Transaction limits (if applicable)
await page.check('[name="set_transaction_limits"]');
await page.fill('[name="single_transaction_limit"]', '50000');
await page.fill('[name="monthly_limit"]', '200000');
await page.fill('[name="annual_limit"]', '1000000');

// Effective dates
await page.fill('[name="authorization_start_date"]', '03/01/2025');
await page.selectOption('[name="authorization_duration"]', 'indefinite');

// Special conditions or restrictions
await page.fill('[name="special_instructions"]', 'Authorization valid for all routine transactions. Redemptions over $100,000 require phone confirmation with primary account holder.');

// Secondary authorized person (if applicable)
await page.check('[name="add_secondary_authorized"]');
await page.fill('[name="secondary_name"]', 'Jennifer Marie Wilson');
await page.fill('[name="secondary_ssn"]', '234-56-7890');
await page.fill('[name="secondary_relationship"]', 'Daughter');
await page.selectOption('[name="secondary_authority_level"]', 'view_only');

// Notification preferences
await page.check('[name="notify_primary_on_transactions"]');
await page.check('[name="email_confirmations"]');
await page.check('[name="monthly_statements"]');

// Banking information for authorized transactions
await page.fill('[name="linked_bank_name"]', 'Bank of America');
await page.fill('[name="routing_number"]', '053000196');
await page.fill('[name="account_number"]', '123456789012');
await page.selectOption('[name="account_type"]', 'checking');

// Security questions for authorized person
await page.fill('[name="security_question_1"]', 'What is your mother\'s maiden name?');
await page.fill('[name="security_answer_1"]', process.env.SECURITY_ANSWER_1);
await page.fill('[name="security_question_2"]', 'What city were you born in?');
await page.fill('[name="security_answer_2"]', process.env.SECURITY_ANSWER_2);

// Identity verification documents
await page.click('[data-testid="upload-id-primary"]');
await page.setInputFiles('[name="primary_identification"]', './documents/primary_drivers_license.pdf');
await page.click('[data-testid="upload-id-authorized"]');
await page.setInputFiles('[name="authorized_identification"]', './documents/authorized_drivers_license.pdf');
await page.click('[data-testid="upload-proof-relationship"]');
await page.setInputFiles('[name="relationship_proof"]', './documents/marriage_certificate.pdf');

// Medallion signature guarantee (if required)
await page.check('[name="medallion_guarantee_required"]');
await page.fill('[name="medallion_institution"]', 'Wells Fargo Bank');
await page.fill('[name="medallion_stamp_number"]', 'MSG-2025-456789');
await page.fill('[name="medallion_date"]', '02/20/2025');

// Account holder certification
await page.check('[name="certify_accuracy"]');
await page.check('[name="certify_authority"]');
await page.check('[name="authorize_treasury_verification"]');
await page.check('[name="acknowledge_liability"]');
await page.check('[name="understand_revocation_rights"]');

// Account holder signature
await page.fill('[name="account_holder_signature"]', 'Margaret Elizabeth Wilson');
await page.fill('[name="signature_date"]', '02/20/2025');

// Authorized person acceptance
await page.check('[name="authorized_accepts_responsibility"]');
await page.check('[name="authorized_agrees_to_terms"]');
await page.fill('[name="authorized_signature"]', 'Robert James Wilson');
await page.fill('[name="authorized_signature_date"]', '02/20/2025');

// Witness information (if required)
await page.fill('[name="witness_name"]', 'Sarah Financial Advisor');
await page.fill('[name="witness_title"]', 'Certified Financial Planner');
await page.fill('[name="witness_signature"]', 'Sarah Financial Advisor');
await page.fill('[name="witness_date"]', '02/20/2025');

await page.click('[data-testid="submit-authorization"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles identity verification, authorization scope validation, and TreasuryDirect submission processes automatically. You can automate account delegation, authority modifications, and revocation workflows.

## Scale your FS Form 5444 automation with Anchor Browser

Run your Playwright TreasuryDirect automations on cloud browsers with enterprise-grade reliability and persistent securities account sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# FSA Form 578
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/fsa-578

Automate USDA farm commodity storage report workflows with Playwright when APIs aren't available.

# How to Automate FSA Form 578 with Playwright

Automate USDA Farm Service Agency commodity storage report workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual inventory reporting and reduce compliance errors by automating repetitive grain storage documentation processes. Use Playwright to interact with FSA systems programmatically.

[View USDA FSA developer resources](https://www.fsa.usda.gov/help) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [FSA Form 578](https://www.fsa.usda.gov/documents/fsa-578) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to FSA farmers.gov system
await page.goto('https://forms.sc.egov.usda.gov/eForms/welcomeAction.do?Home');

// Start new FSA-578 report
await page.click('[data-testid="commodity-reports"]');
await page.click('[data-testid="form-578"]');
await page.selectOption('[name="report_type"]', 'stored_commodities');

// Producer information
await page.fill('[name="producer_name"]', 'Heartland Grain Farms LLC');
await page.fill('[name="farm_number"]', 'IA-089-1234');
await page.fill('[name="tract_number"]', '5678');
await page.fill('[name="federal_ein"]', '42-1234567');

// Contact information
await page.fill('[name="address"]', '4500 County Road 120');
await page.fill('[name="city"]', 'Cedar Rapids');
await page.selectOption('[name="state"]', 'IA');
await page.fill('[name="zip"]', '52404');
await page.fill('[name="phone"]', '319-555-0174');
await page.fill('[name="email"]', 'operations@heartlandgrain.com');

// County FSA office
await page.selectOption('[name="county"]', 'linn');
await page.fill('[name="fsa_office_code"]', 'IA-057');

// Storage facility information
await page.fill('[name="facility_name"]', 'Heartland Main Storage Complex');
await page.fill('[name="facility_address"]', '4500 County Road 120');
await page.fill('[name="facility_city"]', 'Cedar Rapids');
await page.selectOption('[name="facility_state"]', 'IA');
await page.fill('[name="facility_zip"]', '52404');

// Facility type and capacity
await page.selectOption('[name="facility_type"]', 'on_farm_storage');
await page.fill('[name="total_storage_capacity_bushels"]', '150000');
await page.fill('[name="number_of_bins"]', '6');
await page.check('[name="climate_controlled"]');
await page.check('[name="fumigation_capable"]');

// Report period
await page.fill('[name="report_date"]', '02/28/2025');
await page.selectOption('[name="crop_year"]', '2024');
await page.fill('[name="reporting_period_start"]', '12/01/2024');
await page.fill('[name="reporting_period_end"]', '02/28/2025');

// Commodity 1: Corn
await page.click('[data-testid="add-commodity"]');
await page.selectOption('[name="commodity_type_1"]', 'corn');
await page.fill('[name="commodity_grade_1"]', 'US No. 2 Yellow');
await page.fill('[name="quantity_bushels_1"]', '85000');
await page.fill('[name="bin_location_1"]', 'Bins 1, 2, 3');
await page.fill('[name="storage_date_1"]', '10/15/2024');
await page.selectOption('[name="ownership_1"]', 'producer_owned');
await page.fill('[name="ccc_loan_number_1"]', 'CCC-2024-IA-789456');

// Corn quality information
await page.fill('[name="moisture_content_1"]', '14.5');
await page.fill('[name="test_weight_1"]', '56.2');
await page.fill('[name="damaged_kernels_1"]', '2.1');
await page.fill('[name="foreign_material_1"]', '0.8');

// Commodity 2: Soybeans
await page.click('[data-testid="add-commodity"]');
await page.selectOption('[name="commodity_type_2"]', 'soybeans');
await page.fill('[name="commodity_grade_2"]', 'US No. 1');
await page.fill('[name="quantity_bushels_2"]', '45000');
await page.fill('[name="bin_location_2"]', 'Bins 4, 5');
await page.fill('[name="storage_date_2"]', '11/05/2024');
await page.selectOption('[name="ownership_2"]', 'producer_owned');
await page.fill('[name="ccc_loan_number_2"]', 'CCC-2024-IA-789457');

// Soybeans quality information
await page.fill('[name="moisture_content_2"]', '13.0');
await page.fill('[name="test_weight_2"]', '57.8');
await page.fill('[name="damaged_kernels_2"]', '1.5');
await page.fill('[name="foreign_material_2"]', '0.5');

// Commodity 3: Wheat
await page.click('[data-testid="add-commodity"]');
await page.selectOption('[name="commodity_type_3"]', 'wheat');
await page.selectOption('[name="wheat_class_3"]', 'hard_red_winter');
await page.fill('[name="commodity_grade_3"]', 'US No. 2');
await page.fill('[name="quantity_bushels_3"]', '12000');
await page.fill('[name="bin_location_3"]', 'Bin 6');
await page.fill('[name="storage_date_3"]', '07/20/2024');
await page.selectOption('[name="ownership_3"]', 'producer_owned');

// Wheat quality information
await page.fill('[name="moisture_content_3"]', '12.5');
await page.fill('[name="test_weight_3"]', '60.1');
await page.fill('[name="protein_content_3"]', '11.8');

// Total inventory summary
await page.fill('[name="total_bushels_all_commodities"]', '142000');
await page.fill('[name="storage_utilization_percentage"]', '94.7');

// Storage agreements and liens
await page.check('[name="warehouse_receipt_issued"]');
await page.fill('[name="warehouse_receipt_number"]', 'WHR-2024-456789');
await page.check('[name="commodity_under_lien"]');
await page.fill('[name="lienholder_name"]', 'AgriBank FCB');
await page.fill('[name="lien_amount"]', '850000');

// Marketing and disposition
await page.fill('[name="quantity_sold_period"]', '8000');
await page.fill('[name="quantity_removed_period"]', '0');
await page.fill('[name="quantity_damaged_period"]', '150');
await page.fill('[name="damage_cause"]', 'Minor moisture damage in Bin 4 - repaired and dried');

// Insurance coverage
await page.check('[name="crop_insurance_coverage"]');
await page.fill('[name="insurance_provider"]', 'Rain and Hail Insurance');
await page.fill('[name="policy_number"]', 'RH-2024-567890');
await page.fill('[name="coverage_amount"]', '1200000');

// Facility maintenance and inspection
await page.fill('[name="last_inspection_date"]', '01/15/2025');
await page.fill('[name="inspector_name"]', 'County FSA Inspector Johnson');
await page.check('[name="facility_good_condition"]');
await page.fill('[name="maintenance_notes"]', 'All bins inspected and in excellent condition. No structural issues. Ventilation systems operational.');

// Previous losses or damage
await page.selectOption('[name="losses_in_past_year"]', 'yes');
await page.fill('[name="loss_description"]', 'Minor moisture damage in October 2024 affecting 150 bushels. Grain removed and sold. Bin repaired.');
await page.fill('[name="loss_amount_bushels"]', '150');

// Supporting documentation
await page.click('[data-testid="upload-bin-measurements"]');
await page.setInputFiles('[name="bin_capacity_docs"]', './documents/bin_capacity_certifications.pdf');
await page.click('[data-testid="upload-scale-tickets"]');
await page.setInputFiles('[name="scale_tickets"]', './documents/harvest_scale_tickets.pdf');
await page.click('[data-testid="upload-quality-reports"]');
await page.setInputFiles('[name="grain_quality_tests"]', './documents/grain_test_results.pdf');

// Producer certification
await page.check('[name="certify_accuracy"]');
await page.check('[name="certify_ownership"]');
await page.check('[name="certify_quantity"]');
await page.check('[name="acknowledge_penalties"]');
await page.check('[name="agree_to_inspection"]');

// Signature
await page.fill('[name="producer_signature"]', 'William Heartland Owner');
await page.fill('[name="producer_title"]', 'Managing Member');
await page.fill('[name="signature_date"]', '02/28/2025');

// County office verification (if applicable)
await page.fill('[name="fsa_reviewer_name"]', 'Janet County Director');
await page.fill('[name="fsa_reviewer_title"]', 'County Executive Director');
await page.fill('[name="fsa_review_date"]', '03/01/2025');

await page.click('[data-testid="submit-report"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles quantity calculations, quality verification, and FSA submission processes automatically. You can automate monthly reports, loan compliance documentation, and inventory tracking workflows.

## Scale your FSA Form 578 automation with Anchor Browser

Run your Playwright FSA automations on cloud browsers with enterprise-grade reliability and persistent farm program sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# IRS Form 8300
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/irs-8300

Automate IRS Form 8300 cash payment reporting workflows with Playwright when APIs aren't available.

# How to Automate IRS Form 8300 with Playwright

Automate critical IRS Form 8300 cash payment reporting workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual compliance reporting and reduce tax violation risks by automating repetitive large cash transaction declarations. Use Playwright to interact with IRS e-file systems programmatically.

[View IRS developer resources](https://www.irs.gov/e-file-providers/modernized-e-file-overview) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [IRS Form 8300](https://www.irs.gov/pub/irs-pdf/f8300.pdf) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to IRS e-file system
await page.goto('https://bsaefiling.fincen.gov/');
await page.fill('[data-testid="username"]', process.env.IRS_USERNAME);
await page.fill('[data-testid="password"]', process.env.IRS_PASSWORD);
await page.click('[data-testid="login-button"]');

// Start new Form 8300 filing
await page.click('[data-testid="new-form-8300"]');
await page.selectOption('[name="filing_reason"]', 'single_transaction');

// Business information
await page.fill('[name="business_name"]', 'Premier Auto Sales LLC');
await page.fill('[name="business_address"]', '789 Main Street');
await page.fill('[name="business_city"]', 'Phoenix');
await page.selectOption('[name="business_state"]', 'AZ');
await page.fill('[name="business_zip"]', '85001');
await page.fill('[name="business_ein"]', '12-3456789');

// Transaction details
await page.fill('[name="transaction_date"]', '12/10/2024');
await page.fill('[name="cash_amount']', '15000.00');
await page.selectOption('[name="transaction_type"]', 'sale_of_goods');
await page.fill('[name="transaction_description']', '2019 BMW X5 vehicle sale');

// Person making payment
await page.fill('[name="payer_first_name"]', 'Michael');
await page.fill('[name="payer_last_name"]', 'Rodriguez');
await page.fill('[name="payer_address']', '456 Oak Avenue');
await page.fill('[name="payer_city"]', 'Scottsdale');
await page.selectOption('[name="payer_state"]', 'AZ');
await page.fill('[name="payer_zip"]', '85260');
await page.fill('[name="payer_ssn"]', '123-45-6789');
await page.fill('[name="payer_date_of_birth"]', '03/15/1978');

// Payment method details
await page.selectOption('[name="payment_method"]', 'cash');
await page.fill('[name="denominations_100']', '150'); // $100 bills count
await page.fill('[name="foreign_currency_amount']', '0');

// Verification of identity
await page.selectOption('[name="id_type"]', 'drivers_license');
await page.fill('[name="id_number"]', 'D12345678');
await page.selectOption('[name="id_state']', 'AZ');

// Submit report
await page.check('[name="certify_accuracy"]');
await page.fill('[name="preparer_name"]', 'Sarah Financial Controller');
await page.fill('[name="preparer_title"]', 'Controller');
await page.click('[data-testid="submit-form-8300"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles transaction validation, amount calculations, and IRS submission processes automatically. You can automate bulk filings, compliance tracking, and suspicious activity reporting workflows.

## Scale your IRS Form 8300 automation with Anchor Browser

Run your Playwright IRS automations on cloud browsers with enterprise-grade reliability and persistent tax compliance sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# IRS Form W-7
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/irs-w7

Automate ITIN application workflows with Playwright when APIs aren't available.

# How to Automate IRS Form W-7 with Playwright

Automate IRS Individual Taxpayer Identification Number (ITIN) application workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual tax identification processing and reduce approval delays by automating repetitive ITIN application processes. Use Playwright to interact with IRS systems programmatically.

[View IRS developer resources](https://www.irs.gov/e-file-providers/modernized-e-file-program-information) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [IRS Form W-7](https://www.irs.gov/pub/irs-pdf/fw7.pdf) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to IRS online system
await page.goto('https://www.irs.gov/forms-instructions);

// Start new W-7 application
await page.click('[data-testid="new-application"]');
await page.selectOption('[name="form_type"]', 'w7');

// Reason for applying
await page.selectOption('[name="reason_for_itin"]', 'tax_return_filing');
await page.check('[name="attach_federal_return"]');
await page.selectOption('[name="tax_treaty_exception"]', 'no');

// Applicant information
await page.fill('[name="legal_name_first"]', 'Carlos');
await page.fill('[name="legal_name_middle"]', 'Alberto');
await page.fill('[name="legal_name_last"]', 'Mendoza');

// Name at birth (if different)
await page.selectOption('[name="name_changed"]', 'no');

// Date of birth and place
await page.fill('[name="date_of_birth"]', '05/22/1985');
await page.fill('[name="country_of_birth"]', 'Mexico');
await page.fill('[name="state_province_birth"]', 'Jalisco');
await page.fill('[name="city_birth"]', 'Guadalajara');

// Gender
await page.selectOption('[name="gender"]', 'male');

// Mailing address - foreign
await page.selectOption('[name="address_type"]', 'foreign');
await page.fill('[name="foreign_address_line_1"]', 'Calle Reforma 456');
await page.fill('[name="foreign_address_line_2"]', 'Colonia Centro');
await page.fill('[name="foreign_city"]', 'Guadalajara');
await page.fill('[name="foreign_state_province"]', 'Jalisco');
await page.fill('[name="foreign_postal_code"]', '44100');
await page.selectOption('[name="foreign_country"]', 'Mexico');

// US address (if applicable)
await page.check('[name="has_us_address"]');
await page.fill('[name="us_address']', '789 Temporary Street, Apt 3C');
await page.fill('[name="us_city"]', 'Los Angeles');
await page.selectOption('[name="us_state"]', 'CA');
await page.fill('[name="us_zip"]', '90012');

// Contact information
await page.fill('[name="phone_foreign"]', '+52-33-1234-5678');
await page.fill('[name="phone_us"]', '213-555-0145');
await page.fill('[name="email"]', 'cmendoza@email.com');

// Country of citizenship
await page.selectOption('[name="country_citizenship"]', 'Mexico');

// Foreign tax ID (if applicable)
await page.check('[name="has_foreign_tax_id"]');
await page.fill('[name="foreign_tax_id"]', 'MEMC850522HJ8');
await page.selectOption('[name="foreign_tax_country"]', 'Mexico');

// Visa information
await page.selectOption('[name="visa_type"]', 'h1b');
await page.fill('[name="visa_number"]', 'H1B-2024-123456');
await page.fill('[name="visa_expiration"]', '12/31/2026');

// Entry date to US
await page.fill('[name="us_entry_date"]', '01/15/2024');

// Passport information
await page.fill('[name="passport_number"]', 'G12345678');
await page.selectOption('[name="passport_country"]', 'Mexico');
await page.fill('[name="passport_issue_date"]', '03/10/2019');
await page.fill('[name="passport_expiration']', '03/10/2029');

// Family information
await page.selectOption('[name="marital_status"]', 'married');
await page.fill('[name="spouse_name"]', 'Maria Elena Mendoza');
await page.fill('[name="spouse_ssn_itin"]', 'Not applicable');

// Dependent information (if applicable)
await page.click('[data-testid="add-dependent"]');
await page.fill('[name="dependent_first_name"]', 'Sofia');
await page.fill('[name="dependent_middle_name"]', 'Isabel');
await page.fill('[name="dependent_last_name"]', 'Mendoza');
await page.fill('[name="dependent_dob"]', '08/12/2015');
await page.selectOption('[name="dependent_country_birth"]', 'Mexico');
await page.selectOption('[name="dependent_relationship"]', 'daughter');

// Previous ITIN applications
await page.selectOption('[name="previously_applied"]', 'no');

// Previous SSN applications
await page.selectOption('[name="previously_applied_ssn"]', 'no');

// Tax return information
await page.fill('[name="tax_year"]', '2024');
await page.selectOption('[name="filing_status"]', 'married_filing_jointly');
await page.check('[name="claiming_dependents"]');
await page.fill('[name="number_of_dependents"]', '1');

// Income information
await page.fill('[name="us_source_income"]', 'yes');
await page.fill('[name="employer_name"]', 'Tech Innovations Inc');
await page.fill('[name="employer_ein"]', '12-3456789');
await page.fill('[name="employer_address"]', '500 Silicon Valley Drive');
await page.fill('[name="employer_city"]', 'San Jose');
await page.selectOption('[name="employer_state"]', 'CA');
await page.fill('[name="employer_zip"]', '95110');

// Tax treaty benefits (if applicable)
await page.selectOption('[name="claim_treaty_benefits"]', 'no');

// Acceptance agent information (if used)
await page.selectOption('[name="using_acceptance_agent"]', 'yes');
await page.fill('[name="agent_name"]', 'Global Tax Services LLC');
await page.fill('[name="agent_ein"]', '98-7654321');
await page.fill('[name="agent_address"]', '1200 Financial Plaza, Suite 300');
await page.fill('[name="agent_city"]', 'Los Angeles');
await page.selectOption('[name="agent_state"]', 'CA');
await page.fill('[name="agent_zip"]', '90071');
await page.fill('[name="agent_phone"]', '213-555-0190');

// Agent certification
await page.fill('[name="agent_representative"]', 'Patricia Tax Professional');
await page.fill('[name="agent_caf_number"]', 'CAF-123456');

// Supporting documentation checklist
await page.check('[name="doc_passport"]');
await page.check('[name="doc_birth_certificate"]');
await page.check('[name="doc_visa']');
await page.check('[name="doc_employment_letter"]');
await page.check('[name="doc_tax_return"]');

// Document authentication
await page.selectOption('[name="documents_certified"]', 'acceptance_agent');
await page.fill('[name="certification_date"]', '03/05/2025');

// Upload supporting documents
await page.click('[data-testid="upload-passport"]');
await page.setInputFiles('[name="passport_copy"]', './documents/passport_certified_copy.pdf');
await page.click('[data-testid="upload-birth-certificate"]');
await page.setInputFiles('[name="birth_certificate"]', './documents/birth_certificate_certified.pdf');
await page.click('[data-testid="upload-visa"]');
await page.setInputFiles('[name="visa_document"]', './documents/h1b_visa_copy.pdf');
await page.click('[data-testid="upload-tax-return"]');
await page.setInputFiles('[name="tax_return_copy"]', './documents/2024_form_1040.pdf');

// Signature under penalty of perjury
await page.check('[name="certify_true_correct"]');
await page.check('[name="understand_penalties"]');
await page.check('[name="authorize_disclosure"]');

// Applicant signature
await page.fill('[name="applicant_signature"]', 'Carlos Alberto Mendoza');
await page.fill('[name="signature_date"]', '03/05/2025');

// Delegate signature (if applicable)
await page.fill('[name="delegate_signature"]', 'Patricia Tax Professional');
await page.fill('[name="delegate_pin"]', 'CAF-123456');
await page.fill('[name="delegate_date"]', '03/05/2025');

// Acceptance agent signature
await page.fill('[name="agent_signature"]', 'Patricia Tax Professional');
await page.fill('[name="agent_title"]', 'Certified Acceptance Agent');
await page.fill('[name="agent_signature_date"]', '03/05/2025');

// Application submission details
await page.selectOption('[name="submission_method"]', 'acceptance_agent');
await page.fill('[name="submission_date"]', '03/05/2025');

// Mailing address for ITIN
await page.selectOption('[name="send_itin_to"]', 'us_address');

// Special handling instructions
await page.fill('[name="special_instructions"]', 'Expedited processing requested due to pending tax return deadline. Original documents authenticated by CAA.');

await page.click('[data-testid="submit-application"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles document verification, identity validation, and IRS submission processes automatically. You can automate ITIN applications, renewal requests, and dependent ITIN workflows.

## Scale your IRS Form W-7 automation with Anchor Browser

Run your Playwright IRS automations on cloud browsers with enterprise-grade reliability and persistent tax system sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# OWCP Form 915
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/owcp-915

Automate federal workers' compensation claim workflows with Playwright when APIs aren't available.

# How to Automate OWCP Form 915 with Playwright

Automate Department of Labor Office of Workers' Compensation Programs claim submission workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual injury claim processing and reduce approval delays by automating repetitive federal workers' compensation documentation processes. Use Playwright to interact with OWCP systems programmatically.

[View DOL OWCP developer resources](https://www.dol.gov/agencies/owcp) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [OWCP Form 915](https://www.dol.gov/sites/dolgov/files/owcp/dfec/regs/compliance/owcp-915.pdf) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to OWCP system
await page.goto('https://www.dol.gov/agencies/owcp/FECA/regs/compliance/forms');

// Start new OWCP-915 form
await page.click('[data-testid="new-claim"]');
await page.selectOption('[name="form_type"]', 'owcp_915');
await page.selectOption('[name="claim_type"]', 'medical_benefits');

// Employee information
await page.fill('[name="employee_last_name"]', 'Anderson');
await page.fill('[name="employee_first_name"]', 'Robert');
await page.fill('[name="employee_middle_name"]', 'James');
await page.fill('[name="ssn"]', '123-45-6789');
await page.fill('[name="date_of_birth"]', '04/18/1980');

// Contact information
await page.fill('[name="address"]', '345 Federal Plaza, Apt 7B');
await page.fill('[name="city"]', 'Washington');
await page.selectOption('[name="state"]', 'DC');
await page.fill('[name="zip"]', '20001');
await page.fill('[name="phone_home"]', '202-555-0167');
await page.fill('[name="phone_cell"]', '202-555-0168');
await page.fill('[name="email"]', 'randerson@email.com');

// Employment information
await page.fill('[name="agency_name"]', 'Department of Commerce');
await page.fill('[name="agency_code"]', 'DOC-1300');
await page.fill('[name="employing_office"]', 'Bureau of Economic Analysis');
await page.fill('[name="job_title"]', 'Economic Analyst');
await page.fill('[name="occupation_code"]', 'GS-0110-12');
await page.fill('[name="pay_grade"]', 'GS-12');
await page.fill('[name="step"]', '5');

// Duty station
await page.fill('[name="duty_station_address"]', '4600 Silver Hill Road');
await page.fill('[name="duty_station_city"]', 'Suitland');
await page.selectOption('[name="duty_station_state"]', 'MD');
await page.fill('[name="duty_station_zip"]', '20746');

// Supervisor information
await page.fill('[name="supervisor_name"]', 'Margaret Division Chief');
await page.fill('[name="supervisor_title"]', 'Division Chief');
await page.fill('[name="supervisor_phone"]', '301-555-0145');
await page.fill('[name="supervisor_email"]', 'mdivisionchief@commerce.gov');

// Injury or illness information
await page.fill('[name="injury_date"]', '02/15/2025');
await page.fill('[name="injury_time"]', '10:30 AM');
await page.selectOption('[name="injury_type"]', 'traumatic_injury');
await page.fill('[name="date_disability_began"]', '02/15/2025');

// Location of injury
await page.selectOption('[name="injury_location"]', 'duty_station');
await page.fill('[name="injury_specific_location"]', 'Third floor office, Room 315');

// Nature of injury
await page.selectOption('[name="injury_category"]', 'strain_sprain');
await page.selectOption('[name="body_part"]', 'lower_back');
await page.fill('[name="injury_description"]', 'Lower back strain while lifting heavy box of documents from floor to desk. Immediate sharp pain in lumbar region.');

// How injury occurred
await page.fill('[name="injury_circumstances"]', 'Employee was retrieving archived files from storage boxes. Lifted approximately 40-pound box using improper technique. Felt immediate pain and muscle spasm in lower back. Unable to continue work duties.');

// Witnesses
await page.click('[data-testid="add-witness"]');
await page.fill('[name="witness_name_1"]', 'David Colleague');
await page.fill('[name="witness_phone_1"]', '301-555-0178');
await page.fill('[name="witness_email_1"]', 'dcolleague@commerce.gov');

// Medical treatment information
await page.selectOption('[name="medical_treatment_received"]', 'yes');
await page.fill('[name="first_treatment_date"]', '02/15/2025');
await page.selectOption('[name="treatment_type"]', 'emergency_room');

// Medical facility information
await page.fill('[name="facility_name"]', 'Prince George\'s Hospital Center');
await page.fill('[name="facility_address"]', '3001 Hospital Drive');
await page.fill('[name="facility_city"]', 'Cheverly');
await page.selectOption('[name="facility_state"]', 'MD');
await page.fill('[name="facility_zip"]', '20785');
await page.fill('[name="facility_phone"]', '301-555-0200');

// Attending physician
await page.fill('[name="physician_name"]', 'Dr. Sarah Emergency Physician');
await page.fill('[name="physician_specialty"]', 'Emergency Medicine');
await page.fill('[name="physician_phone"]', '301-555-0201');

// Diagnosis and treatment
await page.fill('[name="diagnosis"]', 'Acute lumbar strain, L4-L5 region');
await page.fill('[name="treatment_provided"]', 'Physical examination, X-rays, pain medication, muscle relaxants, ice therapy, ergonomic counseling');

// Work status
await page.selectOption('[name="return_to_work_status"]', 'limited_duty');
await page.fill('[name="work_restrictions']', 'No lifting over 10 pounds, no bending or twisting, frequent position changes, ergonomic chair required');
await page.fill('[name="estimated_return_date"]', '03/15/2025');

// Time loss information
await page.selectOption('[name="time_lost"]', 'yes');
await page.fill('[name="first_day_missed"]', '02/16/2025');
await page.fill('[name="total_days_lost"]', '5');
await page.fill('[name="work_hours_per_day"]', '8');

// Continuation of pay (COP) election
await page.check('[name="elect_cop"]');
await page.fill('[name="cop_start_date"]', '02/16/2025');
await page.fill('[name="cop_days_requested"]', '45');

// Leave usage
await page.check('[name="used_leave"]');
await page.selectOption('[name="leave_type"]', 'sick_leave');
await page.fill('[name="leave_hours"]', '40');
await page.fill('[name="leave_dates"]', '02/16/2025 - 02/20/2025');

// Claim for compensation
await page.selectOption('[name="claim_type_detail"]', 'medical_expenses');
await page.check('[name="claim_wage_loss"]');
await page.check('[name="claim_schedule_award"]');

// Medical expenses claimed
await page.fill('[name="emergency_room_cost"]', '850');
await page.fill('[name="physician_fees"]', '350');
await page.fill('[name="xray_cost"]', '275');
await page.fill('[name="medication_cost"]', '125');
await page.fill('[name="total_medical_expenses"]', '1600');

// Previous injuries or conditions
await page.selectOption('[name="prior_back_injury"]', 'no');
await page.selectOption('[name="preexisting_condition"]', 'no');

// Third party liability
await page.selectOption('[name="third_party_liability"]', 'no');

// Safety equipment
await page.selectOption('[name="safety_equipment_available"]', 'not_applicable');

// Accident investigation
await page.check('[name="supervisor_notified"]');
await page.fill('[name="notification_date"]', '02/15/2025');
await page.fill('[name="notification_time"]', '10:45 AM');
await page.check('[name="incident_report_filed"]');
await page.fill('[name="incident_report_number"]', 'IR-2025-0234');

// Supporting documentation
await page.click('[data-testid="upload-medical-report"]');
await page.setInputFiles('[name="medical_documentation"]', './documents/er_report.pdf');
await page.click('[data-testid="upload-xray"]');
await page.setInputFiles('[name="diagnostic_imaging"]', './documents/lumbar_xray_report.pdf');
await page.click('[data-testid="upload-receipts"]');
await page.setInputFiles('[name="expense_receipts"]', './documents/medical_receipts.pdf');
await page.click('[data-testid="upload-incident-report"]');
await page.setInputFiles('[name="incident_documentation"]', './documents/supervisor_incident_report.pdf');

// Employee statement
await page.fill('[name="employee_statement"]', 'I was performing routine work duties retrieving archived files when injury occurred. I have consistently followed all safety protocols. The injury was purely accidental and occurred in the normal course of my federal employment.');

// Employee certification
await page.check('[name="certify_accuracy"]');
await page.check('[name="certify_work_related"]');
await page.check('[name="understand_penalties"]');
await page.check('[name="authorize_medical_disclosure"]');

// Employee signature
await page.fill('[name="employee_signature"]', 'Robert James Anderson');
await page.fill('[name="employee_signature_date"]', '02/20/2025');

// Supervisor section
await page.selectOption('[name="supervisor_agrees"]', 'agree');
await page.fill('[name="supervisor_comments"]', 'Employee injury confirmed. Witnessed by coworker. Employee followed reporting procedures. Limited duty assignment available upon medical clearance.');

// Supervisor verification
await page.check('[name="injury_occurred_on_duty"]');
await page.check('[name="employee_good_standing"]');
await page.fill('[name="supervisor_signature"]', 'Margaret Division Chief');
await page.fill('[name="supervisor_signature_date"]', '02/21/2025');

// Agency action
await page.selectOption('[name="cop_approved"]', 'yes');
await page.fill('[name="cop_approval_date"]', '02/21/2025');
await page.fill('[name="agency_case_number"]', 'DOC-WC-2025-0456');

// Personnel office contact
await page.fill('[name="hr_contact_name"]', 'Patricia Personnel Specialist');
await page.fill('[name="hr_contact_phone"]', '301-555-0150');
await page.fill('[name="hr_contact_email"]', 'hr.benefits@commerce.gov');

await page.click('[data-testid="submit-claim"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles injury documentation, medical verification, and OWCP submission processes automatically. You can automate claim filings, status tracking, and medical reimbursement workflows.

## Scale your OWCP Form 915 automation with Anchor Browser

Run your Playwright OWCP automations on cloud browsers with enterprise-grade reliability and persistent workers' compensation system sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Integrate Playwright with Anchor Browser
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/index

Integrate Playwright and Anchor Browser

# What is Playwright?

[Playwright](https://playwright.dev/) is Microsoft's modern browser automation framework that enables reliable end-to-end testing and web scraping across all major browsers (Chromium, Firefox, and WebKit). It provides a unified API for controlling browsers programmatically, making it the industry standard for automated browser interactions.

## Why Playwright + Anchor Browser?

Anchor Browser leverages Playwright's robust browser automation capabilities to provide enterprise-grade reliability and cross-browser compatibility. While Playwright handles the low-level browser control, Anchor Browser adds:

* Cloud-hosted browser instances - No local browser management required
* AI-powered interactions - Natural language task execution beyond traditional scripting
* Enterprise security - Isolated environments with authentication and proxy support
* Self-healing automations - Built-in error recovery and adaptation to website changes

### Key Playwright Capabilities

* Multi-Browser Support - Test across Chrome, Firefox, and Safari with identical code
* Fast & Reliable - Auto-wait for elements, built-in retry logic, and parallel execution
* Powerful Debugging - Time-travel debugging, trace viewer, and UI mode for visual testing
* Visual Testing - Automated screenshot comparison and visual regression detection
* Precise Element Selection - Advanced locators for reliable element targeting

### How It Works with Anchor Browser

When you connect to Anchor Browser, you're using Playwright's familiar API but with cloud-hosted browsers:

```javascript node.js theme={null}
import { chromium } from 'playwright';
import AnchorClient from 'anchorbrowser';

const anchorClient = new AnchorClient({
  apiKey: process.env.ANCHOR_API_KEY,
});

// First create a session
const session = await anchorClient.sessions.create();
const cdp_url = session.data.cdp_url;

// Then connect using the session's CDP URL
const browser = await chromium.connectOverCDP(cdp_url);
console.log('Browser connected');

browser.close();
```

This gives you all of Playwright's power while eliminating infrastructure complexity and adding enterprise features.

### Use Cases

* Business Workflow Automation - Automate repetitive tasks in ERP, CRM, and financial systems
* End-to-End Testing - Automated testing of web applications across browsers
* Web Scraping - Reliable data extraction from dynamic websites
* UI Automation - Form filling, clicking, and complex user workflow automation
* Visual Monitoring - Automated screenshot comparison and regression testing
* Performance Testing - Page load timing and interaction performance measurement

## Next Steps

* [Quick Start with Playwright](/quickstart/use-via-code) - Get started in 5 minutes
* [Examples](/examples/form-filling) - Real-world Playwright automation scripts
* [Browser Configuration](/api-reference/browser-sessions/start-browser-session#body-browser) - Advanced browser settings and options


# Integrate Puppeteer with Anchor Browser
Source: https://docs.anchorbrowser.io/integrations/open-source/puppeteer/index

Integrate Puppeteer and Anchor Browser

# What is Puppeteer?

[Puppeteer](https://pptr.dev/) is Google's Node.js library for controlling headless Chrome or Chromium browsers via the DevTools Protocol. It provides a high-level API for browser automation, making it one of the most widely adopted tools for web scraping, testing, and automated interactions.

## Why Puppeteer + Anchor Browser?

Anchor Browser leverages Puppeteer's mature CDP (Chrome DevTools Protocol) integration to provide seamless cloud browser automation. While Puppeteer handles the low-level browser control, Anchor Browser adds:

* Cloud-hosted browser instances - No local browser management required
* AI-powered interactions - Natural language task execution beyond traditional scripting
* Enterprise security - Isolated environments with authentication and proxy support
* Self-healing automations - Built-in error recovery and adaptation to website changes

### Key Puppeteer Capabilities

* CDP Native - Direct Chrome DevTools Protocol integration for precise browser control
* Lightweight & Fast - Minimal overhead with direct browser communication
* Extensive Ecosystem - Rich plugin ecosystem and community support
* Network Interception - Capture and modify network requests and responses
* PDF Generation - Convert web pages to PDFs with full rendering support

### How It Works with Anchor Browser

When you connect to Anchor Browser, you're using Puppeteer's familiar API but with cloud-hosted browsers:

```javascript node.js theme={null}
import AnchorClient from 'anchorbrowser';
import puppeteer from 'puppeteer-core';

const anchorClient = new AnchorClient({
  apiKey: process.env.ANCHOR_API_KEY,
});

// First create a session
const session = await anchorClient.sessions.create();
const cdpUrl = session.data.cdp_url;
const sessionId = session.data.id;

// Connect Puppeteer to the Anchor CDP session
const browser = await puppeteer.connect({
  browserWSEndpoint: cdpUrl,
  defaultViewport: null,
});

// Open a page and navigate
const page = await browser.newPage();
await page.goto('https://example.com');
console.log('Page title:', await page.title());

// Disconnect Puppeteer (doesn't close the Anchor session)
await browser.disconnect();

// Close the session via SDK
await anchorClient.sessions.delete(sessionId);
```

This gives you all of Puppeteer's power while eliminating infrastructure complexity and adding enterprise features.

### Use Cases

* Web Scraping - Extract data from dynamic JavaScript-heavy websites
* PDF Generation - Generate PDFs from web pages with precise rendering
* Screenshot Capture - Automated screenshot generation for monitoring and testing
* Form Automation - Automate form submissions and multi-step workflows
* Network Analysis - Intercept and analyze network traffic for debugging
* Performance Profiling - Measure page load times and runtime performance

## Next Steps

* [Quick Start with Puppeteer](/quickstart/use-via-code) - Get started in 5 minutes
* [Examples](/examples/form-filling) - Real-world Puppeteer automation scripts
* [Browser Configuration](/api-reference/browser-sessions/start-browser-session#body-browser) - Advanced browser settings and options


# Stagehand
Source: https://docs.anchorbrowser.io/integrations/stagehand

Integrate Stagehand with Anchor Browser for AI-powered browser automation

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


# Documentation
Source: https://docs.anchorbrowser.io/introduction

Welcome to Anchor Browser

Anchor is the platform for AI Agentic browser automation, which solves the challenge of automating workflows for web applications that lack APIs or have limited API coverage.

<video />

It simplifies the creation, deployment, and management of browser-based automations, transforming complex web interactions into simple API endpoints.

## Getting started

<CardGroup>
  <Card title="Quick start" icon="rocket" href="/quickstart/use-via-sdk">
    Get up and running with our quickstart guides, whether you code or don't
  </Card>

  <Card title="Live playground" icon="window-restore" href="https://app.anchorbrowser.io/playground">
    Build browser flows in a live interactive playground
  </Card>
</CardGroup>

## Next steps

Explore advanced features and capabilities

<CardGroup>
  <Card title="Connect to AI Agent Frameworks" icon="palette" href="/agent-frameworks/connect-to-agent-frameworks">
    Seamlessly integrate with leading AI agent frameworks.
  </Card>

  <Card title="Authentication and Identities" icon="fingerprint" href="/essentials/authentication-and-identity">
    Securely manage access and identities for your agents.
  </Card>

  <Card title="Build Tools" icon="screwdriver-wrench" href="/essentials/tool-building">
    Build web tools that empower your AI agent.
  </Card>

  <Card title="Example Use-Cases" icon="lightbulb" href="/examples">
    Jumpstart your project with practical, ready-to-use examples.
  </Card>
</CardGroup>


# API Quick Start
Source: https://docs.anchorbrowser.io/quickstart/use-via-api



Our APIs can be used directly (See our [API Reference](/api-reference)) or through integrations to automation platforms. We've created modules for our most commonly used API routes in each of the supported platforms.

Pick your preferred platform to view a quick-start for its usage:

<CardGroup>
  <Card title="Direct API Usage" icon="code" href="/api-reference">
    Use the API directly as you like, See our [API Reference](/api-reference) for more details.
  </Card>

  <Card title="Browser-use Integration" icon="atom-simple" href="/integrations/browseruse-deployment">
    Enhance Browser-Use capabilities with Anchor tools and cloud-based browser sessions
  </Card>

  <Card title="Make Integration" icon="grid-round-2-plus" href="/integrations/make">
    Integrate with Make (formerly Integromat) for no-code automation
  </Card>

  <Card title="CrewAI Integration" icon="people-group" href="/agent-frameworks/crewai">
    Integrate with CrewAI to gain robust qualities of Anchor Browser implementing no-code automation.
  </Card>

  <Card title="Langchain Integration" icon="crow" href="/agent-frameworks/langchain">
    Integrate with Langchain to leverage Anchor Browser's browser tools in your LLM workflows.
  </Card>

  <Card title="Custom Integration" icon="palette" href="/agent-frameworks/custom-agent-framework">
    Integrate with your own platform to leverage Anchor Browser's in your automations.
  </Card>
</CardGroup>

## Quick API Examples

### Single Step Browser Tool Call

The easiest way to utilize Anchor Browser is through browser tools. Browser tools are API endpoints that wrap end-to-end browser functionality in a single API call.

<CodeGroup>
  ```bash curl theme={null}
  curl -X POST "https://api.anchorbrowser.io/v1/tools/perform-web-task" \
    -H "anchor-api-key: YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "task": "Go to anchorbrowser.io and click the Get Started button",
      "headless": false
    }'
  ```

  ```javascript node.js theme={null}
  const axios = require('axios');

  const response = await axios.post('https://api.anchorbrowser.io/v1/tools/perform-web-task', {
    task: 'Go to anchorbrowser.io and click the Get Started button',
    headless: false
  }, {
    headers: {
      'anchor-api-key': process.env.ANCHOR_API_KEY,
      'Content-Type': 'application/json'
    }
  });

  console.log(response.data);
  ```

  ```python python theme={null}
  import requests

  response = requests.post('https://api.anchorbrowser.io/v1/tools/perform-web-task', 
    json={
      'task': 'Go to anchorbrowser.io and click the Get Started button',
      'headless': False
    },
    headers={
      'anchor-api-key': os.getenv('ANCHOR_API_KEY'),
      'Content-Type': 'application/json'
    }
  )

  print(response.json())
  ```
</CodeGroup>

### Multi-Step Browser Flow

For use cases where a custom browser configuration is required, or a multi-step browser flow is needed:

<Steps>
  <Step title="Fetch API Key">
    In [Anchor UI](https://app.anchorbrowser.io/api-key), copy your API key
  </Step>

  <Step title="Create a session">
    [Create a session](/api-reference/browser-sessions/start-browser-session) with the desired configuration
  </Step>

  <Step title="Use tools on the created session">
    Perform [tool calls](/tools-api-reference/ai-tools/ask-webpage) while referencing the created session ID
  </Step>
</Steps>


# Code Quick Start
Source: https://docs.anchorbrowser.io/quickstart/use-via-code



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


# SDK Quick Start
Source: https://docs.anchorbrowser.io/quickstart/use-via-sdk



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


# List Agent Resources
Source: https://docs.anchorbrowser.io/api-reference/agentic-capabilities/list-agent-resources

openapi-mintlify.yaml get /v1/sessions/{sessionId}/agent/files
List all resources that have been uploaded to the browser session for agent use.
Returns resource metadata including name, size, type, and last modified timestamp.




# Pause Agent
Source: https://docs.anchorbrowser.io/api-reference/agentic-capabilities/pause-agent

openapi-mintlify.yaml post /v1/sessions/{session_id}/agent/pause
Pauses the AI agent for the specified browser session.



# Resume Agent
Source: https://docs.anchorbrowser.io/api-reference/agentic-capabilities/resume-agent

openapi-mintlify.yaml post /v1/sessions/{session_id}/agent/resume
Resumes the AI agent for the specified browser session.



# Upload Agent Resources
Source: https://docs.anchorbrowser.io/api-reference/agentic-capabilities/upload-agent-resources

openapi-mintlify.yaml post /v1/sessions/{sessionId}/agent/files
Upload files as agent resources to a browser session using multipart/form-data. 
If you upload a ZIP file, it will be automatically extracted and the files will be made available as agent resources.
If you upload a single file, it will be saved directly as an agent resource.
Resources are then accessible to AI agents for task completion and automation.




# Get Perform Web Task Status
Source: https://docs.anchorbrowser.io/api-reference/ai-tools/get-perform-web-task-status

openapi-mintlify.yaml get /v1/tools/perform-web-task/{workflowId}/status
Get the status of an asynchronous perform-web-task execution by workflow ID.



# Perform Web Task
Source: https://docs.anchorbrowser.io/api-reference/ai-tools/perform-web-task

openapi-mintlify.yaml post /v1/tools/perform-web-task
Start from a URL and perform the given task.



# Create Application
Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/create-application

openapi-mintlify.yaml post /v1/applications
Creates a new application for identity management.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




# Create Authentication Flow
Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/create-authentication-flow

openapi-mintlify.yaml post /v1/applications/{applicationId}/auth-flows
Creates a new authentication flow for an application.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




# Create Identity Token
Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/create-identity-token

openapi-mintlify.yaml post /v1/applications/{applicationId}/tokens
Creates an identity token for a specific application. This token is used to initiate
an authentication flow for linking user identities to the application.

The callback URL must use HTTPS and is where the user will be redirected after authentication.




# Delete Application
Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/delete-application

openapi-mintlify.yaml delete /v1/applications/{applicationId}
Deletes an existing application.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




# Delete Authentication Flow
Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/delete-authentication-flow

openapi-mintlify.yaml delete /v1/applications/{applicationId}/auth-flows/{authFlowId}
Deletes an existing authentication flow.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




# Get Application
Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/get-application

openapi-mintlify.yaml get /v1/applications/{applicationId}
Retrieves details of a specific application by its ID.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




# List Application Authentication Flows
Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/list-application-authentication-flows

openapi-mintlify.yaml get /v1/applications/{applicationId}/auth-flows
Retrieves all authentication flows for a specific application.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




# List Application Identities
Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/list-application-identities

openapi-mintlify.yaml get /v1/applications/{applicationId}/identities
Retrieves all identities associated with a specific application.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




# List Applications
Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/list-applications

openapi-mintlify.yaml get /v1/applications
Retrieves all applications for the authenticated team.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




# Update Authentication Flow
Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/update-authentication-flow

openapi-mintlify.yaml patch /v1/applications/{applicationId}/auth-flows/{authFlowId}
Updates an existing authentication flow.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




# Create Batch Sessions
Source: https://docs.anchorbrowser.io/api-reference/batch-sessions/create-batch-sessions

openapi-mintlify.yaml post /v1/batch-sessions
Creates multiple browser sessions in a single batch operation. This endpoint allows you to 
create up to 5,000 browser sessions simultaneously with the same configuration.

The batch will be processed asynchronously, and you can monitor progress using the batch status endpoint.




# Get Batch Session Status
Source: https://docs.anchorbrowser.io/api-reference/batch-sessions/get-batch-session-status

openapi-mintlify.yaml get /v1/batch-sessions/{batch_id}
Retrieves detailed status information for a specific batch, including progress,
individual session details, and any errors that occurred.




# End All Sessions
Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/end-all-sessions

openapi-mintlify.yaml delete /v1/sessions/all
Terminates all active browser sessions associated with the provided API key.



# End Browser Session
Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/end-browser-session

openapi-mintlify.yaml delete /v1/sessions/{session_id}
Deletes the browser session associated with the provided browser session ID. Requires a valid API key for authentication.



# Get Browser Session
Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/get-browser-session

openapi-mintlify.yaml get /v1/sessions/{session_id}
Retrieves detailed information about a specific browser session.



# Get Browser Session Pages
Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/get-browser-session-pages

openapi-mintlify.yaml get /v1/sessions/{session_id}/pages
Retrieves a list of pages associated with a specific browser session.



# List All Sessions Status
Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/list-all-sessions-status

openapi-mintlify.yaml get /v1/sessions/all/status
Retrieves status information for all browser sessions associated with the API key.



# List Session Downloads
Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/list-session-downloads

openapi-mintlify.yaml get /v1/sessions/{session_id}/downloads
Retrieves metadata of files downloaded during a browser session. Requires a valid API key for authentication.



# Start Browser Session
Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/start-browser-session

openapi-mintlify.yaml post /v1/sessions
Allocates a new browser session for the user, with optional configurations for ad-blocking, captcha solving, proxy usage, and idle timeout.



# Upload Files
Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/upload-files

openapi-mintlify.yaml post /v1/sessions/{sessionId}/uploads
Upload files directly to a browser session for use with web forms and file inputs.

Files are saved to the session's uploads directory and can be referenced in CDP commands.




# Signal Event
Source: https://docs.anchorbrowser.io/api-reference/event-coordination/signal-event

openapi-mintlify.yaml post /v1/events/{event_name}
Signals an event with associated data, unblocking any clients waiting for this event.
This enables coordination between different browser sessions, workflows, or external processes.




# Wait for Event
Source: https://docs.anchorbrowser.io/api-reference/event-coordination/wait-for-event

openapi-mintlify.yaml post /v1/events/{event_name}/wait
Waits for a specific event to be signaled by another process, workflow, or session. 
This endpoint blocks until the event is signaled or the timeout is reached.
Useful for coordinating between multiple browser sessions or workflows.




# Delete Extension
Source: https://docs.anchorbrowser.io/api-reference/extensions/delete-extension

openapi-mintlify.yaml delete /v1/extensions/{id}
Delete an extension and remove it from storage



# Get Extension Details
Source: https://docs.anchorbrowser.io/api-reference/extensions/get-extension-details

openapi-mintlify.yaml get /v1/extensions/{id}
Get details of a specific extension by its ID



# List Extensions
Source: https://docs.anchorbrowser.io/api-reference/extensions/list-extensions

openapi-mintlify.yaml get /v1/extensions
Get all extensions for the authenticated user



# Upload Extension
Source: https://docs.anchorbrowser.io/api-reference/extensions/upload-extension

openapi-mintlify.yaml post /v1/extensions
Upload a new browser extension as a ZIP file. The extension will be validated and stored for use in browser sessions.



# Create Identity
Source: https://docs.anchorbrowser.io/api-reference/identities-early-availability/create-identity

openapi-mintlify.yaml post /v1/identities
Creates a new identity with credentials for authentication.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




# Delete Identity
Source: https://docs.anchorbrowser.io/api-reference/identities-early-availability/delete-identity

openapi-mintlify.yaml delete /v1/identities/{identityId}
Deletes an existing identity.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




# Get Identity
Source: https://docs.anchorbrowser.io/api-reference/identities-early-availability/get-identity

openapi-mintlify.yaml get /v1/identities/{identityId}
Retrieves details of a specific identity by its ID.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




# Get Identity Credentials
Source: https://docs.anchorbrowser.io/api-reference/identities-early-availability/get-identity-credentials

openapi-mintlify.yaml get /v1/identities/{identityId}/credentials
Retrieves the credentials for a specific identity. This endpoint returns sensitive credential data.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




# Update Identity
Source: https://docs.anchorbrowser.io/api-reference/identities-early-availability/update-identity

openapi-mintlify.yaml put /v1/identities/{identityId}
Updates an existing identity's name, metadata, or credentials.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




# Create Integration
Source: https://docs.anchorbrowser.io/api-reference/integrations/create-integration

openapi-mintlify.yaml post /v1/integrations
Creates a new integration with a third-party service like 1Password. 
The integration can then be used in browser sessions to automatically load secrets and credentials.




# Delete Integration
Source: https://docs.anchorbrowser.io/api-reference/integrations/delete-integration

openapi-mintlify.yaml delete /v1/integrations/{integrationId}
Deletes an existing integration and removes its stored credentials.



# List Integrations
Source: https://docs.anchorbrowser.io/api-reference/integrations/list-integrations

openapi-mintlify.yaml get /v1/integrations
Retrieves all integrations for the authenticated team.



# Copy Selected Text
Source: https://docs.anchorbrowser.io/api-reference/os-level-control/copy-selected-text

openapi-mintlify.yaml post /v1/sessions/{sessionId}/copy
Copies the currently selected text to the clipboard



# Drag and Drop
Source: https://docs.anchorbrowser.io/api-reference/os-level-control/drag-and-drop

openapi-mintlify.yaml post /v1/sessions/{sessionId}/drag-and-drop
Performs a drag and drop operation from start coordinates to end coordinates



# Get Clipboard Content
Source: https://docs.anchorbrowser.io/api-reference/os-level-control/get-clipboard-content

openapi-mintlify.yaml get /v1/sessions/{sessionId}/clipboard
Retrieves the current content of the clipboard



# Keyboard Shortcut
Source: https://docs.anchorbrowser.io/api-reference/os-level-control/keyboard-shortcut

openapi-mintlify.yaml post /v1/sessions/{sessionId}/keyboard/shortcut
Performs a keyboard shortcut using the specified keys



# Mouse Click
Source: https://docs.anchorbrowser.io/api-reference/os-level-control/mouse-click

openapi-mintlify.yaml post /v1/sessions/{sessionId}/mouse/click
Performs a mouse click at the specified coordinates



# Mouse Double Click
Source: https://docs.anchorbrowser.io/api-reference/os-level-control/mouse-double-click

openapi-mintlify.yaml post /v1/sessions/{sessionId}/mouse/doubleClick
Performs a double click at the specified coordinates



# Mouse Down
Source: https://docs.anchorbrowser.io/api-reference/os-level-control/mouse-down

openapi-mintlify.yaml post /v1/sessions/{sessionId}/mouse/down
Performs a mouse button down action at the specified coordinates



# Mouse Move
Source: https://docs.anchorbrowser.io/api-reference/os-level-control/mouse-move

openapi-mintlify.yaml post /v1/sessions/{sessionId}/mouse/move
Moves the mouse cursor to the specified coordinates



# Mouse Up
Source: https://docs.anchorbrowser.io/api-reference/os-level-control/mouse-up

openapi-mintlify.yaml post /v1/sessions/{sessionId}/mouse/up
Performs a mouse button up action at the specified coordinates



# Navigate to URL
Source: https://docs.anchorbrowser.io/api-reference/os-level-control/navigate-to-url

openapi-mintlify.yaml post /v1/sessions/{sessionId}/goto
Navigates the browser session to the specified URL



# Paste Text
Source: https://docs.anchorbrowser.io/api-reference/os-level-control/paste-text

openapi-mintlify.yaml post /v1/sessions/{sessionId}/paste
Pastes text at the current cursor position



# Scroll
Source: https://docs.anchorbrowser.io/api-reference/os-level-control/scroll

openapi-mintlify.yaml post /v1/sessions/{sessionId}/scroll
Performs a scroll action at the specified coordinates



# Set Clipboard Content
Source: https://docs.anchorbrowser.io/api-reference/os-level-control/set-clipboard-content

openapi-mintlify.yaml post /v1/sessions/{sessionId}/clipboard
Sets the content of the clipboard



# Take Screenshot
Source: https://docs.anchorbrowser.io/api-reference/os-level-control/take-screenshot

openapi-mintlify.yaml get /v1/sessions/{sessionId}/screenshot
Takes a screenshot of the current browser session and returns it as an image.



# Type Text
Source: https://docs.anchorbrowser.io/api-reference/os-level-control/type-text

openapi-mintlify.yaml post /v1/sessions/{sessionId}/keyboard/type
Types the specified text with optional delay between keystrokes



# Create Profile
Source: https://docs.anchorbrowser.io/api-reference/profiles/create-profile

openapi-mintlify.yaml post /v1/profiles
Creates a new profile from a browser session. A Profile stores cookies, local storage, and cache.



# Delete Profile
Source: https://docs.anchorbrowser.io/api-reference/profiles/delete-profile

openapi-mintlify.yaml delete /v1/profiles/{name}
Deletes an existing profile by its name.



# Get Profile
Source: https://docs.anchorbrowser.io/api-reference/profiles/get-profile

openapi-mintlify.yaml get /v1/profiles/{name}
Retrieves details of a specific profile by its name.



# List Profiles
Source: https://docs.anchorbrowser.io/api-reference/profiles/list-profiles

openapi-mintlify.yaml get /v1/profiles
Fetches all stored profiles.



# Get Session Recording
Source: https://docs.anchorbrowser.io/api-reference/session-recordings/get-session-recording

openapi-mintlify.yaml get /v1/sessions/{session_id}/recordings/primary/fetch
Downloads the primary recording file for the specified browser session. Returns the recording as an MP4 file.



# List Session Recordings
Source: https://docs.anchorbrowser.io/api-reference/session-recordings/list-session-recordings

openapi-mintlify.yaml get /v1/sessions/{session_id}/recordings
Retrieves the URLs of the browser session's video recordings. Requires a valid API key for authentication.



# Pause Session Recording
Source: https://docs.anchorbrowser.io/api-reference/session-recordings/pause-session-recording

openapi-mintlify.yaml post /v1/sessions/{session_id}/recordings/pause
Pauses the video recording for the specified browser session.



# Resume Session Recording
Source: https://docs.anchorbrowser.io/api-reference/session-recordings/resume-session-recording

openapi-mintlify.yaml post /v1/sessions/{session_id}/recordings/resume
Resumes the video recording for the specified browser session.



# Create or Update Task Draft
Source: https://docs.anchorbrowser.io/api-reference/tasks/create-or-update-task-draft

openapi-mintlify.yaml post /v1/task/{taskId}/draft
Creates or updates the draft version of a task. Draft versions are used for development
and testing before publishing.




# Create Task
Source: https://docs.anchorbrowser.io/api-reference/tasks/create-task

openapi-mintlify.yaml post /v1/task
Creates a new task or updates an existing task with the same name. Tasks are reusable code snippets 
that can be executed in browser sessions. Tasks support versioning with draft and published versions.




# Delete Task
Source: https://docs.anchorbrowser.io/api-reference/tasks/delete-task

openapi-mintlify.yaml delete /v1/task/{taskId}
Soft deletes a task and all its versions. The task will no longer be accessible
but the data is preserved for potential recovery.




# Delete Task Version
Source: https://docs.anchorbrowser.io/api-reference/tasks/delete-task-version

openapi-mintlify.yaml delete /v1/task/{taskId}/{taskVersion}
Soft deletes a specific version of a task. The version will no longer be accessible
but the data is preserved for potential recovery.




# Deploy Task
Source: https://docs.anchorbrowser.io/api-reference/tasks/deploy-task

openapi-mintlify.yaml post /v1/task/{taskId}/deploy
Deploys a task by creating a new version with auto-incremented version number.
This is the recommended way to publish task changes.




# Get Latest Task Version
Source: https://docs.anchorbrowser.io/api-reference/tasks/get-latest-task-version

openapi-mintlify.yaml get /v1/task/{taskId}/latest
Retrieves the latest version of a task, including the full code content.




# Get Task Draft
Source: https://docs.anchorbrowser.io/api-reference/tasks/get-task-draft

openapi-mintlify.yaml get /v1/task/{taskId}/draft
Retrieves the draft version of a task, including the full code content.




# Get Task Execution Result
Source: https://docs.anchorbrowser.io/api-reference/tasks/get-task-execution-result

openapi-mintlify.yaml get /v1/task/{taskId}/executions/{executionId}
Retrieves a single execution result by its ID. This endpoint is useful for polling
execution status in async mode or retrieving detailed execution information.




# Get Task Metadata
Source: https://docs.anchorbrowser.io/api-reference/tasks/get-task-metadata

openapi-mintlify.yaml get /v1/task/{taskId}
Retrieves task metadata without the code content. Useful for getting task information
without downloading the full task code.




# Get Task Version
Source: https://docs.anchorbrowser.io/api-reference/tasks/get-task-version

openapi-mintlify.yaml get /v1/task/{taskId}/{taskVersion}
Retrieves a specific version of a task, including the full code content.




# List Task Executions
Source: https://docs.anchorbrowser.io/api-reference/tasks/list-task-executions

openapi-mintlify.yaml get /v1/task/{taskId}/executions
Retrieves execution history for a task, including success/failure status,
execution times, and outputs. Results can be filtered by version and status.




# List Task Versions
Source: https://docs.anchorbrowser.io/api-reference/tasks/list-task-versions

openapi-mintlify.yaml get /v1/task/{taskId}/versions
Retrieves all versions of a specific task, including draft and published versions.




# List Tasks
Source: https://docs.anchorbrowser.io/api-reference/tasks/list-tasks

openapi-mintlify.yaml get /v1/task
Retrieves a paginated list of all tasks for the authenticated team. Tasks are returned 
with their latest version information and metadata.




# Publish Task Version
Source: https://docs.anchorbrowser.io/api-reference/tasks/publish-task-version

openapi-mintlify.yaml post /v1/task/{taskId}/{taskVersion}
Publishes a specific version of a task. This creates a new version if it doesn't exist,
or updates an existing version's metadata.




# Run Task
Source: https://docs.anchorbrowser.io/api-reference/tasks/run-task

openapi-mintlify.yaml post /v1/task/run
Executes a task in a browser session. The task can be run with a specific version or the latest version.
Optionally, you can provide an existing session ID or let the system create a new one.




# Run Task by Name
Source: https://docs.anchorbrowser.io/api-reference/tasks/run-task-by-name

openapi-mintlify.yaml post /v1/task/run/{taskName}
Executes a task by its name, always using the latest version. This is a convenience endpoint
for running tasks without needing to know the task ID.




# Update Task Metadata
Source: https://docs.anchorbrowser.io/api-reference/tasks/update-task-metadata

openapi-mintlify.yaml put /v1/task/{taskId}
Updates task metadata (name and description). This does not affect the task code or versions.




# Get Webpage Content
Source: https://docs.anchorbrowser.io/api-reference/tools/get-webpage-content

openapi-mintlify.yaml post /v1/tools/fetch-webpage
Retrieve the rendered content of a webpage, optionally formatted as Markdown or HTML.



# Screenshot Webpage
Source: https://docs.anchorbrowser.io/api-reference/tools/screenshot-webpage

openapi-mintlify.yaml post /v1/tools/screenshot
This endpoint captures a screenshot of the specified webpage using Chromium. Users can customize the viewport dimensions and capture options.



# USCIS Form I-9
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/ucis-i9

Automate employment eligibility verification workflows with Playwright when APIs aren't available.

# How to Automate USCIS Form I-9 with Playwright

Automate USCIS employment eligibility verification workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual onboarding documentation and reduce compliance errors by automating repetitive employee verification processes. Use Playwright to interact with E-Verify and USCIS systems programmatically.

[View USCIS developer resources](https://www.uscis.gov/tools) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [USCIS Form I-9](https://www.uscis.gov/sites/default/files/document/forms/i-9.pdf) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to E-Verify system
await page.goto('https://www.e-verify.gov/');
await page.fill('[data-testid="username"]', process.env.EVERIFY_USERNAME);
await page.fill('[data-testid="password"]', process.env.EVERIFY_PASSWORD);
await page.click('[data-testid="login-button"]');

// Start new I-9 form
await page.click('[data-testid="new-case"]');
await page.click('[data-testid="form-i9"]');
await page.selectOption('[name="form_version"]', '11_21_2023');

// Employer information
await page.fill('[name="employer_name"]', 'TechVentures Solutions Inc');
await page.fill('[name="employer_ein"]', '12-3456789');
await page.fill('[name="employer_address"]', '2800 Corporate Drive, Suite 500');
await page.fill('[name="employer_city"]', 'San Jose');
await page.selectOption('[name="employer_state"]', 'CA');
await page.fill('[name="employer_zip"]', '95134');

// Section 1: Employee Information and Attestation
// Employee personal information
await page.fill('[name="last_name"]', 'Rodriguez');
await page.fill('[name="first_name"]', 'Maria');
await page.fill('[name="middle_initial"]', 'C');
await page.fill('[name="other_last_names"]', 'Garcia');

// Address
await page.fill('[name="address"]', '456 Apartment Street, Unit 12B');
await page.fill('[name="city"]', 'San Jose');
await page.selectOption('[name="state"]', 'CA');
await page.fill('[name="zip"]', '95110');

// Date of birth and contact
await page.fill('[name="date_of_birth"]', '07/15/1992');
await page.fill('[name="ssn"]', '123-45-6789');
await page.fill('[name="email"]', 'maria.rodriguez@email.com');
await page.fill('[name="phone"]', '408-555-0189');

// Citizenship/immigration status
await page.selectOption('[name="citizenship_status"]', 'us_citizen');

// Employee attestation
await page.check('[name="employee_aware_penalties"]');
await page.fill('[name="employee_signature"]', 'Maria C Rodriguez');
await page.fill('[name="employee_signature_date"]', '03/01/2025');

// Preparer/translator (if applicable)
await page.selectOption('[name="preparer_used"]', 'no');

// Section 2: Employer Review and Verification
// Document verification - List A (identity and employment authorization)
await page.selectOption('[name="document_list"]', 'list_a');
await page.selectOption('[name="list_a_document"]', 'us_passport');
await page.fill('[name="document_title"]', 'U.S. Passport');
await page.fill('[name="issuing_authority"]', 'U.S. Department of State');
await page.fill('[name="document_number"]', '123456789');
await page.fill('[name="expiration_date"]', '06/15/2030');

// Alternative: List B and List C documents
// Uncomment if using List B + List C instead of List A
/*
await page.selectOption('[name="document_list"]', 'list_b_and_c');

// List B - Identity document
await page.selectOption('[name="list_b_document"]', 'drivers_license');
await page.fill('[name="list_b_document_title"]', 'Driver\'s License');
await page.fill('[name="list_b_issuing_authority"]', 'California DMV');
await page.fill('[name="list_b_document_number"]', 'D1234567');
await page.fill('[name="list_b_expiration"]', '07/15/2029');

// List C - Employment authorization document
await page.selectOption('[name="list_c_document"]', 'social_security_card');
await page.fill('[name="list_c_document_title"]', 'Social Security Card');
await page.fill('[name="list_c_issuing_authority"]', 'Social Security Administration');
await page.fill('[name="list_c_document_number"]', '123-45-6789');
*/

// Physical examination of documents
await page.check('[name="documents_appear_genuine"]');
await page.check('[name="documents_relate_to_employee"]');
await page.fill('[name="first_day_of_employment"]', '03/15/2025');

// Additional information
await page.fill('[name="employer_business_name"]', 'TechVentures Solutions Inc');
await page.fill('[name="employer_representative_name"]', 'Jennifer HR Manager');
await page.fill('[name="employer_representative_title"]', 'Human Resources Manager');

// Employer certification
await page.check('[name="certify_examination_completed"]');
await page.fill('[name="employer_signature"]', 'Jennifer HR Manager');
await page.fill('[name="employer_signature_date"]', '03/01/2025');

// Section 3: Reverification and Rehires (if applicable)
await page.selectOption('[name="section_3_required"]', 'no');

// E-Verify case creation (if enrolled)
await page.check('[name="create_everify_case"]');
await page.fill('[name="hire_date"]', '03/15/2025');
await page.selectOption('[name="employee_type"]', 'regular_full_time');

// Supporting documentation upload
await page.click('[data-testid="upload-document-front"]');
await page.setInputFiles('[name="document_image_front"]', './documents/passport_photo_page.pdf');
await page.click('[data-testid="upload-document-back"]');
await page.setInputFiles('[name="document_image_back"]', './documents/passport_signature_page.pdf');

// Record retention information
await page.fill('[name="retention_start_date"]', '03/01/2025');
await page.selectOption('[name="storage_location"]', 'secure_digital_system');
await page.fill('[name="retention_period_years"]', '3');

// Remote verification (if applicable)
await page.selectOption('[name="remote_verification"]', 'no');

// Quality assurance review
await page.check('[name="qa_documents_legible"]');
await page.check('[name="qa_dates_consistent"]');
await page.check('[name="qa_sections_complete"]');
await page.check('[name="qa_signatures_present"]');

// Compliance notes
await page.fill('[name="internal_notes"]', 'Employee provided original U.S. passport. Documents examined in person on 3/1/25. All information verified and accurate. E-Verify case will be created upon hire date.');

// Authorized representative information
await page.fill('[name="hr_contact_name"]', 'Jennifer HR Manager');
await page.fill('[name="hr_contact_email"]', 'hr@techventures.com');
await page.fill('[name="hr_contact_phone"]', '408-555-0100');

// Company location for this employee
await page.fill('[name="work_location_address"]', '2800 Corporate Drive, Suite 500');
await page.fill('[name="work_location_city"]', 'San Jose');
await page.selectOption('[name="work_location_state"]', 'CA');
await page.fill('[name="work_location_zip"]', '95134');

// Supervisor information
await page.fill('[name="supervisor_name"]', 'David Engineering Manager');
await page.fill('[name="supervisor_email"]', 'dmanager@techventures.com');
await page.fill('[name="department"]', 'Software Engineering');

// Job title and details
await page.fill('[name="job_title"]', 'Software Engineer II');
await page.fill('[name="employee_id"]', 'EMP-2025-0789');
await page.selectOption('[name="employment_type"]', 'permanent_full_time');
await page.fill('[name="annual_salary"]', '125000');

// Final certification
await page.check('[name="certify_compliance"]');
await page.check('[name="acknowledge_penalties"]');
await page.check('[name="agree_to_retention_requirements"]');

await page.click('[data-testid="submit-i9"]');

// Download completed form
await page.click('[data-testid="download-i9-pdf"]');

await browser.close();
```

Playwright handles document validation, data verification, and USCIS submission processes automatically. You can automate new hire onboarding, reverification workflows, and compliance audits.

## Scale your USCIS Form I-9 automation with Anchor Browser

Run your Playwright USCIS automations on cloud browsers with enterprise-grade reliability and persistent employment verification sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# VA Form 21-526EZ
Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/government/USA/federal/va-21-526ez

Automate VA disability compensation application workflows with Playwright when APIs aren't available.

# How to Automate VA Form 21-526EZ with Playwright

Automate VA disability compensation and related benefits application workflows with Playwright when APIs aren't available or sufficient. You'll eliminate manual claims processing and reduce approval delays by automating repetitive VA disability documentation processes. Use Playwright to interact with VA.gov systems programmatically.

[View VA developer resources](https://developer.va.gov/) for available APIs when applicable.

## Setup

Install Playwright and configure authentication:

```bash theme={null}
npm install playwright
```

## Automate Workflows

Create scripts for common [VA Form 21-526EZ](https://www.vba.va.gov/pubs/forms/VBA-21-526EZ-ARE.pdf) tasks:

```JavaScript theme={null}
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();

// Navigate to VA.gov
await page.goto('https://www.va.gov/find-forms/'');

// Start new disability claim
await page.click('[data-testid="start-new-claim"]');
await page.selectOption('[name="claim_type"]', 'original_claim');

// Veteran information
await page.fill('[name="last_name"]', 'Martinez');
await page.fill('[name="first_name"]', 'James');
await page.fill('[name="middle_name"]', 'Michael');
await page.fill('[name="suffix"]', '');
await page.fill('[name="ssn"]', '123-45-6789');
await page.fill('[name="va_file_number"]', 'C-12345678');

// Contact information
await page.fill('[name="date_of_birth"]', '08/15/1985');
await page.selectOption('[name="gender"]', 'male');

// Mailing address
await page.fill('[name="address_line_1"]', '789 Veterans Boulevard');
await page.fill('[name="address_line_2"]', 'Apt 4D');
await page.fill('[name="city"]', 'Jacksonville');
await page.selectOption('[name="state"]', 'FL');
await page.fill('[name="zip"]', '32202');
await page.selectOption('[name="country"]', 'USA');

// Phone numbers
await page.fill('[name="phone_home"]', '904-555-0123');
await page.fill('[name="phone_mobile"]', '904-555-0124');
await page.fill('[name="email"]', 'jmartinez@email.com');

// Contact preferences
await page.check('[name="contact_by_email"]');
await page.check('[name="contact_by_phone"]');

// Service information
await page.selectOption('[name="branch_of_service"]', 'army');
await page.fill('[name="service_number"]', 'US-123456789');

// Service period 1
await page.fill('[name="service_start_date_1"]', '06/15/2003');
await page.fill('[name="service_end_date_1"]', '08/20/2011');
await page.selectOption('[name="separation_type_1"]', 'honorable');

// Service period 2 (if applicable)
await page.click('[data-testid="add-service-period"]');
await page.fill('[name="service_start_date_2"]', '09/01/2011');
await page.fill('[name="service_end_date_2"]', '05/30/2015');
await page.selectOption('[name="separation_type_2"]', 'honorable');

// Reserve/National Guard service
await page.check('[name="reserve_service"]');
await page.fill('[name="reserve_component"]', 'Army National Guard');
await page.fill('[name="unit_name"]', '53rd Infantry Brigade Combat Team');
await page.fill('[name="unit_phone"]', '904-555-0200');

// Combat service
await page.check('[name="served_in_combat"]');
await page.fill('[name="combat_locations"]', 'Iraq (2007-2008), Afghanistan (2010-2011)');

// Prisoner of war
await page.selectOption('[name="pow_status"]', 'no');

// Medals and awards
await page.fill('[name="awards"]', 'Bronze Star, Purple Heart, Combat Infantryman Badge, Army Commendation Medal');

// Disabilities being claimed
// Condition 1: PTSD
await page.click('[data-testid="add-disability"]');
await page.fill('[name="condition_name_1"]', 'Post-Traumatic Stress Disorder (PTSD)');
await page.selectOption('[name="condition_cause_1"]', 'combat');
await page.fill('[name="condition_start_date_1"]', '09/2008');
await page.fill('[name="condition_description_1"]', 'Recurring nightmares, flashbacks to combat situations, anxiety, hypervigilance, difficulty sleeping. Symptoms began during deployment to Iraq and have persisted.');

// Condition 2: Tinnitus
await page.click('[data-testid="add-disability"]');
await page.fill('[name="condition_name_2"]', 'Tinnitus');
await page.selectOption('[name="condition_cause_2"]', 'noise_exposure');
await page.fill('[name="condition_start_date_2"]', '06/2007');
await page.fill('[name="condition_description_2"]', 'Constant ringing in both ears. Began after prolonged exposure to weapons fire and explosions during combat operations.');

// Condition 3: Lower back injury
await page.click('[data-testid="add-disability"]');
await page.fill('[name="condition_name_3"]', 'Chronic Lower Back Pain');
await page.selectOption('[name="condition_cause_3"]', 'injury');
await page.fill('[name="condition_start_date_3"]', '03/2010');
await page.fill('[name="condition_description_3"]', 'Lumbar spine injury from IED blast. Chronic pain, limited range of motion, difficulty standing for extended periods.');

// Condition 4: Knee injury
await page.click('[data-testid="add-disability"]');
await page.fill('[name="condition_name_4"]', 'Right Knee Injury');
await page.selectOption('[name="condition_cause_4"]', 'injury');
await page.fill('[name="condition_start_date_4"]', '03/2010');
await page.fill('[name="condition_description_4"]', 'Right knee damaged in same IED incident. Torn meniscus, chronic pain, instability, arthritis.');

// Treatment history
await page.check('[name="receiving_va_care"]');
await page.fill('[name="va_facility_1"]', 'Malcom Randall VA Medical Center');
await page.fill('[name="va_facility_city_1"]', 'Gainesville');
await page.selectOption('[name="va_facility_state_1"]', 'FL');
await page.fill('[name="va_treatment_dates_1"]', '2015 - Present');

// Private medical treatment
await page.check('[name="private_treatment"]');
await page.fill('[name="private_provider_1"]', 'Dr. Sarah Orthopedic Surgeon');
await page.fill('[name="private_facility_1"]', 'Jacksonville Orthopedic Center');
await page.fill('[name="private_address_1"]', '456 Medical Plaza');
await page.fill('[name="private_city_1"]', 'Jacksonville');
await page.selectOption('[name="private_state_1"]', 'FL');
await page.fill('[name="private_zip_1"]', '32207');
await page.fill('[name="private_treatment_dates_1"]', '2012-2015');

// Mental health treatment
await page.fill('[name="mental_health_provider"]', 'Dr. Michael Psychiatrist');
await page.fill('[name="mental_health_facility"]', 'Veterans Mental Health Clinic');
await page.fill('[name="mental_health_dates"]', '2015 - Present');

// Hospitalizations
await page.check('[name="hospitalizations"]');
await page.fill('[name="hospital_name_1"]', 'Walter Reed Army Medical Center');
await page.fill('[name="hospital_admission_date_1"]', '04/01/2010');
await page.fill('[name="hospital_discharge_date_1"]', '04/15/2010');
await page.fill('[name="hospital_reason_1"]', 'Treatment for injuries sustained in IED explosion');

// Supporting documents
await page.click('[data-testid="upload-dd214"]');
await page.setInputFiles('[name="discharge_papers"]', './documents/dd214.pdf');
await page.click('[data-testid="upload-service-medical"]');
await page.setInputFiles('[name="service_medical_records"]', './documents/service_treatment_records.pdf');
await page.click('[data-testid="upload-private-medical"]');
await page.setInputFiles('[name="private_medical_records"]', './documents/private_treatment_records.pdf');
await page.click('[data-testid="upload-buddy-statements"]');
await page.setInputFiles('[name="buddy_statements"]', './documents/witness_statements.pdf');

// Special circumstances
await page.check('[name="combat_related"]');
await page.check('[name="caused_by_service"]');

// Homelessness
await page.selectOption('[name="homeless_status"]', 'at_risk');
await page.fill('[name="homeless_contact"]', 'Florida Veterans Affairs Office');
await page.fill('[name="homeless_phone"]', '904-555-0300');

// Terminal illness
await page.selectOption('[name="terminal_illness"]', 'no');

// Fully developed claim
await page.check('[name="fdc_election"]');
await page.check('[name="understand_fdc"]');

// Direct deposit information
await page.check('[name="direct_deposit"]');
await page.selectOption('[name="account_type"]', 'checking');
await page.fill('[name="routing_number"]', '063100277');
await page.fill('[name="account_number"]', '123456789012');
await page.fill('[name="bank_name"]', 'Navy Federal Credit Union');

// Payment address (if different)
await page.selectOption('[name="payment_address_same"]', 'yes');

// Dependents
await page.check('[name="has_dependents"]');

// Spouse information
await page.fill('[name="spouse_first_name"]', 'Jennifer');
await page.fill('[name="spouse_middle_name"]', 'Ann');
await page.fill('[name="spouse_last_name"]', 'Martinez');
await page.fill('[name="spouse_ssn"]', '987-65-4321');
await page.fill('[name="spouse_dob"]', '11/20/1987');
await page.fill('[name="marriage_date"]', '06/15/2012');
await page.selectOption('[name="marriage_type"]', 'ceremonial');

// Children
await page.click('[data-testid="add-child"]');
await page.fill('[name="child_first_name_1"]', 'Emily');
await page.fill('[name="child_middle_name_1"]', 'Rose');
await page.fill('[name="child_last_name_1"]', 'Martinez');
await page.fill('[name="child_ssn_1"]', '234-56-7890');
await page.fill('[name="child_dob_1"]', '08/10/2013');
await page.selectOption('[name="child_relationship_1"]', 'biological');
await page.check('[name="child_unmarried_1"]');
await page.check('[name="child_under_18_1"]');

// Employment information
await page.selectOption('[name="employment_status"]', 'unemployed');
await page.fill('[name="last_employment_date"]', '03/2015');
await page.fill('[name="unable_to_work_date"]', '03/2015');
await page.fill('[name="unemployment_reason"]', 'Service-connected disabilities prevent full-time employment');

// Education and training
await page.check('[name="using_gi_bill"]');
await page.fill('[name="school_name"]', 'Florida State College at Jacksonville');
await page.fill('[name="education_start_date"]', '08/2016');

// Other benefits
await page.check('[name="receiving_ssdi"]');
await page.fill('[name="ssdi_start_date"]', '01/2016');
await page.fill('[name="ssdi_monthly_amount"]', '1500');

// Military retirement
await page.selectOption('[name="receiving_military_retirement"]', 'no');

// VA pension
await page.selectOption('[name="receiving_va_pension"]', 'no');

// Intent to file date
await page.fill('[name="intent_to_file_date"]', '01/15/2025');

// Certification and signatures
await page.check('[name="certify_accuracy"]');
await page.check('[name="certify_authorization"]');
await page.check('[name="understand_penalties"]');
await page.check('[name="authorize_disclosure"]');
await page.check('[name="agree_to_exam"]');

// Privacy act notice acknowledgment
await page.check('[name="privacy_act_acknowledged"]');

// Veteran signature
await page.fill('[name="veteran_signature"]', 'James Michael Martinez');
await page.fill('[name="signature_date"]', '03/10/2025');

// Representative information (if applicable)
await page.selectOption('[name="has_representative"]', 'yes');
await page.fill('[name="representative_name"]', 'Veterans Service Organization - DAV');
await page.fill('[name="representative_phone"]', '904-555-0400');
await page.fill('[name="representative_email"]', 'davjacksonville@dav.org');

await page.click('[data-testid="submit-claim"]');

// Download confirmation
await page.click('[data-testid="download-confirmation"]');

await browser.close();
```

Playwright handles medical documentation, service verification, and VA submission processes automatically. You can automate disability claims, dependency declarations, and benefit application workflows.

## Scale your VA Form 21-526EZ automation with Anchor Browser

Run your Playwright VA automations on cloud browsers with enterprise-grade reliability and persistent veterans benefits sessions. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)


# Pricing
Source: https://docs.anchorbrowser.io/pricing

Simple, transparent pricing for Anchor Browser automation platform

# Simple, Transparent Pricing

Pay only for what you use. No hidden fees, no surprises.

## Pricing Structure

<CardGroup>
  <Card title="Browser Creation" icon="browser">
    **\$0.01 per browser**

    Every new browser instance created incurs the minimal fee, ensuring cost-effective scaling of your automation workflows.
  </Card>

  <Card title="Browser Usage" icon="clock">
    **\$0.05 per browser hour**

    Charges are based on the total active time of the browser session, calculated to the nearest full minute.
  </Card>

  <Card title="Anchor Proxy" icon="shield">
    **\$8 per GB**

    High-speed, secure connections with residential or mobile IP addresses for seamless automation across the web.
  </Card>

  <Card title="AI Steps" icon="brain">
    **\$0.01 per step**

    Each AI task can consist of multiple steps, depending on its length and complexity.
  </Card>
</CardGroup>

# Plans

Select the plan that matches your automation needs and scale.

<CardGroup>
  <Card>
    # Free

    **\$5 free credits per month**

    Perfect for early exploration and learning the basics.

    * Up to 5 concurrent browsers
    * Up to 500 browser sessions
    * Web proxy available
    * Automated Captcha bypass
  </Card>

  <Card>
    # Starter

    **From \$20.00/month**

    Cloudflare Verified Browser Agents with automated captcha bypass.

    * Up to 25 concurrent browsers
    * Run on any geolocation
    * Authenticated (Logged in) Browsers
    * Built in and custom proxy support
  </Card>

  <Card>
    # Growth

    **From \$1,500/month**

    Enterprise-grade solution with full compliance and security.

    * Up to 100 concurrent browsers
    * SOC2 Type 2, ISO27001, HIPAA, GDPR
    * Anchor Chromium - Full stealth solution
    * BAA, DPA, SLA Guarantee
  </Card>
</CardGroup>

## Example Calculation

<Card title="Cost Breakdown Example">
  **Scenario**: 10 browsers running for 5 hours, using 2GB of residential proxy data

  | Service          | Calculation                    | Cost        |
  | ---------------- | ------------------------------ | ----------- |
  | Browser Creation | 10 browsers × \$0.01           | \$0.10      |
  | Browser Hours    | 10 browsers × 5 hours × \$0.05 | \$2.50      |
  | Proxy Data       | 2GB × \$8                      | \$16.00     |
  | **Total**        |                                | **\$18.60** |
</Card>


# Trust & Security
Source: https://docs.anchorbrowser.io/security



Anchor was engineered from the ground up to be the definitive secure browser solution, empowering developers to deploy to production with confidence. We provide the essential security backbone and advanced capabilities required to build the next generation of browser-based workloads.

This document outlines the security framework of Anchor Browser, covering:

* The reasons why leading enterprises build their solutions on Anchor Browser.
* An overview of our comprehensive Security Architecture.

For a detailed report on our compliance and security posture, please visit the [Anchor Trust Portal](https://trust.anchorbrowser.io/)

## Why Enterprise solutions are built on Anchor Browser

Anchor Browser is the result of deep security expertise from industry veterans, with our team hailing from leaders in cybersecurity such as SentinelOne, Noname Security (acquired by Akamai), and various specialized intelligence units. This collective experience has allowed us to embed robust security capabilities directly into the browser, giving our customers a distinct advantage in enterprise trust, security, and compliance.

### 1. Advanced Features for a More Secure End Solution

* **Complete Browser Isolation & Disposal**: Anchor creates a dedicated, isolated virtual machine (VM) for each browser instance. This VM is permanently terminated and erased upon session completion, ensuring that browsers are never reused and data remnants are eliminated.

* **Official Headful Browser Environments**: As the sole provider of secured and sandboxed environments using the official "Headful" browser operation mode, Anchor runs browsers as they were designed to be run. This ensures maximum stability and leverages the most rigorously tested and penetration-tested browser architecture.

* **Integrated Domain & Network Guardrails**: Anchor implements default network protections to shield customers from malicious websites. We also offer the ability to define granular whitelists of allowed domains, providing precise control over network access at the browser level.

* **Secure Authentication & Credential Management**: With Anchor, customers are never required to store credentials on our platform. Our browsers enable authenticated workflows using secure, encrypted, session-based authentication, eliminating the risks associated with stored credential-based logins.

* **Strict Tenant Isolation**: Anchor enforces rigorous logical isolation between all tenants. This architectural constraint guarantees the integrity and confidentiality of each customer's data.

* **Secure Peer-to-Peer File Transfers**: Secure Peer-to-Peer File Transfers: Uniquely, Anchor facilitates secure file downloads through a peer-to-peer mechanism. File downloads initiated in the browser are transferred directly to the customer's environment, meaning no file artifacts are ever created or stored on Anchor's infrastructure.

### 2. A Secure-by-Design Architecture

Anchor is built on a secure-by-design methodology. This principle ensures that the default configuration is always the most secure, significantly reducing the risk of misconfiguration errors and providing a foundation of trust from the moment you start.

### 3. Shared Responsibility Model

Our shared responsibility model clearly defines the security obligations of both Anchor and our customers. This well defined ownership perimeter approach ensures that all aspects of security are managed effectively, from the underlying infrastructure we secure to the applications you build on top of it.

### 4. Vetted and Audited Supply Chain

We maintain a rigorous security review and auditing process for our entire supply chain. Every component and third-party vendor is scrutinized to ensure they meet our high security standards, protecting our platform and our customers from upstream vulnerabilities.

## Product Architecture & Security Design

### Critical Security Controls

#### Storage of customer data

A core principle of Anchor Browser is minimizing data persistence. By design, we do not store customer data from within the browser sessions. Each browser instance runs in a dedicated, ephemeral virtual machine that is completely destroyed upon session termination. This means that any data accessed, generated, or downloaded during a session is either transferred directly to the customer's own environment via our secure peer-to-peer capability or is irretrievably deleted with the virtual machine. The only customer data we store is essential account and configuration information required for providing our service, such as user roles and network guardrail settings.

#### Data Residency

Anchor Browser infrastructure is by default fully hosted in the United States. All customer data, including browser sessions, account information, and configuration data, is processed and stored exclusively in the AWS `us-east-2` data center in Ohio.

For organizations requiring EU-based infrastructure with full GDPR compliance, we offer dedicated European data residency in the AWS `eu-central-1` data center in Frankfurt on the Growth plan. Contact us at [support@anchorbrowser.io](mailto:support@anchorbrowser.io) or [schedule a call](https://cal.com/team/anchor-browser/30-min-meeting) to get started.

#### Confidentiality & Protection of Customer Data

We enforce strict measures to ensure the confidentiality and integrity of all customer data and platform interactions.

* Strict Tenant Isolation: Our architecture guarantees that each customer's browser instances are logically and physically isolated from one another. There is no possibility of cross-tenant data access.
* Ephemeral Environments: Browsers are never reused between sessions or customers. Every session starts with a pristine, isolated browser instance that is terminated and wiped clean after use, eliminating the risk of data leakage.
* Principle of Least Privilege: Access to all systems and data is governed by the principle of least privilege. Our employees are only granted the minimum level of access necessary to perform their job functions.

#### Data Encryption

Anchor employs robust encryption protocols to protect data at every stage.

* Encryption in Transit: All data transmitted between your local machine and the Anchor Browser instance, as well as any communication with our platform services, is encrypted using industry-standard TLS 1.2 or higher. We enforce the use of strong cipher suites to protect against eavesdropping and man-in-the-middle attacks.
* Encryption at Rest: While we minimize data storage, any essential configuration data or account information stored on our platform is encrypted at rest using AES-256, one of the strongest block ciphers available.

#### Reliability, Backup, and Business Continuity

Anchor is architected for high availability and resilience to ensure uninterrupted service.

* Redundant Architecture: Our infrastructure is deployed across multiple availability zones within our cloud provider's environment. This design protects against single-point-of-failure scenarios and ensures high uptime.
* Automated Backups: We perform regular, automated backups of critical platform configuration data. These backups are encrypted and stored securely, allowing for swift recovery in the unlikely event of a major disruption.
* Disaster Recovery: We maintain a comprehensive business continuity and disaster recovery plan that is regularly tested. This plan ensures that we can restore critical operations within a defined Recovery Time Objective (RTO).

#### Return of Customer Data

Given our ephemeral architecture, there is no session data to return. Any files downloaded during a session are transferred directly to your premises. As for your account and configuration data, you can request a copy of this information at any time during your service agreement. Upon termination of your contract, all associated account data will be permanently deleted from our systems in accordance with our data retention policy.

#### Certifications

Anchor is committed to meeting and exceeding industry standards for security and compliance. We have achieved key certifications that formally validate our security controls and demonstrate our commitment to protecting customer data:

* **SOC 2 Type II**: Anchor has achieved SOC 2 Type II compliance, demonstrating our commitment to security, availability, processing integrity, confidentiality, and privacy controls.
* **ISO 27001**: We are ISO 27001 certified, meeting the international standard for information security management systems.
* **HIPAA**: Anchor is HIPAA compliant, ensuring the protection of healthcare-related data and meeting the requirements of the Health Insurance Portability and Accountability Act.
* **GDPR**: We maintain GDPR compliance, protecting the privacy and data rights of European Union residents.

For the most up-to-date information on our certification status and detailed compliance reports, please visit the [Anchor Trust Portal](https://trust.anchorbrowser.io/).

<div>
  <img alt="SOC 2 Compliance" />

  <img alt="ISO 27001 Certification" />

  <img alt="HIPAA Compliance" />

  <img alt="GDPR Compliance" />
</div>

#### Audits

Anchor engages independent, third-party auditors to conduct regular penetration tests and security assessments of our platform. These rigorous audits help us identify and remediate potential vulnerabilities, ensuring our defenses remain robust against emerging threats. A summary of our latest audit findings can be made available to customers upon request and under a Non-Disclosure Agreement (NDA).

#### Security Logs

We maintain detailed security logs to monitor for and investigate any suspicious activity.

* Audit Trails: We capture comprehensive audit logs of all administrative actions taken within the Anchor platform, such as changes to user permissions or security settings. Access to these logs is restricted to authorized personnel.
* Immutable Logging: Logs are stored in a secure, tamper-evident manner to ensure their integrity for forensic analysis and compliance purposes.

#### Personnel Practices

Our commitment to security extends to our internal team and practices.

* Security Training: We conduct mandatory security awareness training for all employees upon hiring and on an ongoing basis. This training covers data privacy, threat detection, and secure coding practices.
* Access Control: Access to our production environment is strictly controlled and limited to a small number of authorized engineers. We enforce multi-factor authentication (MFA) for all internal systems to add a critical layer of security.


# Zero Data Retention (ZDR) Mode
Source: https://docs.anchorbrowser.io/security/zdr-mode

Enhanced security mode that disables all video and log recordings to prevent sensitive data retention

Zero Data Retention (ZDR) Mode is an enhanced security feature that completely disables video recordings and log recordings for your Anchor account. This mode is designed for organizations handling highly sensitive data that require absolute assurance that no session artifacts are retained on the Anchor platform.

## What is ZDR Mode?

When ZDR Mode is enabled, Anchor disables all recording capabilities for your account, including:

* **Video recordings**: No screen recordings or visual captures of browser sessions
* **Log recordings**: No session logs or activity records

This ensures that no sensitive data from your browser sessions is retained on the Anchor platform, providing an additional layer of data protection beyond our standard ephemeral architecture.

## When to use ZDR Mode

ZDR Mode is recommended for organizations that:

* Handle highly regulated or classified information
* Require strict data residency and retention policies
* Work with sensitive customer data that must not be recorded
* Need to comply with specific industry regulations prohibiting data retention
* Operate in environments where even temporary recording poses compliance risks

## How ZDR Mode works

Once enabled, ZDR Mode:

1. Disables all video recording functionality for browser sessions
2. Prevents session logs from being captured or stored
3. Maintains all other Anchor security features, including ephemeral VMs and tenant isolation
4. Applies to all browser sessions created under your account

Note that ZDR Mode does not affect the core functionality of Anchor Browser. All browser automation, authentication, and networking capabilities remain fully operational.

## Enabling ZDR Mode

ZDR Mode is enabled manually by the Anchor team. To request ZDR Mode for your account:

1. Contact your Anchor account representative or reach out to [support@anchorbrowser.io](mailto:support@anchorbrowser.io)
2. Provide your account details and business justification for requiring ZDR Mode
3. The Anchor team will review your request and enable ZDR Mode for your account
4. You will receive confirmation once ZDR Mode has been activated

## Important considerations

* **Debugging limitations**: With ZDR Mode enabled, you will not have access to video recordings or logs for troubleshooting session issues. Ensure your application has adequate logging and monitoring in place.
* **Permanent setting**: Once enabled, ZDR Mode typically remains active for the duration of your service agreement. Contact the Anchor team if you need to modify this setting.
* **No self-service**: ZDR Mode cannot be toggled on or off by customers. All changes must be requested through the Anchor team.

## Compliance and security

ZDR Mode complements Anchor's existing security architecture, which includes:

* Ephemeral virtual machines that are destroyed after each session
* Strict tenant isolation
* Encryption in transit and at rest
* SOC 2 Type II, ISO 27001, HIPAA, and GDPR compliance

For more information about Anchor's security framework, see our [Trust & Security](/security) documentation or visit the [Anchor Trust Portal](https://trust.anchorbrowser.io/).


