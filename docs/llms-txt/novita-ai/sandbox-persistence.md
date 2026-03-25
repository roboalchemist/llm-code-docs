# Source: https://novita.ai/docs/guides/sandbox-persistence.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sandbox Persistence

export const SandboxConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the example code in this document, please ensure you have properly configured environment variables. For details, please refer to <a href="/guides/sandbox-your-first-agent-sandbox#configure-environment-variables">Configure Environment Variables</a>.</Note>;
  }
};

The sandbox persistence allows you to pause your sandbox and resume it later from the same state it was in when you paused it.

This includes not only state of the sandbox's filesystem but also the sandbox's memory. This means all running processes, loaded variables, data, etc.

<SandboxConfigHint />

<Warning>
  Please note:

  * It takes about 4 seconds per 1 GB RAM to pause the sandbox.
  * It takes about 1 second to resume the sandbox.
  * The data of a paused sandbox is retained permanently until you explicitly call the kill method to destroy it. Attempting to resume a sandbox that has been destroyed or does not exist will result in the NotFoundError in the JavaScript SDK or the NotFoundException in the Python SDK.
</Warning>

## Pausing sandbox

When you pause a sandbox, both the sandbox's <Link href="/guides/sandbox-filesystem">filesystem</Link> and memory state will be saved. This includes all the files in the sandbox's filesystem and all the running processes, loaded variables, data, etc.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()
  console.log('Sandbox created', sandbox.sandboxId)

  // Pause the sandbox.
  // You can save the sandbox ID in your database
  // to resume the sandbox later
  const result = await sandbox.betaPause()
  console.log('Sandbox paused', sandbox.sandboxId, result)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()
  print('Sandbox created', sandbox.sandbox_id)

  # You can save the sandbox ID in your database
  # to resume the sandbox later
  sandbox.beta_pause()
  print('Sandbox paused', sandbox.sandbox_id)

  sandbox.kill()
  ```
</CodeGroup>

## Resuming sandbox

When you resume a sandbox, it will be in the same state it was in when you paused it.
This means that all the files in the sandbox's filesystem will be restored and all the running processes, loaded variables, data, etc. will be restored.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()
  console.log('Sandbox created', sandbox.sandboxId)

  // Pause the sandbox.
  // You can save the sandbox ID in your database
  // to resume the sandbox later
  const result = await sandbox.betaPause()
  console.log('Sandbox paused', sandbox.sandboxId, result)

  // Resume the sandbox from the same state.
  const resumedSandbox = await sandbox.connect()
  console.log('Sandbox resumed', resumedSandbox.sandboxId)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()
  print('Sandbox created', sandbox.sandbox_id)

  # Pause the sandbox.
  # You can save the sandbox ID in your database
  # to resume the sandbox later
  sandbox.beta_pause()
  print('Sandbox paused', sandbox.sandbox_id)

  # Resume the sandbox from the same state.
  connectedSandbox = sandbox.connect()
  print('Sandbox resumed', connectedSandbox.sandbox_id)

  sandbox.kill()
  ```
</CodeGroup>

## Listing paused sandboxes

You can list all paused sandboxes by calling the `Sandbox.list` method and supplying the `state` query parameter.
More information about using the method can be found in [List Sandboxes](/guides/sandbox-list).

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox, SandboxInfo } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()

  // List all paused sandboxes.
  const paginator = Sandbox.list({ query: { state: ['paused'] } })

  // Get all paused sandboxes.
  const sandboxes: SandboxInfo[] = []
  while (paginator.hasNext) {
    const items = await paginator.nextItems()
    sandboxes.push(...items)
  }

  console.log('all paused sandboxes', sandboxes)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox, SandboxQuery, SandboxState, SandboxInfo

  sandbox = Sandbox.create()

  sandbox.beta_pause()
  print('Sandbox paused', sandbox.sandbox_id)

  # List all paused sandboxes.
  paginator = Sandbox.list(query=SandboxQuery(state=[SandboxState.PAUSED]))

  # Get all paused sandboxes.
  sandboxes: list[SandboxInfo] = []
  while paginator.has_next:
    items = paginator.next_items()
    sandboxes.extend(items)

  print('all paused sandboxes', sandboxes)

  sandbox.kill()
  ```
</CodeGroup>

## Removing paused sandboxes

You can remove paused sandboxes by calling the `kill` method on the sandbox instance.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()
  console.log('Sandbox created', sandbox.sandboxId)

  // Pause the sandbox.
  await sandbox.betaPause()

  // Kill the paused sandbox.
  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()

  # Pause the sandbox.
  sandbox.beta_pause()

  # Kill the paused sandbox.
  sandbox.kill()
  ```
</CodeGroup>

## Sandbox's timeout

When you resume a sandbox, the sandbox's timeout is reset to the default timeout of a sandbox - 5 minutes.

You can pass a custom timeout to the `Sandbox.connect()` method like this:

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()

  const connectedSandbox = await Sandbox.connect(sandbox.sandboxId, { timeoutMs: 60 * 1000 })
  console.log('Sandbox connected', connectedSandbox.sandboxId)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()

  connectedSandbox = Sandbox.connect(sandbox.sandbox_id, timeout=60) # 60 seconds
  print('Sandbox connected', connectedSandbox.sandbox_id)

  sandbox.kill()
  ```
</CodeGroup>

## Network

If you have a service (for example a server) running inside your sandbox and you pause the sandbox, the service won't be accessible from the outside and all the clients will be disconnected.
If you resume the sandbox, the service will be accessible again but you need to connect clients again.


Built with [Mintlify](https://mintlify.com).