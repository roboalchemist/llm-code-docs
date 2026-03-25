# Source: https://docs.axonius.com/docs/deploy-patches-connectwise-automate.md

# ConnectWise Automate - Deploy Patches

**ConnectWise Automate - Deploy Patches** action is used to deploy patches for the software that results from the saved query supplied as a trigger (or assets that were selected in the asset table).

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

<Callout icon="📘" theme="info">
  Note

  This enforcement action runs on Software assets.
</Callout>

* **Use stored credentials from ConnectWise Automate adapter** - Select this option to use ConnectWise Automate adapter credentials.

  When you select this option, the **Select Adapter Connection** dropdown is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [ConnectWise Automate](/docs/connectwise) adapter connection.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Entity Type** *(default: 0)*
* **Entity ID** *(default: 0)*
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** - The hostname or IP address of the ConnectWise Automate server.

  * **User Name** and **Password** - The credentials for a user account that has the required-permissions to  perform this action.

  * **Client ID** - Create the Client\_id in this [link](https://developer.connectwise.com/ClientID/Partner_Client_IDs).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## APIs

Axonius uses the [ConnectWise API](https://developer.connectwise.com/Products/Automate/Integrating_with_Automate/API/REST).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).