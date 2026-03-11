# Source: https://docs.axonius.com/docs/beyondtrust-remote-support-update-jump-client.md

# BeyondTrust Remote Support - Update Jump Client

**BeyondTrust Remote Support - Update Jump Client** updates Jump Client resources in BeyondTrust Remote Support for:

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

* **Use stored credentials from the BeyondTrust Remote Support adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [BeyondTrust Remote Support](/docs/beyondtrust-remote-support) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

* **Map Axonius fields to Jump Client fields** - Configure dynamic values to map Axonius asset fields to Jump Client properties that should be updated. Select the Jump Client field to update and map it to the corresponding Axonius field value.

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Domain** - The hostname or IP address of the BeyondTrust Remote Support server.

  * **Client ID** and **Client Secret** - OAuth client ID and client secret associated with a user account that has the [Required Permissions](#required-permissions) to update Jump Clients.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## APIs

Axonius uses the [BeyondTrust Remote Support Configuration API](https://www.beyondtrust.com/docs/remote-support/how-to/integrations/api/configuration-api.htm) - PATCH `/api/config/jump-client/{id}`.

## Required Ports

Axonius must be able to communicate via the following ports:

* TCP port 80/443

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

The values supplied in [**Client ID** and **Client Secret**](#additional-fields) must be associated with a user account with the following permissions:

* **Configuration API** - Allow access (must be enabled in the API Configuration section)
* **Command API** - Read-Only or Full Access permissions
* Jump Client management permissions

### Creating an API Account

**To create an API account for this Enforcement Action**

1. Go to `https://<your-beyondtrustremotesupport-domain>/login` and log in using your username and password.

2. From the left menu, click **Management**, and then click the **API Configuration** tab.

3. In the **API Configuration** section, make sure the **Enable XML API** and **Enable Configuration API** options are selected.

4. In the **API Accounts** section, click **+Add** to add a new API account. The Account Settings page opens for the new account.

5. In **Name**, enter a domain name (for example: 'Axonius').

6. For the credentials for the BeyondTrust Adapter's scheme, use:
   * **OAuth Client ID** (listed on the current page)
   * **OAuth Client Secret** (listed on the current page, and will be visible only once.) You can regenerate it by clicking **Generate New Client Secret**.

7. In the new account's **Permissions** section:
   * Under **Command API**, select the **Read-Only** or **Full Access** option.
   * Under **Configuration API**, select the **Allow Access** option.

8. Add your public IP to the **Network Address Allow List** in the new account's **Network Restrictions** section.

9. Click **Save Changes**. You can now use the credentials provided (Domain name, Client ID, Client Secret) in the Axonius enforcement action configuration.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).