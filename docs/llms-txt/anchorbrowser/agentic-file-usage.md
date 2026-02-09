# Source: https://docs.anchorbrowser.io/agentic-browser-control/agentic-file-usage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Agentic File Usage

> Upload ZIP files to browser sessions for AI agents to use

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
