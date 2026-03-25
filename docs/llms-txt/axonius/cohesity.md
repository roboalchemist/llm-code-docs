# Source: https://docs.axonius.com/docs/cohesity.md

# Cohesity

Cohesity is a cloud data platform that provides a comprehensive range of data management services.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

Select the **Deployment** you want to use to connect, either **Cohesity Cluster** or **Helios**. Each type of deployment requires different connection parameters.

### Cohesity Cluster

![Cohesity - Cohesity Cluster Deployment.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cohesity%20-%20Cohesity%20Cluster%20Deployment.png)

1. **VIP/FQDN of Cohesity cluster** *(required)* - Specify the Cohesity domain.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the access to fetch assets.

3. **Token Domain** *(optional, default: LOCAL)* - Specify the authentication domain to obtain a token for logging in. For a Local user, the domain is always 'LOCAL'. For LDAP/AD users, the domain maps to an LDAP connection string. A user is uniquely identified by a combination of username and domain.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

### Helios

![Cohesity - Helios Deployment.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cohesity%20-%20Helios%20Deployment.png)

1. **Domain** *(required, default: `https://helios.cohesity.com`)* - Specify the Cohesity domain.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. For more information, see [Authorization](https://developer.cohesity.com/apidocs/helios/v1-api/#/http/getting-started/authorization).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## APIs

Axonius uses the [Cohesity REST API](https://developer.cohesity.com/apidocs/660x/#/http/getting-started).

## Required Ports

Axonius must be able to communicate with the value supplied in [Domain](#parameters) via the following ports:

* **TCP port 443/8080**

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Protection Sources Environments to Fetch** *(required, default: kAgent)* - Select from the dropdown which protection source environments to fetch. Each environment fetches different servers that are backed up.
   If the connection is successful but no devices are fetched, go back to this setting and select different environments from the dropdown.
2. **Fetch Protected/Unprotected Objects from Cohesity report** - Select this option to fetch protected/unprotected objects from the Cohesity report export.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                     | Supported | Notes |
| --------------------------- | --------- | ----- |
| Cohesity REST API version 1 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.5