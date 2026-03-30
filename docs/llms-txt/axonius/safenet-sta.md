# Source: https://docs.axonius.com/docs/safenet-sta.md

# SafeNet Trusted Access

SafeNet Trusted Access is a cloud-based access management solution that provides secure access to applications and data.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the SafeNet Trusted Access server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. For more details, see [Get an API key](https://thalesdocs.com/sta/api/index.html#get-an-api-key).

3. **Tenant Code** *(required)* - The unique identifier for a virtual server or account. For more details, see [Tenant code](https://thalesdocs.com/sta/api/index.html#tenant-code).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SafeNet Trusted Access](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SafeNet%20Trusted%20Access.png)

## APIs

Axonius uses the APIs mentioned in [API references](https://thalesdocs.com/sta/api/index.html) as well as the following APIs:

* Users - /api/v1/tenants/`{tenant_code}`/users
* Groups - /api/v1/tenants/`{tenant_code}`/users/`{userId}`/groups
* Applications - /api/v1/tenants/`{tenant_code}`/users/`{userId}`/applications
* Authenticators - /api/v1/tenants/`{tenant_code}`/users/`{userId}`/authenticators

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.30.0