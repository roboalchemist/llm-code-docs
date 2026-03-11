# Source: https://docs.axonius.com/docs/apache-cloudstack.md

# Apache CloudStack

Apache CloudStack is open-source software used to deploy and manage large networks of virtual machines.

## Assets  Types Fetched

Devices, Users, Domains & URLs, Networks

## Before You Begin

<br />

### APIs

Axonius uses the [Apache CloudStack: API Documentation](https://cloudstack.apache.org/api.html).

### Required Permissions

**Minimum recommended role** - Domain Administrator

The API key must have permissions to call the following CloudStack API commands:

**Always Required:**

* `listVirtualMachines` - Fetches device/VM data

**Conditionally Required (based on advanced settings enabled):**

* `listUsers` - Required when `fetch_users` is enabled
* `listDomains` - Required when `fetch_domains` is enabled
* `listNetworks` - Required when `fetch_networks` is enabled
* `listPublicIpAddresses` - Required when `fetch_networks` is enabled

**Note:** The adapter uses the `listall=true` parameter which requires Domain Administrator or Root Administrator level permissions to view all resources within the domain.

## Creating an API Key and Secret Key

To create an API Key and Secret Key in Apache CloudStack:

1. Login as an admin.
2. Navigate to **Accounts**.
3. Select the account in which the user is a member.
4. Click **View Users**.
5. Select the user.
6. Click **Generate Keys.** From the detailed view, the API Key and Secret Key are displayed.

<br />

#### Supported From Version

Supported from Axonius version 4.5

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address**  - The hostname or IP address of the Apache CloudStack server.

2. **API Key** and **Secret Key**- An API key and Secret key associated with a user account that has permissions to fetch assets. To create an API Key and Secret Key, see [Creating an API Key and Secret Key](/docs/apache-cloudstack#creating-an-api-key-and-secret-key).

<Image align="center" alt="CloudStack" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CloudStack.png" />

### Optional Parameters

1. **Verify SSL** *(required, default: False)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

5. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Fetch users** - Select this option to fetch users.
2. **Fetch domains** - Select this option to fetch domains.
3. **Fetch networks** - Select this option to fetch networks.

<br />

## &#x20;Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version  | Supported | Notes |
| -------- | --------- | ----- |
| 4.13.1.0 | Yes       |       |

<br />