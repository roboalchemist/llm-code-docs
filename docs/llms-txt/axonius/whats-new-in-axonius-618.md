# Source: https://docs.axonius.com/docs/whats-new-in-axonius-618.md

# What's New in Axonius 6.1.8

#### Release Date: March 31st 2024

These Release Notes contain new features and enhancements added in version 6.1.8

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

The following features were added to all assets pages:

### Query Wizard Enhancements

#### WHERE and WHERE NOT Operators

Users can now select WHERE and WHERE NOT operators for child expressions in Asset Entity (ENT) and Complex (OBJ) Queries.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### New SAML Setting: Using ADFS Compatible URLs

The ability has been added to use [ADFS compatible](/docs/saml-based-login-settings#saml-advanced-settings) URLs.

### New System Setting: Session Lifetime Settings

Use [Session Lifetime Settings](/docs/managing-timeout#session-lifetime-settings) to require users to reauthenticate after a specified period of time. A notification can be configured to give users time to save any unsaved work. A notification for an Axonius session in an inactive browser tab can also be configured.

<Image alt="SessionLifetimeSetting.png" width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SessionLifetimeSetting.png" />

## General Updates

### Tunnels and Collectors Rebranding

We're thrilled to initiate a significant transformation by updating the terminology for our fundamental deployment tools – Tunnels and Collectors. This enhancement aims to streamline operations and accurately represent their functionalities.

Tunnels have been renamed  **Gateway Nodes** and Collectors were renamed **Compute Nodes**.
**Gateways** are used to enable fetching from a data source that cannot be reached network wise and are used for hosted customers to access information within their internal organizational network. The **Manage Tunnels** page in **System Configuration** was renamed **Gateways**.
**Compute Nodes** are an Axonius instance that enables horizontal decentralization of the load. Therefore, they can be used for Customer-hosted (on-premise / private cloud) instances when more computing resources are needed. The Instances page was renamed **Manage Nodes**.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Management of Enforcement Sets Scheduling

New [**Turn Scheduling On** and **Turn Scheduling Off** actions](/docs/scheduling-ec-set-runs#managing-scheduling-of-enforcement-sets), available under the **More Actions** menu item: **Manage Scheduling**, enable turning on/off scheduling of one or more Enforcement Sets directly from the Enforcement Sets table.

![SchedulingOFf](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SchedulingOFf.png)

### Manage Custom Enrichment - Enrich Assets with CSV File Enforcement Action

New option added to the [Manage Custom Enrichment - Enrich assets with CSV file enforcement action](/docs/add-enrichment) to write enriched values into  "enriched: field name" under the EC artifacts adapter.

### Enhancements to Axonius Actions

The Enforcement Action required and additional fields now appear under the **Required Fields** and **Additional Fields** tabs.\
![RequiredAdditionalFieldTabs](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RequiredAdditionalFieldTabs.png)

## Findings Center New Features and Enhancements

The following new features and enhancements were added to the Findings Center:

* It is now possible to view muted alerts in the Findings Center - Alerts table, in addition to the already presented unmuted alerts, by toggling off the new **Hide muted alerts** toggle.
* In the Alert drawer of unmuted alerts, a **Related Assets** table has been added with the details of each asset related to the alert. It is also possible to navigate to the Assets page to view these assets.