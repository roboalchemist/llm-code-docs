# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6135.md

# What's New in Axonius 6.1.35

#### Release Date: October 6th 2024

These Release Notes contain new features and enhancements added in version 6.1.35.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

The following features were added to all assets pages:

### View by Use Case on Asset Profile Page

Users can now edit the fields displayed in the Asset Profile Table using the new **Edit Table** button (available from the All Fields view), to display only fields that are relevant to a specific scope or use case. The **Edit Table** menu allows users to add and remove fields from the display, and to create and save new views.

![EditTableonAssetProfle1](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EditTableonAssetProfle1.png)

### Query Wizard Enhancements

#### Build Relationship Queries based on Other Asset Types

Users can now build relationship queries based on other asset type fields selected directly from the Query Wizard not only from an existing saved query.

![UpdatedRelationshipQuery](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-XEQ1NSY9.png)

## Asset Graph New Features and Enhancements

### See the Risk on SaaS Applications

The Asset Graph can now [show the risk level](/docs/viewing-risk-level-for-saas-applications) of SaaS applications. When visible, each node includes a colored risk icon indicating the level of risk.

| Icon                                                                                                                                                            | Risk Level  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| <Image alt="AssetGraph-RiskLow.png" width="40px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetGraph-RiskLow.png" />   | Low risk    |
| <Image alt="AssetGraph-RiskMed.png" width="40px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetGraph-RiskMed.png" />   | Medium risk |
| <Image alt="AssetGraph-RiskHigh.png" width="40px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetGraph-RiskHigh.png" /> | High risk   |

### Redesign of the Explore Relationships Process

The [Explore Relationships](/docs/exploring-connections-and-asset-relationships) drawer has been redesigned to be clearer and easier to use.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Enhancements to Axonius Actions

* In the [Manage Custom Enrichment - Enrich Assets with CSV File](/docs/add-enrichment) enforcement action, the **Show assets that did not meet the criteria under 'additional' instead of 'failed'** option has been added under **Additional Fields**. This option enables users to determine under what category assets that match the Enforcement Set query but do not match the enrichment criteria are placed in the Run History:  **Additional** (enabled) or **Failed** (disabled; the default).

* In the [Axonius - Send Email per Asset](/docs/email-send-per-asset) and [Axonius - Send Email to Assets](/docs/send-email-to-entities) enforcement actions, added the **Secondary Email**  additional field, so that the Enforcement Action has the option of sending the email to a specific email address from a specific adapter, instead of to the user's primary email address, for each user that matches the query.