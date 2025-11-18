# Source: https://docs.anchorbrowser.io/agentic-browser-control/agentic-file-usage.md

# Agentic File Usage

> Upload ZIP files to browser sessions for AI agents to use

<Warning>
  **Compatibility Note**: Only works with the `browser-use` agent framework. Not supported with OpenAI CUA.
</Warning>

## Quick Start

Upload a ZIP file containing resources that your AI agent can use to complete tasks. The ZIP file is automatically extracted and made available to the agent.

## Example: Upload ZIP File

<CodeGroup>
  ```javascript node.js theme={null}
  const AnchorClient = require('anchorbrowser');
  const { chromium } = require('playwright');
  const JSZip = require('jszip');

  const ANCHOR_API_KEY = process.env.ANCHOR_API_KEY;

  (async () => {
    // Initialize Anchor client
    const anchorClient = new AnchorClient({
      apiKey: ANCHOR_API_KEY,
    });

    // Create a new session
    const session = await anchorClient.sessions.create();
    console.log('session live view url:', session.data.live_view_url);
    const sessionId = session.data.id;
    const cdp_url = session.data.cdp_url;

    // 1. Create a test ZIP file with content
    const zip = new JSZip();
    zip.file('test.txt', 'Hello from Anchor!\nThis is a test file for the agent.');
    const zipBlob = await zip.generateAsync({ type: 'blob' });
    
    const formData = new FormData();
    formData.append('file', zipBlob, 'test-data.zip');

    // 2. Upload to browser session
    const result = await anchorClient.sessions.agent.files.upload(sessionId, {
      file: zipBlob
    });
    console.log('Upload result:', result);

    // 3. Connect to the browser session and use uploaded files with AI agent
    const browser = await chromium.connectOverCDP(cdp_url);
    const context = browser.contexts()[0];
    const page = context.pages()[0];

    // Navigate to a website where you want to use the uploaded files
    await page.goto('https://v0-download-and-upload-text.vercel.app/');

    // Use AI agent to interact with the page using uploaded files
    const ai = context.serviceWorkers()[0];
    const aiResult = await ai.evaluate("upload a file to the server");
    console.log('AI agent result:', aiResult);
    
    // Close browser to end the script
    await browser.close();
  })();
  ```

  ```python python theme={null}
  import os
  import zipfile
  import tempfile
  import requests
  from anchorbrowser import Anchorbrowser

  ANCHOR_API_KEY = os.getenv("ANCHOR_API_KEY")

  # Initialize Anchor client
  anchor_client = Anchorbrowser(api_key=ANCHOR_API_KEY)

  # Create a new session
  session = anchor_client.sessions.create()
  print('session live view url:', session.data.live_view_url)
  session_id = session.data.id
  cdp_url = session.data.cdp_url

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

  # 3. Navigate to a website where you want to use the uploaded files
  anchor_client.sessions.goto(session_id=session_id, url="https://v0-download-and-upload-text.vercel.app/")

  # 4. Connect to the browser session and use uploaded files with AI agent
  ai_result = anchor_client.tools.perform_web_task(
      prompt="upload test.txt to the server", 
      # prompt="list me all files you have access to", 
      session_id=session_id,
  )
  print('AI agent result:', ai_result)
  ```
</CodeGroup>

That's it! The agent can now access all uploaded files and use them to complete web tasks.
