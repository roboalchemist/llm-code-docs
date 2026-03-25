# Source: https://docs.axonius.com/docs/netwrix-auditor.md

# Netwrix Auditor

Netwrix Auditor is IT auditing software for detecting security threats and validating compliance.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Netwrix Auditor server.

2. **Port** *(optional)* - The port used for the connection.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Netwrix" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Netwrix.png" />

## APIs

Axonius uses the <Anchor label="Netwrix Auditor API" target="_blank" href="https://docs.netwrix.com/docs/auditor/10_6/api/overview">Netwrix Auditor API</Anchor>.

## Required Permissions

The value supplied in [User Name](#parameters) must have read only permissions  in order to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version               | Supported | Notes |
| --------------------- | --------- | ----- |
| Netwrix Auditor v10.0 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.7