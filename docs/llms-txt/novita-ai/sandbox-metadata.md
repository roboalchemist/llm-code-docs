# Source: https://novita.ai/docs/guides/sandbox-metadata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sandbox Metadata

Metadata is a way to attach arbitrary key-value pairs for a sandbox.

This is useful in various scenarios, for example:

* Associate a sandbox with a user session.
* Store custom user data for a sandbox like API keys.
* Associate a sandbox with a user ID and [connect to it later](/guides/sandbox-connect).

You specify metadata when creating a sandbox and can access it later through listing running sandboxes with `Sandbox.list()` method.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  // Create sandbox with metadata.
  const sandbox = await Sandbox.create({
    metadata: {
      userId: '123',
    },
  })

  // List running sandboxes and access metadata.
  const runningSandboxesPaginator = await Sandbox.list({
    query: {
      state: ["running"],
    },
  })

  const runningSandboxes = await runningSandboxesPaginator.nextItems()

  console.log("runningSandboxes[0].metadata: ", runningSandboxes[0].metadata)

  // Example output:
  // { userId: '123' }

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox, SandboxQuery, SandboxState

  # Create sandbox with metadata.
  sandbox = Sandbox.create(
    metadata={
      'userId': '123',
    },
  )

  # List running sandboxes and access metadata.
  running_sandboxes_paginator = Sandbox.list(
    query=SandboxQuery(
      state=[SandboxState.RUNNING],
    ),
  )
  running_sandboxes = running_sandboxes_paginator.next_items()

  print(running_sandboxes[0].metadata)

  # Example output:
  # { userId: '123' }

  sandbox.kill()
  ```
</CodeGroup>

## Filtering sandboxes by metadata

You can also filter sandboxes by metadata, you can find more about it [here](/guides/sandbox-list#filtering-sandboxes).


Built with [Mintlify](https://mintlify.com).