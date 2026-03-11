# Source: https://docs.axonius.com/docs/micro-strategy.md

# MicroStrategy

MicroStrategy is an analytics platform that provides data discovery, reporting, and visualization capabilities for enterprise data assets.

The MicroStrategy adapter provides Axonius with visibility into your analytics platform assets, including user and privilege data.

## Asset Types Fetched

* Users

## Data Retrieved through the Adapter

The adapter retrieves information to provide visibility into your publicly accessible assets. The retrieved data for each asset type may include:

* **Users** - Data such as user ID, name, description, account status (enabled/disabled), date created, and default email address.
* **Privileges** - Complex field data including privilege ID, name, description, categories, and level for both server and project levels.

## Before You Begin

### Required Ports

* TCP Port 443

### Authentication Methods

* **Session-Based Authentication** - The adapter uses a session-based flow where it exchanges the provided username and password for an X-MSTR-AuthToken and session cookies to authenticate subsequent requests.

### Required Permissions

The adapter connection requires that the user account used to connect has the following permissions within the MicroStrategy environment:

* **Web User Access** - Required to establish a connection session and obtain the necessary authentication tokens.
* **User Management** - Required to retrieve detailed user information and associated privilege data.
* **User Listing** - Ability to browse and enumerate users and groups within the platform.
* **Privilege Auditing** - Ability to view server-level and project-level permissions for specific users.

### APIs

Axonius uses the <Anchor label="MicroStrategy REST API" target="_blank" href="https://demo.microstrategy.com/MicroStrategyLibrary/api-docs/index.html">MicroStrategy REST API</Anchor> to retrieve asset data.

### Supported from Version

This adapter is supported from Axonius version 8.0.12.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - Enter the base URL of the MicroStrategy Library environment.
2. **User Name** - Enter the username for the account with the required API privileges.
3. **Password** - Enter the password associated with the username.

<Image align="center" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/MicroStrategy_Add_Connection.png" className="border" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />