# Source: https://novita.ai/docs/guides/sandbox-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List sandboxes

export const SandboxConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the example code in this document, please ensure you have properly configured environment variables. For details, please refer to <a href="/guides/sandbox-your-first-agent-sandbox#configure-environment-variables">Configure Environment Variables</a>.</Note>;
  }
};

You can list sandboxes using the `Sandbox.list()` method.

<SandboxConfigHint />

<Note>
  Once you have information about running sandbox, you can [connect](/guides/sandbox-connect) to it using the `Sandbox.connect()` method.
</Note>

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  // Create a sandbox.
  const sandbox = await Sandbox.create({
    metadata: {
      name: 'My Sandbox',
    },
  })

  // List all running sandboxes.
  const runningSandboxesPaginator = await Sandbox.list({
    query: {
      state: ["running"],
    },
  })

  const runningSandboxes = await runningSandboxesPaginator.nextItems()
  const runningSandbox = runningSandboxes[0]

  console.log('Running sandbox metadata:', runningSandbox.metadata)
  console.log('Running sandbox id:', runningSandbox.sandboxId)
  console.log('Running sandbox started at:', runningSandbox.startedAt)
  console.log('Running sandbox template id:', runningSandbox.templateId)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox, SandboxQuery, SandboxState

  sandbox = Sandbox.create(
    metadata= {
      'name': 'My Sandbox',
    },
  )

  # List all running sandboxes.
  running_sandboxes_paginator = Sandbox.list(
    query=SandboxQuery(
      state=[SandboxState.RUNNING],
    ),
  )

  running_sandboxes = running_sandboxes_paginator.next_items()

  running_sandbox = running_sandboxes[0]
  print('Running sandbox metadata:', running_sandbox.metadata)
  print('Running sandbox id:', running_sandbox.sandbox_id)
  print('Running sandbox started at:', running_sandbox.started_at)
  print('Running sandbox template id:', running_sandbox.template_id)

  sandbox.kill()
  ```
</CodeGroup>

## Filtering sandboxes

You can filter sandboxes by specifying <Link href="/guides/sandbox-metadata">Metadata</Link> key value pairs.
Specifying multiple key value pairs will return sandboxes that match all of them.

This can be useful when you have a large number of sandboxes and want to find only specific ones. The filtering is performed on the server.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  // Create a sandbox with metadata.
  const sandbox = await Sandbox.create({
    metadata: {
      env: 'dev',
      app: 'my-app',
      userId: '123',
    },
  })

  // List all running sandboxes that has `userId` key with value `123` and `env` key with value `dev`.
  const runningSandboxesPaginator = await Sandbox.list({
    query: {
      metadata: { userId: '123', env: 'dev' },
    },
  })

  const runningSandboxes = await runningSandboxesPaginator.nextItems()
  for (const runningSandbox of runningSandboxes) {
    console.log(`list running sandbox (${runningSandbox.sandboxId}) metadata:`, runningSandbox.metadata)
  }

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox, SandboxQuery

  # Create sandbox with metadata.
  sandbox = Sandbox.create(
      metadata={
          "env": "dev",
          "app": "my-app",
          "user_id": "123",
      },
  )

  # List all running sandboxes that has `user_id` key with value `123` and `env` key with value `dev`.
  paginator = Sandbox.list(
      query=SandboxQuery(
          metadata={
              "user_id": "123",
              "env": "dev",
          }
      ),
  )

  sandbox.kill()
  ```
</CodeGroup>

### Listing sandboxes

The `Sandbox.list()` method now supports pagination. In the [advanced pagination](#advanced-pagination) section, you can find more information about pagination techniques using the updated method.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js"  theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()

  const paginator = Sandbox.list()

  // Get the first page of sandboxes (running and paused)
  const firstPage = await paginator.nextItems()
  if (paginator.hasNext) {
      // Get the next page of sandboxes
      const nextPage = await paginator.nextItems()
  }

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()

  # List all sandboxes (running and paused)
  paginator = Sandbox.list()

  firstPage = paginator.next_items()
  if paginator.has_next:
      nextPage = paginator.next_items()

  sandbox.kill()
  ```
</CodeGroup>

### Filtering sandboxes

Filter sandboxes by their current state. The state parameter can contain either "**running**" for running sandboxes or "**paused**" for paused sandboxes, or both.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()

  // List all sandboxes that are running or paused.
  const paginator = Sandbox.list({
    query: {
      state: ['running', 'paused'],
    },
  })

  const sandboxes = await paginator.nextItems()

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox, SandboxQuery, SandboxState

  sandbox = Sandbox.create()

  # List all sandboxes that are running or paused.
  paginator = Sandbox.list(
      query=SandboxQuery(
          state=[SandboxState.RUNNING, SandboxState.PAUSED],
      ),
  )

  # Get the first page of sandboxes (running and paused)
  sandboxes = paginator.next_items()

  sandbox.kill()
  ```
</CodeGroup>

Filter sandboxes by the metadata key value pairs specified during Sandbox creation.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  // Create sandbox with metadata.
  const sandbox = await Sandbox.create({
    metadata: {
      env: 'dev',
      app: 'my-app',
      userId: '123',
    },
  })

  // List all sandboxes that has `userId` key with value `123` and `env` key with value `dev`.
  const paginator = Sandbox.list({
    query: {
      metadata: { userId: '123', env: 'dev' },
    },
  })

  const sandboxes = await paginator.nextItems()

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox, SandboxQuery

  # Create sandbox with metadata.
  sandbox = Sandbox.create(
      metadata={
          "env": "dev",
          "app": "my-app",
          "user_id": "123",
      },
  )

  # List all sandboxes that has `userId` key with value `123` and `env` key with value `dev`.
  paginator = Sandbox.list(
      query=SandboxQuery(
          metadata={
              "user_id": "123",
              "env": "dev",
          }
      ),
  )

  sandboxes = paginator.next_items()

  sandbox.kill()
  ```
</CodeGroup>

### Advanced pagination

For more granular pagination, you can set custom per-page item limit (default and maximum is **1000**) and specify an offset parameter (`nextToken` or `next_token`) to start paginating from.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()

  const paginator = Sandbox.list({
    limit: 1000,
    // nextToken: '<base64-encoded-token>',
  })

  // Fetch the next page
  await paginator.nextItems()

  // Additional paginator properties
  // Whether there is a next page
  console.log("paginator.hasNext: ", paginator.hasNext)

  // Next page token
  console.log("paginator.nextToken: ", paginator.nextToken)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()

  paginator = Sandbox.list(
      limit=1000,
      # next_token='<base64-encoded-token>',
  )

  # Fetch the next page
  paginator.next_items()

  # Whether there is a next page
  print("paginator.has_next: ", paginator.has_next)

  # Next page offset parameter
  print("paginator.next_token: ", paginator.next_token)

  sandbox.kill()
  ```
</CodeGroup>

You can fetch all pages by looping through the paginator while checking if there is a next page (using `hasNext` or `has_next` property) and fetching until there are no more pages left to fetch:

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox, SandboxInfo } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()

  const paginator = Sandbox.list()

  const sandboxes: SandboxInfo[] = []
  while (paginator.hasNext) {
    const items = await paginator.nextItems()
    sandboxes.push(...items)
  }

  for (const sandbox of sandboxes) {
    console.log(`list sandbox (${sandbox.sandboxId})`)
  }

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox, SandboxInfo

  sandbox = Sandbox.create()

  paginator = Sandbox.list()

  # Get all sandboxes
  sandboxes: list[SandboxInfo] = []
  while paginator.has_next:
      items = paginator.next_items()
      sandboxes.extend(items)

  sandbox.kill()
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).