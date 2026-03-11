# Source: https://docs.axonius.com/docs/disable-lastpass-user.md

# LastPass - Disable Users

**LastPass - Disable Users** disables each LastPass user that matches the parameters of the selected saved query, and match the Enforcement Action Conditions, if defined, or assets selected on the relevant asset page.

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

* **Use stored credentials from LastPass adapter** - Select this option to use the first connected LastPass adapter credentials.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

* **Account Type** *(default: LastPass API)* - Select the Account Type from the dropdown.
  * If the Account Type selected is **LastPass API**, provide values for the following parameters:
    1. **Host Name or IP Address** *(default: `https://identity-api.lastpass.com`)* - The hostname or IP address of the LastPass server that Axonius can communicate via the [Required Ports](#required-ports).
    2. **API Key** - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to perform this action.
    3. **Public Key File** and  **Private Key File** - Click **Choose file** to upload the Public key file and Private key file, used for authentication. For more information, see [Generating Keys](/docs/lastpass) under **Required Permissions**.
  * If the Account Type selected is **LastPass Business API**, provide values for the following parameters:
    1. **Host Name or IP Address** *(default: `https://lastpass.com`)* - The hostname or IP address of the LastPass server that Axonius can communicate via the [Required Ports](#required-ports).
    2. **CID (Account number)** - Specify the CID (account number) used to make requests to the LastPass Business API.
    3. **Provisioning hash** - Specify the provisioning hash used to make requests to the LastPass Business API.
       To obtain the CID and provisioning hash, see [Generating the CID and Provisioning Hash](/docs/lastpass) under **Required Permissions**.
* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.
* **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
  <br />

## APIs

Axonius integrates with APIs for LastPass Personal and LastPass Business accounts.

* If you have a LastPass Personal account, you can use the legacy [ LastPass Plain Auth API](https://mfa-developer.lastpass.com/index.html@p=263.html).
* If you have a LastPass Business account, it is preferable to use the [LastPass Business API](https://admin.lastpass.com/advanced/enterpriseApi/api-reference).

## Required Ports

Axonius must be able to communicate with the value supplied in [Connection Settings](#Connection-Settings) via the following ports:

* TCP port 443

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).