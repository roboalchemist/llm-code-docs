# Source: https://docs.datadoghq.com/continuous_delivery/features/code_changes_detection.md

---
title: Code Changes Detection
description: Learn how CD Visibility detects code changes.
breadcrumbs: >-
  Docs > Continuous Delivery Visibility > CD Visibility Features > Code Changes
  Detection
---

# Code Changes Detection

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### Join the Preview!

CD Visibility is in Preview. If you're interested in this feature, complete the form to request access.

[Request Access](https://docs.google.com/forms/d/e/1FAIpQLScNhFEUOndGHwBennvUp6-XoA9luTc27XBwtSgXhycBVFM9yA/viewform?usp=sf_link)
{% /callout %}

## Overview{% #overview %}

Code Changes Detection allows Datadog to identify the commits introduced as part of a deployment. This is particularly valuable to:

- Understand where specific changes have been deployed, such as tracking when updates reach the `production` environment.
- Diagnose incidents related to a deployment by providing visibility into the exact changes introduced. This helps teams quickly pinpoint potential root causes and accelerate troubleshooting.

To detect the code changes deployed, Datadog runs the [`git log`](https://git-scm.com/docs/git-log) between the current deployment commit SHA and the previous deployment commit SHA. Merge commits are excluded from the computation.

The deployed code changes are visible inside any deployment execution of the [Deployment Executions page](https://app.datadoghq.com/ci/deployments/executions). The **Code Changes** tab shows the previous deployment taken into consideration, and the code changes detected between the two.

{% image
   source="https://datadog-docs.imgix.net/images/continuous_delivery/features/code_changes_tab.bcacbe742c913ca40d6f650698673b42.png?auto=format"
   alt="Code Changes tab for changes detection feature" /%}

Additionally, the **Deployments** column of the [Recent Code Changes](https://app.datadoghq.com/ci/commits) page displays the service and environment details for all deployments that included a specific commit. This view provides a quick way to understand if and where your code changes are deployed. Hovering over the service value reveals whether the deployment has reached all expected environments, based on where the service is typically deployed.

{% image
   source="https://datadog-docs.imgix.net/images/continuous_delivery/features/recent_code_changes_deployments.2545431cfb858a3d1ea9216f5d709129.png?auto=format"
   alt="Showing deployments in Recent Code Changes page" /%}

Code changes are only detected for deployments that:

- Have a service (`@deployment.service`) with file path specs defined in Software Catalog (see the setup instructions for more information).
- Have an environment (`@deployment.env`).
- Have a repository URL (`@deployment.git.repository_url`) and a commit SHA (`@deployment.git.commit.sha`).

## Setup{% #setup %}

To allow Code Changes Detection on your deployments, two steps are required:

1. Synchronize your repository metadata to Datadog.
1. Specify the source code file path for your services.

### Synchronize repository metadata to Datadog{% #synchronize-repository-metadata-to-datadog %}

{% tab title="GitHub" %}

{% alert level="danger" %}
GitHub workflows running the [`pull_request` trigger ](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request)are not supported by the GitHub integration. If you are using the `pull_request` trigger, use the alternative method.
{% /alert %}

If the [GitHub integration](https://docs.datadoghq.com/integrations/github/) is not already installed, install it on the [GitHub integration tile](https://app.datadoghq.com/integrations/github/).

When configuring the GitHub App:

1. Select at least **Read** repository permissions for **Contents** and **Pull Requests**.
1. Subscribe at least to **Push**, **PullRequest** and **PullRequestReview** events.

To confirm that the setup is valid, select your GitHub App in the [GitHub integration tile](https://app.datadoghq.com/integrations/github/) and verify that, in the **Datadog Features** table, the **Pull Request Information** feature is marked as valid.
{% /tab %}

{% tab title="GitLab" %}
Follow the [in-app onboarding](https://app.datadoghq.com/integrations/gitlab-source-code?subPath=configuration) to set up the GitLab Source Code integration.

**Note**: The scope of the service account's personal access token needs to be at least `read_api`.
{% /tab %}

{% tab title="Other Git Providers" %}
You can upload your Git repository metadata with the [`datadog-ci git-metadata upload`](https://github.com/DataDog/datadog-ci/tree/master/packages/base/src/commands/git-metadata) command. When this command is executed, Datadog receives the repository URL, the commit SHA of the current branch, and a list of tracked file paths.

Run this command in CI for every new commit. When a deployment is executed for a specific commit SHA, ensure that the `datadog-ci git-metadata upload` command is run for that commit **before** the deployment event is sent.

{% alert level="danger" %}
Do not provide the `--no-gitsync` option to the `datadog-ci git-metadata upload` command. When that option is included, the commit information is not sent to Datadog and changes are not detected.
{% /alert %}

You can validate the correct setup of the command by checking the command output. An example of a correct output is:

```
Reporting commit 007f7f466e035b052415134600ea899693e7bb34 from repository git@github.com:organization/example-repository.git.
180 tracked file paths will be reported.
â  Handled in 0.077 seconds.
```

{% /tab %}

### Specify service file path patterns{% #specify-service-file-path-patterns %}

To correctly understand the code changes that a deployment has introduced, only the commits affecting the specific service being deployed should be considered.

This can be done in [Software Catalog](https://docs.datadoghq.com/tracing/software_catalog) by specifying, for the interested services, the source code glob file path patterns in the [service definition](https://docs.datadoghq.com/tracing/software_catalog/adding_metadata).

If the service definition contains a **full** GitHub or GitLab URL to the application folder, a single path pattern is automatically used. The link type must be **repo** and the link name must be either "Source" or the name of the service (`shopist` in the examples below).

If your repository contains a single service and you want all directories to be considered for code changes, you may skip this step. If you deploy two or more services from a repository, specifying the source code path patterns is required.

**Example (schema version v2.2):**

{% tab title="GitHub" %}

```yaml
links:
  - name: shopist
    type: repo
    provider: github
    url: https://github.com/organization/example-repository/tree/main/src/apps/shopist
```

{% /tab %}

{% tab title="GitLab" %}

```yaml
links:
  - name: shopist
    type: repo
    provider: gitlab
    url: https://gitlab.com/organization/example-repository/-/tree/main/src/apps/shopist?ref_type=heads
```

{% /tab %}

Code Changes Detection for deployments of the `shopist` service will only consider the Git commits that include changes within the `src/apps/shopist/**` path. You can configure more granular control using either `extensions[datadoghq.com/cd-visibility]` or `extensions[datadoghq.com/dora-metrics]`. If both extensions are detected, `extensions[datadoghq.com/cd-visibility]` is used.

**Example (schema version v2.2):**

```yaml
extensions:
  datadoghq.com/cd-visibility:
    source_patterns:
      - src/apps/shopist/**
      - src/libs/utils/**
```

Code Changes Detection for deployments of the `shopist` service will only consider the Git commits that include changes within the `src/apps/shopist/**` or the `src/libs/utils/**` paths.

If the source code patterns for a service are defined in both a link and an extension, only the extension is considered when filtering the commits.

#### Use service file path patterns to track changes across the entire repository{% #use-service-file-path-patterns-to-track-changes-across-the-entire-repository %}

To detect changes across the entire repository, use appropriate file path patterns. For example, `"**"` matches all files.

**Example (schema version v2.2):**

```yaml
extensions:
  datadoghq.com/cd-visibility:
    source_patterns:
      - "**"
```

In this case, Code Changes Detection for deployments of the `shopist` service will consider the Git commits that include changes in the whole repository tree.

{% alert level="danger" %}
If a pattern is exactly `**` or begins with it, enclose it in quotes, as `*` is reserved in YAML for anchors.
{% /alert %}

## Further Reading{% #further-reading %}

- [Learn about Deployment Visibility](https://docs.datadoghq.com/continuous_delivery/deployments/)
- [Learn how to query and visualize deployments](https://docs.datadoghq.com/continuous_delivery/explorer)
