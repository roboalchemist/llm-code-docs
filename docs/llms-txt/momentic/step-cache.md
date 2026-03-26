# Source: https://momentic.ai/docs/step-cache.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Step caching

> How Momentic uses caching to improve test performance

This page describes the behavior of step caches. For more information about
module caching or persisting auth state, see
[the module docs](/modules#caching).

Momentic improves test performance by caching element data. Most steps run in
milliseconds by avoiding repeated AI lookups, while still maintaining accuracy.

## How caching works

Caching is automatically applied to most interactive steps such as
[Click](/steps/click) and [Type](/steps/type). When these steps are executed,
Momentic stores contextual information about the targeted element, including:

* CSS selectors and HTML attributes.
* Accessibility roles and metadata.
* Screenshots and visual cues.
* Element location and dimensions.

This allows Momentic to reuse known element data across test runs instead of
re-identifying it every time.

Momentic will bust the existing cache if the target element changes
significantly or if the templated description is different than what was cached.

Caches are only ever saved on successful test runs. Additionally, the test run
must be **eligible** for cache saving (see below).

## Cache saving eligibility

<Info>A test run is always eligible if the `--save-cache` flag is passed.</Info>

* If the test is running in a CI environment, the test is eligible for cache
  saving. This is defined by the environment variable `CI` being set to `true`.
* If the test is not running in a CI environment, caches are saved when running
  on a branch **not configured** as a main branch or protected branch. These
  branches are specified in the
  [project configuration](/cli/configuration#gitmainbranch).

## Where caching is never applied

* Steps like [AI check](/steps/ai-check) or [AI extract](/steps/ai-extract)
  which rely on dynamic evaluation.
* Steps with variables that have continuously changing values (e.g.
  `CLICK the {{ Date.now() }} timer`).

## Disabling cache

<Warning>
  Disabling cache may drastically increase test duration and non-determinism.
</Warning>

You can disable caching globally by passing the `--disable-cache` flag when
running tests:

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --disable-cache
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --disable-cache
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --disable-cache
  ```
</CodeGroup>

You can disable caching on a per-step basis in the step options. This is useful
when the target element is dynamic and changes between test runs (e.g., "last
item in list")

## How cache keys are generated

Cache keys are based on:

* The step's unique ID.
* IDs of any parent modules.
* The resolved element description.
* Dynamic template values (e.g., `{{ env.USERNAME }}`).

If any of these inputs change, the cache is invalidated and regenerated.

## Storage and expiration

Cache is:

* Securely stored on Momentic Cloud.
* Isolated per organization and only accessible during authenticated test runs.
* Automatically expired after 90 days of inactivity.

## Failed steps and caching

Cache is only created when a step **successfully** executes. Failed steps do not
generate or store cache entries.

## Git-based caching

In order to ensure that tests continue to run smoothly while engineers are
making changes concurrently, caches are isolated by git branch when possible:

* For the main branch (configured in `momentic.config.yaml`), caches are stored
  for each commit. This allows new branches to seed their caches from main.
* For non-main branches, only the latest caches are stored.
* When a new branch is created based off of main, its caches will be seeded with
  the latest values before the merge base commit.
* When a feature branch is merged into the main branch, the caches from the
  merged branch and the previous commit on main are combined it order to ensure
  consistency with both previous runs on the main branch as well as checks that
  passed in that branch's CI.


Built with [Mintlify](https://mintlify.com).