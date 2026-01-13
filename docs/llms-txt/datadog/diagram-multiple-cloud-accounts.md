# Source: https://docs.datadoghq.com/cloudcraft/getting-started/diagram-multiple-cloud-accounts.md

---
title: Diagram Multiple Cloud Accounts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Cloudcraft (Standalone) > Getting started > Diagram Multiple Cloud
  Accounts
source_url: >-
  https://docs.datadoghq.com/getting-started/diagram-multiple-cloud-accounts/index.html
---

# Diagram Multiple Cloud Accounts

Cloudcraft is a tool designed to help visualize and plan cloud architecture in a seamless and efficient manner. This guide explains how to use the legacy experience within Cloudcraft to diagram multiple cloud accounts. Consolidate multiple cloud accounts into a single cohesive diagram with the following steps.

## 1. Enable the legacy experience

To work with multiple cloud accounts, you must enable the legacy diagramming experience:

1. Open Cloudcraft and navigate to the **Live** tab.
1. Locate the **New Live Experience** toggle and ensure it is switched **off**.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/diagram-multiple-cloud-accounts/new-live-experience-toggle.04e27d4d0d9795e0a50d7834c1d9de42.png?auto=format"
   alt="Cloudcraft interface showing new live experience toggle for multiple cloud accounts." /%}

## 2. Layout the first account

After the legacy experience is enabled, lay out the first account:

1. Choose the initial cloud account you want to visualize.
1. Start a scan of this account to gather its current architecture details.
1. Select the **Auto Layout** button to automatically arrange the components of this account within the diagram.

## 3. Layout the second account

After successfully laying out the first account, you can add more accounts into the diagram:

1. Choose the second cloud account you wish to add.
1. Perform a scan of the second account to capture its architecture.
1. Select **Auto Layout**.
1. Access the **Options** dropdown and select **Include existing components.** This action ensures the components from the first account remain visible, integrating both accounts into a single diagram.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/diagram-multiple-cloud-accounts/auto-layout-options.f480b84871701853ae4a2cbb709c4dbd.png?auto=format"
   alt="Cloudcraft interface showing AWS inventory and live component options." /%}

{% alert level="info" %}
You can repeat this process to include more accounts in a diagram.
{% /alert %}

Follow the above steps to have a consolidated view of multiple cloud accounts within one Cloudcraft diagram. Review the layout to ensure all necessary components are included and positioned as desired. Adjust any placements manually if needed to improve clarity or presentation.
