# Source: https://docs.axonius.com/docs/beyondtrust-remote-support.md

# BeyondTrust Remote Support

The BeyondTrust Remote Support adapter (formerly Bomgar) allows support technicians to remotely connect to end-user systems through firewalls from their computers or mobile devices.
BeyondTrust returns all devices that have had a session initiated with them.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Domain** *(required)* - The hostname or IP address of the BeyondTrust Remote Support server.

2. **Client ID** and **Client Secret** *(required)* - OAuth client ID and client secret associated with a user account with the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Domain** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Domain** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![beyondtrustremotesupport](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/beyondtrustremotesupport.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can apply to all connections for this adapter or a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Maximum days of history to fetch** *(optional, default: 7)* - Enter the maximum days of history to fetch clients. This field must have a value in it to perform the fetch.
2. **Fetch Jump Clients** - Select this option to fetch information about [Jump Clients](https://www.beyondtrust.com/products/remote-support/features/jump-clients). This setting requires the [Configuration API](https://www.beyondtrust.com/docs/remote-support/how-to/integrations/api/configuration-api.htm) to be enabled.
3. **Parse public IPs to Network Interfaces** *(default: true)* - This adapter parses public IPs as Network Interfaces by default. Clear this option to not parse public IPs to Network Interfaces.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

The BeyondTrust Remote Support adapter uses the [reporting API](https://www.beyondtrust.com/docs/remote-support/how-to/integrations/api/reporting/index.htm) to get the [Archives listing](https://www.beyondtrust.com/docs/remote-support/how-to/integrations/api/reporting/archive.htm) for the past seven days (archives are saved for up to seven days).

## Required Permissions

The values supplied in [**Client ID** and **Client Secret**](#parameters) must be associated with a user account with read access to devices.

### Creating an API Account

**To create an API account and connect the BeyondTrust Adapter**

1. Go to `https://<your-beyondtrustremotesupport-domain>/login` and log in using your username and password.

   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BeyondTrustRemoteSupportLogin.png)

2. From the left menu, click **Management**, and then click the **API Configuration** tab.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BeyondTrustRemoteSupportManagementAPIConfig.png)

3. In the **API Configuration** section (see above screen), make sure the **Enable XML API** and **Enable Archive API** options are selected.

4. In the **API Accounts** section (see above screen), click **+Add** to add a new API account. The Account Settings page opens for the new account.

   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BeyondTrustRemoteSupportManagementAPIConfigNameOAurh.png)

5. In **Name**, enter a domain name (for example:  'Axonius').

6. For the credentials for the BeyondTrust Adapter's scheme, use:

   * **OAuth Client ID** (listed on the current page)
   * **OAuth Client Secret** (listed on the current page, and will be visible only once.) You can regenerate it by clicking **Generate New Client Secret**.

7. In the new account's **Permissions** section:
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BeyondTrustRemoteSupportAPIConfig.png)

   * Under **Command API**, select the **Read-Only** or **Full Access** option.
   * Under **Reporting API**, select the **Allow Access to Archive Reports** option.

8. Add your public IP to the **Network Address Allow List** in the new account's  **Network Restrictions** section (see above screen).

9. Click **Save Changes**. You can now use the credentials provided (Domain name, Client ID, Client Secret) in the Axonius adapter configuration.

## Related Enforcement Actions

* [BeyondTrust Remote Support - Update Jump Client](https://docs.axonius.com/axonius-help-docs/docs/beyondtrust-remote-support-update-jump-client)
* [BeyondTrust Remote Support - Delete Jump Client](https://docs.axonius.com/axonius-help-docs/docs/beyondtrust-remote-support-delete-jump-client)