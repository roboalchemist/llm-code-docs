# Source: https://mastra.ai/guides/deployment/amazon-ec2

# Deploy Mastra to Amazon EC2

Deploy your Mastra server to Amazon EC2. This gives you full control over your server environment and supports long-running agents and workflows.

> **Info:** This guide covers deploying the [Mastra server](https://mastra.ai/docs/server/mastra-server). If you're using a [server adapter](https://mastra.ai/docs/server/server-adapters) or [web framework](https://mastra.ai/docs/deployment/web-framework), deploy the way you normally would for that framework.

## Before you begin

You'll need:

- A [Mastra application](https://mastra.ai/guides/getting-started/quickstart)
- An [EC2](https://aws.amazon.com/ec2/) instance (Ubuntu or Amazon Linux) with Git and Node.js 22.13.0+ installed

For production, you'll also need:

- A domain name pointing to your instance (required for SSL certificates)
- An SSL certificate for your domain (e.g., using [Certbot](https://certbot.eff.org/) with Let's Encrypt)
- A reverse proxy (e.g., [nginx](https://nginx.org/)) to forward traffic to your application

## Deploy

1. Connect to your EC2 instance and clone your repository:

   **Public Repository**:

   ```bash
   git clone https://github.com/<your-username>/<your-repository>.git
   ```

   **Private Repository**:

   ```bash
   git clone git@github.com:<your-username>/<your-repository>.git
   ```

   Navigate to the repository directory:

   ```bash
   cd "<your-repository>"
   ```

2. Install dependencies:

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

3. Create a `.env` file and add your environment variables:

   ```bash
   touch .env
   ```

   Remember to set your environment variables needed to run your application (e.g. your model provider API key):

   ```bash
   OPENAI_API_KEY=<your-openai-api-key>
   # Add other required environment variables
   ```

4. Build the application:

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

5. Run the application:

   ```bash
   node --env-file=".env" .mastra/output/index.mjs
   ```

   This is a basic example. In production, use a process manager like [PM2](https://pm2.keymetrics.io/) or [systemd](https://systemd.io/) to keep your application running and handle restarts.

   > **Warning:** Set up [authentication](https://mastra.ai/docs/server/auth) before exposing your endpoints publicly.

6. Your Mastra server is now running on port 4111, but it's only accessible locally.

   You can open port 4111 in your EC2 security group for direct access, or configure a reverse proxy (such as nginx) to listen on ports 80 and 443 and forward requests to `http://localhost:4111`.

   In production, you should use a reverse proxy so you can configure HTTPS. HTTPS encrypts traffic and is required for most webhook integrations and external services your agents interact with.

7. Verify your deployment at `https://<your-ec2-address>/api/agents`, which should return a JSON list of your agents.

8. You can now call your Mastra endpoints over HTTP.

## Next steps

- [Connect from a Mastra Client](https://mastra.ai/docs/server/mastra-client)
- [Deployment overview](https://mastra.ai/docs/deployment/overview)