# Source: https://mastra.ai/guides/deployment/vercel

# Deploy Mastra to Vercel

Use `@mastra/deployer-vercel` to deploy your Mastra server as serverless functions on Vercel. The deployer bundles your code and generates a `.vercel/output` directory conforming to Vercel's [Build Output API](https://vercel.com/docs/build-output-api/v3), ready to deploy with no additional configuration.

> **Info:** This guide covers deploying the [Mastra server](https://mastra.ai/docs/server/mastra-server). If you're using a [server adapter](https://mastra.ai/docs/server/server-adapters) or [web framework](https://mastra.ai/docs/deployment/web-framework), deploy the way you normally would for that framework.

## Before you begin

You'll need a [Mastra application](https://mastra.ai/guides/getting-started/quickstart) and a [Vercel](https://vercel.com/) account.

> **Warning:** Vercel Functions use an ephemeral filesystem, so any storage you configure (including observability storage) must be hosted externally. If you're using [LibSQLStore](https://mastra.ai/reference/storage/libsql) with a file URL, switch to a remotely hosted database.

## Installation

Add the `@mastra/deployer-vercel` package to your project:

**npm**:

```bash
npm install @mastra/deployer-vercel@latest
```

**pnpm**:

```bash
pnpm add @mastra/deployer-vercel@latest
```

**Yarn**:

```bash
yarn add @mastra/deployer-vercel@latest
```

**Bun**:

```bash
bun add @mastra/deployer-vercel@latest
```

Import [`VercelDeployer`](https://mastra.ai/reference/deployer/vercel) and set it as the deployer in your Mastra configuration:

```typescript
import { Mastra } from '@mastra/core'
import { VercelDeployer } from '@mastra/deployer-vercel'

export const mastra = new Mastra({
  deployer: new VercelDeployer(),
})
```

## Deploy

1. Push your project to a remote Git provider (e.g. GitHub) and connect your repository to Vercel.

   By default, Vercel runs `npm run build`, which triggers `mastra build`. If you don't have a build script, add `"build": "mastra build"` to your `package.json`.

   > **Note:** Remember to set your environment variables needed to run your application (e.g. your [model provider](https://mastra.ai/models/providers) API key).

2. Once you're ready, click **Deploy** and wait for the first deployment to complete.

3. Verify your deployment at `https://<your-project>.vercel.app/api/agents`, which should return a JSON list of your agents.

   Since the Mastra server prefixes every endpoint with `/api`, you have to add it to your URLs when making requests.

4. You can now call your Mastra endpoints over HTTP.

   > **Warning:** Set up [authentication](https://mastra.ai/docs/server/auth) before exposing your endpoints publicly.

## Studio

You can deploy [Studio](https://mastra.ai/docs/getting-started/studio) alongside your API by enabling the `studio` option. Studio is deployed as static assets served from Vercel's Edge CDN, so it doesn't consume function invocations.

```typescript
import { Mastra } from '@mastra/core'
import { VercelDeployer } from '@mastra/deployer-vercel'

export const mastra = new Mastra({
  deployer: new VercelDeployer({
    studio: true,
  }),
})
```

After deploying, Studio is available at the root URL (`https://<your-project>.vercel.app/`) and the API remains at `/api/*`. Studio automatically connects to the API on the same origin — no additional environment variables are needed.

> **Warning:** Once Studio is connected to your Mastra server, it has full access to your agents, workflows, and tools. Be sure to secure it properly in production (e.g. behind authentication, VPN, etc.) to prevent unauthorized access.

## Optional overrides

The Vercel deployer supports configuration options that are written to the Vercel Output API function config. See the [`VercelDeployer` reference](https://mastra.ai/reference/deployer/vercel) for available options like `maxDuration`, `memory`, and `regions`.

## Observability

Serverless functions can terminate immediately after returning a response. Any pending async work - like sending telemetry - may get killed before completing. Awaiting `flush()` ensures all traces are sent before the function exits.

```typescript
import type { VercelRequest, VercelResponse } from '@vercel/node'
import { mastra } from '../src/mastra'

export default async function handler(req: VercelRequest, res: VercelResponse) {
  const { message } = req.body
  const agent = mastra.getAgent('myAgent')
  const result = await agent.generate([{ role: 'user', content: message }])

  const observability = mastra.getObservability()
  await observability?.flush()

  return res.json(result)
}
```

> **Warning:** The Vercel deployer doesn't include `flush` calls. If you need this, you'll need to wrap the handler yourself to add the logic before returning the response. Alternatively, deploy to a long-running server like a [virtual machine](https://mastra.ai/guides/deployment/digital-ocean) where this isn't an issue.

## Related

- [VercelDeployer reference](https://mastra.ai/reference/deployer/vercel)
- [Deployment overview](https://mastra.ai/docs/deployment/overview)
- [Server adapters](https://mastra.ai/docs/server/server-adapters)
- [Web framework integration](https://mastra.ai/docs/deployment/web-framework)