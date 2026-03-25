# Source: https://docs.axonius.com/docs/mcafee-mvision.md

# Trellix MVision

Trellix MVision is a CASB solution that protects data and stops threats in the cloud across SaaS, PaaS, IaaS, and on-premise environments.

Note: This adapter was formerly called McAfee MVision Cloud (pre version 6.0.10).

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Trellix MVision server. The default value is *[https://api.mvision.mcafee.com](https://api.mvision.mcafee.com)*.
2. **Client ID** *(required)* -  A client ID. Create the client ID as follows: Login to the MVISION EPO console and open a new tab, and go to the [McAfee MVision sign in page](https://auth.ui.mcafee.com/email.html#redirect_uri=https://auth.ui.mcafee.com/support.html). Copy the value of client\_id.
3. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. Refer to [APIs](/docs/mcafee-mvision#apis) for information about how to generate the API Key.
4. **Client Secret**  *(optional)* - The Client Secret. Refer to (#APIs) for information about how to generate the Client Secret.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **Client Secret** is required. Client Secret is the preferred method of Authentication.
</Callout>

5. **User Name** and **Password** *(optional)* - The credentials for a user account that has the permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **Client Secret** is not supplied, **User Name** and **Password** are required.
</Callout>

6. **Permission Scope** - The scope of permission to grant. The default value is *epo.admin*.

7. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

8. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

9. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

10. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="TrellixMVision" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TrellixMVision.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Maximum number of retries for each request** *(required, default: 5)* - Requests sent to Trellix may return errors from the Trellix side. This is the maximum number of retries per request sent to the server (as opposed to the total amount of retries).
2. **Time to wait before retrying requests**  - Time (in seconds) to wait after an unsuccessful (for any reason) request before retrying.

<Callout icon="📘" theme="info">
  Note

  Every Client ID has a request cap on the MVision API. This adapter is optimized to deliver all the devices using the smallest number of requests possible.
  If fetches fail periodically and intermittently (success, then failure, then success, then failure, …), change the fetch schedule.
</Callout>

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [ MVision API](https://developer.manage.trellix.com/).

### Generating the API Key

Login to the [MVision Developer Portal](https://developer.manage.trellix.com/mvision/docs/umam)

1. Select *Documentation*
2. Select *MVision Developer Portal*
3. Select  *Self Service*
4. Select  *API Access Management*
   The API Key is displayed at the top of the key, copy the API key.
5. Click generate Client Secret to generate a client secret and copy it.

## Required Permissions

The value supplied in [User Name](#parameters) must have epo.device.r permissions to fetch assets.

The value supplied in [API Key](#parameters) must be associated with credentials that have epo.device.r permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.5