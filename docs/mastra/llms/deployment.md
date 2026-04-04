# Source: https://mastra.ai/docs/mastra-cloud/deployment

# Deployment

Deploy your Mastra application to production and expose your agents, tools, and workflows as REST API endpoints.

> **Info:** Mastra Cloud is currently in beta, but many teams are already using it to deploy their agents. It's the easiest way to run Mastra agents in a managed environment.

## Enable deployments

After [setting up your project](https://mastra.ai/docs/mastra-cloud/setup), select **Deployment** in the sidebar and select **Enable Deployments**.

Once enabled, your project automatically builds and deploys. Future pushes to your main branch trigger automatic redeployments.

## Dashboard

The **Overview** page shows your project's domain URL, status, latest deployment, and connected agents and workflows.

![Project dashboard](/assets/images/mastra-cloud-project-dashboard-6890c8032419d5fb075313d08bfd598b.jpg)

Click the **Deployments** menu item to view build logs. Open **Settings** to configure environment variables, branch, storage, and endpoint URLs.

> **Note:** Changes to settings require a new deployment to take effect

## Storage configuration

Mastra Cloud offers two storage options:

1. **Mastra Cloud Store**: Managed storage provided by Mastra Cloud
2. **Bring your own database**: Connect to your own external database

### Using Mastra Cloud Store

When using the managed Mastra Cloud Store (enabled in your project settings), storage must be configured on the `Mastra` instance, not on individual agent `Memory` instances.

Configure storage on your Mastra instance:

```typescript
import { Mastra } from '@mastra/core'
import { LibSQLStore } from '@mastra/libsql'

export const mastra = new Mastra({
  storage: new LibSQLStore({
    id: 'mastra-store',
    url: 'file:./mastra.db',
  }),
  agents: { myAgent },
})
```

Agents can use Memory without specifying storage as they inherit from the Mastra instance:

```typescript
import { Agent } from '@mastra/core/agent'
import { Memory } from '@mastra/memory'

export const myAgent = new Agent({
  id: 'my-agent',
  memory: new Memory({
    // No storage here - uses instance-level storage from Mastra Cloud Store
    options: {
      lastMessages: 20,
    },
  }),
})
```

### Bring your own database

If you don't use Mastra Cloud Store, you can use any [storage provider](https://mastra.ai/docs/memory/storage) with any configuration. Set your database connection strings as environment variables in your project's **Settings** page.

## Using your deployment

After deployment, interact with your agents using the [Mastra Client](https://mastra.ai/docs/server/mastra-client) or call the REST API endpoints directly.

## Next steps

- [Studio](https://mastra.ai/docs/mastra-cloud/studio) - Test your agents in the cloud
- [Observability](https://mastra.ai/docs/mastra-cloud/observability) - Monitor traces and logs