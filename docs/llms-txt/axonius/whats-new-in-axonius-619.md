# Source: https://docs.axonius.com/docs/whats-new-in-axonius-619.md

# What's New in Axonius 6.1.9

#### Release Date: April 7th 2024

These Release Notes contain new features and enhancements added in version 6.1.9.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

The following features were added to all assets pages:

### Query Wizard Enhancements

**Updates to Operators for Date Fields**

* The new [ 'previous weeks' operator](/docs/query-wizard-operators#operators-for-date-fields) queries assets from the selected number of weeks since the previous Monday.

* The 'previous month' operator has been renamed to 'previous months' and allows users to select the number of previous calendar months to compare the value for.

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Adapter Interface

#### Edit Columns on Adapter Fetch History and Adapter Connections Pages

Edit Columns is now available  on the **[Adapters Fetch History](/docs/adapters-fetch-history)** and **[Adapter Connections](/docs/adapter-connections)** Pages.
This means users can add columns to the pages, remove columns, freeze columns display and save their selections as **[Saved Views](/docs/setting-page-columns-display#saved-views)**.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Increased Enforcement Set Run Priority Levels

Available Enforcement Set [run priority levels](/docs/scheduling-ec-set-runs#setting-the-run-priority) have increased from 1-10 to 1-20. All Enforcement Sets scheduled to run every global discovery cycle run in the order of their set priorities - those with priority 1 (highest priority) run first, and those with priority 20 (lowest priority) run last.

### Export Run History to CSV File

It is now possible to export to a CSV file the [Run History table data](/docs/view-ec-set-history#the-run-history-page) of all runs, filtered runs, or a single run, by clicking **Export CSV** above the table on the Run History page.
![EnforcementSetsRunHistory](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EnforcementSetsRunHistory.png)

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

The **[**Dynamic Value statements** Wizard](/docs/using-the-dynamic-value-statement-wizard)** now supports *also*, enabling writing to more than one enforcement action field in a single statement.\
![WizardSwitchCaseNew](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WizardSwitchCaseNew.png)