# Source: https://docs.snowflake.com/en/release-notes/bcr-bundles/un-bundled/unbundled-behavior-changes-implemented-archive.md

# Archived implemented unbundled behavior changes

Archived implemented unbundled behavior changes are unbundled behavior changes with an implementation date older than two years.
Snowflake periodically moves older but still relevant implemented unbundled behavior changes to this page.

For more information about unarchived BCRs, see:

* [Recently implemented changes](unbundled-behavior-changes.md) that were previously pending/disabled, were not part of a behavior change bundle, and cannot be disabled.
* [Upcoming pending changes](unbundled-behavior-changes.md) that will not be part of a behavior change bundle and cannot be enabled in advance.
* [Canceled behavior changes](unbundled-cancelled-behavior-changes.md) that have been removed from BCR bundles and will not be implemented.

If you have questions about any of these behavior changes, please feel free to contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).

## Archived implemented behavior changes

The following table lists behavior changes that were implemented but archived after a certain period of time, typically two years.

| Release Date | Functional Area | Implemented Behavior Change | Additional Notes |
| --- | --- | --- | --- |
| **Nov 30, 2023** | Snowflake Native App Framework | [Snowflake Native App Framework: Need to recreate or update some APPLICATION objects](bcr-update-app-dev-mode.md) |  |
| **Nov 14, 2023** | Snowflake Native App Framework | [Snowflake Native App Framework: Providers must accept terms of service to set the DISTRIBUTION property to EXTERNAL](bcr-enforce-provider-tos.md) |  |
| **Nov 14, 2023** | Snowflake Native App Framework | [Snowflake Native App Framework Changes to the version output for the SHOW APPLICATIONS and DESC APPLICATION commands](bcr-add-unversioned-status.md) |  |
| **Nov 7, 2023** | Snowflake Native App Framework | [Snowflake Native App Framework Cannot use “UNVERSIONED” as the prefix of a version label](bcr-prevent-unversioned-in-version-name.md) |  |
| **October 23, 2023** | SQL Changes — Usage Views & Information Schema Views / Table Functions | [WAREHOUSE_EVENTS_HISTORY view: Change to the CLUSTER_NUMBER column output](bcr-warehouse-events-history-cluster-number.md) |  |
| **Sep 28, 2023** | Data Loading and Unloading | [Stronger UTF-8 validation for external files](bcr-1013-1014.md) |  |
| **Sep 19, 2023** | SQL Changes — Commands & Functions | [SHOW APPLICATIONS command: Changes to the LABEL column output](bcr-show-applications-output-change.md) | This change is enabled by default and cannot be disabled. |
| **Aug 23, 2023** | SQL Changes — Security | [CREATE USER command: NETWORK_POLICY parameter must specify a valid network policy](bcr-non-existing-network-policy.md) |  |
| **Sep 27, 2022** | Snowflake CLI, Connectors, Drivers, and SQL API Changes | [Snowflake Connector for Python: Empty results of fetch_arrow and fetch_pandas are typed](bcr-812.md) |  |
| **Aug 24, 2022** | Snowflake CLI, Connectors, Drivers, and SQL API Changes | [Snowflake .NET driver update - August 2022](dot-net-driver-relnotes.md) | Snowflake .NET driver 2.0.16: Replaces .NET Standard 2.0 with .NET 6.0 |
| **2021 and 2022** | Infrastructure Changes | [Microsoft Azure subnet expansion (Pending for selected accounts)](bcr-MSAzure-2021-11-29.md) | This change only impacts accounts hosted on Azure that are using the functionality documented in the provided article. |
