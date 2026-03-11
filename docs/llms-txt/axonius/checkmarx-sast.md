# Source: https://docs.axonius.com/docs/checkmarx-sast.md

# Checkmarx SAST

Checkmarx SAST (CxSAST) is a static application security testing solution used to identify security vulnerabilities in custom code. It is used by development, DevOps, and security teams to scan source code early in the SDLC, identify vulnerabilities, and provide actionable insights to remediate them.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Business Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Checkmarx SAST server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Checkmarx SAST" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Checkmarx%20SAST.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch projects as assets** -  Select this option to ingest Checkmarx projects as Device Entities.
2. **Fetch engine servers as assets** - Select this option to ingest "Engine Servers" as Devices.
3. **Last scan to include in project** -  Specify the number of past scans to include in each project.  (Default is 1: only the most recent).
4. **Include only active users** - Select this option to only fetch active users.
5. **Parse applications as devices** - Select this option to parse applications as devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the following APIs:

* Devices: [Checkmarx SAST API](https://checkmarx.stoplight.io/docs/checkmarx-sast-api-reference-guide/2aqowtq5uxtec-step-1-requesting-an-access-token-for-authentication)
* Users: [Checkmarx SAST Access Control (REST) API](https://docs.checkmarx.com/en/34965-46624-using-the-access-control--rest--api.html)

## Required Permissions

The value supplied in [User Name](#parameters) must have SAST Admin role.