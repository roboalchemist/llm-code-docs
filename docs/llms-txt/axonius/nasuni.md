# Source: https://docs.axonius.com/docs/nasuni.md

# Nasuni

Nasuni offers a file services platform built for the cloud that delivers infinite scale, built-in backup, global file sharing, and local file server performance.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Nasuni  Management Console server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1300\).png)

## APIs

Axonius uses the [Nasuni Management Console API v1.1.0](http://docs.api.nasuni.com/nmc/api/1.1.0/#nasuni-management-console-api).

## Required Permissions

Before any calls to NMC API can be made, the 'Enable NMC API Access' permission must be set within the Nasuni Management Console on the group of the user supplied in [User Name](#parameters), see [here](http://docs.api.nasuni.com/nmc/api/1.1.0/#authentication) for more details.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version               | Supported | Notes |
| --------------------- | --------- | ----- |
| Version 8.5 and above | Yes       |       |