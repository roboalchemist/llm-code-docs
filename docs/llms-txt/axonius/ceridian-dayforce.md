# Source: https://docs.axonius.com/docs/ceridian-dayforce.md

# Ceridian Dayforce

Ceridian Dayforce is an HR cloud platform that delivers payroll, benefits, workforce, and talent management.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Managed Identities

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Ceridian Dayforce server.

2. **Client Namespace** *(required)* - Specify the Client Namespace of the Ceridian Dayforce server.

3. **Use the redirect URI to receive the response** *(default: disabled)* - The adapter needs to connect to a version-specific URL to function. When the Ceridian Dayforce cloud application is updated, this URL can change. When the adapter tries to connect to the outdated URL, it receives an error message that includes the new redirect URL.
   * When this option is enabled, the adapter automatically detects the new URL in the error message and uses it to update the **Host Name or IP Address** field in the adapter's connection. This means that the adapter continues to work without any manual intervention.
   * When this option is disabled, the adapter’s connection breaks whenever the URL changes. To restore connectivity, you must copy the new URL from the error message and update the adapter's connection settings yourself.

4. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="CeridianDayforce1" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CeridianDayforce1.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Async Chunks** *(optional, default: 20)* - Specify the number of chunks of the asynchronous parallel requests for all connections to fetch.
2. **Use Employee Number for Employee ID** *(optional)* - Select to force Axonius to set the aggregated **Employee ID** field with the Employee Number from the Ceridian Dayforce adapter to correlate users.

<Callout icon="📘" theme="info">
  Note

  Only select **Use Employee Number for Employee ID** when correlation results aren't correct.
</Callout>

3. **Enable real-time asset updates (Supported events: New hires, New terminations)** - When enabled, the system regularly fetches data from Ceridian Dayforce and checks it for new hires and terminations. It then activates any workflows configured with the Ceridian Dayforce New Hire and New Termination events.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Dayforce API](https://usconfig60.dayforcehcm.com/api/ddn/swagger/). /V1/Employees endpoint

[ Dayforce Documentation](https://developers.dayforce.com/Special-Pages/Welcome-Page.aspx?returnurl=%2FBuild%2FHome.aspx)​The following Ceridian Dayforce expanders are used: 'EmploymentStatuses, WorkAssignments, Contacts, EmployeeManagers'

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443/8080**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                     | Supported | Notes |
| --------------------------- | --------- | ----- |
| Ceridian Dayforce Version 1 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.5

## Related Enforcement Actions

* [Ceridian Dayforce - Update Employee](https://docs.axonius.com/axonius-help-docs/docs/ceridian-dayforce-update-employee)