# Source: https://juno.build/docs/guides/vue/deploy.md

# Source: https://juno.build/docs/guides/sveltekit/deploy.md

# Source: https://juno.build/docs/guides/react/deploy.md

# Source: https://juno.build/docs/guides/nextjs/deploy.md

# Source: https://juno.build/docs/guides/docusaurus/deploy.md

# Source: https://juno.build/docs/guides/astro/deploy.md

# Source: https://juno.build/docs/guides/angular/deploy.md

# Deploy an Angular App

Use this guide to deploy your project to production.

## 1\. Create a container

1.  Log in to the [Juno Console](https://console.juno.build).
    
2.  Click the **Launch a new satellite** button (the container for your project) from the launchpad
    
3.  Enter a **name** and select **Website**
    
4.  Confirm with **Create a Satellite**
    
5.  The platform will then provision its resources.
    
6.  Once the process is complete, click Continue to access the overview page.
    

## 2\. Configure your project

Create a `juno.config.mjs` file at the root of your project. Replace the `PROD_SATELLITE_ID` with the ID of the Satellite you created earlier and `dist/<application-name>/browser` with your project's name.

```
import { defineConfig } from "@junobuild/config";/** @type {import('@junobuild/config').JunoConfig} */export default defineConfig({  satellite: {    ids: {      development: "<DEV_SATELLITE_ID>",      production: "<PROD_SATELLITE_ID>"    },    source: "dist/<application-name>/browser",    predeploy: ["npm run build"]  }});
```

## 3\. How to deploy

You can deploy using either ([GitHub Actions](#github-actions-deployment)) or ([CLI](#cli-deployment)) (command line interface).

### GitHub Actions deployment

1.  From your Satellite's overview, navigate to the **Setup** tab.
    
2.  Click on **Add an access key**.
    
3.  Generate a new key with the default option. Click **Submit**.
    
4.  Upon successful creation, a **Secret token** will be displayed. Copy the value and save it as an [encrypted secret](https://docs.github.com/en/actions/security-guides/encrypted-secrets) in your GitHub repository or organization, using the key `JUNO_TOKEN`.
    
5.  Create a `deploy.yml` file in the `.github/workflows` subfolder of your repo.
    
6.  Add the following workflow configuration:
    

*   npm
*   yarn
*   pnpm

.github/workflows/deploy.yml

```
name: Deploy to Junoon:  workflow_dispatch:  push:    branches: [main]jobs:  deploy:    runs-on: ubuntu-latest    steps:      - name: Check out the repo        uses: actions/checkout@v4      - uses: actions/setup-node@v4        with:          node-version: 24          registry-url: "https://registry.npmjs.org"      - name: Install Dependencies        run: npm ci      - name: Deploy to Juno        uses: junobuild/juno-action@main        with:          args: hosting deploy        env:          JUNO_TOKEN: ${{ secrets.JUNO_TOKEN }}
```

.github/workflows/deploy.yml

```
name: Deploy to Junoon:  workflow_dispatch:  push:    branches: [main]jobs:  deploy:    runs-on: ubuntu-latest    steps:      - name: Check out the repo        uses: actions/checkout@v4      - uses: actions/setup-node@v4        with:          node-version: 24          registry-url: "https://registry.npmjs.org"      - name: Enable Corepack        run: corepack enable      - name: Activate Yarn        run: corepack prepare yarn@1.x --activate      - name: Install Dependencies        run: yarn install --frozen-lockfile      - name: Deploy to Juno        uses: junobuild/juno-action@main        with:          args: hosting deploy        env:          JUNO_TOKEN: ${{ secrets.JUNO_TOKEN }}
```

.github/workflows/deploy.yml

```
name: Deploy to Junoon:  workflow_dispatch:  push:    branches: [main]jobs:  deploy:    runs-on: ubuntu-latest    steps:      - name: Check out the repo        uses: actions/checkout@v4      - uses: actions/setup-node@v4        with:          node-version: 24          registry-url: "https://registry.npmjs.org"      - uses: pnpm/action-setup@v4        with:          version: 10      - name: Install Dependencies        run: pnpm i --frozen-lockfile      - name: Deploy to Juno        uses: junobuild/juno-action@main        with:          args: hosting deploy        env:          JUNO_TOKEN: ${{ secrets.JUNO_TOKEN }}
```

### CLI deployment

1.  Install the CLI

*   npm
*   yarn
*   pnpm

```
npm i -g @junobuild/cli
```

```
yarn global add @junobuild/cli
```

```
pnpm add -g @junobuild/cli
```

2.  Authenticate the CLI. This will open the Juno Console.

```
juno login
```

**Tip:**

An access token is used to identify your terminal. That's why the CLI asks whether you want to encrypt it with a password. For security reasons, it's recommended that you do so.

3.  In the browser window, click **Authorize** to grant permission.
    
4.  Deploy your site:
    

```
juno hosting deploy
```