# Source: https://docs.axonius.com/docs/webroot-endpoint-protection.md

# Webroot Endpoint Protection

Webroot Endpoint Protection protects against threats across email, browsers, files, URLs, ads, apps, and more.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Webroot Domain** *(required)* - The hostname or IP address of the Webroot Endpoint Protection server.

2. **GSM Key** *(required)* - The Webroot GSM to query the API.

3. **Site ID** *(optional)* - The Webroot site key composed of a 32-digit  UUID (Universal Unique Identifier). If omitted, the adapter will attempt to fetch all sites that the API client has permissions to retrieve.

4. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

5. **Client ID** and **Client Secret** *(required)* - The Client ID and Client Secret associated with a user account that has the permissions to fetch assets. Follow these instructions to [Create API Client Credentials](https://docs.webroot.com/us/en/business/wsab_globalsitemanager_adminguide/Content/WorkingWithSettings/CreatingAPIClientCredentials.htm).

6. **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **Webroot Domain**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Webroot Domain**.

8. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Webroot Domain** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Webroot Domain** via the value supplied in **HTTPS Proxy**.

10. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="Webroot.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Webroot.png" />

## APIs

Axonius uses the [Webroot Unity API](https://unityapi.webrootcloudav.com/Docs/en/APIDoc/APIReference).

<Callout icon="📘" theme="info">
  Note

  Axonius now requires the **Console.GSM** scope instead of the **SkyStatus.Reports** scope.
</Callout>