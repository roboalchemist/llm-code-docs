# Source: https://docs.datadoghq.com/dora_metrics/calculation.md

---
title: DORA Metrics Calculation
description: Learn how DORA metrics are calculated in Datadog.
breadcrumbs: Docs > DORA Metrics > DORA Metrics Calculation
---

# DORA Metrics Calculation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

This page explains how Datadog calculates each of the four key DORA metrics:

- Deployment frequency
- Change lead time
- Change failure rate
- Failed deployment recovery time

## Deployment frequency{% #deployment-frequency %}

Deployment frequency measures how often an organization successfully releases to production. It is calculated based on the count of deployment events over a specific time frame.

## Change lead time{% #change-lead-time %}

Change lead time measures how long it takes a commit to get into production. For a single Git commit, change lead time (CLT) is calculated as the time from the commit's creation to when the deployment including that commit was executed.

To calculate a deployment's change lead time, Datadog runs a `git log` between the deployment's commit SHA and the previous deployment's commit SHA to find all the commits being deployed. Then, it aggregates the related change lead time values for all these commits. Datadog doesn't store the actual content of files in your repository, only Git commit and tree objects.

### Example: Calculating change lead time{% #example-calculating-change-lead-time %}

The following example illustrates how Datadog uses the commit history to calculate a deployment's change lead time.

{% image
   source="https://datadog-docs.imgix.net/images/dora_metrics/git_log_example.9cbb52146b3b562f0cb538c3150ba4f9.png?auto=format"
   alt="An example of a detected rollback deployment" /%}

In the graph above, C is the first commit, followed by C1 and C2. A feature branch is created from C2 with commit C3, then merged back into the main branch with merge commit C4. C4 has two parents: C2 and C3.

The process includes two deployments:

1. The first deployment is created from C1. Because this is the first deployment Datadog observes with Git data, there is no previous deployment to compare against, so change lead time (CLT) is not computed yet.

1. A second deployment is created from C4 and finishes at 7 pm. Datadog calculates CLT for this deployment as follows:

   - Identify the previous deployment commit: C1.
   - Run `git log C1..C4` to find all commits that are reachable from C4 but not from C1. In this example that set is C2, C3, and C4. Remove merge commits from this set, since they do not introduce new code on their own. That leaves C2 and C3.
   - For each remaining commit, compute CLT as `deployment_finished_at - commit_timestamp`:
     - C3: 7 pm - 4 pm = 3 hours
     - C2: 7 pm - 3 pm = 4 hours
   - For this deployment, these values are then aggregated, for example:
     - Average CLT: 3.5 hours
     - Maximum CLT: 4 hours
     - Minimum CLT: 3 hours

At a higher level, DORA metrics in Datadog use the median across deployments. This approach is preferred because it is less sensitive to outliers and gives a more accurate and reliable view of typical performance.

### Recommendations for change lead time{% #recommendations-for-change-lead-time %}

Using commit-level granularity provides a more accurate view of engineering performance. At the deployment level, metrics are calculated as an average of averages, which can obscure key insights. This approach treats all deployments equally, even if one contains one commit and another contains ten, misrepresenting their impact.

### Limitations{% #limitations %}

- Change lead time is not available for the first deployment of a service that includes Git information.
- Change lead time is not available if the most recent deployment of a service was more than 60 days ago.
- The calculation includes a maximum of 5000 commits per deployment.
- When squashing commits to merge pull requests:
  - For GitHub and GitLab: Metrics are emitted for the original commits.
  - For other Git providers: Metrics are emitted for the new commit added to the target branch.
- When rebasing, either manually or to merge pull requests, metrics are calculated using the original commit timestamps, but the SHA shown reflects the newly created rebased commit.

### Change lead time stages{% #change-lead-time-stages %}

Datadog breaks down change lead time into the following fields, which represent the different stages from commit creation to deployment.

**Note**: These fields are measured for every commit and not per deployment or pull request. There are several edge cases depending on the way the commits were introduced to the deployment. For details, see the limitations for change lead time stages.

| Metric             | Description                                                                                                                                                     |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Time to PR Ready` | Time from the commit's creation until the PR is ready for review. This metric is only available for commits made before the PR is marked as ready for review.   |
| `Review Time`      | Time from when the PR is marked ready for review until it receives the last approval. This metric is only available for commits made before the PR is approved. |
| `Merge Time`       | Time from the last approval until the PR is merged.                                                                                                             |
| `Time to Deploy`   | Time from PR merge to start of deployment. If a commit has no associated PR, this metric is calculated as the time from commit creation to start of deployment. |
| `Deploy Time`      | Time from start of deployment to end of deployment. This metric is not available if there is no deployment duration information.                                |

#### Limitations{% #limitations-clt-stages %}

- Change lead time stage breakdown metrics are only available when the source of repository metadata is GitHub or GitLab.
- For most stages, there must be a pull request (PR) associated with a commit. A commit is associated with a PR if the commit is first introduced to the target branch when merging that PR. If a commit has no associated PR, only `Time to Deploy` and `Deploy Time` fields are available.
- When rebasing, either manually or to merge pull requests, the change lead time stage breakdown is unavailable for these commits. This is because rebased commits are not associated with any pull request.

## Change failure rate{% #change-failure-rate %}

Change failure rate measures the percentage of deployments causing a failure in production. It is calculated as:

$$\text"Change Failure Rate" = \text"Number of change failures" / \text"Number of total deployments"$$

A deployment is marked as a change failure through the detection of rollbacks and rollforward deployments. For more information, see the [Change Failure Detection documentation](https://docs.datadoghq.com/dora_metrics/change_failure_detection/).

### Limitations{% #limitations-1 %}

- Rollback detection requires Git metadata (commit SHA) or version tags. Deployments without this metadata cannot be classified as rollbacks.
- Rollforward detection requires PR metadata (titles, labels, or branch names) or version tags. Deployments without this metadata cannot be classified as rollforwards.

## Failed deployment recovery time{% #failed-deployment-recovery-time %}

Failed deployment recovery time measures how long it takes to recover from a failure in production. It is calculated as the duration between the change that resulted in degraded service and its remediation, either through a rollback or rollforward deployment.

### Limitations{% #limitations-2 %}

- For [static rules](https://docs.datadoghq.com/dora_metrics/change_failure_detection/#static-rules), recovery time is calculated between the matched deployment and the immediately preceding deployment.

## Further reading{% #further-reading %}

- [Learn about DORA Metrics](https://docs.datadoghq.com/dora_metrics/)
- [Learn about DORA Metrics Data Collected](https://docs.datadoghq.com/dora_metrics/data_collected/)
- [Set up data sources for DORA Metrics](https://docs.datadoghq.com/dora_metrics/setup/)
