# Source: https://docs.axonius.com/docs/send-asset-data-to-kovrr.md

# Send Assets Data - Kovrr

**Send Assets Data - Kovrr** sends asset details to Kovvr Quantum, according to the proper format for:

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
* **Company ID** - Your company ID in Kovrr.
* **Full Host Name or IP Address** *(default: `https://www.kovrr.app`)* - Enter the full host name or IP address.
* **Client ID** - The ID of the client.
* **Client Secret** - The secret of the client.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **CIS Controls** - Select one or more from the list.
* **NIST Controls** - Select one or more from the list.
* **Aggregate by tags** - Enter tag names to be added to the assets. The assets can then be aggregated by tag.
* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.
* **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Permissions

The account used to access Kovrr must have write permissions in Kovrr.

## Version Matrix

This Enforcement Action has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version   | Supported | Notes |
| --------- | --------- | ----- |
| Kovrr 5.0 | Yes       |       |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).