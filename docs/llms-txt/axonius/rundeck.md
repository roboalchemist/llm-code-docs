# Source: https://docs.axonius.com/docs/rundeck.md

# Rundeck

Rundeck is an open-source tool that helps to define build, deploy and manage automation.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Rundeck server.

2. **API Token** *(required)* - An API Token associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information on obtaining an API Token, see [API Reference](https://docs.rundeck.com/docs/api/#authentication).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Rundeck](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Rundeck.png)

## APIs

Axonius uses the [Rundeck API](https://docs.rundeck.com/docs/api/).

## Required Permissions

In order to fetch assets, access to the project is required. For further information, refer to [Project Scope Resources and Actions](https://docs.rundeck.com/docs/administration/security/authorization.html#project-scope-resources-and-actions).

## Supported From Version

Supported from Axonius version 6.0