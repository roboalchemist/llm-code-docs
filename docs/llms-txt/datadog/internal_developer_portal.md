# Source: https://docs.datadoghq.com/internal_developer_portal.md

---
title: Internal Developer Portal
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Internal Developer Portal
---

# Internal Developer Portal

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% video
   url="https://datadog-docs.imgix.net/images/tracing/internal_developer_portal/scrolling_the_catalog.mp4" /%}

## Overview{% #overview %}

Creating an IDP is a critical part of [Platform Engineering](https://www.datadoghq.com/knowledge-center/platform-engineering/) best practices. Datadog's Internal Developer Portal (IDP) is a fully managed solution that unifies live telemetry, metadata, and self-service workflows to standardize and accelerate software delivery and optimize developer experience.

- Powered by live telemetry, [Software Catalog](https://docs.datadoghq.com/internal_developer_portal/software_catalog) inventories every service and environment in real time and enriches each entry with descriptive metadata for ownership and operational context.
- [Self-Service Actions](https://docs.datadoghq.com/internal_developer_portal/self_service_actions) and [Scorecards](https://docs.datadoghq.com/internal_developer_portal/scorecards) translate platform policies into one-click tasks, ensuring every change meets observability, security, and production criteria.
- Built-in [Engineering Reports](https://docs.datadoghq.com/internal_developer_portal/eng_reports) give platform engineers and leaders real-time visibility into software quality, standards adoption, and developer experience, making it easy to identify gaps and drive data-backed decisions.

If you're new to IDP, start with the [Getting Started guide](https://docs.datadoghq.com/getting_started/internal_developer_portal/), which walks through setup and basic usage.

{% callout %}
##### Sign up for early access to our upcoming features!



[Request Access](https://www.datadoghq.com/product-preview/idp-preview-features/)
{% /callout %}

## Common use cases{% #common-use-cases %}

- [Accelerate developer onboarding](https://docs.datadoghq.com/internal_developer_portal/use_cases/dev_onboarding)
- [Improve incident response](https://docs.datadoghq.com/internal_developer_portal/use_cases/incident_response)
- [Manage and map dependencies](https://docs.datadoghq.com/internal_developer_portal/use_cases/dependency_management)
- [Evaluate production readiness](https://docs.datadoghq.com/internal_developer_portal/use_cases/production_readiness)

## Main features{% #main-features %}

- [Centralize observability, ownership, and engineering knowledge with Software Catalog](https://docs.datadoghq.com/internal_developer_portal/software_catalog)
- [Promote engineering best practices at scale with Scorecards](https://docs.datadoghq.com/internal_developer_portal/scorecards)
- [Accelerate releases through Self-Service Actions](https://docs.datadoghq.com/internal_developer_portal/self_service_actions)
- [Track reliability and scorecard compliance with Engineering Reports](https://docs.datadoghq.com/internal_developer_portal/eng_reports)
- [Monitor external dependencies with External Provider Status](https://docs.datadoghq.com/internal_developer_portal/external_provider_status)

## Working with teams{% #working-with-teams %}

Use [Datadog Teams](https://docs.datadoghq.com/account_management/teams/) to enable team-based features in IDP:

- Track your teams in Datadog and automatically sync with your external sources of truth
- Assign teams as owners of services and other entities
- Create [hierarchies](https://docs.datadoghq.com/account_management/teams/manage/#subteams-hierarchical-teams) to have parent-child relationships between your teams
- Filter views by teams throughout IDP (for example, in Software Catalog, Scorecards, and Engineering Reports)

If your organization manages team structure in GitHub, use GitHub Integration for Teams to automatically sync GitHub teams to Datadog.

## Further reading{% #further-reading %}

- [Turn feedback into action across your engineering org with Datadog Forms](https://www.datadoghq.com/blog/datadog-forms)
- [Exploring IDP in Datadog](https://app.datadoghq.com/idp/get-started)
- [Getting Started with Internal Developer Portal](https://docs.datadoghq.com/getting_started/internal_developer_portal/)
- [Improve developer experience and collaboration with Software Catalog](https://www.datadoghq.com/blog/software-catalog)
- [Prioritize and promote service observability best practices with Service Scorecards](https://www.datadoghq.com/blog/service-scorecards)
- [Empower your engineering teams with Self-Service Actions in Datadog Software Catalog](https://www.datadoghq.com/blog/software-catalog-self-service-actions)
- [How Datadog's Infrastructure team manages internal deployments using the Service Catalog and CI/CD Visibility](https://www.datadoghq.com/blog/how-datadog-manages-internal-deployments/)
- [Ship software quickly and confidently with Datadog IDP](https://www.datadoghq.com/blog/internal-developer-portal/)
- [Sync your Backstage catalog with Datadog IDP](https://www.datadoghq.com/blog/datadog-backstage-plugin/)
- [Coordinate large-scale engineering initiatives with IDP Campaigns](https://www.datadoghq.com/blog/idp-campaigns/)
