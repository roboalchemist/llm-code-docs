# Source: https://novita.ai/docs/guides/sandbox-cli-shutdown-sandboxes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Shutdown running sandboxes

export const SandboxCliConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the command-line related example code in this document, please refer to the <Link href="/guides/sandbox-cli">tutorial</Link> to install the CLI and complete <Link href="/guides/sandbox-cli-auth">authentication</Link>.</Note>;
  }
};

You can shutdown single or all running sandboxes with the CLI.

<SandboxCliConfigHint />

## Shutdown single sandbox

To shutdown a single sandbox, run the following command:

```bash Bash icon="terminal" theme={"system"}
novita-sandbox-cli sandbox kill <sandbox-id>
```

## Shutdown all sandboxes

To shutdown all running sandboxes, run the following command:

```bash Bash icon="terminal" theme={"system"}
novita-sandbox-cli sandbox kill --all
```


Built with [Mintlify](https://mintlify.com).