# Source: https://novita.ai/docs/guides/sandbox-auto-persistence.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Auto Pause and Resume

export const SandboxBetaVersionWarning = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Warning>The following features require <Link href="/guides/sandbox-sdk-and-cli#install-beta-sdk" target="self">installing the Beta SDK & CLI</Link>. Please note that beta features are subject to change and may be less stable than production releases. If you encounter any issues while using these features, please <Link href="https://meetings-na2.hubspot.com/junyu" target="_blank">contact us</Link>.</Warning>;
  }
};

<SandboxBetaVersionWarning />

When the sandbox instance is not currently needed but you need to be able to resume it at any time later, you can refer to the [documentation](/guides/sandbox-persistence) to manually pause and resume sandbox instances.

The **"Auto Pause and Resume"** feature allows your sandbox instance to automatically pause after [timeout](/guides/sandbox-lifecycle) and resume when needed. When you attempt to perform operations (such as executing commands, running code, or file operations) on a paused sandbox, it will automatically resume without manual intervention.

## Enable Auto Pause

You can enable the auto pause feature by setting the `auto_pause` parameter to `true` when creating a sandbox instance. The sandbox instance will automatically pause after timeout and can be resumed later.

<Warning>
  Note: The resumed sandbox instance will still have the auto pause feature enabled and will automatically pause again after timeout.
</Warning>

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter';

  const sandbox = await Sandbox.create(
      {
          timeoutMs: 5_000,
          autoPause: true
      },
  );
  console.log('Sandbox created', sandbox.sandboxId)

  console.log('Waiting for 10 seconds...')
  await new Promise(resolve => setTimeout(resolve, 10000));

  const resumedSandbox = await Sandbox.connect(sandbox.sandboxId)
  console.log('Sandbox resumed', resumedSandbox.sandboxId)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.core import Sandbox
  import time

  sandbox = Sandbox.create(
      timeout=5,
      auto_pause=True,
  )
  print('Sandbox created', sandbox.sandbox_id)

  print('Waiting for 10 seconds...')
  time.sleep(10)

  resumed_sandbox = Sandbox.connect(sandbox.sandbox_id)
  print('Sandbox resumed', resumed_sandbox.sandbox_id)

  sandbox.kill()
  ```
</CodeGroup>

## Enable Auto Resume

You can enable the auto resume feature by setting the `auto_resume` key in `metadata` to `true` when creating a sandbox instance. Once enabled, when you attempt to operate on a paused sandbox (such as executing commands, running code, file operations, etc.), the sandbox will automatically resume.

<Warning>
  Note: The default timeout for the resumed sandbox is 5 minutes. You can update the sandbox timeout using the `setTimeout` or `set_timeout` method.
</Warning>

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter';

  const sandbox = await Sandbox.create(
      {
          metadata:{"auto_resume": "true"}
      }
  );
  console.log('Sandbox created', sandbox.sandboxId)

  await sandbox.betaPause()
  console.log('Sandbox paused', sandbox.sandboxId)

  const result = await sandbox.commands.run('ls -al')
  console.log('Command result', result)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.core import Sandbox

  sandbox = Sandbox.create(
      metadata={
          "auto_resume": "true",
      }
  )
  print('Sandbox created', sandbox.sandbox_id)

  sandbox.beta_pause()
  print('Sandbox paused', sandbox.sandbox_id)

  result = sandbox.commands.run('ls -al')
  print('Command result', result)

  sandbox.kill()
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).