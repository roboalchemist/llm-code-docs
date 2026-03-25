# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6121.md

# What's New in Axonius 6.1.21

#### Release Date: June 30th 2024

These Release Notes contain new features and enhancements added in version 6.1.21.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

### New 'Job Titles' Asset Type

New asset type added: Job Titles.
Job Titles are assets  related to job titles. Fetched by adapters such as Okta.

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Adapter Interface

#### Partially Connected Status

A new 'Partially Connected' status was added for adapter connections. It is displayed in orange. It shows when an  adapter is partially connected, has begun to fetch data, but is not fetching all the assets that it can. The user can click on the adapter connection to see an explanation. This is currently available for specific adapters only.

### CSV for Adapter Fetch History

**Enforcement Actions which Send CSV for Adapter Fetch History Include Selection of Associated Fetch Events**

For Enforcement Sets which send CSV files for Adapter Fetch History, when 'Include Associated fetch events' is selected, details of the associated Fetch Events are included in the CSV file that is created.

## Assets Pages

### EOL/EOS and Latest Version Support for Amazon Linux

[Devices in Axonius](/docs/devices-page#os-end-of-life-end-of-support-and-latest-os-version) now support End of Life, End of Support, Latest Version, and Is Latest Version for the Amazon Linux operating system.