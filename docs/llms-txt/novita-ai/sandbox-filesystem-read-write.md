# Source: https://novita.ai/docs/guides/sandbox-filesystem-read-write.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Read & write files

export const SandboxConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the example code in this document, please ensure you have properly configured environment variables. For details, please refer to <a href="/guides/sandbox-your-first-agent-sandbox#configure-environment-variables">Configure Environment Variables</a>.</Note>;
  }
};

<SandboxConfigHint />

## Reading files

You can read files from the sandbox filesystem using the `files.read()` method.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()

  // Create a file in the sandbox for testing
  const filePathInSandbox = '/tmp/test-file'
  await sandbox.files.write(filePathInSandbox, "test-file-content")

  const fileContent = await sandbox.files.read(filePathInSandbox)
  console.log(fileContent)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()

  file_path_in_sandbox = '/tmp/test-file'
  sandbox.files.write(file_path_in_sandbox, "test-file-content")

  file_content = sandbox.files.read(file_path_in_sandbox)
  print(file_content)

  sandbox.kill()
  ```
</CodeGroup>

## Writing single files

You can write single files to the sandbox filesystem using the `files.write()` method.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()

  const filePathInSandbox = '/tmp/test-file'

  const result = await sandbox.files.write(filePathInSandbox, "test-file-content")
  console.log(result)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()

  file_path_in_sandbox = '/tmp/test-file'
  result = sandbox.files.write(file_path_in_sandbox, "test-file-content")
  print(result)

  sandbox.kill()
  ```
</CodeGroup>

## Writing multiple files

You can also write multiple files to the sandbox filesystem using the `files.write()` method.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()

  const result = await sandbox.files.write([
      { path: '/tmp/test-file-1', data: 'file content 1' },
      { path: '/tmp/test-file-2', data: 'file content 2' }
  ])

  console.log(result)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()

  result = sandbox.files.write_files([
      { "path": "/tmp/test-file-1", "data": "file content 1" },
      { "path": "/tmp/test-file-2", "data": "file content 2" }
  ])
  print(result)

  sandbox.kill()
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).