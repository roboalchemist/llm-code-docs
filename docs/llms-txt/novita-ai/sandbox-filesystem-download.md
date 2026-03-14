# Source: https://novita.ai/docs/guides/sandbox-filesystem-download.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Download data from sandbox

export const SandboxConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the example code in this document, please ensure you have properly configured environment variables. For details, please refer to <a href="/guides/sandbox-your-first-agent-sandbox#configure-environment-variables">Configure Environment Variables</a>.</Note>;
  }
};

You can download data from the sandbox using the `files.read()` method.

<SandboxConfigHint />

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import fs from 'fs'
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()

  // Create a file in the sandbox for testing
  const filePathInSandbox = '/tmp/test-file'
  await sandbox.files.write(filePathInSandbox, "test-file-content")

  // Read file from sandbox
  const content = await sandbox.files.read(filePathInSandbox)

  // Write file to local filesystem
  const localFilePath = './local-test-file'
  fs.writeFileSync(localFilePath, content)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()

  # Create a file in the sandbox for testing
  file_path_in_sandbox = '/tmp/test-file'
  sandbox.files.write(file_path_in_sandbox, "test-file-content")

  # Read file from sandbox
  content = sandbox.files.read(file_path_in_sandbox)

  # Write file to local filesystem
  local_file_path = './local-test-file'
  with open(local_file_path, 'w') as file:
    file.write(content)

  sandbox.kill()
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).