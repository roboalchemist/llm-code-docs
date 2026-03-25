# Source: https://docs.axonius.com/docs/linode.md

# Linode

Linode, acquired by Akamai, is a cloud hosting provider that provides Linux-based virtual machines, cloud infrastructure, and managed services.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.linode.com`)* - The hostname or IP address of the Linode server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Access Token** *(required)* - An access token associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   To create an Access Token, see [Get an Access Token](https://www.linode.com/docs/products/tools/api/get-started/#get-an-access-token).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Linode](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Linode.png)

## APIs

Axonius uses the [Linode API](https://www.linode.com/docs/api/) for the following:

* Devices
  * [Linode Instances](https://www.linode.com/docs/api/linode-instances/#linodes-list)
  * [NodeBalancers](https://www.linode.com/docs/api/nodebalancers/#nodebalancers-list)
* Users -[Account](https://www.linode.com/docs/api/account/#users-list)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [Access Token](#parameters) must be associated with credentials that have Read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 5.0