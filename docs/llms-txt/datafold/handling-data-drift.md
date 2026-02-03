# Source: https://docs.datafold.com/deployment-testing/best-practices/handling-data-drift.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Handling Data Drift

> Ensuring Datafold in CI executes apples-to-apples comparison between staging and production environments.

<Note>
  **Note**

  This section of the docs is only relevant if the data used as inputs during the PR build are inconsistent with the data used as inputs during the last production build. Please contact [support@datafold.com](mailto:support@datafold.com) if you'd like to learn more.
</Note>

## What is data drift in CI?

Datafold is used in CI to illuminate the impact of a pull request's proposed code change by comparing two versions of the data and identifying differences.

**Data drift in CI** happens when those data differences occur due to *changes in upstream data sources*—not because of proposed code changes.

Data drift in CI adds "noise" to your CI testing analysis, making it tricky to tell if data differences are due to new code, or changes in the source data. Unless both versions rely on the same snapshot of upstream data, data drift can compromise your ability to see the true effect of the code changes.

<Tip>
  **Tip**

  dbt users should implement Slim CI in [dbt Core](https://www.datafold.com/blog/taking-your-dbt-ci-pipeline-to-the-next-level) or [dbt Cloud](https://www.datafold.com/blog/slim-ci-the-cost-effective-solution-for-successful-deployments-in-dbt-cloud) to prevent most instances of data drift. Slim CI reduces build time and eliminates most instances of data drift because the CI build depends on upstreams in production due to state deferral. However, Slim CI will not *completely* eliminate data drift in CI, specifically in cases where the model being modified in the PR depends on a source. In those cases, we recommend [**building twice in CI**](/deployment-testing/best-practices/handling-data-drift#build-twice-in-ci).
</Tip>

## Why prevent data drift in CI?

By eliminating data drift entirely, you can be confident that any differences detected in CI are driven only by your code, not unexpected data changes.

You can think of this as similar to a scientific experiment, where the control versus treatment groups ideally exist in identical baseline conditions, with the treatment as the only variable which would cause differential outcomes.

In practice, many organizations do not completely eliminate data drift, and still derive value from automatic data diffing and analysis conducted by Datafold in CI, in spite of minor noise that does exist.

## Handling data drift

We recommend two options for removing data drift to the greatest extent possible:

* [Build twice in CI](#build-twice-in-ci)
* [Build CI data from clone of prod sources](#build-ci-data-from-clone-of-prod-sources)

In both of these approaches, Datafold compares transformations of identical upstream data, so that any detected differences will be due to the code changes alone, ensuring an accurate comparison with no false positives.

By building two versions of the data in CI, you can ensure an "apples-to-apples" comparison that depends on the same version of upstream data.

When deciding between the two, choose the one that best matches your workflow:

| Workflow                                              | Approach                      | Why                                                                                           |
| ----------------------------------------------------- | ----------------------------- | --------------------------------------------------------------------------------------------- |
| Data changes frequently in production                 | Build twice in CI             | Isolates PR impact without waiting on recent production updates, using a consistent snapshot. |
| Production has complex orchestration or multiple jobs | Build CI data from prod clone | Allows a stable comparison by freezing upstream data from a fixed production state.           |
| Performance and speed are critical                    | Build CI data from prod clone | Limits CI build to a single snapshot, reducing the processing load on the pipeline.           |
| Simplified orchestration with minimal dependencies    | Build twice in CI             | Reduces the need to manage production snapshots by running both environments in CI.           |

### Build twice in CI

This method involves two CI builds: one representing PR data, and another representing production data, both based on an identical snapshot of upstream data.

1. Create a fixed snapshot of the upstream data that both builds will use.
2. The CI pipeline executes two builds: one using the PR branch of code, and another using the base branch of code.
3. Datafold compares these two data environments, both created in CI, and detects differences.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-architecture-diagram.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4af6a3be0e9c23b3749718e509b3f685" data-og-width="1600" width="1600" data-og-height="1073" height="1073" data-path="images/deployment_testing/data-drift-architecture-diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-architecture-diagram.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=efb5672ba068149181dd52467eced4a9 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-architecture-diagram.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e16e4dab91e5ab3262259f3cbf6a757e 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-architecture-diagram.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=84776475ba7379451f5c7083f6ef3e85 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-architecture-diagram.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=94e2c2b507e3b053e3ebec23a43a9fdc 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-architecture-diagram.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=448aa14941898078c2f6811b2f848b62 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-architecture-diagram.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a456e60067785874ff9f7c53fffe93c1 2500w" />
</Frame>

<Note>
  If performance is a concern, you can use a reduced or filtered upstream data set to speed up the CI process while still providing rich insight into the data.
</Note>

<Note>
  This method assumes the production build doesn’t involve multiple jobs that process different sets of models at different times.
</Note>

### Build CI data from clone of prod sources

This method involves comparing a CI build based on a snapshot of the upstream source data *from the time of the last production build* to the production version of transformed data.

1. Update orchestration to create and store a snapshot of the upstream source data at the time of the production transformation job.
2. The CI pipeline executes a data transformation build using the PR branch of code, with the snapshotted upstream data as the upstream source.
3. Datafold compares the CI data environment with production data and detects differences.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-solution-clone-of-prod.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=dfb3fea3a072ed93dfd9d1df61e612a7" data-og-width="1600" width="1600" data-og-height="1073" height="1073" data-path="images/deployment_testing/data-drift-solution-clone-of-prod.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-solution-clone-of-prod.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=c3135ad5a87531f0dbfcfb42d8bb0888 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-solution-clone-of-prod.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=3cd32956e685bd09274d50f67b602a33 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-solution-clone-of-prod.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=07b9d676204f1b700433ca859948a5d0 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-solution-clone-of-prod.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=82eb0091dbcddd7a4197eb3624c1a830 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-solution-clone-of-prod.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a5476d1c597ae7efbfcf5b3ec973a690 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/data-drift-solution-clone-of-prod.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=edea7eb9c4fb444a74b30f6d8f129135 2500w" />
</Frame>
