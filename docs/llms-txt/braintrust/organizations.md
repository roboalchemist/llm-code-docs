# Source: https://braintrust.dev/docs/admin/organizations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage organizations

> Configure organization settings and integrations

Organizations represent your team or business in Braintrust. Each organization contains projects, users, and organization-wide settings. You can create multiple organizations to organize projects differently, and users can be members of multiple organizations.

Configure your organization by going to <Icon icon="settings-2" /> **Settings**. You can also customize organization settings using the [API](/api-reference).

## Invite members

Add users to your organization:

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Organization**, select **Members**.
3. Click **Invite**.
4. Enter email addresses (one per line for multiple invites).
5. Select a permission group (Owners, Engineers, or Viewers).
6. Click **Send invites**.

Invited users receive an email with a link to join your organization. They must be assigned to at least one permission group.

## Configure permission groups

Permission groups are the core of Braintrust's access control system. They are collections of users that can be granted specific permissions to projects, experiments, and datasets.

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Organization**, select **Permission groups**.
3. View existing groups or create new ones.
4. Assign users to groups when inviting members.

For detailed information about creating and managing permission groups, see [Control access](/admin/access-control).

## Manage API keys

Create API keys for authentication:

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Organization**, select **API keys**.
3. Click **+ API key**.
4. Enter a name to identify the key.
5. Click **Create**.
6. Copy the key immediately (it won't be shown again).

API keys inherit permissions from the user who created them. Organization owners can view and manage all API keys in the organization.

<Note>
  Store API keys securely. Anyone with an API key can access Braintrust with the permissions of the key's creator.
</Note>

## Create service tokens

Service tokens enable system integrations without tying credentials to individual users:

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Organization**, select **Service tokens**.
3. Click **+ Service token**.
4. Enter a name for the service account.
5. Assign permission groups or grant specific permissions.
6. Enter a name for the service token.
7. Click **Create**.
8. Copy the token immediately (it won't be shown again).

Service tokens use the `bt-st-` prefix. Use them anywhere API keys (`sk-` prefix) are accepted.

<Note>
  Only organization owners can manage service accounts and service tokens.
</Note>

## Configure AI providers

Set up API keys for AI providers used across your organization:

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Organization**, select **AI providers**.
3. Click the provider you want to configure.
4. Enter your API key for that provider.
5. Click **Save**.

Configured providers are available in playgrounds, experiments, and the AI Proxy without users needing individual API keys.

You can also configure AI providers inline directly from playgrounds and prompt pages. When you attempt to run a playground or prompt without a configured provider, you'll see an option to add your API key inline without leaving the page.

<Note>
  Organization-level AI provider keys serve as defaults across all projects. Individual projects can override these keys with [project-level configuration](/admin/projects#configure-ai-providers). When both are configured, project-level keys take precedence for that specific project.
</Note>

<Note>
  API keys are encrypted at rest using [transparent data encryption](https://en.wikipedia.org/wiki/Transparent_data_encryption) with a [unique 256-bit key and nonce](https://libsodium.gitbook.io/doc/secret-key_cryptography/aead).
</Note>

### Add custom providers

Braintrust supports custom AI providers, allowing you to integrate any AI model or endpoint into your evaluation and tracing workflows. See [Custom providers](/integrations/ai-providers/custom) for details.

## Select models for Loop

[Loop](/observe/loop) requires organization-level AI providers to function. Before selecting models, ensure you have [configured AI providers](#configure-ai-providers) at the organization level.

Select which models your organization can use in Loop:

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Organization**, select **Loop**.
3. Select models.

## Enable Slack integration

Connect Slack to send alerts and notifications to your channels:

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Organization**, select **Integrations**.
3. Click **Enable Slack**.
4. Authorize Braintrust to access your Slack workspace.
5. Select which channels Braintrust can access.

Once enabled, you can configure alerts to send notifications to specific Slack channels. See [Set up alerts](/admin/automations/alerts) for details.

## Set environment variables

Define secrets available to all functions in your organization:

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Organization**, select **Env variables**.
3. Click **Add variable**.
4. Enter a key and value.
5. Click **Save**.

Environment variables are accessible from prompts, scorers, and tools. Use them for API keys, database credentials, or configuration values.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  // Access in TypeScript functions
  const apiKey = process.env.MY_API_KEY;
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # Access in Python functions
  import os
  api_key = os.environ["MY_API_KEY"]
  ```
</CodeGroup>

## Configure API URLs (self-hosted)

For self-hosted deployments, set custom API URLs:

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Organization**, select **API URL**.
3. Enter your URLs:
   * **API URL**: Main API endpoint.
   * **Proxy URL**: AI Proxy endpoint.
   * **Realtime URL**: Realtime API endpoint.
4. Click **Save**.

Test connectivity using the provided test commands.

When you configure these API URLs, Braintrust automatically provisions a service token for your data plane. This enables features like [data retention](/admin/automations/data-management#data-retention) without requiring manual service token setup. You can view and manage this token in the [Service tokens](#create-service-tokens) section.

## Set git metadata logging

Control which git metadata fields are logged:

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Organization**, select **Logging**.
3. Enable **Collect git metadata**.
4. Select fields to log.
5. Click **Save**.

Git metadata helps track which code version generated specific logs or experiment results.

## Configure environments

Create environments to version prompts and functions:

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Organization**, select **Environments**.
3. Click **+ Environment**.
4. Enter environment name (e.g., "production", "staging", "dev").
5. Click **Create environment**.

Assign prompt and function versions to environments to separate development from production. See [Manage environments](/deploy/environments) for details.

## Delete an organization

To delete an organization, [contact Braintrust](https://braintrust.dev/contact).

## Next steps

* [Control access](/admin/access-control) with permission groups
* [Manage projects](/admin/projects) within your organization
* [Configure the AI Proxy](/admin/proxy) for centralized provider access
* [Set up automations](/admin/automations) for alerts and data management
