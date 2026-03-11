# Source: https://docs.axonius.com/docs/cisco-identity-intelligence.md

# Cisco Identity Intelligence

Cisco Identity Intelligence (formerly Oort) is an AI-powered solution that provides unified visibility across identity stores, analyzes identity behavior, and enables action on risky access attempts.

The Cisco Identity Intelligence adapter enables Axonius to fetch and catalog identities, providing visibility into behavioral risks and security insights.

## Asset Types Fetched

* Users

## Data Retrieved through the Adapter

* **User Identity** - User ID, display name, login email, and phone numbers.
* **Organizational Details** - Company, department, job title, and user type classification.
* **Status and Activity** - Account status and last active timestamp.
* **Last Sign-In Details** - Complex data including timestamp, location (city, state, country), result, IP address, and sign-in reason.

## Before You Begin

### Required Ports

* TCP port 443 (HTTPS)

### Authentication Methods

* This adapter uses the OAuth 2.0 Client Credentials flow.
* Axonius sends the **Client ID** and **Client Secret** to the **Authentication Domain** (the authorization server) to request a short-lived access token. This token is then used to authenticate API requests made to the **Host Name**.

### Required Permissions

The API user must have:

* Access to the `ListEndUsersConnection` GraphQL query.
* **Read-only** (Viewer) privileges for the end-user data.
* Enumeration of end-user records.

### Configuring the Read-Only Permissions

1. Log in to the Cisco Identity Intelligence console.
2. Navigate to **Integrations > API Access** (or **Add Integration > Add API Client**).
3. Create a new client specifically for Axonius.
4. Assign the **Read-Only** role to this client to limit its scope to fetching user identity data only.
5. Copy the generated **Client ID** and **Client Secret** into the Axonius connection parameters.

### APIs

Axonius uses the <Anchor label="Oort Public APIs" target="_blank" href="https://docs.oort.io/public-api">Oort Public APIs</Anchor> to retrieve asset data.

### Supported from Version

This adapter is supported from Axonius version 8.0.4.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - Enter the hostname or IP address of the Cisco Identity Intelligence server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Authentication Domain**  - Enter the domain used for authentication tokens. This is usually the `Auth0` domain associated with your specific account (for example: `your-tenant.auth0.com`).

3. **Client ID** - Enter the API Client ID generated specifically for Axonius within the Cisco Identity Intelligence console.

4. **Client Secret** - Enter the API Client Secret associated with the Client ID. Treat this as a sensitive password.

<Image align="center" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Cisco_Identity_Intelligence_Add_Connection.png" className="border" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).