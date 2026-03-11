# Source: https://docs.axonius.com/docs/pingone-openidm.md

# PingOne Advanced Identity Cloud

PingOne Advanced Identity Cloud is a high-performance identity store that provides the necessary encryption to protect enterprise data at rest and encryption.

<Callout icon="📘" theme="info">
  Note

  This page describes how to connect **PingOne Advanced Identity Cloud** deployments. To connect **PingIDM (formerly ForgeRock)** (on-prem platform), see [PingIDM (formerly ForgeRock)](/docs/forgerock).
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the PingOne Advanced Identity Cloud server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **Realm** - Your PingOne Advanced Identity Cloud realm ID.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![PingOne Advanced Identity Cloud](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PingOne%20Advanced%20Identity%20Cloud.png)

## APIs

Axonius uses the following APIs:

* [Authentication through OAuth 2.0 and subject mappings](https://backstage.forgerock.com/docs/idcloud/latest/idm-auth/rsfilter-module.html)
* [Authorization header (HTTP Basic)](https://backstage.forgerock.com/docs/idcloud/latest/am-oauth2/client-auth-header.html)
* Authenticate - /am/json/realms/root/realms/`{realm}`/authenticate
* User - /openidm/managed/`{realm}`\_user

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.30.0