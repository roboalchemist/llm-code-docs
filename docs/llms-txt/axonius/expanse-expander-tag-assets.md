# Source: https://docs.axonius.com/docs/expanse-expander-tag-assets.md

# Palo Alto Networks Cortex Xpanse - Tag Assets

**Palo Alto Networks Cortex Xpanse - Tag Assets** adds tags to Internet assets for:

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

* **Use stored credentials from the Palo Alto Networks Cortex Xpanse adapter** - Select this option to use the first connected [Palo Alto Networks Cortex Xpanse](/docs/palo-alto-networks-cortex-xpanse) adapter credentials.

  <Callout icon="📘" theme="info">
    Note

    * To use this option, you must successfully configure a [Palo Alto Networks Cortex Xpanse](/docs/palo-alto-networks-cortex-xpanse) adapter connection.
    * The user name and the password used for the adapter connection must have the required permissions to add tags.
  </Callout>

* **Tags** - The name of the new tag to add. Type the name of a tag and press **Enter**. Multiple tags can be added. To add a tag as a *key:value* pair, separate the key and value with a : (colon).

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection Parameters

  If **Use stored credentials from the Palo Alto Networks Cortex Xpanse adapter** is disabled, these fields are required.

  * **Host Name or IP Address** *(default: `https://expander.expanse.co`)* - The host name or IP address of a Palo Alto Networks Xpanse Cortex server.

  * **Client ID** - Specify the user account that has permissions to add tags.
    To obtain a Client ID, see [Acquiring a Client ID and Client Secret](/docs/palo-alto-networks-cortex-xpanse#acquiring-a-client-id-and-client-secret).

  * **Client Secret** -  Specify the client secret that has permissions to add tags. To obtain a Client Secret, see [ Acquiring a Client ID and Client Secret](/docs/palo-alto-networks-cortex-xpanse#acquiring-a-client-id-and-client-secret).

  * **API key** - An API Key associated with a user account that has permissions to add tags. This is mandatory for API v2. When **Client ID** and **Client Secret** are provided, API Key is not required.

  * **API Key ID** - If you select API v2 you need to add both an API Key and the API ID. In addition, make sure you enter the correct domain for your API version.

  * **API Version** - Select the API Version v1, or v2.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

## Required Ports

Axonius must be able to communicate with the value supplied in [Hostname or IP Address](#parameters) via the following ports:

* TCP port 80
* TCP port 443

## APIs

Axonius uses the [Palo Alto Networks Cortex Xpanse](https://docs-cortex.paloaltonetworks.com/r/Cortex-Xpanse-REST-API/Add-Tags-to-Assets) API.

## Required Permissions

The credentials of the user account used to add tags must have permission to write tags to assets.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).