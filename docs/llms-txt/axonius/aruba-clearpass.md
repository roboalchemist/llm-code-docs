# Source: https://docs.axonius.com/docs/aruba-clearpass.md

# HPE Aruba Networking ClearPass Policy Manager

HPE Aruba Networking ClearPass Policy Manager is a network access control (NAC) solution that allows enterprises to identify devices, enforce policies, and remediate threats.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Aruba ClearPass Domain** *(required)* - Use your HPE Aruba Networking ClearPass Policy Manager domain.

2. **Client ID** and **Client Secret** *(required)* - The client ID and client secret you created to use the Aruba ClearPass API. For more details, see the [Create an Aruba ClearPass RestAPI Client](#/creating-an-aruba-clearpass-restapi-client) section below.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="ArubaCLearPass" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ArubaCLearPass.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Get extended agent information** *(required, default: true)* - Select whether to fetch extended agent information from the ClearPass agent.
2. **Get device fingerprint information** - Select this option to add the fingerprint information to devices.
3. **Do not fetch endpoint devices without 'Last Seen'** - Select this option to ignore endpoint devices without 'Last Seen' during the fetch.
4. **Fetch network devices** *(required, default: true)* - By default Axonius fetches network devices, regardless of the **Do not fetch endpoint devices without 'Last Seen'** setting. Clear this option to not fetch network devices.
5. **Fetch Endpoint devices** *(required, default: true)* - By default Axonius fetches endpoint devices. Clear this option to not fetch endpoint devices.
6. **Set endpoint devices as network infrastructure device** - Select whether to set endpoint devices as network infrastructure devices.
7. **Results per page** *(required, default: 100)*  - Set the number of results per page received for a given request to gain better control on the performance of connections for this adapter.
8. **Asynchronous request chunk size** *(required, default: 100)* - Set the number of async requests to do at once.
9. **Wait time between Asynchronous chunks** *(required, default: 0)* - Set how many seconds to wait between each batch of async requests.
10. **Show Only Devices with Attributes** - Select this option to fetch only devices with attributes.
11. **Parse Full-Username as hostname** - Select this option to parse the "Full-Username" field as hostname from Aruba ClearPass.
12. **Custom field pre-process configuration (JSON)** - Enter a JSON configuration to pre-parse the raw data before parsing the actual device data. Use the following format:

```
{
    "PATH_IN_RAW_DATA": {
    "action": "ACTION_CHOSEN",
    "value": "SOMEVALUE"
    },
    "ANOTHER_PATH": {
    "action": "ACTION_CHOSEN",
    "value": "SOMEVALUE"
    }
}
```

* `PATH_IN_RAW_DATA` - The path to altered field.
* `action` - How to alter the field. The supported actions are: `remove_prefix`, `remove_suffix`
* `value` - The value to be altered.

**Example:** the following JSON configuration modifies the raw data of the value located in `attributes/CustomHostname` by removing the “host/”, prefix, if it exists.

```
{
    "attributes/CustomHostname": {
    "action": "remove_prefix",
    "value": "host/"
    }
}
```

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the Adapter Configuration tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Creating an Aruba ClearPass RestAPI Client

You must create a client to use the Aruba ClearPass API. Consider this client as the App definition on Aruba ClearPass. Without this client, access to the API isn't possible.

**To create the client**

1. Open **Aruba ClearPass Guest** and go to **Administration** –`>` **API Services** –`>` **API Clients** and click **Create API Client**.
2. Provide the following information:
   * Client ID - Creates the connection between the user and the API.
   * Operator Profile - Includes the API Services access rights. Axonius required read-only permissions.
   * Grant Type - Set the OAuth2 authentication method as 'Client Credentials'.
   * Public Client - Make sure this option is cleared.

<Callout icon="📘" theme="info">
  Note

  Read Only Administrator Operator Profile doesn't give API permissions by default.
</Callout>

3. Save changes and copy the **Client ID** and the **Client Secret**.
4. Add the **IP address of the Axonius instance** to the **ClearPass API Access List**.

### Creating a ClearPass Profile

**To create a Profile in ClearPass**

1. From **Operator Logins** `>` **Profile**, select **Edit** to edit the profile that the user created.

<Image align="center" alt="ClearPAssConfig1.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ClearPAssConfig1.png" />

2. From Policy Manager, select **Custom**.
3. Allow Read access to the following:
   * Administrator
   * API Services
   * Devices
   * Insight
   * Onboard
   * Platform
   * Policy Manager

<Callout icon="📘" theme="info">
  Note

  The 'Insight Module' needs to be enabled in order to fetch device IP addresses.
</Callout>