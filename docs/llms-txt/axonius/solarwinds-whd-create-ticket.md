# Source: https://docs.axonius.com/docs/solarwinds-whd-create-ticket.md

# SolarWinds Web Help Desk - Create Ticket

**SolarWinds Web Help Desk - Create Ticket** creates one ticket in SolarWinds Web Help Desk for:

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

* **Host Name or IP Address** - The full URL of the SolarWinds server.
* **Problem Type ID** - The type ID of the ticket to create.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Connection and Credentials

* **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to perform this Enforcement Action.
* **API Key** - The API key related to the user name and password provided.

<Callout icon="📘" theme="info">
  Note

  One of the following connection methods is required:

  * User Name and Password

  * User Name and API Key

  * API Key
</Callout>

* **Account ID** - Your SolarWinds account identifier.

## Ticket Main Settings

* **Ticket Subject** - Enter a short description of the ticket issue.
* **Ticket Description** - Enter a full description of the issue.

## Ticket Additional Settings

* **Room** - The ticket room.
* **Location ID** - The location ID of the ticket to create.
* **Department ID** - The department ID.
* **Client Reporter ID** - The client reporter ID.
* **Client Tech ID** - The client tech ID.
* **Status Type ID** - The status type ID.
* **Priority Type ID** - The priority type ID.

## Additional Fields

These fields are optional.

* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.
* **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
* **BCC Address** - The BCC email address.
* **CC Address For Tech** - The CC email address.
* **Assign To Creating Tech** - Select to assign the ticket to the creating tech.
* **Should Email Client** - Select to send email to the client.
* **Should Email Group Manager** - Select to send email to the group manager.
* **Should Email Tech** - Select to send email to the tech.
* **Should Email Tech Group Level** - Select to send email to the tech group level.
* **Create ticket even if no new entities were added** - By default Axonius creates a ticket even if no new entities were added. Clear this option to not create a ticket even if no new entities were added.

## APIs

Axonius uses the [SolarWinds Web Help Desk](https://documentation.solarwinds.com/archive/pdf/whd/whdapiguide.pdf) API.

## Required Ports

Axonius must be able to communicate with the values supplied in **Connection Parameters** via the following ports:

* SolarWinds Web Help Desk port

## Required Permissions

The values supplied in [Connection Parameters](#connection-parameters) above must have the following permissions:

* Authentication to perform request action

## Version Matrix

This Enforcement Action has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| 12.8.2  | Yes       |       |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).