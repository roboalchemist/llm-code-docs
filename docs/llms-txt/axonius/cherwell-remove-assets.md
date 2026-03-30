# Source: https://docs.axonius.com/docs/cherwell-remove-assets.md

# Cherwell - Remove Assets

**Cherwell - Remove Assets** removes asset details from Cherwell for:

* Assets that match the results of the selected saved query, and match the Enforcement Action Conditions, if defined, or assets selected on the relevant asset page.

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

* **Use stored credentials from Cherwell IT Service Management adapter** - Select this option to use the first connected Cherwell IT Service Management adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

    <Callout icon="📘" theme="info">
      Note

      * To use this option, you must successfully configure a [Cherwell IT Service Management](/docs/cherwell) adapter connection.
      * The user name and the password used for the adapter connection must be a user with permissions to create new incidents.
    </Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Cherwell domain** - The hostname or IP address of the Cherwell server.

  * **User name** and **Password** - The user name and the password of a user account that has permissions to read and to modify devices.

  * **Client ID** - Enter the client ID created in the CSM Administrator. For details, see [Cherwell - Obtaining API Client IDs](https://help.cherwell.com/bundle/cherwell_rest_api_940_help_only/page/oxy_ex-1/content/system_administration/rest_api/csm_rest_obtaining_client_ids.html#ObtainingApiClientIds#OpenSwagger#ObtainingApiClientIds#OpenSwagger).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Sleep 1 second every token request** - Select this option to wait before sending authentication tokens.
* **Exclude connections** - From the list, select the connections to ignore. You can select more than one.
* **Remove asset even if target Cherwell domain is different from source Cherwell domain** - When selected, the asset is removed from the Cherwell domain specified in this Enforcement Action even if the Cherwell domain used to add this asset is different.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).