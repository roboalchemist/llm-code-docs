# Source: https://developers.cloudflare.com/ai-search/get-started/dashboard/index.md

---

title: Dashboard · Cloudflare AI Search docs
description: Create and configure AI Search using the Cloudflare dashboard.
lastUpdated: 2026-01-19T17:29:33.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/ai-search/get-started/dashboard/
  md: https://developers.cloudflare.com/ai-search/get-started/dashboard/index.md
---

This guide walks you through creating an AI Search instance using the Cloudflare dashboard.

## Prerequisites

AI Search integrates with R2 for storing your data. You must have an active R2 subscription before creating your first AI Search instance.

[Go to **R2 Overview**](https://dash.cloudflare.com/?to=/:account/r2/overview)

## Create an AI Search instance

[Go to **AI Search**](https://dash.cloudflare.com/?to=/:account/ai/ai-search)

1. In the Cloudflare Dashboard, go to **Compute & AI** > **AI Search**.
2. Select **Create**.
3. In **Create a RAG**, select **Get Started**.
4. Choose how you want to connect your [data source](https://developers.cloudflare.com/ai-search/configuration/data-source/).
5. Configure [chunking](https://developers.cloudflare.com/ai-search/configuration/chunking/) and [embedding](https://developers.cloudflare.com/ai-search/configuration/models/) settings for how your content is processed.
6. Configure [retrieval settings](https://developers.cloudflare.com/ai-search/configuration/retrieval-configuration/) for how search results are returned.
7. Name your AI Search instance.
8. Create a [service API token](https://developers.cloudflare.com/ai-search/configuration/service-api-token/).
9. Select **Create**.

## Try it out

Once indexing is complete, you can run your first query. You can check indexing status on the **Overview** tab of your instance.

1. Go to **Compute & AI** > **AI Search**.
2. Select your instance.
3. Select the **Playground** tab.
4. Select **Search with AI** or **Search**.
5. Enter a query to test the response.

## Add to your application

There are multiple ways you can connect AI Search to your application:

[Workers Binding](https://developers.cloudflare.com/ai-search/usage/workers-binding/)Query AI Search directly from your Workers code.

[REST API](https://developers.cloudflare.com/ai-search/usage/rest-api/)Query AI Search using HTTP requests.
