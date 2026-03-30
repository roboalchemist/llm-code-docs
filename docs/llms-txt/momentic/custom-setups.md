# Source: https://momentic.ai/docs/ci/custom-setups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom setups

The following guide contains useful information for using Momentic in custom CI
setups.

## Best practices

Most CI providers set the `CI` environment variable to `true` by default. This
allows Momentic to automatically detect when tests are being run in CI. In
custom setups, this isn't always the case.

We recommend setting the environment variable `CI=true` to enable all CI-related
features by default and more closely mimic standard CI environments.

## Saving caches

By default, Momentic CLI does not save caches for test runs on the configured
git main branch. This is to prevent developers from accidentally polluting those
caches when building tests locally.

In standard CI setups like GitHub Actions, GitLab CI, and Travis CI, Momentic
can automatically infer that tests are being run in a CI environments and
override this behavior to save caches. However, in custom CI setups, you need to
pass the --save-cache flag to the run command in order to enable cache saving.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --save-cache [options] [tests...]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --save-cache [options] [tests...]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --save-cache [options] [tests...]
  ```
</CodeGroup>

<Tip>
  We recommend always saving caches during CI runs in order to ensure optimal
  performance and consistency.
</Tip>

You can read more about caching in Momentic in the [docs](/step-cache).

## Git metadata

Momentic collects git metadata during test runs in order to power several
features:

* Cache isolation
* Test run traceability
* GitHub status messages

And more.

In order to collect this data, Momentic relies on either the git CLI tool or
special handling for specific CI providers. Some custom CI setups may not have
git installed or might have incomplete information.

In order to provide the metadata manually, you can set any combination of the
following environment variables. All of these are optional, but providing more
information will lead to better results.

<Tip>
  In order to get the best caching performance possible, we recommend providing
  at least `GIT_BRANCH_NAME`, `GIT_COMMIT_SHA`, `GIT_COMMIT_TIMESTAMP`,
  `LAST_COMMIT_ON_MAIN_SHA`, `LAST_COMMIT_ON_MAIN_TIMESTAMP`, and if possible
  `MERGED_GIT_BRANCH_NAME`.
</Tip>

* `MOMENTIC_GIT_OVERRIDE=true`: must be set to enable git metadata overrides
* `GIT_COMMIT_SHA`: the full commit SHA
* `GIT_COMMIT_SHA_SHORT`: the short commit SHA (if not provided, this will be
  derived from the full SHA)
* `GIT_COMMIT_TIMESTAMP`: the current commit timestamp in ISO 8601 format
* `GIT_BRANCH_NAME`: the current branch name
* `GIT_ORIGIN_URL`: the git origin URL
* `GIT_COMMIT_AUTHOR_NAME`: the commit author's name
* `GIT_COMMIT_MESSAGE`: the commit message
* `LAST_COMMIT_ON_MAIN_SHA`: the full commit SHA of the last commit on main.
  When using git, this is the output of running `git merge-base main HEAD`. On
  main, this is the current commit SHA.
* `LAST_COMMIT_ON_MAIN_TIMESTAMP`: the commit timestamp of
  `LAST_COMMIT_ON_MAIN_SHA` in ISO 8601 format.
* `MERGED_GIT_BRANCH_NAME`: when on main, the name of the branch that was merged
  to create the current commit. This is usually derived from pull/merge requests
  using our GitHub/GitLab integrations.
* `GITHUB_REPOSITORY`: the GitHub repository name in the format `owner/repo` (if
  applicable)
* `GITLAB_PROJECT_PATH`: the GitLab project path in the format
  `group/subgroup/repo` (if applicable)
* `GIT_USERNAME`: the username of the current git user (if applicable)
* `GIT_EMAIL`: the email of the current git user (if applicable)
* `GIT_NAME`: the name of the current git user (if applicable)


Built with [Mintlify](https://mintlify.com).