# Source: https://docs.axonius.com/docs/hunters-security-add-identifiers-to-tag.md

# Hunters Security - Add Identifiers to Tag

**Hunters Security - Add Identifiers to Tag** adds identifiers to tags in Hunters Security for:

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

These fields must be configured to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the [Hunters](https://docs.axonius.com/axonius-help-docs/docs/hunters-security) adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

    <Callout icon="📘" theme="info">
      To use this option, you must successfully configure a [Hunters](https://docs.axonius.com/axonius-help-docs/docs/hunters-security) adapter connection.
    </Callout>

* **Tag UUID** - Enter the tag UUID to which to add identifiers.

* **Tag Identifiers** - Fill in the following fields:
  * **Identifier Type** - Select the identifier type.
  * **Kind** - Select the identifier kind.
  * **Value** - Enter the identifier value.

* Click **Add Identifiers** to add multiple identifiers.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** - The hostname or IP address of the Hunters server.
  * **Client ID** and **Client Secret** - The credentials for a user account that has the Required Permissions to fetch assets.
  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.
  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## APIs

Axonius uses the Hunters API.

## Required Ports

Axonius must be able to communicate via the following ports:

* TCP port 443

## Required Permissions

* **Access Control Philosophy** - Hunters emphasizes using minimal, tightly scoped access (e.g., read‑only) where possible when setting up API credentials.
* **API token roles** - Assign roles to the API tokens to control which of the platform users can use the API token to gain access to routes using that token. To access Leads & Stories, the API token role of ‘*Customer*’ or higher is needed.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).