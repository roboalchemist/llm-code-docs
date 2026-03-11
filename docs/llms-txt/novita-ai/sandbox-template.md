# Source: https://novita.ai/docs/guides/sandbox-template.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sandbox Templates

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

Sandbox templates allow you to customize the sandbox environment to your needs.

<Tip>
  Novita Agent Sandbox service has built-in public templates for out-of-the-box use. You can find these public templates in the <Link href="https://novita.ai/sandbox-console/template" target="_blank">console</Link>.
</Tip>

<SandboxCliConfigHint />

To create a sandbox template, you specify the `novita.Dockerfile`. We then take this Dockerfile and create a new sandbox template from it and give you back a template ID.

You can then use this template ID to create a new sandbox with the SDK based on the template you created.

## How to create custom sandbox

**Steps**

1. [Install CLI](#1-install-cli)
2. [Initialize sandbox template](#2-initialize-sandbox-template)
3. [Customize `novita.Dockerfile`](#3-customize-novita-dockerfile)
4. [Build your sandbox template](#4-build-your-sandbox-template)
5. [Start your custom sandbox](#5-start-your-custom-sandbox)

### 1. Install CLI

Please refer to the <Link href="/guides/sandbox-cli">tutorial</Link> for installation and complete <Link href="/guides/sandbox-cli-auth">authentication</Link>.

### 2. Initialize sandbox template

The following command will create a basic `novita.Dockerfile` in the current directory.

<CodeGroup isTerminalCommand>
  ```bash Bash icon="terminal" theme={"system"}
  novita-sandbox-cli template init
  ```
</CodeGroup>

### 3. Customize `novita.Dockerfile`

Now you can customize your sandbox template by editing the `novita.Dockerfile` file.

<CodeGroup title="novita.Dockerfile">
  ```dockerfile novita.Dockerfile icon="docker" theme={"system"}
  # Make sure to use this base image
  FROM novitalabs/code-interpreter:latest

  # Install some Python packages
  RUN pip install cowsay
  ```
</CodeGroup>

### 4. Build your sandbox template

Now you can build your sandbox template. We'll use Docker and the CLI.
What is going to happen is that CLI will call Docker to build the image and then push it to the Novita cloud.
Then we convert the Docker image to a micro VM that can be then launched as a sandbox with our SDK.

<CodeGroup isTerminalCommand>
  ```bash Bash icon="terminal" theme={"system"}
  novita-sandbox-cli template build -c "/root/.jupyter/start-up.sh"
  ```
</CodeGroup>

This process will take a moment. In the end, you'll see your template ID that you'll need to use to create a sandbox with the SDK.

### 5. Start your custom sandbox

Now you can use the template ID to create a sandbox with the SDK.

<SandboxConfigHint />

<CodeGroup>
  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from 'novita-sandbox/code-interpreter'

  // Your template ID from the previous step
  const templateID = 'id-of-your-template'

  // Pass the template ID to the `Sandbox.create` method
  const sandbox = await Sandbox.create(templateID)

  // The template installed cowsay, so we can use it
  const result = await sandbox.runCode(`
  import cowsay
  cowsay.say('Hello!')`)

  console.log(result)

  await sandbox.kill()
  ```

  ```python Python icon="python" theme={"system"}
  from novita_sandbox.code_interpreter import Sandbox

  # Your template ID from the previous step
  template_id = 'id-of-your-template'

  # Pass the template ID to the `Sandbox.create` method
  sandbox = Sandbox.create(template_id)

  # The template installed cowsay, so we can use it
  result = sandbox.run_code("""
  import cowsay
  cowsay.say('Hello!')""")

  print(result)

  sandbox.kill()
  ```
</CodeGroup>

## How it works

Every time you are building a sandbox template, we create a container based on the `novita.Dockerfile` file you create in the process.
We extract the container's filesystem, do provisioning and configuration (e.g. installing required dependencies), and start a sandbox.

Then, these steps happen:

1. We take the running sandbox.
2. (Only if you specified the [start command](/guides/sandbox-template-start-cmd), otherwise this step is skipped) Execute the start command.
3. Wait for readiness (by default 20 seconds if start command is specified, otherwise immediately ready). Readiness check can be configured using [ready command](/guides/sandbox-template-ready-cmd).
4. Snapshot the sandbox and make it ready for you to spawn it with the SDK.

We call this sandbox snapshot a *sandbox template*.

<Note title="Sandbox Snapshot">
  Snapshots are saved running sandboxes. We serialize and save the whole sandbox's filesystem together with all the running processes in a way that can be loaded later.

  This allows us to load the sandbox in a few hundred milliseconds any time later with all the processes already running and the filesystem exactly as it was.
</Note>


Built with [Mintlify](https://mintlify.com).