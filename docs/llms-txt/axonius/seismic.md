# Source: https://docs.axonius.com/docs/seismic.md

# Seismic

Seismic is a unified AI-powered sales enablement platform that provides customer-facing teams with the skills, content, tools, and insights needed to engage buyers and drive revenue growth.

The Seismic adapter enables Axonius to fetch and catalog users, roles, and entitlements, providing comprehensive visibility into access governance and system settings within the platform.

## Asset Types Fetched

* Users
* Roles

## Data Retrieved through the Adapter

* **Users** - Full name, email address, user ID, status, and assigned roles.
* **Roles** - Role names, permissions, and security role configurations.

## Before You Begin

### Required Ports

* TCP port 443

### Authentication Methods

* OAuth 2.0 with Client Credentials

### Required Permissions

The credentials used for the connection must be associated with an account that has an administrative role within the Seismic tenant.

### Generating the Client ID and Client Secret

1. Log in to your Seismic instance as an Administrator.
2. Navigate to **Settings > Integration Management** (or **Developer Portal**).
3. Select **App Management** or **Connected Apps**.
4. Select the option to create a new application for the **OAuth 2.0 Client Credentials** flow.
5. Assign a name to the application (e.g., "Axonius Adapter").
6. Ensure the following **Required Scopes** are assigned to the application:
   1. `seismic.reporting`
   2. `seismic.user.view`
7. Generate the credentials.
8. Copy the **Client ID** and **Client Secret** and save them in a secure location.

For more information, see the <Anchor label="Login with client credentials flow" target="_blank" href="https://developer.seismic.com/seismicsoftware/reference/login-with-client-credentials-user-delegation-flow">Login with client credentials flow</Anchor> on the Seismic website.

### APIs

Axonius uses the <Anchor label="Seismic API" target="_blank" href="https://developer.seismic.com/seismicsoftware/reference/introduction-overview">Seismic API</Anchor> to retrieve asset data.

### Supported from Version

This adapter is supported from Axonius version 8.0.8.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - Enter the the hostname or IP address of the Seismic server (default: `https://api.seismic.com`).
2. **Tenant** - Enter the name of your specific Seismic tenant.
3. **User ID** - Enter the User ID of the administrative account.
4. **Client ID** - Enter the Client ID generated from the Seismic portal.
5. **Client Secret** - Enter the Client Secret associated with the **Client ID**.

<Image align="center" alt="Seismic adapter - Add Connection" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Seiemic_Add_Connection.png" className="border" />

### Optional Parameters

1. **API Tier** - Select the API tier that corresponds to your Seismic subscription level (default: **Tier 1**). This setting ensures that Axonius respects the specific rate limits and throttling thresholds associated with your Seismic instance.

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Enrich List Users Endpoint with List Roles Endpoint** - Toggle this option on to include detailed role information for each fetched user.
2. **Fetch SecurityRoles from List Roles Endpoint** - Toggle this option on to retrieve additional security-specific roles from the roles endpoint.