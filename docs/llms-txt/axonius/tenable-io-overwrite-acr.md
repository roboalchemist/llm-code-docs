# Source: https://docs.axonius.com/docs/tenable-io-overwrite-acr.md

# Tenable.io - Overwrite ACR

**Tenable.io - Overwrite ACR** updates the ACR score of assets returned by the selected query **or** assets selected on the relevant asset page, and sends the assets' UUID and updated score to Tenable.io.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## APIs

Axonius uses the [Tenable Update ACR API](https://developer.tenable.com/reference/assets-bulk-update-acr).

In addition, the following are required to successfully run this Enforcement Action:

**API endpoint:** POST /api/v2/assets/bulk-jobs/acr

**User role:** Scan Operator \[24] user role

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from Tenable.io adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Tenable.io](/docs/tenableio) adapter connection.
  </Callout>

* **ACR score** - The new ACR score to assign to the assets. Must be a number between 1 and 10.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Tenable.io Domain** - The hostname of the Tenable.io server. When fetching assets and vulnerabilities, a different hard-coded domain is used (currently [https://cloud.tenable.com](https://cloud.tenable.com)).

  * **Access API Key** and **Secret API Key** - An API Key + Secret associated with a user account that has the Required Permissions to fetch assets.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).