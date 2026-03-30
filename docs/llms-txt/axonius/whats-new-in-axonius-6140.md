# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6140.md

# What's New in Axonius 6.1.40

#### Release Date: November 10th 2024

These Release Notes contain new features and enhancements added in version 6.1.40.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

The following features were added to all assets pages:

### Query Wizard Enhancements

#### Select if the Query Wizard's IN Operator Searches for Values That Equal or Contain the Defined Criteria

The [IN operator](/docs/adding-multiple-values-to-query-expression) in the Query Wizard is now split into the `IN (contains)` and the `IN (equals)` operators allowing users to decide how the IN operator queries the designated values.

* Use `IN (Equals)` to search for the provided values that match the exact wording and case, as the query criteria.

* Use `IN (Contains)` to search the for the values that include a partial match or match in a different case, as the query criteria.

## Reports  New Features and Enhancements

The following enhancements were added to reports.

* The ability was added to [configure CSV export options](/docs/report-configuration-page) when including a CSV with the query results in the report.
  ![ConfigCSVOptionsReport.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ConfigCSVOptionsReport.png)

## SaaS Management New Features and Enhancements

### New Applications Settings Field: Setting Status

The new 'Setting Status' field displays value of 'Properly Configured' in green text when the Settings Score is equal to 1, and a value of 'Misconfigured' in red text when the Settings Score is less than 1.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Field Mapping Runs Outside the Discovery Cycle

[Field Mapping](/docs/managing-field-mapping) Enforcement sets are triggered in the Post-Correlation phase of the [Discovery Cycle](/docs/discovery-cycle) after all other Enforcement sets have completed to run. However, now they continue running asynchronously outside the Discovery Cycle. This enables the Discovery Cycle to proceed to the next phase before the Field Mapping Enforcement set runs conclude.

* **Last Run Time** and **Last Run Status** columns have been added to the Field Mapping table to enable tracking the run status of Field Mappings.

* It is now possible to navigate from a Field Mapping to its Enforcement Set Run History page to get more information about the run.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

#### Dynamic Value Statement Wizard Enhancements

The [Dynamic Value Statement Wizard](/docs/using-the-dynamic-value-statement-wizard) now supports the following functions in All and Switch/Case statements. These functions assign to the action field the result of the functions on  an adapter field or custom input resolved string value.

* **To upper** - Converts the string to uppercase.

* **To lower** - Converts the string to lowercase.

* **Substring** - Extracts a substring from the value in the adapter field or custom input beginning from the specified start position in the string (**From**) for the length specified (**Length**).

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**BeyondTrust PRA Cloud**](/docs/beyondtrust-pra-cloud)
  * BeyondTrust PRA Cloud is a privileged remote access solution that provides secure remote access to critical systems without requiring a VPN, enhancing secure management of privileged accounts. (Fetches: Devices, Users)
* [**Morphisec Unified Threat Prevention Platform**](/docs/morphisec)
  * Morphisec Unified Threat Prevention Platform provides centralized control, monitoring, and configuration of Morphisec’s endpoint security solutions. (Fetches: Devices)

### Adapter Updates

The following adapters were enhanced:

* **[Asana](/docs/asana#advanced-settings)** - Added the capability to fetch user status.
* [**BMC Atrium CMDB**](/docs/bmc-atrium-cmdb) - Added the capability to fetch a list of specific customer-provided attributes.
* [**Claroty CTD**](/docs/claroty) - Added the option to fetch installed programs.
* [**Citrix Director**](/docs/citrix-director) - Added the option to fetch the catalog name.
* [**CyCognito Platform**](/docs/cycognito-platform) -   Added the option to filter out inactive and/or semi-related assets.
* [**Datadog**](/docs/datadog) - Added the options to fetch:
  * Network devices
  * Interfaces for each network device
* **DocuSign** - Added the capability to filter the users by statuses: Active, Closed, ActivationSent.
* [**ManageEngine Endpoint (Desktop) Central and Patch Manager Plus**](/docs/manageengine-desktop-central) - It is now possible to specify a DC Instance to add to the headers for the API calls.
* **[Microsoft Entra ID (Azure AD) and Microsoft Intune](/docs/microsoft-azure-active-directory-ad#microsoft-entra-id-advanced-settings)** - Added the option to enrich Intune devices with enrollment profile information.
* [**Tableau**](/docs/tableau) - Added the option to fetch users from all sites.
* [**Tailscale**](/docs/tailscale) - Added support for OAuth authentication using the new Client ID and Client Secret parameters.
* **Workday** - Improvements made to X.509 authentication

### New Enforcement Actions

The following Enforcement Actions were added:

* **[Microsoft Entra ID (formerly Azure AD) - Create Group](/docs/create-azure-ad-group)** - Create Group - Creates a new group in Entra ID.
* **[MVISION ePO - Add Asset](/docs/trellix-epo-add-asset)** -  adds assets returned by the selected query or assets selected on the relevant asset page to MVISION ePo.

### Updated Enforcement Actions

The following Enforcement Actions were updated:

* **[Cherwell IT Service Management - Create Incident](/docs/create-cherwell-incident)** - This action now supports use of a Gateway.
* **ManageEngine ServiceDesk Plus - Create and Update Assets**   - Added "Use first IP address only" and “Use first MAC address only“ fields.