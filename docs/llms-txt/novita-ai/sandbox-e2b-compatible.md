# Source: https://novita.ai/docs/guides/sandbox-e2b-compatible.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# E2B SDK Compatibility

Novita Agent Sandbox provides a compatibility API that allows you to use the E2B SDK and CLI. This is useful if you are already using the E2B SDK and CLI and want to switch to Novita Agent Sandbox. However, we recommend using the Novita [Agent Sandbox SDK](/guides/sandbox-sdk-and-cli) to access all features.

## Installation

### Code Interpreter SDK

<CodeGroup>
  ```bash JavaScript & TypeScript icon="terminal" theme={"system"}
  npm i @e2b/code-interpreter@beta
  ```

  ```bash Python icon="terminal" theme={"system"}
  pip install e2b-code-interpreter==1.2.0b5
  ```
</CodeGroup>

### Core SDK

<CodeGroup>
  ```bash JavaScript & TypeScript icon="terminal" theme={"system"}
  npm i e2b@beta
  ```

  ```bash Python icon="terminal" theme={"system"}
  pip install e2b==1.2.0b6
  ```
</CodeGroup>

### Desktop SDK

<CodeGroup>
  ```bash JavaScript & TypeScript icon="terminal" theme={"system"}
  npm i @e2b/desktop@beta
  ```

  ```bash Python icon="terminal" theme={"system"}
  pip install e2b-desktop==1.7.1b1
  ```
</CodeGroup>

### CLI

<CodeGroup>
  ```bash Bash icon="terminal" theme={"system"}
  npm i -g @e2b/cli@v1.9.2
  ```
</CodeGroup>

## Setup Configuration

You need to set the following environment variables in your project to use the E2B SDK and CLI with Novita Agent Sandbox.

```bash Bash icon="terminal" theme={"system"}
export E2B_DOMAIN=sandbox.novita.ai
export E2B_API_KEY="<Your Novita AI API Key>"
```

## Examples

Below is an example showing how to create a sandbox through the SDK and run specified commands using E2B SDK.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from '@e2b/code-interpreter'
  // or import { Sandbox } from 'e2b'
  // or import { Sandbox } from '@e2b/desktop'

  const sbx = await Sandbox.create()
  const execution = await sbx.commands.run('ls -l')
  console.log(execution)

  await sbx.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from e2b_code_interpreter import Sandbox
  # or from e2b import Sandbox
  # or from e2b_desktop import Sandbox

  sbx = Sandbox.create()
  execution = sbx.commands.run('ls -l')
  print(execution)

  sbx.kill()
  ```
</CodeGroup>

Below is an example showing how to use the E2B CLI with Novita Agent Sandbox.

<CodeGroup>
  ```bash Bash icon="terminal" theme={"system"}
  export E2B_DOMAIN=sandbox.novita.ai
  # Authentication in CLI
  e2b auth login

  # Start sandbox and connect to terminal
  e2b sandbox spawn <template-id>

  # List sandboxes
  e2b sandbox list

  # Shutdown running sandboxes
  e2b sandbox kill <sandbox-id>
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).