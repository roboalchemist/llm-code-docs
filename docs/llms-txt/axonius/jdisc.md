# Source: https://docs.axonius.com/docs/jdisc.md

# JDisc Discovery

JDisc Discovery is a network inventory and documentation tool that helps identify and manage IT assets and networks.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the JDisc Discovery server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![JDisc Discovery](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/JDisc%20Discovery.png)

## APIs

Axonius uses the [JDisc Discovery GraphQL API](https://jdisc.com/2021/01/07/jdisc-discovery-graphql-api/).

## Required Permissions

The value supplied in [User Name](#parameters) must have read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.1