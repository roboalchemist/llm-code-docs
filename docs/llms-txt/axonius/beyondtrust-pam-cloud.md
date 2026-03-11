# Source: https://docs.axonius.com/docs/beyondtrust-pam-cloud.md

# BeyondTrust Privilege Management Cloud

BeyondTrust Privilege Management Cloud delivers privilege management and application control, allowing organizations to eliminate admin rights across the entire business and enforce least privilege.

## Asset Types Fetched

* Devices, Users

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* Client ID/Client Secret

### APIs

Axonius uses the [Endpoint Privilege Management API - version 1](https://www.beyondtrust.com/docs/privilege-management/console/pm-cloud/api/v1/index.htm).

To authenticate to the PM Cloud API and create a token, see [Authenticate to the PM Cloud API](https://www.beyondtrust.com/docs/privilege-management/console/pm-cloud/api/index.htm).

### Permissions

The value supplied in [Client ID](#required-parameters) must have Read-only permissions to fetch assets.

#### Supported From Version

Supported from Axonius version 4.6

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the BeyondTrust Privilege Management Cloud server. This should be in the format of: `https://[yourProductionSub-domainName]-services.pm.beyondtrustcloud.com`
2. **Client ID** and **Client Secret** - The credentials for a user account that has the Required Permissions to fetch assets.
   To obtain the Client ID and Client Secret, see [Configure Access to the Management API](https://www.beyondtrust.com/docs/privilege-management/console/pm-cloud/configuration/configure-api-settings.htm).
3. **API Version** *(default: v1)* - Select the API Version you want to use to connect, either v1 or v3.

![BeyondTrust%20Privilege%20Management%20Cloud](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BeyondTrust%20Privilege%20Management%20Cloud.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Avoid Duplications** - Select this option to choose the record with the latest "Last Seen" value if the device has the same hostname and the same domain.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>