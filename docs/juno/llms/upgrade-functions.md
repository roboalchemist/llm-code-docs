# Source: https://juno.build/docs/guides/github-actions/upgrade-functions.md

# Upgrade Serverless Functions (Optional)

**Caution:**

We do not recommend upgrading your container directly from CI in **production**. This approach hands over control to automation, which may not be suitable for critical environments. Prefer a change workflow and executing the upgrade with your CLI or in the Console UI.

---

## Configuration

To configure an action to upgrade your Satellite container, follow these steps:

1.  Create an `upgrade.yml` file in the `.github/workflows` subfolder of your repository.
2.  Paste the following code into the file:

*   npm
*   yarn
*   pnpm

.github/workflows/upgrade.yml

```
name: Upgrade Satellite Containeron:  workflow_dispatch:jobs:  upgrade:    runs-on: ubuntu-latest    steps:      - name: Check out the repo        uses: actions/checkout@v4      - uses: actions/setup-node@v4        with:          node-version: 24          registry-url: "https://registry.npmjs.org"      - name: Install Dependencies        run: npm ci      - name: Build        uses: junobuild/juno-action@full        with:          args: functions build      - name: Upgrade        uses: junobuild/juno-action@full        with:          args: functions upgrade        env:          JUNO_TOKEN: ${{ secrets.JUNO_TOKEN }}
```

.github/workflows/upgrade.yml

```
name: Upgrade Satellite Containeron:  workflow_dispatch:jobs:  upgrade:    runs-on: ubuntu-latest    steps:      - name: Check out the repo        uses: actions/checkout@v4      - uses: actions/setup-node@v4        with:          node-version: 24          registry-url: "https://registry.npmjs.org"      - name: Enable Corepack        run: corepack enable      - name: Activate Yarn        run: corepack prepare yarn@1.x --activate      - name: Install Dependencies        run: yarn install --frozen-lockfile      - name: Build        uses: junobuild/juno-action@full        with:          args: functions build      - name: Upgrade        uses: junobuild/juno-action@full        with:          args: functions upgrade        env:          JUNO_TOKEN: ${{ secrets.JUNO_TOKEN }}
```

.github/workflows/upgrade.yml

```
name: Upgrade Satellite Containeron:  workflow_dispatch:jobs:  upgrade:    runs-on: ubuntu-latest    steps:      - name: Check out the repo        uses: actions/checkout@v4      - uses: actions/setup-node@v4        with:          node-version: 24          registry-url: "https://registry.npmjs.org"      - uses: pnpm/action-setup@v4        with:          version: 10      - name: Install Dependencies        run: pnpm i --frozen-lockfile      - name: Build        uses: junobuild/juno-action@full        with:          args: functions build      - name: Upgrade        uses: junobuild/juno-action@full        with:          args: functions upgrade        env:          JUNO_TOKEN: ${{ secrets.JUNO_TOKEN }}
```