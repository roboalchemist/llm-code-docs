# Source: https://novita.ai/docs/guides/sandbox-commands.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Running commands in sandbox

export const SandboxConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the example code in this document, please ensure you have properly configured environment variables. For details, please refer to <a href="/guides/sandbox-your-first-agent-sandbox#configure-environment-variables">Configure Environment Variables</a>.</Note>;
  }
};

<SandboxConfigHint />

You can run terminal commands inside the sandbox using the `commands.run()` method.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()

  const result = await sandbox.commands.run('ls -l')
  console.log(result)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()

  result = sandbox.commands.run('ls -l')
  print(result)

  sandbox.kill()
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).