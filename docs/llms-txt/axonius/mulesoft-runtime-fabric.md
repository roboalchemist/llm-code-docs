# Source: https://docs.axonius.com/docs/mulesoft-runtime-fabric.md

# Mulesoft Runtime Fabric

Mulesoft Runtime Fabric is a container service that automates the deployment and orchestration of Mule applications and gateways.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Mulesoft Runtime Fabric server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. Refer to [Mulesoft Client ID and Client Secret ](https://docs.mulesoft.com/access-management/organization#client-id-and-client-secret) for information about how to obtain the Client ID and Client Secret.

3. **Organization ID** *(optional)*   - Enter an Organization ID, if you want to use a specific  Organization ID.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="MulesoftRuntimeFabric" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MulesoftRuntimeFabric.png" />

## APIs

Axonius uses the

* Runtime Fabric API
* Access Management API

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [Client ID](#parameters) must be associated with credentials that have read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 5.0