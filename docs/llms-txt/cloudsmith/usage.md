# Source: https://help.cloudsmith.io/docs/usage.md

# Usage

The Client Statistics page shows usage information of all access to your Workspace or Repositories. It includes the next areas:

* Overview of usage
* Delivery Summary
* Package Delivery
* Artifact data

<Image align="center" src="https://files.readme.io/ce8de7d7788e745325c566b91d87c4737f63004209b23e69882ff8a761cd8a68-overview.gif" />

To access this feature, click on **Usage** on the top right corner of your Workspace/Repository Overview page.

### Overview of usage

The total amount accumulated during the **Current Billing Cycle** for:

* Package Delivery.
* Artifact data.
* Packages.
* Container images.
* Open Source delivery.

When applicable, it also includes a comparative (percentage variation) with the previous comparable cycle.

<Image align="center" src="https://files.readme.io/e6d6d8c61fec4810ce4a7cabe7a1a2d2926d1df7e0fa0cfebd2058cc45d8dbdb-overview_usage.png" />

### Delivery Summary

Displays a list of all of the package bandwidth for the selected time scope. The results can be grouped by package or repository, and display the trend compared with the previous comparable time scope.

All of the data available in this chart is sourced from the [Client Logs](./client-logs) feature.\
Click on any of the entries in the list to view its own data in the Client Logs.

<Image align="center" src="https://files.readme.io/5721cbc446da461fa4b3db456668029b9fee51f4d4ab40735890e2bdc222e244-delivery_summary.png" />

### Package Delivery

The "Package Delivery" chart presents data related to package consumption, enabling monitoring and analysis of download trends over defined periods. It displays metrics such as total downloads and bytes transferred, contributing to an understanding of artifact distribution and utilization.

<Image align="center" src="https://files.readme.io/ec1f41a2d5d355d2e018d0bad18ee129c3b5680192460f9472bdbed16a063d42-package_downloads.png" />

This section can be displayed as a chart or a table. In both cases, it displays the same information: package download activity. Users can select various aggregate types, including "Bytes Downloaded Sum" for data transfer volume, or other metrics like download counts.\
Basically, aggregate allows you to decide *how you want to quantify or summarize the package download activity*. Here you can find a detailed list of options available:

* **Bytes Downloaded Average**.
* **Bytes Downloaded Sum**.
* **Unique IP Address Count**.
* **Request Count**.
* **Time Taken** (Avg, Max, P50, P75, P90, P95, P99, Sum).

#### Time Period Selection

* **Period**: Pre-configured options are available for historical data analysis (e.g., "Previous 12 months").
* **Date Selection**: A configurable date range picker (e.g., "10 Jun 2024 - 10 Jun 2025") allows for specific data window definition.
* **Interval**: Data can be viewed by different time intervals, such as "Month" or other available options. In order words, this is the *bucket size for which the "Aggregate" calculation is performed*.

#### Filtering Options

These filters allow you yo refine displayed data based on specific criteria:

* **Package format**: Filters by package type (e.g., npm, Maven, Docker).

* **Repository type**: Filters by repository classification (e.g., private, public).

* **Repository**: Filters data for a specific repository.

* **IP address**: Filters usage originating from specific IP addresses.

* **User type**: Differentiates between user classifications.

* **User**: Filters by individual user download activity.

* **Entitlement token**: Filters usage associated with specific access tokens.

* Other filters available for **plot Configuration**:
  * **Group by**: Allows data aggregation based on selected criteria (e.g., package format, repository).
  * **Plot Type**: Options include "Interval" (data per period) and "Accumulated" (cumulative data).
  * **Scale**: Selection between "Linear" and "Log" scales for data display.

* **Reset Filters**: A "Reset Filters" function is available to restore default filter settings.

#### **Purpose**

This chart serves to provide data for:

* Monitoring bandwidth consumption, and impact on billing.
* Identifying package download frequencies.
* Tracking user-specific download activities, although **Client Logs** might be better suited for this goal.
* Evaluating the impact of different repositories or package formats.
* Reviewing access patterns via entitlement tokens.

### Artifact Data

Total amount of Artifact data stored within the Workspace/Repository.

<Image align="center" src="https://files.readme.io/134d723b3920badb66c4477651e99e64a5f2a4552d8bd83c3e2ab7a41f9d2bc9-artifact_data.png" />

This will increase with time as more artifacts are stored within your Workspace. [Retention Rules](/artifact-management/retention-rules) can help to automate storage management.

## Usage via the CLI

You can query the number of active (has been downloaded) and inactive (has not been downloaded) packages via the Cloudsmith CLI with the `cloudsmith metrics packages` command:

```shell
cloudsmith metrics packages OWNER/REPOSITORY
```

Example:

```shell
cloudsmith metrics packages demo/examples-repo
```

<Image align="center" src="https://files.readme.io/7314f40467961cd097b949cdbf16b620f38a0709314d1c115d2f4d9af3e4a2ef-5b18a8e-metrics-packages.png" />

You can also query package activity during a specific time range using the `--start` and `--finish` parameters and ISO 8601 formatted datetimes.

Example:

```shell
cloudsmith metrics packages demo/examples-repo --start=2019-01-01T00:00:00Z --finish=2019-12-31T00:00:00Z
```

### Specific Packages

You can query one or more specific packages by adding the `--packages` flag with package identifiers as a comma-separated list  (See [Package Identification](/artifact-management/identifying-a-package) for more information).

Example:

```shell
cloudsmith metrics packages demo/examples-repo --packages=ZGCV58VqT8Sl
```