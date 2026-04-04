# Source: https://docs.datadoghq.com/continuous_delivery/deployments.md

---
title: CD Visibility in Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Continuous Delivery Visibility > CD Visibility in Datadog
---

# CD Visibility in Datadog

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

CD Visibility provides a deployment-first view into your CD health by displaying important metrics and results from your deployments.

## Setup{% #setup %}

- [Argo CD](https://docs.datadoghq.com/continuous_delivery/deployments/argocd)
- [CI Providers (GitLab, Jenkins, CircleCI, and more)](https://docs.datadoghq.com/continuous_delivery/deployments/ciproviders)

{% alert level="info" %}
If you are using a provider that is not supported, [fill out this form to request support](https://docs.google.com/forms/d/e/1FAIpQLSeHpvshBu20v6qqMrAjMpUJrwYpRlaGai1mkAPsPU78hWZOKA/viewform?usp=sf_link).
{% /alert %}

## Use deployment data{% #use-deployment-data %}

When creating a [dashboard](https://app.datadoghq.com/dashboard/lists) or a [notebook](https://app.datadoghq.com/notebook/list), you can use deployment data in your search query, which updates the visualization widget options. For more information, see the [Dashboards](https://docs.datadoghq.com/dashboards) and [Notebooks documentation](https://docs.datadoghq.com/notebooks).

## Share deployment data{% #share-deployment-data %}

You can export your search query to a [saved view](https://docs.datadoghq.com/continuous_delivery/explorer/saved_views) by clicking the **Export** button.

{% image
   source="https://datadog-docs.imgix.net/images/continuous_delivery/explorer/deployment_executions_export.2a58544734a521baa19e2d0b561c3829.png?auto=format"
   alt="Deployment execution results appearing in the CD Visibility Explorer" /%}

## Further reading{% #further-reading %}

- [Learn how to query and visualize deployments](https://docs.datadoghq.com/continuous_delivery/explorer)
- [Learn about CD Visibility Features](https://docs.datadoghq.com/continuous_delivery/features)
