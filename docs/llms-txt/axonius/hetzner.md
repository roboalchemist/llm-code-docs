# Source: https://docs.axonius.com/docs/hetzner.md

# Hetzner

Hetzner is a hosting provider that offers dedicated servers and cloud solutions for various IT needs.

The Hetzner adapter enables Axonius to fetch and catalog compute instances, server metadata, and network configurations, ensuring comprehensive visibility into your cloud infrastructure resources.

## Asset Types Fetched

* Devices

## Data Retrieved through the Adapter

* **Devices** - Server status, IP addresses (public/private), MAC addresses, server type details (cores, memory, disk), architecture, and OS details (flavor, version).

## Before You Begin

### Required Ports

* TCP port 443

### Authentication Methods

* API Key (API token)

### Required Permissions

The API Key used for the connection must be associated with an account that has permissions to fetch assets via the Hetzner Cloud API.

* **Server Access** - The API Key must have permissions to discover servers (`GET /servers`) and retrieve server metadata.
* **Network and Storage** - The permissions must allow access to associated network configurations and storage metadata to ensure complete asset details are fetched.

### APIs

Axonius uses the <Anchor label="Hetzner Cloud API" target="_blank" href="https://docs.hetzner.cloud/reference/cloud#overview">Hetzner Cloud API</Anchor> to retrieve asset data.

### Generating the API Key (Token)

1. Log in to the <Anchor label="Hetzner Cloud Console" target="_blank" href="https://console.hetzner.cloud">Hetzner Cloud Console</Anchor>.
2. Select the **Project** you want to connect to Axonius.
3. In the left navigation menu, click **Security**.
4. Select the **API Tokens** tab.
5. Click **Generate API Token**.
6. Enter a description for the token (for example: "Axonius Adapter").
7. Select **Read** permissions.
8. Click **Generate API Token**.
9. Copy the token and save it in a secure location.

### Supported from Version

This adapter is supported from Axonius version 8.0.7.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name** or **IP Address** - Enter the hostname or IP address of the Hetzner Cloud API (for example: `https://api.hetzner.cloud/v1`).
2. **API Key** - Enter the API token generated from the Hetzner Cloud Console.

<Image align="center" alt="Hetzner adapter - Add Connection" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Hetzner_Add_Connection.png" className="border" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).