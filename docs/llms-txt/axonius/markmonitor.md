# Source: https://docs.axonius.com/docs/markmonitor.md

# MarkMonitor

MarkMonitor provides domain management, security, and consulting.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Users, Domains & URLs

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the MarkMonitor server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **API Key** *(optional)* - An API Key associated with a user account that has permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. **Fetch Users** *(default: true)* - By default Axonius fetches users. Clear this option to not fetch users.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![MarkMonitor](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MarkMonitor.png)

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [MarkMonitor RestAPI v2](https://corp.markmonitor.com/domains/setup/restapi/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80**
* **TCP port 443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| v2      | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.7