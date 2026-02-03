# Source: https://docs.datadoghq.com/database_monitoring/data_collected.md

# Source: https://docs.datadoghq.com/dora_metrics/data_collected.md

# Source: https://docs.datadoghq.com/containers/kubernetes/data_collected.md

# Source: https://docs.datadoghq.com/containers/docker/data_collected.md

# Source: https://docs.datadoghq.com/containers/datadog_operator/data_collected.md

# Source: https://docs.datadoghq.com/containers/amazon_ecs/data_collected.md

# Source: https://docs.datadoghq.com/code_coverage/data_collected.md

---
title: Code Coverage Data Collected
description: >-
  Learn about the data collected by Code Coverage including source code provider
  webhooks, coverage reports, and git metadata.
breadcrumbs: Docs > Code Coverage > Code Coverage Data Collected
---

# Code Coverage Data Collected

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### Join the Preview!

Code Coverage is in Preview. This product replaces Test Optimization's [code coverage](https://docs.datadoghq.com/tests/code_coverage) feature, which is being deprecated. Complete the form to request access for the new Code Coverage product.

[Request Access](http://datadoghq.com/product-preview/code-coverage/)
{% /callout %}

## Source Code Provider Integration{% #source-code-provider-integration %}

The exact data received by Datadog depends on your source code provider type:

{% tab title="GitHub" %}
Code Coverage relies on the following GitHub webhooks:

- Pull request
- Pull request review
- Pull request review comment
- Push

None of the webhooks include your source code content; they only include metadata about the pull request, such as title, description, author, labels, and commit SHAs.

See GitHub's [webhook events and payloads documentation](https://docs.github.com/en/webhooks/webhook-events-and-payloads) for a detailed description of the data sent by these webhooks.
{% /tab %}

{% tab title="Gitlab" %}
Code Coverage relies on Gitlab webhooks. The webhooks do not include your source code content. They only include metadata about the merge request, such as the title, description, author, labels, and commit SHAs.

See Gitlab's [webhook events and payloads documentation](https://docs.gitlab.com/user/project/integrations/webhook_events/) for a detailed description of the data sent by webhooks.
{% /tab %}

{% tab title="Azure DevOps" %}
Code Coverage relies on Azure DevOps webhooks. The webhooks do not include your source code content. They only include metadata about the pull request, such as the title, description, author, labels, and commit SHAs.

See Azure DevOps' [webhook events and payloads documentation](https://learn.microsoft.com/en-us/azure/devops/service-hooks/events?view=azure-devops#git.pullrequest.created) for a detailed description of the data sent by webhooks.
{% /tab %}

By default, when synchronizing your repositories, Datadog doesn't store the actual content of files in your repository, only the Git commit and tree objects.

See [Datadog Source Code Integration](https://docs.datadoghq.com/integrations/guide/source-code-integration) for more information about how Datadog integrates with your source code provider.

## Code Coverage Report Upload{% #code-coverage-report-upload %}

The `datadog-ci coverage upload` command sends the following data to Datadog:

- **Coverage reports**: The report files, which contain the coverage data for your codebase. The data depends on the coverage tool and report format you are using, and normally includes file paths, line numbers, and coverage percentages.
- **Git metadata**: Git repository URL, branch name, commit SHA, timestamp, author information, and list of file paths that were changed in the commit. You can disable Git metadata upload by adding `--skip-git-metadata-upload=1` to the command.
- **Git diff summary**: List of file paths that were changed in the commit, along with the numbers of added and removed lines. You can disable Diff data upload by adding `--upload-git-diff=0` to the command.
- **CI metadata**: Information about the CI environment, such as the CI provider, job ID, and pipeline ID.

No source code is uploaded to Datadog.

## Further reading{% #further-reading %}

- [Code Coverage](https://docs.datadoghq.com/code_coverage)
- [Set up Code Coverage](https://docs.datadoghq.com/code_coverage/setup)
