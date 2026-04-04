# Source: https://novita.ai/docs/guides/sandbox-idle-timeout.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Idle Timeout

export const SandboxBetaVersionWarning = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Warning>The following features require <Link href="/guides/sandbox-sdk-and-cli#install-beta-sdk" target="self">installing the Beta SDK & CLI</Link>. Please note that beta features are subject to change and may be less stable than production releases. If you encounter any issues while using these features, please <Link href="https://meetings-na2.hubspot.com/junyu" target="_blank">contact us</Link>.</Warning>;
  }
};

<SandboxBetaVersionWarning />

We can set a timeout for each sandbox (refer to [Lifecycle Management](/guides/sandbox-lifecycle)). When the sandbox running time reaches the timeout, the sandbox will be automatically killed. However, in some scenarios, we cannot determine the expected running time of the sandbox, but we want the sandbox to be automatically killed when not in use to save costs. In this case, you can use the **"Idle Timeout"** feature.

When creating a sandbox, we can set the `idle_timeout` parameter in metadata (unit: seconds, minimum is 60) to enable the **"Idle Timeout"** feature. Once enabled, when the system detects that the sandbox has no operations (executing commands, running code, file operations, etc.) within the specified time range, the system will kill the sandbox instance. Otherwise, the sandbox will continue to run until it reaches the maximum time limit for sandbox operation (currently default is 3600 seconds).

Please refer to the following example:

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter';

  const sandbox = await Sandbox.create(
      {
          metadata: { "idle_timeout": "60" }
      }
  );
  console.log('Sandbox created', sandbox.sandboxId)

  const result = await sandbox.commands.run('ls -al')
  console.log('Command result', result)

  await new Promise(resolve => setTimeout(resolve, 90000));

  const isRunning = await sandbox.isRunning()
  console.log('Sandbox is running', isRunning)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.core import Sandbox
  import time

  sandbox = Sandbox.create(
      metadata={"idle_timeout": "60"}  # Minimum time is 60s, you can customize it
  )
  print('Sandbox created', sandbox.sandbox_id)

  result = sandbox.commands.run('ls -al')
  print('Command result', result)

  print('Waiting for 90 seconds...')
  time.sleep(90)

  is_running = sandbox.is_running()
  print('Sandbox is running', is_running)

  sandbox.kill()
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).