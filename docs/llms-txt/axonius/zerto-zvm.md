# Source: https://docs.axonius.com/docs/zerto-zvm.md

# Zerto ZVM

Zerto ZVM is a data loss protection solution that provides disaster recovery, backup and workload mobility software for virtualized infrastructures and cloud environments. This adapter supports on-prem deployment.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Zerto ZVM server.

2. **Port** *(required, default: 9669)* - The port used for the connection.

3. **Zerto ZVM Deployment** *(required)* - Select the deployment method used for the connection, either Windows or Linux.

4. **User Name/Client ID** and **Password/Client Secret** *(required)* - The credentials for a user account that has the permissions to fetch assets. Fill in User Name and Password for Windows deployment.  For Linux deployment, fill in Client ID and Client Secret. For more information, see [Creating Keycloak Credentials](https://help.zerto.com/bundle/Linux.ZVM.HTML.10.0/page/Creating_Keycloak_Credentials.htm).

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ZertoZVM](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ZertoZVM.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch only protected VMs**  - Select this option to fetch only protected VMs.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Zerto Virtual Replication API](https://help.zerto.com/bundle/API.ZVR.HTML/page/Using_the_APIs.htm#apisintro_91474482_1071346).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:
The default port is 9669. The port configured in Axonius must match the port configured in the ZVM console.

## Required Permissions

The value supplied in [User Name](#parameters) must have Read permission for the List VMs endpoint in order to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version      | Supported | Notes |
| ------------ | --------- | ----- |
| Zerto ZVM v1 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.7