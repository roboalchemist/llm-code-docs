# Source: https://docs.axonius.com/docs/mist.md

# Mist

Mist AI leverages data ingested from numerous sources, including APs, switches and firewalls to optimize user experiences and simplify operations across the wireless access, wired access, and SD-WAN domains.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

* Users - Currently, users = admins (only admins are fetched)

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password for Cloud
* API Key/API Token for on-prem

### APIs

Axonius uses the [Mist API](https://www.mist.com/documentation/mist-api-introduction/).

### Permissions

The value supplied in [User Name](#required-parameters) or [API Token](#required-parameters) and must have 'Observer' permissions to fetch assets.

#### Supported From Version

Supported from Axonius version 4.5

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(default: `https://api.mist.com`)* - The hostname or IP address of the Mist server. You need to use the correct URL for your Mist hosting region. Refer to [Regional Clouds in Mist documentation - page 17](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.juniper.net/documentation/us/en/software/mist/mist-management/mist-management.pdf).  As a result, the URL for the API is allocated according to the region. The APIs are detailed in the tables of 'IP Addresses and Ports to allow' for each Region in the Mist documentation, in the relevant API row for each region . You can also identify this in your Mist Management page, where you will see a URL in the format of `https://manage.ac2.mist.com` in which case their API URL and URL to use in the adapter will be `https://api.ac2.mist.com`.
2. **Organization ID** - The ID of the organization as created in the Mist service.
3. **User Name** and **Password** - The credentials for a user account that has the Required Permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **API Token** is not supplied, **User Name** and **Password** are required.
</Callout>

4. **API Token** - An API Token associated with a user account that has the Required Permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **API Token** is required.
</Callout>

<Image alt="mist.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/mist.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Users** - Select this option to fetch users.
2. **Fetch Clients** - Select this option to fetch WiFi clients.
3. **Enhancing Wireless Client Data with Access Point Name** - Select this option to add the Access Point name to the Wireless Client device type assets.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>