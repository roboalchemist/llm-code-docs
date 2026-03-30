# Source: https://docs.axonius.com/docs/skillcast.md

# Skillcast

Skillcast is a platform that offers compliance training and e-learning solutions.

The Skillcast adapter enables Axonius to fetch and catalog users, providing visibility into their compliance status and training assignments.

## Asset Types Fetched

* Users

## Data Retrieved through the Adapter

* **User Identity** - User Name, Email, Employee ID, and internal User ID.
* **Training and Compliance** - Assignment titles, completion status, deadlines, and exemption details.

## Before You Begin

### Required Ports

* TCP port 443 (HTTPS)

### Authentication Methods

* **Token-based (default)** - The adapter uses the credentials to retrieve a session (bearer) token for subsequent requests.
* **Basic** - The adapter sends the username and password encoded in the request headers.

### Required Permissions

The adapter requires a dedicated **Integration User** account with the following permissions configured in the Skillcast Management Console:

* **API and Integration Access** - The account role must have the API access explicitly enabled.
* **Read Access** - The account requires **Read-only** access to user assignments.
* **Read/Write Access** - The account requires **Read/Write** access to employees.

### APIs

Axonius uses the <Anchor label="Skillcast API" target="_blank" href="https://apidocs.skillcast.io/">Skillcast API</Anchor> to retrieve asset data..

* **Base URL** - `https://<Skillcast Domain>/skillcastapi/`
* **Primary Endpoints** -
  * Fetch Users - `/employees`
  * Fetch Training - `/employees/{userId}/assignments`

### Supported from Version

This adapter is supported from Axonius version 8.0.4.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Skillcast Domain** - Enter the domain of your Skillcast instance (for example: `client-name.skillcast.io`) .

2. **User Name** and **Password** - Enter the credentials for a user account that has permission to fetch assets.

<Image align="center" alt="Skillcast adapter - Add Connection" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Skillcast_Add_Connection.png" className="border" />

### Optional Parameters

1. **Use Basic Authentication** - Select this option to force HTTP basic authentication instead of generating a session token.

2. **Verify SSL** - Select (selected by default) whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).