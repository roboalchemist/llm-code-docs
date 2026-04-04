# Source: https://docs.augmentcode.com/context-services/context-connectors/quickstart/github-actions-indexing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# GitHub Actions Auto-Indexing

> Automatically index your repository on every push using GitHub Actions in 5 minutes

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

## Prerequisites

* A GitHub repository
* Augment API credentials

## Steps

### 1. Create the workflow file

Create `.github/workflows/augment-index.yml` in your repository:

```yaml  theme={null}
name: Index Repository

on:
  push:
    branches:
      - main
  workflow_dispatch:  # Allow manual triggering

jobs:
  index:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Restore index state
        uses: actions/cache@v4
        with:
          path: .augment-index-state
          key: augment-index-${{ github.ref_name }}-${{ github.sha }}
          restore-keys: |
            augment-index-${{ github.ref_name }}-

      - name: Index repository
        run: |
          npx @augmentcode/context-connectors index github \
            --owner ${{ github.repository_owner }} \
            --repo ${{ github.event.repository.name }} \
            --ref ${{ github.sha }} \
            -i ${{ github.repository_owner }}/${{ github.event.repository.name }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          AUGMENT_API_TOKEN: ${{ secrets.AUGMENT_API_TOKEN }}
          AUGMENT_API_URL: ${{ secrets.AUGMENT_API_URL }}
```

### 2. Set up GitHub repository secrets

Go to your repository **Settings → Secrets and variables → Actions** and add:

| Secret Name         | Value                                                              |
| ------------------- | ------------------------------------------------------------------ |
| `AUGMENT_API_TOKEN` | Your Augment API token                                             |
| `AUGMENT_API_URL`   | Your tenant URL (e.g., `https://your-tenant.api.augmentcode.com/`) |

**How to get your credentials:**

```bash  theme={null}
# Login to Augment
auggie login

# Print your credentials
auggie token print
```

This outputs your `accessToken` (use for `AUGMENT_API_TOKEN`) and `tenantURL` (use for `AUGMENT_API_URL`).

### 3. Commit and push

```bash  theme={null}
git add .github/workflows/augment-index.yml
git commit -m "Add Augment indexing workflow"
git push
```

### 4. Verify it's working

Go to your repository's **Actions** tab. You should see the "Index Repository" workflow running.

Once complete, you can search your index:

```bash  theme={null}
export AUGMENT_API_TOKEN='your-token'
export AUGMENT_API_URL='https://your-tenant.api.augmentcode.com/'
npx ctxc search "authentication logic" -i myorg/myrepo
```

## Done!

Your repository will now automatically re-index on every push to the main branch. The workflow uses GitHub Actions cache to store index state for efficient incremental updates.

## Also Works With

| Instead of...     | Try...                                                              |
| ----------------- | ------------------------------------------------------------------- |
| Main branch only  | Edit the workflow to add more branches: `branches: [main, develop]` |
| GitHub cache      | Use S3 storage: add `--store s3` and set `CC_S3_BUCKET` env var     |
| Custom index name | Change the `-i` value to your preferred name                        |

## How It Works

The workflow:

1. **Triggers** on every push to your main branch
2. **Restores** the previous index state from GitHub Actions cache
3. **Indexes** the repository using the GitHub API (no checkout needed for indexing)
4. **Caches** the new index state for the next run

This approach is much faster than full re-indexing on every push.

## Advanced: Using S3 Storage

For production use or team sharing, you can store indexes in S3 instead of GitHub cache:

1. Edit `.github/workflows/augment-index.yml`
2. Add S3 configuration to the command:

```yaml  theme={null}
- name: Index repository
  run: |
    npx @augmentcode/context-connectors index github \
      --owner ${{ github.repository_owner }} \
      --repo ${{ github.event.repository.name }} \
      --ref ${{ github.sha }} \
      -i ${{ github.repository_owner }}/${{ github.event.repository.name }} \
      --store s3
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    AUGMENT_API_TOKEN: ${{ secrets.AUGMENT_API_TOKEN }}
    AUGMENT_API_URL: ${{ secrets.AUGMENT_API_URL }}
    AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
    AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    CC_S3_BUCKET: my-team-indexes
```

3. Add AWS credentials to repository secrets

This allows multiple repositories or team members to share the same index.
