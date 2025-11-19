# Source: https://docs.hypermode.com/apps/deploy-app.md

# Deploy

> Deploy your Apps to production with Hypermode

Once you've developed and tested your App locally, you're ready to deploy it to
production on Hypermode. This guide walks you through setting up automatic
deployment for your Modus app.

## Prerequisites

Before deploying, ensure you have:

* A completed Modus app (see the [Develop guide](/apps/develop-app) for setup)
* A GitHub account and repository
* Your app configured in the Hypermode console (see the
  [Create Your App guide](/apps/create-app))

## Automatic deployment via GitHub Actions

Add a GitHub Actions workflow to your repository for automatic deployments.

Create `.github/workflows/ci-modus-build.yml`:

<Note>
  This workflow can stray out of date as new Golang releases are made. If you
  encounter issues, checkout our [open source recipes
  repo](https://github.com/hypermodeinc/modus-recipes/blob/main/.github/workflows/build.yml).
</Note>

```yaml
name: ci-modus-build

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: "22"

      - name: Setup Go
        uses: actions/setup-go@v5
        with:
          go-version: "1.24.5"

      - name: Setup TinyGo
        uses: acifani/setup-tinygo@v2
        with:
          tinygo-version: "0.38.0"

      - name: Build project
        run: npx -p @hypermode/modus-cli -y modus build

      - name: Publish GitHub artifact
        uses: actions/upload-artifact@v4
        with:
          name: build
          path: ./build/*
          retention-days: 7
```

Once the workflow is added, **any push to the `main` branch automatically
deploys your app**:

```bash
# Commit your changes
git add .
git commit -m "Deploy my Modus app"

# Push to trigger deployment
git push origin main
```

The deployment automatically:

1. Builds your Modus app via GitHub Actions
2. Deploys to your Hypermode endpoint
3. Makes your functions available via GraphQL

## Production features

Your deployed app includes:

* **Automatic scaling**: Functions scale to zero when not in use
* **HTTPS endpoints**: Secure GraphQL API
* **Bearer token auth**: API key authentication
* **Real-time logs**: Monitor function execution in the Activity tab
* **Environment variables**: Manage secrets and configuration

### Viewing function activity

Monitor your function executions in the Activity tab:

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-logs.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=f480dbee804ad81a29c3cff18886740b" alt="Function logs showing execution times and status" width="2684" height="1890" data-path="images/apps/console-logs.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-logs.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=8f79c47dc0517414498a9d8ab2711414 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-logs.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=cc70727763f09d22cfd2746ec7208c6b 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-logs.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=409cc44f693f10ef17236d7f1b2e55cb 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-logs.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=3e7edd8ff2ca7dc9c03f18a2cba06ac6 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-logs.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=3ccbaff89c7a5f9b5c750b0ad5aa63d3 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-logs.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=2760a2d92654f5f71fed34d3bc2101de 2500w" data-optimize="true" data-opv="2" />

You can see:

* Function execution history
* Response times and duration
* Success/error status
* Execution timestamps

### Environment variables

Configure environment variables in the Environment variables tab:

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-envs.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=22bd445f7ea0cf99d91f70029b057479" alt="Environment variables configuration panel" width="2684" height="1890" data-path="images/apps/console-envs.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-envs.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=064da9f2447b6a6933619a559c676c81 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-envs.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=aa8407a9d1c73725a85d75c00faef0b3 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-envs.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=451d4f70f680e092c0ec821423a4e68c 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-envs.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=4ccf63592d586c7cea1a07249b5fcbea 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-envs.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=ac153c77191796b5b5565a1ba319133f 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-envs.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=3d5cc5d919d1ea27a212b53bf1e53453 2500w" data-optimize="true" data-opv="2" />

Set production environment variables for:

* API keys and secrets
* Database connection strings
* Feature flags
* External service configurations

## Testing your deployment

Test your deployed functions via GraphQL:

```bash
curl -X POST https://your-app-endpoint.hypermode.app/graphql \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ sayHello(name: \"Production\") }"}'
```

## Next steps

With your app deployed, your development workflow becomes:

1. Develop and test locally with `modus dev`
2. Commit and push changes to GitHub
3. Automatic deployment to production
4. Monitor via Hypermode console

Your Modus app is now live and ready to handle production traffic with automatic
scaling, built-in observability, and secure endpoints.
