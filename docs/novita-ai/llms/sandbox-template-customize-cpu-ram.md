# Source: https://novita.ai/docs/guides/sandbox-template-customize-cpu-ram.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Customize sandbox CPU & RAM

export const SandboxCliConfigHint = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Note>Before running the command-line related example code in this document, please refer to the <Link href="/guides/sandbox-cli">tutorial</Link> to install the CLI and complete <Link href="/guides/sandbox-cli-auth">authentication</Link>.</Note>;
  }
};

You can customize the CPU and RAM of your sandbox template via CLI.

<SandboxCliConfigHint />

You need to create a <Link href="/guides/sandbox-template">sandbox template</Link> first.

During the build step, you can specify the CPU and RAM of your sandbox template.

The following command will create a sandbox template with 2 vCPUs and 2GB RAM.

```bash Bash icon="terminal" theme={"system"}
novita-sandbox-cli template build -c "/root/.jupyter/start-up.sh" --cpu-count 2 --memory-mb 2048
```

## Through Configuration File

You can also specify the vCPU and RAM specifications for the sandbox template in the `novita.toml` file in the same directory where you run the `novita-sandbox-cli template build` command.

```toml Toml icon="gear" theme={"system"}
template_id = "0r0efkbfwzfp9p7qpc1c"
dockerfile = "novita.Dockerfile"
template_name = "my-agent-sandbox"
ready_cmd = "<your-ready-command>"
# Specify sandbox template vCPU and RAM specifications as 2 vCPUs and 2GB RAM
cpu_count = 2
memory_mb = 2_048
```


Built with [Mintlify](https://mintlify.com).