# Source: https://docs.axonius.com/docs/redcloak-tdr-add-remove-tag.md

# Secureworks Taegis XDR - Add/Remove Tag

**Secureworks Taegis XDR - Add/Remove Tag** adds or removes tags on assets that match the results of the selected saved query, and match the Enforcement Action Conditions, if defined or assets selected on the relevant asset page.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Secureworks Taegis XDR (Red Cloak TDR)](/docs/secureworks-red-cloak-threat-detection-and-response-tdr) adapter connection.
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

* **Use stored credentials from the Secureworks Taegis XDR (Red Cloak TDR) adapter** - Select this option to use the the first connected Secureworks Taegis XDR (Red Cloak TDR) adapter credentials.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Secureworks Taegis XDR (Red Cloak TDR)](/docs/secureworks-red-cloak-threat-detection-and-response-tdr) adapter connection.
  </Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Tag** - The tag to be added or removed.
* **Add or remove tag** - Select the action to perform.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Client ID** and **Client Secret** - The credentials for an account that has the permissions to perform this action.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

  * **Secureworks Region** *(default: US1)* - Select the region of your domain.

    <Callout icon="📘" theme="info">
      Region Identification

      The following URLs are associated with each drop-down selection on the connection configuration panel:

      * **US1** - *[https://api.ctpx.secureworks.com](https://api.ctpx.secureworks.com)*
      * **US2** - *[https://api.delta.taegis.secureworks.com](https://api.delta.taegis.secureworks.com)*
      * **EU** - *[https://api.echo.taegis.secureworks.com](https://api.echo.taegis.secureworks.com)*
    </Callout>

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## APIs

Axonius uses the [Assets GraphQL API ](https://docs.ctpx.secureworks.com/apis/assets_api/#createassettag-type-tag) API.

## Required Permissions

The values supplied in [Connection Parameters](#connection-parameters) above must have permission to add and remove tags from assets.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).