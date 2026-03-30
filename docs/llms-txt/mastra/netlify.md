# Source: https://mastra.ai/guides/deployment/netlify

# Deploy Mastra to Netlify

Use `@mastra/deployer-netlify` to deploy your Mastra server as serverless functions on Netlify. The deployer bundles your code and generates a `.netlify` directory conforming to Netlify's [frameworks API](https://docs.netlify.com/build/frameworks/frameworks-api/#netlifyv1functions), ready to deploy.

> **Info:** This guide covers deploying the [Mastra server](https://mastra.ai/docs/server/mastra-server). If you're using a [server adapter](https://mastra.ai/docs/server/server-adapters) or [web framework](https://mastra.ai/docs/deployment/web-framework), deploy the way you normally would for that framework.

## Before you begin

You'll need a [Mastra application](https://mastra.ai/guides/getting-started/quickstart) and a [Netlify](https://www.netlify.com/) account.

> **Warning:** Netlify Functions use an ephemeral filesystem, so any storage you configure (including observability storage) must be hosted externally. If you're using [LibSQLStore](https://mastra.ai/reference/storage/libsql) with a file URL, switch to a remotely hosted database.

## Installation

Add the `@mastra/deployer-netlify` package to your project:

**npm**:

```bash
npm install @mastra/deployer-netlify@latest
```

**pnpm**:

```bash
pnpm add @mastra/deployer-netlify@latest
```

**Yarn**:

```bash
yarn add @mastra/deployer-netlify@latest
```

**Bun**:

```bash
bun add @mastra/deployer-netlify@latest
```

Import [`NetlifyDeployer`](https://mastra.ai/reference/deployer/netlify) and set it as the deployer in your Mastra configuration:

```typescript
import { Mastra } from '@mastra/core'
import { NetlifyDeployer } from '@mastra/deployer-netlify'

export const mastra = new Mastra({
  deployer: new NetlifyDeployer(),
})
```

Create a `netlify.toml` file with the following contents in your project root:

```toml
[build]
  command = "mastra build"
```

## Deploy

After setting up your project, push it to your remote Git provider of choice (e.g. GitHub).

1. Connect your repository to Netlify. During the setup process, Netlify will detect your `netlify.toml` file and set the build command to `mastra build`.

   > **Note:** Remember to set your environment variables needed to run your application (e.g. your [model provider](https://mastra.ai/models/providers) API key).

2. Once you're ready, click the **Deploy** button and wait for the first deployment to complete. It'll tell you that one function has been deployed.

3. Verify your deployment at `https://<random-slug>.netlify.app/api/agents`, which should return a JSON list of your agents.

   Since the [Mastra server](https://mastra.ai/docs/server/mastra-server) prefixes every API endpoint with `/api`, you have to add it to your URLs when making requests.

   > **Info:** Netlify functions are typically deployed at `https://<random-slug>.netlify.app/.netlify/functions/api`. The `NetlifyDeployer` redirects any request from `/*` to `/.netlify/functions/api/:splat`, so you don't need to include the `.netlify/functions` prefix in your URLs.

4. You can now call your Mastra endpoints over HTTP.

   > **Warning:** Set up [authentication](https://mastra.ai/docs/server/auth) before exposing your endpoints publicly.