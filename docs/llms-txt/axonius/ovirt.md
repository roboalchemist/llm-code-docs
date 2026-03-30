# Source: https://docs.axonius.com/docs/ovirt.md

# oVirt

oVirt is a free, open-source virtualization management platform. It may be used to fetch data from Red Hat Virtualization.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Adapter Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the oVirt server that can communicate via the [Required Ports](https://portal.document360.io/#required-ports).

2. **Port** *(required, default: 9090)* - The port used in the connection.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the Required Permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![oVirt](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/oVirt.png)

## API

Axonius uses [oVirt REST API V4.4](http://ovirt.github.io/ovirt-engine-api-model/4.4/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 9090**

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have permissions to fetch assets.