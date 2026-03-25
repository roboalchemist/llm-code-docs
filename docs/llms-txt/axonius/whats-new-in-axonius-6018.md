# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6018.md

# What's New in Axonius 6.0.18

#### Release Date: January  21st 2024

These Release Notes contain new features and enhancements added in versions 6.0.17 and 6.0.18.

* Read [What's New in Axonius 6.0](/docs/whats-new-in-axonius-600) to see all Axonius 6.0 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [ongoing updates to adapters and enforcement actions in Axonius 6.0](/docs/axonius-60-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

The following features were added to all assets pages:

**Data Refinement**
Data refinement now supports 'earlier than' and 'later than' fields for *versions*.

## Software Management Module New Features and Enhancements

The following new features and enhancements were added to the Software Management Module:

### Software Approval List

New [**Software Approval**](/docs/software-approval-list) lists enable users to manage a list of Software categorized into Approved/Not-approved. As software is detected it is automatically assigned the Approved/Not-approved status on the **Software Page**. It is then possible to see this information in queries, charts, etc. and take appropriate action if required. The **Software List** can be created and updated either by:

* Importing a CSV file that contains a list of 'Software' and 'Approval Status'.
* Manually adding Software using the **Add Software** button.
* Updating the 'Approval Status' field in the Software page using **Custom Fields**, which is then synchronized with the **Approval List**.

<Image alt="SoftwareApprovalList" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SoftwareApprovalList.png" />

## SaaS Management New Features and Enhancements

**Affiliated Users Enrichment Field**
A New 'Affiliated Users' enrichment field was added to the [**SaaS Applications** Asset page](/docs/saas-applications#enrichment-fields). This field counts all the users affiliated with a given SaaS application, including users coming from all available sources: the application’s adapter, user extensions, or DNS records.

## Asset Graph New Features and Enhancements

### Create Custom Groups using Multi-Select

**Custom Groups using Multi-Select** allows users to select multiple asset icons and [create custom asset groups](/docs/asset-graph#creating-custom-node-groups). This helps reduce the clutter in their graph, and custom groups can be acted on as a single entity. For example:
Users can select all the user nodes that belong to the same department and group them together. Then, they can Filter, Enforce, Segment, or explore further connections to the group with just a few clicks.

### Organize the Graph with Layouts

Users can choose between organic or hierarchical representations for personalized data visualization. Tailor the [graph layout](/docs/using-graph-layouts) to match the logic of the node relationships, optimizing clarity and understanding. This enhances user control, improves visual representation, and boosts data comprehension by offering flexible graph layouts catering to individual preferences and specific use cases.

### New Asset Graph Node Design and Color Scheme

The [Asset Graph](/docs/asset-graph) nodes have been redesigned and given a new modern color scheme.

### Expand by Single Asset's Adapter Connections

The ability was added to [segment a single asset](/docs/exploring-connections-and-asset-relationships#viewing-a-single-assets-adapter-connections) node to view the node's adapter connections. Then, one or more of the connections can be explored.

## Findings Center New Features and Enhancements

The [Alert drawer](/docs/viewing-alert-information#viewing-a-findings-center-alert) now displays under the **Count 1** and **Count 2** columns the number of assets that were compared in the Query comparison or Query change over time condition that triggered the alert.

![AlertDrawerCompareCounts(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AlertDrawerCompareCounts\(1\).png)

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Adapters Page Redesign

A new [Adapter Catalog](/docs/adapters-page) page now  presents adapters as a tile view by default. Tiles show adapter name, description and connection status. In addition, supported assets for each adapter are now displayed. Configured adapters are now always shown at the top of the tile view/table.
[Adapter Profile](/docs/adapter-profile-page) page was redesigned. Links for advanced settings are now at the left side of the profile page. A new Search was added to the Profile side panel to easily search for any advanced adapter setting, whether general, or specific for that adapter.

<Image alt="AdapterTiles" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdapterTiles.png" />

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### New Enterprise Password Manager  Added

**[CyberArk Privilege Cloud Vault](/docs/managing-external-passwords#cyberark-privilege-cloud-vault)** Password Manager was added.

### New Data Aggregation Setting Added

New option to [add all extensions to SaaS applications](/docs/configuring-data-aggregation-settings) even when the vendors aren't recognized by Axonius's internal Vendors database.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

The following functions and operators can now be used in a Dynamic Value statement:

* **The *average* Function**
  * The new [average](/docs/using-functions-and-keywords#using-the-average-function) function returns the average of the number values in a list field.\
    Syntax: **average**(\[adapter.arrayfield])

* **The *date-format* Function**
  * The new [date-format](/docs/using-functions-and-keywords#using-the-dateformat-function-for-string-manipulations) function formats a date field using a specified format for the date and time.
    Syntax: **date\_format**(\[adapter.field], "format")

* **The *substring* Function**
  * The new *substring* function for string manipulation returns a substring of the field value, beginning from the specified start position in the string until the specified end position in the string. For example: substring('first last', 6, 10) = last
    Syntax: **substring**(\[adapter.field], start\_index, end\_index)

* **The *to\_lower* Function**
  * The new *to\_lower* function for string manipulation converts the string in the adapter field to lowercase.
    Syntax: **to\_lower**(\[adapter.field])

* **The *to\_upper* Function**
  * The new *to\_upper* function for string manipulation converts the string in the adapter field to uppercase.
    Syntax: **to\_upper**(\[adapter.field])

* **The *field\_not\_exists* Operator**
  * The new [*field\_not\_exists*](/docs/using-functions-and-keywords#using-the-fieldnotexists-operator) operator tests whether an adapter field exists.
    Syntax: **field\_not\_exists**

* **The *in\_net* Operator**
  * The new [*in\_net*](/docs/using-functions-and-keywords#using-the-innet-operator) operator tests whether the IP addresses in an adapter list field or in an adapter string field are in the specified IP address range.
    Syntax: **in\_net** (IP address range)

* **The *not\_in\_net* Operator**
  * The new [*not\_in\_net*](/docs/using-functions-and-keywords#using-the-notinnet-operator) operator tests whether the IP addresses in an adapter list field or in an adapter string field are not in the specified IP address range.
    Syntax: **not\_in\_net** (IP address range)

## New User-Device Association Settings

An Association section has been added to the [Configuring Enrichment Settings](/docs/configuring-enrichment-settings#association) page with the following settings:

* Users to be associated with devices that share a mutual domain (if domain exists on the device)
* Avoid association if device doesn't have a domain
* Filter users from Last Used Users