# Source: https://novita.ai/docs/guides/sandbox-commands-background.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Running commands in background

export const SandboxConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the example code in this document, please ensure you have properly configured environment variables. For details, please refer to <a href="/guides/sandbox-your-first-agent-sandbox#configure-environment-variables">Configure Environment Variables</a>.</Note>;
  }
};

<SandboxConfigHint />

To run commands in background, pass the `background` option to the `commands.run()` method. This will return immediately and the command will continue to run in the sandbox.
You can then later kill the command using the `commands.kill()` method.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()

  // Start the command in the background
  const command = await sandbox.commands.run('echo hello; sleep 10; echo world', {
    background: true,
    onStdout: (data) => {
      console.log(data)
    },
  })

  // Kill the command
  await command.kill()

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()

  # Start the command in the background
  command = sandbox.commands.run('echo hello; sleep 10; echo world', background=True)

  # Get stdout and stderr from the command running in the background.
  # You can run this code in a separate thread or use command.wait() to wait for the command to finish.
  for stdout, stderr, _ in command:
      if stdout:
          print(stdout)
      if stderr:
          print(stderr)

  # Kill the command
  command.kill()

  sandbox.kill()
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).