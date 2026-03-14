# Source: https://novita.ai/docs/guides/sandbox-commands-streaming.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Streaming command output

export const SandboxConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the example code in this document, please ensure you have properly configured environment variables. For details, please refer to <a href="/guides/sandbox-your-first-agent-sandbox#configure-environment-variables">Configure Environment Variables</a>.</Note>;
  }
};

<SandboxConfigHint />

To stream command output as it is being executed, pass the `onStdout`, `onStderr` callbacks to the `commands.run()` method in JavaScript
or the `on_stdout`, `on_stderr` callbacks to the `commands.run()` method in Python.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()
  const result = await sandbox.commands.run('echo hello; sleep 1; echo world', {
    onStdout: (data) => {
      console.log(data)
    },
    onStderr: (data) => {
      console.log(data)
    },
  })

  console.log(result)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()

  result = sandbox.commands.run('echo hello; sleep 1; echo world',
                                on_stdout=lambda data: print(data),
                                on_stderr=lambda data: print(data))

  print(result)

  sandbox.kill()
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).