# Source: https://docs.axonius.com/docs/cases-1.md

# Cases

The **Cases** Assets page provides a centralized view of all Cases created in Case Management.
It shows all Cases based on a selected query (shown above the search bar) or all Cases, if no query is chosen.
By presenting Cases as standard Axonius assets, this page enhances your ability to track, monitor, and use Case data across the platform, including in the Action Center, Workflows, and Dashboards.

## Required Permissions

You need permissions for **Cases assets** in order to view this page.

## Opening the Cases Assets

**To open the Cases assets page**

* In the left navigation pane, click the **Assets** icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Asset_Icon\(1\).png).

* From the left-pane, expand **Tickets**, and select **Cases**.

  <Image alt="CaseAssets.png" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CaseAssets(1).png" className="border" />

For each Case, the query results table displays multiple columns.

You can set the columns displayed on the page, and freeze specific columns so that they are not scrolled. Refer to [Setting Page Columns Display](/docs/setting-page-columns-display).

For general information about working with tables, refer to [Working with Tables](https://docs.axonius.com/docs/working-with-tables).

### Case Fields

There are many fields that you can view and query on the Cases page. This includes the following fields:

* **Case ID** - ID number of the Case.

* **Case Title** - The name assigned to the Case.

* **Case Type** - The type of Case.

* **Related Assets: Entity ID** - Complex field that shows assets which triggered the Case.
  * This field displays the IDs of the assets related to the Case.
  * Click an ID to open its asset profile page. For example, if the related asset is of type User, clicking it opens the user's asset profile page.

* **Priority** - The urgency of the Case. P0 is the highest; P4 is the lowest.

* **Due Date** - The date (and optionally, the time) by which all assets in the Case are due to be resolved.

* **Due In** - The number of days until the Due Date, displayed in color if due in 1 to 10 days or overdue. This value is calculated by hours remaining (24 and under = 1 day remaining, 24-48 = 2 days, etc.). Or if the Due Date has passed, displays **Overdue**.

* **Base Query** – The query on which the Case is based. For a Case created by the **Create new case** enforcement action, this is the Enforcement Set query.

* **Assignee** - The user assigned to handle the Case.

* **Status** - Status of the Case.

* **Progress** - The progress of the Case (in percentage). Learn more on [how the case progress is calculated](/docs/viewing-and-editing-case-details#tracking-case-progress).

* **Created On** - The date and time that the Case was created.

* **Query Entity** - The asset type that the Case query runs on.

* **Tags** - Tags associated with the Finding.

## Performing Actions on Case Assets

For single Case actions, hover over the Case and click an action at the end of its row. For bulk actions, select multiple Cases and choose an action from the top of the page. Refer to [Asset Actions](/docs/devices-actions) for details.

The structure of the **Cases** page and navigating it are similar to all the **Assets** pages.
For more details on the different elements and the navigation in the **Cases** page, see [Assets page](/docs/assets-page).

## Creating Queries

Use Queries to gain deeper insights into your Cases. Create granular queries with various filters to easily drill down to Cases that match your required search criteria.
You can create queries using:

* **Query Wizard** (default) - Build queries using the **Query Wizard**,  or in the query bar, select a saved query or write your own.

* **Basic** mode - Create queries by selecting filters.

Both modes allow you to create unique sets of queries tailored to your needs.

Learn more about creating Queries [using the Query Wizard](/docs/query-wizard-and-query-filter#working-with-the-query-wizard) and [Basic mode](/docs/basic-query-mode).

## Viewing a Case Asset Profile

Click an individual asset row in the Cases table to see all its relevant data. To learn more, see [Asset Profile page](/docs/asset-profile-page).

<Image alt="CaseProfilePage.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CaseProfilePage.png" />

* In the Case asset profile page, the **Related Assets** field displays the information of the first asset related to the Case (**Asset Name**, **Entity ID**, and **Asset Type**), followed by `+` and the number of additional related assets. Hover over the number to display the information on the top 10 additional assets.
  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RelatedAssetsList.png)
* To view the **Related Assets** complex field: In the left pane, under **Tables**, click **Related Assets**. Alterntely, click the **Related Assets** link in the Asset Profile.
  * Learn more about the [Related Assets complex field](/docs/asset-profile-page-complex-fields#related-assets).