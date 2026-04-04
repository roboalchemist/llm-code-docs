# Source: https://momentic.ai/docs/ci/github-actions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GitHub Actions

The following example shows how to use Momentic with
[GitHub Actions](https://github.com/features/actions).

For more usage examples, see the
[momentic-ai/examples](https://github.com/momentic-ai/examples) repository.

For a given root `package.json`:

```json package.json theme={null}
{
  "name": "my-momentic-repo",
  "scripts": {},
  "devDependencies": {
    "momentic": "latest"
  }
}
```

Create a file called `.github/workflows/ci.yml` in your repository with the
following contents:

```yaml ci.yml theme={null}
name: CI

on:
  push:
    branches: ["main"]
  pull_request:
    types: [opened, synchronize]

jobs:
  build:
    name: Test
    timeout-minutes: 15
    runs-on: ubuntu-latest

    steps:
      - name: Check out code
        uses: actions/checkout@v4
        with:
          fetch-depth: 2

      - name: Setup Node.js environment
        uses: actions/setup-node@v4
        with:
          node-version: 20.19.0
          cache: "npm"

      - name: Install dependencies
        run: npm install

      - name: Install browsers
        run: npx momentic install-browsers --all

      - name: Test
        run: npx momentic run

      - name: Upload results
        if: always()
        run: npx momentic results upload test-results
```

## Authentication

To run any commands, you must authenticate with Momentic. You can do this by
adding the `MOMENTIC_API_KEY` environment variable to your GitHub Actions
workflow.

1. Create an API key in
   [Momentic Cloud](https://app.momentic.ai/settings/api-keys).

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/create-api-key.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=54eb9f3c01e00a3ae7d71996760dcd39" width="3616" height="2434" data-path="images/create-api-key.png" />
</Frame>

Copy the value to a safe place. You'll need it in a moment.

2. Go to your GitHub repository settings and click on the **Secrets** and then
   **Actions** tab. Create a new secret called `MOMENTIC_API_KEY` and enter the
   value of your API key.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/ci/gha-secrets-page.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=1fcc5414a200db0da879f06e92d758a2" width="3636" height="2532" data-path="images/ci/gha-secrets-page.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/ci/gha-new-secret.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=b9c0b0e9e5b2c6d758284b6bb9dc7dac" width="3636" height="2532" data-path="images/ci/gha-new-secret.png" />
</Frame>

3. At the top of your GitHub Actions workflow, provide the following environment
   variables to jobs that use `momentic`:

```yaml ci.yml {8-10} theme={null}
# ...

jobs:
  build:
    name: Build and Test
    timeout-minutes: 15
    runs-on: ubuntu-latest
    # To authenticate, set the following environment variables.
    env:
      MOMENTIC_API_KEY: ${{ secrets.MOMENTIC_API_KEY }}

    steps:
      - name: Check out code
        uses: actions/checkout@v4
        with:
          fetch-depth: 2
    # ...
```

## Sharding

If you have a large test suite, you can use sharding to run tests in parallel.
This can significantly speed up your CI runs.

To shard the test suite, pass the `--shard-index` and `--shard-count` options to
the `momentic run` command. The `shard-index` is the index of the current shard
(starting from 1), and `shard-count` is the total number of shards.

In order to collect test results inside a single run group in Momentic cloud,
you need to add a separate step after all tests complete to merge and upload
results.

```yaml ci.yml theme={null}
name: CI

on:
  push:
    branches: ["main"]
  pull_request:
    types: [opened, synchronize]

jobs:
  run-tests:
    name: Run tests
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        shardIndex: [1, 2]
        shardTotal: [2]
    steps:
      - name: Check out code
        uses: actions/checkout@v4
        with:
          fetch-depth: 2

      - name: Setup Node.js environment
        uses: actions/setup-node@v4
        with:
          node-version: 20.19.0
          cache: "npm"

      - name: Install dependencies
        run: npm install

      - name: Install browsers
        run: npx momentic install-browsers --all

      - name: Test
        run: |
          npx momentic run \
            --output-dir test-results/shard-${{ matrix.shardIndex }} \
            --shard-index ${{ matrix.shardIndex }} \
            --shard-count ${{ matrix.shardTotal }}

      - name: Save test results artifact
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: test-results-${{ matrix.shardIndex }}
          path: ./test-results
          retention-days: 1

  upload-results:
    name: Merge and upload test results
    runs-on: ubuntu-latest
    if: always()
    timeout-minutes: 5
    needs:
      - run-tests

    steps:
      - name: Check out code
        uses: actions/checkout@v4
        with:
          fetch-depth: 2

      - name: Setup Node.js environment
        uses: actions/setup-node@v4
        with:
          node-version: 20.19.0
          cache: "npm"

      - name: Install dependencies
        run: npm install

      - name: Download all test results artifacts
        uses: actions/download-artifact@v4
        with:
          path: ./test-results
          pattern: test-results-*
          merge-multiple: true

      - name: Merge test results
        run: npx momentic results merge --output-dir test-results/merged test-results

      - name: Upload test results to Momentic
        run: npx momentic results upload test-results/merged
```


Built with [Mintlify](https://mintlify.com).