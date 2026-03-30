# Source: https://momentic.ai/docs/ci/gitlab-ci.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GitLab CI

The following example shows how to use Momentic with
[GitLab CI](https://docs.gitlab.com/runner/).

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

Create a file called `gitlab-ci.yml` in your repository with the following
contents:

```yaml gitlab-ci.yml theme={null}
image: node:latest
stages:
  - build
build:
  stage: build
  script:
    - npm install
    - npx momentic install-browsers --all
    - npx momentic run
  after_script:
    - npx momentic results upload test-results
```

## Authentication

To run any commands, you must authenticate with Momentic. You can do this by
adding the `MOMENTIC_API_KEY` environment variable to your GitLab CI workflow.

1. Create an API key in
   [Momentic Cloud](https://app.momentic.ai/settings/api-keys).

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/create-api-key.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=54eb9f3c01e00a3ae7d71996760dcd39" width="3616" height="2434" data-path="images/create-api-key.png" />
</Frame>

Copy the value to a safe place. You'll need it in a moment.

2. Go to your GitLab repository settings and click on the **Settings** and then
   **CI/CD** tab. Create a new variable called `MOMENTIC_API_KEY` and enter the
   value of your API key.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/ci/gitlab-variables.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=cd56ac4ac202c7a8c2d4080f4a5bda2b" width="1920" height="1089" data-path="images/ci/gitlab-variables.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/ci/gitlab-add-variable.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=26a03b39ff2e7faed136332f39ff040f" width="1920" height="1100" data-path="images/ci/gitlab-add-variable.png" />
</Frame>

3. GitLab CI automatically loads environment variables stored in project
   settings into the CI environment. No modifications are necessary for the CI
   file.

## Sharding

If you have a large test suite, you can use sharding to run tests in parallel.
This can significantly speed up your CI runs.

To shard the test suite, pass the `--shard-index` and `--shard-count` options to
the `momentic run` command. The `shard-index` is the index of the current shard
(starting from 1), and `shard-count` is the total number of shards.

In order to collect test results inside a single run group in Momentic cloud,
you need to add a separate step after all tests complete to merge and upload
results.

```yaml gitlab-ci.yml theme={null}
image: node:latest
stages:
  - test
  - merge-results

test:
  stage: test
  script:
    - npm install
    - npx momentic install-browsers --all
    - npx momentic run --shard-index=$CI_NODE_INDEX --shard-count=$CI_NODE_TOTAL --output-dir test-results/shard-$CI_NODE_INDEX
  parallel: 2
  artifacts:
    paths:
      - test-results
    expire_in: 12 hours
    when: always

merge-results:
  stage: merge-results
  when: always
  dependencies:
    - test
  script:
    - npm install
    - npx momentic results merge --output-dir test-results/merged test-results
    - npx momentic results upload test-results/merged
```


Built with [Mintlify](https://mintlify.com).