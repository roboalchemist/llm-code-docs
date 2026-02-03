# Source: https://docs.datadoghq.com/continuous_delivery/features/rollbacks_detection.md

---
title: Rollback Detection
description: Learn how CD Visibility detects deployment rollbacks.
breadcrumbs: >-
  Docs > Continuous Delivery Visibility > CD Visibility Features > Rollback
  Detection
---

# Rollback Detection

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

Knowing when specific deployments are performing a rollback is useful to:

- Understand deployment stability and the frequency of rollbacks across your services.
- Identify patterns in deployment issues that lead to rollbacks.

To detect rollbacks, Datadog compares the current deployment version with the previous versions deployed for the same service and environment. A rollback is identified when both of the following occur:

- The current version is different from the previous version. This ensures that redeploying the same version does not constitute a rollback.
- The current version matches a version that was previously deployed.

You can search for rollback deployments in [Deployment Executions](https://app.datadoghq.com/ci/deployments/executions), using the `@deployment.is_rollback` tag:

{% image
   source="https://datadog-docs.imgix.net/images/continuous_delivery/features/rollbacks-deployment-executions.84c8e64121587602152de74c33f1fdc3.png?auto=format"
   alt="Rollback indicator in Deployment Executions page" /%}

You can also see more detailed information in the event detail:

{% image
   source="https://datadog-docs.imgix.net/images/continuous_delivery/features/rollbacks-detail.a338f3fee546958b77e8cdc6d5e89a6c.png?auto=format"
   alt="Rollback detail" /%}

## Requirements{% #requirements %}

Rollback detection works for deployments that have all of the following:

- A service (`@deployment.service`)
- An environment (`@deployment.env`)
- A version identifier (`@deployment.version`)

### Version for CI-based providers{% #version-for-ci-based-providers %}

For CI-based providers, Datadog uses the `--revision` parameter that you pass to the `datadog ci` command. This parameter should contain the version identifier for your deployment (such as a commit SHA, image tag, or version number).

### Version for Argo CD{% #version-for-argo-cd %}

For Argo CD deployments, Datadog uses the version from correlated images to detect rollbacks. Datadog identifies the "main" image from your deployment and extracts the version tag from it.

To enable rollback detection for Argo CD deployments, you need to correlate your images with commits using the [`datadog-ci deployment correlate-image` command](https://github.com/DataDog/datadog-ci/tree/master/packages/plugin-deployment#correlate) as explained in the [Argo CD monitoring documentation](https://docs.datadoghq.com/continuous_delivery/deployments/argocd#correlate-deployments-with-ci-pipelines).

When images are properly correlated, Datadog populates a version tag from the image metadata, which is then used for rollback detection.

## Further Reading{% #further-reading %}

- [Learn about Deployment Visibility](https://docs.datadoghq.com/continuous_delivery/deployments/)
- [Learn how to query and visualize deployments](https://docs.datadoghq.com/continuous_delivery/explorer)
