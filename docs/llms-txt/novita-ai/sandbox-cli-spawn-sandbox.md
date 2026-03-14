# Source: https://novita.ai/docs/guides/sandbox-cli-spawn-sandbox.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create sandbox and connect to terminal

export const SandboxCliConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the command-line related example code in this document, please refer to the <Link href="/guides/sandbox-cli">tutorial</Link> to install the CLI and complete <Link href="/guides/sandbox-cli-auth">authentication</Link>.</Note>;
  }
};

<SandboxCliConfigHint />

With the following command, you can use the command line tool to start a sandbox and connect to the terminal.

```bash Bash icon="terminal" theme={"system"}
novita-sandbox-cli sandbox create <template-id>
```


Built with [Mintlify](https://mintlify.com).