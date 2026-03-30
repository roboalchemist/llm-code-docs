# Source: https://mastra.ai/guides/deployment/digital-ocean

# Deploy Mastra to Digital Ocean

This guide covers Digital Ocean's App Platform and Droplets. Each of these offerings has its own set of strengths and is suited for different types of projects and developer expertise. Read [Digital Ocean's comparison](https://www.digitalocean.com/community/conceptual-articles/digitalocean-app-platform-vs-doks-vs-droplets) to understand the differences and choose the best option for your project.

> **Info:** This guide covers deploying the [Mastra server](https://mastra.ai/docs/server/mastra-server). If you're using a [server adapter](https://mastra.ai/docs/server/server-adapters) or [web framework](https://mastra.ai/docs/deployment/web-framework), deploy the way you normally would for that framework.

## Before you begin

You'll need a [Mastra application](https://mastra.ai/guides/getting-started/quickstart) and a [Digital Ocean](https://www.digitalocean.com/) account.

The **App Platform** uses an ephemeral filesystem, so any storage you configure (including observability storage) must be hosted externally. If you're using [LibSQLStore](https://mastra.ai/reference/storage/libsql) with a file URL, switch to a remotely hosted database.

## App Platform

After setting up your project, push it to your remote Git provider of choice (e.g. GitHub).

1. Follow the official [App Platform quickstart](https://docs.digitalocean.com/products/app-platform/getting-started/quickstart/#create-an-app). It'll guide you through connecting your repository, selecting the branch to deploy from, and configuring the source directory if necessary.

2. Make sure that a "Node.js" build is detected. You'll need to configure a build command. Set it based on your package manager:

   **npm**:

   ```bash
   npm run build
   ```

   **pnpm**:

   ```bash
   pnpm run build
   ```

   **Yarn**:

   ```bash
   yarn build
   ```

   **Bun**:

   ```bash
   bun run build
   ```

3. Add any required environment variables for your Mastra application. This includes API keys, database URLs, and other configuration values.

4. Your app will be built and deployed automatically. Digital Ocean will provide you with a URL to access your deployed application.

5. You can now call your Mastra endpoints over HTTP.

   > **Warning:** Set up [authentication](https://mastra.ai/docs/server/auth) before exposing your endpoints publicly.

## Droplets

### Prerequisites

- A Droplet running Ubuntu 24.04 LTS or later
- A domain name with an A record pointing to your droplet
- A reverse proxy configured (e.g., using [nginx](https://nginx.org/))
- SSL certificate configured (e.g., using [Let's Encrypt](https://letsencrypt.org/))
- Node.js 22.13.0 or later installed on your droplet

### Deploy

After setting up your project, push it to your remote Git provider of choice (e.g. GitHub). Connect to your Droplet and make sure `git` is installed.

1. Clone your repository:

   **Public Repository**:

   ```bash
   git clone https://github.com/<your-username>/<your-repository>.git
   ```

   **Private Repository**:

   ```bash
   git clone https://<your-username>:<your-personal-access-token>@github.com/<your-username>/<your-repository>.git
   ```

   Navigate to the repository directory:

   ```bash
   cd "<your-repository>"
   ```

2. Install the project dependencies:

   **npm**:

   ```bash
   npm install
   ```

   **pnpm**:

   ```bash
   pnpm install
   ```

   **Yarn**:

   ```bash
   yarn install
   ```

   **Bun**:

   ```bash
   bun install
   ```

3. Set the required environment variables for your Mastra application. Create a `.env` file in the root of your project:

   ```bash
   touch .env
   ```

   Edit the `.env` file and add your environment variables:

   ```bash
   OPENAI_API_KEY=your-api-key
   ```

4. Build the project:

   **npm**:

   ```bash
   npm run build
   ```

   **pnpm**:

   ```bash
   pnpm run build
   ```

   **Yarn**:

   ```bash
   yarn build
   ```

   **Bun**:

   ```bash
   bun run build
   ```

   This will create a production build of Mastra's server in the `.mastra/output` directory.

5. You can run the [Mastra Server](https://mastra.ai/docs/deployment/mastra-server) by running the `mastra start` command:

   ```bash
   mastra start
   ```

   > **Info:** Your Mastra application will run on port 4111 by default. Ensure your reverse proxy is configured to forward requests to this port.

6. You can now call your Mastra endpoints over HTTP.

   > **Warning:** Set up [authentication](https://mastra.ai/docs/server/auth) before exposing your endpoints publicly.

## Related

- [Digital Ocean App Platform](https://docs.digitalocean.com/products/app-platform/)
- [Digital Ocean Droplets](https://docs.digitalocean.com/products/droplets/)