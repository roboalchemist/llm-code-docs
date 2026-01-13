# Source: https://docs.datadoghq.com/continuous_integration/explorer/saved_views.md

# Source: https://docs.datadoghq.com/continuous_delivery/explorer/saved_views.md

---
title: Saved Views
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Delivery Visibility > Explore CD Visibility Deployments >
  Saved Views
source_url: https://docs.datadoghq.com/explorer/saved_views/index.html
---

# Saved Views

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

Saved views allow you to save the state of the [Deployment Executions page](https://app.datadoghq.com/ci/deployments/executions) and enable effective troubleshooting by providing you with access to scoped queries, relevant facets, visualization options, and the time range.

Saved views can keep track of your:

- Deployment results and environment data
- Search queries (such as failed deployment executions with a specific CD provider, failing deployment executions in a given environment by their deployment status, deployment executions that required rollbacks, and deployment IDs or URLs)
- Live time range (such as the past hour or the past week)
- Visualizations (such as a timeseries, top list, table, or list)

You can also use saved views to share common queries and configurations with your teammates.

## Saved views{% #saved-views %}

To access your saved views, expand **> Views** to the left in the [Deployment Executions page](https://app.datadoghq.com/ci/deployments/executions).

All saved views except for the default view are shared across the organization, including custom saved views created by users. These are editable by anyone in your organization and display the user's avatar who created the view. Click **Save** to create a custom saved view from the current content in your Explorer.

{% alert level="info" %}
Update, rename, and delete actions are disabled for read-only users.
{% /alert %}

{% image
   source="https://datadog-docs.imgix.net/images/continuous_delivery/explorer/saved_view.da00fa6fd762e6e3a7313ae3fee535c0.png?auto=format"
   alt="Default view in the CD Visibility Explorer" /%}

You can:

- Load or reload a saved view
- Update a saved view with the current view's configuration
- Rename or delete a saved view
- Share a saved view through a short link
- Favorite a saved view to add it to your Saved Views list accessible in the navigation menu

{% alert level="info" %}
Update, rename, and delete actions are disabled for read-only users.
{% /alert %}

## Default views{% #default-views %}

You can set a saved view to be your default landing page in the [Deployment Executions page](https://app.datadoghq.com/ci/deployments/executions). Default views are set per user and have no impact on your organization.

{% image
   source="https://datadog-docs.imgix.net/images/continuous_delivery/explorer/default_view.6dac8370d043d36f1907518e61aa88a5.png?auto=format"
   alt="Default view in the CD Visibility Explorer" /%}

Temporarily override your default saved view by completing an action in the UI or opening links in the Explorer that embeds a different configuration.

In the default view entry in the **Views** panel, you can:

- Click on the entry to reload your default view
- Update your default view with the current parameters
- Reset your default view back to the default setting for a fresh restart

## Further reading{% #further-reading %}

- [Learn how to create a search query](https://docs.datadoghq.com/continuous_delivery/explorer/search_syntax/)
