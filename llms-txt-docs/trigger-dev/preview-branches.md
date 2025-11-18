# Source: https://trigger.dev/docs/deployment/preview-branches.md

# Preview branches

> Create isolated environments for each branch of your code, allowing you to test changes before merging to production. You can create preview branches manually or automatically from your git branches.

## How to use preview branches

The preview environment is special – you create branches from it. The branches you create live under the preview environment and have all the features you're used to from other environments (like staging or production). That means you can trigger runs, have schedules, test them, use Realtime, etc.

<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-environment-branches.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=1ea48ad7377b6824a293e69044448b53" alt="Preview environment and branches" data-og-width="620" width="620" data-og-height="420" height="420" data-path="deployment/preview-environment-branches.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-environment-branches.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=69369bcd1ab2140a176cc511b15c2a97 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-environment-branches.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=89cfa57faadd32d488631ba089082c2e 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-environment-branches.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=11366f107502a534f4301c76b7e6493d 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-environment-branches.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=f51b933f65ef7dcb24e693185e8142dc 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-environment-branches.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=1c035becc9fb7ae0e75b8171a176d03c 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-environment-branches.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=c5f3be2cf5cd9cc99e18cc5a0f9a0998 2500w" />

We recommend you automatically create a preview branch for each git branch when a Pull Request is opened and then archive it automatically when the PR is merged/closed.

The process to use preview branches looks like this:

1. Create a preview branch
2. Deploy to the preview branch (1+ times)
3. Trigger runs using your Preview API key (`TRIGGER_SECRET_KEY`) and the branch name (`TRIGGER_PREVIEW_BRANCH`).
4. Archive the preview branch when the branch is done.

There are two main ways to do this:

1. Automatically: using GitHub Actions (recommended).
2. Manually: in the dashboard and/or using the CLI.

### Limits on active preview branches

We restrict the number of active preview branches (per project). You can archive a preview branch at any time (automatically or manually) to unlock another slot – or you can upgrade your plan.

Once archived you can still view the dashboard for the branch but you can't trigger or execute runs (or other write operations).

This limit exists because each branch has an independent concurrency limit. For the Cloud product these are the limits:

| Plan  | Active preview branches |
| ----- | ----------------------- |
| Free  | 0                       |
| Hobby | 5                       |
| Pro   | 20 (then paid for more) |

For full details see our [pricing page](https://trigger.dev/pricing).

## Triggering runs and using the SDK

Before we talk about how to deploy to preview branches, one important thing to understand is that you must set the `TRIGGER_PREVIEW_BRANCH` environment variable as well as the `TRIGGER_SECRET_KEY` environment variable.

When deploying to somewhere that supports `process.env` (like Node.js runtimes) you can just set the environment variables:

```bash  theme={null}
TRIGGER_SECRET_KEY="tr_preview_1234567890"
TRIGGER_PREVIEW_BRANCH="your-branch-name"
```

If you're deploying somewhere that doesn't support `process.env` (like some edge runtimes) you can manually configure the SDK:

```ts  theme={null}
import { configure } from "@trigger.dev/sdk";
import { myTask } from "./trigger/myTasks";

configure({
  secretKey: "tr_preview_1234567890", // WARNING: Never actually hardcode your secret key like this
  previewBranch: "your-branch-name",
});

async function triggerTask() {
  await myTask.trigger({ userId: "1234" }); // Trigger a run in your-branch-name
}
```

## Preview branches with GitHub Actions (recommended)

This GitHub Action will:

1. Automatically create a preview branch for your Pull Request (if the branch doesn't already exist).
2. Deploy the preview branch.
3. Archive the preview branch when the Pull Request is merged/closed.

```yml .github/workflows/trigger-preview-branches.yml theme={null}
name: Deploy to Trigger.dev (preview branches)

on:
  pull_request:
    types: [opened, synchronize, reopened, closed]

jobs:
  deploy-preview:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Use Node.js 20.x
        uses: actions/setup-node@v4
        with:
          node-version: "20.x"

      - name: Install dependencies
        run: npm install

      - name: Deploy preview branch
        run: npx trigger.dev@latest deploy --env preview
        env:
          TRIGGER_ACCESS_TOKEN: ${{ secrets.TRIGGER_ACCESS_TOKEN }}
```

For this workflow to work, you need to set the following secrets in your GitHub repository:

* `TRIGGER_ACCESS_TOKEN`: A Trigger.dev personal access token (they start with `tr_pat_`). [Learn how to create one and set it in GitHub](/github-actions#creating-a-personal-access-token).

Notice that the deploy command has `--env preview` at the end. We automatically detect the preview branch from the GitHub actions env var.

You can manually specify the branch using `--branch <branch-name>` in the deploy command, but this isn't required.

## Preview branches with the CLI (manual)

### Deploying a preview branch

Creating and deploying a preview branch manually is easy:

```bash  theme={null}
npx trigger.dev@latest deploy --env preview
```

This will create and deploy a preview branch, automatically detecting the git branch. If for some reason the auto-detection doesn't work it will let you know and tell you do this:

```bash  theme={null}
npx trigger.dev@latest deploy --env preview --branch your-branch-name
```

### Archiving a preview branch

You can manually archive a preview branch with the CLI:

```bash  theme={null}
npx trigger.dev@latest preview archive
```

Again we will try auto-detect the current branch. But you can specify the branch name with `--branch <branch-name>`.

## Creating and archiving preview branches from the dashboard

From the "Preview branches" page you can create a branch:

<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=2f169fe8a12fd5e71c68e72dff38d0ba" alt="Preview branches page" data-og-width="2832" width="2832" data-og-height="2060" height="2060" data-path="deployment/preview-branches.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=d77850e6aabba369b59bb11e49415629 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=c18074538e204e2a8049d3969049d6c9 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=84140227247ee335b6daec14586fc2f8 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=59cdc0dedce739dfbd926cf171029898 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=d0335bb6a3865d7f3e51b5bbc26b7642 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=643a7ea8cea29bec0cf4c3dd5e9b7b9f 2500w" />
<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches-new.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=daac2d1f55ba7ddc7bba83bceb9f65f8" alt="Create preview branch" data-og-width="1196" width="1196" data-og-height="603" height="603" data-path="deployment/preview-branches-new.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches-new.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=72cd18942952158e9ebfcf4a788e653e 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches-new.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=3d166afef618f1e992dfa921dd2a73e5 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches-new.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=f3e9a8814ae6039751aa648dec8b2066 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches-new.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=051c4f7ed376b7e7901debb23142125a 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches-new.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=d241dccbfbbad0d59a165feba6f2ae5d 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches-new.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=c07177baf4a0581142ac55f2213181e5 2500w" />

You can also archive a branch:

<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches-archive.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=1908c37fe8b46c3f942b0caf386094fd" alt="Archive preview branch" data-og-width="2832" width="2832" data-og-height="2060" height="2060" data-path="deployment/preview-branches-archive.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches-archive.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=e1035c51deb29876494525b4317f4fb4 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches-archive.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=a237012a0892cdb9fab4e40a293d1041 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches-archive.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=a809dadcaa8d7903ad34610951721884 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches-archive.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=834c2099f1f7771a793c9ec84717b5fa 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches-archive.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=9cbcbaf8c212805aea80207a731a24d5 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-branches-archive.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=0c65583a0291f776674ff89c21c409ca 2500w" />

## Environment variables

You can set environment variables for "Preview" and they will get applied to all branches (existing and new). You can also set environment variables for a specific branch. If they are set for both then the branch-specific variables will take precedence.

<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-environment-variables.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=dcf6d3db8d2892e68351ddcdd367ac6e" alt="Environment variables" data-og-width="1012" width="1012" data-og-height="586" height="586" data-path="deployment/preview-environment-variables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-environment-variables.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=379f827c4015c9d2fd362267843a84cf 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-environment-variables.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=fa4d754f9946cf09cfeacd065f5eeddb 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-environment-variables.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=ba1f6b354220f2bf3b06ac13be1343f0 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-environment-variables.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=9b3b68749706d0c00978ea6fb4dc7b29 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-environment-variables.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=cb25b22522a78e81bac0b2d06475058d 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/deployment/preview-environment-variables.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=3d088494a88aa0bc8a52775e17448ed6 2500w" />

These can be set manually in the dashboard, or automatically at deploy time using the [syncEnvVars()](/config/extensions/syncEnvVars) or [syncVercelEnvVars()](/config/extensions/syncEnvVars#syncvercelenvvars) build extensions.

### Sync environment variables

Full instructions are in the [syncEnvVars()](/config/extensions/syncEnvVars) documentation.

```ts trigger.config.ts theme={null}
import { defineConfig } from "@trigger.dev/sdk";
// You will need to install the @trigger.dev/build package
import { syncEnvVars } from "@trigger.dev/build/extensions/core";

export default defineConfig({
  //... other config
  build: {
    // This will automatically detect and sync environment variables
    extensions: [
      syncEnvVars(async (ctx) => {
        // You can fetch env variables from a 3rd party service like Infisical, Hashicorp Vault, etc.
        // The ctx.branch will be set if it's a preview deployment.
        return await fetchEnvVars(ctx.environment, ctx.branch);
      }),
    ],
  },
});
```

### Sync Vercel environment variables

You need to set the `VERCEL_ACCESS_TOKEN`, `VERCEL_PROJECT_ID` and `VERCEL_TEAM_ID` environment variables. You can find these in the Vercel dashboard. Full instructions are in the [syncVercelEnvVars()](/config/extensions/syncEnvVars#syncvercelenvvars) documentation.

The extension will automatically detect a preview branch deploy from Vercel and sync the appropriate environment variables.

```ts trigger.config.ts theme={null}
import { defineConfig } from "@trigger.dev/sdk";
// You will need to install the @trigger.dev/build package
import { syncVercelEnvVars } from "@trigger.dev/build/extensions/core";

export default defineConfig({
  //... other config
  build: {
    // This will automatically detect and sync environment variables
    extensions: [syncVercelEnvVars()],
  },
});
```
