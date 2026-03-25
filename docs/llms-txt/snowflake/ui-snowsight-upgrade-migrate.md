# Source: https://docs.snowflake.com/en/user-guide/ui-snowsight-upgrade-migrate.md

# Upgrading to Snowsight from Classic Console

> **Important:**
>
> With the general enablement of the [2025_06 behavior change bundle](../release-notes/bcr-bundles/2025_06_bundle.md),
> the Snowsight upgrade is complete. All customers are now in Stage 3 (Snowsight Only)
> where Snowsight is the only interface available and Classic Console is no longer accessible.

After your account is upgraded to Snowsight from Classic Console, follow this guide to learn more about Snowsight
and adapt your key workflows.

For all the latest capabilities of Snowsight, see [Snowsight: The Snowflake web interface](ui-snowsight.md). No major new features have been released for Classic Console since April 2022.

## Top questions after upgrading to Snowsight

1. Where are my old worksheets?
2. How do I load data from a file?
3. How do I preview data while writing SQL?
4. How do I see query details from my worksheet?
5. Where is my account info?

### Where are my old worksheets?

Snowsight doesn’t automatically copy the worksheets you had open in Classic Console.

If you don’t see the queries and worksheets that you were running in Classic Console, import your worksheets.

### How do I load data from a file?

In Snowsight, you can load data from a local file or a file on a stage into an existing or new table.

While in a worksheet, you can use the object explorer to load data into an existing table.

You can also navigate to a database schema and create a table from a file.

See [Load data using Snowsight](data-load-web-ui.md) for full details.

### How do I preview data while writing SQL?

If you want to preview the contents of a data table while writing SQL or Snowpark Python in a worksheet, you can use the object explorer:

1. From a worksheet, select Databases in the object explorer. If you don’t see the object explorer, select Open sidebar.
2. Locate the database and schema that contain the table you want to preview, and then select the table.
3. In the table details section that appears, select  (Preview table).

   A data preview opens overlaying your worksheet, displaying a sample of data in the table.

You can also preview the column names and comments of a database table without previewing the data. See [Refer to database object names in worksheets](ui-snowsight-query.md).

### How do I see query details from my worksheet?

After you run a SQL query, when you view the Results, you can select the Query Details to see information about your query,
such as the bytes scanned and the end time.

To review the queries that have been run in the worksheet, as well as the results for those queries, select
(Query history).

For more details, see [View query history](ui-snowsight-query.md). If you open the query details, you open the query profile for the
query. See [Review Query Profile](ui-snowsight-activity.md).

### Where is my account info?

To retrieve your account information, such as to copy the account identifier to sign in to Snowflake CLI, the Snowflake VS Code Extension, or
another connection to Snowflake, you can use the account menu in Snowsight:

1. Open the account selector and review the list of accounts that you previously signed in to.
2. Select View account details.

   The Account Details dialog displays information about the account, including the account identifier and the account URL.

## Import worksheets

You can import your Classic Console SQL worksheets into Snowsight even if you can no longer access the Classic Console.

> **Important:**
>
> Snowsight has a maximum worksheet size of 1 MB, and larger worksheets cannot be imported. See Troubleshoot issues with upgrading to Snowsight.

### Import worksheets from Classic Console into Snowsight Worksheets

To import your Classic Console SQL worksheets into Snowsight Worksheets, follow these steps:

1. Sign in to [Snowsight](ui-snowsight-gs.md).
2. In the navigation menu, select Projects » Worksheets.
3. Select the … more menu at the top right of your worksheet, then select Import Worksheets.
4. In the confirmation dialog, select Import.

Snowflake creates a folder named Import YYYY-MM-DD and places all worksheets from the Classic Console in that folder.

### Import worksheets from Classic Console into Snowsight Workspaces

To import your Classic Console SQL worksheets into Snowsight Workspaces, follow these steps:

1. Sign in to [Snowsight](ui-snowsight-gs.md).
2. In the navigation menu, select Projects » Workspaces.
3. Select the … more menu in the Worksheets pane.
4. Select Import Worksheets from Classic.
5. In the confirmation dialog, select Import.

Snowflake creates a folder named Import YYYY-MM-DD and places all worksheets from the Classic Console in that folder.

## Troubleshoot issues with upgrading to Snowsight

The following scenarios can help you troubleshoot common issues that can occur when upgrading your workflow to Snowsight.

### I can’t access Snowsight

You might need to update network policies and firewall rules to allow Snowflake URLs access to Snowsight.

See [Preparing Private Connectivity for Snowsight](https://community.snowflake.com/s/article/Private-Connectivity-URLs-with-Snowsight-And-Client-Redirect) in Snowflake Community and [Signing in to Snowsight](ui-snowsight-gs.md).

### Some of my worksheets failed to import

Possible causes and resolutions:

Cause:
:   The worksheet is too large. Snowsight has a maximum worksheet size of 1MB and worksheets larger than 1MB fail to import.

Solution:
:   If you still have access to the Classic Console, consider whether you can split large worksheets into smaller worksheets that
    you can organize semantically in one folder, or do something similar.

Cause:
:   The worksheet uses an unsupported file version.

Solution:
:   If you still have access to the Classic Console, manually copy the contents of each worksheet that failed to import to a new
    worksheet in Snowsight.

Cause:
:   The worksheet failed to import and can’t be opened or run.

Solution:
:   If you still have access to the Classic Console, try to open the worksheet in Classic Console and copy the contents into
    a worksheet in Snowsight. If you cannot open the worksheet, contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).

### I don’t want my imported worksheets to be in a folder

To remove a worksheet from a folder, do the following:

1. In Snowsight, open the worksheet.
2. Select the worksheet name, and in the drop-down menu that appears, select Move to and choose the relevant option:

   * Select the name of an existing folder. The current parent folder for the worksheet is not an option to select.
   * Select + New Folder to create a folder and move the worksheet to that folder.
   * Select Remove from Folder to remove the worksheet from the folder.

   The menu closes and the worksheet moves to the new location.

> **Note:**
>
> You can’t move multiple worksheets at the same time. A worksheet can only be in one folder.

### Usage information looks different in Snowsight

Usage information might be different in Snowsight compared with the Classic Console because the
Classic Console has a 2 million row limitation in the query used to calculate usage.

Use Snowsight for accurate usage information. See [Exploring overall cost](cost-exploring-overall.md).

### Pages load slowly and sometimes I see a white screen

Your default warehouse is used to load some pages in Snowsight.
If your warehouse is overloaded, pages like the database object explorer might load slowly or not at all.

You can see which warehouse is used for client-generated tasks in Query History. See [Monitor query activity with Query History](ui-snowsight-activity.md).

## Share feedback about Snowsight

If you have concerns about Snowsight replacing your existing workflow with the Classic Console,
contact your Snowflake account representative.

## Related videos

A Quick Look At The Latest Upgrade To Snowsight
