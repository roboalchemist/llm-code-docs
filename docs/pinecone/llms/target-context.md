# Source: https://docs.pinecone.io/reference/cli/target-context.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# CLI target context

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

Most CLI operations happen within the context of a specific organization and project. The **target context** is the organization and project scope that the CLI uses when running commands.

Before setting target context, you must authenticate with the CLI. See [CLI authentication](/reference/cli/authentication) for details on authentication methods.

## Why target context matters

By specifying a target organization and/or project, you're telling the CLI which resources to operate on.

* **Control plane operations** (creating indexes, listing indexes): Always happen within a specific project.
* **Admin API operations**:
  * Organization operations don't require target context. They operate on organizations you have access to.
  * Project management operations are scoped to your target organization. For example, running `pc project list` shows projects in the target org.
  * API key operations are scoped to the target project, unless you specify `--id`.

## How target context works

How the CLI sets and uses target context depends on your authentication method and how you configure it.

### User login

When you authenticate with `pc auth login`, the CLI automatically [targets](/reference/cli/target-context):

* The default organization returned by the server for your user.
* The first project in the list of that organization's projects.

However, you can change organization and project as needed:

```bash  theme={null}
pc auth login
pc target -o "my-org" -p "my-project"
```

### Service account

**Configured via CLI command**

When you configure a service account with `pc auth configure --client-id --client-secret`, the CLI automatically targets the organization associated with the service account (service accounts belong to a single organization). Then, to target a project:

* If the selected organization has only one project, the CLI automatically targets it.
* If that organization has multiple projects, the CLI prompts you to select one (or you can use the `--project-id` flag).
* If it doesn't have any projects, create one and then target it manually.

To change to a specific target project:

```bash  theme={null}
pc target -p "different-project"
```

Or, to select a project interactively:

```bash  theme={null}
pc target
```

**Configured via environment variables**

If you set service account credentials via environment variables (`PINECONE_CLIENT_ID` and `PINECONE_CLIENT_SECRET`) without running `pc auth configure`, the CLI does **not** automatically set any target context. You must explicitly set it with `pc target`.

Service accounts are scoped to a single organization. You can only target the organization associated with your service account credentials. To do this, and also target a specific project within that organization:

```bash  theme={null}
pc target -o "my-org" -p "my-project"
```

Or, to select a project interactively (the CLI discovers the organization automatically):

```bash  theme={null}
pc target
```

### API key

When you set a default API key (with `pc auth configure --api-key` or the `PINECONE_API_KEY` environment variable), the CLI does **not** change or clear its stored target context. However, in this scenario, control plane operations **do** use the API key's organization and project — not the CLI's saved target context (regardless of any calls you've made to `pc target`, or the output of `pc target --show`). This happens because Pinecone API keys are always scoped to a specific organization and project, and they cannot access resources outside of that scope.

<Note>
  Because Pinecone API keys cannot be used to authenticate calls to the Admin API, Admin API operations still authentiate with your user login token or service account credentials (if available).
</Note>

```bash  theme={null}
pc auth login
pc target -o "my-org" -p "my-project"
# Setting an API key doesn't change stored target context
pc auth configure --api-key "YOUR_API_KEY"
pc target --show  # Still shows my-org and my-project, but they're not used for control plane operations
```

## Viewing and managing target context

To view your current target organization and project:

```bash  theme={null}
# Show current target context
pc target --show

# Clear target context
pc target --clear
```
