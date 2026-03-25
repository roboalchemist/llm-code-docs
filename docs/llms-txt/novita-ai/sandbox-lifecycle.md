# Source: https://novita.ai/docs/guides/sandbox-lifecycle.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sandbox Lifecycle

export const SandboxConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the example code in this document, please ensure you have properly configured environment variables. For details, please refer to <a href="/guides/sandbox-your-first-agent-sandbox#configure-environment-variables">Configure Environment Variables</a>.</Note>;
  }
};

When you start the sandbox, it stays alive for 5 minutes by default but you can change it by passing the `timeout` parameter.
After the time passes, the sandbox will be automatically shutdown.

<SandboxConfigHint />

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  // Create sandbox with and keep it running for 60 seconds.
  const sandbox = await Sandbox.create({
    timeoutMs: 60_000, // The units are milliseconds.
  })

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  # Create sandbox with and keep it running for 60 seconds.
  sandbox = Sandbox.create(
    timeout=60, # The units are seconds.
  )

  sandbox.kill()
  ```
</CodeGroup>

## Change sandbox timeout during runtime

You can change the sandbox timeout when it's running by calling the the `setTimeout` method in JavaScript or `set_timeout` method in Python.

When you call the set timeout method, the sandbox timeout will be reset to the new value that you specified.

This can be useful if you want to extend the sandbox lifetime when it's already running.
You can for example start with a sandbox with 1 minute timeout and then periodically call set timout every time user interacts with it in your app.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  // Create sandbox with and keep it running for 60 seconds.
  const sandbox = await Sandbox.create({ timeoutMs: 60_000 })

  // Change the sandbox timeout to 30 seconds.
  // The new timeout will be 30 seconds from now.
  await sandbox.setTimeout(30_000)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  # Create sandbox with and keep it running for 60 seconds.
  sandbox = Sandbox.create(timeout=60)

  # Change the sandbox timeout to 30 seconds.
  # The new timeout will be 30 seconds from now.
  sandbox.set_timeout(30)

  sandbox.kill()
  ```
</CodeGroup>

## Retrieve sandbox information

You can retrieve sandbox information like sandbox ID, template, metadata, started at/end at date by calling the `getInfo` method in JavaScript or `get_info` method in Python.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  // Create sandbox with and keep it running for 60 seconds.
  const sandbox = await Sandbox.create({ timeoutMs: 60_000 })

  // Retrieve sandbox information.
  const info = await sandbox.getInfo()

  console.log(info)

  // Output example:
  // {
  //   sandboxId: 'i8kktl6jolbramfm8cp3k-a402f90a',
  //   templateId: '23j9hy90m6r461w7nkrn',
  //   name: 'code-interpreter-v1',
  //   metadata: {},
  //   envdVersion: '0.2.0',
  //   envdAccessToken: undefined,
  //   startedAt: 2025-06-30T06:46:36.096Z,
  //   endAt: 2025-06-30T07:16:36.096Z
  // }

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  # Create sandbox with and keep it running for 60 seconds.
  sandbox = Sandbox.create(timeout=60)

  # Retrieve sandbox information.
  info = sandbox.get_info()

  print(info)

  sandbox.kill()
  ```
</CodeGroup>

## Shutdown sandbox

You can shutdown the sandbox any time even before the timeout is up by calling the `kill` method.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  // Create sandbox with and keep it running for 60 seconds.
  const sandbox = await Sandbox.create({ timeoutMs: 60_000 })

  // Shutdown the sandbox immediately.
  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  # Create sandbox with and keep it running for 60 seconds.
  sandbox = Sandbox.create(timeout=60)

  # Shutdown the sandbox immediately.
  sandbox.kill()
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).