# Source: https://momentic.ai/docs/ci/circleci.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# CircleCI

The following example shows how to use Momentic with
[CircleCI](https://circleci.com/).

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

Create a file called `.circleci/config.yml` in your repository with the
following contents:

```yaml config.yml theme={null}
version: 2.1
orbs:
  node: circleci/node@5.0.2
workflows:
  test:
    jobs:
      - test
jobs:
  test:
    docker:
      - image: cimg/node:lts
    steps:
      - checkout
      - node/install-packages

      - run:
          name: Install browsers
          command: npx momentic install-browsers --all

      - run:
          name: Run Momentic tests
          command: npx momentic run
          when: always

      - run:
          name: Upload results
          command: npx momentic results upload test-results
          when: always
```

## Authentication

To run any commands, you must authenticate with Momentic. You can do this by
setting the `MOMENTIC_API_KEY` environment variable in your CircleCI project
settings.

1. Create an API key in
   [Momentic Cloud](https://app.momentic.ai/settings/api-keys).

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/create-api-key.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=54eb9f3c01e00a3ae7d71996760dcd39" width="3616" height="2434" data-path="images/create-api-key.png" />
</Frame>

Copy the value to a safe place. You'll need it in a moment.

2. Go to your CircleCI project settings and click on the **Environment
   Variables** tab. Create a new secret called `MOMENTIC_API_KEY` and enter the
   value of your API key.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/ci/cci-env-var-page.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=3e83e686070e40d2c8cdd65887f9d5c6" width="3636" height="2532" data-path="images/ci/cci-env-var-page.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/ci/cci-add-env-var.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=07f8fd6de33c0e5468ad36b02f72cbb0" width="3636" height="2532" data-path="images/ci/cci-add-env-var.png" />
</Frame>

3. CircleCI automatically loads environment variables stored in project settings
   into the CI environment. No modifications are necessary for the CI file.

## Sharding

If you have a large test suite, you can use sharding to run tests in parallel.
This can significantly speed up your CI runs.

To shard the test suite, pass the `--shard-index` and `--shard-count` options to
the `momentic run` command. The `shard-index` is the index of the current shard
(starting from 1), and `shard-count` is the total number of shards.

In order to collect test results inside a single run group in Momentic cloud,
you need to add a separate step after all tests complete to merge and upload
results.

```yaml config.yml theme={null}
version: 2.1
orbs:
  node: circleci/node@5.0.2

jobs:
  run-tests:
    parallelism: 2
    executor: node/default
    steps:
      - checkout
      - node/install-packages

      - run:
          name: Install browsers
          command: npx momentic install-browsers --all

      - run:
          name: Run tests
          command: |
            npx momentic run \
              --output-dir test-results/shard-${CIRCLE_NODE_INDEX} \
              --shard-index $(($CIRCLE_NODE_INDEX+1)) \
              --shard-count ${CIRCLE_NODE_TOTAL}

      - store_artifacts:
          when: always
          path: ./test-results

      - persist_to_workspace:
          when: always
          root: .
          paths:
            - test-results

  upload-results:
    executor: node/default
    steps:
      - checkout
      - node/install-packages

      - attach_workspace:
          at: .

      - run:
          name: Merge test results
          command: npx momentic results merge --output-dir test-results/merged test-results

      - run:
          name: Upload test results
          command: npx momentic results upload test-results/merged

workflows:
  test:
    jobs:
      - run-tests
      - upload-results:
          requires:
            - run-tests:
              - success
              - failed
```


Built with [Mintlify](https://mintlify.com).