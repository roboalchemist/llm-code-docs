# Source: https://novita.ai/docs/guides/sandbox-cli-list-sandboxes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List sandboxes

export const SandboxCliConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the command-line related example code in this document, please refer to the <Link href="/guides/sandbox-cli">tutorial</Link> to install the CLI and complete <Link href="/guides/sandbox-cli-auth">authentication</Link>.</Note>;
  }
};

<SandboxCliConfigHint />

### List all running sandboxes

To list all running sandboxes, use the following command:

```bash Bash icon="terminal" theme={"system"}
novita-sandbox-cli sandbox list
```

### Filter by state

To filter the sandboxes by their state you can specify the `--state` flag, which can either be "**running**", "**paused**" or both.

```bash Bash icon="terminal" theme={"system"}
novita-sandbox-cli sandbox list --state running,paused
```

This will return all sandboxes, both running and paused.

### Filter by metadata

To filter the sandboxes by their metadata, use the `--metadata` flag.

```bash Bash icon="terminal" theme={"system"}
novita-sandbox-cli sandbox list --metadata key1=value1,key2=value2
```

### List limit

To limit the amount of sandboxes returned by the command, use the `--limit` flag.

```bash Bash icon="terminal" theme={"system"}
novita-sandbox-cli sandbox list --limit 10
```

By default, the command will return all sandboxes.


Built with [Mintlify](https://mintlify.com).