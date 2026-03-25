# Source: https://docs.axonius.com/docs/huntress.md

# Huntress

Huntress is a managed endpoint detection and response (EDR) solution.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required, default: api.huntress.io )* - The hostname or IP address of the Huntress server.

2. **Organization ID** - The organization ID of the specific organization the customer wishes to fetch devices from.

3. **API Key** *(required)* - An API Key associated with a user account that has    Permissions  to fetch assets. Generate an API Key on the API Key generation page from Huntress at .huntress.io/account/api\_credentials

4. **API Key Secret** *(required)* - The API Key Secret, this is displayed when the API key is created.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

9. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Huntress](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Huntress.png)

## APIs

Axonius uses the [Huntress API](https://api.huntress.io/docs#introduction).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP ports 80/443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version     | Supported | Notes |
| ----------- | --------- | ----- |
| Huntress v1 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.7