# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6122.md

# What's New in Axonius 6.1.22

#### Release Date: July 7th 2024

These Release Notes contain new features and enhancements added in version 6.1.22.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Vulnerability Management Module New Features and Enhancements

The following new features and enhancements were added to the Vulnerability Management Module:

### Vulnerabilities Exclusion Rules

It is now possible to exclude Vulnerabilities. Users can exclude vulnerabilities  by creating rules about vulnerabilities to be excluded across the system. It is also possible to exclude vulnerabilities only on specific devices. This enables users to prioritize vulnerabilities to see which to handle first, or whether to accept the risk and exclude  them. The Vulnerabilities rules are shown on a new [Exclusion Rules](/docs/vulnerabilities-exclusion-rules) page.

![VulnExclusionRN](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/VulnExclusionRN.png)

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### New Create Enforcement Set Drawer

The [**Create Enforcement Set** drawer](/docs/create-ec-set) is now divided into four tabs: **Select Assets**, **Select Action**, **Select Schedule**, and **Enforcement Set Name**.
![CreateEnforcementSetDrawerNew](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateEnforcementSetDrawerNew.png)

### New Enforcement Action Tile Library

The [Enforcement Action Tile library](/docs/create-ec-set#selecting-the-enforcement-set-action) is now grouped by vendor (based on the action's adapter, except for 'Axonius Utilities'). For each vendor, this now displays the number of actions, and the categories of the actions. It is possible to expand the row of the vendor to see all its actions, grouped by category. The updated '[Enforcement Action Library](/docs/action-library)' page in the documentation reflects this new structure.
The new **Requires Credentials** badge (yellow) appears only if there is no configured adapter connection for the vendor.

In the screen below:

* The **Airtable** vendor has three Enforcement Actions of the category **Manage Users and User Groups**. The down arrow can be clicked to view these three actions.

* The **Amazon Web Services (AWS)** vendor has six Enforcement Actions and is expanded to show the actions grouped by the three categories - **Notify**, **Manage AWS Services**, and **Manage Software**.

![ActionLibraryByVendor](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ActionLibraryByVendor.png)

## SaaS Management New Features and Enhancements

### New SaaS Applications Enrichment Field

The new Total Expenses by Adapter Connection field displays the total spend for each SaaS application, segmented by source. You can click on the amount to view the details on the Expenses page.