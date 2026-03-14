# Source: https://novita.ai/docs/guides/sandbox-template-start-cmd.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Start Command

export const SandboxConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the example code in this document, please ensure you have properly configured environment variables. For details, please refer to <a href="/guides/sandbox-your-first-agent-sandbox#configure-environment-variables">Configure Environment Variables</a>.</Note>;
  }
};

export const SandboxCliConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the command-line related example code in this document, please refer to the <Link href="/guides/sandbox-cli">tutorial</Link> to install the CLI and complete <Link href="/guides/sandbox-cli-auth">authentication</Link>.</Note>;
  }
};

The start command allows you to specify a command that will be **already running** when you spawn your custom sandbox.
This way, you can for example have running servers or seeded databases inside the sandbox that are already fully ready when you spawn the sandbox using the SDK and with zero waiting time for your users during the runtime.

The idea behind the start command feature is to lower the wait times for your users and have everything ready for your users when you spawn your sandbox.

You can see how it works [here](/guides/sandbox-template#how-it-works).

<SandboxCliConfigHint />

## How to add start command

When you are building a sandbox template you can specify the start command by using the `-c` option:

```bash Bash icon="terminal" theme={"system"}
novita-sandbox-cli template build -c "<your-start-command>"
```

When you spawn the custom sandbox you built, the start command will be already running if there was no error when we tried to execute it.

### Sandbox template config

You can specify the start command also inside the `novita.toml` in the same directory where you run `novita-sandbox-cli template build`.

```toml Toml icon="gear" theme={"system"}
template_id = "0r0efkbfwzfp9p7qpc1c"
dockerfile = "novita.Dockerfile"
template_name = "my-agent-sandbox"
start_cmd = "<your-start-command>"
```

## Logs

You can retrieve the start command's logs using the CLI during runtime.

<Note>
  These logs are the logs from the start command during the build phase.
</Note>

<SandboxConfigHint />

```bash Bash icon="terminal" theme={"system"}
novita-sandbox-cli sandbox logs <sandbox-id>
```


Built with [Mintlify](https://mintlify.com).