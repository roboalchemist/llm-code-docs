# Source: https://docs.axonius.com/docs/jetbrains-users.md

# JetBrains Users

JetBrains is an integrated development environment (IDE) for software development that provides a suite of tools and features to help developers write, test, and deploy code.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Hub Service URL** *(required)* - The hostname or IP address of the JetBrains Users server.

2. **Permanent Token** *(optional)* - An API Key associated with a user account that has permissions to fetch assets. For more information, see [Permanent Token Authorization](https://www.jetbrains.com/help/youtrack/devportal/OAuth-authorization-in-youtrack.html).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![JetBrains Users](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/JetBrains%20Users.png)

## APIs

Axonius uses the [Youtrack and HUB API](https://www.jetbrains.com/help/youtrack/devportal/rest-api-user-resources.html#hub-rest-api-url).

## Supported From Version

Supported from Axonius version 6.1.37.0