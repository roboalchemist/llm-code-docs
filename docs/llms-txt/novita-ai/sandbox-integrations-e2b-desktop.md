# Source: https://novita.ai/docs/guides/sandbox-integrations-e2b-desktop.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Computer use with E2B Desktop

export const SetupApiKeyGuide = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <>
                If you don't have a Novita account, you need to <Link href="https://novita.ai/user/register" target="_blank">sign up</Link> first. For details, please refer to <Link href="/guides/quickstart" target="_blank">Quick Start</Link>. After signing up, you can create an API key through the <Link href="https://novita.ai/settings/key-management" target="_blank">Key Management</Link> page and save it for subsequent steps.
            </>;
  }
};

[E2B Desktop](https://github.com/e2b-dev/desktop) is an open-source secure virtual desktop framework specifically engineered for developing Computer Use Agents. This solution provides a comprehensive, isolated desktop environment that enables AI agents to securely interact with desktop applications through controlled virtualization.

This document will provide detailed instructions on how to run this project based on Novita Agent sandbox service.

### 1. Get Novita API Key

<SetupApiKeyGuide />

### 2. Environment Configuration

Before you start using the service, you need to configure the necessary environment variables:

```bash Bash icon="terminal" highlight={1} theme={"system"}
export E2B_DOMAIN=sandbox.novita.ai
export E2B_API_KEY=<Your API key obtained in the previous step>
```

Running example:

<img src="https://mintcdn.com/novitaai/x1b8G4-Z9MJIBPJz/guides/images/sbx-e2b-desktop-env.png?fit=max&auto=format&n=x1b8G4-Z9MJIBPJz&q=85&s=7b590d78947f00f34e7e364f6f74b24f" alt="Setup Environment Variables" width="1200" data-path="guides/images/sbx-e2b-desktop-env.png" />

### 3. SDK Installation

Select the appropriate installation method corresponding to your development environment and programming language:

<CodeGroup>
  ```bash JavaScript & TypeScript icon="terminal"  theme={"system"}
  npm i @e2b/desktop@2.0.1
  ```

  ```bash Python icon="terminal" theme={"system"}
  pip install e2b-desktop==2.0.1
  ```
</CodeGroup>

### 4. Implementation Examples

#### Get Virtual Desktop Stream VNC URL

The following implementation demonstrates the instantiation of a virtual desktop environment and the retrieval of VNC access endpoints for remote desktop interaction:

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  // demo.ts implementation
  import { Sandbox } from '@e2b/desktop'

  // Initialize virtual desktop sandbox instance
  const desktop = await Sandbox.create()

  // Activate desktop streaming service
  await desktop.stream.start()

  // Retrieve interactive VNC endpoint URL
  const url = desktop.stream.getUrl()
  console.log(url)

  // Expected output format:
  // Browser-accessible URL for interactive virtual desktop session. Suitable for application integration.
  // https://6080-ik0n7lc3j0dvqd4jxy6g7.sandbox.novita.ai/vnc.html?autoconnect=true&resize=scale

  // Retrieve read-only VNC endpoint URL (interaction disabled)
  const urlDisabledInteraction = desktop.stream.getUrl({ viewOnly: true })
  console.log(urlDisabledInteraction)
  // Expected output format:
  // Browser-accessible URL for view-only virtual desktop session (non-interactive mode). Suitable for monitoring applications.
  // https://6080-ik0n7lc3j0dvqd4jxy6g7.sandbox.novita.ai/vnc.html?autoconnect=true&view_only=true&resize=scale

  // Keep the program running
  console.log("Desktop stream started, press Ctrl+C to stop the program...")
  const interval = setInterval(() => {}, 1000)

  // Register interrupt signal handlers for resource cleanup
  let isCleaning = false
  const cleanup = async () => {
      if (isCleaning) return
      isCleaning = true
      
      console.log("\nProgram interrupted, cleaning up resources...")
      clearInterval(interval)
      try {
          await desktop.stream.stop() // Terminate streaming service
          await desktop.kill()        // Deallocate sandbox instance
      } catch (err) {
          console.error("Error cleaning up resources:", err)
      }
      process.exit(0)
  }

  process.on('SIGINT', cleanup)
  process.on('SIGTERM', cleanup)
  ```

  ```python Python icon="python" theme={"system"}
  # demo.py implementation
  from e2b_desktop import Sandbox

  # Initialize virtual desktop sandbox instance
  desktop = Sandbox.create()

  # Activate desktop streaming service
  desktop.stream.start()

  # Retrieve interactive VNC endpoint URL
  url = desktop.stream.get_url()
  print(url)
  # Expected output format:
  # Browser-accessible URL for interactive virtual desktop session. Suitable for application integration.
  # https://6080-ik0n7lc3j0dvqd4jxy6g7.sandbox.novita.ai/vnc.html?autoconnect=true&resize=scale

  # Retrieve read-only VNC endpoint URL (interaction disabled)
  url_readonly = desktop.stream.get_url(view_only=True)
  print(url_readonly)
  # Expected output format:
  # Browser-accessible URL for view-only virtual desktop session (non-interactive mode). Suitable for monitoring applications.
  # https://6080-ik0n7lc3j0dvqd4jxy6g7.sandbox.novita.ai/vnc.html?autoconnect=true&view_only=true&resize=scale

  # Implement keyboard interrupt handling for graceful shutdown
  try:
      print("Desktop stream started, press Ctrl+C to stop the program...")
      import time
      while True:
          time.sleep(0.1)
  except KeyboardInterrupt:
      print("\nProgram interrupted, cleaning up resources...")

  # Execute resource deallocation procedures
  desktop.stream.stop()  # Terminate streaming service
  desktop.kill()        # Deallocate sandbox instance
  ```
</CodeGroup>

Running example:

<img src="https://mintcdn.com/novitaai/x1b8G4-Z9MJIBPJz/guides/images/sbx-e2b-desktop-run-tsx.png?fit=max&auto=format&n=x1b8G4-Z9MJIBPJz&q=85&s=f8cdcc27d9edc87ce0013b0f15c6b876" alt="Run Example" width="1200" data-path="guides/images/sbx-e2b-desktop-run-tsx.png" />

Access virtual desktop stream VNC URL:

<img src="https://mintcdn.com/novitaai/x1b8G4-Z9MJIBPJz/guides/images/sbx-e2b-desktop-streaming.png?fit=max&auto=format&n=x1b8G4-Z9MJIBPJz&q=85&s=ae0782153ef8dd90e1225216f31a1bef" alt="Desktop Streaming" width="1200" data-path="guides/images/sbx-e2b-desktop-streaming.png" />

Additional implementation examples and advanced use cases are available in the <Link href="https://github.com/e2b-dev/desktop/tree/main/examples" target="_blank">official E2B Desktop repository</Link>.


Built with [Mintlify](https://mintlify.com).