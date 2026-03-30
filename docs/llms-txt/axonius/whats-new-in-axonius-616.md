# Source: https://docs.axonius.com/docs/whats-new-in-axonius-616.md

# What's New in Axonius 6.1.6

#### Release Date: March 17th 2024

These Release Notes contain new features and enhancements added in version 6.1.6.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

The following features were added to all assets pages:

### Query Wizard Enhancements

#### Added Operators for Field Comparison Queries

`>` (Greater than)  and `<` (lesser than) operators are now supported for numeric fields in [Field Comparison queries](/docs/selecting-source-options-in-the-query-wizard#field-comparison).

### New Association Field in Group Asset

The [AD Group Members](/docs/identity-overview#association-fields) field displays the AD users who belong to this group. For each user, the field shows their username, email, Internal User ID, and SID. You can also choose to display just one of these parameters.

## Vulnerability Management  and Software Management Module New Features and Enhancements

The following new features and enhancements were added to the Software Management Module:

**Search**
Search on the **Vulnerabilities**  and **Software** pages and their corresponding Profile pages is now case insensitive.

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Bulk Activate Connections

On the **Adapters Connections** page it is now possible to activate a number of adapter connections at once using the **[Activate](/docs/adapter-connections#activating-adapter-connections)** action.

![ACtivateRN](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ACtivateRN.png)

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Custom Enrichment Management Table

A new [Custom Enrichment Management table](/docs/managing-custom-enrichment) was added to **System Settings> Data> Custom Enrichment Management**. This table shows information on user-generated custom enrichment fields and enables navigating directly from the row of a field to the assets enriched with this field.

![CustomeEnrichmentManagementTableB](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomeEnrichmentManagementTableB.png)

## General Updates

### Login Page Redesign

The Axonius login page has been redesigned with sleek aesthetics, improved functionality, and a more intuitive user experience.

<Image alt="NewLogINRN" width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NewLogINRN.png" />

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

The **[Wizard](/docs/using-the-dynamic-value-statement-wizard)** is now the default tool for configuring **Dynamic Value statements** for an enforcement action. When **Configure Dynamic Values** is enabled in an enforcement action, the **Wizard** tab, which now appears to the left of the **Syntax** tab, opens by default.

![ECWizard](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ECWizard.png)

## Axonius-hosted (SaaS) Deployments New Features and Enhancements

### Rotate Tunnel Certificate

It is now possible to [rotate the the Tunnel Certificate](/docs/manage-tunnels#rotating-the-tunnel-certificate) for security or compliance purposes, or if the system displays a message that your tunnel certificate has expired or is about to expire.