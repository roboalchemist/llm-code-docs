# Source: https://docs.datadoghq.com/continuous_integration/guides/ingestion_control.md

---
title: Set Ingestion Control for CI Visibility
description: >-
  Learn how to define condition(s) by which to exclude specific events from
  being processed by CI Visibility.
breadcrumbs: >-
  Docs > Continuous Integration Visibility > CI Visibility Guides > Set
  Ingestion Control for CI Visibility
---

# Set Ingestion Control for CI Visibility

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Exclusion filters provide fine-grained control over your CI Visibility budget by allowing you to define one or more conditions by which to exclude specific events from being processed by Datadog.

### Compatibility{% #compatibility %}

Filters are available for Pipeline Visibility.

## Adding an exclusion filter{% #adding-an-exclusion-filter %}

Exclusion filters are not required for setting up Pipeline Visibility. By default, all data is ingested and processed.

To create filters for your organization, your user account must have the `ci_ingestion_control_write` [permission](https://docs.datadoghq.com/account_management/rbac/permissions/#ci-visibility).

1. In Datadog, navigate to **CI** > **Settings** > **Ingestion Settings**.
1. Select **Add an Exclusion Filter**.

{% image
   source="https://datadog-docs.imgix.net/images/ci/add-ci-exclusion-filter.278705819eee202f50e61c17781dfa5e.png?auto=format"
   alt="Add an Exclusion Filter button" /%}
Name the filter and define a query. After you define a query, the preview above the input fields shows ingested data that matches your query. Once your filter is created and enabled, events like the ones shown in the preview are excluded from ingestion.
{% image
   source="https://datadog-docs.imgix.net/images/ci/exclusion-filter-pipeline.628dc6fde9a38dabdcf42e36fb683d93.png?auto=format"
   alt="Creating an exclusion filter for a specific pipeline" /%}

Once you have added a filter, each row in this page displays:

- **Filter name** - the name of the filter
- **Exclusion query** - the query that was defined for that filter
- Toggle to enable/disable the filter - newly created filters are toggled on by default

All spans matching one or more filters are neither ingested nor processed by Datadog.

## Defining queries for an exclusion filter{% #defining-queries-for-an-exclusion-filter %}

Filters are defined flexibly through a query editor interface. Rely on [tags](https://docs.datadoghq.com/getting_started/tagging/) and attributes to create your filters.

### Example exclusion filters{% #example-exclusion-filters %}

Below are examples of how exclusion filters can help you optimize your CI Visibility usage and billing.

#### Filter by git author email address{% #filter-by-git-author-email-address %}

You can exclude one or more specific committers from being monitored by defining a filter with git author email address (`@git.commit.author.email`). The screenshot below shows a filter in which all spans associated with commits from this particular git author email are not ingested.

{% image
   source="https://datadog-docs.imgix.net/images/ci/exclusion-filter-email.5af098f5ab246d75b1d67ceb630e5b32.png?auto=format"
   alt="Ingestion control exclusion filter for email address" /%}

#### Filter by git author email domain{% #filter-by-git-author-email-domain %}

You can also exclude many committers at once by email domain (for instance, you may want to exclude external contributors committing to monitored repositories). The screenshot below shows a filter in which all spans associated with commits from email address domains that do not match the one in the query are not ingested.

{% image
   source="https://datadog-docs.imgix.net/images/ci/exclusion-filter-domain.a0ddc3f869308ba86eb45b81173a2e17.png?auto=format"
   alt="Ingestion control exclusion filter for email domain" /%}

#### Filter by repository{% #filter-by-repository %}

You can exclude specific repositories from being monitored (for example, an internal testing repository) by defining a filter with repository name (`@git.repository.name`) or ID (`@git.repository.id`). The screenshot below shows a filter in which all spans associated with commits to this repository are not ingested.

{% image
   source="https://datadog-docs.imgix.net/images/ci/exclusion-filter-repo.4104b37a35a17838dc80df93848948d3.png?auto=format"
   alt="Ingestion control exclusion filter for repository" /%}

## Updating exclusion filters{% #updating-exclusion-filters %}

Exclusion filters can be enabled/disabled, updated, and deleted by users with `ci_ingestion_control_write` [permissions](https://docs.datadoghq.com/account_management/rbac/permissions/#ci-visibility). They are applied at the organization level. You can view detailed information about who modified exclusion filters by using Datadog [Audit Trail](https://docs.datadoghq.com/account_management/audit_trail/events/#ci-visibility-events).

### Enabling and disabling filters{% #enabling-and-disabling-filters %}

A toggle on the right hand side of each filter allows you to enable and disable the filter at any time. Newly created filters are toggled on by default.

**Note**: In most scenarios, filters are applied to ingested data within <1 second (p95) of being enabled. However, it is possible that an enabled filter takes up to a few minutes to take effect.

### Updating filters{% #updating-filters %}

You can rename a filter or modify the query for an exclusion filter at any time within the **Ingestion Settings** page.

{% image
   source="https://datadog-docs.imgix.net/images/ci/exclusion-filter-edit.bac66a9b85f535bd56a5026252490b8e.png?auto=format"
   alt="Ingestion control edit exclusion filter button" /%}

### Deleting filters{% #deleting-filters %}

You can delete a filter by clicking on the deletion icon.

{% image
   source="https://datadog-docs.imgix.net/images/ci/exclusion-filter-delete.e7dbcbb13bbb09b27beb825c4e5d94fc.png?auto=format"
   alt="Ingestion control delete exclusion filter button" /%}

## Further reading{% #further-reading %}

- [Streamline your CI testing with Datadog Test Impact Analysis](https://www.datadoghq.com/blog/streamline-ci-testing-with-datadog-intelligent-test-runner/)
- [Learn about Pipeline Visibility](https://docs.datadoghq.com/continuous_integration/pipelines)
