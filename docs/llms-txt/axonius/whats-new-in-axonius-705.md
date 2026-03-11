# Source: https://docs.axonius.com/docs/whats-new-in-axonius-705.md

# What's New in Axonius Asset Cloud 7.0.5

#### Release Date: August 17th 2025

These Release Notes contain new features and enhancements added in version 7.0.5.

* Read [**What's New in Axonius 7.0**](/docs/whats-new-in-axonius-700) to see all Axonius 7.0 features.

***

## Axonius Platform New Features and Enhancements

### Query Wizard Enhancements

#### Adding Custom Count Operator Fields to the Query Wizard

You can now enable the count operators (`count =`, `count >`, `count <`) for up to 10 additional fields of your choice, including custom data fields and common enrichment fields.\
This new feature is available in **System Settings → Query Configuration**.

Once configured, count operators can be used in the Query Wizard for the newly added fields.

<Image alt="CountOperatorQueryConfig.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CountOperatorQueryConfig.png" />

***

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

#### New Dynamic Value Statement Functions

The following functions were added to the Dynamic Value statement functionality:

* **generate\_string** function - The [**generate\_string** function](/docs/using-functions-and-keywords#using-the-generatestring-function) creates a secure, random string of a specified length and character type. This enables generating unique identifiers, temporary passwords, or security tokens directly within workflows.
  * **Syntax:** `generate_string(Length, Character_Mode)`
  * **Parameters:**
    * **Length** - The total number of characters in the generated string (default: 16).
    * **Character Mode** - The type of characters to include. Options are **alphanumeric** (default), **hex**, **letters**, or **numbers**.
  * **Example:** `generate_string(6, letters)` returns an output like *aBcDef*

* **filter** function - The [**filter** function](/docs/using-functions-and-keywords#using-the-filter-function) enables dynamically filtering values from single values or arrays (lists). This gives the flexibility to configure a filter within a workflow without being limited to a predefined saved query.
  * **Syntax:** `filter([field], Operator, Criteria)`
  * **Parameters:**
    * **field** - A single value string or a multiple values string field.
    * **Operator** - The comparison to be applied. Supported operators are `contains`, `not_contains`, `gt` (greater than), `lt` (less than), and `regex`. It is possible to combine multiple operators and criteria.
  * **Example:** `filter([1,5,3], gt, "2")` returns the output `[5,3]`.

***

### Cases New Features and Enhancements

The **Create a Case Set** wizard now enables [triggering automated **Workflows** directly from the **Add Actions** step](/docs/adding-follow-up-actions).\
This new feature applies specifically to event-based scenarios, such as when an asset is no longer part of a Case query or when a ticket's status changes.\
The workflow's triggering event is preconfigured to match the selected condition and cannot be replaced, ensuring it is automatically initiated by the correct event without any manual setup.

<Image alt="AddWorkflowConditions.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddWorkflowConditions.png" />

***

### Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the standard functionality across all adapters:

#### New Adapter Ingestion Rule `trim_regex` Post Action

The new [`trim_regex` post action](/docs/setting-adapter-ingestion-rules) can be used to remove a specific string or pattern from a field using regex patterns.\
This enables cleaning up or standardizing data by removing unwanted text.\
For example, it can be used to remove the MAC address (and the preceding dash) from the end of an **Asset Name** and **Host Name** field.

**Syntax:**

* `[field]` - The target field from which to remove the string.
* `[regex_template]` - The regex pattern that identifies the string to be removed.

***

#### Adapter Advanced Settings

**Terminate after X hours of an active fetch**

The following setting was added to the **Adapter Configuration** section in [Advanced Settings](/docs/advanced-settings):

* Added the capacity to set a threshold time (in hours) that will terminate a running successful fetch operation of an adapter when its fetch exceeds the time set (including an appropriate log and status).\
  This allows you to manage the duration of the discovery cycle, ensuring that even successful fetches stay within the planned time frame.

***

#### Adapter Connections

* The "Terminate after X hours of an active fetch" field was added to the [Adapter Connections](/docs/adapter-connections) page.

***

## Adapter and Enforcement Action Updates

### New Adapters

The following new adapters were added:

* [**ManageEngine EventLog Analyzer**](/docs/manage-engine-event-log-analyzer)
  * ManageEngine EventLog Analyzer is a web-based SIEM solution that provides real-time log monitoring, threat detection, compliance reporting, and forensic analysis across diverse IT environments.\
    *(Fetches: Devices)*

* [**Recorded Future Attack Surface Intelligence**](/docs/recorded-future-asi)
  * Recorded Future Attack Surface Intelligence maps and monitors your exposed digital assets in real time, helping you proactively reduce risk — unlike the core platform, which focuses on external threats, this tool reveals your attack surface from an attacker’s perspective.\
    *(Fetches: Devices, Vulnerabilities, SaaS Applications)*

* [**ThreatMon**](/docs/threat-mon)
  * ThreatMon is a platform that provides cyber intelligence for monitoring and analyzing potential threats.\
    *(Fetches: Alerts/Incidents)*

***

### Adapter Updates

The following adapters were updated:

* [**Ceridian Dayforce**](/docs/ceridian-dayforce) - Added the option for the adapter to automatically detect the new URL in the error message and use it to update the **Host Name or IP Address** field in the adapter's connection.
* [**Dell PowerStore**](/docs/dell-power-store) - Added the option to fetch NFS server assets.
* [**Elasticsearch**](/docs/elasticsearch) - Added the option to fetch users instead of devices if logs contain user data.
* [**Infoblox DDI**](/docs/infoblox) - This adapter now supports Layer7 API Gateway connection.
* [**IONIX (formerly Cyberpion)**](/docs/ionix) - This adapter now fetches Domains & URLs and Application Services as assets (and no longer fetches Devices).
* [**OneTrust**](/docs/one-trust) - This adapter now supports Layer7 API Gateway connection.
* [**Oracle NetSuite**](/docs/netsuite) - Added the option to enter the look-back period for fetching vendor payment transactions.
* [**Palo Alto Networks Cortex XSOAR**](/docs/paloalto-xsoar) - Added the option to choose between API v6 and API v8 in the connection parameters.
* [**ServiceNow**](/docs/servicenow) - The [Custom Parsing](/docs/adapter-custom-parsing) capability now supports Users as well.
* [**Tenable.sc (SecurityCenter)**](/docs/tenablesc-formerly-securitycenter) - Added the option to fetch software name for CVEs associated with Plugin ID 63155.
* [**Venafi**](/docs/venafi) - Added the option to parse devices that have CertificateDetails only under Certificates (and not as Devices).

***

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Jamf Pro - Lock Device**](https://docs.axonius.com/axonius-help-docs/docs/lock-device) - Now works for device assets.

* [**Monday - Manage Users**](/docs/monday-manage-users) - Performs the following actions on users:
  * Activate User
  * Deactivate User
  * Update User Role
  * Delete User from Workspace

* [**NAVEX - Create User**](/docs/navex-create-user) - Creates new users in NAVEX.

* [**NAVEX - Delete User**](/docs/navex-delete-user) - Deletes users from NAVEX.

* [**NAVEX - Assign User Group**](/docs/navex-update-users-groups) - Assigns users to a group in NAVEX.

* [**NAVEX - Update User Details**](/docs/navex-update-user) - Updates the user's group in NAVEX.