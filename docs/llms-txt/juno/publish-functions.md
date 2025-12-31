# Source: https://juno.build/docs/guides/github-actions/publish-functions.md

# Build and Publish Serverless Functions

This section explains how to automate the build and publication of your serverless functions using GitHub Actions. The process works for functions written in TypeScript or Rust and helps integrate function deployment into your development workflow.

---

## Configuration

To configure an action to build and publish serverless functions, follow these steps:

1.  Create or edit `publish.yml` in `.github/workflows/`.
2.  Paste the following code into the file:

*   npm
*   yarn
*   pnpm

.github/workflows/publish.yml

```
name: Publish Serverless Functionson:  workflow_dispatch:  push:    branches: [main]jobs:  publish:    runs-on: ubuntu-latest    steps:      - name: Check out the repo        uses: actions/checkout@v4      - uses: actions/setup-node@v4        with:          node-version: 24          registry-url: "https://registry.npmjs.org"      - name: Install Dependencies        run: npm ci      - name: Build        uses: junobuild/juno-action@full        with:          args: functions build      - name: Publish        uses: junobuild/juno-action@full        with:          args: functions publish        env:          JUNO_TOKEN: ${{ secrets.JUNO_TOKEN }}
```

.github/workflows/publish.yml

```
name: Publish Serverless Functionson:  workflow_dispatch:  push:    branches: [main]jobs:  publish:    runs-on: ubuntu-latest    steps:      - name: Check out the repo        uses: actions/checkout@v4      - uses: actions/setup-node@v4        with:          node-version: 24          registry-url: "https://registry.npmjs.org"      - name: Enable Corepack        run: corepack enable      - name: Activate Yarn        run: corepack prepare yarn@1.x --activate      - name: Install Dependencies        run: yarn install --frozen-lockfile      - name: Build        uses: junobuild/juno-action@full        with:          args: functions build      - name: Publish        uses: junobuild/juno-action@full        with:          args: functions publish        env:          JUNO_TOKEN: ${{ secrets.JUNO_TOKEN }}
```

.github/workflows/publish.yml

```
name: Publish Serverless Functionson:  workflow_dispatch:  push:    branches: [main]jobs:  publish:    runs-on: ubuntu-latest    steps:      - name: Check out the repo        uses: actions/checkout@v4      - uses: actions/setup-node@v4        with:          node-version: 24          registry-url: "https://registry.npmjs.org"      - uses: pnpm/action-setup@v4        with:          version: 10      - name: Install Dependencies        run: pnpm i --frozen-lockfile      - name: Build        uses: junobuild/juno-action@full        with:          args: functions build      - name: Publish        uses: junobuild/juno-action@full        with:          args: functions publish        env:          JUNO_TOKEN: ${{ secrets.JUNO_TOKEN }}
```

This action will build and publish your serverless function bundle.

If your access key is an **editor**, the changes will be automatically deployed to your Satellite's CDN.

If your key is only a **submitter**, the release will be proposed as a pending change for manual approval. To avoid errors in submit-only workflows, you can explicitly use the `--no-apply` flag to skip auto-application.

```
- name: Publish  uses: junobuild/juno-action@full  with:    args: functions publish --no-apply  env:    JUNO_TOKEN: ${{ secrets.JUNO_TOKEN }}
```

---

## Optimization & Best Practices

Below are key considerations to ensure efficient and cost-effective publication of your functions.

### Triggering on Release

You can adjust the trigger to publish your serverless function only on releases, which helps reduce unnecessary CI runs and deployments.

```
on:  release:    types: [released]
```

This ensures that your function bundle is built and published only when a GitHub release is published.