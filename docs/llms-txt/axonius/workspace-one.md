# Source: https://docs.axonius.com/docs/workspace-one.md

# Workspace One - Intelligence Report API

Workspace ONE Intelligence reporting uses a cloud-based report storage system to gather data and create the reports.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **API Domain** *(required)* - The API Domain, in the format `https://api.{region}.data.vmservices`

2. **Authentication Domain** *(required)* - The credentials for a user account that has  permission to fetch assets, in the format `https://auth.{region}.data.vmservices`

3. **Client ID** and **Client Secret** *(required)* - Credentials  associated with a user account that has permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="WorkspaceOneIntelligenceReport" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WorkspaceOneIntelligenceReport.png" />

## APIs

Axonius uses the [Workspace ONE Intelligence API](https://techzone.vmware.com/getting-started-workspace-one-intelligence-apis-workspace-one-operational-tutorial#downloading-the-report)

## Supported From Version

Supported from Axonius version 6.0