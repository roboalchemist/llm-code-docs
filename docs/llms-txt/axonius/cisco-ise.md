# Source: https://docs.axonius.com/docs/cisco-ise.md

# Cisco Identity Services Engine (ISE) - Apply Policy to Devices

**Cisco Identity Services Engine (ISE) - Apply Policy to Devices** assigns a policy to or clears policies from devices in Cisco Identity Services Engine for:

* Assets that match the selected saved query, and
* Assets that match the Enforcement Action dynamic values, if defined.
* Assets selected on the relevant asset page.

<Callout icon="📘" theme="info">
  Note

  To use this Enforcement Action, you must successfully configure a [Cisco Identity Services Engine (ISE)](/docs/cisco-identity-services-engine-ise) adapter connection.
</Callout>

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

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Use stored credentials from [Cisco Identity Services Engine (ISE)](/docs/cisco-identity-services-engine-ise) adapter** - Select this option to use the Ivanti Security Controls connected adapter credentials.

  * When you select this option, the **Select Adapter Connection** dropdown is available, and you can choose which adapter connection to use for this Enforcement Action.
* **Action** - Select between Apply and Clear.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Cisco ISE Domain** - The hostname or IP address of the Cisco ISE server that  Axonius can communicate with via the [Required Ports](#required-ports).

  * **Cisco pxGrid Domain** - Set this parameter to connect to a pxgrid domain instead of the regular domain used for ERS. When this parameter is not set, the same ISE domain is used for both pxgrid and ERS APIs.

  * **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to perform this action.

  * **Use pxGrid to Fetch Live Sessions**  -

  * If enabled, Axonius will enrich the data collected from Cisco ISE by enabling pxGrid. Using pxGrid requires a plus licence and requires an additional authentication step from pxGrid Services on your Cisco ISE domain. For more details, see [Authorize Axonius in pxGrid Services](/docs/cisco-identity-services-engine-ise#auth).

  * If disabled, Axonius will not enable pxGrid.

  * **pxGrid Client Certificate** / **pxGrid Client Private Key** / **pxGrid Client Private Key Password** / **pxGrid Client Root CA chain** - These settings are required for xmpp client with pxgrid 1

    * For details, contact [Axonius Support](https://support.axonius.com/).

    <Callout icon="📘" theme="info">
      Note

      The xmpp client has been deprecated by Cisco. Axonius will continue supporting it, but it is advised to transition to the REST client to fetch pxGrid data.
    </Callout>

  * **Use v1.1 Object Model for ERS API** - Select when using either Cisco ISE versions 2.4 or  2.7, or if you receive a “Connection Fails”  HTTP 400 error.

    <Callout icon="📘" theme="info">
      Note

      This parameter is only used with the ERS API. It has no effect when using the pxGrid API.
    </Callout>

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Policy Name** - The name of Adaptive Network Control (ANC) policy to apply.

## Required Permissions

The user account used to connect must have permissions to assign policies to devices. See [Cisco Identity Services Engine (ISE)](/docs/cisco-identity-services-engine-ise#required-permissions).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).