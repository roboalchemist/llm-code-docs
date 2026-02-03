# Source: https://docs.datadoghq.com/data_observability/quality_monitoring/business_intelligence/powerbi.md

---
title: Power BI
description: >-
  Connect Power BI to Datadog Data Observability to view end-to-end lineage from
  warehouse tables to dashboards.
breadcrumbs: >-
  Docs > Data Observability Overview > Quality Monitoring > Business
  Intelligence Integrations > Power BI
---

# Power BI

## Overview{% #overview %}

Datadog's Power BI integration helps data teams make changes to their data platform without breaking dashboards, and identify unused reports and dashboards to remove. When Datadog connects, it:

- Pulls metadata from your Power BI account like datasets, reports, and dashboards.
- Automatically generates lineage between warehouse tables with downstream datasets, reports, and dashboards.

## Connect Power BI{% #connect-power-bi %}

### Create an app registration and security group{% #create-an-app-registration-and-security-group %}

#### App registration{% #app-registration %}

1. Sign into Microsoft Azure.
1. Search for **App registrations**.
1. Click **New registration**.
1. Fill in the required fields and register an application for Datadog.
1. Copy the Application (client) ID somewhere safe.
1. Go to **Certificates & secrets** in sidebar and click **New client secret**.
1. Add a secret for Datadog.
1. Copy the secret value somewhere safe.

#### Security group{% #security-group %}

1. Search for **Azure Active Directory**.
1. Go to **Groups** in the sidebar and click **New group**.
1. Create a group for the app registration.
1. Click into the newly created group. You may need to refresh the page for it to show up.
1. Go to **Members** in the sidebar and click **Add members**.
1. Find the app registration created earlier and add it as a member.

### Grant access in Power BI{% #grant-access-in-power-bi %}

#### Enable API and admin API access for security group in Power BI Admin{% #enable-api-and-admin-api-access-for-security-group-in-power-bi-admin %}

1. Go to the Power BI Admin portal.
1. In Tenant settings, go to **Developer settings**.
1. Enable **Allow service principals to use Power BI APIs** for your security group.
1. In Tenant settings, find **Admin API settings**.
1. Enable the following for your security group:
   - **Allow service principals to use read-only admin APIs**
   - **Enhance admin APIs responses with detailed metadata**
   - **Enhance admin APIs responses with DAX and mashup expressions**

#### Grant access to workspaces{% #grant-access-to-workspaces %}

From the Power BI Admin portal:

1. From the sidebar, click **Workspaces** to open the Workspaces pane.
1. For each workspace you want Datadog to have access to, open the **Access** panel by clicking the three vertical dots and selecting **Workspace access**.

### Add the Power BI integration{% #add-the-power-bi-integration %}

1. Navigate to the [Power BI integration tile](https://app.datadoghq.com/integrations/power-bi) and enter your tenant ID, and the client ID and secret from earlier.
1. After you've entered these credentials, click **Save**.

## What's next{% #whats-next %}

When your Power BI account is successfully connected, Datadog syncs and automatically derives lineage from warehouse tables/columns to Power BI datasets, reports, and dashboards.

Initial syncs may take up to several hours depending on the size of your Power BI deployment.

After syncing, you can explore your Power BI assets and their upstream dependencies in the [Data Observability Explorer](https://app.datadoghq.com/datasets/catalog).

## Further reading{% #further-reading %}

- [Learn about Data Observability](https://docs.datadoghq.com/data_observability/)
