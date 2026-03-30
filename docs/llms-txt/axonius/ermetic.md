# Source: https://docs.axonius.com/docs/ermetic.md

# Ermetic

Ermetic is a cloud infrastructure security platform, focusing on identity protection.

The Ermetic adapter enables Axonius to fetch and catalog cloud infrastructure assets, including devices, users, vulnerabilities (Aggregated Security Findings), and SaaS applications, ensuring comprehensive visibility into identity risks and cloud security posture.

## Asset Types Fetched

* Devices
* Aggregated Security Findings
* Users
* SaaS Applications
* Databases
* Object Storage
* Serverless Functions

## Before You Begin

### Authentication Methods

* API Key

### Required Permissions

The user account used for the connection must have permissions to fetch assets via the Ermetic API.

### Creating an API Token

1. From the Ermetic platform, navigate to **Settings (<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Settings_cog.png" />)**  > **API** > **Create Token**.
2. Specify a name for the token.
3. Select the permission. For more information about each role, see <Anchor label="Permissions by Role" target="_blank" href="https://us.app.ermetic.com/docs/administration/administrativeAccess/permissionsByRole/index">Permissions by Role</Anchor>.
4. Click **Create Token**.
5. After the token is created, make sure to copy the token value to a secure location, as it cannot be viewed again.

### APIs

Axonius uses the <Anchor label="Ermetic API" target="_blank" href="https://us.app.ermetic.com/docs/api/index">Ermetic API</Anchor> to retrieve asset data.

### Supported from Version

This adapter is supported from Axonius version 4.5.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** *(default: `https://us.app.ermetic.com`)* - Enter the hostname or IP address of the Ermetic server.

2. **API Key** - Enter the API token associated with a user account that has permissions to fetch assets. To create an API token, see <Anchor label="Creating a new API Token" target="_blank" href="/docs/ermetic#creating-a-new-api-token">Creating a new API Token</Anchor>.

<Image alt="Ermetic" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Ermetic.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Device types to fetch** - From the dropdown select one or more device types to fetch (default: AWS EC2 Instances and Azure Compute Virtual Machines).
2. **Fetch AWS users** - Select this option to fetch AWS users.
3. **Fetch Azure users** - Select this option to fetch Azure users.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| 1.26    | Yes       |       |

<br />