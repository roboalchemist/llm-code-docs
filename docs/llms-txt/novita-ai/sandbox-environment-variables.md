# Source: https://novita.ai/docs/guides/sandbox-environment-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Environment variables

export const SandboxConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the example code in this document, please ensure you have properly configured environment variables. For details, please refer to <a href="/guides/sandbox-your-first-agent-sandbox#configure-environment-variables">Configure Environment Variables</a>.</Note>;
  }
};

This page covers how to set and use environment variables in a sandbox, and default environment variables inside the sandbox.

<SandboxConfigHint />

## Setting environment variables

There are 3 ways to set environment variables in a sandbox:

* [Global environment variables when creating the sandbox](#1-global-environment-variables).
* [When running code in the sandbox](#2-setting-environment-variables-when-running-code).
* [When running commands in the sandbox](#3-setting-environment-variables-when-running-commands).

### 1. Global environment variables

You can set global environment variables when creating a sandbox.

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create({
    envs: {
      MY_VAR: 'my_value',
    },
  })

  const result = await sandbox.commands.run("echo $MY_VAR")

  console.log(result)

  // Output example:
  // { exitCode: 0, error: undefined, stdout: 'my_value\n', stderr: '' }

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create(
    envs={
      'MY_VAR': 'my_value',
    },
  )

  result = sandbox.commands.run("echo $MY_VAR")

  print(result)

  # Output example:
  # { exitCode: 0, error: undefined, stdout: '123\n', stderr: '' }

  sandbox.kill()
  ```
</CodeGroup>

### 2. Setting environment variables when running code

You can set environment variables for specific code execution call in the sandbox.

<Note>
  If you had a global environment variable with the same name, it will be overridden.
</Note>

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()

  const result = await sandbox.runCode('import os; print(os.environ.get("MY_VAR"))', {
    envs: {
      MY_VAR: 'my_value',
    },
  })
  console.log(result.logs)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()
  result = sandbox.run_code(
      'import os; print(os.environ.get("MY_VAR"))',
      envs={
          'MY_VAR': 'my_value'
      }
  )

  print(result)

  sandbox.kill()
  ```
</CodeGroup>

### 3. Setting environment variables when running commands

You can set environment variables for specific command execution in the sandbox.

<Note>
  If you had a global environment variable with the same name, it will be overridden.
</Note>

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  const sandbox = await Sandbox.create()

  const result = await sandbox.commands.run('echo $MY_VAR', {
    envs: {
      MY_VAR: '123',
    },
  })

  console.log(result)

  // Output example:
  // { exitCode: 0, error: undefined, stdout: '123\n', stderr: '' }

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  sandbox = Sandbox.create()
  result = sandbox.commands.run(
      'echo $MY_VAR',
      envs={
          'MY_VAR': '123'
      }
  )

  print(result)

  # Output example:
  # CommandResult(stderr='', stdout='123\n', exit_code=0, error='')

  sandbox.kill()
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).