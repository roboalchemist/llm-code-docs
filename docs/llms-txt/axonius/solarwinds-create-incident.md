# Source: https://docs.axonius.com/docs/solarwinds-create-incident.md

# SolarWinds - Create Incident

**SolarWinds - Create Incident** creates an incident in SolarWinds for:

* Assets returned by the selected query or assets selected on the relevant asset page.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.
* **Split Tickets By** - When enabled, group assets into different tickets based on a shared attribute. Click the adapter icon to select an adapter (or Aggregated), and then click the **Select Adapter Field** box to select the asset field used to generate a separate ticket for each unique value.

  <Callout icon="📘" theme="info">
    Note

    * The **Split Tickets By** option appears only in ticket creation actions, and does not appear in ticket-per-asset creation or ticket update actions.
    * For assets containing multiple values, the system uses only the first value to perform the split.
  </Callout>

<br />

* **Use stored credentials from  SolarWinds adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [SolarWinds](/docs/solarwinds-service-desk) adapter connection.
</Callout>

* **Incident Title** - Specify the incident title.

## Additional Fields

These fields are optional.

* **Description** - Add a description for the incident.
* **Site ID** - The site ID.
* **Department ID** - The department ID.
* **Assigned to Email** - The email address to which notification will be sent when the incident is created.
* **State** - As defined by SolarWinds Service Desk.
* **Priority** - As defined by SolarWinds Service Desk.
* **Category** - As defined by SolarWinds Service Desk.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** - The hostname or IP address of the SolarWinds Service Desk server.

  * **API Key** - An API Key associated with a user account that has permissions to perform this action. For details, see [How to Setup Token Authentication In SolarWinds](https://documentation.solarwinds.com/en/success_center/swsd/content/completeguidetoswsd/token-authentication-for-api-integration.htm).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

## APIs

Axonius uses the [SolarWinds ITSM API](https://apidoc.samanage.com/#tag/Incident/operation/createIncident).

## Required Permissions

The value supplied in [User name](#parameters) must have 'creating incident' permissions.

## Version Matrix

This action has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version           | Supported | Notes |
| ----------------- | --------- | ----- |
| SolarWinds (V2.1) | Yes       |       |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).