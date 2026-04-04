# Source: https://docs.datadoghq.com/data_observability/quality_monitoring/business_intelligence/sigma.md

---
title: Sigma
description: >-
  Connect Sigma to Datadog Data Observability to view end-to-end lineage from
  warehouse tables to workbooks.
breadcrumbs: >-
  Docs > Data Observability Overview > Quality Monitoring > Business
  Intelligence Integrations > Sigma
---

# Sigma

## Overview{% #overview %}

Datadog's Sigma integration helps data teams make changes to their data platform without breaking Sigma workbooks, and identify unused workbooks or datasets. When Datadog connects, it:

- Pulls metadata from your Sigma site, including workbooks and queries.
- Automatically generates lineage between warehouse tables and columns and downstream Sigma datasets and workbooks.

## Connect Sigma{% #connect-sigma %}

### Retrieve API keys{% #retrieve-api-keys %}

Follow [Sigma's API client instructions](https://help.sigmacomputing.com/reference/generate-client-credentials) to retrieve a Client ID and Client Secret (also called an API token).

### Add the Sigma integration{% #add-the-sigma-integration %}

1. Navigate to the [Sigma integration tile](https://app.datadoghq.com/integrations/sigma-computing) and enter the following information:

   - Account name
   - Client ID
   - Client secret
   - Cloud provider. If you don't know your cloud provider, you can find it using Sigma's [Supported cloud platforms and regions documentation](https://help.sigmacomputing.com/docs/region-warehouse-and-feature-support#supported-cloud-platforms-and-regions).

1. After you've entered these credentials, click **Save**.

## What's next{% #whats-next %}

When your Sigma account is successfully connected, Datadog syncs and automatically derives lineage from warehouse tables/columns to Sigma workbooks.

Initial syncs may take up to several hours depending on the size of your Sigma deployment.

After syncing, you can explore your Sigma assets and their upstream dependencies in the [Data Observability Explorer](https://app.datadoghq.com/datasets/catalog).

## Further reading{% #further-reading %}

- [Learn about Data Observability](https://docs.datadoghq.com/data_observability/)
