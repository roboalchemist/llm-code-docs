# Source: https://docs.axonius.com/docs/whats-new-axonius-50.md

# What's New in Axonius 5.0

#### Release Date: May-14-2023

Axonius version 5.0 includes all features and enhancements from the previous 4.8 incremental releases since version 4.8.1. Read the release notes to learn what's new.

## Release Highlights

* [Dashboard Templates](/docs/whats-new-axonius-50#dashboard-templates)
* [Data Analytics](/docs/whats-new-axonius-50#new-data-analytics-page)
* [New Asset Profile Page](/docs/whats-new-axonius-50#new-asset-profile-page)
* [Software Management Module Add-On](/docs/whats-new-axonius-50#software-management-module-addon)
* [Data Scopes](/docs/whats-new-axonius-50#data-scopes)

## Ongoing Updates

Check out ongoing updates to Version 5.0:

* [ What's New in Axonius 5.0.1](/docs/whats-new-in-axonius501)

* [What's New in Axonius 5.0.2](/docs/whats-new-in-axonius-502)

* [What's New in Axonius 5.0.3](/docs/whats-new-in-axonius-503)

* [What's New in Axonius 5.0.5](/docs/whats-new-in-axonius-505)

* [What's New in Axonius 5.0.6](/docs/whats-new-in-axonius-506)

* [Axonius 5.0 Ongoing Adapter and Enforcement Action Updates](/docs/axonius-50-adapter-and-enforcement-action-updates).

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards.

### Dashboard Templates

Axonius now provides a set of preconfigured [Dashboard templates](/docs/using-dashboard-templates). The templates cover the most common role-based scenarios in order to provide you with relevant insights about your environment quickly. They're also intended to give you quick access to the data you need.

A template is a Dashboard that contains a group of useful charts around a common theme. The charts in the Dashboard were built based on Axonius customers' wide ranging experiences with Dashboards, including common interests and the most likely data included in charts.

The charts are preconfigured with saved queries. Once the appropriate adapters are connected and a Discovery Cycle is run, the charts will display system information.

The following sets of templates  are available:

* Visibility and Trends
* Vulnerabilities Management
* Cloud Environment Insights
* Compliance and Risk
* Remote Workforce

### Dashboard Enhancements

* Select which Dashboards to view and set default setups
* Updated and enhanced System Lifecycle Chart
* Text Widget
* Timeline Charts - support week / month aggregations

#### Spaces are Now Called Dashboards

Dashboard Spaces have been renamed to Dashboards throughout the Axonius Cybersecurity Asset Management product, providing greater consistency throughout the product.

#### Select Which Dashboards to View and Configure Default Setups

* Capability was added to [select which Dashboards](/docs/selecting-dashboards) to view. You can also set the order of the Dashboard tabs and configure a user default setup. Admins can configure a default setup for all users of a Data Scope.

<Image alt="NEWManageDashboards.png" width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NEWManageDashboards.png" />

### System Lifecycle Chart Updated

The [System Lifecycle Chart](/docs/system-lifecycle-chart) was updated to show all  discovery stages. In addition, the chart has direct links from the relevant stages to the **Activity Log**, **Adapter Fetch History**,  and  **Enforcement Run History** pages. A new **Discovery Log**  chart shows the last five Discovery Cycles. An arrow next to any of the Discovery Cycles shows all  the phases of that cycle. It is possible to click **Activity Log**  or **Adapters Fetch History** to open those pages filtered by the cycle.

![Lifecycle for RN](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Lifecycle%20for%20RN.png)

#### New Text Only Tile

Capability was added to create a Dashboard tile that displays a [text](/docs/text-only) only message. This allows you to display a label or message to all users of the Dashboard and to explain the purpose of a Dashboard in a clear and meaningful way.

#### Data Aggregation by Week or Month on Timeline Charts

The capability was added to show data on a [timeline chart](/docs/query-timeline-chart), aggregated by week or month to show the average of the unique results per day in the respective periods.
![TimelineChart - AggregateDWM.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TimelineChart%20-%20AggregateDWM.png)

#### Field Summary Chart Supports Vulnerabilities Queries

* The [**Field Summary**](/docs/field-summary-chart) chart now supports vulnerabilities queries. Timeline view is not supported.

#### Hiding the Total Asset Count

Capability was added to [hide the total asset count](/docs/hiding-ttl-asset-cnt) in the following chart types:

* Field Segmentation - Bars
* Comparison - Bars
* Matrix - Bars

This enables users to see a more accurate asset count in certain circumstances.

![HideTotalAssetCount.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HideTotalAssetCount.png)

#### More Dashboard Enhancements

**Enable Timeline Cache**

* The history of timeline graphs is now saved in cache so it isn't calculated every Discovery Cycle. This makes subsequent calculations faster.

**Unlimited Query Time Range**

* Added the capability to query over an unlimited time range.

**Using the Total CVE Count Field in Dashboard Queries**

* The Total CVE Count field is now supported in Dashboard queries

**Import/Export of Dashboards for Systems with Data Scopes Enabled**

* It is now possible for systems with Data Scopes enabled to [import and export Dashboards](/docs/importing-and-exporting-dashboards).

## New Data Analytics Page

Users can now perform advanced calculations, aggregations, and calculate statistics on raw data (query results) from Axonius, without having to export data to external tools. The new [Data Analytics](/docs/analyzing-query-data) page allows users to view query results and create a pivot table for easier analysis.

Users can:

* Create pivot tables
* Create aggregations
* Perform statistical calculations
* Save data for further analysis
* Include data analysis in reports to share with management
* Apply conditional formatting

![DataAnalyticsRN](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DataAnalyticsRN.png)

## Devices and Users Page New Features and Enhancements

The following new features and enhancements were added to the **Devices** and **Users** pages.

### New Asset Profile Page

A new **[Asset Profile](/docs/asset-profile-page)** page was added to the system. This replaces the current  Adapter Connections tab and the Aggregated tab on the  Device/User Profile pages. The information from Adapter Connections and the Aggregated data are shown together on the new **Asset Profile** page.
The new **Asset Profile** page presents all of the information about fields on an asset in a clear way, in one place. Asset data is better organized, consolidated, and searchable, resulting in greater ease of use, less effort, and greater clarity

![AssetProfilePage1](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetProfilePage1.png)

A new side panel shows all the fields on an asset, under **All Fields**, and also *Aggregated*  fields and *Preferred* fields.  Users can search for any field.

The **Tags** table was moved to the side panel and shows all of the tags placed on the asset. A new **[Tables](/docs/asset-profile-page-complex-fields)** tab shows a default list of complex fields for assets. Users can pin any field presented as a table  (fields for which a name is displayed as a blue link in the main table) to this new table folder. It will be displayed whenever the customer opens this asset. It is also possible for customers to unpin fields  they do not want to display. A new **Profile ID** shows information about the asset (user or device) in a very clear way.

Documentation for this new section, as well for other items connected to assets, can be found under the  new **Working with Asset Pages** section on the Documentation site.

### Asset  Custom Fields Redesign

* **Add Custom Fields** on the **Devices** and **Users** **Profile** pages was renamed **Manage Asset Custom Fields**.
* The [**Manage Asset Custom Fields**](/docs/devices-actions#add-custom-field)**Add Custom Fields** dialog was redesigned to be easier to use.
* You can now select the field type when adding custom fields.

![ManageAssetCustomFieldsOld](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageAssetCustomFieldsOld.png)

### Inline Edit of Custom Data Fields from Asset Pages

[**Custom fields**](/docs/working-with-custom-data) on assets can now be edited directly from the asset tables without having to use [Manage Custom Fields](/docs/device-profile-page#managing-custom-fields) on the Asset Profile pages.

<Image alt="CustomField-InlineEdit.png" width="250px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomField-InlineEdit.png" />

## Assets Pages

The following features were added to all assets pages:

### Searching for an Existing Enforcement Set to Run on an Asset

Users can now easily and quickly find a predefined Enforcement Set to run on one or more selected assets on an assets page, from the dialog that opens when selecting the **Actions** menu option - **[Enforce> Use Existing Enforcement](/docs/devices-actions#enforce-use-existing-enforcement)**.

* A search capability has been added so that users can search for an Enforcement Set by its name (partial or whole). This search capability is particularly useful and time-saving when users have many Enforcement Sets defined in the system.
* The list of existing Enforcement Sets is now in descending order of the date they were created (i.e., newest to oldest). If users know when a particular Enforcement Set was created, finding it takes less time.

  ### Quick Tag and Custom Data Actions on Query Results

Users can now quickly create Enforcement Sets to periodically assign [Custom Fields](/docs/working-with-custom-data#adding-custom-fields-to-query-or-filter-results-with-a-quick-enforcement-action) or [Tags](/docs/working-with-tags#adding-tags-to-query-or-filter-results-with-a-quick-enforcement-action) to all  assets matching a query directly from the asset page. The new **EC Actions** menu is displayed once you start creating a query.

![ECQuick](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ECQuick.png)

### Create Ticket

It is now possible to [create a ticket/incident](/docs/devices-actions#create-ticket) in a third-party ticketing system directly from an assets table. This shortcut enables users to create an Enforcement Set of the **Create Incident or Ticket** category for a single or several assets (of the same type) in just one click directly from the asset **Actions** menu without having to open it in the Enforcement Center. Using this shortcut saves time and effort.

![NewMenuRN](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NewMenuRN.png)

### Copy Button for Multiple Values

It is now possible to copy values in fields that contain a list of values.

### Query Wizard Enhancements

* **Field Comparison Supports Aggregated ‘Last Seen’ and ‘First Seen’ fields**
  * In Field Comparison queries, the capability to use the aggregated ‘Last Seen’ and ‘First Seen’ fields to compare  ‘Last Seen’ or ‘First Seen’ with other date fields was added (For example, aggregated ‘Last Seen’ compared to ‘Last Seen’ from a specific adapter).

* **in (plain text)**

  * An option to use an **[in (plain text)](/docs/adding-multiple-values-to-query-expression#in-plain-text)** operator was added to the Query Wizard. This allows adding lists of items directly into the operator field in the Query Wizard. This is useful if you need to enter more than 2000 values.

* **Data Scope Name**

  * It is now possible to choose more than one Data Scope name in the Query Wizard in order to create queries on a number of Data Scope names (for customers who have this feature enabled).

* **Enhancement to OS: Distribution field**

  * Enhancement to OS: Distribution field  to support comparison of iOS distribution with the `<` and `>` operators. This adds the capability to query on devices with an iOS older or newer than a specific version.

* **Enhancement to Query Wizard Text Box**

  * In some cases, when the Query Wizard text box was too narrow, the complete title of long queries was not displayed. This has been remediated and titles are displayed on mouse over.

* **New CVE Severity Fields**

  * The following new fields,  **Total CVE Count by Severity**, were added to the Query Wizard:

    * Total Critical CVE Count
    * Total High CVE Count
    * Total Medium CVE Count
    * Total Low CVE Count

  The data in these fields is based on an Axonius static analysis. These fields can be used in Dashboard charts.

## Vulnerability Management Module New Features and Enhancements

The following new features and enhancements were added to the Vulnerability Management Module

### Using Vulnerabilities Queries in Enforcement Actions

The [Vulnerability Management Module](/docs/vulnerabilities) now supports automatic Enforcement Actions, enabling users to perform a wide range of automated activities. Among the examples  are:

* Ability to allocate actions to teams using tags
* Notification  by email of newly found critical vulnerabilities
* Capability to automatically create tickets to handle vulnerability remediation

The following [Enforcement Center Actions](/docs) can be used with vulnerability queries.

* [Axonius - Push System Notification](/docs/push-system-notification)
* [Axonius - Send Email](/docs/send-email)
* [Email - Send per Asset](/docs/email-send-per-asset)
* [Axonius - Add Custom Data to Assets](/docs/add-custom-data)
* [Axonius - Remove Custom Data from Assets](/docs/remove-custom-data)
* [Axonius - Add Tag](/docs/add-remove-tag)
* [Axonius - Remove Tag](/docs/add-remove-tag)
* [Cherwell  - Create Incident](/docs/create-cherwell-incident)
* [Cherwell - Create Incident per Asset](/docs/create-cherwell-incident-per-entity)
* [Freshservice - Create Ticket](/docs/create-freshservice-ticket)
* [Freshservice - Create Ticket per Asset](/docs/create-fresh-service-ticket-per-entity)
* [Jira - Create Issue](/docs/create-jira-issue)
* [Jira - Create Issue per Asset](/docs/create-jira-issue-per-entity)
* [Jira Service Management - Create Issue](/docs/create-jira-service-desk-ticket)
* [Jira Service Management - Create Issue per Asset ](/docs/create-jira-service-desk-incident-per-entity)
* [ServiceNow - Create Incident](/docs/create-servicenow-incident)
* [ServiceNow - Create Incident per Asset](/docs/create-servicenow-incident-per-entity)

### Support of Custom Data

It is now possible to add **Custom Data** to **Vulnerabilities** using the **[Actions](/docs/vulnerabilities#adding-custom-data-to-vulnerabilities)** menu. In addition,  **Axonius - Add Custom Data to Assets** and **Axonius - Remove Custom Data from Assets** are supported.

![VulnerabilitesAddCustomData](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/VulnerabilitesAddCustomData.png)

### Historical Snapshot

It is now possible to select a date for which vulnerability data will be displayed, using a new date picker on the [Vulnerabilities](/docs/vulnerabilities#displaying-historical-data) page.

## Software Management Module Add-On

The Software Management Module delivers a complete software inventory, contextualized with device, user, and vulnerability associations.
It enables users to:

* Gain a single unified view for all software from all sources across all devices - a credible, comprehensive distribution.
* Discover specific software and potential software gaps using Software Query.
* Categorize software - Authorized/Unauthorized (via Tags).
* Software utilization tracking - Identify over/under usage (via Device Counts).

![SWManagementV5](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SWManagementV5.png)

To learn all about the capabilities of the Software Management Module, refer to:

* [Software](/docs/software)

* [Software Profile](/docs/software-profile)

## Query Management New Features and Enhancements

The following new features and enhancements were added to the Queries.

### Archive Saved Queries

Added the capability to [move saved queries to an archive folder](/docs/managing-queries-folders#archiving-saved-queries). Once a query is in the **Archive**  folder, users will no longer be able to choose it when they create new charts, Enforcement Actions, reports, or other queries. However, it will continue to work correctly in existing charts, actions, reports, and other queries.

### Create Enforcement Sets from Saved Queries Page

The capability was added to be able to create an Enforcement Action directly from the **Action** menu of the [**Queries** page](/docs/managing-queries#creating-an-enforcement-action).

### Duplicate Query Enhancement

When duplicating a query it is now possible to configure whether the query is private or public.

## Reports  New Features and Enhancements

The following enhancements were added to reports.

### Custom Page Header for Reports

Capability was added to configure a [text header](/docs/configuring-user-interface-settings) that will appear on all report pages.

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters.

### Adapter Interface

* **Adapter Fetch Status**

**Adapter Fetch Status** was added to the **[Adapter Connections](/docs/adapter-connections)** page. This shows the status of the last fetch as displayed on the **Adapter Fetch History** page.  It is also possible to filter by this value.

* **Last Successful Fetch**
  * On the **[Adapter Connections](/docs/adapter-connections)** page a new **Last Successful Fetch** column  was added. This shows the time and date of the last successful fetch for that connection.
* **Export Adapter Connections to CSV**

You can export the **[Adapter Connections](/docs/adapter-connections#exporting-adapter-connections-to-csv)** table to a CSV file.

* **Installed Version**

Data about the Axonius product version that is installed (operational) at the time of a fetch was added to the **[Adapter Fetch History](/docs/adapters-fetch-history)** page to improve understanding of variances between fetches at different times.

* **Notes**

Added the capability to add notes to adapter connections on the [Adapter Configuration](/docs/adding-a-new-adapter-connection#setting-adapter-connection-parameters) page. Notes that are added are displayed on the [Adapter Connections](/docs/adapter-connections) page and can be searched for using a new notes search box.

* **Last Connection Update**

**Last Connection Update** Column was added to the **[Adapters Fetch History](/docs/adapters-fetch-history)** page. This shows if the adapter or the connection configuration were updated since the last fetch. If a change was made, a link in this column opens the **Activity  Log** page filtered to the change.

* **Exclude Devices with IPv6 Range from Fetch**

Capability was added to exclude a device within one or more comma-separated [IPv6 address ranges from the fetch](/docs/advanced-settings#exclude-devices-within-ip-ranges-ipv4-and-ipv6).

### Ingestion Rule Updates

* **Two new operators are now supported:**
  * **Field Starts With**  (field\_starts\_with )  - Checks whether the value from the value of one field in an entity starts with the value of another field in that entity.

  * **Field Not Starts** With ( field\_not\_starts\_with)  - Checks whether the value from the value of one field in an entity  does not start  with the value of another field in that entity.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings.

### New System Settings

The [Axonius System Settings ](/docs/using-the-system-settings-page) was completely redesigned to make it easier and faster to use. The new Settings also offer better visibility and control.
New features include:

* New *Search* for all system settings, titles, and field names.
* Organization of settings into more categories and sub-categories in a logical way that exposes all categories and configurations so they can be found even when they are toggled off.
* Easy to find and always visible *Save* button at the bottom of all pages.
* A warning if the user leaves a page without saving changes.

![NewSettingsdRN](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NewSettingsdRN.png)

### Added User Interface Settings

The following settings have been added.

#### Custom Company Logo for Emails

It is now possible to add a company logo as a header and footer of emails sent by the Enforcement Center. The feature is enabled from the [**System Settings> GUI> UI**](/docs/configuring-user-interface-settings) page.
Branding emails with a company logo significantly increases the likelihood that recipients open these emails, as they often question the validity of emails without a company logo and treat them as spam.

#### Custom Page Header for Reports

Capability was added to configure a [text header](/docs/configuring-user-interface-settings) that will appear in all report pages.

#### Manage Custom Fields and Tags

* **Affected Assets**

  * The capability was added to click the number of **Affected Assets** to see a list of assets with their details for [**Custom  Fields**](/docs/managing-custom-fields) and [**Tags**](/docs/managing-tags).

* **Manage Custom Fields for Vulnerabilities**
  * It is now possible to manage **Custom Fields** for **Vulnerabilities** from the **[Manage Custom Fields](/docs/managing-custom-fields)** settings page.

* **Custom Fields: Select One from a List of Specified Values**
  The capability has been added that allows Admin users to [create custom fields](/docs/managing-custom-fields) with a fixed list of values. The user can then select one of those values when using the field.

<Image alt="CreateCustomField-SingleSelect.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateCustomField-SingleSelect.png" />

* **Edit Single Select Custom Fields**
  * It is also possible to  edit values of *Single Select* custom fields in the Management table on the  **[System Settings `>` Data `>` Custom Data and Tags](/docs/managing-custom-fields-and-tags#editing-a-single-select-custom-field)** page, using a new  **Edit** action from the **Actions** menu. This includes modifying, deleting, and adding values of a custom field.

#### Click Studios Passwordstate

Added **Click Studios Passwordstate** as a new option to the Password Manager field under the [Enterprise Password Management Settings](/docs/managing-external-passwords#click-studios-passwordstate) section.
The integration between Axonius and Click Studios Passwordstate enables Axonius to securely pull privileged credentials from Click Studios Passwordstate. The integration helps to ensure that privileged credentials are secured in Click Studios Passwordstate, rotated to meet company guidelines, and meet complexity requirements.

**Tunnel Support Added to CyberArk Vault**

* Added capability to select tunnel through which to connect to the CyberArk Vault under Enterprise Password Management Settings.

### Data Scopes

For users who have this feature enabled:

* **Create a Dynamic Data Scope per Login**
  * You can configure a dynamic Data Scope for a user based on their login credentials.

* **Move between Data Scopes**

  * Admin users can now specify roles that are authorized to [move between scopes](/docs/switch-data-scopes).

* **Data Scopes: Assign Authorized Data Scopes to Users**

  * When adding a user, Admin [users](/docs/manage-users) can specify the data scopes to which the user is authorized to connect.

  <Image alt="ManageRoles-AuthorizedDataScopes.png" width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageRoles-AuthorizedDataScopes.png" />

### Identity Provider Settings

* **LDAP Login: Prioritize Logon Name**

  * Capability was added to select which [LDAP username field](/docs/ldap-login-settings) should have priority, CN or sAMAccountName, when both are present. You can also select to only use one of the LDAP username fields.

  <Image alt="PrioritizeLoginName.png" width="300px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PrioritizeLoginName.png" />

### New Permissions

* A new  **Manage Tunnels**  permission was added.

## Cloud Asset Compliance New Features and Enhancements

The following updates were made to [Axonius Cloud Asset Compliance](/docs/cloud-asset-compliance-page):

### Data Scopes: Exclude Data from Cloud Provider Accounts

Capability was added to exclude data from selected cloud provider accounts when [creating a Data Scope](/docs/data-scope-management). You can exclude as many cloud accounts as necessary.

<Image alt="ExcludeCloudAccountsfromScope.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExcludeCloudAccountsfromScope.png" />

## General Updates

### User Interface

In the framework of ongoing updates and improvements to the Axonius user interface, the position of some of the buttons in the system were slightly moved to improve the user experience. Please note the following changes:

* **Save** and **Cancel** on charts are now at the bottom of the page.
* **EC Advanced options`-`View Runs** and **Delete Enforcement** were moved to the top of the page.

#### Drag and Drop for Table Columns

It is now possible to change the order of columns in tables in the system by dragging and dropping the column from the table itself. This is available for all tables in the system (in addition to asset tables, you can also use this for all adapter connection tables, activity logs, etc). The changes in column positioning are only permanent on pages which allow saving of column order using **Edit Columns**.

#### Create New Asset

It is now possible to [manually create assets](/docs/manually-creating-an-asset) based on custom data. This allows you to create your own assets with your own data. This is useful in the case there are assets which have “one-off” characteristics Once created, these assets are exactly the same as any other asset in the system.

<Image alt="CreateNewAssetDialog.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateNewAssetDialog.png" />

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Legacy Enforcement Center Deprecation

The **Enforcement Center** was redesigned and new capabilities were added in version 4.8.0. Both the new **Enforcement Center** and the legacy Enforcement Center were available in parallel from Version 4.8.0. As of version 5.0 the legacy Enforcement Center is now deprecated and no longer available.

### Enhancements to the Enforcement Set Drawer

The following enhancements were made to the [Enforcement Set drawer](/docs/creating-new-enforcement-sets):

* Added capability to display Enforcements in a list view in the Enforcement Set drawer.
* Enforcement Actions are divided into their categories with **Recently Used** at the top of the list.

<Image alt="CreateNewECSet-ListView.png" height="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateNewECSet-ListView.png" />

### Run Enforcement Set on First X Number of Assets

* Added capability to run Enforcement Action on [top X assets](/docs/scheduling-ec-set-runs) matching the query.

<Image alt="ECSetRunOnTopXAssets.png" width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ECSetRunOnTopXAssets.png" />

### Wait Until Cycle Ends

It is now possible to schedule an Enforcement Set to run at the end of each discovery cycle by selecting the **wait until cycle ends** option in the [Scheduling section](/docs/scheduling-ec-set-runs) of the Enforcement Set drawer (when **Set scheduling** is toggled on). This means that all Enforcement Sets with this option enabled, and which started while the cycle is running, run at the end of the cycle.

### Enhancements to the Enforcements List

The following enhancements were made to the [Enforcements list](/docs/using-the-ec-page):

* Added the Folder Path column
* You can filter Enforcement Runs by Run Duration and Discovery Cycle
* Added the Next Run column to the Enforcements list
* Sorting the Enforcements list alphabetically is now case insensitive

### Return to the Enforcement Center from the Run Drawer

* A link was added to the title bar of the [Run drawer](/docs/view-ec-set-history) to go to the Enforcement Center.

![RunDrawerReturnToEC.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RunDrawerReturnToEC.png)

### View Assets from which Tags or Custom Data were Removed

Added the capability to remove existing tags or custom data from [assets that were not returned](/docs/view-ec-set-history#viewing-detailed-run-information-and-the-enforcement-set-configuration) by the selected query in the Enforcement Action. These assets can be viewed in the list of affected assets - **Additional**.

![ECRunHistory-AdditionalCustomData.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ECRunHistory-AdditionalCustomData-noRed.png)

### Condition Statement  Updates

The following updates were made to the condition statement functionality.

**New Condition Statement Functions**

* Added the "less than" and "greater than"[functions](/docs/using-functions-and-keywords) for switch statements.

  `switch lt()`

  `switch gt()`

* Added the ability to compare the case against a field value.

  `switch count ([field])`

* You can use the [**field\_exists** operator](/docs/using-functions-and-keywords) to test whether a field exists and set its value to the specified value.

### Enhancements to Axonius Actions

* **Remove Values from Custom Data**
  * In the [**Axonius - Remove Custom Data from Assets**](/docs/remove-custom-data) action  it is now possible to remove values from assets not returned by the query.
* **Axonius - Send Email**
  \*The [**Axonius - Send Email action**](/docs/send-email) action was completely redesigned to create a more readable and customizable email. The changes include the capability to select which fields to include in the email and the number of rows of data to include.

#### Manage Custom Enrichment - Enrich assets with CSV file

* **Custom Enrichment: Custom Fields are Supported**
  * You can now use custom fields when [defining custom enrichments](/docs/custom-enrichment), both in the Custom Enrichment configuration and in the [Custom Enrichment Enforcement Action](/docs/add-enrichment). The **Custom Enrichment - Enrich assets with CSV file** Enforcement Action adds powerful scheduling and customization capabilities to Custom Enrichment.
* **Manage Custom Enrichment - Remove custom enrichment**

  * It is now possible to use this [action](/docs/add-enrichment) to remove custom enrichments from all assets returned by the query selected.

## New Adapters

The following new adapters were added to this release:

* [**Adobe Acrobat Sign**](/docs/adobe-acrobat-sign)
  * Adobe Acrobat Sign allows users to create, edit, collaborate, e-sign, and share PDFs, on any device. (Fetches: Users)

* [**Airtable Enterprise**](/docs/airtable-enterprise)
  * Airtable Enterprise is a spreadsheet-database hybrid serving as a low-code platform for building collaborative apps. (Fetches: Users)

* [**AssetSonar**](/docs/asset-sonar)
  * AssetSonar maintains, tracks, and manages a single source of truth for the IT asset landscape. (Fetches: Devices)

* [**BOSSDesk**](/docs/boss-desk)
  * BOSSDesk is an IT Service Management and Help Desk Software for both On-Premise and in the Cloud. (Fetches: Devices)

* [**Bricata**](/docs/bricata)
  * Bricata is a network detection and response platform. (Fetches: Devices)

* **[Brivo](/docs/brivo)**
  * Brivo is a cloud-based access control solution that helps protect building, employees, visitors, customers, residents and data.  (Fetches: Devices)

* [**CheckPoint Harmony Mobile**](/docs/checkpoint-harmony-mobile)
  * CheckPoint Harmony Mobile uses file protection capabilities to block the download of malicious files to mobile devices and prevent file-based cyberattacks on organizations.  (Fetches: Devices)

* [**Cisco Industrial Network Director (IND)**](/docs/cisco-industrial-network-director)
  * Cisco Industrial Network Director (IND) enables deployment and monitoring of Cisco Industrial Ethernet switches in industrial networks.  (Fetches: Devices and Users)

* [**CloudCheckr**](/docs/cloudcheckr)
  * CloudCheckr is multi-cloud optimization and resource management software that includes cost management, security and compliance management, and resource utilization. (Fetches: Devices)

* **[CrowdStrike Falcon Discover](/docs/crowd-strike-falcon-discover)**
  * CrowdStrike Falcon Discover is a network security monitoring tool that provides real-time visibility into devices, users, and applications. (Fetches: Devices)

* **[CrowdStrike Kubernetes Protection](/docs/crowd-strike-kubernetes-protection)**
  * CrowdStrike Kubernetes Protection provides cloud-native application security, including breach prevention, workload protection, and cloud security posture management. (Fetches: Devices)

* **[CyberArk Idaptive](/docs/cyberark-idaptive)**
  * Idaptive Identity Management Platform is an identity and access management solution that unifies identity and access management services. (Fetches: Devices, Users)

* [**Databricks**](/docs/databricks)
  * Databricks combines data warehouses & data lakes into a lakehouse architecture that handles  data, analytics, and AI use cases. (Fetches: Devices)

* [**DOJ CSAM**](/docs/doj-csam)
  * DOJ’s proprietary Cyber Security Assessment and Management (CSAM) automates assessments and authorizations to provide a comprehensive assessment and continuous monitoring service. (Fetches: Devices)

* [**Dynamics CMDB (HelpDesk)**](/docs/helpdesk)
  * HelpDesk integrated with Microsoft Dynamics provides a complete ticketing solution. (Fetches: Devices)

* [**Easyvista Service Manager**](/docs/easyvista-service-manager)
  * EasyVista is an ITSM (IT Service Management) solution including change, release, incident, problem, and knowledge management. (Fetches: Devices)

* [**FortifyData**](/docs/fortify-data)
  * FortifyData is a threat exposure management platform for identifying, monitoring, and managing cyber risk. (Fetches: Devices)

* [**GlobalSign Atlas**](/docs/global-sign-atlas)
  * GlobalSign Atlas offers cloud certificate management and automation. (Fetches: Devices)

* **[GluWare](/docs/gluware)**
  * GluWare provides a Multi-vendor, multi-platform, and multi-domain network automation tool. (Fetches: Devices)

* [**HAProxy**](/docs/haproxy)
  * HAProxy is free and open source software that provides a high availability load balancer and reverse proxy for TCP and HTTP-based applications. (Fetches: Devices and Users)

* **[Hitachi Operations Center](/docs/hitachi-operations-center)**
  * Hitachi Ops Center provides data infrastructure management including automation, analytics, and protection. (Fetches: Devices)

* **[Horizon3.ai](/docs/horizon3-ai)**
  * NodeZero by Horizon3 provides continuous autonomous penetration testing via SaaS. (Fetches: Devices)

* [**HPE (SAN)**](/docs/hpe-san)
  * HPE storage area networking (SAN) provides storage solutions for performance, scalability, and manageability.  (Fetches: Devices)

* [**Huntress**](/docs/huntress)
  * Huntress is a managed endpoint detection and response (EDR) solution. (Fetches: Devices)

* [**IBM VPC**](/docs/ibm-vpc)
  * IBM Cloud Virtual Private Cloud (VPC) is a secure software-defined network (SDN) on which customers can build isolated private clouds.  (Fetches: Devices)

* **[IFS Assys](/docs/ifs-assyst)**
  * IFS Assys is IT service management (ITSM) software that helps automate business processes.  (Fetches: Devices)

* **[Imperva WAF](/docs/imperva-waf)**
  * Imperva Web Application Firewall (WAF) allows customers to monitor, filter, and block incoming and outgoing data packets from a web application or website. (Fetches: Devices)

* [**Imperva WAF Cloud**](/docs/imperva-waf-cloud)
  * Imperva Web Application Firewall (WAF) allows customers to monitor, filter, and block incoming and outgoing data packets from a web application or website.   (Fetches: Devices)

* [**Intruder.io**](/docs/intruder-io)
  * Intruder is an online vulnerability scanner that enables the identification of misconfigurations, missing patches, encryption weaknesses, application bugs, and more.  (Fetches: Devices)

* **[Keyfactor](/docs/keyfactor)**

* Keyfactor provides PKI as-a-Service enabling protection of every device, workload, and digital transaction with a unique and trusted identity.  (Fetches: Devices)

* [**ManageEngine Firewall Analyzer**](/docs/manage-engine-firewall-analyzer)
  * ManageEngine Firewall Analyzer is an agentless log analytics and configuration management software that analyzes logs from firewalls and generates real-time alert notifications and security and bandwidth reports. (Fetches: Devices)

* **[Microsoft Dynamics 365](/docs/microsoft-dynamics-365-finance)**
  * Microsoft Dynamics 365 Finance is a Microsoft enterprise resource planning system for medium to large organizations. (Fetches: Devices, Users)

* **[Mimecast](/docs/mimecast)**
  * Mimecast provides email security, data management and compliance, and security awareness and user behavior solutions. (Fetches: Users)

* **[Mutiny](/docs/mutiny)**
  * Mutiny is a network monitoring and alerting appliance. (Fetches: Devices)

* [**Namecheap**](/docs/name-cheap)
  * Namecheap offers free public DNS to help users get connected quickly and securely. (Fetches: Devices)

* [**Netwrix Auditor**](/docs/netwrix-auditor)
  * Netwrix Auditor is IT auditing software for detecting security threats and validating compliance. (Fetches: Users)

* [**N-Sight RMM**](/docs/n-sight-rmm)
  * N-Sight RMM provides remote monitoring and access, ticketing, and management for Windows, Linux, and Mac devices. (Fetches: Devices)

* **[Nutanix Prism Central](/docs/nutanix)**
  * Nutanix delivers hybrid and multicloud management, unified storage, database services, and desktop services to support applications and workloads. (Fetches: Devices, Users)

* [**Onspring Compass**](/docs/onspring-compass)
  * Onspring is cloud-based automated GRC software for business process management. (Fetches: Devices)

* [**Oracle Enterprise Manager**](/docs/oracle-enterprise-manager)
  * Oracle Enterprise Manager is an on-premises management platform that provides a single dashboard to manage all Oracle deployments. (Fetches: Devices)

* [**Oracle Ksplice**](/docs/oracle-ksplice)
  * Oracle Ksplice provides fast secure kernel and userspace patching without the need for reboots. (Fetches: Devices)

* [**PagerDuty**](/docs/pagerduty)
  * PagerDuty is a digital operations platform for system administrators and support teams to manage incident response. (Fetches: Users)

* **[Palo Alto Networks Prisma Access](/docs/palo-alto-prisma-access)**
  * Prisma Access SASE from Palo Alto Networks converges network security, SD-WAN, and autonomous digital experience management in the cloud to provide a secure access service edge. (Fetches: Devices, Users)

* [**Paycor**](/docs/paycor)
  * Paycor is an automated human capital management (HCM) platform for managing HR and payroll needs in one place. (Fetches: Users)

* **[Paylocity](/docs/paylocity)**
  * Paylocity is a cloud-based payroll and human capital management software. (Fetches: Users)

* [**Pingboard**](/docs/pingboard)
  * Pingboard creates real-time organizational charts by automatically synchronizing organizational charts with HRMS software. (Fetches:  Users)

* **[Polymer DLP](/docs/polymer-dlp)**
  * Polymer is a DLP solution that automates identification, monitoring, and remediation for sensitive data in cloud environments, and helps companies stay compliant with HIPAA, PCI. and GDPR.

* [**Rapid7 Insight Account Platform**](/docs/rapid7-insight-account)
  * Rapid7 Insights API: This API provides API access for the entire Rapid7 Insights platform and suite of products. (Fetches: Users)

* [**RecordedFuture**](/docs/recorded-future)
  * RecordedFuture threat intelligence helps identify the vulnerabilities that pose an actual risk to an organization, adding context and data to CVE scoring. (Fetches: Devices)

* [**Robin**](/docs/robin-io)
  * Robin (now Symworld Cloud) is a Kubernetes-based platform that automates the deployment, scaling, and lifecycle management of data- and network-intensive applications. (Fetches: Devices, Users)

* [**RUCKUS Cloud**](/docs/ruckus-networks)
  * CommScope RUCKUS Cloud is a network management-as-a-service platform that enables IT to provision, manage, optimize, and troubleshoot wired and wireless networks. (Fetches: Devices, Users)

* [**Sassafras**](/docs/sassafras)
  * Sassafras is IT asset management software that allows organizations to inventory and manage IT assets.   (Fetches: Devices)

* **[Secure Code Warrior](/docs/secure-code-warrior)**
  * Secure Code Warrior is a training platform that helps developers learn to write secure code. (Fetches: Users)

* **[Serraview](/docs/serraview)**
  * Serraview is workplace management and space optimization software. (Fetches: Users)

* **[Sensu](/docs/sensu)**
  * Sensu is a cloud monitoring solution that provides monitoring workflows automation and visibility into multi-cloud environments. (Fetches: Devices)

* [**Sentra**](/docs/sentra)
  * Sentra offers cloud data security posture management (DSPM), allowing customers to automatically discover, classify, monitor, and protect cloud data.    (Fetches: Devices)

* [**SharePoint**](/docs/sharepoint)
  * SharePoint creates internal websites where organizations store, organize, share, and access information from any device.  (Fetches: Devices)

* **[Shockwave Cloud](/docs/shockwave-cloud)**
  * Shockwave Cloud helps identify and track cloud related issues and misconfigurations.   (Fetches: Devices, Users)

* [**Snyk**](/docs/snyk)
  * Snyk is a developer security platform integrating directly into development tools, workflows, and automation pipelines. (Fetches: Devices)

* **[Stairwell](/docs/stairwell)**
  * Stairwell offers a threat hunting and detection and response platform called “Inception.” (Fetches: Devices)

* **[TeamCity](/docs/teamcity)**

* TeamCity is a build management and continuous integration server. (Fetches: Devices)

* **[TeamDynamix](/docs/team-dynamix)**
  * TeamDynamix is an ITSM/ESM and project portfolio management solution with enterprise integration and automation.  (Fetches: Devices, Users)

* **[Tenable.ot](/docs/tenableot)**
  * Tenable.ot provides the ability to identify operational technology (OT) assets, communicate risk, and prioritize action. (Fetches: Devices)

* [**Trellix ePO**](/docs/trellix-epo)
  * Trellix provides hardware, software, and services to investigate cybersecurity attacks, protect against malicious software, and analyze IT security risks. (Fetches: Devices)

* [**Trend Micro Vision One**](/docs/trendmicro-vision-one)
  * Trend Micro Vision One is a threat defense platform that includes: Advanced extended detection and response (XDR) capabilities. (Fetches: Devices)

* [**TruPortal**](/docs/tru-portal)
  * TruPortal is a secure, web-based access credential system for physical access. (Fetches: Devices)

* [**Udemy**](/docs/udemy)
  * Udemy is an online learning and teaching marketplace. (Fetches: Devices)

* **[Unimus](/docs/unimus)**
  * Unimus is a network configuration and automation tool which provides information on devices, backups, and configurations. (Fetches: Devices)

* **[Unitrends](/docs/unitrends)**
  * Unitrends (a Kaseya company) provides all-in-one enterprise backup continuity and disaster recovery solutions. (Fetches: Devices)

* [**Upkeep**](/docs/upkeep)
  * UpKeep Asset Operations Management Platform is a mobile-first CMMS (computerized maintenance management system), EAM (enterprise asset management), and IIoT (industrial internet of things) suite of solutions. (Fetches: Devices)

* [**Uptrends**](/docs/uptrends)
  * Uptrends is a cloud-based solution for monitoring websites, servers, APIs, and network performance. Integrate Uptrends with the Axonius Cybersecurity Asset Management Platform. (Fetches: Devices, Users)

* [**Uyuni**](/docs/uyuni)
  * Uyuni is an open-source configuration and infrastructure management solution for software-defined infrastructure.  (Fetches: Devices)

* [**Velociraptor**](/docs/velociraptor)
  * Velociraptor is an open-source endpoint monitoring, digital forensic and cyber response platform. (Fetches: Devices, Users)

* [**Veracode**](/docs/veracode)
  * Veracode provides static, dynamic, and software composition scanning to identify vulnerabilities in the software development lifecycle. (Fetches: Devices)

* [**Vicarius**](/docs/vicarius)
  * Vicarius is a consolidated vulnerability discovery, prioritization, and remediation solution.  (Fetches: Devices)

* [**Virtru Gmail Encryption**](/docs/virtru-gmail-encryption)
  * Virtru Gmail Encryption protects Gmail messages and attachments with end-to-end encryption while maintaining user ownership and control. (Fetches: Users)

* [**VMware NSX**](/docs/vmware-nsx)
  * VMware NSX provides an agile software-defined infrastructure to build cloud-native application environments. (Fetches: Devices)

* [**Zerto ZVM**](/docs/zerto)
  * Zerto ZVM is a data loss protection solution that provides disaster recovery, backup and workload mobility software for virtualized infrastructures and cloud environments. This adapter supports on-prem deployment. (Fetches: Devices)

* [**Zimperium zIPS**](/docs/zimperium)
  * Zimperium zIPS is a mobile threat defense solution for enterprises, providing protection to both corporate owned and BYOD devices. (Fetches: Devices, Users)
    For more details:

* Explore the entire [list of supported and integrated adapters](/docs/adapters-list).

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Absolute - Unenroll Asset**](/docs/absolute-unenroll-asset) - unenrolls Absolute Assets for assets that match the results of the selected saved query or assets selected on the relevant asset page.

* **[BigFix - Create Fixlet Action](/docs/bigfix-create-fixlet-action)** creates and executes a BigFix Fixlet action on assets that match the results of the selected saved query or assets selected on the relevant asset page.

* [**BigFix Remove Asset**](/docs/bigfix-remove-asset) - This action removes assets from aAssets that match the results of the selected saved query or assets selected on the relevant asset page.

* **[Equinix - Create Users](/docs/equinix-create-users)** -  creates Users in Equinix for assets that match the results of the selected saved query or assets selected on the relevant asset page.

* **[Equinix - Disable Users](/docs/equinix-disable-users)** - disables Users in Equinix for assets that match the results of the selected saved query or assets selected on the relevant asset page.

* **[Equinix - Remove Users](/docs/equinix-remove-users)** -  removes Users in Equinix for assets that match the results of the selected saved query or assets selected on the relevant asset page.

* [**GCP - Add or Remove Tags to/from Assets**](/docs/gce-compute-add-tags) - This action adds or removes tags from Google Cloud Provider assets.

* [**Jira Service Management - Create Issue**](/docs/create-jira-service-desk-ticket) creates one incident in Jira Service Management for all of the assets retrieved from the saved query supplied as a trigger (or from the entities selected in the asset table).

* **[Manage Engine ServiceDesk Plus  - Create Request](/docs/manage-engine-sdp-create-request)** - creates a ManageEngine ServiceDesk Plus request for  assets that match the results of the selected saved query or assets selected on the relevant asset page.

* [**ManageEngine ServiceDesk Plus - Create and Update Assets**](/docs/create-and-update-manage-engine-device) - creates a ManageEngine ServiceDesk Plus Asset, or updates ManageEngine ServiceDesk Plus Assets for assets that match the results of the selected saved query or assets selected on the relevant asset page.

* **[Microsoft Active Directory (AD) - Change Assets OU](/docs/change-users-devices-ou)** moves the assets (users or devices) retrieved from the saved query supplied as a trigger (or assets that were selected in the asset table) from one Organizational Unit (OU) to another in Microsoft Active Directory (AD).

* [**Okta - Add or Remove Users to/from Group**](/docs/okta-add-remove-user-in-group) adds or removes each user retrieved from the saved query supplied as a trigger (or users selected in the asset table) to an Okta group.

* [**SentinelOne - Remove Asset**](/docs/sentinelone-remove-asset) - This action removes existing assets from SentinelOne.

* [**SentinelOne - EC Isolate/Unisolate Assets**](/docs/sentinelone-isolate-unisolate-assets) - Isolates or unisolates assets in the SentinelOne.

* [**Slack - Send Message to Channel**](/docs/slack-send-message-to-channel) - Posts a message to a Slack channel for assets that match the results of the selected saved query or assets selected on the relevant asset page.

* [**Sophos Central - Remove Assets**](/docs/sophos-central-remove-asset) - Removes assets from Sophos Central for assets that match the results of the selected saved query or assets selected on the relevant asset page.

* [**Splunk - Create and Update Assets**](/docs/splunk-create-and-update-assets) - Creates or updates assets in Splunk.

* [**Tanium - Create Software Deployment**](/docs/tanium-deploy-software) - Installs, updates or removes Tanium Software for assets that match the results of the selected saved query or assets selected on the relevant asset page.

* [**Zoho Desk - Create Ticket**](/docs/zoho-create-ticket) - This action creates a Zoho Desk ticket.

For more details:

* See the complete [**Enforcement Action Library**](/docs/action-library).