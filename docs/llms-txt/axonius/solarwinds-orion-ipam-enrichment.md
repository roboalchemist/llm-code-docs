# Source: https://docs.axonius.com/docs/solarwinds-orion-ipam-enrichment.md

# SolarWinds Network Performance Monitor - IPAM Information Enrichment

**SolarWinds Network Performance Monitor - IPAM Information Enrichment** enriches each device's IPAM subnet information by using the preferred IP field.

* Assets that match the parameters of the selected saved query, and match the Enforcement Action Conditions, if defined, or assets selected on the relevant asset page.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from  SolarWinds Network Performance Monitor adapter** - Select this option to use the first connected SolarWinds Network Performance Monitor adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  NOTE

  To use this option, you must successfully configure a [SolarWinds](/docs/solarwinds-service-desk) adapter connection.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **IP Address** – The hostname or IP Address of the SolarWinds management server.

  * **User Name** and **Password** - The user name and password for an account that has admin access to the management server API. Note that the account might have to be a local account with admin access and not an AD integrated account.

  * **Port** *(default: 17774)* - The port used for the connection. Port 17774 for SWIS REST is now default for SolarWinds. Note that from SolarWinds Release 2023.1 SWIS REST Endpoint on port 17778 is deprecated and has been replaced with port \* SolarWinds recommends you migrate SWIS REST Endpoint to port 17774.

  * **Custom Properties List** *(optional)* - Specify a comma-separated list of SolarWinds properties.

  * If supplied, the adapter connection will add a device field for each of the comma-separated list properties that have been defined in this field.

  * If not supplied, the adapter connection will not fetch any additional SolarWinds properties.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **Certificate File** *(optional)*  - It is possible to  encrypt the SolarWinds DB connection and connect to it by using a Certification file. Upload the certificate file.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## APIs

Axonius uses the [SolarWinds Orion SDK](https://thwack.solarwinds.com/community/it-resources/orion-sdk).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                                           | Supported | Notes                                                                                                                                                                              |
| ------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SolarWind Orion Platform version 2018.4 and later | Yes       | Axonius uses the [SolarWinds Orion SDK](https://thwack.solarwinds.com/community/it-resources/orion-sdk), which is supported for SolarWind Orion Platform version 2018.4 and later. |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).