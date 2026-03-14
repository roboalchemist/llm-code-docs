# Source: https://novita.ai/docs/guides/sandbox-filesystem-watch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Watch sandbox directory for changes

export const SandboxConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the example code in this document, please ensure you have properly configured environment variables. For details, please refer to <a href="/guides/sandbox-your-first-agent-sandbox#configure-environment-variables">Configure Environment Variables</a>.</Note>;
  }
};

You can watch a directory for changes using the `files.watchDir()` method in JavaScript and `files.watch_dir()` method in Python.

<Note>
  Since events are tracked asynchronously, their delivery may be delayed.
  It's recommended not to collect or close watcher immediately after making a change.
</Note>

<SandboxConfigHint />

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox, FilesystemEventType } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()
  const dirname = '/tmp'

  // Start watching directory for changes
  const handle = await sandbox.files.watchDir(dirname, async (event) => {
    console.log(`got event: ${event.type} - ${event.name}`)
    if (event.type === FilesystemEventType.WRITE) {
      console.log(`wrote to file ${event.name}`)
    }
  })

  // Trigger file write event
  await sandbox.files.write(`${dirname}/test-file`, 'test-file-content')

  // Stop watching directory for changes
  handle.stop()

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox, FilesystemEventType

  sandbox = Sandbox.create()
  dirname = '/tmp'

  # Watch directory for changes
  handle = sandbox.files.watch_dir(dirname)
  # Trigger file write event
  sandbox.files.write(f"{dirname}/test-file", "test-file-content")

  # Retrieve the latest new events since the last `get_new_events()` call
  events = handle.get_new_events()
  for event in events:
    print(f"got event: {event.type} - {event.name}")
    if event.type == FilesystemEventType.WRITE:
      print(f"wrote to file {event.name}")

  # Stop watching directory for changes
  handle.stop()

  sandbox.kill()
  ```
</CodeGroup>

## Recursive Watching

You can enable recursive watching using the parameter `recursive`.

<Note>
  When rapidly creating new folders (e.g., deeply nested path of folders), events other than `CREATE` might not be emitted. To avoid this behavior, create the required folder structure in advance.
</Note>

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox, FilesystemEventType } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()
  const dirname = '/tmp'

  // Start watching directory for changes
  const handle = await sandbox.files.watchDir(dirname, async (event) => {
    console.log(`got event: ${event.type} - ${event.name}`)
    if (event.type === FilesystemEventType.WRITE) {
      console.log(`wrote to file ${event.name}`)
    }
  }, {
    recursive: true
  })

  // Trigger file write event
  await sandbox.files.write(`${dirname}/test-folder/test-file`, 'test-file-content')

  // Stop watching directory for changes
  handle.stop()

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox, FilesystemEventType

  sandbox = Sandbox.create()
  dirname = '/tmp'

  # Watch directory for changes
  handle = sandbox.files.watch_dir(dirname, recursive=True)
  # Trigger file write event
  sandbox.files.write(f"{dirname}/test-folder/test-file", "test-file-content")

  # Retrieve the latest new events since the last `get_new_events()` call
  events = handle.get_new_events()
  for event in events:
    print(f"got event: {event.type} - {event.name}")
    if event.type == FilesystemEventType.WRITE:
      print(f"wrote to file {event.name}")

  # Stop watching directory for changes
  handle.stop()

  sandbox.kill()
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).