# Source: https://docs.envzero.com/guides/community-and-resources/support-and-help/env-zero-cli.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# env zero CLI Tool

> Step-by-step guide to installing and using the env zero CLI for managing environments from your terminal

# env zero CLI

The env zero CLI provides a command-line interface for managing your cloud environments and deployments directly from your local machine. This guide walks you through installing, configuring, and using the CLI to build custom workflows while maintaining all the governance and visibility that env zero provides.

## Prerequisites

Before you begin, ensure you have:

* Node.js installed on your local machine
* An env zero account with appropriate permissions
* Access to create API keys in your organization

## Step 1: Install the CLI

Install the env zero CLI globally using npm or yarn:

<CodeGroup>
  ```bash npm theme={null}
  npm install -g @env0/cli
  ```

  ```bash yarn theme={null}
  yarn global add @env0/cli
  ```

</CodeGroup>

Verify the installation by checking the version:

```bash  theme={null}
env0 --version
```

## Step 2: Create API credentials

Navigate to your env zero organization settings to create API credentials:

1. Go to **Organization** → **Settings** → **API Keys**
2. Click **Add API Key**
3. Enter a descriptive name for your key
4. Copy and save both the API Key ID and secret

<Warning>
  Save your API Key ID and secret immediately - the secret will not be available after you close this window.
</Warning>

## Step 3: Configure the CLI

Configure the CLI with your credentials and organization details:

```bash  theme={null}
env0 configure
```

The CLI will prompt you for:

* API Key ID
* API Key Secret
* Organization ID
* Project ID (optional)
* Blueprint ID (optional)

<Tip>
  If you don't know your organization, project, or blueprint IDs, you can find them in the env0 UI. The CLI will help you discover these values during configuration.
</Tip>

## Step 4: Deploy your first environment

Deploy an environment using the CLI:

```bash  theme={null}
env0 deploy
```

The CLI will show real-time deployment logs with organized steps including:

* Git clone
* Terraform init
* Terraform plan
* Terraform apply

## Step 5: Use approval workflows

For deployments that require approval, use the `-a` flag:

```bash  theme={null}
env0 deploy -a
```

The deployment will pause and wait for approval. You can approve or cancel using:

<CodeGroup>
  ```bash approve theme={null}
  env0 approve
  ```

  ```bash cancel theme={null}
  env0 cancel
  ```

</CodeGroup>

## Step 6: Destroy environments

Destroy environments when they're no longer needed:

```bash  theme={null}
env0 destroy
```

## Advanced usage

The env zero CLI supports many additional commands and options. For complete documentation including:

* All available commands and flags
* Advanced configuration options
* Integration examples
* Troubleshooting guides

Visit our comprehensive guide:

<Card title="Complete env zero CLI documentation" icon="terminal" href="https://www.env0.com/blog/introducing-the-env0-cli">
  Read the full blog post with detailed command reference, advanced examples, and workflow demonstrations.
</Card>

## Next steps

* [API Reference](/api-reference/getting-started/authentication) - Complete API documentation
* [Getting Started Guide](/guides/getting-started) - Learn the basics of env zero
* [Workflows](/guides/admin-guide/workflows) - Advanced workflow configuration

Built with [Mintlify](https://mintlify.com).
