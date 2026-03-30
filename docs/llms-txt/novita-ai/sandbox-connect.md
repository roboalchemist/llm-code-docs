# Source: https://novita.ai/docs/guides/sandbox-connect.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to running sandbox

export const SandboxConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the example code in this document, please ensure you have properly configured environment variables. For details, please refer to <a href="/guides/sandbox-your-first-agent-sandbox#configure-environment-variables">Configure Environment Variables</a>.</Note>;
  }
};

If you have a running sandbox, you can connect to it using the `Sandbox.connect()` method and then start controlling it with our SDK.

This is useful if you want to, for example, reuse the same sandbox instance for the same user after a short period of inactivity.

<SandboxConfigHint />

## 1. Get the sandbox ID

To connect to a running sandbox, you first need to retrieve its ID. You can do this by calling the `Sandbox.list()` method.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from "novita-sandbox/code-interpreter"

  // Get all running sandboxes
  const runningSandboxesPaginator = await Sandbox.list({
    query: {
      state: ["running"],
    },
  })

  const runningSandboxes = await runningSandboxesPaginator.nextItems()
  if (runningSandboxes.length === 0) {
    throw new Error("No running sandboxes found")
  }
  const runningSandboxId = runningSandboxes[0].sandboxId

  console.log(`got a running sandbox: ${runningSandboxId}`)
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox, SandboxQuery, SandboxState

  sandbox = Sandbox.create()

  # Get all running sandboxes
  running_sandboxes_paginator = Sandbox.list(query=SandboxQuery(state=[SandboxState.RUNNING]))

  running_sandboxes = running_sandboxes_paginator.next_items()
  if len(running_sandboxes) == 0:
    raise Exception("No running sandboxes found")
  running_sandbox_id = running_sandboxes[0].sandbox_id

  # got a running sandbox.
  print("got a running sandbox: ", running_sandbox_id)

  sandbox.kill()
  ```
</CodeGroup>

## 2. Connect to the sandbox

Now that you have the sandbox ID, you can connect to the sandbox using the `Sandbox.connect()` method.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from "novita-sandbox/code-interpreter"

  // Get all running sandboxes
  const runningSandboxesPaginator = await Sandbox.list({
    query: {
      state: ["running"],
    },
  })

  const runningSandboxes = await runningSandboxesPaginator.nextItems()
  if (runningSandboxes.length === 0) {
    throw new Error("No running sandboxes found")
  }
  const runningSandboxId = runningSandboxes[0].sandboxId

  // connect to the sandbox.
  const sandbox = await Sandbox.connect(runningSandboxId)
  console.log("connected to sandbox: ", sandbox.sandboxId)

  // Now you can use the sandbox as usual
  // ...
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox, SandboxQuery, SandboxState

  sandbox = Sandbox.create()

  # Get all running sandboxes.
  running_sandboxes_paginator = Sandbox.list(query=SandboxQuery(state=[SandboxState.RUNNING]))

  running_sandboxes = running_sandboxes_paginator.next_items()
  if len(running_sandboxes) == 0:
    raise Exception("No running sandboxes found")
  running_sandbox_id = running_sandboxes[0].sandbox_id

  # connect to the sandbox.
  sandbox = Sandbox.connect(running_sandbox_id)
  print("got a running sandbox: ", sandbox.sandbox_id)

  # Now you can use the sandbox as usual
  # ...

  sandbox.kill()
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).