# Source: https://docs.axonius.com/docs/netiq.md

# NetIQ Advanced Authentication

NetIQ Advanced Authentication provides a centralized authentication framework that adds a strong level of authentication (MFA or 2 Factor).

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the NetIQ Advanced Authentication server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Login Method** *(required, default: Password)* - Defines whether to use a regular password or LDAP password for the login.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image align="center" alt="image.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1519).png" />

## APIs

Axonius uses thr [NetIQ Advanced AuthenticationFramework](https://www.netiq.com/documentation/netiq-advanced-authentication-framework-51/pdfdoc/guides/api-documentation.pdf).

## Required Permissions

The value supplied in [User Name](#parameters) must have Admin permissions to fetch assets.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version      | Supported | Notes |
| ------------ | --------- | ----- |
| NetIQ AA 6.3 | Yes       |       |