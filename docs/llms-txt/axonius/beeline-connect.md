# Source: https://docs.axonius.com/docs/beeline-connect.md

# Beeline Professional Edition Connect

Beeline Professional Edition Connect is a workforce management solution that offers vendor management and talent acquisition capabilities.

### Asset Types Fetched

* Users

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* Client ID/Client Secret

### APIs

Axonius uses the [Beeline Professional Edition XML API](https://oc.pages.utmost.co/xml-api.html#tag/Users).

### Permissions

Authentication is handled using OAuth Client Credentials flow. To get a token, make a POST request to `/api/integration/client/oauth/token` with your `client_id`, `client_secret`, and `grant_type=client_credentials`.

The `client_id` is configured by a system administrator and is tied to ABAC (Attribute-Based Access Control) policies. These policies define which actions (read, create, update, delete) are allowed on which resources, even down to individual fields.

To access the `/uc/api/connect/v1/users` endpoint, your `client_id` must have a policy that allows reading user data. If the appropriate policy is not in place, the API will return an error such as 403 Forbidden.

#### Supported From Version

Supported from Axonius version 7.0.2

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(default: `https://tenant.utmost.co`)* - The hostname or IP address of the Beeline server.
2. **Client ID** and **Client Secret**  - The credentials for a user account that has the  Required Permissions to fetch assets.

<Image alt="Beeline Professional Edition Connect.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Beeline%20Professional%20Edition%20Connect.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />

## &#x20;Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Fetch Users of sub type user from Users** - Select this option to fetch user data from the /uc/api/connect/v1/users endpoint.
2. **Fetch Users of sub type Worker from Workers**  **(default enabled)** -  Select this option to fetch  worker data from the /uc/api/connect/v1/workers endpoint.
   1. **Classification Reference Codes** - Enter a comma separated list of of classification reference codes to filter by. If not provided, all workers will be fetched.