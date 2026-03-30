# Source: https://docs.axonius.com/docs/haproxy.md

# HAProxy

HAProxy is free and open source software that provides a high availability load balancer and reverse proxy for TCP and HTTP-based applications.

### Asset Types Fetched

* Devices, Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the [HAProxy Enterprise Data Plane API](https://www.haproxy.com/documentation/dataplaneapi/enterprise/#get-/services/haproxy/configuration/acls).

### Permissions

The value supplied in [User Name](#required-parameters) must have read-only permissions in order to fetch assets.

#### Supported From Version

Supported from Axonius version 4.8

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the HAProxy server.

2. **User Name** and **Password** - The credentials for a user account that has the permissions to fetch assets.

3. **API Version** *(default: Version 2)* - Select the API Version, either Version 2 or Version 3.

![HAProxy](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HAProxy.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version     | Supported | Notes |
| ----------- | --------- | ----- |
| HAProxy 2.6 | Yes       |       |