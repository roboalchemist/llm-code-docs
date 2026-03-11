# Source: https://docs.axonius.com/docs/cisco-orbital-enrich-device.md

# Enrich Cisco AMP device using Cisco Orbital

**Enrich Cisco AMP device using Cisco Orbital** enriches devices fetched by the Cisco AMP adapter for:

* Assets returned by the selected query or assets selected on the relevant asset page.

This action triggers a Live Cisco Orbital Query and adds the information returned by the query to each asset.

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

* **Client ID** - Enter your Client ID. To generate your Client ID:
  1. Log into to the admin panel of Cisco AMP
  2. Go to the **Business Page** from the **Accounts** dropdown menu.
  3. Click **Edit**.
  4. Under **Features**, click on the "Regenerate…" button beside **3rd Party API Access** to generate the Client ID.

* **Region** - Select between North America, Asia Pacific, Japana and China, or Europe.

* **Cisco Orbital Query** - Enter a Live Cisco Orbital Query.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.
* **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Cisco Orbital API](https://developer.cisco.com/docs/orbital/queries/).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).