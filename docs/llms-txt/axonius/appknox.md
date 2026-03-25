# Source: https://docs.axonius.com/docs/appknox.md

# Appknox

Appknox is a tool that provides mobile app security testing and analysis. It allows you to identify and fix security vulnerabilities in your mobile apps, ensuring that they are secure and compliant with industry standards.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users, Vulnerabilities, SaaS Applications, Application Resources

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Appknox server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Access Key ID** and **Secret Access Key** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Appknox.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Appknox.png)

## APIs

Axonius uses the Appknox Public API.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

The value supplied in [Access Key ID and Secret Access Key](#parameters) must be associated with credentials that have the following permissions in order to fetch assets:

1. Users:Read
2. Projects:Read
3. Scan Results (VA): Read

## Supported From Version

Supported from Axonius version 6.1.54.0