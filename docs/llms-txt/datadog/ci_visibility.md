# Source: https://docs.datadoghq.com/account_management/billing/ci_visibility.md

---
title: CI Visibility Billing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Account Management > Billing > CI Visibility Billing
source_url: https://docs.datadoghq.com/billing/ci_visibility/index.html
---

# CI Visibility Billing

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

This guide provides a non-exhaustive list of billing considerations for [CI Visibility](https://docs.datadoghq.com/continuous_integration/pipelines).

## Counting committers{% #counting-committers %}

A committer is an active Git contributor, identified by their Git author email address. For billing purposes, a committer is included if they make at least three commits in a given month.

## Billing for commits made by bots or actions performed in the GitHub UI{% #billing-for-commits-made-by-bots-or-actions-performed-in-the-github-ui %}

Commits made by verified bots or through actions performed directly in the GitHub UI are not billed by Datadog. These are automatically excluded from billing calculations. Only verified bots are excluded from billing.

## Excluding commits from specific people{% #excluding-commits-from-specific-people %}

Yes, you can exclude commits from specific people by using [exclusion filters](https://docs.datadoghq.com/continuous_integration/guides/ingestion_control).

## Further Reading{% #further-reading %}

- [Learn about Pipeline Visibility](https://docs.datadoghq.com/continuous_integration/pipelines)
- [Learn about Ingestion Controls for CI Visibility](https://docs.datadoghq.com/continuous_integration/guides/ingestion_control)
