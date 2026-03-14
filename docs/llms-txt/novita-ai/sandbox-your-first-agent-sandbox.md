# Source: https://novita.ai/docs/guides/sandbox-your-first-agent-sandbox.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Your First Agent Sandbox

## Create an Account

If you don't have a Novita account, you need to <Link href="https://novita.ai/user/register" target="_blank">sign up</Link> first. For details, please refer to <Link href="/guides/quickstart">Quickstart guide</Link>.

## Create API Key

Go to the Novita <Link href="https://novita.ai/settings/key-management" target="_blank">Key Management page</Link>, you can create an API key and save the API key value for use in subsequent steps.

## Install SDK

You can install the SDK by executing the following commands.

<CodeGroup isTerminalCommand>
  ```bash JavaScript & TypeScript SDK icon="terminal" theme={"system"}
  npm i novita-sandbox
  ```

  ```bash Python SDK icon="terminal" theme={"system"}
  pip install novita-sandbox
  ```
</CodeGroup>

## Configure Environment Variables

Create a `.env` file in your project folder (if it doesn't exist), and configure the API key and API domain address.

<Warning>
  For JavaScript and TypeScript projects, you need to import the `dotenv/config` package in your project; for Python projects, you need to import the `dotenv` library in your project and call the `load_dotenv` method to load environment variables.
  For details, please refer to the [example](#use-sdk-to-start-agent-sandbox).
</Warning>

```bash .env icon="terminal" highlight={2} theme={"system"}
NOVITA_API_KEY=sk_*** # Novita API key obtained from previous steps
```

Or you can configure the API key and API domain address by setting environment variables in your terminal.

```bash Bash icon="terminal" highlight={2} theme={"system"}
export NOVITA_API_KEY=sk_*** # Novita API key obtained from previous steps
```

## Use SDK to Start Agent Sandbox

Below is a simple example showing how to create a sandbox through the SDK and run specified commands.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  // index.ts
  import 'dotenv/config'
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  // The .env file should be located in the project root directory
  // dotenv/config will automatically look for .env in the current working directory
  // Or 
  // You can set the environment variable in the command line
  // export NOVITA_API_KEY=sk_***

  const sandbox = await Sandbox.create()
  const execution = await sandbox.runCode('print("hello world")')
  console.log(execution.logs)

  const files = await sandbox.files.list('/tmp')
  console.log(files)

  // Close sandbox when no longer needed
  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  # main.py
  from dotenv import load_dotenv
  from novita_sandbox.code_interpreter import Sandbox


  # The .env file should be located in the project root directory
  # dotenv will automatically look for .env in the current working directory
  load_dotenv()

  # Or 
  # You can set the environment variable in the command line
  # export NOVITA_API_KEY=sk_***

  sandbox = Sandbox.create()
  execution = sandbox.run_code("print('hello world')")
  print(execution.logs)

  files = sandbox.files.list("/")
  print(files)

  # Close sandbox when no longer needed
  sandbox.kill()
  ```
</CodeGroup>

Execute the following commands to run the above code.

<CodeGroup isTerminalCommand>
  ```bash index.ts icon="terminal" theme={"system"}
  npx tsx ./index.ts
  ```

  ```bash main.py icon="terminal" theme={"system"}
  python main.py
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).