# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6142.md

# What's New in Axonius 6.1.42

#### Release Date: November 24th, 2024

These Release Notes contain new features and enhancements added in version 6.1.42.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## New Global Search

Users can now perform free-text searches using the new [ Search bar](/docs/searching-for-assets) from any page in Axonius to find assets or identify security misconfigurations such as vulnerabilities. The search is immediate. The search is run on all asset types, and the field names available for search for those assets. The **Recently Searched** and **Recently Viewed** sections allow users to access their latest search results or specific assets among these results.

<Image alt="SearchForAssets" width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-TSDDCWDY.png" />

Upon entering free text, a list of results appears instantly. Users can see which asset types were found, the number of each asset type found, and the asset field that returned results.

<Image alt="ResultsList" width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-0MHNBP16.png" />

From the **Search for Assets** dialog, users can:

* Investigate a specific asset by clicking any record from the result list. This opens the relevant [Asset Profile page](/docs/asset-profile-page).
* View the detailed list of results and explore them in the Assets Pages by selecting **View Results** at the bottom right of the dialog.

## Assets Pages

The following features were added to all assets pages:

### Query Wizard Enhancements

The following new features and enhancements were added to the Query Wizard.

#### Field Descriptions

When users select a specific field in the Query Wizard,[field descriptions](/docs/field-descriptions) are displayed in a new field selection list. Field descriptions help users understand and use asset fields in queries. They explain the purpose of each field and its data type, making it easier to choose the right field for the query they are creating. The description also includes the data type, such as Single Select, Integer, String, Array, and more.

![FieldDescriptionDropdown.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FieldDescriptionDropdown.png)

## Findings Center New Features and Enhancements

The **[Findings Center](/docs/findings-center-overview)** was redesigned to make user experience smoother and more efficient.

* The Findings Center now shows the alerts triggered by the Findings in an aggregated view, enabling users to access the alerts through the Findings that triggered them. This replaces the previous interface that had separate tabs for Findings and Alerts.
  * The Findings are sorted by the time they triggered an alert with the most recent at the top of the table.
* A new Folder pane enables viewing Findings according to their categories. These categories include All Findings, Cyber Asset Management, and Internal System, as well as SaaS Management if enabled.
  * Alerts from System Settings go into the Internal System category.
  * By default, alerts from the Enforcement Center go into the Cyber Asset Management category.
  * A blue **New** badge displays the number of Findings with new alerts next to each category.
* A new blue notification dot on the **Findings Center** icon in the side menu indicates that at least one new alert has been triggered in the Findings Center since the user last visited this page. This replaces the notification bell at the top of the application.

![FindingsCenterwithCategoryPaneB](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FindingsCenterwithCategoryPaneB.png)

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Dashboard Management Enhancements

The following fields were added to the [Dashboard Manager](/docs/manage-dashboards) table:

* **Last Modified** - The latest date when changes were applied to the dashboard, including name and description, filters, access management, chart location, and any other presentation changes.

* **Date Created** - The date the dashboard was created.

* **Last Viewed** - The date the dashboard was last viewed by any user.

## Asset Graph New Features and Enhancements

The following new features and enhancements were added to the **Asset Graph**.

* The [Asset Graph](/docs/asset-graph) is now available when a [Data Scope](/docs/data-scope-management) is configured with excluded fields.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### New Permissions

It is now possible to hide the **Support Center** link from the **Help and Support** menu of specific non-admin users' consoles, by clearing the **Enable Support Center link** checkbox (enabled by default) on the **Permissions** page under **Global Actions**.

![PermissionsSupportCenter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PermissionsSupportCenter.png)

## General Updates

### Performance Improvements

As part of ongoing efforts, Axonius has made a range of improvements in our infrastructure that lead to multiple performance improvements across the board in this version.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

#### to\_int Function

The new [*to\_int* function](/docs/using-functions-and-keywords#using-the-toint-function) converts a string or float value to an integer value.  This function is useful for converting a String/Float value to Integer format before adding it to a Custom String field (using the [Axonius - Add Custom Data to Assets enforcement action](/docs/add-custom-data)).
**Syntax:** to\_int (\[adapter.field])

#### Relationship Fields Lookup Added to Syntax Helper

The Syntax Helper now includes a new  **[Relationship Field](/docs/using-the-syntax-helper#adding-a-relationship-field-to-a-statement)** tab. This feature allows users to select and copy a Relationship Field into a Dynamic Value statement. The Relationship Field is an adapter field of a related asset based on a Relationship. This enables the value to be used to configure fields in the Enforcement Action configuration dialog.

![SyntaxHelperRelationshipField](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SyntaxHelperRelationshipField.png)

#### Dynamic Value Statement Wizard Enhancements

The Dynamic Value Statement Wizard now supports the [**relation** function](/docs/using-the-dynamic-value-statement-wizard#using-the-relation-function-in-the-wizard) in All and Switch/Case statements. This function assigns the value of an adapter field in a related asset (an asset that is related to the Enforcement Center action via a Relationship) to the action field.

![RelationWizard](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RelationWizard.png)

### Enhancements to Axonius Actions

* The [**Axonius - Push System Notification**](/docs/push-system-notification) configuration now requires selecting a specific **Alert Category** in the Findings Center as the destination for incoming alerts. In addition, users can now select an **Alert name** so that incoming alerts have a unique name instead of a system-assigned default name.

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**ActivTrak**](/docs/activtrak)
  * ActivTrak is a workforce analytics tool that provides insights into productivity and operational efficiency. (Fetches: Devices, Users)
* [**Fidelis**](/docs/fidelis)
  * Fidelis is a cybersecurity platform that offers threat detection, investigation, and response capabilities across networks, endpoints, and cloud environments. (Fetches: Devices)

### Adapter Updates

The following adapters were enhanced:

* **[AWS (Amazon Web Services](/docs/connecting-the-aws-adapter-using-cf-organizations))** - The AWS documentation page was updated to include an embedded version of the 'Axonius CloudFormation Template'.
* [**Black Kite**](/docs/black-kite) - Added the option to fetch subdomains as URLs instead of devices.
* [**Cato Networks**](/docs/cato)
  * This adapter now fetches SaaS applications.
  * Added the option to fetch users applications.
  * Added the capability to set the number of days you want as a usage time frame.
* [**Check Point Infinity**](/docs/checkpoint-infinity) - Added the option to use API Key authentication.
* [**Claroty CTD**](/docs/claroty) - Added the capability to enter a list of specific fields to fetch.
* [**Microsoft Azure**](/docs/microsoft-azure) - Added the option to get VM size information.
* [**Rapid7 InsightVM**](/docs/rapid7-insightvm) - Added the option to not ingest duplicate CVEs.
* [**SafeBreach**](/docs/safebreach) - Added the option to to enable the addition of Simulation Steps from the execution history to each Node.
* [**StackRox**](/docs/stackrox) - This adapter now fetches containers as assets.
* [**Stairwell**](/docs/stairwell) - Added the option to parse the label field as the asset name and host name.

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Enrich Cisco AMP device using Cisco Orbital**](/docs/cisco-orbital-enrich-device) - Enriches devices fetched by the Cisco AMP adapter with information from a Live Cisco Orbital Query.

* [**Cisco Support - Enrich Cisco Devices OS with EOL/EOS**](/docs/cisco-support-eox-enrichment)

* **[Microsoft Entra ID (formerly Azure AD) - Add or Remove License to/from Groups](/docs/azure-ad-assign-license-to-group)**

* [**Tanium - Create Software Deployment**](/docs/tanium-deploy-software) - Installs, updates, or removes existing software packages preconfigured on the Tanium server.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* [**Datadog Add Tag to Assets**](/docs/tag-in-datadog) - Added the option to send hostnames to Datadog in lowercase.
* **[Assign Active Directory Group to Users](/docs/assign-active-directory-group-to-user)**  - A number of configuration changes were made including: Group IDs renamed to Group DNs, Semicolon-separation instead of comma-separation in group IDs for the action.
* [**Tanium - Create Action**](/docs/tanium-create-action) - Added the option to use hostnames from all Tanium adapters and not only from Tanium Client Status.